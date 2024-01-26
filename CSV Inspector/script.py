import csv
import os

# Define global constants
FILE_PATH = 'file.csv' # Replace with the actual path to your CSV file
FILE_EXTENSION = '.csv'

def get_file_info(csv_file):
    file_info = {}

    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Check if there is at least one column in the CSV file
            if not reader.fieldnames:
                raise ValueError("CSV file has no columns.")

            # Initialize file_info dictionary with column names
            for column in reader.fieldnames:
                file_info[column] = {
                    'max_length': 0,
                    'empty_cells': 0,
                }
            
            total_records = 0
            
            for row in reader:
                total_records += 1
                # Iterate through each column and update the variables
                for column in file_info.keys():
                    cell_value = row[column]
                    file_info[column]['max_length'] = max(file_info[column]['max_length'], len(str(cell_value)))

                    # Check for empty cells
                    if not cell_value.strip():
                            file_info[column]['empty_cells'] += 1

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

    return file_info, total_records

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
    
    file_info, total_records = get_file_info(file_path)


    if file_info:
        # Display the results

        print(f'Total Records: {total_records}')

        for column, info in file_info.items():
            print(f'{column.capitalize()} Max Length: {info["max_length"]}')
            print(f'{column.capitalize()} Empty Cells: {info["empty_cells"]}')

if __name__ == "__main__":
    main()
