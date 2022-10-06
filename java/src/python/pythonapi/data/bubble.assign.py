from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "bubble.x3d"
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
meta6.content = "https://coderextreme.net/X3DJSONLD/bubble.x3d"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

NavigationInfo8 = NavigationInfo()
NavigationInfo8.type = ["EXAMINE"]
Scene7.addChildren([NavigationInfo8])

Viewpoint9 = Viewpoint()
Viewpoint9.position = [0,0,4]
Viewpoint9.orientation = [1,0,0,0]
Viewpoint9.description = "Bubble in action"
Scene7.addChildren([Viewpoint9])

ProtoDeclare10 = ProtoDeclare()
ProtoDeclare10.name = "Bubble"

ProtoBody11 = ProtoBody()

Transform12 = Transform()
Transform12.DEF = "transform"

Shape13 = Shape()

Sphere14 = Sphere(radius = 0.25)
Shape13.geometry = Sphere14

Appearance15 = Appearance()

Material16 = Material()
Material16.diffuseColor = [1,0,0]
Material16.transparency = 0.2
Appearance15.material = Material16
Shape13.appearance = Appearance15
Transform12.addChildren([Shape13])

Script17 = Script()
Script17.DEF = "bounce"

field18 = field()
field18.name = "scale"
field18.accessType = "inputOutput"
field18.type = "SFVec3f"
field18.value = "1 1 1"
Script17.addField([field18])

field19 = field()
field19.name = "translation"
field19.accessType = "inputOutput"
field19.type = "SFVec3f"
field19.value = "0 0 0"
Script17.addField([field19])

field20 = field()
field20.name = "velocity"
field20.accessType = "inputOutput"
field20.type = "SFVec3f"
field20.value = "0 0 0"
Script17.addField([field20])

field21 = field()
field21.name = "scalvel"
field21.accessType = "inputOutput"
field21.type = "SFVec3f"
field21.value = "0 0 0"
Script17.addField([field21])

field22 = field()
field22.name = "set_fraction"
field22.accessType = "inputOnly"
field22.type = "SFFloat"
Script17.addField([field22])

Script17.setSourceCode('''ecmascript:\n"+
"function initialize() {\n"+
"    velocity = new SFVec3f(Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125);\n"+
"\n"+
"    scalvel = new SFVec3f(Math.random() * 0.4, Math.random() * 0.4, Math.random() * 0.4);\n"+
"}\n"+
"\n"+
"function set_fraction(value) {\n"+
"	translation = new SFVec3f(\n"+
"		translation.x + velocity.x,\n"+
"		translation.y + velocity.y,\n"+
"		translation.z + velocity.z);\n"+
"	scale = new SFVec3f(\n"+
"		scale.x + scalvel.x,\n"+
"		scale.y + scalvel.y,\n"+
"		scale.z + scalvel.z);\n"+
"        // if you get to far away or too big, explode\n"+
"        if ( Math.abs(translation.x) > 256) {\n"+
"		translation.x = 0;\n"+
"		initialize();\n"+
"	}\n"+
"        if ( Math.abs(translation.y) > 256) {\n"+
"		translation.y = 0;\n"+
"		initialize();\n"+
"	}\n"+
"        if ( Math.abs(translation.z) > 256) {\n"+
"		translation.z = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.x) > 20) {\n"+
"		scale.x = scale.x/2;\n"+
"		translation.x = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.y) > 20) {\n"+
"		scale.y = scale.y/2;\n"+
"		translation.y = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.z) > 20) {\n"+
"		scale.z = scale.z/2;\n"+
"		translation.z = 0;\n"+
"		initialize();\n"+
"	}\n"+
"}\n"+
"''')
Transform12.addChildren([Script17])

TimeSensor23 = TimeSensor()
TimeSensor23.DEF = "bubbleClock"
TimeSensor23.cycleInterval = 10
TimeSensor23.loop = True
Transform12.addChildren([TimeSensor23])

ROUTE24 = ROUTE()
ROUTE24.fromNode = "bounce"
ROUTE24.fromField = "translation_changed"
ROUTE24.toNode = "transform"
ROUTE24.toField = "set_translation"
Transform12.addChildren([ROUTE24])

ROUTE25 = ROUTE()
ROUTE25.fromNode = "bounce"
ROUTE25.fromField = "scale_changed"
ROUTE25.toNode = "transform"
ROUTE25.toField = "set_scale"
Transform12.addChildren([ROUTE25])

ROUTE26 = ROUTE()
ROUTE26.fromNode = "bubbleClock"
ROUTE26.fromField = "fraction_changed"
ROUTE26.toNode = "bounce"
ROUTE26.toField = "set_fraction"
Transform12.addChildren([ROUTE26])
ProtoBody11.addChildren([Transform12])
ProtoDeclare10.protoBody = ProtoBody11
Scene7.addChildren([ProtoDeclare10])

ProtoInstance27 = ProtoInstance()
ProtoInstance27.name = "Bubble"
ProtoInstance27.DEF = "bubbleA"
Scene7.addChildren([ProtoInstance27])
X3D0.scene = Scene7
