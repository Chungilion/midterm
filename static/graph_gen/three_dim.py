import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata


# Load the data from CSV
import os
project_root = os.path.dirname(os.path.abspath(__file__))  # Get the current file's directory
data_path = os.path.join(project_root, 'data', 'ai_universities_full_data.csv')
df = pd.read_csv(data_path)

# Extract relevant columns for 3D plotting
x = df['Founded Year']
y = df['AI Rank Latin America']
z = df['AI Rank World']

# Generate grid data for surface plot interpolation
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
X, Y = np.meshgrid(xi, yi)
Z = griddata((x, y), z, (X, Y), method='cubic')

# Set up the figure and 3D axes
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot a surface with interpolated data
surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.6)

# Overlay a wireframe to highlight grid lines
wire = ax.plot_wireframe(X, Y, Z, color='gray', linewidth=0.5, alpha=0.3)

# Add individual data points for contrast
scatter = ax.scatter(x, y, z, color='red', s=50, label='University Data Points')

# Set labels and title
ax.set_title('3D Plot of AI Rank by University Founded Year', fontsize=16, fontweight='bold')
ax.set_xlabel('Founded Year', fontsize=14)
ax.set_ylabel('AI Rank Latin America', fontsize=14)
ax.set_zlabel('AI Rank World', fontsize=14)

# Add a color bar for the surface plot
cbar = fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)
cbar.set_label('AI Rank World')

# Adjust viewing angle to match the reference image
ax.view_init(elev=20, azim=225)

# Add legend
ax.legend(loc='upper left')

# Save and display the plot
output_path = os.path.join(project_root, 'charts', 'three_dimensional.png')
plt.savefig(output_path, dpi=300)
