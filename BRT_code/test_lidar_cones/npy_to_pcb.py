import numpy as np
import open3d as o3d
from pathlib import Path

in_path = Path("lidar_out/npy_out")
out_path = Path("lidar_out/pcd_out")
out_path.mkdir(parents=True, exist_ok=True)

for npy in in_path.glob("*.npy"):
    pts = np.load(npy)          # Nx3 or Nx4
    xyz = pts[:, :3]

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz.astype(np.float64))

    out_file = out_path / (npy.stem + ".pcd")
    o3d.io.write_point_cloud(str(out_file), pcd)  # ASCII by default
    print("Wrote", out_file)
