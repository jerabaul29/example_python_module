[![testing](https://github.com/jerabaul29/example_python_package/actions/workflows/python-package.yml/badge.svg)](https://github.com/jerabaul29/example_python_package/actions/workflows/python-package.yml)

# example_python_package

Just a toy example of a python package (a package being a collection of modules, which are ```.py``` files) to illustrate how python package / module things can be set up on a machine, and a few things I often use when setting up python repos containing code.

This is a quick reminder / example of setup, and a WIP as some questions / functionalities are needed on some of my projects and added here for "documentation".

## Package set up

The idea here is to set up the package so that it is available on the machine, and to organize a bit the architecture of the the repo containing it. A nice blog post discussing this in much details is (among many others such posts): https://docs.python-guide.org/writing/structure/ .

A nice convention is to put the package in a folder having the same name, here, **example_package**.

### Setting up on a machine by hand by adding to pythonpath

A simple way to set up is to add to pythonpath by adding the following line to bashrc:

```bash
export PYTHONPATH="${PYTHONPATH}:SET_YOUR_PATH/example_python_module"
```

For example on my machine, where this lives together with my other git repositories, and my username is ```jrmet```:

```bash
export PYTHONPATH="${PYTHONPATH}:/home/jrmet/Desktop/Git/example_python_module"
```

A way to set it up on "all" machines with a similar **~/Desktop/Git/** organisation (which I use personally by default) is use the environment ```$HOME``` variable (which contains ```/home/jrmet```), and to write:

```bash
export PYTHONPATH="${PYTHONPATH}:${HOME}/Desktop/Git/example_python_module"
```

The whole package then gets available to the python interpreter.

### Using the package

Once the package is added to the pythonpath, it is available on this system:

```
>>> from example_package import some_module
>>> from example_package.some_sub_module import some_sub_module_1
>>> from example_package.some_other_sub_module import some_other_sub_module_1
>>> some_module.some_module_hello()
hello from some_module
>>> some_sub_module_1.some_sub_module_2_hello()
hello from some_sub_module_2
>>> some_other_sub_module_1.some_other_sub_module_2_hello()
hello from some_other_sub_module_2
```

## Unit testing

Unit testing is a very convenient way to 1) help ensure code quality and correctness, 2) gain a lot of time when refactoring code. Some companies have a policy that "if you refactor code, and all unit tests are passing, then you have done your work; any bug introduced by the code refactoring is not your responsibility, but the responsibility of the person owning the code pieces that now fail". I like this idea.

There are many ways to set up unit testing with Python. I like to use ```pytest```. Pytest will automatically find the folders / files / functions starting with the ```test``` prefix, and run them. See the **tests** folder for an example. There are many options for using ```pytest```, but usually what one needs is some variations around:

```
~/Desktop/Git/example_python_module [main|✚1…1]> pytest -v .
================================================= test session starts ==================================================
platform linux -- Python 3.8.5, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/jrmet/Desktop/Git/example_python_module
collected 2 items                                                                                                      

tests/tests_some_module/test_42.py::test_42_passing PASSED                                                       [ 50%]
tests/tests_some_module/test_42.py::test_42_failing FAILED                                                       [100%]

======================================================= FAILURES =======================================================
___________________________________________________ test_42_failing ____________________________________________________

    def test_42_failing():
        """Example of a failing test."""
>       assert(some_module_42() == 43)
E       assert 42 == 43
E         +42
E         -43

tests/tests_some_module/test_42.py:11: AssertionError
=============================================== short test summary info ================================================
FAILED tests/tests_some_module/test_42.py::test_42_failing - assert 42 == 43
============================================= 1 failed, 1 passed in 0.11s ==============================================
```

## Requirements

The ```requirements.txt``` should contain the list of packages needed and the lowest versions needed. This allows for automatic installation. When using a ```setup.py``` script these requirements can also be listed as an ```install_requires``` list, in which case the ```requirements.txt``` can be reduced to ```.``` for defaulting to the information contained in the ```setup.py```.

## CI/CD

CI/CD can be set up using the github ```Actions```. The setup for the actions is set in **.github/workflows**. To set up a new workflow, use the web API and edit the configuration file there. It is also possible to generate a badge that can be put on the main readme file.

