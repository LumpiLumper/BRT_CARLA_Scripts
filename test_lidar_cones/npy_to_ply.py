import numpy as np
from pathlib import Path

in_path = Path("lidar_out/npy_out")
out_path = Path("lidar_out/ply_out")

out_path.mkdir(parents=True, exist_ok=True)

for file in in_path.glob("*.npy"):
    pts = np.load(file)          # Nx4  
    xyz = pts[:, :3]
    inten = pts[:, 3]

    out_file = out_path / (file.stem + ".ply")

    with open(out_file, "w") as f:
        f.write("ply\nformat ascii 1.0\n")
        f.write(f"element vertex {xyz.shape[0]}\n")
        f.write("property float x\nproperty float y\nproperty float z\n")
        f.write("property float intensity\n")
        f.write("end_header\n")
        for (x, y, z), it in zip(xyz, inten):
            f.write(f"{x} {y} {z} {it}\n")

print("Wrote", out_path)