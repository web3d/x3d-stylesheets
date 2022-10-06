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
meta4.content = "flowers.x3d"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "creator"
meta5.content = "John Carlson"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "5 or more prismatic flowers"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "generator"
meta7.content = "X3D-Edit, https://savage.nps.edu/X3D-Edit"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "identifier"
meta8.content = "https://coderextreme.net/X3DJSONLD/flowers.x3d"
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

ProtoDeclare12 = ProtoDeclare()
ProtoDeclare12.name = "flower"

ProtoBody13 = ProtoBody()

Transform14 = Transform()
Transform14.DEF = "transform"
Transform14.translation = [0,0,0]

Shape15 = Shape()

Appearance16 = Appearance()

Material17 = Material()
Material17.diffuseColor = [.7,.7,.7]
Material17.specularColor = [.5,.5,.5]
Appearance16.material = Material17

ComposedCubeMapTexture18 = ComposedCubeMapTexture()
ComposedCubeMapTexture18.DEF = "texture"

ImageTexture19 = ImageTexture()
ImageTexture19.url = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]
ComposedCubeMapTexture18.back = ImageTexture19

ImageTexture20 = ImageTexture()
ImageTexture20.url = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]
ComposedCubeMapTexture18.bottom = ImageTexture20

ImageTexture21 = ImageTexture()
ImageTexture21.url = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]
ComposedCubeMapTexture18.front = ImageTexture21

ImageTexture22 = ImageTexture()
ImageTexture22.url = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]
ComposedCubeMapTexture18.left = ImageTexture22

ImageTexture23 = ImageTexture()
ImageTexture23.url = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]
ComposedCubeMapTexture18.right = ImageTexture23

ImageTexture24 = ImageTexture()
ImageTexture24.url = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]
ComposedCubeMapTexture18.top = ImageTexture24
Appearance16.texture = ComposedCubeMapTexture18

ComposedShader25 = ComposedShader(language = "GLSL")

field26 = field()
field26.name = "xxxcube"
field26.type = "SFInt32"
field26.accessType = "inputOutput"
field26.value = "0"
ComposedShader25.addField([field26])

field27 = field()
field27.name = "cube"
field27.type = "SFNode"
field27.accessType = "inputOutput"

ComposedCubeMapTexture28 = ComposedCubeMapTexture()
ComposedCubeMapTexture28.USE = "texture"
field27.addChildren([ComposedCubeMapTexture28])
ComposedShader25.addField([field27])

field29 = field()
field29.name = "chromaticDispertion"
field29.type = "SFVec3f"
field29.accessType = "inputOutput"
field29.value = "0.98 1.0 1.033"
ComposedShader25.addField([field29])

field30 = field()
field30.name = "bias"
field30.type = "SFFloat"
field30.accessType = "inputOutput"
field30.value = "0.5"
ComposedShader25.addField([field30])

field31 = field()
field31.name = "scale"
field31.type = "SFFloat"
field31.accessType = "inputOutput"
field31.value = "0.5"
ComposedShader25.addField([field31])

field32 = field()
field32.name = "power"
field32.type = "SFFloat"
field32.accessType = "inputOutput"
field32.value = "2.0"
ComposedShader25.addField([field32])

ShaderPart33 = ShaderPart()
ShaderPart33.url = ["../shaders/common.vs","https://coderextreme.net/X3DJSONLD/shaders/common.vs"]
ShaderPart33.type = "VERTEX"
ComposedShader25.addParts([ShaderPart33])

ShaderPart34 = ShaderPart()
ShaderPart34.url = ["../shaders/gl_flowers_chromatic.fs","https://coderextreme.net/X3DJSONLD/shaders/gl_flowers_chromatic.fs"]
ShaderPart34.type = "FRAGMENT"
ComposedShader25.addParts([ShaderPart34])
Appearance16.addShaders([ComposedShader25])

ComposedShader35 = ComposedShader(language = "GLSL")

field36 = field()
field36.name = "xxxcube"
field36.type = "SFInt32"
field36.accessType = "inputOutput"
field36.value = "0"
ComposedShader35.addField([field36])

field37 = field()
field37.name = "cube"
field37.type = "SFNode"
field37.accessType = "inputOutput"

ComposedCubeMapTexture38 = ComposedCubeMapTexture()
ComposedCubeMapTexture38.USE = "texture"
field37.addChildren([ComposedCubeMapTexture38])
ComposedShader35.addField([field37])

field39 = field()
field39.name = "chromaticDispertion"
field39.type = "SFVec3f"
field39.accessType = "inputOutput"
field39.value = "0.98 1.0 1.033"
ComposedShader35.addField([field39])

field40 = field()
field40.name = "bias"
field40.type = "SFFloat"
field40.accessType = "inputOutput"
field40.value = "0.5"
ComposedShader35.addField([field40])

field41 = field()
field41.name = "scale"
field41.type = "SFFloat"
field41.accessType = "inputOutput"
field41.value = "0.5"
ComposedShader35.addField([field41])

field42 = field()
field42.name = "power"
field42.type = "SFFloat"
field42.accessType = "inputOutput"
field42.value = "2.0"
ComposedShader35.addField([field42])

ShaderPart43 = ShaderPart()
ShaderPart43.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]
ShaderPart43.type = "VERTEX"
ComposedShader35.addParts([ShaderPart43])

ShaderPart44 = ShaderPart()
ShaderPart44.url = ["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]
ShaderPart44.type = "FRAGMENT"
ComposedShader35.addParts([ShaderPart44])
Appearance16.addShaders([ComposedShader35])

ComposedShader45 = ComposedShader(language = "GLSL")
ComposedShader45.DEF = "shader"

field46 = field()
field46.name = "xxxcube"
field46.type = "SFInt32"
field46.accessType = "inputOutput"
field46.value = "0"
ComposedShader45.addField([field46])

field47 = field()
field47.name = "cube"
field47.type = "SFNode"
field47.accessType = "inputOutput"

ComposedCubeMapTexture48 = ComposedCubeMapTexture()
ComposedCubeMapTexture48.USE = "texture"
field47.addChildren([ComposedCubeMapTexture48])
ComposedShader45.addField([field47])

field49 = field()
field49.name = "chromaticDispertion"
field49.type = "SFVec3f"
field49.accessType = "inputOutput"
field49.value = "0.98 1.0 1.033"
ComposedShader45.addField([field49])

field50 = field()
field50.name = "bias"
field50.type = "SFFloat"
field50.accessType = "inputOutput"
field50.value = "10"
ComposedShader45.addField([field50])

field51 = field()
field51.name = "scale"
field51.type = "SFFloat"
field51.accessType = "inputOutput"
field51.value = "10"
ComposedShader45.addField([field51])

field52 = field()
field52.name = "power"
field52.type = "SFFloat"
field52.accessType = "inputOutput"
field52.value = "2.0"
ComposedShader45.addField([field52])

ShaderPart53 = ShaderPart()
ShaderPart53.url = ["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]
ShaderPart53.type = "VERTEX"
ComposedShader45.addParts([ShaderPart53])

ShaderPart54 = ShaderPart()
ShaderPart54.url = ["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]
ShaderPart54.type = "FRAGMENT"
ComposedShader45.addParts([ShaderPart54])
Appearance16.addShaders([ComposedShader45])
Shape15.appearance = Appearance16
#
#			<Sphere></Sphere>
#			

IndexedFaceSet55 = IndexedFaceSet(convex = False, creaseAngle = 0)
IndexedFaceSet55.DEF = "Orbit"

Coordinate56 = Coordinate()
Coordinate56.DEF = "OrbitCoordinates"
IndexedFaceSet55.coord = Coordinate56
Shape15.geometry = IndexedFaceSet55
Transform14.addChildren([Shape15])
ProtoBody13.addChildren([Transform14])

Script57 = Script()
Script57.DEF = "Bounce"

field58 = field()
field58.name = "translation"
field58.accessType = "inputOutput"
field58.type = "SFVec3f"
field58.value = "0 0 0"
Script57.addField([field58])

field59 = field()
field59.name = "velocity"
field59.accessType = "inputOutput"
field59.type = "SFVec3f"
field59.value = "0 0 0"
Script57.addField([field59])

field60 = field()
field60.name = "set_fraction"
field60.accessType = "inputOnly"
field60.type = "SFTime"
Script57.addField([field60])

field61 = field()
field61.accessType = "inputOutput"
field61.name = "coordinates"
field61.type = "MFVec3f"
Script57.addField([field61])

field62 = field()
field62.accessType = "outputOnly"
field62.name = "coordIndexes"
field62.type = "MFInt32"
Script57.addField([field62])

field63 = field()
field63.name = "a"
field63.type = "SFFloat"
field63.accessType = "inputOutput"
field63.value = "0.5"
Script57.addField([field63])

field64 = field()
field64.name = "b"
field64.type = "SFFloat"
field64.accessType = "inputOutput"
field64.value = "0.5"
Script57.addField([field64])

field65 = field()
field65.name = "c"
field65.type = "SFFloat"
field65.accessType = "inputOutput"
field65.value = "3"
Script57.addField([field65])

field66 = field()
field66.name = "d"
field66.type = "SFFloat"
field66.accessType = "inputOutput"
field66.value = "3"
Script57.addField([field66])

field67 = field()
field67.name = "tdelta"
field67.type = "SFFloat"
field67.accessType = "inputOutput"
field67.value = "0.5"
Script57.addField([field67])

field68 = field()
field68.name = "pdelta"
field68.type = "SFFloat"
field68.accessType = "inputOutput"
field68.value = "0.5"
Script57.addField([field68])

Script57.setSourceCode('''ecmascript:\n"+
"			function newBubble() {\n"+
"			    translation = new SFVec3f(0, 0, 0);\n"+
"			    velocity = new SFVec3f(\n"+
"			    	Math.random() - 0.5,\n"+
"				Math.random() - 0.5,\n"+
"				Math.random() - 0.5);\n"+
"			}\n"+
"			function set_fraction() {\n"+
"			    translation = new SFVec3f(\n"+
"			    	translation.x + velocity.x,\n"+
"				translation.y + velocity.y,\n"+
"				translation.z + velocity.z);\n"+
"			    if (Math.abs(translation.x) > 10) {\n"+
"					newBubble();\n"+
"			    } else if (Math.abs(translation.y) > 10) {\n"+
"					newBubble();\n"+
"			    } else if (Math.abs(translation.z) > 10) {\n"+
"					newBubble();\n"+
"			    } else {\n"+
"					velocity = new SFVec3f(\n"+
"						velocity.x + Math.random() * 0.2 - 0.1,\n"+
"						velocity.y + Math.random() * 0.2 - 0.1,\n"+
"						velocity.z + Math.random() * 0.2 - 0.1\n"+
"					);\n"+
"			    }\n"+
"			    animate_flowers();\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     var cis = [];\n"+
"			     newBubble();\n"+
"			     resolution = 100;\n"+
"			     updateCoordinates(resolution);\n"+
"			     for ( i = 0; i < resolution-1; i++) {\n"+
"				for ( j = 0; j < resolution-1; j++) {\n"+
"				     cis.push(i*resolution+j);\n"+
"				     cis.push(i*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j);\n"+
"				     cis.push(-1);\n"+
"				}\n"+
"			    }\n"+
"			     coordIndexes = new MFInt32(cis);\n"+
"			}\n"+
"\n"+
"			function updateCoordinates(resolution) {\n"+
"			     theta = 0.0;\n"+
"			     phi = 0.0;\n"+
"			     delta = (2 * 3.141592653) / (resolution-1);\n"+
"			     var crds = [];\n"+
"			     for ( i = 0; i < resolution; i++) {\n"+
"				for ( j = 0; j < resolution; j++) {\n"+
"					rho = a + b * Math.cos(c * theta) * Math.cos(d * phi);\n"+
"					crds.push(new SFVec3f(\n"+
"						rho * Math.cos(phi) * Math.cos(theta),\n"+
"						rho * Math.cos(phi) * Math.sin(theta),\n"+
"						rho * Math.sin(phi)\n"+
"					));\n"+
"					theta += delta;\n"+
"				}\n"+
"				phi += delta;\n"+
"				coordinates = new MFVec3f(crds);\n"+
"			     }\n"+
"			}\n"+
"\n"+
"			function animate_flowers(fraction, eventTime) {\n"+
"				choice = Math.floor(Math.random() * 4);\n"+
"				switch (choice) {\n"+
"				case 0:\n"+
"					a += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 1:\n"+
"					b += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 2:\n"+
"					c += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				case 3:\n"+
"					d += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				}\n"+
"				if (a > 1) {\n"+
"					a =  0.5;\n"+
"				}\n"+
"				if (b > 1) {\n"+
"					b =  0.5;\n"+
"				}\n"+
"				if (c < 1) {\n"+
"					c =  4;\n"+
"				}\n"+
"				if (d < 1) {\n"+
"					d =  4;\n"+
"				}\n"+
"				if (c > 10) {\n"+
"					c = 4;\n"+
"				}\n"+
"				if (d > 10) {\n"+
"					d = 4;\n"+
"				}\n"+
"				resolution = 100;\n"+
"				updateCoordinates(resolution);\n"+
"			}\n"+
"\n"+
"''')
ProtoBody13.addChildren([Script57])

TimeSensor69 = TimeSensor()
TimeSensor69.DEF = "TourTime"
TimeSensor69.cycleInterval = 0.150
TimeSensor69.loop = True
ProtoBody13.addChildren([TimeSensor69])

TimeSensor70 = TimeSensor()
TimeSensor70.DEF = "SongTime"
TimeSensor70.loop = True
ProtoBody13.addChildren([TimeSensor70])

Sound71 = Sound()
Sound71.maxBack = 100
Sound71.maxFront = 100
Sound71.minBack = 20
Sound71.minFront = 20

AudioClip72 = AudioClip()
AudioClip72.DEF = "AudioClip"
AudioClip72.description = "Chandubabamusic #1"
AudioClip72.url = ["../resources/chandubabamusic1.wav"]
Sound71.source = AudioClip72
ProtoBody13.addChildren([Sound71])

ROUTE73 = ROUTE()
ROUTE73.fromField = "cycleTime"
ROUTE73.fromNode = "SongTime"
ROUTE73.toField = "startTime"
ROUTE73.toNode = "AudioClip"
ProtoBody13.addChildren([ROUTE73])

ROUTE74 = ROUTE()
ROUTE74.fromNode = "TourTime"
ROUTE74.fromField = "cycleTime"
ROUTE74.toNode = "Bounce"
ROUTE74.toField = "set_fraction"
ProtoBody13.addChildren([ROUTE74])

ROUTE75 = ROUTE()
ROUTE75.fromNode = "Bounce"
ROUTE75.fromField = "translation"
ROUTE75.toNode = "transform"
ROUTE75.toField = "set_translation"
ProtoBody13.addChildren([ROUTE75])
#
#		<ROUTE fromField=\"coordIndexes\" fromNode=\"Bounce\" toField=\"set_coordIndex\" toNode=\"Orbit\"/>
#		<ROUTE fromField=\"coordinates\" fromNode=\"Bounce\" toField=\"set_point\" toNode=\"OrbitCoordinates\"/>
#		
ProtoDeclare12.protoBody = ProtoBody13
Scene9.addChildren([ProtoDeclare12])

Transform76 = Transform()

ProtoInstance77 = ProtoInstance()
ProtoInstance77.name = "flower"
Transform76.addChildren([ProtoInstance77])
#
#            <ProtoInstance name=\"flower\"/>
#            <ProtoInstance name=\"flower\"/>
#	    
Scene9.addChildren([Transform76])
X3D0.scene = Scene9
