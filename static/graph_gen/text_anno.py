import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV
import os
project_root = os.path.dirname(os.path.abspath(__file__))  # Get the current file's directory
data_path = os.path.join(project_root, 'data', 'ai_universities_full_data.csv')
df = pd.read_csv(data_path)

# Set the style
sns.set_style('whitegrid')
plt.figure(figsize=(12, 8))

# Create the scatter plot with a vibrant color
plt.scatter(df['Founded Year'], df['AI Rank Latin America'], 
            color='#e63946', alpha=0.8, edgecolor='black', s=100)

# Add title and labels with customization
plt.title('AI Rank of Universities in Latin America by Founded Year', fontsize=16, fontweight='bold', color='black')
plt.xlabel('Year Founded', fontsize=14, fontweight='bold', color='black')
plt.ylabel('AI Rank Latin America', fontsize=14, fontweight='bold', color='black')

# Invert y-axis for better visualization (lower rank is better)
plt.gca().invert_yaxis()

# Annotate the top 3 universities by AI Rank Latin America
top_3 = df.nsmallest(3, 'AI Rank Latin America')
for i, row in top_3.iterrows():
    plt.annotate(f"Top: {row['University']}", 
                 (row['Founded Year'], row['AI Rank Latin America']),
                 textcoords="offset points", xytext=(-5,5), ha='right', fontsize=10, color='black', 
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='#ffcb69', alpha=0.8))

# Annotate the most bottom university by AI Rank Latin America
most_bottom = df.nlargest(1, 'AI Rank Latin America')
for i, row in most_bottom.iterrows():
    plt.annotate(f"Lowest: {row['University']}", 
                 (row['Founded Year'], row['AI Rank Latin America']),
                 textcoords="offset points", xytext=(-5,5), ha='right', fontsize=10, color='black', 
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='#f1fa3c', alpha=0.8))

# Annotate the oldest university
oldest_university = df.loc[df['Founded Year'].idxmin()]
plt.annotate(f"Oldest: {oldest_university['University']}", 
             (oldest_university['Founded Year'], oldest_university['AI Rank Latin America']),
             textcoords="offset points", xytext=(-5,5), ha='left', fontsize=10, color='black', 
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='#a8dadc', alpha=0.8))

# Annotate the youngest university
youngest_university = df.loc[df['Founded Year'].idxmax()]
plt.annotate(f"Youngest: {youngest_university['University']}", 
             (youngest_university['Founded Year'], youngest_university['AI Rank Latin America']),
             textcoords="offset points", xytext=(-5,5), ha='right', fontsize=10, color='black', 
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='#98c1d9', alpha=0.8))

# Add grid with reduced opacity for better contrast
plt.grid(True, linestyle='--', alpha=0.6)

# Set the background to make it stand out
plt.gca().set_facecolor('white')

# Save and show the plot
output_path = os.path.join(project_root, 'charts', 'text_annotation.png')
plt.savefig(output_path, dpi=300)
