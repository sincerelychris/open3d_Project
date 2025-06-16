import numpy as np
import open3d as o3d
import trimesh
import pyvista as pv

# Example of creating a point cloud from your scanner data
# Assuming your scanner data is in points_xyz format
points_xyz = np.random.rand(1000, 3)  # Replace with your actual scanner data

# Using Open3D
# Create point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points_xyz)

# Estimate normals
pcd.estimate_normals()

# Create mesh using Poisson surface reconstruction
mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd)

# Visualize
o3d.visualization.draw_geometries([mesh])

# Alternative using Trimesh and PyVista
# Convert to trimesh
tmesh = trimesh.Trimesh(vertices=points_xyz, process=True)

# Make watertight if needed
tmesh.fill_holes()

# Visualize with PyVista
plotter = pv.Plotter()
plotter.add_mesh(pv.wrap(tmesh))
plotter.show()


