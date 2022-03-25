# mpia-python-template

This repository contains a Python template suitable for starting new projects. The goal of this template is to create a properly 
packaged Python project which requires minimal set-up effort for the user. Our goal is also to encourage proper testing and documentation 
practices. This template contains a `tests/` directory with example code and it is automatically set up for automated GitHub Actions tests. 
Documentation templates with `sphinx` which automatically pull the API information from the code docstrings are also configured. 

This template does not assume GitHub tags, it is not set up for PyPi releases and it does not produce ReadTheDocs documentation, however such extensions can be easily added on to the template by motivated users. Please contact the template authors if you need help with these tasks.

# How to Use This Template

Click on the green "Use This Template" button in the upper right corner of the screen to make a copy of the template.

Select location for the new repository. For projects led by MPIA staff and/or with an MPIA advisor, we encourage you to create your repository within the `mpi-astronomy` organization but you can also create a copy under your own account.

Select a name for your reporsitory, select if it should be Public (recommended) or Private. Here as an example we will use `new_project` as the name of your new repository. 

Click on the Create Repository from Template button.

# Customize the Tempate

0. Create a new  `conda` environment for your project. This will allow you to track dependencies a lot easier.

1. Clone the repository locally:

`git clone git@github.com:mpi-astronomy/new_project.git`

If you have not set us SSH keys on your machine, then follow the instructions [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

2. Edit the `setup.cfg` file. 

Specifically change the following lines:

```name = my_package
version = 0.0.1
author = Example Author
author_email = author@example.com
description = A small example package
url = https://github.com/mpi-astronomy/new_project
project_urls =
    Bug Tracker = https://github.com/mpi-astronomy/new_project/issues
    Sourse Code = https://github.com/mpi-astronomy/new_project
```

The `name` here will be the name of your package, it does not have to be the same as the name of the repository (as shown here). This will be the name used to import your package once installed. 

The `version` variable must be manually incremented. Do not set versions elsewhere in the package. 

As you develop your code, you will need to specify any dependencies. Add any new dependencies after 
line 29 in `setup.cfg`. 

Test and documentation dependencies can be specified in the appropriate sections. 

3. Rename your package. 

If you chose a different name for your package in `name` you should now rename your directory name as well:
```
cd src/
git mv my_package new_package_name
```

4. Add your code to the `src/new_package_name/` directory. All your code should be `*.py` files in this directory. Do not add other directories inside `src/` unless you know what you are doing. Add your tests to the `tests/` directory. Edit the `docs\index.rst` file to create documentation for your project. 

5. Edit the `README.md`. Add a short description of your package instead of this text.

6. Edit the `CITATION.cff` file to specify how you want your code cited.

# What not to Change

1. Do not change the `LICENSE` file and definitely do not delete it. For more information, see [this article](https://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/). 

2. If you are an MPIA employee, do not change the `CODE_OF_CONDUCT.md` file.

3. You should not have to change `pyproject.toml` (unless you know what you are doing). In this setup you do not need to have `setup.py` or `requirements.txt` files. If you catch yourself creating these files, you have not followed the instructions. 

# Then What?

To use the code locally, install of your code from the `new_project` directory:
`pip install -e .`

This will create and installation such that you can keep editing the files. 

```pip install -e ".[tests]"

git clean -xdf
pip install .
pip install -e .

pip install -e ".[docs]"
flake8 
pytest --cov=.

```

