from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "pp3.x3d"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "creator"
meta3.content = "John Carlson"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "translator"
meta4.content = "John Carlson"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "created"
meta5.content = "5 May 2015"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "05 May 2017"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "description"
meta7.content = "A process pipeline between three spheres (try typing on spheres and blue"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "identifier"
meta8.content = "https://coderextreme.net/x3d/pp3.x3d"
head1.addMeta([meta8])

meta9 = meta()
meta9.name = "generator"
meta9.content = "manual"
head1.addMeta([meta9])
X3D0.head = head1

Scene10 = Scene()

ProtoDeclare11 = ProtoDeclare()
ProtoDeclare11.name = "Process"

ProtoBody12 = ProtoBody()

Group13 = Group()
#left

Transform14 = Transform()
Transform14.scale = [0.5,0.5,0.5]

Shape15 = Shape()

Appearance16 = Appearance()

Material17 = Material()
Material17.diffuseColor = [0.7,1,0]
Material17.transparency = 0.5
Appearance16.material = Material17
Shape15.appearance = Appearance16

Extrusion18 = Extrusion(creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine = [-2.5,0,0,-1.5,0,0])
Shape15.geometry = Extrusion18
Transform14.addChildren([Shape15])
#<Transform translation=\"-2.5 0 0\"> <Shape> <Text DEF=\"LeftString\" string='\"l\"'/> </Shape> </Transform> <StringSensor DEF=\"LeftSensor\" enabled=\"false\"/> <TouchSensor DEF=\"LeftTouch\" enabled=\"true\"/>
Group13.addChildren([Transform14])
#right

Transform19 = Transform()
Transform19.scale = [0.5,0.5,0.5]

Shape20 = Shape()

Appearance21 = Appearance()

Material22 = Material()
Material22.diffuseColor = [0,0.7,1]
Material22.transparency = 0.5
Appearance21.material = Material22
Shape20.appearance = Appearance21

Extrusion23 = Extrusion(creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine = [1.5,0,0,2.5,0,0])
Shape20.geometry = Extrusion23
Transform19.addChildren([Shape20])

Transform24 = Transform()
Transform24.translation = [2,0,0]

Shape25 = Shape()

Appearance26 = Appearance()

Material27 = Material()
Material27.DEF = "MaterialLightBlue"
Material27.diffuseColor = [1,1,1]
Appearance26.material = Material27
Shape25.appearance = Appearance26

Text28 = Text()
Text28.DEF = "RightString"
Text28.string = ["r"]
Shape25.geometry = Text28
Transform24.addChildren([Shape25])
Transform19.addChildren([Transform24])

StringSensor29 = StringSensor()
StringSensor29.DEF = "RightSensor"
StringSensor29.enabled = False
StringSensor29.deletionAllowed = True
Transform19.addChildren([StringSensor29])

TouchSensor30 = TouchSensor()
TouchSensor30.description = "touch to activate"
TouchSensor30.DEF = "RightTouch"
Transform19.addChildren([TouchSensor30])
Group13.addChildren([Transform19])
#up

Transform31 = Transform()
Transform31.scale = [0.5,0.5,0.5]

Shape32 = Shape()

Appearance33 = Appearance()

Material34 = Material()
Material34.diffuseColor = [0,0.7,1]
Material34.transparency = 0.5
Appearance33.material = Material34
Shape32.appearance = Appearance33

Extrusion35 = Extrusion(creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine = [0,1.5,0,0,2.5,0])
Shape32.geometry = Extrusion35
Transform31.addChildren([Shape32])

Transform36 = Transform()
Transform36.translation = [-0.5,2,0]

Shape37 = Shape()

Appearance38 = Appearance()

Material39 = Material()
Material39.USE = "MaterialLightBlue"
Appearance38.material = Material39
Shape37.appearance = Appearance38

Text40 = Text()
Text40.DEF = "UpString"
Text40.string = ["u"]
Shape37.geometry = Text40
Transform36.addChildren([Shape37])
Transform31.addChildren([Transform36])

StringSensor41 = StringSensor()
StringSensor41.DEF = "UpSensor"
StringSensor41.enabled = False
StringSensor41.deletionAllowed = True
Transform31.addChildren([StringSensor41])

TouchSensor42 = TouchSensor()
TouchSensor42.description = "touch to activate"
TouchSensor42.DEF = "UpTouch"
Transform31.addChildren([TouchSensor42])
Group13.addChildren([Transform31])
#down

Transform43 = Transform()
Transform43.scale = [0.5,0.5,0.5]

Shape44 = Shape()

Appearance45 = Appearance()

Material46 = Material()
Material46.diffuseColor = [0.7,1,0]
Material46.transparency = 0.5
Appearance45.material = Material46
Shape44.appearance = Appearance45

Extrusion47 = Extrusion(creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine = [0,-2.5,0,0,-1.5,0])
Shape44.geometry = Extrusion47
Transform43.addChildren([Shape44])
#<Transform translation=\"-0.5 -2.5 0\"> <Shape> <Text DEF=\"DownString\" string='\"d\"'/> </Shape> </Transform> <StringSensor DEF=\"DownSensor\" enabled=\"false\"/> <TouchSensor description='touch to activate' DEF=\"DownTouch\" enabled=\"true\"/>
Group13.addChildren([Transform43])
#center

Transform48 = Transform()

Shape49 = Shape()

Appearance50 = Appearance()

Material51 = Material()
Material51.diffuseColor = [1,0,0.7]
Appearance50.material = Material51
Shape49.appearance = Appearance50

Sphere52 = Sphere()
Shape49.geometry = Sphere52
Transform48.addChildren([Shape49])

Transform53 = Transform()
Transform53.scale = [0.5,0.5,0.5]
Transform53.translation = [-0.5,0,1]

Shape54 = Shape()

Appearance55 = Appearance()

Material56 = Material()
Material56.USE = "MaterialLightBlue"
Appearance55.material = Material56
Shape54.appearance = Appearance55

Text57 = Text()
Text57.DEF = "CenterString"
Shape54.geometry = Text57
Transform53.addChildren([Shape54])
Transform48.addChildren([Transform53])

StringSensor58 = StringSensor()
StringSensor58.DEF = "CenterSensor"
StringSensor58.enabled = False
StringSensor58.deletionAllowed = True
Transform48.addChildren([StringSensor58])

TouchSensor59 = TouchSensor()
TouchSensor59.description = "touch to activate"
TouchSensor59.DEF = "CenterTouch"
Transform48.addChildren([TouchSensor59])
Group13.addChildren([Transform48])
ProtoBody12.addChildren([Group13])

Script60 = Script()
Script60.DEF = "RightSingleToMultiString"

field61 = field()
field61.name = "set_rightstring"
field61.accessType = "inputOnly"
field61.type = "SFString"
Script60.addField([field61])

field62 = field()
field62.name = "rightlines"
field62.accessType = "outputOnly"
field62.type = "MFString"
Script60.addField([field62])

Script60.setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	rightlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_rightstring(rightstr) {\n"+
"	rightlines = new MFString(rightstr);\n"+
"}''')
ProtoBody12.addChildren([Script60])

Script63 = Script()
Script63.DEF = "UpSingleToMultiString"

field64 = field()
field64.name = "set_upstring"
field64.accessType = "inputOnly"
field64.type = "SFString"
Script63.addField([field64])

field65 = field()
field65.name = "uplines"
field65.accessType = "outputOnly"
field65.type = "MFString"
Script63.addField([field65])

Script63.setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	uplines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_upstring(upstr) {\n"+
"	uplines = new MFString(upstr);\n"+
"}''')
ProtoBody12.addChildren([Script63])

Script66 = Script()
Script66.DEF = "CenterSingleToMultiString"

field67 = field()
field67.name = "set_centerstring"
field67.accessType = "inputOnly"
field67.type = "SFString"
Script66.addField([field67])

field68 = field()
field68.name = "centerlines"
field68.accessType = "outputOnly"
field68.type = "MFString"
Script66.addField([field68])

Script66.setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	centerlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_centerstring(centerstr) {\n"+
"	centerlines = new MFString(centerstr);\n"+
"}''')
ProtoBody12.addChildren([Script66])

ROUTE69 = ROUTE()
ROUTE69.fromField = "enteredText"
ROUTE69.fromNode = "CenterSensor"
ROUTE69.toField = "set_centerstring"
ROUTE69.toNode = "CenterSingleToMultiString"
ProtoBody12.addChildren([ROUTE69])

ROUTE70 = ROUTE()
ROUTE70.fromField = "centerlines"
ROUTE70.fromNode = "CenterSingleToMultiString"
ROUTE70.toField = "set_string"
ROUTE70.toNode = "CenterString"
ProtoBody12.addChildren([ROUTE70])

ROUTE71 = ROUTE()
ROUTE71.fromField = "isOver"
ROUTE71.fromNode = "CenterTouch"
ROUTE71.toField = "set_enabled"
ROUTE71.toNode = "CenterSensor"
ProtoBody12.addChildren([ROUTE71])

ROUTE72 = ROUTE()
ROUTE72.fromField = "enteredText"
ROUTE72.fromNode = "RightSensor"
ROUTE72.toField = "set_rightstring"
ROUTE72.toNode = "RightSingleToMultiString"
ProtoBody12.addChildren([ROUTE72])

ROUTE73 = ROUTE()
ROUTE73.fromField = "rightlines"
ROUTE73.fromNode = "RightSingleToMultiString"
ROUTE73.toField = "set_string"
ROUTE73.toNode = "RightString"
ProtoBody12.addChildren([ROUTE73])

ROUTE74 = ROUTE()
ROUTE74.fromField = "isOver"
ROUTE74.fromNode = "RightTouch"
ROUTE74.toField = "set_enabled"
ROUTE74.toNode = "RightSensor"
ProtoBody12.addChildren([ROUTE74])

ROUTE75 = ROUTE()
ROUTE75.fromField = "enteredText"
ROUTE75.fromNode = "UpSensor"
ROUTE75.toField = "set_upstring"
ROUTE75.toNode = "UpSingleToMultiString"
ProtoBody12.addChildren([ROUTE75])

ROUTE76 = ROUTE()
ROUTE76.fromField = "uplines"
ROUTE76.fromNode = "UpSingleToMultiString"
ROUTE76.toField = "set_string"
ROUTE76.toNode = "UpString"
ProtoBody12.addChildren([ROUTE76])

ROUTE77 = ROUTE()
ROUTE77.fromField = "isOver"
ROUTE77.fromNode = "UpTouch"
ROUTE77.toField = "set_enabled"
ROUTE77.toNode = "UpSensor"
ProtoBody12.addChildren([ROUTE77])
ProtoDeclare11.protoBody = ProtoBody12
Scene10.addChildren([ProtoDeclare11])

NavigationInfo78 = NavigationInfo()
Scene10.addChildren([NavigationInfo78])

Viewpoint79 = Viewpoint()
Viewpoint79.description = "Process pipes"
Viewpoint79.orientation = [1,0,0,-0.4]
Viewpoint79.position = [0,5,12]
Scene10.addChildren([Viewpoint79])

Transform80 = Transform()
Transform80.translation = [0,-2.5,0]

ProtoInstance81 = ProtoInstance()
ProtoInstance81.name = "Process"
Transform80.addChildren([ProtoInstance81])
Scene10.addChildren([Transform80])

Transform82 = Transform()

ProtoInstance83 = ProtoInstance()
ProtoInstance83.name = "Process"
Transform82.addChildren([ProtoInstance83])
Scene10.addChildren([Transform82])

Transform84 = Transform()
Transform84.translation = [0,2.5,0]

ProtoInstance85 = ProtoInstance()
ProtoInstance85.name = "Process"
Transform84.addChildren([ProtoInstance85])
Scene10.addChildren([Transform84])
X3D0.scene = Scene10
