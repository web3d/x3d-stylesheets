from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

component2 = component()
component2.name = "EnvironmentalEffects"
component2.level = 1
head1.addComponent([component2])

component3 = component()
component3.name = "EnvironmentalEffects"
component3.level = 3
head1.addComponent([component3])

component4 = component()
component4.name = "Shaders"
component4.level = 1
head1.addComponent([component4])

component5 = component()
component5.name = "CubeMapTexturing"
component5.level = 1
head1.addComponent([component5])

meta6 = meta()
meta6.name = "title"
meta6.content = "bubbles.x3d"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "creator"
meta7.content = "John Carlson"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "generator"
meta8.content = "manual"
head1.addMeta([meta8])

meta9 = meta()
meta9.name = "identifier"
meta9.content = "https://coderextreme.net/X3DJSONLD/bubbles.x3d"
head1.addMeta([meta9])

meta10 = meta()
meta10.name = "description"
meta10.content = "not sure what this is"
head1.addMeta([meta10])
X3D0.head = head1

Scene11 = Scene()

NavigationInfo12 = NavigationInfo()
NavigationInfo12.type = ["EXAMINE"]
Scene11.addChildren([NavigationInfo12])

Viewpoint13 = Viewpoint()
Viewpoint13.DEF = "Tour"
Viewpoint13.description = "Tour Views"
Scene11.addChildren([Viewpoint13])

Viewpoint14 = Viewpoint()
Viewpoint14.position = [0,0,4]
Viewpoint14.description = "sphere in road"
Scene11.addChildren([Viewpoint14])

Background15 = Background()
Background15.backUrl = ["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"]
Background15.bottomUrl = ["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"]
Background15.frontUrl = ["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"]
Background15.leftUrl = ["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"]
Background15.rightUrl = ["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"]
Background15.topUrl = ["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"]
Scene11.addChildren([Background15])

Transform16 = Transform()
Transform16.DEF = "Rose01"

Shape17 = Shape()

Sphere18 = Sphere()
Shape17.geometry = Sphere18

Appearance19 = Appearance()
Appearance19.DEF = "_01_-_Default"

Material20 = Material()
Material20.diffuseColor = [0.7,0.7,0.7]
Material20.specularColor = [0.5,0.5,0.5]
Appearance19.material = Material20

ComposedCubeMapTexture21 = ComposedCubeMapTexture()

ImageTexture22 = ImageTexture()
ImageTexture22.url = ["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"]
ComposedCubeMapTexture21.back = ImageTexture22

ImageTexture23 = ImageTexture()
ImageTexture23.url = ["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"]
ComposedCubeMapTexture21.bottom = ImageTexture23

ImageTexture24 = ImageTexture()
ImageTexture24.url = ["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"]
ComposedCubeMapTexture21.front = ImageTexture24

ImageTexture25 = ImageTexture()
ImageTexture25.url = ["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"]
ComposedCubeMapTexture21.left = ImageTexture25

ImageTexture26 = ImageTexture()
ImageTexture26.url = ["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"]
ComposedCubeMapTexture21.right = ImageTexture26

ImageTexture27 = ImageTexture()
ImageTexture27.url = ["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"]
ComposedCubeMapTexture21.top = ImageTexture27
Appearance19.texture = ComposedCubeMapTexture21

ComposedShader28 = ComposedShader(language = "GLSL")
ComposedShader28.DEF = "cobweb"

field29 = field()
field29.name = "cube"
field29.accessType = "inputOutput"
field29.type = "SFInt32"
field29.value = "0"
ComposedShader28.addField([field29])

field30 = field()
field30.name = "chromaticDispertion"
field30.accessType = "inputOutput"
field30.type = "SFVec3f"
field30.value = "0.98 1 1.033"
ComposedShader28.addField([field30])

field31 = field()
field31.name = "bias"
field31.accessType = "inputOutput"
field31.type = "SFFloat"
field31.value = "0.5"
ComposedShader28.addField([field31])

field32 = field()
field32.name = "scale"
field32.accessType = "inputOutput"
field32.type = "SFFloat"
field32.value = "0.5"
ComposedShader28.addField([field32])

field33 = field()
field33.name = "power"
field33.accessType = "inputOutput"
field33.type = "SFFloat"
field33.value = "2"
ComposedShader28.addField([field33])

ShaderPart34 = ShaderPart()
ShaderPart34.url = ["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]
ShaderPart34.type = "VERTEX"
ComposedShader28.parts = ShaderPart34

ShaderPart35 = ShaderPart()
ShaderPart35.url = ["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]
ShaderPart35.type = "FRAGMENT"
ComposedShader28.parts = ShaderPart35
Appearance19.shaders = ComposedShader28

ComposedShader36 = ComposedShader(language = "GLSL")
ComposedShader36.DEF = "x3dom"

field37 = field()
field37.name = "cube"
field37.accessType = "inputOutput"
field37.type = "SFInt32"
field37.value = "0"
ComposedShader36.addField([field37])

field38 = field()
field38.name = "chromaticDispertion"
field38.accessType = "inputOutput"
field38.type = "SFVec3f"
field38.value = "0.98 1 1.033"
ComposedShader36.addField([field38])

field39 = field()
field39.name = "bias"
field39.accessType = "inputOutput"
field39.type = "SFFloat"
field39.value = "0.5"
ComposedShader36.addField([field39])

field40 = field()
field40.name = "scale"
field40.accessType = "inputOutput"
field40.type = "SFFloat"
field40.value = "0.5"
ComposedShader36.addField([field40])

field41 = field()
field41.name = "power"
field41.accessType = "inputOutput"
field41.type = "SFFloat"
field41.value = "2"
ComposedShader36.addField([field41])

ShaderPart42 = ShaderPart()
ShaderPart42.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]
ShaderPart42.type = "VERTEX"
ComposedShader36.parts = ShaderPart42

ShaderPart43 = ShaderPart()
ShaderPart43.url = ["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]
ShaderPart43.type = "FRAGMENT"
ComposedShader36.parts = ShaderPart43
Appearance19.shaders = ComposedShader36
Shape17.appearance = Appearance19
Transform16.addChildren([Shape17])
Scene11.addChildren([Transform16])

TimeSensor44 = TimeSensor()
TimeSensor44.DEF = "TourTime"
TimeSensor44.cycleInterval = 5
TimeSensor44.loop = True
Scene11.addChildren([TimeSensor44])

PositionInterpolator45 = PositionInterpolator()
PositionInterpolator45.DEF = "TourPosition"
PositionInterpolator45.key = [0,1]
PositionInterpolator45.keyValue = [0,0,10,0,0,-10]
Scene11.addChildren([PositionInterpolator45])

OrientationInterpolator46 = OrientationInterpolator()
OrientationInterpolator46.DEF = "TourOrientation"
OrientationInterpolator46.key = [0,1]
OrientationInterpolator46.keyValue = [0,1,0,0,0,1,0,3.1416]
Scene11.addChildren([OrientationInterpolator46])

Script47 = Script()
Script47.DEF = "RandomTourTime"

field48 = field()
field48.name = "set_cycle"
field48.accessType = "inputOnly"
field48.type = "SFTime"
Script47.addField([field48])

field49 = field()
field49.name = "lastKey"
field49.accessType = "inputOutput"
field49.type = "SFFloat"
field49.value = "0"
Script47.addField([field49])

field50 = field()
field50.name = "orientations"
field50.accessType = "inputOutput"
field50.type = "MFRotation"
field50.value = "0 1 0 0 0 1 0 -1.57 0 1 0 3.14 0 1 0 1.57 0 1 0 0 1 0 0 -1.57 0 1 0 0 1 0 0 1.57 0 1 0 0"
Script47.addField([field50])

field51 = field()
field51.name = "positions"
field51.accessType = "inputOutput"
field51.type = "MFVec3f"
field51.value = "0 0 10 -10 0 0 0 0 -10 10 0 0 0 0 10 0 10 0 0 0 10 0 -10 0 0 0 10"
Script47.addField([field51])

field52 = field()
field52.name = "position_changed"
field52.accessType = "outputOnly"
field52.type = "MFVec3f"
Script47.addField([field52])

field53 = field()
field53.name = "set_orientation"
field53.accessType = "inputOnly"
field53.type = "MFRotation"
Script47.addField([field53])

field54 = field()
field54.name = "orientation_changed"
field54.accessType = "outputOnly"
field54.type = "MFRotation"
Script47.addField([field54])

Script47.setSourceCode('''ecmascript:\n"+
"               function set_cycle(value) {\n"+
"                        var ov = lastKey;\n"+
"                        do {\n"+
"                            lastKey = Math.round(Math.random()*(positions.length-1));\n"+
"                        } while (lastKey === ov);\n"+
"                        var vc = lastKey;\n"+
"                        \n"+
"                        orientation_changed = new MFRotation();\n"+
"                        orientation_changed[0] = new SFRotation(orientations[ov].x, orientations[ov].y, orientations[ov].z, orientations[ov].w);\n"+
"                        orientation_changed[1] = new SFRotation(orientations[vc].x, orientations[vc].y, orientations[vc].z, orientations[vc].w);\n"+
"                        position_changed = new MFVec3f();\n"+
"                        position_changed[0] = new SFVec3f(positions[ov].x,positions[ov].y,positions[ov].z);\n"+
"                        position_changed[1] = new SFVec3f(positions[vc].x,positions[vc].y,positions[vc].z);\n"+
"                    // }\n"+
"               }''')
Scene11.addChildren([Script47])

ROUTE55 = ROUTE()
ROUTE55.fromNode = "TourTime"
ROUTE55.fromField = "cycleTime_changed"
ROUTE55.toNode = "RandomTourTime"
ROUTE55.toField = "set_cycle"
Scene11.addChildren([ROUTE55])

ROUTE56 = ROUTE()
ROUTE56.fromNode = "RandomTourTime"
ROUTE56.fromField = "orientation_changed"
ROUTE56.toNode = "TourOrientation"
ROUTE56.toField = "set_keyValue"
Scene11.addChildren([ROUTE56])

ROUTE57 = ROUTE()
ROUTE57.fromNode = "RandomTourTime"
ROUTE57.fromField = "position_changed"
ROUTE57.toNode = "TourPosition"
ROUTE57.toField = "set_keyValue"
Scene11.addChildren([ROUTE57])

ROUTE58 = ROUTE()
ROUTE58.fromNode = "TourTime"
ROUTE58.fromField = "fraction_changed"
ROUTE58.toNode = "TourOrientation"
ROUTE58.toField = "set_fraction"
Scene11.addChildren([ROUTE58])

ROUTE59 = ROUTE()
ROUTE59.fromNode = "TourOrientation"
ROUTE59.fromField = "value_changed"
ROUTE59.toNode = "Tour"
ROUTE59.toField = "set_orientation"
Scene11.addChildren([ROUTE59])

ROUTE60 = ROUTE()
ROUTE60.fromNode = "TourTime"
ROUTE60.fromField = "fraction_changed"
ROUTE60.toNode = "TourPosition"
ROUTE60.toField = "set_fraction"
Scene11.addChildren([ROUTE60])

ROUTE61 = ROUTE()
ROUTE61.fromNode = "TourPosition"
ROUTE61.fromField = "value_changed"
ROUTE61.toNode = "Tour"
ROUTE61.toField = "set_position"
Scene11.addChildren([ROUTE61])
X3D0.scene = Scene11
