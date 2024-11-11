import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data from CSV
import os
project_root = os.path.dirname(os.path.abspath(__file__))  # Get the current file's directory
data_path = os.path.join(project_root, 'data', 'ai_universities_full_data.csv')
df = pd.read_csv(data_path)

# Set the style
sns.set_style('darkgrid')
plt.figure(figsize=(12, 8))

# Normalize founded years for color mapping
norm = plt.Normalize(df['Founded Year'].min(), df['Founded Year'].max())

# Create the scatter plot with a gradient color based on the year founded
scatter = plt.scatter(df['Founded Year'], df['AI Rank Latin America'], 
                      c=df['Founded Year'], cmap='viridis',  # Using the viridis colormap
                      alpha=0.8, edgecolor='black', s=100)

# Add title and labels with customization
plt.title('AI Rank of Universities in Latin America by Founded Year', fontsize=16, fontweight='bold', color='navy')
plt.xlabel('Year Founded', fontsize=14, fontweight='bold')
plt.ylabel('AI Rank Latin America', fontsize=14, fontweight='bold')

# Invert y-axis for better visualization (lower rank is better)
plt.gca().invert_yaxis()

# Add color bar to indicate the mapping of color to the year founded
cbar = plt.colorbar(scatter)
cbar.set_label('Year Founded')

# Add grid with reduced opacity for better contrast
plt.grid(True, linestyle='--', alpha=0.6)

# Set the background to make it stand out
plt.gca().set_facecolor('#f0f0f0')

# Save and show the plot
output_path = os.path.join(project_root, 'charts', 'scatter.png')
plt.savefig(output_path, dpi=300)
