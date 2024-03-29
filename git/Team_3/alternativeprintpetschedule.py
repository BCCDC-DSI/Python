import pandas as pd

def read_and_print_csv(file_path):
    try:
        # Reading the CSV file
        df = pd.read_csv(file_path)
        print(f"Contents of {file_path}:")
        print(df)
        print("\n")  # Add a newline for better readability between CSVs
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
    except pd.errors.ParserError:
        print(f"Error: The file {file_path} is improperly formatted.")
    except Exception as e:
        print(f"An unexpected error occurred while reading {file_path}: {e}")

def main():
    # File paths
    cat_csv = 'Data/cat.csv'
    dog_csv = 'Data/dog.csv'

    # Reading and printing the contents of the CSV files
    read_and_print_csv(cat_csv)
    read_and_print_csv(dog_csv)

if __name__ == "__main__":
    main()
