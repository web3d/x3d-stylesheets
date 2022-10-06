from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "creator"
meta2.content = "John W Carlson"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "created"
meta3.content = "December 13 2015"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "modified"
meta4.content = "April 18 2017"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "title"
meta5.content = "fors2.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "identifier"
meta6.content = "https://coderextreme.net/X3DJSONLD/fors2.x3d"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "description"
meta7.content = "beginnings of a force directed graph in 3D"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "generator"
meta8.content = "Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit"
head1.addMeta([meta8])
X3D0.head = head1

Scene9 = Scene()

ProtoDeclare10 = ProtoDeclare()
ProtoDeclare10.name = "node"

ProtoInterface11 = ProtoInterface()

field12 = field()
field12.name = "position"
field12.accessType = "inputOutput"
field12.type = "SFVec3f"
field12.value = "0 0 0"
ProtoInterface11.addField([field12])
ProtoDeclare10.protoInterface = ProtoInterface11

ProtoBody13 = ProtoBody()

Transform14 = Transform()
Transform14.DEF = "transform"

IS15 = IS()

connect16 = connect()
connect16.nodeField = "translation"
connect16.protoField = "position"
IS15.addConnect([connect16])
Transform14.IS = IS15

Shape17 = Shape()
#comment before Sphere
#comment after Sphere
#comment after Appearance

Sphere18 = Sphere()
Shape17.geometry = Sphere18

Appearance19 = Appearance()
#comment before Material
#comment after Material

Material20 = Material()
Material20.diffuseColor = [1,0,0]
Appearance19.material = Material20
Shape17.appearance = Appearance19
Transform14.addChildren([Shape17])
ProtoBody13.addChildren([Transform14])

PositionInterpolator21 = PositionInterpolator()
PositionInterpolator21.DEF = "NodePosition"
PositionInterpolator21.key = [0,1]
PositionInterpolator21.keyValue = [0,0,0,0,5,0]
ProtoBody13.addChildren([PositionInterpolator21])

Script22 = Script()
Script22.DEF = "MoveBall"

field23 = field()
field23.name = "translation"
field23.accessType = "inputOutput"
field23.type = "SFVec3f"
field23.value = "50 50 0"
Script22.addField([field23])

field24 = field()
field24.name = "old"
field24.accessType = "inputOutput"
field24.type = "SFVec3f"
field24.value = "0 0 0"
Script22.addField([field24])

field25 = field()
field25.name = "set_cycle"
field25.accessType = "inputOnly"
field25.type = "SFTime"
Script22.addField([field25])

field26 = field()
field26.name = "keyValue"
field26.accessType = "outputOnly"
field26.type = "MFVec3f"
Script22.addField([field26])

Script22.setSourceCode(''' ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f([old, translation]);\n"+
"						// Browser.println(translation);\n"+
"					}\n"+
" ''')
ProtoBody13.addChildren([Script22])

TimeSensor27 = TimeSensor()
TimeSensor27.DEF = "nodeClock"
TimeSensor27.cycleInterval = 3
TimeSensor27.loop = True
ProtoBody13.addChildren([TimeSensor27])

ROUTE28 = ROUTE()
ROUTE28.fromNode = "nodeClock"
ROUTE28.fromField = "cycleTime"
ROUTE28.toNode = "MoveBall"
ROUTE28.toField = "set_cycle"
ProtoBody13.addChildren([ROUTE28])

ROUTE29 = ROUTE()
ROUTE29.fromNode = "nodeClock"
ROUTE29.fromField = "fraction_changed"
ROUTE29.toNode = "NodePosition"
ROUTE29.toField = "set_fraction"
ProtoBody13.addChildren([ROUTE29])

ROUTE30 = ROUTE()
ROUTE30.fromNode = "MoveBall"
ROUTE30.fromField = "keyValue"
ROUTE30.toNode = "NodePosition"
ROUTE30.toField = "keyValue"
ProtoBody13.addChildren([ROUTE30])

ROUTE31 = ROUTE()
ROUTE31.fromNode = "NodePosition"
ROUTE31.fromField = "value_changed"
ROUTE31.toNode = "transform"
ROUTE31.toField = "set_translation"
ProtoBody13.addChildren([ROUTE31])
ProtoDeclare10.protoBody = ProtoBody13
Scene9.addChildren([ProtoDeclare10])

ProtoDeclare32 = ProtoDeclare()
ProtoDeclare32.name = "cylinder"

ProtoInterface33 = ProtoInterface()

field34 = field()
field34.name = "positionA"
field34.accessType = "inputOnly"
field34.type = "SFVec3f"
ProtoInterface33.addField([field34])

field35 = field()
field35.name = "positionB"
field35.accessType = "inputOnly"
field35.type = "SFVec3f"
ProtoInterface33.addField([field35])
ProtoDeclare32.protoInterface = ProtoInterface33

ProtoBody36 = ProtoBody()

Shape37 = Shape()

Extrusion38 = Extrusion(creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine = [0,-50,0,0,0,0,0,50,0])
Extrusion38.DEF = "extrusion"
Shape37.geometry = Extrusion38

Appearance39 = Appearance()

Material40 = Material()
Material40.diffuseColor = [0,1,0]
Appearance39.material = Material40
Shape37.appearance = Appearance39
ProtoBody36.addChildren([Shape37])

Script41 = Script()
Script41.DEF = "MoveCylinder"

field42 = field()
field42.name = "spine"
field42.accessType = "inputOutput"
field42.type = "MFVec3f"
field42.value = "0 -50 0 0 0 0 0 50 0"
Script41.addField([field42])

field43 = field()
field43.name = "set_endA"
field43.accessType = "inputOnly"
field43.type = "SFVec3f"
Script41.addField([field43])

field44 = field()
field44.name = "set_endB"
field44.accessType = "inputOnly"
field44.type = "SFVec3f"
Script41.addField([field44])

IS45 = IS()

connect46 = connect()
connect46.nodeField = "set_endA"
connect46.protoField = "positionA"
IS45.addConnect([connect46])

connect47 = connect()
connect47.nodeField = "set_endB"
connect47.protoField = "positionB"
IS45.addConnect([connect47])
Script41.IS = IS45

Script41.setSourceCode(''' ecmascript:\n"+
"\n"+
"                function set_endA(value) {\n"+
"		    if (typeof spine === \"undefined\") {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([value, spine[1]]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_endB(value) {\n"+
"		    if (typeof spine === \"undefined\") {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([spine[0], value]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_spine(value) {\n"+
"		    Browser.print('\\n'+'\"');\n"+
"                    spine = value;\n"+
"                }\n"+
" ''')
ProtoBody36.addChildren([Script41])

ROUTE48 = ROUTE()
ROUTE48.fromNode = "MoveCylinder"
ROUTE48.fromField = "spine"
ROUTE48.toNode = "extrusion"
ROUTE48.toField = "set_spine"
ProtoBody36.addChildren([ROUTE48])
ProtoDeclare32.protoBody = ProtoBody36
Scene9.addChildren([ProtoDeclare32])

Transform49 = Transform()
Transform49.scale = [0.1,0.1,0.1]

ProtoInstance50 = ProtoInstance()
ProtoInstance50.name = "node"
ProtoInstance50.DEF = "nodeA"

fieldValue51 = fieldValue()
fieldValue51.name = "position"
fieldValue51.value = "-50 -50 -50"
ProtoInstance50.addFieldValue([fieldValue51])
Transform49.addChildren([ProtoInstance50])

ProtoInstance52 = ProtoInstance()
ProtoInstance52.name = "node"
ProtoInstance52.DEF = "nodeB"

fieldValue53 = fieldValue()
fieldValue53.name = "position"
fieldValue53.value = "50 50 50"
ProtoInstance52.addFieldValue([fieldValue53])
Transform49.addChildren([ProtoInstance52])

ProtoInstance54 = ProtoInstance()
ProtoInstance54.name = "cylinder"
ProtoInstance54.DEF = "linkA"

fieldValue55 = fieldValue()
fieldValue55.name = "positionA"
fieldValue55.value = "0 0 0"
ProtoInstance54.addFieldValue([fieldValue55])

fieldValue56 = fieldValue()
fieldValue56.name = "positionB"
fieldValue56.value = "50 50 50"
ProtoInstance54.addFieldValue([fieldValue56])
Transform49.addChildren([ProtoInstance54])
Scene9.addChildren([Transform49])

ROUTE57 = ROUTE()
ROUTE57.fromNode = "nodeA"
ROUTE57.fromField = "position"
ROUTE57.toNode = "linkA"
ROUTE57.toField = "positionA"
Scene9.addChildren([ROUTE57])

ROUTE58 = ROUTE()
ROUTE58.fromNode = "nodeB"
ROUTE58.fromField = "position"
ROUTE58.toNode = "linkA"
ROUTE58.toField = "positionB"
Scene9.addChildren([ROUTE58])
X3D0.scene = Scene9
