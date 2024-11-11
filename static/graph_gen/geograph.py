#Please don't run this before checking out the img folder sir
#I couldn't find the latitude or longtitude so I improvised
#THe words are still overlapping each other so I have to zoom them in and save it as the image in ./img

import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd

# Load the adjusted data from the modified CSV file
import os
project_root = os.path.dirname(os.path.abspath(__file__))  # Get the current file's directory
data_path = os.path.join(project_root, 'data', 'data_for_geograph.csv')
df = pd.read_csv(data_path)

# Create a GeoDataFrame using the latitude and longitude columns from the CSV file
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['Longitude'], df['Latitude']))

# Load the Natural Earth dataset (make sure you have the path to the .shp file)
project_root = os.path.dirname(os.path.abspath(__file__))  # Get the current file's directory
shapefile_path = os.path.join(project_root, 'data', '110m_cultural', 'ne_110m_admin_0_countries.shp')

# Load the shapefile
world = gpd.read_file(shapefile_path)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
world.plot(ax=ax, color='#a3d977', edgecolor='#8d99ae')  # Green for land and gray for borders

# Plotting the universities with a contrasting color
gdf.plot(ax=ax, color='#e63946', markersize=30, alpha=0.8, edgecolor='black')  # Red markers with black edges

# Annotating the universities with adjusted positions
for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf['University']):
    plt.text(x, y, label, fontsize=7, ha='right', color='black', weight='bold', backgroundcolor='white',
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='white', alpha=0.7))

# Set limits to focus on Latin America
ax.set_xlim(-100, -30)  # Longitude range to focus on Latin America
ax.set_ylim(-60, 15)    # Latitude range to focus on Latin America

# Set a natural ocean color for the background
ax.set_facecolor('#92c5de')  # Light blue for the ocean

plt.title('Geographical Distribution of AI Universities in Latin America', fontsize=16, fontweight='bold')
plt.xlabel('Longitude', fontsize=12)
plt.ylabel('Latitude', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# Save and show the plot
output_path = os.path.join(project_root, 'charts', 'geograph.png')
plt.savefig(output_path, dpi=300)