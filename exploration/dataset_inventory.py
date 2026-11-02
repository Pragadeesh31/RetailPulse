import csv
from pathlib import Path

DATA_PATH = Path("RetailPulse/data/raw") # Define the path to the directory containing the CSV files


def inspect_csv(file_path):
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file: # Open the CSV file with UTF-8 encoding and handle potential BOM

        reader = csv.DictReader(file) # Create a CSV reader object that maps the information in each row to a dictionary
        columns = reader.fieldnames # Get the column names from the CSV file
        row_count = sum(1 for _ in reader) # Count the number of rows in the CSV file by iterating through the reader object

    file_size = file_path.stat().st_size / (1024 * 1024) # Get the file size in bytes and convert it to megabytes

    print("\n-------------------------")
    print(f"File: {file_path.name}")
    print(f"Rows: {row_count}")
    print(f"Columns: {len(columns)}")
    print(f"Size: {file_size:.2f} MB")
    print(f"Column Names: {columns}")


def main():
    csv_files = list(DATA_PATH.glob("*.csv")) # Get all CSV files in the specified directory

    if not csv_files:
        print("No CSV files found!")
        return

    print(f"Total CSV files: {len(csv_files)}")

    for file in sorted(csv_files):
        inspect_csv(file)


if __name__ == "__main__": # Check if the script is being run directly (not imported as a module)
    main()
