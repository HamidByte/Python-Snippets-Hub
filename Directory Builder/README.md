# Directory Builder (dirbuilder.py)

A Python script designed to quickly create project structures based on a predefined layout. It simplifies the process of setting up directory hierarchies with files and folders. Creating a project structure manually can be time-consuming. This script allows you to automate the process, reading a predefined structure from a file and generating the necessary directories and files in your specified project path.

## Requirements

- Python 3

## Usage

**Project Structure File:**

Edit the `structure.txt` file to define your desired project structure. Each line represents a file or directory path relative to the project root. For example:

```bash
my-app/config/appConfig.js",
my-app/config/database.js",
my-app/controllers/database.js",
my-app/controllers/postController.js",
my-app/middlewares/authentication.js",
my-app/middlewares/authorization.js",
my-app/models/post.js",
my-app/models/user.js",
my-app/package.json",
my-app/public/images",
my-app/public/styles",
my-app/routes/index.js",
my-app/routes/api/users.js",
my-app/routes/api/posts.js",
my-app/routes/web/home.js",
my-app/routes/web/auth.js",
my-app/server.js",
my-app/services",
my-app/utils",
```

In this example, the script creates directories and the nested directories along with empty files.

**Run the Script:**

Replace `PROJECT_PATH` in the script with your desired project directory, then run:

```bash
python dirbuilder.py
```

**Output:**

The script creates the specified project structure at the provided project path.

## Combining with Directory Tree Visualizer

You can use `dirbuilder.py` in conjunction with `dirtree.py` to enhance your experience. Utilize `dirtree.py` to visualize and create a directory hierarchy for any existing project. Then, leverage that structure with `dirbuilder.py` to replicate the same organizational setup.
