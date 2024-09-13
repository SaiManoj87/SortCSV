import pandas as pd

# Correct the paths to the CSV files for Windows
path_to_file1 = r'/path/to/your/file1.csv'
path_to_file2 = r'/path/to/your/file2.csv'  # Update this path accordingly

# Load the CSV files from the specified paths
df1 = pd.read_csv(path_to_file1)
df2 = pd.read_csv(path_to_file2)

# Sort both dataframes by the 'id' column
df1_sorted = df1.sort_values(by='id')
df2_sorted = df2.sort_values(by='id')

# Define paths for the output sorted files
output_path_file1 = r'/path/to/your/file1_sorted.csv'
output_path_file2 = r'/path/to/your/file2_sorted.csv'  # Update this path accordingly

# Save the sorted dataframes back to new CSV files at the specified output paths
df1_sorted.to_csv(output_path_file1, index=False)
df2_sorted.to_csv(output_path_file2, index=False)