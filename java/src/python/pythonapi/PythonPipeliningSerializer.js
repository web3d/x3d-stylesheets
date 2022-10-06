"use strict";

const DOUBLE_SUFFIX = '';
const FLOAT_SUFFIX  = '';

var fs = require("fs");

function PythonPipeliningSerializer () {
    this.code = [];
    this.codeno = 0;
    this.preno = 0;
}

PythonPipeliningSerializer.prototype = {
	serializeToString : function(json, element, clazz, mapToMethod, fieldTypes) {
		this.code = [];
		this.codeno = 0;
		this.preno = 0;
		var stack = [];

		var str = "";
		// str += "# -*- coding: "+json.X3D.encoding+" -*-\n";

		str += "import X3Dpackage\n";
		str += "\n";

		stack.unshift(this.preno);
		this.preno++;
		var bodystr = "";
        
        // https://stackoverflow.com/questions/48469666/error-enoent-no-such-file-or-directory-open-moviedata-json
        // https://stackoverflow.com/questions/3151436/how-can-i-get-the-current-directory-name-in-javascript
        // console.log('Current directory: ' + process.cwd()); // Node.js method for current directory - not what is needed here
        // https://flaviocopes.com/node-get-current-folder/ use __dirname under Node.js
        
		bodystr += element.nodeName+stack[0]+" = ";
		bodystr += "("; // wrap entire expression in parenthesis to avoid needing line-continuation characters
		bodystr += "X3Dpackage."+element.nodeName;
		bodystr += this.subSerializeToString(element, mapToMethod, fieldTypes, 3, stack);
		str += "\n";
		bodystr += ")"; // wrap entire expression in parenthesis to avoid needing line-continuation characters
		str += bodystr;
		str += "\n";
		str += "\n";
		// str += element.nodeName+stack[0]+".toFileX3D(\""+clazz+"_RoundTrip.x3d\")\n";
		stack.shift();
		return str;
	},

	printSubArray : function (attrType, type, values, co, j, lead, trail) {
        // https://stackoverflow.com/questions/359494/which-equals-operator-vs-should-be-used-in-javascript-comparisons
		if (type === "int") {
			for (var v in values) {
				if (values[v] > 0x7fffffff) {
				    values[v] = values[v] - 4294967296;
				}
			}
		}
		if (type === "boolean") {
			for (var vv in values) {
			    if (values[vv] === 'true') {
				values[vv] = "True";
			    } else if (values[vv] === 'false') {
				values[vv] = "False";
			    }
			}
		}
		if (values[0] === "" || values[0] === null) {
			values.shift();
		}
		if (values.length > 0 && (values[values.length-1] === "" || values[values.length-1] === null)) {
			values.pop();
		}

		//if (attrType.startsWith("SF")) {
		    //return     lead+values.join(j)+trail; // avoid array brackets on SF types
		//} else {
		    return '['+lead+values.join(j)+trail+']';
		//}
	},

	printParentChild : function (element, node, cn, mapToMethod, n) {
		var prepre = ".";
		var addpre = "set";
		if (cn > 0 && node.nodeName !== 'IS') {
			addpre = "add";
		}
		if (node.nodeName === 'field') {
			addpre = "add";
		}

		var method = node.nodeName;
		if (typeof mapToMethod[element.nodeName] === 'object') {
			if (typeof mapToMethod[element.nodeName][node.nodeName] === 'string') {
				addpre = "";
				method = mapToMethod[element.nodeName][node.nodeName];
			} else {
				method = method.charAt(0).toUpperCase() + method.slice(1);
			}
		} else if (typeof mapToMethod[element.nodeName] === 'string') {
			addpre = "";
			method = mapToMethod[element.nodeName];
		} else {
			method = method.charAt(0).toUpperCase() + method.slice(1);
		}
		for (var a in node.attributes) {
			var attrs = node.attributes;
			try {
				parseInt(a);
				var attrsa = attrs[a];
				var attr = attrsa.nodeName;
				if (attrs.hasOwnProperty(a) && attrsa.nodeType === 2) { // attribute
					if (attr === "containerField") {
						method = attrsa.nodeValue.charAt(0).toUpperCase() + attrsa.nodeValue.slice(1);
						if (method === "Shaders") {
							addpre = "add";
							if (element.nodeName === "ProtoBody") {
								method = "Child";
							}
						} else {
							addpre = "set";
						}
					}
				}
			} catch (e) {
				console.error(e);
			}
		}
		if (node.nodeName === "IS") {
			method = "IS";
			addpre = "set";
		}
		if (addpre+method === "setJoints") {
			method = "Joints";
			addpre = "add";
		}
		if (addpre+method === "setValue") {
			method = "Value";
			addpre = "add";
		}
		if (addpre+method === "addChild" || method === "Children") {
			method = "Children";
			addpre = "add";
		}
                if (element.nodeName === 'Scene' && method === "Metadata") {
                        method = "Children"
                        addpre = "add";
		}
		return prepre+addpre+method;
	},
	stringValue : function(attrsa, attr, attrType, element) {
		var strval;
		var nodeValue = attrsa.nodeValue;
		if (nodeValue === 'NULL') {
			strval = "";
		} else if (attrType === "SFString") {
			if (attr === "accessType") {
				strval = '"'+nodeValue+'"';
			} else {
				strval = '"'+nodeValue.
					replace(/\\n/g, '\\\\n').
					replace(/\\?"/g, "\\\"") +'"';
			}
		} else if (attrType === "SFInt32") {
			strval = nodeValue;
		} else if (attrType === "SFFloat") {
			strval = nodeValue+FLOAT_SUFFIX;
		} else if (attrType === "SFDouble") {
			strval = nodeValue+DOUBLE_SUFFIX;
		} else if (attrType === "SFBool") {
			if (nodeValue === 'true') {
				strval = "True";
			} else if (nodeValue === 'false') {
				strval = "False";
			} else {
				strval = nodeValue;
			}
		} else if (attrType === "SFTime") {
			strval = nodeValue+DOUBLE_SUFFIX;
		} else if (attrType === "MFTime") {
			strval = this.printSubArray(attrType, "double", nodeValue.split(/[ ,\t\n]+/), this.codeno, DOUBLE_SUFFIX+',', '', DOUBLE_SUFFIX);
		} else if (attrType === "MFString") {
			nodeValue = nodeValue.replace(/^ *(.*) *$/, "$1");
			strval = this.printSubArray(attrType, "java.lang.String",
				nodeValue.substr(1, nodeValue.length-2).split(/"[ ,\t\r\n]+"/).
				map(function(x) {
					var y = x.
					       replace(/(\\\\+)/g, '$1$1').
					       replace(/\\\\"/g, '\\\"').
					       replace(/""/g, '\\"\\"').
					       replace(/&quot;&quot;/g, '\\"\\"').
					       // replace(/&/g, "&amp;").
					       replace(/\\n/g, '\\n');
					if (y !== x) {
						// console.error("Python Replacing "+x+" with "+y);
					}
					return y;
				}), this.codeno, '","', '"', '"');
		} else if (
			attrType === "MFInt32"||
			attrType === "MFImage"||
			attrType === "SFImage") {
			strval = this.printSubArray(attrType, "int", nodeValue.split(/[ ,\t\n]+/), this.codeno, ',', '', '');
		} else if (
			attrType === "SFColor"||
			attrType === "MFColor"||
			attrType === "SFColorRGBA"||
			attrType === "MFColorRGBA"||
			attrType === "SFVec2f"||
			attrType === "SFVec3f"||
			attrType === "SFVec4f"||
			attrType === "MFVec2f"||
			attrType === "MFVec3f"||
			attrType === "MFVec4f"||
			attrType === "SFMatrix3f"||
			attrType === "SFMatrix4f"||
			attrType === "MFMatrix3f"||
			attrType === "MFMatrix4f"||
			attrType === "SFRotation"||
			attrType === "MFRotation"||
			attrType === "MFFloat") {
			strval = this.printSubArray(attrType, "float", nodeValue.split(/[ ,\t\n]+/), this.codeno, FLOAT_SUFFIX+',', '', FLOAT_SUFFIX);
		} else if (
			attrType === "SFVec2d"||
			attrType === "SFVec3d"||
			attrType === "SFVec4d"||
			attrType === "MFVec2d"||
			attrType === "MFVec3d"||
			attrType === "MFVec4d"||
			attrType === "SFMatrix3d"||
			attrType === "SFMatrix4d"||
			attrType === "MFMatrix3d"||
			attrType === "MFMatrix4d"||
			attrType === "MFDouble") {
			strval = this.printSubArray(attrType, "double", nodeValue.split(/[ ,\t\n]+/), this.codeno, DOUBLE_SUFFIX+',', '', DOUBLE_SUFFIX);
		} else if (attrType === "MFBool") {
			strval = this.printSubArray(attrType, "boolean", nodeValue.split(/[ ,\t\n]+/), this.codeno, ',', '', '');
		} else {
			strval = '"'+nodeValue.replace(/\n/g, '\\\\n').replace(/\\?"/g, "\\\"")+'"';
		}
		return strval;
	},
	subSerializeToString : function(element, mapToMethod, fieldTypes, n, stack) {
		var initstr = [];
		var setstr = "";
		var str = "";
		var attrType = "";
		for (var a in element.attributes) {
			var accessType = "inputOutput";
			var attrs = element.attributes;
			try {
				parseInt(a);
				var attrsa = attrs[a];
				var attr = attrsa.nodeName;
				if (attrs.hasOwnProperty(a) && attrsa.nodeType === 2) { // attribute
					// not found in field types
					// Fixes for X3DOM
					if (attr === "xmlns:xsd") {
						continue;
					} else if (attr === "xsd:noNamespaceSchemaLocation" ) {
						continue;
					} else if (attr === 'containerField') {
						continue;
					} else if (attr === "id") {
						continue;
					} else if (element.nodeName === "Sphere" && attr === "subdivision") {
						continue;
					} else if (element.nodeName === "X3D" && attr === "showStat") {
						continue;
					} else if (element.nodeName === "X3D" && attr === "showLog") {
						continue;
					} else if (element.nodeName === "X3D" && attr === "width") {
						continue;
					} else if (element.nodeName === "X3D" && attr === "height") {
						continue;
					} else if (element.nodeName === "X3D" && attr === "backend") {
						continue;
					} else if (element.nodeName === "Background" && attr === "groundTransparency") {
						continue;
					} else if (element.nodeName === "Background" && attr === "skyTransparency") {
						continue;
					}
					attrType = "SFString";
					if (typeof fieldTypes[element.nodeName] !== 'undefined'
					 && typeof fieldTypes[element.nodeName][attr] !== 'undefined') {
						attrType = fieldTypes[element.nodeName][attr][0];
						accessType = fieldTypes[element.nodeName][attr][1];
					}
					var strval = this.stringValue(attrsa, attr, attrType, element);
					var method = attr;
					// if (attr !== 'mustEvaluate' && attr !== 'proxy' && attr !== 'side' && attr !== 'style' && attr !== 'bottom' && attr !== 'height' && attr !== 'category' && attr !== 'solid' && attr !== 'justify' && attr !== 'ccw' && attr !== 'convex' && attr !== 'family' && attr !== 'bboxSize' && attr !== 'bboxCenter' && attr !== "normalPerVertex" && attr !== "normalIndex" && attr !== "texCoordIndex" && attr !== "coordIndex" && attr !== "directOutput" && attr !== "crossSection" && attr !== "spine" && attr !== "creaseAngle" && attr !== "repeatS" && attr !== "repeatT" && attr !== "colorPerVertex" && attr !== "size" && attr !== "bottomRadius" && attr !== "radius" && attr !== "language") {
						method = "set"+method.charAt(0).toUpperCase() + method.slice(1);
						if (attr === "class") {
							method = "setClass";
						}
					if (accessType !== 'initializeOnly') {

                    // Object typing when setting values:
//						setstr += '.'+method+"(X3Dpackage."+attrType+"("+strval+"))";// field type casting
						setstr += '.'+method+"("+strval+")"; // avoid type casting

					} else {
						if (attr === "class") {
							method = "Class";
						} else if (attr === "global") {
							method = "Global";
						}
						initstr.push(method+' = '+strval);
					}
				}
			} catch (e) {
				console.error(e);
			}
			attrType = "";
		}
		str += "("+initstr.join(", ")+")";
		if (setstr !== "") {
			str += setstr;
//			str += " \\\n";
		} else {
//			str += " \\";
//			str += "\n";
		}
        var lastNodeType = element.childNodes[0];
		for (var cn in element.childNodes) {
			var node = element.childNodes[cn];
			if (element.childNodes.hasOwnProperty(cn) && node.nodeType === 1) { // element
//              console.log('node type 1: ' + node); // trace
                lastNodeType = node.nodeType;
				var ch = "";
				stack.unshift(this.preno);
				this.preno++;
				// ch += node.nodeName+stack[0] + " = ";
				ch += "\n";
				ch += "  ".repeat(n);

				method = this.printParentChild(element, node, cn, mapToMethod, n);
				ch += method;
				ch += "(";
				if (method === 'addChildren') {
					ch += '[';
				}
				ch += "X3Dpackage."+node.nodeName;
				ch += this.subSerializeToString(node, mapToMethod, fieldTypes, n+1, stack);
//				ch += "  ".repeat(n);
				if (method === 'addChildren') {
					ch += ']';
				}
				ch += ")";
//				ch += " \\"; // line continuation is optional inside parenthesis or braces
				str += ch;
				stack.shift();
			} else if (element.childNodes.hasOwnProperty(cn) && node.nodeType === 8) { // comment
//              console.log('node type 8: ' + node); // trace
                lastNodeType = node.nodeType;
                // process a comment
				var y = node.nodeValue.
					replace(/\\/g, '\\\\').
					replace(/"/g, '\\"');
				// str += "\n"+element.nodeName+stack[0];
				// str += ".addComments(CommentsBlock(\"\"\""+y+"\"\"\")) \\\n";
				str += "\n";
                // python comments: https://docs.python.org/3.7/tutorial/introduction.html
				str += "  ".repeat(n);
				str += y.split("\n").map(function(x) {
					return x.replace(/^/g, '#');
					}).join("\n");
				str += "\n";
				if (y !== node.nodeValue) {
					// console.error("Java Comment Replacing "+node.nodeValue+" with "+y);
				}
			} else if (element.childNodes.hasOwnProperty(cn) && node.nodeType === 4) {  // CDATA section (shaders and scripts)
//              console.log('node type 4: ' + node); // trace
                lastNodeType = node.nodeType;
				str += ".setSourceCode('''"+node.nodeValue.split(/\r?\n/).map(function(x) {
					return x.
					        replace(/\\/g, '\\\\').
                            replace(/"/g, '\\"')
                            /*
                            .replace(/\\n/g, "\\\\n")
                            */
					;
					}).join('\\n\"+\n\"')+"''')\n";
			}
		}
//      console.log('lastNodeType=' + lastNodeType); // trace
        if (lastNodeType === 8) // comment
            str += "\n" + "  ".repeat(n); // line break after comment before closing parentheses
		return str;
	}
};

if (typeof module === 'object')  {
	module.exports = PythonPipeliningSerializer;
}
