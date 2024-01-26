# CSV Inspector

This Python script analyzes a CSV file using the csv module, iterating through rows to gather insights such as the total number of records, lengths, and count of empty cells in each column.

## Requirements

- Python 3.x

## Usage

1. Ensure you have Python installed on your system.

2. Download the script file (`script.py`) to your local machine.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Modify the `FILE_PATH` global constant to specify the path to your CSV file.

   ```python
   FILE_PATH = 'file.csv'
   ```

5. Run the script:

   ```bash
   python script.py
   ```

6. The script will display insights about each column in the following format:

   ```plaintext
   Total Records: X
   Column 1 Max Length: Y
   Column 2 Max Length: Z
   Column 3 Max Length: W
   ...
   Column 1 Empty Cells: A
   Column 2 Empty Cells: B
   Column 3 Empty Cells: C
   ...
   ```
