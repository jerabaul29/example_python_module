# example_python_module

Just a toy example of a python module to illustrate how python module things can be set up on a machine.

A nice blog post discussing this in much details is (among many others such posts): https://docs.python-guide.org/writing/structure/ .

This is a quick reminder / example of setup, and a WIP as some questions / functionalities are needed on some of my projects.

## Setting up on a machine by hand by adding to pythonpath

A simple way to set up is to add to pythonpath by adding the following line to bashrc:

```bash
export PYTHONPATH="${PYTHONPATH}:SET_YOUR_PATH/example_python_module"
```

For example on my machine, where this lives together with my other git repositories:

```bash
export PYTHONPATH="${PYTHONPATH}:/home/jrmet/Desktop/Git/example_python_module"
```

The whole module then gets available to the python interpreter.

## Using the module

Once the module is added to the pythonpath, it is available on this system:

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
