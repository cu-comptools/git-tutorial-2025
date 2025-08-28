# Git and GitHub tutorial

## 1. Contributing to a project with no direct access (via a fork)

1. Create a fork of the repository on GitHub: click on the "Fork" button to the right of this repository
2. Navigate to your fork of the repository on GitHub
3. Create a local copy of your fork: in the terminal, 
```bash
git clone git@github.com:<your username>/git-tutorial-2025
```
4. Now you have a local copy of this repo! Make some changes. Correct your name in the "students.txt" file (on your machine, not on GitHub).
5. Add the file to the upcoming commit from the terminal: `git add students.txt`
6. Add a useful message that summarizes your changes. Either add a message directly in the command line with
```bash
git commit -m "<Very useful commit message>"
```
or set the default commit message editor to be your editor of choice:
```bash
git config --global core.editor "<your favorite editor, such as vim>"
```
7. Push your changes from your local environment to your fork on GitHub: 
```bash
git push [--set-upstream ...]
```
8. Create a pull request to the original repository (that you forked). We will review and merge them.

## 2. Contributing to a project directly 

1. Change directory (`cd`) into `cu-comptools` on your machine, since you already have a copy from submitting homework.
2. Git clone _this_ repository directly (not your fork of it!): 
```bash
git clone git@github.com:cu-comptools/git-tutorial-2025
```
Unlike a fork, this creates a local copy of the repository itself, not your fork of it, so any changes you make and push would directly change the repository. So it's best to proceed from here with caution and use best practices when making changes: creating a new branch with the changes and then submitting a pull request into the main branch.
3. Bug fix exercise: create a new branch, `git checkout -b quadfix-<your name>`. Take a look at the code `utils/quadroots.py` (or `utils/quadroots.m` if you're working in MATLAB), which contains a bug. Fix this bug. 

To test whether you successfully fixed the bug, you will try running the unit test I wrote. In Python, this will be done via `pytest` (which you may have to install via conda or pip). In MATLAB, it'll be done by running the function without arguments, i.e. just executing the file. 

In Python,
```bash
python -m pytest
```

4. Once the bug is fixed, commit your changes with `git commit` and a useful message. 

5. When pushing, git will ask you to specify which remote you want to push to, with the `git push --set-upstream origin quadfix-<your-name>` command. This specifies that you want your repository on GitHub (the remote called "origin") to have a new branch with the same name as your local branch.
6. Submit a pull request to the `main` branch. We'll review and merge later.

## 3. Documentation exercise

1. In the `utils/` directory, there's another `.py` (`.m`) file that implements a single function. It only has a hint in its docstring. Look up the source from the hint, read the code, and try to figure out what the function does.
2. Write a docstring for this function.
4. Create a new branch for your work with the name `docfix-<your name>`, push to the remote repository, and submit a pull request to the main branch.

## 4. Unit test exercise

1. In most projects, like this one, there will be a `tests/` directory housing unit tests. They will usually be executed automatically, most often even before the contribution gets merged (upon a pull request). If in Python, inspect `tests/test_utils.py`, if in MATLAB, take a look at how the self-test is executed in `utils/quadroots.m`. 
2. Now take the function in `chebutils` and try to come up with a test case: is there a check you can devise for this function where you know the analytic answer? Code up your test input, your expected output from the function, and write a statement that takes the absolute or relative error between the expected answer an the output of a call of the function with the test arguments. Then come up with a resonable upper bound for this error, and put it in an `assert` statement. 
3. Run the unit tests to see if they work (the function is guaranteed to be correct).
4. As before, make a temporary new branch called `unittest-<your name>`, and submit a pull request with your unit test.

