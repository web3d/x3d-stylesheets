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
meta4.content = "flowerproto.x3d"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "creator"
meta5.content = "John Carlson"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "A flower proto with configurable shaders"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "generator"
meta7.content = "X3D-Edit, https://savage.nps.edu/X3D-Edit"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "identifier"
meta8.content = "https://coderextreme.net/X3DJSONLD/flowerproto.x3d"
head1.addMeta([meta8])
X3D0.head = head1

Scene9 = Scene()

ProtoDeclare10 = ProtoDeclare()
ProtoDeclare10.name = "FlowerProto"

ProtoInterface11 = ProtoInterface()

field12 = field()
field12.accessType = "inputOutput"
field12.name = "vertex"
field12.type = "MFString"
field12.value = "\"../shaders/gl_flowers_chromatic.vs\""
ProtoInterface11.addField([field12])

field13 = field()
field13.accessType = "inputOutput"
field13.name = "fragment"
field13.type = "MFString"
field13.value = "\"../shaders/pc_flowers.fs\""
ProtoInterface11.addField([field13])
ProtoDeclare10.protoInterface = ProtoInterface11

ProtoBody14 = ProtoBody()

Transform15 = Transform()
Transform15.DEF = "transform"
Transform15.translation = [0,0,0]

Shape16 = Shape()

Appearance17 = Appearance()

Material18 = Material()
Material18.diffuseColor = [.7,.7,.7]
Appearance17.material = Material18

ComposedCubeMapTexture19 = ComposedCubeMapTexture()
ComposedCubeMapTexture19.DEF = "texture"

ImageTexture20 = ImageTexture()
ImageTexture20.url = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]
ComposedCubeMapTexture19.back = ImageTexture20

ImageTexture21 = ImageTexture()
ImageTexture21.url = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]
ComposedCubeMapTexture19.bottom = ImageTexture21

ImageTexture22 = ImageTexture()
ImageTexture22.url = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]
ComposedCubeMapTexture19.front = ImageTexture22

ImageTexture23 = ImageTexture()
ImageTexture23.url = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]
ComposedCubeMapTexture19.left = ImageTexture23

ImageTexture24 = ImageTexture()
ImageTexture24.url = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]
ComposedCubeMapTexture19.right = ImageTexture24

ImageTexture25 = ImageTexture()
ImageTexture25.url = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]
ComposedCubeMapTexture19.top = ImageTexture25
Appearance17.texture = ComposedCubeMapTexture19

ComposedShader26 = ComposedShader(language = "GLSL")
ComposedShader26.DEF = "shader"

field27 = field()
field27.name = "cube"
field27.type = "SFInt32"
field27.accessType = "inputOutput"
field27.value = "0"
ComposedShader26.addField([field27])
#
#                                <field name='cube' type='SFNode' accessType=\"inputOutput\">
#                                    <ComposedCubeMapTexture USE=\"texture\"/>
#                                </field>
#				

field28 = field()
field28.name = "chromaticDispertion"
field28.type = "SFVec3f"
field28.accessType = "inputOutput"
field28.value = "0.98 1.0 1.033"
ComposedShader26.addField([field28])

field29 = field()
field29.name = "bias"
field29.type = "SFFloat"
field29.accessType = "inputOutput"
field29.value = "10"
ComposedShader26.addField([field29])

field30 = field()
field30.name = "scale"
field30.type = "SFFloat"
field30.accessType = "inputOutput"
field30.value = "10"
ComposedShader26.addField([field30])

field31 = field()
field31.name = "power"
field31.type = "SFFloat"
field31.accessType = "inputOutput"
field31.value = "2.0"
ComposedShader26.addField([field31])

field32 = field()
field32.name = "a"
field32.type = "SFFloat"
field32.accessType = "inputOutput"
field32.value = "3"
ComposedShader26.addField([field32])

field33 = field()
field33.name = "b"
field33.type = "SFFloat"
field33.accessType = "inputOutput"
field33.value = "1"
ComposedShader26.addField([field33])

field34 = field()
field34.name = "c"
field34.type = "SFFloat"
field34.accessType = "inputOutput"
field34.value = "3"
ComposedShader26.addField([field34])

field35 = field()
field35.name = "d"
field35.type = "SFFloat"
field35.accessType = "inputOutput"
field35.value = "3"
ComposedShader26.addField([field35])

field36 = field()
field36.name = "tdelta"
field36.type = "SFFloat"
field36.accessType = "inputOutput"
field36.value = "0.5"
ComposedShader26.addField([field36])

field37 = field()
field37.name = "pdelta"
field37.type = "SFFloat"
field37.accessType = "inputOutput"
field37.value = "0.5"
ComposedShader26.addField([field37])

ShaderPart38 = ShaderPart()
ShaderPart38.type = "VERTEX"

IS39 = IS()

connect40 = connect()
connect40.nodeField = "url"
connect40.protoField = "vertex"
IS39.addConnect([connect40])
ShaderPart38.IS = IS39
ComposedShader26.addParts([ShaderPart38])

ShaderPart41 = ShaderPart()
ShaderPart41.type = "FRAGMENT"

IS42 = IS()

connect43 = connect()
connect43.nodeField = "url"
connect43.protoField = "fragment"
IS42.addConnect([connect43])
ShaderPart41.IS = IS42
ComposedShader26.addParts([ShaderPart41])
Appearance17.addShaders([ComposedShader26])
Shape16.appearance = Appearance17

Sphere44 = Sphere()
Shape16.geometry = Sphere44
Transform15.addChildren([Shape16])

Script45 = Script()
Script45.DEF = "Bounce"

field46 = field()
field46.name = "translation"
field46.accessType = "inputOutput"
field46.type = "SFVec3f"
field46.value = "0 0 0"
Script45.addField([field46])

field47 = field()
field47.name = "velocity"
field47.accessType = "inputOutput"
field47.type = "SFVec3f"
field47.value = "0 0 0"
Script45.addField([field47])

field48 = field()
field48.name = "set_fraction"
field48.accessType = "inputOnly"
field48.type = "SFTime"
Script45.addField([field48])

field49 = field()
field49.name = "a"
field49.type = "SFFloat"
field49.accessType = "inputOutput"
field49.value = "0.5"
Script45.addField([field49])

field50 = field()
field50.name = "b"
field50.type = "SFFloat"
field50.accessType = "inputOutput"
field50.value = "0.5"
Script45.addField([field50])

field51 = field()
field51.name = "c"
field51.type = "SFFloat"
field51.accessType = "inputOutput"
field51.value = "3"
Script45.addField([field51])

field52 = field()
field52.name = "d"
field52.type = "SFFloat"
field52.accessType = "inputOutput"
field52.value = "3"
Script45.addField([field52])

field53 = field()
field53.name = "tdelta"
field53.type = "SFFloat"
field53.accessType = "inputOutput"
field53.value = "0.5"
Script45.addField([field53])

field54 = field()
field54.name = "pdelta"
field54.type = "SFFloat"
field54.accessType = "inputOutput"
field54.value = "0.5"
Script45.addField([field54])

Script45.setSourceCode('''ecmascript:\n"+
"			function initialize() {\n"+
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
"			    for (var j = 0; j <= 2; j++) {\n"+
"				    if (Math.abs(translation.x) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.y) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.z) > 10) {\n"+
"					initialize();\n"+
"				    } else {\n"+
"					velocity.x += Math.random() * 0.2 - 0.1;\n"+
"					velocity.y += Math.random() * 0.2 - 0.1;\n"+
"					velocity.z += Math.random() * 0.2 - 0.1;\n"+
"				    }\n"+
"			    }\n"+
"			    animate_flowers();\n"+
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
"				tdelta += 0.5;\n"+
"				pdelta += 0.5;\n"+
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
"			}\n"+
"\n"+
"''')
Transform15.addChildren([Script45])

TimeSensor55 = TimeSensor()
TimeSensor55.DEF = "TourTime"
TimeSensor55.cycleInterval = 0.150
TimeSensor55.loop = True
Transform15.addChildren([TimeSensor55])

ROUTE56 = ROUTE()
ROUTE56.fromNode = "TourTime"
ROUTE56.fromField = "cycleTime"
ROUTE56.toNode = "Bounce"
ROUTE56.toField = "set_fraction"
Transform15.addChildren([ROUTE56])

ROUTE57 = ROUTE()
ROUTE57.fromNode = "Bounce"
ROUTE57.fromField = "translation_changed"
ROUTE57.toNode = "transform"
ROUTE57.toField = "set_translation"
Transform15.addChildren([ROUTE57])

ROUTE58 = ROUTE()
ROUTE58.fromNode = "Bounce"
ROUTE58.fromField = "a"
ROUTE58.toNode = "shader"
ROUTE58.toField = "a"
Transform15.addChildren([ROUTE58])

ROUTE59 = ROUTE()
ROUTE59.fromNode = "Bounce"
ROUTE59.fromField = "b"
ROUTE59.toNode = "shader"
ROUTE59.toField = "b"
Transform15.addChildren([ROUTE59])

ROUTE60 = ROUTE()
ROUTE60.fromNode = "Bounce"
ROUTE60.fromField = "c"
ROUTE60.toNode = "shader"
ROUTE60.toField = "c"
Transform15.addChildren([ROUTE60])

ROUTE61 = ROUTE()
ROUTE61.fromNode = "Bounce"
ROUTE61.fromField = "d"
ROUTE61.toNode = "shader"
ROUTE61.toField = "d"
Transform15.addChildren([ROUTE61])

ROUTE62 = ROUTE()
ROUTE62.fromNode = "Bounce"
ROUTE62.fromField = "tdelta"
ROUTE62.toNode = "shader"
ROUTE62.toField = "tdelta"
Transform15.addChildren([ROUTE62])

ROUTE63 = ROUTE()
ROUTE63.fromNode = "Bounce"
ROUTE63.fromField = "pdelta"
ROUTE63.toNode = "shader"
ROUTE63.toField = "pdelta"
Transform15.addChildren([ROUTE63])
ProtoBody14.addChildren([Transform15])
ProtoDeclare10.protoBody = ProtoBody14
Scene9.addChildren([ProtoDeclare10])
X3D0.scene = Scene9
