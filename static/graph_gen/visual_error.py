import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import os

# Load the data from CSV
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

# Calculate residuals (errors between the observed and predicted values)
residuals = y - predictions

# Estimate standard error of predictions (standard deviation of residuals)
std_dev = np.std(residuals)

# Calculate 95% confidence intervals for the predictions
ci_upper = predictions + 1.96 * std_dev  # Upper bound of 95% CI
ci_lower = predictions - 1.96 * std_dev  # Lower bound of 95% CI

# Set the style for Seaborn
sns.set_style('whitegrid')

# Create the plot
plt.figure(figsize=(12, 8))

# Sort the values for smooth continuous plot
sorted_indices = X['Founded Year'].argsort()
sorted_years = X['Founded Year'].values[sorted_indices]
sorted_predictions = predictions[sorted_indices]
sorted_ci_lower = ci_lower[sorted_indices]
sorted_ci_upper = ci_upper[sorted_indices]

# Scatter plot of observed data with error bars
plt.errorbar(X['Founded Year'], y, yerr=std_dev, fmt='o', color='red', 
             ecolor='gray', elinewidth=2, capsize=3, label='Observed Data with Error Bars')

# Plot the predictions line
plt.plot(sorted_years, sorted_predictions, color='black', label='Predicted AI Rank')

# Add a shaded confidence band around the predictions (±95% confidence interval)
plt.fill_between(sorted_years, sorted_ci_lower, sorted_ci_upper, color='lightblue', alpha=0.5, 
                 label='95% Confidence Interval')

# Add title and labels
plt.title('AI Rank Predictions with Error Bars', fontsize=16, fontweight='bold', color='black')
plt.xlabel('Year Founded', fontsize=14, fontweight='bold', color='black')
plt.ylabel('AI Rank Latin America', fontsize=14, fontweight='bold', color='black')

# Add legend
plt.legend()

# Show grid
plt.grid(True, linestyle='--', alpha=0.6)

# Set the background to white
plt.gca().set_facecolor('white')

# Save and show the plot
output_path = os.path.join(project_root, 'charts', 'visual_error.png')
plt.savefig(output_path, dpi=300)
