from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

Scene1 = Scene()

NavigationInfo2 = NavigationInfo()
NavigationInfo2.type = ["EXAMINE","ANY"]
Scene1.addChildren([NavigationInfo2])

DirectionalLight3 = DirectionalLight()
DirectionalLight3.direction = [0,-0.8,-0.2]
DirectionalLight3.intensity = 0.5
Scene1.addChildren([DirectionalLight3])

Background4 = Background()
Background4.skyColor = [1.000,1.000,1.000]
Scene1.addChildren([Background4])

Viewpoint5 = Viewpoint()
Viewpoint5.description = "One mathematical orbital"
Viewpoint5.position = [0,0,50]
Scene1.addChildren([Viewpoint5])

Transform6 = Transform()
Transform6.translation = [0,-1,1]
Transform6.rotation = [0,1,0,3.1415926]
Transform6.scale = [1.5,1.5,1.5]

Shape7 = Shape()

Appearance8 = Appearance()

Material9 = Material()
Material9.transparency = 0.1
Material9.diffuseColor = [0.9,0.3,0.3]
Material9.specularColor = [0.8,0.8,0.8]
Material9.shininess = 0.145
Appearance8.material = Material9
Shape7.appearance = Appearance8

IndexedFaceSet10 = IndexedFaceSet(ccw = False, convex = False, coordIndex = [0,1,2,-1], creaseAngle = 0, solid = True)
IndexedFaceSet10.DEF = "ifs"

Coordinate11 = Coordinate()
Coordinate11.DEF = "crd"
Coordinate11.point = [0,0,1,0,1,0,1,0,0]
IndexedFaceSet10.coord = Coordinate11
Shape7.geometry = IndexedFaceSet10
Transform6.addChildren([Shape7])
Scene1.addChildren([Transform6])

Script12 = Script()
Script12.DEF = "FlowerScript"

field13 = field()
field13.accessType = "inputOnly"
field13.name = "set_fraction"
field13.type = "SFFloat"
Script12.addField([field13])

field14 = field()
field14.accessType = "outputOnly"
field14.name = "coordinates"
field14.type = "MFVec3f"
Script12.addField([field14])

field15 = field()
field15.accessType = "outputOnly"
field15.name = "coordIndexes"
field15.type = "MFInt32"
Script12.addField([field15])

Script12.setSourceCode('''ecmascript:\n"+
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
"''')
Scene1.addChildren([Script12])

TimeSensor16 = TimeSensor()
TimeSensor16.DEF = "Clock"
TimeSensor16.cycleInterval = 16
TimeSensor16.loop = True
Scene1.addChildren([TimeSensor16])

ROUTE17 = ROUTE()
ROUTE17.fromNode = "FlowerScript"
ROUTE17.fromField = "coordIndexes"
ROUTE17.toNode = "ifs"
ROUTE17.toField = "coordIndex"
Scene1.addChildren([ROUTE17])

ROUTE18 = ROUTE()
ROUTE18.fromNode = "FlowerScript"
ROUTE18.fromField = "coordinates"
ROUTE18.toNode = "crd"
ROUTE18.toField = "point"
Scene1.addChildren([ROUTE18])

ROUTE19 = ROUTE()
ROUTE19.fromNode = "Clock"
ROUTE19.fromField = "fraction_changed"
ROUTE19.toNode = "FlowerScript"
ROUTE19.toField = "set_fraction"
Scene1.addChildren([ROUTE19])
X3D0.scene = Scene1
