## CLEAN CODE for (astro-)physicists 

Repository for the "Clean Code for (astro-)physicists" Lecture in WiSe 23/24

### On this repository:
This repository will be updated throughout the course. 

#### Structure 
```
clean_code_ws_2324
  ┠─ exam            # (sample solution of the project)
  ┠─ examples        # (code examples from the lecture)
  ┠─ exercises       # (coding exercises and sample solutions)
  ┠─ resources       # (Sample data needed by code examples and project)
  ┖─ tests  
       ┠─ exam       # Unit tests for the project implementation
       ┠─ examples   # Unit test examples   
       ┖─ exercises  # Unit tests for the exercises
```

#### Rules
- Checkout `master` branch and pull changes regularly during the lecture (i.e., at least daily).
- If you want to commit your changes: 
    - create a new branch starting with unique personal identifier (e.g., Initials: "Johannes Hölken" -> Branch prefix: `jh_`)
    - Optional push your branch to the repo for a backup. Be aware that pushed solutions are visible to all participants. 




### Git Quickstart
First you need to create/provide an ssh key to gitlab. Please follow this tutorial: https://docs.gitlab.com/ee/user/ssh.html

**Clone this repository**
```
# SSH Checkout:
git clone git@gitlab.gwdg.de:cleancode/clean_code_ws_2324.git 
```

**Pull changes from master branch**
```
git checkout master
git pull
```

**Inspect your local copy of the repository**
```
git status
```
Lists all changes done locally and not yet tracked/committed.

```
git log
```
Displays the history of commit messages on the current branch.

**Creating (own) branches and committing changes** 
```
# Option A: Create a new branch:
git checkout -b <INITIALS>_<BRANCH_NAME>

# Option B: Re-Use an existing branch:
git checkout <EXISTING_BRANCH_NAME>
git pull 

# Add the files you want in this commit:
git add file/to/commit_1.py
git add file/to/commit_2.py
#  ... 

# When everything is set up give a descriptive name to the commit 
# and store it in the git-db:
git commit –m “My solution to exercise 123”

# Optional: Push to this onlne repository:
git push 
# If the branch does not (yet) exists in the online repo, 
# you might need to tell git where to push it to:
git push --set-upstream origin <INITIALS>_<BRANCH_NAME>

```

### Testing
Tests can e executed by typing `pytest` on the command line.

Use `pytest --cov` to inspect the coverage statistics.

```
---------- coverage: platform linux, python 3.8.10-final-0 -----------
Name                 Stmts   Miss  Cover
----------------------------------------
exam/__init__.py         0      0   100%
exam/errors.py           4      0   100%
exam/game_logic.py      47      0   100%
exam/hangman.py          7      7     0%
exam/interface.py       55      0   100%
exam/word_db.py         17      0   100%
----------------------------------------
TOTAL                  130      7    95%
```

To generate an HTML report for the coverage try 
```bash 
$ pytest --cov --cov-report html
```
and have a look at the generated  `htmlcov/index.html` file.
