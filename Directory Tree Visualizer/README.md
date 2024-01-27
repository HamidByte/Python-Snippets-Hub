# Directory Tree Visualizer (dirtree.py)

dirtree.py is a Python utility toolkit designed for effective directory navigation and visualization. It offers various functions to suit different visualization needs, allowing users to explore and understand project hierarchies. Whether you need a simple tree view or a beautified structure, dirtree.py has you covered.

## Main Features

- **Simple Tree:** Display a simple tree view of the directory.
- **Absolute Path Tree (Platform-Independent):** Display the absolute path tree using forward slashes or backward slashes, automatically adjusting to the underlying operating system.
- **Relative Path Tree (Platform-Independent):** Display the relative path tree using forward slashes or backward slashes, automatically adjusting to the underlying operating system.
- **Absolute Path Tree (User-Defined Style):** Display the absolute path tree with a user-defined path style (Unix or Windows).
- **Relative Path Tree (User-Defined Style):** Display the relative path tree with a user-defined path style (Unix or Windows).
- **Directory Tree Structure:** Display a structured tree view of the directory.
- **Beautify Tree Structure:** Display a beautified tree view of the directory.

## Prerequisites and Dependencies

- Python 3.x

## Usage

### Simple Tree:

Display a simple tree view of the directory.

```bash
python dirtree.py simple /path/to/directory
```

**Example Output:**

```bash
directory/
file1.txt
file2.txt
subdirectory/
file3.txt
```

### Absolute Path Tree (Platform-Independent):

Display the absolute path tree using forward slashes or backward slashes depending upon which operating system are you using. This script automatically adjusts to the underlying operating system, using forward slashes for Unix-like systems and backward slashes for Windows systems.

```bash
python dirtree.py abs_pi /path/to/directory
```

**Example Output for Windows:**

```bash
E:\path\to\directory
E:\path\to\directory\file1.txt
E:\path\to\directory\file2.txt
E:\path\to\directory\subdirectory
E:\path\to\directory\subdirectory\file3.txt
```

**Example Output for Linux:**

```bash
E:/path/to/directory
E:/path/to/directory/file1.txt
E:/path/to/directory/file2.txt
E:/path/to/directory/subdirectory
E:/path/to/directory/subdirectory/file3.txt
```

### Relative Path Tree (Platform-Independent):

Display the relative path tree using forward slashes or backward slashes depending upon which operating system are you using. This script automatically adjusts to the underlying operating system, using forward slashes for Unix-like systems and backward slashes for Windows systems.

```bash
python dirtree.py rel_pi /path/to/directory
```

**Example Output for Windows:**

```bash
directory
directory\file1.txt
directory\file2.txt
directory\subdirectory
directory\subdirectory\file3.txt
```

**Example Output for Linux:**

```bash
directory
directory/file1.txt
directory/file2.txt
directory/subdirectory
directory/subdirectory/file3.txt
```

### Absolute Path Tree (User-Defined Style):

Display the absolute path tree with a user-defined path style. This script enables users to explicitly specify the desired path style (Unix or Windows), offering flexibility and consistency across different operating systems.

Change the --path_style parameter as needed, '/' for unix like path formatting and '\' for windows like path format.

```bash
python dirtree.py abs /path/to/directory --path_style /
```

**Example Output:**

```bash
E:/path/to/directory
E:/path/to/directory/file1.txt
E:/path/to/directory/file2.txt
E:/path/to/directory/subdirectory
E:/path/to/directory/subdirectory/file3.txt
```

### Relative Path Tree (User-Defined Style):

Display the absolute path tree with a user-defined path style. This script enables users to explicitly specify the desired path style (Unix or Windows), offering flexibility and consistency across different operating systems.

Change the --path_style parameter as needed, '/' for unix like path formatting and '\' for windows like path format.

```bash
python dirtree.py rel /path/to/directory --path_style /
```

**Example Output:**

```bash
directory
directory/file1.txt
directory/file2.txt
directory/subdirectory
directory/subdirectory/file3.txt
```

### Directory Tree Structure:

Display a structured tree view of the directory.

```bash
python dirtree.py tree /path/to/directory
```

**Example Output:**

```bash
+-- directory/
   +-- file1.txt
   +-- file2.txt
   +-- subdirectory/
      +-- file3.txt
```

### Beautify Tree Structure:

Display a beautified tree view of the directory.

```bash
python dirtree.py beautify /path/to/directory
```

**Example Output:**

```bash
- directory/
   |- file1.txt
   |- file2.txt
   |- subdirectory/
      |- file3.txt
```

### Notes

- Adjust the `/path/to/directory` to the actual path you want to visualize.
- Use the `--path_style` option to specify the path style for formatting (auto, /, \).
- Choose the desired function based on your visualization requirements.
