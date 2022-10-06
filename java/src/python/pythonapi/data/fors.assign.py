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
meta4.name = "title"
meta4.content = "force.x3d"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/force.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "beginnings of a force directed graph in 3D"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "generator"
meta7.content = "Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit"
head1.addMeta([meta7])
X3D0.head = head1

Scene8 = Scene()

ProtoDeclare9 = ProtoDeclare()
ProtoDeclare9.name = "node"

ProtoInterface10 = ProtoInterface()

field11 = field()
field11.name = "position"
field11.accessType = "inputOutput"
field11.type = "SFVec3f"
field11.value = "0 0 0"
ProtoInterface10.addField([field11])
ProtoDeclare9.protoInterface = ProtoInterface10

ProtoBody12 = ProtoBody()

Transform13 = Transform()
Transform13.DEF = "transform"

IS14 = IS()

connect15 = connect()
connect15.nodeField = "translation"
connect15.protoField = "position"
IS14.addConnect([connect15])
Transform13.IS = IS14

Shape16 = Shape()

Sphere17 = Sphere()
Shape16.geometry = Sphere17

Appearance18 = Appearance()

Material19 = Material()
Material19.diffuseColor = [1,0,0]
Appearance18.material = Material19
Shape16.appearance = Appearance18
Transform13.addChildren([Shape16])

Transform20 = Transform()
Transform20.translation = [1,0,0]

Shape21 = Shape()

Text22 = Text()
Text22.string = ["Node"]

FontStyle23 = FontStyle(family = ["SERIF"], justify = ["MIDDLE","MIDDLE"], size = 5)
Text22.fontStyle = FontStyle23
Shape21.geometry = Text22

Appearance24 = Appearance()

Material25 = Material()
Material25.diffuseColor = [0,0,1]
Appearance24.material = Material25
Shape21.appearance = Appearance24
Transform20.addChildren([Shape21])
Transform13.addChildren([Transform20])
ProtoBody12.addChildren([Transform13])

PositionInterpolator26 = PositionInterpolator()
PositionInterpolator26.DEF = "NodePosition"
PositionInterpolator26.key = [0,1]
PositionInterpolator26.keyValue = [0,0,0,0,5,0]
ProtoBody12.addChildren([PositionInterpolator26])

Script27 = Script()
Script27.DEF = "MoveBall"

field28 = field()
field28.name = "translation"
field28.accessType = "inputOutput"
field28.type = "SFVec3f"
field28.value = "50 50 0"
Script27.addField([field28])

field29 = field()
field29.name = "old"
field29.accessType = "inputOutput"
field29.type = "SFVec3f"
field29.value = "0 0 0"
Script27.addField([field29])

field30 = field()
field30.name = "set_cycle"
field30.accessType = "inputOnly"
field30.type = "SFTime"
Script27.addField([field30])

field31 = field()
field31.name = "keyValue"
field31.accessType = "outputOnly"
field31.type = "MFVec3f"
Script27.addField([field31])

Script27.setSourceCode('''\n"+
"ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f([old, translation]);\n"+
"						// Browser.println(translation);\n"+
"					}\n"+
"''')
ProtoBody12.addChildren([Script27])

TimeSensor32 = TimeSensor()
TimeSensor32.DEF = "nodeClock"
TimeSensor32.cycleInterval = 3
TimeSensor32.loop = True
ProtoBody12.addChildren([TimeSensor32])

ROUTE33 = ROUTE()
ROUTE33.fromNode = "nodeClock"
ROUTE33.fromField = "cycleTime"
ROUTE33.toNode = "MoveBall"
ROUTE33.toField = "set_cycle"
ProtoBody12.addChildren([ROUTE33])

ROUTE34 = ROUTE()
ROUTE34.fromNode = "nodeClock"
ROUTE34.fromField = "fraction_changed"
ROUTE34.toNode = "NodePosition"
ROUTE34.toField = "set_fraction"
ProtoBody12.addChildren([ROUTE34])

ROUTE35 = ROUTE()
ROUTE35.fromNode = "MoveBall"
ROUTE35.fromField = "keyValue"
ROUTE35.toNode = "NodePosition"
ROUTE35.toField = "keyValue"
ProtoBody12.addChildren([ROUTE35])

ROUTE36 = ROUTE()
ROUTE36.fromNode = "NodePosition"
ROUTE36.fromField = "value_changed"
ROUTE36.toNode = "transform"
ROUTE36.toField = "set_translation"
ProtoBody12.addChildren([ROUTE36])
ProtoDeclare9.protoBody = ProtoBody12
Scene8.addChildren([ProtoDeclare9])

ProtoDeclare37 = ProtoDeclare()
ProtoDeclare37.name = "cylinder"

ProtoInterface38 = ProtoInterface()

field39 = field()
field39.name = "set_positionA"
field39.accessType = "inputOnly"
field39.type = "SFVec3f"
ProtoInterface38.addField([field39])

field40 = field()
field40.name = "set_positionB"
field40.accessType = "inputOnly"
field40.type = "SFVec3f"
ProtoInterface38.addField([field40])
ProtoDeclare37.protoInterface = ProtoInterface38

ProtoBody41 = ProtoBody()

Shape42 = Shape()

Extrusion43 = Extrusion(creaseAngle = 0.785, crossSection = [1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00], spine = [0,-50,0,0,50,0])
Extrusion43.DEF = "extrusion"
Shape42.geometry = Extrusion43

Appearance44 = Appearance()

Material45 = Material()
Material45.diffuseColor = [0,1,0]
Appearance44.material = Material45
Shape42.appearance = Appearance44
ProtoBody41.addChildren([Shape42])

Script46 = Script()
Script46.DEF = "MoveCylinder"

field47 = field()
field47.name = "spine"
field47.accessType = "inputOutput"
field47.type = "MFVec3f"
field47.value = "0 -50 0 0 50 0"
Script46.addField([field47])

field48 = field()
field48.name = "set_endA"
field48.accessType = "inputOnly"
field48.type = "SFVec3f"
Script46.addField([field48])

field49 = field()
field49.name = "set_endB"
field49.accessType = "inputOnly"
field49.type = "SFVec3f"
Script46.addField([field49])

IS50 = IS()

connect51 = connect()
connect51.nodeField = "set_endA"
connect51.protoField = "set_positionA"
IS50.addConnect([connect51])

connect52 = connect()
connect52.nodeField = "set_endB"
connect52.protoField = "set_positionB"
IS50.addConnect([connect52])
Script46.IS = IS50

Script46.setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"                function set_endA(value) {\n"+
"		    if (typeof spine === 'undefined') {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([value, spine[1]]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_endB(value) {\n"+
"		    if (typeof spine === 'undefined') {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([spine[0], value]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_spine(value) {\n"+
"                    spine = value;\n"+
"                }\n"+
"''')
ProtoBody41.addChildren([Script46])

ROUTE53 = ROUTE()
ROUTE53.fromNode = "MoveCylinder"
ROUTE53.fromField = "spine"
ROUTE53.toNode = "extrusion"
ROUTE53.toField = "set_spine"
ProtoBody41.addChildren([ROUTE53])
ProtoDeclare37.protoBody = ProtoBody41
Scene8.addChildren([ProtoDeclare37])

Transform54 = Transform()
Transform54.DEF = "HoldsContent"
Transform54.scale = [0.1,0.1,0.1]

PlaneSensor55 = PlaneSensor()
PlaneSensor55.DEF = "clickGenerator"
PlaneSensor55.enabled = True
PlaneSensor55.minPosition = [-50,-50]
PlaneSensor55.maxPosition = [50,50]
PlaneSensor55.description = "click on background to add nodes, click on nodes to add links"
Transform54.addChildren([PlaneSensor55])

ProtoInstance56 = ProtoInstance()
ProtoInstance56.DEF = "nodeA"
ProtoInstance56.name = "node"

fieldValue57 = fieldValue()
fieldValue57.name = "position"
fieldValue57.value = "0.0 0.0 0.0"
ProtoInstance56.addFieldValue([fieldValue57])
Transform54.addChildren([ProtoInstance56])

ProtoInstance58 = ProtoInstance()
ProtoInstance58.DEF = "nodeB"
ProtoInstance58.name = "node"

fieldValue59 = fieldValue()
fieldValue59.name = "position"
fieldValue59.value = "50.0 50.0 50.0"
ProtoInstance58.addFieldValue([fieldValue59])
Transform54.addChildren([ProtoInstance58])

ProtoInstance60 = ProtoInstance()
ProtoInstance60.DEF = "linkA"
ProtoInstance60.name = "cylinder"

fieldValue61 = fieldValue()
fieldValue61.name = "set_positionA"
fieldValue61.value = "0 0 0"
ProtoInstance60.addFieldValue([fieldValue61])

fieldValue62 = fieldValue()
fieldValue62.name = "set_positionB"
fieldValue62.value = "50 50 50"
ProtoInstance60.addFieldValue([fieldValue62])
Transform54.addChildren([ProtoInstance60])
Scene8.addChildren([Transform54])

ROUTE63 = ROUTE()
ROUTE63.fromNode = "nodeA"
ROUTE63.fromField = "position"
ROUTE63.toNode = "linkA"
ROUTE63.toField = "set_positionA"
Scene8.addChildren([ROUTE63])

ROUTE64 = ROUTE()
ROUTE64.fromNode = "nodeB"
ROUTE64.fromField = "position"
ROUTE64.toNode = "linkA"
ROUTE64.toField = "set_positionB"
Scene8.addChildren([ROUTE64])
X3D0.scene = Scene8
