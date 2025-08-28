import pandas as pd
import numpy as np

# 1. Create a more comprehensive sample dataset to simulate a real-world scenario.
#    In a real application, you would replace this with a data loading function
#    like: `df = pd.read_csv('your_dataset.csv')`
data = {
    'region': ['Europe', 'North America', 'Asia', 'Latin America', 'Oceania', 'North America', 'Europe', 'Asia', 'Europe', None, 'Latin America', 'Oceania', 'North America', 'Europe', 'Asia', 'Latin America', 'Oceania', 'Europe', 'Asia', 'North America', None],
    'customer_id': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008', 'C009', 'C010', 'C011', 'C012', 'C013', 'C014', 'C015', 'C016', 'C017', 'C018', 'C019', 'C020', 'C021'],
    'pre_order_date': ['2024-07-02', '2024-07-03', '2024-07-04', '2024-07-05', '2024-07-06', '2024-07-07', '2024-07-08', '2024-07-09', '2024-07-10', '2024-07-11', '2024-07-12', '2024-07-13', '2024-07-14', '2024-07-15', '2024-07-16', '2024-07-17', '2024-07-18', '2024-07-19', '2024-07-20', '2024-07-21', '2024-07-22'],
    'demographic_group': ['Casual', 'Gamer', 'Tech Enthusiast', 'Family', 'Student', 'Gamer', 'Casual', 'Family', 'Student', 'Gamer', 'Tech Enthusiast', 'Casual', 'Gamer', None, 'Family', 'Student', 'Tech Enthusiast', 'Casual', 'Gamer', 'Family', 'Student'],
    'pre_order_quantity': [2, 1, 1, 3, 2, 5, 2, 4, 1, 2, 3, 5, 1, np.nan, 4, 2, 2, 1, 3, 1, np.nan]
}
df = pd.DataFrame(data)

# Print the original DataFrame to show the missing values
print("Original DataFrame with missing values:")
print(df)
print("-" * 50)

# 2. Calculate the percentage of records with missing values
#    The `any(axis=1)` method checks for missing values in any column for each row.
total_rows = len(df)
rows_with_missing_values = df.isnull().any(axis=1).sum()
percentage_with_missing = (rows_with_missing_values / total_rows) * 100

print(f"Total number of records: {total_rows}")
print(f"Number of records with at least one missing value: {rows_with_missing_values}")
print(f"Percentage of records with missing values: {percentage_with_missing:.2f}%")
print("-" * 50)

# 3. Handle the missing values using a dynamic approach
#    This method is more robust as it automatically handles missing values
#    based on the data type of each column.

# Make a copy to avoid modifying the original DataFrame
cleaned_df_filled = df.copy()

# Identify categorical and numerical columns
categorical_cols = cleaned_df_filled.select_dtypes(include=['object', 'category']).columns
numerical_cols = cleaned_df_filled.select_dtypes(include=np.number).columns

# Fill missing values in categorical columns with the mode (most frequent value)
for col in categorical_cols:
    if cleaned_df_filled[col].isnull().any():
        mode_val = cleaned_df_filled[col].mode()[0]
        cleaned_df_filled[col].fillna(mode_val, inplace=True)

# Fill missing values in numerical columns with the mean
for col in numerical_cols:
    if cleaned_df_filled[col].isnull().any():
        mean_val = cleaned_df_filled[col].mean()
        cleaned_df_filled[col].fillna(mean_val, inplace=True)


# Print the cleaned DataFrame after filling values
print("Cleaned DataFrame (after filling missing values dynamically):")
print(cleaned_df_filled)
print("-" * 50)

# REWRITING TASK 2
# 4. Calculate total pre-sale orders per month, region, and demographic group
#    First, ensure the 'pre_order_date' column is in datetime format.
cleaned_df_filled['pre_order_date'] = pd.to_datetime(cleaned_df_filled['pre_order_date'])

#    Extract the month and year into a new column for grouping.
cleaned_df_filled['order_month'] = cleaned_df_filled['pre_order_date'].dt.to_period('M')

#    Group by the new 'order_month' column, 'region', and 'demographic_group', and sum the quantities.
monthly_orders = cleaned_df_filled.groupby(['order_month', 'region', 'demographic_group'])['pre_order_quantity'].sum().reset_index()

# Print the resulting aggregated DataFrame
print("Total pre-sale orders per month, region, and demographic group:")
print(monthly_orders)
print("-" * 50)






















