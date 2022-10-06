# X3D Python Language Binding

* Related: http://www.web3d.org/wiki/index.php/X3D_JSON_Encoding

## Design Requirements, Goals and Use Cases

Design requirement:

* X3D Scene Authoring Interface (SAI) programming language binding for Python
* Loader to manipulate a scene graph using Python programming

Design goals and primary use cases:

* Provide a programming capability that tracks X3DJSAIL by using PyJNIus
* Once Python syntax is established, we will convert all X3D Examples

## Initial implementation

For now, this is just initial implementation.  Maybe someday another will occur.

* Describe how to '''build''' a configuration library using PyJNIUS in combination with X3DJSAIL.

Basic command line (possibly at anaconda prompt, if necessary).

Run ant:

1. Install dependencies

```
cd pyjnius
ant install.dependencies
```

2. Build python files

```
cd pyjnius
ant configuration
```

* Describe how to '''use'''   a configuration library using PyJNIUS in combination with X3DJSAIL

Convert X3D to Python:

```
node xml2all.js <file>.x3d
```

produces <file>.py and <file>.future.py

To run those files, use python:

```
python <file>.py   # produces <file>.new.x3d
```

```
python <file>.future.py # if no problems, produces <file>.newFile.x3d
```

## Programming environments

* Stock install from python.org

* PyCharm,  Don

* Anaconda, Don
** https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments
** https://stackoverflow.com/questions/48174935/conda-creating-a-virtual-environment

1.  Start anaconda prompt from Start Menu.  Type Anacond.. to find it

2.  Create virtual environment

```
conda create --name=x3d
```
3.  Confirm environment creation

```
conda info --envs
```
4.  Enter environment
```
conda activate x3d
```
5. Run ant commands and python commands as above

* Vim text editor, John
* Bash command prompt, John

1. Run ant commands and python commands as above

* [Pyjnius documentation](https://pyjnius.readthedocs.io/en/stable)

## Design patterns

This section will compare various Python styles.  Parts may be mutually compatible.

* Style 1

/insert source/

* Style 2

/insert source//

* Style 3

/insert source//

## PyJNIus

Instructions here

## Future Goals

We will keep code that is different than stock X3D SAI and X3DJSAIL in a different file tree.

Many other cool things will be possible!

