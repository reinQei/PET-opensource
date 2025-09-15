import os
import subprocess
from pathlib import Path


def info_board():
    print("Before we start, create a new repository on GitHub")
    print("1. Go to GitHub and create a new repository")
    print("2. Copy the repository URL")
    print("3. Paste the repository URL into the terminal")
    print("4. Press Enter")
    print("5. Wait for the repository to be initialized")

def fast_init_repos():
    try:
        repos = input("Enter ssh link of the repository to initialize: ")
    except ValueError:
        print("Invalid repository")
        return

    workspace = "/workspace"
    repos_name = repos.split("/")[-1].replace(".git", "")
    repo_path_for_work = os.path.join(workspace, repos_name)

    subprocess.run(["git", "clone", repos], cwd=workspace, check=True)

    subprocess.run(["bash", "-lc", "mkdir -p src materials"], cwd=repo_path_for_work, check=True)
    subprocess.run(["bash", "-lc", "touch README.md src/.gitkeep materials/.gitkeep"], cwd=repo_path_for_work, check=True)
    
    subprocess.run(["git", "add", "."], cwd=repo_path_for_work, check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=repo_path_for_work, check=True)
    subprocess.run(["git", "branch", "-M", "main"], cwd=repo_path_for_work, check=True)
    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=repo_path_for_work, check=True)
    subprocess.run(["git", "checkout", "-b", "develop"], cwd=repo_path_for_work, check=True)
    subprocess.run(["git", "push", "-u", "origin", "develop"], cwd=repo_path_for_work, check=True)


if __name__ == "__main__":
    info_board()
    fast_init_repos()