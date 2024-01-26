import csv
import os

# Define global constants
FILE_PATH = 'file.csv' # Replace with the actual path to your CSV file
FILE_EXTENSION = '.csv'

def get_max_lengths(csv_file):
    max_lengths = {}

    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Check if there is at least one column in the CSV file
            if not reader.fieldnames:
                raise ValueError("CSV file has no columns.")

            # Initialize max_lengths dictionary with column names
            for column in reader.fieldnames:
                max_lengths[column] = 0
            
            for row in reader:
                # Iterate through each column and update the max length if needed
                for column in max_lengths.keys():
                    max_lengths[column] = max(max_lengths[column], len(row[column]))

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

    return max_lengths

def main():
    file_path = FILE_PATH

    # Check if the file has a .csv extension
    # if not file_path.lower().endswith(FILE_EXTENSION):
    #     raise ValueError("Invalid file type. Please provide a CSV file.")

    # Alternatively

    # file_extension = os.path.splitext(file_path)[1]
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() != FILE_EXTENSION:
        raise ValueError("Invalid file type. Please provide a CSV file.")
    
    max_lengths = get_max_lengths(file_path)

    if max_lengths:
        # Display the results
        for column, length in max_lengths.items():
            print(f'{column.capitalize()} Max Length: {length}')

if __name__ == "__main__":
    main()
