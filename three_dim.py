import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Load the data from CSV
df = pd.read_csv('./data/ai_universities_full_data.csv')

# Set the style
sns.set_style('whitegrid')
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Normalize the founded years for color mapping
norm = plt.Normalize(df['Founded Year'].min(), df['Founded Year'].max())

# Create the 3D scatter plot using AI Rank World as the Z-axis
scatter = ax.scatter(df['Founded Year'], 
                     df['AI Rank Latin America'], 
                     df['AI Rank World'],  # Z-axis is now AI Rank World
                     c=norm(df['Founded Year']), cmap='plasma', s=100, alpha=0.8)

# Add title and labels with customization
ax.set_title('3D Scatter Plot of AI Rank (Latin America & World) by Year Founded', fontsize=16, fontweight='bold', color='black')
ax.set_xlabel('Year Founded', fontsize=14, fontweight='bold', color='black')
ax.set_ylabel('AI Rank Latin America', fontsize=14, fontweight='bold', color='black')
ax.set_zlabel('AI Rank World', fontsize=14, fontweight='bold', color='black')

# Add color bar to indicate mapping of color to year founded
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Year Founded')

# Set the background color to make it stand out
ax.set_facecolor('white')
plt.savefig('./img/three_dimensional.png')
# Show the plot
plt.show()
