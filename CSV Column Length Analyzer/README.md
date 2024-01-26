# CSV Column Length Analyzer

This simple Python script analyzes a CSV file and determines the maximum length of each column. The script uses the `csv` module to read the CSV file and iterates through each row to find the maximum length for each column.

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

6. The script will print the maximum length of each column in the following format:

   ```plaintext
   Column 1 Max Length: X
   Column 2 Max Length: Y
   Column 3 Max Length: Z
   ...
   ```
