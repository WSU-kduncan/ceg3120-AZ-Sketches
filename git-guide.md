## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - To use: `git status`
- clone
  - Used to copy a repository. If the repository lies on a remote server.
  - To use: 'git clone username@host:/path/to/repository'
- add
  - Used to add files to the staging area.
  - To use: 'git add <temp.txt>'
- rm
  - Used to remove files from the index and the working directory.
  - To use: 'git rm filename.txt'
- commit
  - create a snapshot of the changes and save it to the git directory.
  - To use: 'git commit –m “Message to go with the commit here”'
- push
  - Used to send local commits to the master branch of the remote repository.
  - To use: 'git push origin <master>'
- fetch
   - Allows users to fetch all objects from the remote repository that don’t currently reside in the local working directory.
  - To use: 'git fetch origin'
- merge
  - Used to merge a branch into the active one.
  - To use: 'git merge <branch-name>'
- pull
  - Merges all the changes present in the remote repository to the local working directory.
  - To use: 'git pull'
- branch
  - Will list, create, or delete branches.
  - If you want to list all the branches present in the repository, the command should look like this: 'git branch'
  - If you want to delete a branch, use: 'git branch –d <branch-name>'
- checkout
  - Creates branches and helps you to navigate between them. For example, the following basic command creates a new branch and automatically switches you to it: 'command git checkout -b <branch-name>'
  - To switch from one branch to another, simply use: 'git checkout <branch-name>' 
- init
  - Creates a new local GIT repository. The following Git command will create a repository in the current directory: 'git init'
  - You can create a repository within a new directory by specifying the project name: 'git init [project name]'
- remote
  - Lets you view all remote repositories.
  - The following command will list all connections along with their URLs: 'git remote –v'
  - To connect the local repository to a remote server, use the command below: 'git remote add origin <host-or-remoteURL>' 
  - Meanwhile, the following command will delete a connection to a specified remote repository: 'git remote rm <name-of-the-repository>' 


## git files & folders

- .git folder
  - The.git folder is the directory which is created when you do 'git init'.
- .gitignore file
  - A .gitignore file is a plain text file where each line contains a pattern for files/directories to ignore.
- .git/hooks
  - All Git hooks are ordinary scripts that Git executes when certain events occur in the repository.


## GitHub

- Pull requests
  - When you open a pull request, you're proposing your changes and requesting that someone review and pull in your contribution and merge them into their branch.
- SSH authentication to repositories
  - SSH keys are used to authenticate secure connections.
- Actions
  - GitHub Actions Automate your workflow from idea to production.


## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)
  - Pro Git Book is a guide that allows readers to have a basic understanding of what Git is and how it is different from any other centralized version control systems that most users use.
