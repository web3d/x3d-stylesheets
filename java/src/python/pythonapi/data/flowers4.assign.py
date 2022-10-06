from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

component2 = component()
component2.name = "Shaders"
component2.level = 1
head1.addComponent([component2])

component3 = component()
component3.name = "CubeMapTexturing"
component3.level = 1
head1.addComponent([component3])

meta4 = meta()
meta4.name = "title"
meta4.content = "flowers4.x3d"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "creator"
meta5.content = "John Carlson"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "generator"
meta6.content = "manual"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "identifier"
meta7.content = "https://coderextreme.net/X3DJSONLD/flowers4.x3d"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "description"
meta8.content = "an animated flower"
head1.addMeta([meta8])
X3D0.head = head1

Scene9 = Scene()

NavigationInfo10 = NavigationInfo()
NavigationInfo10.type = ["EXAMINE","ANY"]
Scene9.addChildren([NavigationInfo10])

Background11 = Background()
Background11.backUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]
Background11.bottomUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]
Background11.frontUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]
Background11.leftUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]
Background11.rightUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]
Background11.topUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]
Scene9.addChildren([Background11])

Transform12 = Transform()
Transform12.DEF = "transform"

Shape13 = Shape()

Appearance14 = Appearance()

Material15 = Material()
Material15.diffuseColor = [.7,.7,.7]
Material15.specularColor = [.5,.5,.5]
Appearance14.material = Material15

ComposedCubeMapTexture16 = ComposedCubeMapTexture()

ImageTexture17 = ImageTexture()
ImageTexture17.url = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]
ComposedCubeMapTexture16.back = ImageTexture17

ImageTexture18 = ImageTexture()
ImageTexture18.url = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]
ComposedCubeMapTexture16.bottom = ImageTexture18

ImageTexture19 = ImageTexture()
ImageTexture19.url = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]
ComposedCubeMapTexture16.front = ImageTexture19

ImageTexture20 = ImageTexture()
ImageTexture20.url = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]
ComposedCubeMapTexture16.left = ImageTexture20

ImageTexture21 = ImageTexture()
ImageTexture21.url = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]
ComposedCubeMapTexture16.right = ImageTexture21

ImageTexture22 = ImageTexture()
ImageTexture22.url = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]
ComposedCubeMapTexture16.top = ImageTexture22
Appearance14.texture = ComposedCubeMapTexture16

ComposedShader23 = ComposedShader(language = "GLSL")
ComposedShader23.DEF = "shader"

field24 = field()
field24.name = "cube"
field24.type = "SFInt32"
field24.accessType = "inputOutput"
field24.value = "0"
ComposedShader23.addField([field24])

field25 = field()
field25.name = "chromaticDispertion"
field25.accessType = "inputOutput"
field25.type = "SFVec3f"
field25.value = "0.98 1.0 1.033"
ComposedShader23.addField([field25])

field26 = field()
field26.name = "bias"
field26.type = "SFFloat"
field26.accessType = "inputOutput"
field26.value = "0.5"
ComposedShader23.addField([field26])

field27 = field()
field27.name = "scale"
field27.type = "SFFloat"
field27.accessType = "inputOutput"
field27.value = "0.5"
ComposedShader23.addField([field27])

field28 = field()
field28.name = "power"
field28.type = "SFFloat"
field28.accessType = "inputOutput"
field28.value = "2"
ComposedShader23.addField([field28])

ShaderPart29 = ShaderPart()
ShaderPart29.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]
ShaderPart29.type = "VERTEX"
ComposedShader23.addParts([ShaderPart29])

ShaderPart30 = ShaderPart()
ShaderPart30.url = ["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]
ShaderPart30.type = "FRAGMENT"
ComposedShader23.addParts([ShaderPart30])
Appearance14.addShaders([ComposedShader23])
Shape13.appearance = Appearance14
#
#                <Sphere>
#		

IndexedFaceSet31 = IndexedFaceSet(convex = False, creaseAngle = 0)
IndexedFaceSet31.DEF = "Orbit"

Coordinate32 = Coordinate()
Coordinate32.DEF = "OrbitCoordinates"
IndexedFaceSet31.coord = Coordinate32
Shape13.geometry = IndexedFaceSet31
Transform12.addChildren([Shape13])
Scene9.addChildren([Transform12])

Script33 = Script()
Script33.DEF = "OrbitScript"

field34 = field()
field34.accessType = "inputOnly"
field34.name = "set_fraction"
field34.type = "SFFloat"
Script33.addField([field34])

field35 = field()
field35.accessType = "inputOutput"
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
"     updateCoordinates(resolution);\n"+
"     var cis = [];\n"+
"     for ( i = 0; i < resolution-1; i++) {\n"+
"     	for ( j = 0; j < resolution-1; j++) {\n"+
"	     cis.push(i*resolution+j);\n"+
"	     cis.push(i*resolution+j+1);\n"+
"	     cis.push((i+1)*resolution+j+1);\n"+
"	     cis.push((i+1)*resolution+j);\n"+
"	     cis.push(-1);\n"+
"	}\n"+
"    }\n"+
"    coordIndexes = new MFInt32(cis);\n"+
"}\n"+
"\n"+
"function updateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var crds = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta) * Math.cos(h * phi);\n"+
"		crds.push(new SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		));\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     coordinates = new MFVec3f(crds);\n"+
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
"	updateCoordinates(resolution);\n"+
"}\n"+
"      ''')
Scene9.addChildren([Script33])

TimeSensor37 = TimeSensor()
TimeSensor37.DEF = "Clock"
TimeSensor37.cycleInterval = 16
TimeSensor37.loop = True
Scene9.addChildren([TimeSensor37])

ROUTE38 = ROUTE()
ROUTE38.fromField = "coordIndexes"
ROUTE38.fromNode = "OrbitScript"
ROUTE38.toField = "set_coordIndex"
ROUTE38.toNode = "Orbit"
Scene9.addChildren([ROUTE38])

ROUTE39 = ROUTE()
ROUTE39.fromField = "coordinates"
ROUTE39.fromNode = "OrbitScript"
ROUTE39.toField = "set_point"
ROUTE39.toNode = "OrbitCoordinates"
Scene9.addChildren([ROUTE39])

ROUTE40 = ROUTE()
ROUTE40.fromField = "fraction_changed"
ROUTE40.fromNode = "Clock"
ROUTE40.toField = "set_fraction"
ROUTE40.toNode = "OrbitScript"
Scene9.addChildren([ROUTE40])
X3D0.scene = Scene9
