import sys
import numpy as np
import open3d as o3d

path = sys.argv[1] if len(sys.argv) > 1 else "lidar_out/lidar_000000.npy"
pts = np.load(path)  # Nx4

xyz = pts[:, :3]
intensity = pts[:, 3]

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz.astype(np.float64))

# color by intensity (normalized grayscale)
i = intensity.astype(np.float64)
i = (i - i.min()) / (i.max() - i.min() + 1e-9)
colors = np.stack([i, i, i], axis=1)
pcd.colors = o3d.utility.Vector3dVector(colors)

o3d.visualization.draw_geometries([pcd])
