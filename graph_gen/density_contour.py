import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data from CSV
df = pd.read_csv('./data/ai_universities_full_data.csv')

# Set the style
sns.set_style('whitegrid')
plt.figure(figsize=(12, 8))

# Create a density contour plot with a vibrant color palette
sns.kdeplot(x=df['Founded Year'], y=df['AI Rank Latin America'], 
            cmap='plasma', fill=True, thresh=0, levels=20, alpha=0.8)

# Add title and labels with customization
plt.title('Density Contour Plot of AI Rank by Year Founded', fontsize=16, fontweight='bold', color='black')
plt.xlabel('Year Founded', fontsize=14, fontweight='bold', color='black')
plt.ylabel('AI Rank Latin America', fontsize=14, fontweight='bold', color='black')

# Invert y-axis for better visualization (lower rank is better)
plt.gca().invert_yaxis()

# Add grid with reduced opacity for better contrast
plt.grid(True, linestyle='--', alpha=0.6)

# Set the background to make it stand out
plt.gca().set_facecolor('white')

# Save and show the plot
plt.savefig('img/density_contour.png', dpi=300)  # Save as high resolution
plt.show()
