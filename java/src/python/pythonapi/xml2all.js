"use strict";

// Convert X3D DOM to various formats

process.argv.shift();
process.argv.shift();

var convertXML = require('./convertXML.js');

convertXML([
	{ 
	serializer : './PythonSerializer.js',
	folder : "",
	extension : ".serial.py",
	},
	{ 
	serializer : './PythonKwargsSerializer.js',
	folder : "",
	extension : ".kwargs.py",
	},
	{ 
	serializer : './PythonAssignSerializer.js',
	folder : "",
	extension : ".assign.py",
	},
	{ 
	serializer : './PythonPipeliningSerializer.js',
	folder : "",
	extension : ".pipe.py",
	}
	]);
