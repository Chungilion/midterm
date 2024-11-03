import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data from CSV
df = pd.read_csv('./data/ai_universities_full_data.csv')

# Set the style
sns.set_style('darkgrid')
plt.figure(figsize=(12, 8))

# Calculate counts for each bin
hist_data, bin_edges = np.histogram(df['AI Rank Latin America'], bins=20)

# Normalize counts for color scaling
norm = plt.Normalize(hist_data.min(), hist_data.max())

# Create the histogram with a subtle transition in color
for count, edge in zip(hist_data, bin_edges[:-1]):
    # Define a color that transitions subtly from a light blue to dark blue
    color = plt.cm.Blues(norm(count) * 0.8 + 0.2)  # Adjusting for a softer transition
    plt.bar(edge, count, width=np.diff(bin_edges), 
            color=color, 
            edgecolor='black')  # Edge color for better definition

# Add title and labels with customization
plt.title('Distribution of AI Rank in Latin America', fontsize=16, fontweight='bold', color='navy')
plt.xlabel('AI Rank Latin America', fontsize=14, fontweight='bold')
plt.ylabel('Number of Universities', fontsize=14, fontweight='bold')

# Add grid with reduced opacity for better contrast
plt.grid(True, linestyle='--', alpha=0.6)

# Set the background to make it stand out
plt.gca().set_facecolor('#f0f0f0')

# Save and show the plot
plt.savefig('img/histogram.png')
plt.show()
