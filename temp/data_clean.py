import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Load the dataset
file_path = './data/taiwan_universities_detailed.csv'
df = pd.read_csv(file_path)

# Clean up the columns by removing extra text and converting to appropriate types
df['QS Ranking'] = df['QS Ranking'].str.extract('(\d+)').astype(float)  # Extract numeric values
df['Status'] = df['Status'].str.replace('Status\n', '')
df['Research Output'] = df['Research Output'].str.replace('Research Output\n', '')
df['Student/Faculty Ratio'] = df['Student/Faculty Ratio'].str.extract('(\d+)').astype(float)
df['International Students'] = df['International Students'].str.extract('(\d+)').astype(float)
df['Total Faculty'] = df['Total Faculty'].str.replace('Total Faculty\n', '').str.replace(',', '').astype(float)

# Check if data is cleaned properly
df.head()
