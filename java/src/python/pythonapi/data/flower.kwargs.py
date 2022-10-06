from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    Scene1 = Scene(    NavigationInfo2 = NavigationInfo(type=["EXAMINE","ANY"]), 
    DirectionalLight3 = DirectionalLight(direction=[0,-0.8,-0.2], intensity=0.5), 
    Background4 = Background(skyColor=[1.000,1.000,1.000]), 
    Viewpoint5 = Viewpoint(description="One mathematical orbital", position=[0,0,50]), 
    Transform6 = Transform(translation=[0,-1,1], rotation=[0,1,0,3.1415926], scale=[1.5,1.5,1.5],      Shape7 = Shape(      Appearance8 = Appearance(       Material9 = Material(transparency=0.1, diffuseColor=[0.9,0.3,0.3], specularColor=[0.8,0.8,0.8], shininess=0.145)), 
      IndexedFaceSet10 = IndexedFaceSet(ccw=False, convex=False, coordIndex=[0,1,2,-1], creaseAngle=0, DEF="ifs", solid=True,        Coordinate11 = Coordinate(DEF="crd", point=[0,0,1,0,1,0,1,0,0])))), 
    Script12 = Script(DEF="FlowerScript",      field13 = field(accessType="inputOnly", name="set_fraction", type="SFFloat"), 
     field14 = field(accessType="outputOnly", name="coordinates", type="MFVec3f"), 
     field15 = field(accessType="outputOnly", name="coordIndexes", type="MFInt32"),      sourceCode = '''ecmascript:\n"+
"    \n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"var resolution = 150;\n"+
"var t = 0;\n"+
"var p = 0;\n"+
"\n"+
"function initialize() {\n"+
"     var localci = new Array();\n"+
"     var ci = 0;\n"+
"     var buf = [];\n"+
"     for (var i = 0; i < resolution-1; i++) {\n"+
"     	for (var j = 0; j < resolution-1; j++) {\n"+
"	     localci[ci] = i*resolution+j;\n"+
"	     localci[ci+1] = i*resolution+j+1;\n"+
"	     localci[ci+2] = (i+1)*resolution+j+1;\n"+
"	     localci[ci+3] = (i+1)*resolution+j;\n"+
"	     localci[ci+4] = -1;\n"+
"	     buf.push(localci[ci]);\n"+
"	     buf.push(localci[ci+1]);\n"+
"	     buf.push(localci[ci+3]);\n"+
"	     buf.push(localci[ci+4]);\n"+
"\n"+
"	     buf.push(localci[ci+1]);\n"+
"	     buf.push(localci[ci+2]);\n"+
"	     buf.push(localci[ci+3]);\n"+
"	     buf.push(localci[ci+4]);\n"+
"	     ci += 5;\n"+
"	}\n"+
"    }\n"+
"    updateCoordinates(resolution);\n"+
"    coordIndexes = new x3dom.fields.MFInt32(buf);\n"+
"}\n"+
"\n"+
"function updateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var buf = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta + t) * Math.cos(h * phi + p);\n"+
"		var coord = new x3dom.fields.SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		);\n"+
"	     	buf.push(coord);\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     coordinates = new x3dom.fields.MFVec3f(buf);\n"+
"}\n"+
"\n"+
"function set_fraction() {\n"+
"	choice = Math.floor(Math.random() * 4);\n"+
"	switch (choice) {\n"+
"	case 0:\n"+
"		e += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 1:\n"+
"		f += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 2:\n"+
"		g += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 3:\n"+
"		h += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	}\n"+
"	t += 0.5;\n"+
"	p += 0.5;\n"+
"	if (f < 1) {\n"+
"		f = 10;\n"+
"	}\n"+
"	if (g < 1) {\n"+
"		g = 4;\n"+
"	}\n"+
"	if (h < 1) {\n"+
"		h = 4;\n"+
"	}\n"+
"	updateCoordinates(resolution);\n"+
"}\n"+
"''', ), 
    TimeSensor16 = TimeSensor(DEF="Clock", cycleInterval=16, loop=True), 
    ROUTE17 = ROUTE(fromNode="FlowerScript", fromField="coordIndexes", toNode="ifs", toField="coordIndex"), 
    ROUTE18 = ROUTE(fromNode="FlowerScript", fromField="coordinates", toNode="crd", toField="point"), 
    ROUTE19 = ROUTE(fromNode="Clock", fromField="fraction_changed", toNode="FlowerScript", toField="set_fraction")))
