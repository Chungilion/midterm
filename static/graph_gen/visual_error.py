import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Load the data from CSV
import os
project_root = os.path.dirname(os.path.abspath(__file__))  # Get the current file's directory
data_path = os.path.join(project_root, 'data', 'ai_universities_full_data.csv')
df = pd.read_csv(data_path)

# Fit a polynomial regression model for a smooth curve
X = df[['Founded Year']]
y = df['AI Rank Latin America']
poly = PolynomialFeatures(degree=3)  # Using a polynomial of degree 3 for a better fit
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)

# Predict the values
predictions = model.predict(X_poly)

# Calculate 95% confidence interval (assuming normal distribution of errors)
# Here, we use a simple standard deviation approach; for more accuracy, use bootstrapping or statistical methods
std_dev = np.std(y - predictions)
ci = 1.96 * std_dev  # 1.96 for 95% confidence interval

# Set the style
sns.set_style('whitegrid')
plt.figure(figsize=(12, 8))

# Sort the values for a smooth continuous plot
sorted_indices = X['Founded Year'].argsort()
sorted_years = X['Founded Year'].values[sorted_indices]
sorted_predictions = predictions[sorted_indices]

# Plot the predictions line
plt.plot(sorted_years, sorted_predictions, color='black', label='Predicted AI Rank')

# Add a shaded confidence band around the predictions (±95% confidence interval)
plt.fill_between(sorted_years, sorted_predictions - ci, sorted_predictions + ci, 
                 color='lightblue', alpha=0.5, label='95% Confidence Interval')

# Overlay actual data points for reference
plt.scatter(X['Founded Year'], y, color='red', edgecolor='black', s=50, zorder=3, label='Observed Data')

# Add title and labels with customization
plt.title('AI Rank Predictions with 95% Confidence Interval', fontsize=16, fontweight='bold', color='black')
plt.xlabel('Year Founded', fontsize=14, fontweight='bold', color='black')
plt.ylabel('AI Rank Latin America', fontsize=14, fontweight='bold', color='black')

# Add legend
plt.legend()

# Add grid with reduced opacity for better contrast
plt.grid(True, linestyle='--', alpha=0.6)

# Set the background to make it stand out
plt.gca().set_facecolor('white')

# Save and show the plot
output_path = os.path.join(project_root, 'charts', 'visual_error.png')
plt.savefig(output_path, dpi=300)
