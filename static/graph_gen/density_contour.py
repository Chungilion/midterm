import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data from CSV
try:
    import os
    project_root = os.path.dirname(os.path.abspath(__file__))  # Get the current file's directory
    data_path = os.path.join(project_root, 'data', 'ai_universities_full_data.csv')
    df = pd.read_csv(data_path)
    print("Data loaded successfully")
except FileNotFoundError:
    print("CSV file not found. Please check the file path.")
    raise

# Check if required columns exist
if 'Founded Year' not in df.columns or 'AI Rank Latin America' not in df.columns:
    print("Required columns are missing in the data.")
    raise ValueError("The columns 'Founded Year' and/or 'AI Rank Latin America' are missing.")
else:
    print("Columns found: 'Founded Year' and 'AI Rank Latin America'")
    print("Sample data:\n", df[['Founded Year', 'AI Rank Latin America']].head())

# Ensure there is data in the columns
if df['Founded Year'].isnull().all() or df['AI Rank Latin America'].isnull().all():
    print("Data is missing in the specified columns.")
    raise ValueError("Columns 'Founded Year' and/or 'AI Rank Latin America' have no data.")

# Set the style
sns.set_style('whitegrid')
plt.figure(figsize=(12, 8))

# Create a density contour plot with adjustments for low data density
try:
    contour = sns.kdeplot(x=df['Founded Year'], y=df['AI Rank Latin America'], 
                          cmap='plasma', fill=True, levels=10, alpha=0.8)
    print("Contour plot created successfully.")
except Exception as e:
    print("Error in creating contour plot:", e)
    raise

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

# Add color bar for the density levels
if contour.get_children():
    mappable = contour.get_children()[0]
    plt.colorbar(mappable, label='Density Level')

# Save the plot as a high-resolution image in an existing folder
output_path = os.path.join(project_root, 'charts', 'density_contour.png')
plt.savefig(output_path, dpi=300)
