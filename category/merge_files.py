import pandas as pd
import glob
import os

def merge_csv_files(input_folder, output_file):
    """
    Merges all CSV files in a folder into a single CSV file.

    Args:
        input_folder (str): The path to the folder containing the CSV files.
        output_file (str): The path to the output CSV file.
    """

    all_files = glob.glob(os.path.join(input_folder, "*.csv"))

    if not all_files:
        print(f"No CSV files found in {input_folder}")
        return

    li = []

    for filename in all_files:
        try:
            df = pd.read_csv(filename)
            li.append(df)
        except pd.errors.EmptyDataError:
            print(f"Warning: {filename} is empty and will be skipped.")
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        except Exception as e:
            print(f"An unexpected error occurred while reading {filename}: {e}")

    if li:  # Only proceed if there are dataframes to concatenate
        try:
            frame = pd.concat(li, axis=0, ignore_index=True)
            frame.to_csv(output_file, index=False)
            print(f"Successfully merged {len(all_files)} CSV files into {output_file}")
        except Exception as e:
            print(f"An error occurred during concatenation or saving: {e}")

# Example usage:
input_folder = "output_results"  # Replace with your input folder
output_file = "merged_output.csv"  # Replace with your desired output file name

merge_csv_files(input_folder, output_file)