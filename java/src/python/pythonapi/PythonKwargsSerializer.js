"use strict";

const DOUBLE_SUFFIX = '';
const FLOAT_SUFFIX = '';

function PythonKwargsSerializer () {
this.code = [];
this.codeno = 0;
this.preno = 0;
}


PythonKwargsSerializer.prototype = {
	serializeToString : function(json, element, clazz, mapToMethod, fieldTypes) {
		this.code = [];
		this.codeno = 0;
		this.preno = 0;
		var stack = [];

		var str = "";
		// str += "# -*- coding: "+json.X3D.encoding+" -*-\n";

		str += "from X3Dpackage import *\n";

		stack.unshift(this.preno);
		this.preno++;
		str += element.nodeName+stack[0]+" = "+element.nodeName+"(";
		var as = this.subSerializeAttrsToString(element, mapToMethod, fieldTypes, 3, stack);
		var ns = this.subSerializeNodesToString(element, mapToMethod, fieldTypes, 3, stack);
		if (as && ns) {
			str += as+", "+ns;
		} else {
			if (typeof as !== 'undefined') {
				str += as;
			}
			if (typeof ns !== 'undefined') {
				str += ns;
			}
		}
		if (str.substr(str.length-3, 3) === "), ") {
			str = str.substring(0, str.length-2);
		}
		str += ")\n";
		// str += element.nodeName+stack[0]+".toFileX3D(\""+clazz+".newf.x3d\")\n";
		stack.shift();
		return str;
	},

	printSubArray : function (attrType, type, values, co, j, lead, trail) {
                if (type === "int") {
                        for (var v in values) {
				if (values[v] > 0x7fffffff) {
				    values[v] = values[v] - 4294967296
				}

				/*
                                if (values[v] > 4200000000) {
                                        values[v] = "0x"+parseInt(values[v]).toString(16).toUpperCase();
                                }
				*/
                        }
                }
		if (values[0] === "" || values[v] === null) {
			values.shift();
		}
		if (values.length >= 0 && (values[values.length-1] === "" || values[values.length-1] === null)) {
			values.pop();
		}
		return '['+lead+values.join(j)+trail+']';
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
				if (attrs.hasOwnProperty(a) && attrsa.nodeType == 2) {
					if (attr === "containerField") {
						if (method === "setShaders") {
							addpre = "add";
							if (element.nodeName === "ProtoBody") {
								method = "Child";
							}
						} else {
							method = "set"+attrsa.nodeValue.charAt(0).toUpperCase() + attrsa.nodeValue.slice(1);
							addpre = "";
						}
					}
				}
			} catch (e) {
				console.error(e);
			}
		}
		if (node.nodeName === "IS") {
			method = "setIS";
			addpre = "";
		}
		if (method === "setJoints") {
			method = "addJoints"
			addpre = "";
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
					replace(/\\?"/g, "\\\"")
					+'"';
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
			strval = this.printSubArray(attrType, "double", nodeValue.split(/[ ,\t\r\n]+/), this.codeno, DOUBLE_SUFFIX+',', '', DOUBLE_SUFFIX);
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
			strval = this.printSubArray(attrType, "int", nodeValue.split(/[ ,\t\r\n]+/), this.codeno, ',', '', '');
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
			strval = this.printSubArray(attrType, "float", nodeValue.split(/[ ,\t\r\n]+/), this.codeno, FLOAT_SUFFIX+',', '', FLOAT_SUFFIX);
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
			strval = this.printSubArray(attrType, "double", nodeValue.split(/[ ,\t\r\n]+/), this.codeno, DOUBLE_SUFFIX+',', '', DOUBLE_SUFFIX);
		} else if (attrType === "MFBool") {
			strval = this.printSubArray(attrType, "boolean", nodeValue.split(/[ ,\t\r\n]+/), this.codeno, ',', '', '');
		} else {
			strval = '"'+nodeValue.replace(/\n/g, '\\\\n').replace(/\\?"/g, "\\\"")+'"';
		}
		return strval;
	},
	subSerializeNodesToString : function(element, mapToMethod, fieldTypes, n, stack) {
		var str = "";
		var attrType = "";
		for (var cn in element.childNodes) {
			var node = element.childNodes[cn];
			if (element.childNodes.hasOwnProperty(cn) && node.nodeType == 1) {
				var ch = "";
				/*
				if (element.nodeName === "Appearance" && node.NodeName === "ComposedShader") {
					ch += "X3DNode [] {";
				}
				*/
				stack.unshift(this.preno);
				this.preno++;
				if (str.length > 0) {
					ch += "\n";
				}
				ch += " ".repeat(n)+node.nodeName+stack[0] + " = ";
				ch += node.nodeName+"(";
				var as = this.subSerializeAttrsToString(node, mapToMethod, fieldTypes, n+1, stack);
				var ns = this.subSerializeNodesToString(node, mapToMethod, fieldTypes, n+1, stack);
				if (as && ns) {
					ch += as+", "+ns;
				} else {
					if (typeof as !== 'undefined') {
						ch += as;
					}
					if (typeof ns !== 'undefined') {
						ch += ns;
					}
				}
				if (ch.substr(ch.length-3, 3) === "), ") {
					ch = ch.substring(0, ch.length-2);
				}
				ch += "), ";
				str += ch;
				stack.shift();
			} else if (element.childNodes.hasOwnProperty(cn) && node.nodeType == 8) {
				var y = node.nodeValue.
					replace(/\\/g, '\\\\').
					replace(/"/g, '\\"');
				// str += "\n"+element.nodeName+stack[0];
				// str += ".addComments(CommentsBlock(\"\"\""+y+"\"\"\")) \\\n";
				str += (" ".repeat(n))+y.split("\r\n").map(function(x) {
					return x.replace(/^/g, '#');
					}).join("\r\n");
				str += "\r\n";
				if (y !== node.nodeValue) {
					// console.error("Java Comment Replacing "+node.nodeValue+" with "+y);
				}
			} else if (element.childNodes.hasOwnProperty(cn) && node.nodeType == 4) {
				// str += "\n"+element.nodeName+stack[0];
				str += (" ".repeat(n))+"sourceCode = '''"+node.nodeValue.split("\r\n").map(function(x) {
					return x.
					        replace(/\\/g, '\\\\').
						replace(/"/g, '\\"')
						/*
						.replace(/\\n/g, "\\\\n")
						*/
					;
					}).join('\\n\"+\n\"')+"''', ";
			}
		}
		return str;
	},
	subSerializeAttrsToString : function(element, mapToMethod, fieldTypes, n, stack) {
		var attrType = "";
		var str = "";
		for (var a in element.attributes) {
			var accessType = "inputOutput";
			var attrs = element.attributes;
			try {
				parseInt(a);
				var attrsa = attrs[a];
				var attr = attrsa.nodeName;
				if (attrs.hasOwnProperty(a) && attrsa.nodeType == 2) {
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
					// look at object model
					attrType = "SFString";
					if (typeof fieldTypes[element.nodeName] !== 'undefined'
					&& typeof fieldTypes[element.nodeName][attr] !== 'undefined') {
						attrType = fieldTypes[element.nodeName][attr][0];
						accessType = fieldTypes[element.nodeName][attr][1];
					}
					var strval = this.stringValue(attrsa, attr, attrType, element);
					var method = attr;
					if (attr === "class") {
						method = "Class";
					} else if (attr === "global") {
						method = "Global";
					}
					str += method+"="+strval;
					str += ", ";
				}
			} catch (e) {
				console.error(e);
			}
			attrType = "";
		}
		if (str.startsWith(", ")) {
			str = str.substr(2); // strip off comma
		}
		if (str.endsWith(", ")) {
			str = str.substring(0, str.length-2); // strip off comma
		}
		return str;
	}
};


if (typeof module === 'object')  {
	module.exports = PythonKwargsSerializer;
}
