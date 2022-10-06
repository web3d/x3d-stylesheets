from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.0"

head1 = head()

meta2 = meta()
meta2.content = "title"
meta2.name = "flowers2.x3d"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "John Carlson"
meta3.name = "author"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "John Carlson"
meta4.name = "transcriber"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "23 January 2005"
meta5.name = "created"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "05 May 2017"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "2 random mathematical roses in spherical dimensions. rho = a + b * cos(c * theta) * cos(d * phi)"
meta7.name = "description"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "https://coderextreme.net/x3d/flowers2.x3d"
meta8.name = "url"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "manually written"
meta9.name = "generator"
head1.addMeta([meta9])
X3D0.head = head1

Scene10 = Scene()

NavigationInfo11 = NavigationInfo()
NavigationInfo11.type = ["EXAMINE","ANY"]
Scene10.addChildren([NavigationInfo11])

Viewpoint12 = Viewpoint()
Viewpoint12.description = "Two mathematical orbitals"
Viewpoint12.position = [0,0,50]
Scene10.addChildren([Viewpoint12])

Group13 = Group()

DirectionalLight14 = DirectionalLight()
DirectionalLight14.direction = [1,1,1]
Group13.addChildren([DirectionalLight14])

Transform15 = Transform()
Transform15.DEF = "OrbitTransform"
Transform15.translation = [8,0,0]

Shape16 = Shape()

Appearance17 = Appearance()

Material18 = Material()
Material18.diffuseColor = [0,0.5,1]
Material18.specularColor = [0,0.5,1]
Appearance17.material = Material18
Shape16.appearance = Appearance17

IndexedFaceSet19 = IndexedFaceSet(convex = False, creaseAngle = 0)
IndexedFaceSet19.DEF = "Orbit"

Coordinate20 = Coordinate()
Coordinate20.DEF = "OrbitCoordinates"
IndexedFaceSet19.coord = Coordinate20
Shape16.geometry = IndexedFaceSet19
Transform15.addChildren([Shape16])
Group13.addChildren([Transform15])

Transform21 = Transform()
Transform21.DEF = "OrbitTransform2"
Transform21.translation = [-8,0,0]

Shape22 = Shape()

Appearance23 = Appearance()

Material24 = Material()
Material24.diffuseColor = [1,0.5,0]
Material24.specularColor = [1,0.5,0]
Material24.transparency = 0.75
Appearance23.material = Material24
Shape22.appearance = Appearance23

IndexedFaceSet25 = IndexedFaceSet(creaseAngle = 0)
IndexedFaceSet25.DEF = "Orbit2"

Coordinate26 = Coordinate()
Coordinate26.DEF = "OrbitCoordinates2"
IndexedFaceSet25.coord = Coordinate26
Shape22.geometry = IndexedFaceSet25
Transform21.addChildren([Shape22])
Group13.addChildren([Transform21])

TimeSensor27 = TimeSensor()
TimeSensor27.DEF = "Clock"
TimeSensor27.cycleInterval = 16
TimeSensor27.loop = True
Group13.addChildren([TimeSensor27])

OrientationInterpolator28 = OrientationInterpolator()
OrientationInterpolator28.DEF = "OrbitPath"
OrientationInterpolator28.key = [0.0,0.50,1.0]
OrientationInterpolator28.keyValue = [1.0,0.0,0.0,0.0,1.0,0.0,0.0,3.14,1.0,0.0,0.0,6.28]
Group13.addChildren([OrientationInterpolator28])

Script29 = Script()
Script29.DEF = "OrbitScript"

field30 = field()
field30.accessType = "inputOnly"
field30.name = "set_fraction"
field30.type = "SFFloat"
Script29.addField([field30])

field31 = field()
field31.accessType = "outputOnly"
field31.name = "coordinates"
field31.type = "MFVec3f"
Script29.addField([field31])

field32 = field()
field32.accessType = "outputOnly"
field32.name = "coordIndexes"
field32.type = "MFInt32"
Script29.addField([field32])

Script29.setSourceCode('''\n"+
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
"      ''')
Group13.addChildren([Script29])

Script33 = Script()
Script33.DEF = "OrbitScript2"

field34 = field()
field34.accessType = "inputOnly"
field34.name = "set_fraction"
field34.type = "SFFloat"
Script33.addField([field34])

field35 = field()
field35.accessType = "outputOnly"
field35.name = "coordinates"
field35.type = "MFVec3f"
Script33.addField([field35])

field36 = field()
field36.accessType = "outputOnly"
field36.name = "coordIndexes"
field36.type = "MFInt32"
Script33.addField([field36])

Script33.setSourceCode('''\n"+
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
"      ''')
Group13.addChildren([Script33])
Scene10.addChildren([Group13])

ROUTE37 = ROUTE()
ROUTE37.fromField = "coordIndexes"
ROUTE37.fromNode = "OrbitScript"
ROUTE37.toField = "coordIndex"
ROUTE37.toNode = "Orbit"
Scene10.addChildren([ROUTE37])

ROUTE38 = ROUTE()
ROUTE38.fromField = "coordinates"
ROUTE38.fromNode = "OrbitScript"
ROUTE38.toField = "point"
ROUTE38.toNode = "OrbitCoordinates"
Scene10.addChildren([ROUTE38])

ROUTE39 = ROUTE()
ROUTE39.fromField = "fraction_changed"
ROUTE39.fromNode = "Clock"
ROUTE39.toField = "set_fraction"
ROUTE39.toNode = "OrbitScript"
Scene10.addChildren([ROUTE39])

ROUTE40 = ROUTE()
ROUTE40.fromField = "coordIndexes"
ROUTE40.fromNode = "OrbitScript2"
ROUTE40.toField = "coordIndex"
ROUTE40.toNode = "Orbit2"
Scene10.addChildren([ROUTE40])

ROUTE41 = ROUTE()
ROUTE41.fromField = "coordinates"
ROUTE41.fromNode = "OrbitScript2"
ROUTE41.toField = "point"
ROUTE41.toNode = "OrbitCoordinates2"
Scene10.addChildren([ROUTE41])

ROUTE42 = ROUTE()
ROUTE42.fromField = "fraction_changed"
ROUTE42.fromNode = "Clock"
ROUTE42.toField = "set_fraction"
ROUTE42.toNode = "OrbitScript2"
Scene10.addChildren([ROUTE42])

ROUTE43 = ROUTE()
ROUTE43.fromField = "fraction_changed"
ROUTE43.fromNode = "Clock"
ROUTE43.toField = "set_fraction"
ROUTE43.toNode = "OrbitPath"
Scene10.addChildren([ROUTE43])

ROUTE44 = ROUTE()
ROUTE44.fromField = "value_changed"
ROUTE44.fromNode = "OrbitPath"
ROUTE44.toField = "rotation"
ROUTE44.toNode = "OrbitTransform"
Scene10.addChildren([ROUTE44])

ROUTE45 = ROUTE()
ROUTE45.fromField = "value_changed"
ROUTE45.fromNode = "OrbitPath"
ROUTE45.toField = "rotation"
ROUTE45.toNode = "OrbitTransform2"
Scene10.addChildren([ROUTE45])
X3D0.scene = Scene10
