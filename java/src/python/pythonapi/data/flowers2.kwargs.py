from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.0",    head1 = head(    meta2 = meta(content="title", name="flowers2.x3d"), 
    meta3 = meta(content="John Carlson", name="author"), 
    meta4 = meta(content="John Carlson", name="transcriber"), 
    meta5 = meta(content="23 January 2005", name="created"), 
    meta6 = meta(content="05 May 2017", name="modified"), 
    meta7 = meta(content="2 random mathematical roses in spherical dimensions. rho = a + b * cos(c * theta) * cos(d * phi)", name="description"), 
    meta8 = meta(content="https://coderextreme.net/x3d/flowers2.x3d", name="url"), 
    meta9 = meta(content="manually written", name="generator")), 
   Scene10 = Scene(    NavigationInfo11 = NavigationInfo(type=["EXAMINE","ANY"]), 
    Viewpoint12 = Viewpoint(description="Two mathematical orbitals", position=[0,0,50]), 
    Group13 = Group(     DirectionalLight14 = DirectionalLight(direction=[1,1,1]), 
     Transform15 = Transform(DEF="OrbitTransform", translation=[8,0,0],       Shape16 = Shape(       Appearance17 = Appearance(        Material18 = Material(diffuseColor=[0,0.5,1], specularColor=[0,0.5,1])), 
       IndexedFaceSet19 = IndexedFaceSet(convex=False, DEF="Orbit", creaseAngle=0,         Coordinate20 = Coordinate(DEF="OrbitCoordinates")))), 
     Transform21 = Transform(DEF="OrbitTransform2", translation=[-8,0,0],       Shape22 = Shape(       Appearance23 = Appearance(        Material24 = Material(diffuseColor=[1,0.5,0], specularColor=[1,0.5,0], transparency=0.75)), 
       IndexedFaceSet25 = IndexedFaceSet(DEF="Orbit2", creaseAngle=0,         Coordinate26 = Coordinate(DEF="OrbitCoordinates2")))), 
     TimeSensor27 = TimeSensor(DEF="Clock", cycleInterval=16, loop=True), 
     OrientationInterpolator28 = OrientationInterpolator(DEF="OrbitPath", key=[0.0,0.50,1.0], keyValue=[1.0,0.0,0.0,0.0,1.0,0.0,0.0,3.14,1.0,0.0,0.0,6.28]), 
     Script29 = Script(DEF="OrbitScript",       field30 = field(accessType="inputOnly", name="set_fraction", type="SFFloat"), 
      field31 = field(accessType="outputOnly", name="coordinates", type="MFVec3f"), 
      field32 = field(accessType="outputOnly", name="coordIndexes", type="MFInt32"),       sourceCode = '''\n"+
"\n"+
"ecmascript:\n"+
"\n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"\n"+
"function initialize() {\n"+
"     resolution = 100;\n"+
"     generateCoordinates(resolution);\n"+
"     var localci = [];\n"+
"     for ( i = 0; i < resolution-1; i++) {\n"+
"     	for ( j = 0; j < resolution-1; j++) {\n"+
"	     localci.push(i*resolution+j);\n"+
"	     localci.push(i*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j);\n"+
"	     localci.push(-1);\n"+
"	}\n"+
"    }\n"+
"    coordIndexes = new MFInt32(localci);\n"+
"}\n"+
"\n"+
"function generateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var localc = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta) * Math.cos(h * phi);\n"+
"		localc.push(new SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		));\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     coordinates = new MFVec3f(localc);\n"+
"}\n"+
"\n"+
"function set_fraction(fraction, eventTime) {\n"+
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
"	if (f < 1) {\n"+
"		f = 10;\n"+
"	}\n"+
"	if (g < 1) {\n"+
"		g = 4;\n"+
"	}\n"+
"	if (h < 1) {\n"+
"		h = 4;\n"+
"	}\n"+
"	resolution = 100;\n"+
"	generateCoordinates(resolution);\n"+
"}\n"+
"      ''', ), 
     Script33 = Script(DEF="OrbitScript2",       field34 = field(accessType="inputOnly", name="set_fraction", type="SFFloat"), 
      field35 = field(accessType="outputOnly", name="coordinates", type="MFVec3f"), 
      field36 = field(accessType="outputOnly", name="coordIndexes", type="MFInt32"),       sourceCode = '''\n"+
"\n"+
"ecmascript:\n"+
"\n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"\n"+
"function initialize() {\n"+
"     resolution = 100;\n"+
"     generateCoordinates(resolution);\n"+
"     var localci = [];\n"+
"     for ( i = 0; i < resolution-1; i++) {\n"+
"     	for ( j = 0; j < resolution-1; j++) {\n"+
"	     localci.push(i*resolution+j);\n"+
"	     localci.push(i*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j);\n"+
"	     localci.push(-1);\n"+
"	}\n"+
"    }\n"+
"    coordIndexes = new MFInt32(localci);\n"+
"}\n"+
"\n"+
"function generateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var localc = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta) * Math.cos(h * phi);\n"+
"		localc.push(new SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		));\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     \n"+
"     coordinates = new MFVec3f(localc);\n"+
"}\n"+
"\n"+
"function set_fraction(fraction, eventTime) {\n"+
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
"	if (f < 1) {\n"+
"		f = 10;\n"+
"	}\n"+
"	if (g < 1) {\n"+
"		g = 4;\n"+
"	}\n"+
"	if (h < 1) {\n"+
"		h = 4;\n"+
"	}\n"+
"	resolution = 100;\n"+
"	generateCoordinates(resolution);\n"+
"}\n"+
"      ''', )), 
    ROUTE37 = ROUTE(fromField="coordIndexes", fromNode="OrbitScript", toField="coordIndex", toNode="Orbit"), 
    ROUTE38 = ROUTE(fromField="coordinates", fromNode="OrbitScript", toField="point", toNode="OrbitCoordinates"), 
    ROUTE39 = ROUTE(fromField="fraction_changed", fromNode="Clock", toField="set_fraction", toNode="OrbitScript"), 
    ROUTE40 = ROUTE(fromField="coordIndexes", fromNode="OrbitScript2", toField="coordIndex", toNode="Orbit2"), 
    ROUTE41 = ROUTE(fromField="coordinates", fromNode="OrbitScript2", toField="point", toNode="OrbitCoordinates2"), 
    ROUTE42 = ROUTE(fromField="fraction_changed", fromNode="Clock", toField="set_fraction", toNode="OrbitScript2"), 
    ROUTE43 = ROUTE(fromField="fraction_changed", fromNode="Clock", toField="set_fraction", toNode="OrbitPath"), 
    ROUTE44 = ROUTE(fromField="value_changed", fromNode="OrbitPath", toField="rotation", toNode="OrbitTransform"), 
    ROUTE45 = ROUTE(fromField="value_changed", fromNode="OrbitPath", toField="rotation", toNode="OrbitTransform2")))
