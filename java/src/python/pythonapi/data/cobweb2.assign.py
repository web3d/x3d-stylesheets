from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "geo.x3d"
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
meta6.content = "https://coderextreme.net/X3DJSONLD/geo.x3d"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "translated"
meta7.content = "13 March 2016"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "generator"
meta8.content = "X3dToJson.xslt, http://www.web3d.org/x3d/stylesheets/X3dToJson.html"
head1.addMeta([meta8])
X3D0.head = head1

Scene9 = Scene()

NavigationInfo10 = NavigationInfo()
NavigationInfo10.type = ["EXAMINE"]
Scene9.addChildren([NavigationInfo10])

Viewpoint11 = Viewpoint()
Viewpoint11.position = [0,0,4]
Viewpoint11.orientation = [1,0,0,0]
Viewpoint11.description = "Bubbles in action"
Scene9.addChildren([Viewpoint11])

Background12 = Background()
Background12.backUrl = ["../resources/images/BK.png","https://coderextreme.net/X3DJSONLD/images/BK.png"]
Background12.bottomUrl = ["../resources/images/BT.png","https://coderextreme.net/X3DJSONLD/images/BT.png"]
Background12.frontUrl = ["../resources/images/FR.png","https://coderextreme.net/X3DJSONLD/images/FR.png"]
Background12.leftUrl = ["../resources/images/LF.png","https://coderextreme.net/X3DJSONLD/images/LF.png"]
Background12.rightUrl = ["../resources/images/RT.png","https://coderextreme.net/X3DJSONLD/images/RT.png"]
Background12.topUrl = ["../resources/images/TP.png","https://coderextreme.net/X3DJSONLD/images/TP.png"]
Scene9.addChildren([Background12])

ProtoDeclare13 = ProtoDeclare()
ProtoDeclare13.name = "Bubble"

ProtoBody14 = ProtoBody()

Transform15 = Transform()
Transform15.DEF = "transform"

Shape16 = Shape()

Sphere17 = Sphere(radius = 0.25)
Shape16.geometry = Sphere17

Appearance18 = Appearance()

Material19 = Material()
Material19.diffuseColor = [1,0,0]
Material19.transparency = 0.2
Appearance18.material = Material19
Shape16.appearance = Appearance18
Transform15.addChildren([Shape16])

Script20 = Script()
Script20.DEF = "bounce"

field21 = field()
field21.name = "scale"
field21.accessType = "inputOutput"
field21.type = "SFVec3f"
field21.value = "1 1 1"
Script20.addField([field21])

field22 = field()
field22.name = "translation"
field22.accessType = "inputOutput"
field22.type = "SFVec3f"
field22.value = "0 0 0"
Script20.addField([field22])

field23 = field()
field23.name = "velocity"
field23.accessType = "inputOutput"
field23.type = "SFVec3f"
field23.value = "0 0 0"
Script20.addField([field23])

field24 = field()
field24.name = "scalvel"
field24.accessType = "inputOutput"
field24.type = "SFVec3f"
field24.value = "0 0 0"
Script20.addField([field24])

field25 = field()
field25.name = "set_fraction"
field25.accessType = "inputOnly"
field25.type = "SFFloat"
Script20.addField([field25])

Script20.setSourceCode('''ecmascript:\n"+
"function initialize() {\n"+
"    velocity = new SFVec3f(Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125);\n"+
"\n"+
"    scalvel = new SFVec3f(Math.random() * 0.4, Math.random() * 0.4, Math.random() * 0.4);\n"+
"}\n"+
"\n"+
"function set_fraction(value) {\n"+
"    if (typeof translation === 'undefined') {\n"+
"		translation = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof velocity === 'undefined') {\n"+
"		velocity = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof scalevel === 'undefined') {\n"+
"		scalevel = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof scale === 'undefined') {\n"+
"		scale = new SFVec3f(1, 1, 1);\n"+
"    }\n"+
"    translation = new SFVec3f(	translation.x + velocity.x, translation.y + velocity.y, translation.z + velocity.z);\n"+
"    scale = new SFVec3f(scale.x + scalvel.x, scale.y + scalvel.y, scale.z + scalvel.z);\n"+
"    // if you get to far away or too big, explode\n"+
"    if ( Math.abs(translation.x) &gt; 256) {\n"+
"	translation.x = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if ( Math.abs(translation.y) &gt; 256) {\n"+
"	translation.y = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if ( Math.abs(translation.z) &gt; 256) {\n"+
"	translation.z = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.x) &gt; 20) {\n"+
"	scale.x = scale.x/20;\n"+
"	translation.x = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.y) &gt; 20) {\n"+
"	scale.y = scale.y/20;\n"+
"	translation.y = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.z) &gt; 20) {\n"+
"	scale.z = scale.z/20;\n"+
"	translation.z = 0;\n"+
"	initialize();\n"+
"    }\n"+
"}''')
Transform15.addChildren([Script20])

TimeSensor26 = TimeSensor()
TimeSensor26.DEF = "bubbleClock"
TimeSensor26.cycleInterval = 10
TimeSensor26.loop = True
Transform15.addChildren([TimeSensor26])

ROUTE27 = ROUTE()
ROUTE27.fromNode = "bounce"
ROUTE27.fromField = "translation_changed"
ROUTE27.toNode = "transform"
ROUTE27.toField = "set_translation"
Transform15.addChildren([ROUTE27])

ROUTE28 = ROUTE()
ROUTE28.fromNode = "bounce"
ROUTE28.fromField = "scale_changed"
ROUTE28.toNode = "transform"
ROUTE28.toField = "set_scale"
Transform15.addChildren([ROUTE28])

ROUTE29 = ROUTE()
ROUTE29.fromNode = "bubbleClock"
ROUTE29.fromField = "fraction_changed"
ROUTE29.toNode = "bounce"
ROUTE29.toField = "set_fraction"
Transform15.addChildren([ROUTE29])
ProtoBody14.addChildren([Transform15])
ProtoDeclare13.protoBody = ProtoBody14
Scene9.addChildren([ProtoDeclare13])

ProtoInstance30 = ProtoInstance()
ProtoInstance30.name = "Bubble"
ProtoInstance30.DEF = "bubbleA"
Scene9.addChildren([ProtoInstance30])

ProtoInstance31 = ProtoInstance()
ProtoInstance31.name = "Bubble"
ProtoInstance31.DEF = "bubbleB"
Scene9.addChildren([ProtoInstance31])

ProtoInstance32 = ProtoInstance()
ProtoInstance32.name = "Bubble"
ProtoInstance32.DEF = "bubbleC"
Scene9.addChildren([ProtoInstance32])

ProtoInstance33 = ProtoInstance()
ProtoInstance33.name = "Bubble"
ProtoInstance33.DEF = "bubbleD"
Scene9.addChildren([ProtoInstance33])
X3D0.scene = Scene9
