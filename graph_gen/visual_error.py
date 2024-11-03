import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the data from CSV
df = pd.read_csv('./data/ai_universities_full_data.csv')

# Fit a simple linear regression model
X = df[['Founded Year']]
y = df['AI Rank Latin America']
model = LinearRegression()
model.fit(X, y)

# Predict the values
predictions = model.predict(X)

# Calculate residuals
residuals = y - predictions

# Set the style
sns.set_style('whitegrid')
plt.figure(figsize=(12, 8))

# Create the residual plot in black and white
plt.scatter(predictions, residuals, color='black', alpha=0.8, edgecolor='white', s=100)
plt.axhline(0, color='black', linestyle='--')  # Line at y=0

# Add title and labels with customization
plt.title('Residual Plot for AI Rank Predictions', fontsize=16, fontweight='bold', color='black')
plt.xlabel('Predicted AI Rank', fontsize=14, fontweight='bold', color='black')
plt.ylabel('Residuals', fontsize=14, fontweight='bold', color='black')

# Add grid with reduced opacity for better contrast
plt.grid(True, linestyle='--', alpha=0.6)

# Set the background to make it stand out
plt.gca().set_facecolor('white')

# Save and show the plot
plt.savefig('img/visual_error.png', dpi=300)  # Save as high resolution
plt.show()
