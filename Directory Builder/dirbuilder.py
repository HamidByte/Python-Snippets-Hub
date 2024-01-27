import os

# Define global constants
PROJECT_PATH = 'E:/my-nodejs-app' # Provide your desired project directory

def create_project_structure(project_path):
    # Define the structure or read from the file
    # structure = [
    #     "my-app/config/appConfig.js",
    #     "my-app/config/database.js",
    #     "my-app/controllers/database.js",
    #     "my-app/controllers/postController.js",
    #     "my-app/middlewares/authentication.js",
    #     "my-app/middlewares/authorization.js",
    #     "my-app/models/post.js",
    #     "my-app/models/user.js",
    #     "my-app/package.json",
    #     "my-app/public/images",
    #     "my-app/public/styles",
    #     "my-app/routes/index.js",
    #     "my-app/routes/api/users.js",
    #     "my-app/routes/api/posts.js",
    #     "my-app/routes/web/home.js",
    #     "my-app/routes/web/auth.js",
    #     "my-app/server.js",
    #     "my-app/services",
    #     "my-app/utils",
    # ]
    # Read the directory structure from a file
    with open("structure.txt", "r") as file:
        structure = [line.strip() for line in file.readlines()]

    # Create directories and files
    for item in structure:
        item_path = os.path.join(project_path, item)
        if "." in item:
            # File
            os.makedirs(os.path.dirname(item_path), exist_ok=True)
            with open(item_path, "w") as file:
                pass  # Creating an empty file
        else:
            # Directory
            os.makedirs(item_path, exist_ok=True)

    print(f"Project structure created at {project_path}")

if __name__ == '__main__':
    project_directory = PROJECT_PATH
    create_project_structure(project_directory)