## Pyjnius project mapping X3DJSAIL to Python binding

This experimental work explored multiple variations for using X3DJSAIL to 
map X3D to a Python language binding.

Almost everything worked, but Pyjnius was unable to keep aligned with 
X3DJSAIL object return types and so perhaps 20% of the API was unworkable.

Focus of work has shifted to completing a native Python X3D package written in Python.

This project is being retained in case Pyjnius changes someday occur, enabling
this work to be finished as a second implementation of X3D Python.


## Project summary

This folder converts X3D XML to Python and then runs the result.
It also installs various tools for running the conversion.

Ant targets

all
	depends on targerts clean and configuration
	calls processAllScenes.x3dToPython
          processAllScenes.pythonValidation

clean
	clean out unnecessary backup files (only)

configuration.prerequisites
	Configure prerequisites for local Python installation">

makeorg
	create python tree

configuration
	depends on clean,configuration.prerequisites HelloWorld.python

processAllScenes.x3dToPython
	calls processSingleScene.x3dToPython on each file


processSingleScene.x3dToPython
	convert X3D to python on a single file

processAllScenes.pythonValidation
        calls processSingleScene.pythonValidation on each file

processSingleScene.pythonValidation
	runs python file

HelloWorld.python
	converts HelloWorld X3D file to python and runs it.
