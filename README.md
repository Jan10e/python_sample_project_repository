<!--
-*- coding: utf-8 -*-

 Author: Jantine Broek <jantine.broek@simmons-simmons.com>
 License: MIT
-->

<!-- Banners -->
[![DOI](https://zenodo.org/badge/DOI/12.3456/zenodo.78910.svg)](https://zenodo.org/)
[![Website](https://img.shields.io/website?up_message=online&url=https://gitlab.com/wavelength-data-science/sample_project_repo.git)](https://gitlab.com/wavelength-data-science/sample_project_repo.git)
[![PyPI](https://img.shields.io/pypi/v/a_project.svg)](https://pypi.org/project/a_project)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)


# Sample Project Repository
***
README.md files are written in markdown. [Learn how to write markdown here](https://docs.gitlab.com/ee/user/markdown.html).
## Table of contents
1. [General Info](#general-info)
   1. [Structuring a Repository](#structuring-repo)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)


<a name="general-info"></a>
## General info
***

This is a **sample project repository** for project developed in Python. This
section will tell you about this repository, but it will also tell you what to
put in the *General Info* section of your own packages.

This is a simple project and serves as an example repo to put your code in an
appropriate format. It also contains some tips for getting started writing and
contributing to Python packages. If you want to learn more about structuring
your project, check out
[this guide](https://docs.python-guide.org/writing/structure/).
For non-Python repo's, such as Azure, check out
[these examples](https://github.com/topics).

The *General Info* section of your README.md file should explain what your
package is for and why it is useful.

<a name="structuring-repo"></a>
### i. Structuring a repository

An integral part of having reusable code is having a sensible repository
structure. That is, which files do we have and how do we organise them.
Unfortunately, figuring out how to structure a Python project best is not
a trivial task. As with writing code, the key is to conform to standard
practice where possible and to name everything as helpfully as you can.

The example structure contained in this repository will help you organise
your code so that you won't have to do major restructuring once you want to
publish it:

```text
   project_name
   ├── docs
   │   ├── user_guide
   │   ├── api [if necessary]
   │   └── source
   │       ├── conf.py
   │       └── index.rst
   ├── project_name
   │   └── __init__.py
   ├── tests
   │   └── __init__.py
   ├── .gitignore
   ├── LICENSE.txt
   ├── README.md
   ├── requirements.txt [or add all in setup.py]
   ├── setup.cfg
   ├── setup.py
   ├── .toml
   └── .pre-commit-config.yaml
```

<a name="installation"></a>
## Installation
***
In general, the installation section will contain something like the
following if the package has been published to PyPI:
```bash
pip install mypackage
```
If installation is best done via downloading a private repository, this sort
of thing should work:
```bash
cd some/suitable/path
git clone https://gitlab.com/simmons_wavelength/cloned_repository.git
cd cloned_repository
python -m pip install -e .
```
You may also want to investigate
[this Stackoverflow question about installing packages from private git
repositories](https://stackoverflow.com/questions/4830856/is-it-possible-to-use-pip-to-install-a-package-from-a-private-github-repository).

**However**, this particular template repository is not supposed to be
installed,
[it is supposed to be
forked](https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html).
Forking is how you copy a repository as a starting point for a new and
unconnected repository.

<a name="usage"></a>
## Usage
***
The usage section of your readme should call out some specific use cases
(assuming that the user has already installed the package successfully) and
then maybe link to more extensive documentation stored elsewhere. For this
package, a usage example might be:

```python
# use either import PACKAGE
import sample_project_repository

# or use from PACKAGE import FUNCTION
from sample_project_repository import main

main.print_hi("Jantine") # output: Hi, Jantine
```
### How to get started using this template repository

1. Fork the repository in Gitlab to set up a new repository with a new name but the same content
2. Clone the repository to where you will work on it
3. Set up an appropriate conda environment, e.g.

`conda create --name awesomepackage python=3.8`

4. Activate your conda environment and install pip (installing pip
   is good practice to make sure the version of pip used to install packages
   while you have an active conda environment is the version within
   that environment, not the global version)

```bash
conda activate awesomepackage
conda install pip
```

5. Install the following packages in your conda environment that do not
   need to be listed as dependencies in your setup.py file but will be needed
   for test driven development and keeping code stylistically consistent:

```bash
pip install pre-commit black flake8 pytest pytest-cov parameterized
```

6. Edit the .pre-commit-config.yaml to make sure any relevant package
   directories are listed under the reorder-python-imports hook. [This
   is explained pretty well on the PyPI page for reorder-python-
   imports](https://pypi.org/project/reorder-python-imports/) (under
   Console Scripts, about the option --application-directories).

7. Run precommit a couple of times (first time, code quality checks
  may fail but automatic code editing may take place so that they pass
  next time). Type this in the console:

`pre-commit run --all-files`

8. Run all tests (`--cov-report=term-missing` and `--cov-branch` are
   arguments to the pytest package that are available when we are using
   the pytest-cov package and cause the pytest coverage checker to examine
   branches in code structure and make sure e.g. we have tests for each
   branch of an if block):

```bash
pytest --cov=awesomepackage --cov-report=term-missing --cov-branch
```
9. Write more code and tests (possibly not in that order).

We don't add a precommit hook for running unit tests because we want
precommit to run quickly and runnning unit tests is often slow (indeed,
precommit doesn't have any prebuilt hooks for running unit tests for this
reason)*

<a name="contributing"></a>
## Contributing
***
Tell people how to contribute to your project in this section. You don't
need to explain how to use git as we have below - just say where to raise
issues, how to make merge requests, who to contact, etc.

For this template repository there are more explicit instructions, which
apply to almost any code you contribute to at Wavelength:

(Note that you can technically go about this in a few ways, especially
if you're confident with git, but the below is pretty reliable.)

1. Raise an issue in Gitlab describing the change you believe needs to
   be made to a repository, or select (or be assigned) an existing issue
2. Create a merge request related to the issue
3. Clone the repository

```bash
git clone https://gitlab.com/simmons_wavelength/swl_sample_project_repository.git
```

4. Create a local branch that is named the same as the branch that
   was automatically created when you made the merge request and check
   it out.

`git branch BRANCH_NAME`

`git checkout BRANCH_NAME`

or combine these two commands with

`git checkout -b BRANCH_NAME`

5. Set the "upstream" of your branch to the corresponding branch in the
   remote repository using `git branch -u origin/BRANCH_NAME` (where
   BRANCH_NAME is the name of the branch created when you created your
   merge request) and use `git branch –vv` to check that

   * There's an asterisk next to the branch you thought you had
   checked out

   * The upstream of the branch (in the square brackets) is similar
   to origin\BRANCH_NAME (where BRANCH_NAME is the name of the branch
   created when you created your merge request)

6. Write your code
7. Write your tests (could do this before you write your code if you
   want!)
8. Make sure your code passes precommit hooks and unit tests
9. Commit your code with a descriptive message of what you did, e.g.

`git commit -m "Added unit testing examples to sample code"`

10. Push your changes with

`git push -u origin BRANCH_NAME`

*Strictly speaking you don't need `-u origin BRANCH_NAME` if you followed
step 5 correctly, as it's just setting the upstream again. Better safe
than sorry though.*

11. Inform the owner of the repository that your branch is ready to be
merged or rebased (depending on their preference)
12. Find something else to help out with.

<a name="license"></a>
## Licence
***
Choose an appropriate licence for your project and tell your users
which one you have chosen in this section.

The license for this template repository is the
[MIT licence](http://choosealicence.com/licenses/mit/).


```text
___                ___  ___          ___   __
\  \              /  /  \  \        /  /  |  |
 \  \     __     /  /    \  \      /  /   |  |
  \  \  /    \  /  /      \  \    /  /    |  |
   \  \/  __  \/  /        \  \  /  /     |  |
    \    /  \    /          \  \/  /      |  |______
     \__/    \__/            \____/       |_________|
.law

                                           2016-2021
```
