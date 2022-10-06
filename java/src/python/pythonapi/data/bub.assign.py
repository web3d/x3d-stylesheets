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
meta4.content = "bub.x3d"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "creator"
meta5.content = "John Carlson"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "3 prismatic spheres"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "generator"
meta7.content = "X3D-Edit, https://savage.nps.edu/X3D-Edit"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "identifier"
meta8.content = "https://coderextreme.net/X3DJSONLD/bub.x3d"
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

Viewpoint12 = Viewpoint()
Viewpoint12.position = [0,0,20]
Viewpoint12.description = "Look at the bubbles flying"
Scene9.addChildren([Viewpoint12])

ProtoDeclare13 = ProtoDeclare()
ProtoDeclare13.name = "Bubble"

ProtoBody14 = ProtoBody()

Transform15 = Transform()
Transform15.DEF = "transform"
Transform15.translation = [0,0,0]

Shape16 = Shape()
Shape16.DEF = "myShape"

Appearance17 = Appearance()

Material18 = Material()
Material18.diffuseColor = [.7,.7,.7]
Material18.specularColor = [.5,.5,.5]
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
#
#					<ComposedShader DEF='gl' language=\"GLSL\">
#					  <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/>
#					  <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/>
#					  <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/>
#
#					  <ShaderPart url='\"../shaders/gl.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/gl.vs\"' type='VERTEX'></ShaderPart>
#					  <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart>
#					</ComposedShader>
#					<ComposedShader DEF='freewrl' language=\"GLSL\">
#					  <field name='fw_textureCoodGenType' type='SFInt32' accessType=\"inputOutput\" value='0'/>
#					  <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/>
#					  <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/>
#
#					  <ShaderPart url='\"../shaders/freewrl.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/freewrl.vs\"' type='VERTEX'></ShaderPart>
#					  <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart>
#					</ComposedShader>
#					

ComposedShader26 = ComposedShader(language = "GLSL")
ComposedShader26.DEF = "x3dom"

field27 = field()
field27.name = "cube"
field27.type = "SFInt32"
field27.accessType = "inputOutput"
field27.value = "0"
ComposedShader26.addField([field27])

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
field29.value = "0.5"
ComposedShader26.addField([field29])

field30 = field()
field30.name = "scale"
field30.type = "SFFloat"
field30.accessType = "inputOutput"
field30.value = "0.5"
ComposedShader26.addField([field30])

field31 = field()
field31.name = "power"
field31.type = "SFFloat"
field31.accessType = "inputOutput"
field31.value = "2.0"
ComposedShader26.addField([field31])

ShaderPart32 = ShaderPart()
ShaderPart32.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]
ShaderPart32.type = "VERTEX"
ComposedShader26.addParts([ShaderPart32])

ShaderPart33 = ShaderPart()
ShaderPart33.url = ["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]
ShaderPart33.type = "FRAGMENT"
ComposedShader26.addParts([ShaderPart33])
Appearance17.addShaders([ComposedShader26])
#
#					<ComposedShader DEF='instant' language=\"GLSL\">
#					  <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/>
#					  <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/>
#					  <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/>
#
#                              <ShaderPart url='\"../shaders/instant.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/instant.vs\"' type='VERTEX'></ShaderPart>
#                              <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart>
#                            </ComposedShader>
#                            

ComposedShader34 = ComposedShader(language = "GLSL")
ComposedShader34.DEF = "cobweb"

field35 = field()
field35.name = "cube"
field35.type = "SFNode"
field35.accessType = "inputOutput"

ComposedCubeMapTexture36 = ComposedCubeMapTexture()
ComposedCubeMapTexture36.USE = "texture"
field35.addChildren([ComposedCubeMapTexture36])
ComposedShader34.addField([field35])

field37 = field()
field37.name = "chromaticDispertion"
field37.type = "SFVec3f"
field37.accessType = "inputOutput"
field37.value = "0.98 1.0 1.033"
ComposedShader34.addField([field37])

field38 = field()
field38.name = "bias"
field38.type = "SFFloat"
field38.accessType = "inputOutput"
field38.value = "0.5"
ComposedShader34.addField([field38])

field39 = field()
field39.name = "scale"
field39.type = "SFFloat"
field39.accessType = "inputOutput"
field39.value = "0.5"
ComposedShader34.addField([field39])

field40 = field()
field40.name = "power"
field40.type = "SFFloat"
field40.accessType = "inputOutput"
field40.value = "2.0"
ComposedShader34.addField([field40])

ShaderPart41 = ShaderPart()
ShaderPart41.url = ["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]
ShaderPart41.type = "VERTEX"
ComposedShader34.addParts([ShaderPart41])

ShaderPart42 = ShaderPart()
ShaderPart42.url = ["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc.fs"]
ShaderPart42.type = "FRAGMENT"
ComposedShader34.addParts([ShaderPart42])
Appearance17.addShaders([ComposedShader34])
Shape16.appearance = Appearance17

Sphere43 = Sphere()
Shape16.geometry = Sphere43
Transform15.addChildren([Shape16])
ProtoBody14.addChildren([Transform15])

Script44 = Script()
Script44.DEF = "Bounce"

field45 = field()
field45.name = "translation"
field45.accessType = "inputOutput"
field45.type = "SFVec3f"
field45.value = "0 0 0"
Script44.addField([field45])

field46 = field()
field46.name = "velocity"
field46.accessType = "inputOutput"
field46.type = "SFVec3f"
field46.value = "0 0 0"
Script44.addField([field46])

field47 = field()
field47.name = "set_fraction"
field47.accessType = "inputOnly"
field47.type = "SFTime"
Script44.addField([field47])

Script44.setSourceCode('''ecmascript:\n"+
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
"			    if (Math.abs(translation.x) > 10) {\n"+
"				initialize();\n"+
"			    } else if (Math.abs(translation.y) > 10) {\n"+
"				initialize();\n"+
"			    } else if (Math.abs(translation.z) > 10) {\n"+
"				initialize();\n"+
"			    } else {\n"+
"				velocity.x += Math.random() * 0.2 - 0.1;\n"+
"				velocity.y += Math.random() * 0.2 - 0.1;\n"+
"				velocity.z += Math.random() * 0.2 - 0.1;\n"+
"			    }\n"+
"			}\n"+
"               ''')
ProtoBody14.addChildren([Script44])

TimeSensor48 = TimeSensor()
TimeSensor48.DEF = "TourTime"
TimeSensor48.cycleInterval = 0.150
TimeSensor48.loop = True
ProtoBody14.addChildren([TimeSensor48])

ROUTE49 = ROUTE()
ROUTE49.fromNode = "TourTime"
ROUTE49.fromField = "cycleTime"
ROUTE49.toNode = "Bounce"
ROUTE49.toField = "set_fraction"
ProtoBody14.addChildren([ROUTE49])

ROUTE50 = ROUTE()
ROUTE50.fromNode = "Bounce"
ROUTE50.fromField = "translation_changed"
ROUTE50.toNode = "transform"
ROUTE50.toField = "set_translation"
ProtoBody14.addChildren([ROUTE50])
ProtoDeclare13.protoBody = ProtoBody14
Scene9.addChildren([ProtoDeclare13])

ProtoInstance51 = ProtoInstance()
ProtoInstance51.name = "Bubble"
Scene9.addChildren([ProtoInstance51])

ProtoInstance52 = ProtoInstance()
ProtoInstance52.name = "Bubble"
Scene9.addChildren([ProtoInstance52])

ProtoInstance53 = ProtoInstance()
ProtoInstance53.name = "Bubble"
Scene9.addChildren([ProtoInstance53])
X3D0.scene = Scene9
