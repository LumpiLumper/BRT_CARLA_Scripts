import carla
import time
import json
import numpy as np
from pathlib import Path

HOST, PORT = "127.0.0.1", 2000
OUT = Path("lidar_out")
OUT.mkdir(exist_ok=True)

def find_cone_blueprint(bp_lib):
    # Prefer a cone if present; otherwise fall back to something small-ish.
    for b in bp_lib.filter("static.prop.*"):
        if "cone" in b.id.lower():
            return b
    # fallback
    for cand in ["static.prop.streetbarrier", "static.prop.trafficwarning", "static.prop.bin"]:
        try:
            return bp_lib.find(cand)
        except Exception:
            pass
    return bp_lib.filter("static.prop.*")[0]

def main():
    client = carla.Client(HOST, PORT)
    client.set_timeout(120.0)

    world = client.get_world()
    bp = world.get_blueprint_library()

    # Make sim deterministic-ish
    settings = world.get_settings()
    settings.synchronous_mode = True
    settings.fixed_delta_seconds = 0.05
    world.apply_settings(settings)

    traffic_manager = client.get_trafficmanager()
    traffic_manager.set_synchronous_mode(True)

    actors = []

    try:
        # Load a map (optional). Keeping current map is fine too.
        # world = client.load_world("Town03")

        # Spawn vehicle
        vehicle_bp = bp.filter("vehicle.*model3*")
        vehicle_bp = vehicle_bp[0] if vehicle_bp else bp.filter("vehicle.*")[0]
        spawn = world.get_map().get_spawn_points()[0]
        vehicle = world.spawn_actor(vehicle_bp, spawn)
        actors.append(vehicle)

        # Spawn cones
        cone_bp = find_cone_blueprint(bp)
        print("Using prop blueprint:", cone_bp.id)

        cones = []
        base = spawn.location
        z = base.z
        for i in range(5):
            for j in range(4):
                x = base.x + 12 + i * 4
                y = base.y + (j - 1.5) * 2.0
                tf = carla.Transform(carla.Location(x=x, y=y, z=z))
                c = world.spawn_actor(cone_bp, tf)
                cones.append(c)
                actors.append(c)

        # LiDAR
        lidar_bp = bp.find("sensor.lidar.ray_cast")
        lidar_bp.set_attribute("range", "50")
        lidar_bp.set_attribute("channels", "32")
        lidar_bp.set_attribute("points_per_second", "32000")  # lighter for CPU
        lidar_bp.set_attribute("rotation_frequency", "10")
        lidar_bp.set_attribute("upper_fov", "10")
        lidar_bp.set_attribute("lower_fov", "-30")

        lidar_tf = carla.Transform(carla.Location(x=0.0, y=0.0, z=2.2))
        lidar = world.spawn_actor(lidar_bp, lidar_tf, attach_to=vehicle)
        actors.append(lidar)

        frame_buf = {}

        def on_lidar(meas: carla.LidarMeasurement):
            pts = np.frombuffer(meas.raw_data, dtype=np.float32).reshape(-1, 4)
            frame_buf[meas.frame] = pts

        lidar.listen(on_lidar)

        # Warm-up
        for _ in range(20):
            world.tick()

        N = 50
        for _ in range(N):
            frame = world.tick()

            # Wait for matching LiDAR frame
            t0 = time.time()
            while frame not in frame_buf and time.time() - t0 < 5.0:
                time.sleep(0.001)

            pts = frame_buf.pop(frame, None)
            if pts is None:
                print("Missed LiDAR for frame", frame)
                continue

            np.save(OUT / f"lidar_{frame:06d}.npy", pts)

            labels = []
            for c in cones:
                bb = c.bounding_box
                # bb.location is relative to actor; transform to world
                center_w = c.get_transform().transform(bb.location)
                labels.append({
                    "actor_id": c.id,
                    "type_id": c.type_id,
                    "center_world": [center_w.x, center_w.y, center_w.z],
                    "extent": [bb.extent.x, bb.extent.y, bb.extent.z],
                    "rotation_world": [
                        c.get_transform().rotation.pitch,
                        c.get_transform().rotation.yaw,
                        c.get_transform().rotation.roll,
                    ],
                })

            (OUT / f"labels_{frame:06d}.json").write_text(json.dumps(labels, indent=2))

            if frame % 10 == 0:
                print("Saved frame", frame, "points", pts.shape[0])

        print("Done. Wrote to:", OUT.resolve())

    finally:
        # Cleanup
        for a in actors[::-1]:
            try:
                if hasattr(a, "stop"):
                    a.stop()
                a.destroy()
            except Exception:
                pass

        s = world.get_settings()
        s.synchronous_mode = False
        world.apply_settings(s)
        traffic_manager.set_synchronous_mode(False)

if __name__ == "__main__":
    main()
