import os
import argparse

def simple_tree(dir_path):
    print(os.path.basename(dir_path) + '/')

    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            simple_tree(item_path)
        else:
            print(item)

# Platform-Independent Path Handling for Absolute Path Tree
def absolute_path_tree_pi(dir_path):
    print(dir_path)
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            absolute_path_tree_pi(item_path)
        else:
            print(item_path)

# User-Defined Path Formatting for Absolute Path Tree
def absolute_path_tree(dir_path, path_style='auto'):
    if path_style == 'auto':
        path_style = os.path.sep  # Use the default separator based on the platform

    print(dir_path.replace(os.path.sep, path_style))
    for item in os.listdir(dir_path):
        item_path = os.path.normpath(os.path.join(dir_path, item))
        if os.path.isdir(item_path):
            absolute_path_tree(item_path, path_style)
        else:
            print(item_path.replace(os.path.sep, path_style))

# Platform-Independent Path Handling for Relative Path Tree
def relative_path_tree_pi(dir_path, relative_path=""):
    current_path = os.path.join(relative_path, os.path.basename(dir_path))
    print(current_path)

    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            relative_path_tree_pi(item_path, current_path)
        else:
            print(os.path.join(current_path, item))

# User-Defined Path Formatting for Relative Path Tree
def relative_path_tree(dir_path, relative_path="", path_style='auto'):
    if path_style == 'auto':
        path_style = os.path.sep  # Use the default separator based on the platform

    current_path = os.path.join(relative_path, os.path.basename(dir_path))
    print(current_path.replace(os.path.sep, path_style) + path_style)

    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            relative_path_tree(item_path, current_path, path_style)  # Use current_path instead of os.path.join(current_path, item)
        else:
            print(os.path.join(current_path, item).replace(os.path.sep, path_style))

def directory_tree_structure(dir_path, indent=''):
    print(indent[:-1] + '+-- ' + os.path.basename(dir_path) + '/')
    indent += '   '

    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            directory_tree_structure(item_path, indent)
        else:
            print(indent + '+-- ' + item)

def beautify_tree_structure(dir_path, indent=''):
    print(f"{indent}- {os.path.basename(dir_path)}")

    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            beautify_tree_structure(item_path, indent + '  |')
        else:
            print(f"{indent}  |- {item}")

def main():
    parser = argparse.ArgumentParser(description='Directory Tree Visualizer')

    # Specify the function to execute (simple, abs_pi, rel_pi, abs, rel, tree, beautify)
    parser.add_argument('function', choices=['simple', 'abs_pi', 'rel_pi', 'abs', 'rel', 'tree', 'beautify'],
                        help='Function to execute. Choose one of the following: simple, abs_pi, rel_pi, abs, rel, tree, beautify.')

    # Specify the path parameter
    parser.add_argument('path', help='Path parameter. Enter the path to the target directory.')

    # Specify an optional argument for path style formatting
    parser.add_argument('--path_style', default='auto',
                    help='Path style for formatting. Choose one of the following: auto, /, \\ (default: auto).\n'
                         'Examples:\n'
                         '  - For Unix-like paths: --path_style /\n'
                         '  - For Windows paths: --path_style \\\n'
                         '  - Automatic detection based on the platform: --path_style auto')

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print("Error: The specified path does not exist.")
    else:
        base_path = os.path.abspath(args.path)

        if args.function == 'simple':
            # Simple tree
            simple_tree(base_path)
        elif args.function == 'abs_pi':
            # Platform-Independent Path Handling for absolute path tree
            absolute_path_tree_pi(base_path)
        elif args.function == 'rel_pi':
            # Platform-Independent Path Handling for relative path tree
            relative_path_tree_pi(base_path)
        elif args.function == 'abs':
            # User-Defined Path Formatting for absolute path tree
            absolute_path_tree(base_path, args.path_style)
        elif args.function == 'rel':
            # User-Defined Path Formatting for relative path tree
            relative_path_tree(base_path, path_style=args.path_style)
        elif args.function == 'tree':
            # Directory Tree Structure
            directory_tree_structure(base_path)
        elif args.function == 'beautify':
            # Beautify Tree Structure
            beautify_tree_structure(base_path)

if __name__ == '__main__':
    main()
