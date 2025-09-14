import os
import time


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

    os.system(f"git clone {repos}")
    repos_name = repos.split("/")[-1].replace(".git", "")
    os.system(f"cd {repos_name}")
    os.system("git init")
    os.system("mkdir src | mkdir materials | touch README.md")
    os.system("touch src/.gitkeep | touch materials/.gitkeep")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")
    os.system("git push origin main")
    os.system("git branch develop")
    os.system("git checkout develop")
    os.system("git add .")
    os.system("git commit -m 'Initial develop-branch commit'")
    os.system("git push origin develop")

if __name__ == "__main__":
    info_board()
    fast_init_repos()