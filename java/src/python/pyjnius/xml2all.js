"use strict";

// Convert X3D DOM to various formats

process.argv.shift();
process.argv.shift();

var convertXML = require('./convertXML.js');

convertXML([
	{ 
	serializer : './PythonSerializer.js',
	folder : "",
	extension : ".py",
	},
	{ 
	serializer : './PythonPipeliningSerializer.js',
	folder : "",
	extension : ".future.py",
	}
	]);
