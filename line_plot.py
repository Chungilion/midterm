import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV
df = pd.read_csv('./data/ai_universities_full_data.csv')

# Set the style
sns.set_style('darkgrid')
plt.figure(figsize=(12, 8))

# Plotting the AI Rank Latin America against the Founded Year
plt.plot(df['AI Rank Latin America'], df['Founded Year'], marker='o', color='#4e79a7', alpha=0.8)

# Add title and labels with customization
plt.title('Year Founded of Universities by AI Rank in Latin America', fontsize=16, fontweight='bold', color='navy')
plt.xlabel('AI Rank Latin America', fontsize=14, fontweight='bold')
plt.ylabel('Year Founded', fontsize=14, fontweight='bold')

# Add grid with reduced opacity for better contrast
plt.grid(True, linestyle='--', alpha=0.6)

# Set the background to make it stand out
plt.gca().set_facecolor('#f0f0f0')

# Save and show the plot
plt.savefig('img/lineplot.png')
plt.show()
