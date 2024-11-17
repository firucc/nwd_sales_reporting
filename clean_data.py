import pandas as pd
import os

def clean_sales_data(input_file, output_file):
    """
    Cleans the sales data CSV file.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the cleaned CSV file.
    """
    try:
        # Load the dataset
        print(f"Loading data from {input_file}...")
        df = pd.read_csv(input_file)

        # Show initial data summary
        print("Initial data preview:")
        print(df.head())

        # Remove duplicates
        print("Removing duplicate rows...")
        df = df.drop_duplicates()

        # Handle missing values
        print("Filling missing values in 'Revenue' column with 0...")
        df['Revenue'] = df['Revenue'].fillna(0)

        # Standardize column names
        print("Standardizing column names...")
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

        # Filter invalid data (e.g., negative revenues)
        print("Filtering invalid data...")
        df = df[df['revenue'] >= 0]

        # Save the cleaned dataset
        print(f"Saving cleaned data to {output_file}...")
        df.to_csv(output_file, index=False)

        print("Data cleaning completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Define input and output file paths
    input_path = "nwd_product_sales.csv"
    output_path = "cleaned_sales_data.csv"

    # Clean the dataset
    clean_sales_data(input_path, output_path)