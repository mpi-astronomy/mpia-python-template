# mpia-python-template

This repository contains a Python template suitable for starting new projects. This template has three main goals:
- To create a properly 
packaged Python project which requires minimal set-up effort for the user. Following the seven steps below you will have the structure of a python package in ~15 minutes.
- To encourage proper testing. This template includes a GitHub actions workflow, `.github/workflows/ci.yml`, that will run continuous integration on the `tests` directory at every push or pull request. 
- To encourage code and package documentation. This template includes pre-configured documentation in the `docs` directory which will automatically pull the information from the code docstrings. A GitHub actions workflow, `.github/workflows/docs.yml`, also publishes the documentation to a GitHub Pages webpage at every push or pull request.

This template does not assume GitHub tags, it is not set up for PyPi releases and it does not produce ReadTheDocs documentation, however such extensions can be easily added on to the template by motivated users. Please contact the template authors if you need help with these tasks.

There is a lot of (sometimes contradictory) information on how to package a Python project. Here we have generally followed the [current recommendations](https://packaging.python.org/en/latest/tutorials/packaging-projects/) of the Python Packaging Authority. 

# How to Use This Template

Click on the green "Use This Template" button in the upper right corner of the screen to make a copy of the template.

Select location for the new repository. For projects led by MPIA staff and/or with an MPIA advisor, we encourage you to create your copy within the `mpi-astronomy` organization but you can also create a copy under your own account.

Select a name for your repository, select if it should be Public (recommended) or Private. Here as an example we will use `new_project` as the name of your new repository. 

Click on the `Create Repository from Template` button.

# Customize the Template in 7 Easy Steps

1. We recommend creating a new environment for your project. This will allow you to track dependencies a lot easier. There are several different ways to do this (`virtualenv`, `pipenv`). Here we show an example with `conda`:

```
conda create --name new_environment python
conda activate new_environment
```
Do not install dependencies that are necessary for your code with `conda`. All dependencies should be specified in the `setup.cfg` files (see step 2). If you need some libraries to do diagnostic work, you can install them now (e.g., `pip install numpy matplotlib ipython`) but make sure that they are included in `setup.cfg` if your package needs them.  We strongly recommend using `pip` for installation rather than `conda`. Note: if you do not have `conda` installed, we recommend [`miniconda`](https://docs.conda.io/en/latest/miniconda.html).

2. Make a copy of the repository on your computer:

`git clone git@github.com:mpi-astronomy/new_project.git`

If you have not set us SSH keys on your machine, then follow the instructions [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

3. Edit the `setup.cfg` file. 

Specifically change the following lines:

```
name = new_package_name
version = 0.0.1
author = Your Name
author_email = your.name@example.com
description = A small example package to do X and Y
url = https://github.com/mpi-astronomy/new_project
project_urls =
    Bug Tracker = https://github.com/mpi-astronomy/new_project/issues
    Source Code = https://github.com/mpi-astronomy/new_project
```

The `name` here will be the name of your package, it does not have to be the same as the name of the repository (as shown here). This will be the name used to import your package once installed. 

The `version` variable must be manually incremented. There are only two places where you should set the version: here and in the `CITATION.cff` file (see below). Make sure you increment them both.  

As you develop your code, you will need to specify any dependencies. Add any new dependencies after 
line 28 in `setup.cfg`. 

Test and documentation dependencies can be specified in the appropriate sections.

4. Rename your package. 

If you chose a different name for your package in `name` you should now rename your directory name as well. For example, in the previous step I changed the name of this package from the default `my_package` to `new_package_name`. Here we rename the directory too:
```
cd src/
git mv my_package new_package_name
```

5. Edit the `README.md`. Add a short description of your package instead of this text.

6. Edit the `CITATION.cff` file to specify how you want your code cited. The `CITATION.cff` file allows you to generate a `BibTeX` citation directly from the repository page (see `Cite this repository` in the upper right corner of this page). The fields we include here are the minimum recommended in the [AstroBetter post](https://www.astrobetter.com/blog/2019/07/01/citing-astronomy-software-inline-text-examples/) on citing astronomical software with no DOI. Please review the recommendations therein if you would like to add more information to the citation. Additional information about `CITATION.cff` files can be found [here](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files).   

7. Add your code to the `src/new_package_name/` directory. All your code should be `*.py` files in this directory. Do not add other directories inside `src/` unless you know what you are doing. Add your tests to the `tests/` directory. Edit the `docs/index.rst` file to create documentation for your project. 

🎉 You have a package. 

# What not to Change

1. Do not change the `LICENSE` file and definitely do not delete it. For more information, see [this article](https://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/). 

2. If you are an MPIA employee, do not change the `CODE_OF_CONDUCT.md` file.

3. You should not have to change `pyproject.toml` (unless you know what you are doing). In this setup you do not need to have `setup.py` or `requirements.txt` files. All your requirements should be listed in the `setup.cfg` file. If you have a more complex package that requires that things happen at installation, you may also need to create a `setup.py` file, but we are going to keep things here simple.  

# Then What?

Once you have made a local copy of the repository, you can install the package and start developing, testing and documenting it. 

**Installation**

With the package structure used here, you do not have to point Python to the location of your package. You absolutely SHOULD NOT be adding the package directory to your `$PYTHONPATH`. Instead, you can use `pip` to install it locally:
```
pip install -e ~/path/to/new_project
```
or `pip install -e .` if you are already in the `new_project` directory. `pip` will install all the dependencies specified in the `setup.cfg` file. The `-e` flag makes the install editable which means that you do not have to install the package again and again after each change. Changes to your files inside the project folder will automatically reflect in changes on your installed package. If you are working in an interactive environment (`ipython`, `Jupyter`) you will need to re-import any modules that have changed. For example, after editing `module_x.py` you will need to do the following to have the changes available in the Python interpreter:

```
import importlib
importlib.reload(module_x)
```

An accessible description of `pip install` can be found in [here](https://www.reddit.com/r/learnpython/comments/ayx7za/how_does_pip_install_e_work_is_there_a_specific/).

To install a non-editable version, do:
```
pip install ~/path/to/new_project
```
This is how you can use your package once you are no longer developing it. Any users who are not contributing code can installing your package with:
```
pip install git+https://github.com/mpi-astronomy/new_project.git
```

**Commit early and often**

As you make changes to your package, get into the habit of committing changes early and often. Every time you add a new function, a new test, edit the docstring:
```
git add new_module.py
git commit -m "Added a function to reverse the sprocket of the whoosle."
```
And every few commits:
```
git push
```

`git` will not keep track of the files that `pip` creates during the installation, but once in a while it may be useful to clear them out and run `pip install -e .` again. 

**Testing your code**

Ideally, you should be writing tests along with the new code. To test your code, first install the test dependencies:
```
pip install -e ".[tests]"
```

Then run the tests from the `new_project` directory:
```
pytest --cov=.
```

The `--cov=.` flag generates a report on how much of you code is covered by tests. Ideally this should be >80%.

To check for compliance with the Python style guide, run `flake8`:
```
flake8
```

This repository come pre-set with continuous integration using GitHub Actions. Every time you push a commit or make a pull request, all tests will be automatically run by GitHub. On the GitHub page for your repository you should have an `Action` tab (forth from the left). This tab will show you the test results. While you can (and should) run the test suite locally, these runs are usually only on your operating system against one version of python. The advantage of CI is that you can test your code against different versions of python, different versions of key libraries and different operating systems. Here we have set up a simple test matrix which runs against four different versions of python. You can make the CI more complex if you need. You can disable/enable actions as shown [here](https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow) or by deleting the `.github/workflows/ci.yml` file (use `git rm`). 

**Creating documentation**

If/when you want to update the auto-generated `sphinx` documentation, you can edit the `docs/index.rst` file. This file is in `reStructuredText` format. More information on making your docs pretty is available in the [`sphinx` docs](https://www.sphinx-doc.org/en/master/tutorial/index.html).

To generate the documentation, you need to first install the dependencies and then make the pages:
```
pip install -e ".[docs]"
cd docs/
make html
open _build/html/index.html
```
`sphinx` can also generate a PDF of your docs, but this is left as an exercise for the user.

This repository is also set to auto-generate an HTML page with the documentation and creates a GitHub pages webpage. While the files are auto-generated, the page must be made visible in the first place. Go to the `Settings` tab in GitHub and in the left-hand menu navigate to the `Pages` option. Select the `gh-pages` branch in the drop down `Source` menu. This is a one-time setting. The URL for your documentation will be displayed in the green banner. The example documentation page for this repository can be found at [https://mpi-astronomy.github.io/mpia-python-template/](https://mpi-astronomy.github.io/mpia-python-template/). 

You can disable/enable the auto-generated documentation builds as shown [here](https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow) or by deleting the `.github/workflows/docs.yml` file (use `git rm`). To unpublish the documentation page, you also need to delete the `gh-pages` branch, see instructions [here](https://docs.github.com/en/pages/getting-started-with-github-pages/unpublishing-a-github-pages-site#unpublishing-a-project-site).
