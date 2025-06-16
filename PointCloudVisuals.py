
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
data = pd.read_csv('Uploads/RawdataPoints/PyTorch/3D Scan_0.csv', header=None).values[0]

# 2. Create x-axis points (measurement positions)
x_points = np.arange(len(data))

# 3. Create a simple 2D plot
plt.figure(figsize=(15, 6))
plt.plot(x_points, data, 'b-', linewidth=1)
plt.grid(True)
plt.title('Line Scanner Profile')
plt.xlabel('Measurement Point')
plt.ylabel('Distance (mm)')

# 4. Add some basic statistics
plt.axhline(y=np.mean(data), color='r', linestyle='--', label='Mean')
plt.legend()

# Show the plot
plt.show()

# Print some basic statistics
print(f"Number of points: {len(data)}")
print(f"Min value: {np.min(data):.2f} mm")
print(f"Max value: {np.max(data):.2f} mm")
print(f"Range: {np.max(data) - np.min(data):.2f} mm")