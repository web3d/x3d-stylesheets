from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "cobweb.x3d"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "creator"
meta3.content = "John Carlson"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "description"
meta4.content = "Tour around a prismatic sphere"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "generator"
meta5.content = "X3D-Edit, https://savage.nps.edu/X3D-Edit"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "identifier"
meta6.content = "https://coderextreme.net/X3DJSONLD/cobweb.x3d"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

NavigationInfo8 = NavigationInfo()
NavigationInfo8.type = ["EXAMINE"]
Scene7.addChildren([NavigationInfo8])

Viewpoint9 = Viewpoint()
Viewpoint9.position = [0,0,4]
Viewpoint9.orientation = [1,0,0,0]
Viewpoint9.description = "Bubbles in action"
Scene7.addChildren([Viewpoint9])

Background10 = Background()
Background10.backUrl = ["../resources/images/BK.png","https://coderextreme.net/X3DJSONLD/images/BK.png"]
Background10.bottomUrl = ["../resources/images/BT.png","https://coderextreme.net/X3DJSONLD/images/BT.png"]
Background10.frontUrl = ["../resources/images/FR.png","https://coderextreme.net/X3DJSONLD/images/FR.png"]
Background10.leftUrl = ["../resources/images/LF.png","https://coderextreme.net/X3DJSONLD/images/LF.png"]
Background10.rightUrl = ["../resources/images/RT.png","https://coderextreme.net/X3DJSONLD/images/RT.png"]
Background10.topUrl = ["../resources/images/TP.png","https://coderextreme.net/X3DJSONLD/images/TP.png"]
Scene7.addChildren([Background10])

ProtoDeclare11 = ProtoDeclare()
ProtoDeclare11.name = "Bubble"

ProtoBody12 = ProtoBody()

Transform13 = Transform()
Transform13.DEF = "transform"

Shape14 = Shape()

Sphere15 = Sphere(radius = 0.25)
Shape14.geometry = Sphere15

Appearance16 = Appearance()

Material17 = Material()
Material17.diffuseColor = [1,0,0]
Material17.transparency = 0.2
Appearance16.material = Material17
Shape14.appearance = Appearance16
Transform13.addChildren([Shape14])

Script18 = Script()
Script18.DEF = "bounce"

field19 = field()
field19.name = "scale"
field19.accessType = "inputOutput"
field19.type = "SFVec3f"
field19.value = "1 1 1"
Script18.addField([field19])

field20 = field()
field20.name = "translation"
field20.accessType = "inputOutput"
field20.type = "SFVec3f"
field20.value = "0 0 0"
Script18.addField([field20])

field21 = field()
field21.name = "velocity"
field21.accessType = "inputOutput"
field21.type = "SFVec3f"
field21.value = "0 0 0"
Script18.addField([field21])

field22 = field()
field22.name = "scalvel"
field22.accessType = "inputOutput"
field22.type = "SFVec3f"
field22.value = "0 0 0"
Script18.addField([field22])

field23 = field()
field23.name = "set_fraction"
field23.accessType = "inputOnly"
field23.type = "SFFloat"
Script18.addField([field23])

Script18.setSourceCode('''ecmascript:\n"+
"function initialize() {\n"+
"    velocity = new SFVec3f(Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125);\n"+
"\n"+
"    scalvel = new SFVec3f(Math.random() * 0.4, Math.random() * 0.4, Math.random() * 0.4);\n"+
"}\n"+
"\n"+
"function set_fraction(value) {\n"+
"    translation = new SFVec3f(	translation.x + velocity.x, translation.y + velocity.y, translation.z + velocity.z);\n"+
"    scale = new SFVec3f(scale.x + scalvel.x, scale.y + scalvel.y, scale.z + scalvel.z);\n"+
"    // if you get to far away or too big, explode\n"+
"    if ( Math.abs(translation.x) > 256) {\n"+
"	translation.x = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if ( Math.abs(translation.y) > 256) {\n"+
"	translation.y = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if ( Math.abs(translation.z) > 256) {\n"+
"	translation.z = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.x) > 20) {\n"+
"	scale.x = scale.x/20;\n"+
"	translation.x = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.y) > 20) {\n"+
"	scale.y = scale.y/20;\n"+
"	translation.y = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.z) > 20) {\n"+
"	scale.z = scale.z/20;\n"+
"	translation.z = 0;\n"+
"	initialize();\n"+
"    }\n"+
"}\n"+
"''')
Transform13.addChildren([Script18])

TimeSensor24 = TimeSensor()
TimeSensor24.DEF = "bubbleClock"
TimeSensor24.cycleInterval = 10
TimeSensor24.loop = True
Transform13.addChildren([TimeSensor24])

ROUTE25 = ROUTE()
ROUTE25.fromNode = "bounce"
ROUTE25.fromField = "translation_changed"
ROUTE25.toNode = "transform"
ROUTE25.toField = "set_translation"
Transform13.addChildren([ROUTE25])

ROUTE26 = ROUTE()
ROUTE26.fromNode = "bounce"
ROUTE26.fromField = "scale_changed"
ROUTE26.toNode = "transform"
ROUTE26.toField = "set_scale"
Transform13.addChildren([ROUTE26])

ROUTE27 = ROUTE()
ROUTE27.fromNode = "bubbleClock"
ROUTE27.fromField = "fraction_changed"
ROUTE27.toNode = "bounce"
ROUTE27.toField = "set_fraction"
Transform13.addChildren([ROUTE27])
ProtoBody12.addChildren([Transform13])
ProtoDeclare11.protoBody = ProtoBody12
Scene7.addChildren([ProtoDeclare11])

ProtoInstance28 = ProtoInstance()
ProtoInstance28.name = "Bubble"
ProtoInstance28.DEF = "bubbleA"
Scene7.addChildren([ProtoInstance28])

ProtoInstance29 = ProtoInstance()
ProtoInstance29.name = "Bubble"
ProtoInstance29.DEF = "bubbleB"
Scene7.addChildren([ProtoInstance29])

ProtoInstance30 = ProtoInstance()
ProtoInstance30.name = "Bubble"
ProtoInstance30.DEF = "bubbleC"
Scene7.addChildren([ProtoInstance30])

ProtoInstance31 = ProtoInstance()
ProtoInstance31.name = "Bubble"
ProtoInstance31.DEF = "bubbleD"
Scene7.addChildren([ProtoInstance31])
X3D0.scene = Scene7
