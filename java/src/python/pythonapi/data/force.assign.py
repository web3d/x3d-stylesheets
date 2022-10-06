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

Group13 = Group()

Transform14 = Transform()
Transform14.DEF = "transform"

IS15 = IS()

connect16 = connect()
connect16.nodeField = "translation"
connect16.protoField = "position"
IS15.addConnect([connect16])
Transform14.IS = IS15

Shape17 = Shape()

Sphere18 = Sphere()
Shape17.geometry = Sphere18

Appearance19 = Appearance()

Material20 = Material()
Material20.diffuseColor = [1,0,0]
Appearance19.material = Material20
Shape17.appearance = Appearance19
Transform14.addChildren([Shape17])

Transform21 = Transform()
Transform21.translation = [1,0,0]

Shape22 = Shape()

Text23 = Text()
Text23.string = ["Node"]

FontStyle24 = FontStyle(family = ["SERIF"], justify = ["MIDDLE","MIDDLE"], size = 5)
Text23.fontStyle = FontStyle24
Shape22.geometry = Text23

Appearance25 = Appearance()

Material26 = Material()
Material26.diffuseColor = [0,0,1]
Appearance25.material = Material26
Shape22.appearance = Appearance25
Transform21.addChildren([Shape22])
Transform14.addChildren([Transform21])
Group13.addChildren([Transform14])

PositionInterpolator27 = PositionInterpolator()
PositionInterpolator27.DEF = "NodePosition"
PositionInterpolator27.key = [0,1]
PositionInterpolator27.keyValue = [0,0,0,0,5,0]
Group13.addChildren([PositionInterpolator27])

Script28 = Script()
Script28.DEF = "MoveBall"

field29 = field()
field29.name = "translation"
field29.accessType = "inputOutput"
field29.type = "SFVec3f"
field29.value = "50 50 0"
Script28.addField([field29])

field30 = field()
field30.name = "old"
field30.accessType = "inputOutput"
field30.type = "SFVec3f"
field30.value = "0 0 0"
Script28.addField([field30])

field31 = field()
field31.name = "set_cycle"
field31.accessType = "inputOnly"
field31.type = "SFTime"
Script28.addField([field31])

field32 = field()
field32.name = "keyValue"
field32.accessType = "outputOnly"
field32.type = "MFVec3f"
Script28.addField([field32])

Script28.setSourceCode('''\n"+
"ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f([old, translation]);\n"+
"						// Browser.println(translation);\n"+
"					}\n"+
"''')
Group13.addChildren([Script28])

TimeSensor33 = TimeSensor()
TimeSensor33.DEF = "nodeClock"
TimeSensor33.cycleInterval = 3
TimeSensor33.loop = True
Group13.addChildren([TimeSensor33])

ROUTE34 = ROUTE()
ROUTE34.fromNode = "nodeClock"
ROUTE34.fromField = "cycleTime"
ROUTE34.toNode = "MoveBall"
ROUTE34.toField = "set_cycle"
Group13.addChildren([ROUTE34])

ROUTE35 = ROUTE()
ROUTE35.fromNode = "nodeClock"
ROUTE35.fromField = "fraction_changed"
ROUTE35.toNode = "NodePosition"
ROUTE35.toField = "set_fraction"
Group13.addChildren([ROUTE35])

ROUTE36 = ROUTE()
ROUTE36.fromNode = "MoveBall"
ROUTE36.fromField = "keyValue"
ROUTE36.toNode = "NodePosition"
ROUTE36.toField = "keyValue"
Group13.addChildren([ROUTE36])

ROUTE37 = ROUTE()
ROUTE37.fromNode = "NodePosition"
ROUTE37.fromField = "value_changed"
ROUTE37.toNode = "transform"
ROUTE37.toField = "set_translation"
Group13.addChildren([ROUTE37])
ProtoBody12.addChildren([Group13])
ProtoDeclare9.protoBody = ProtoBody12
Scene8.addChildren([ProtoDeclare9])

ProtoDeclare38 = ProtoDeclare()
ProtoDeclare38.name = "cylinder"

ProtoInterface39 = ProtoInterface()

field40 = field()
field40.name = "set_positionA"
field40.accessType = "inputOnly"
field40.type = "SFVec3f"
ProtoInterface39.addField([field40])

field41 = field()
field41.name = "set_positionB"
field41.accessType = "inputOnly"
field41.type = "SFVec3f"
ProtoInterface39.addField([field41])
ProtoDeclare38.protoInterface = ProtoInterface39

ProtoBody42 = ProtoBody()

Group43 = Group()

Shape44 = Shape()

Extrusion45 = Extrusion(creaseAngle = 0.785, crossSection = [1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00], spine = [0,-50,0,0,50,0])
Extrusion45.DEF = "extrusion"
Shape44.geometry = Extrusion45

Appearance46 = Appearance()

Material47 = Material()
Material47.diffuseColor = [0,1,0]
Appearance46.material = Material47
Shape44.appearance = Appearance46
Group43.addChildren([Shape44])

Script48 = Script()
Script48.DEF = "MoveCylinder"

field49 = field()
field49.name = "spine"
field49.accessType = "inputOutput"
field49.type = "MFVec3f"
field49.value = "0 -50 0 0 50 0"
Script48.addField([field49])

field50 = field()
field50.name = "set_endA"
field50.accessType = "inputOnly"
field50.type = "SFVec3f"
Script48.addField([field50])

field51 = field()
field51.name = "set_endB"
field51.accessType = "inputOnly"
field51.type = "SFVec3f"
Script48.addField([field51])

IS52 = IS()

connect53 = connect()
connect53.nodeField = "set_endA"
connect53.protoField = "set_positionA"
IS52.addConnect([connect53])

connect54 = connect()
connect54.nodeField = "set_endB"
connect54.protoField = "set_positionB"
IS52.addConnect([connect54])
Script48.IS = IS52

Script48.setSourceCode('''\n"+
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
Group43.addChildren([Script48])

ROUTE55 = ROUTE()
ROUTE55.fromNode = "MoveCylinder"
ROUTE55.fromField = "spine"
ROUTE55.toNode = "extrusion"
ROUTE55.toField = "set_spine"
Group43.addChildren([ROUTE55])
ProtoBody42.addChildren([Group43])
ProtoDeclare38.protoBody = ProtoBody42
Scene8.addChildren([ProtoDeclare38])

Transform56 = Transform()
Transform56.DEF = "HoldsContent"
Transform56.scale = [0.1,0.1,0.1]

PlaneSensor57 = PlaneSensor()
PlaneSensor57.DEF = "clickGenerator"
PlaneSensor57.enabled = True
PlaneSensor57.minPosition = [-50,-50]
PlaneSensor57.maxPosition = [50,50]
PlaneSensor57.description = "click on background to add nodes, click on nodes to add links"
Transform56.addChildren([PlaneSensor57])

ProtoInstance58 = ProtoInstance()
ProtoInstance58.DEF = "nodeA"
ProtoInstance58.name = "node"

fieldValue59 = fieldValue()
fieldValue59.name = "position"
fieldValue59.value = "0.0 0.0 0.0"
ProtoInstance58.addFieldValue([fieldValue59])
Transform56.addChildren([ProtoInstance58])

ProtoInstance60 = ProtoInstance()
ProtoInstance60.DEF = "nodeB"
ProtoInstance60.name = "node"

fieldValue61 = fieldValue()
fieldValue61.name = "position"
fieldValue61.value = "50.0 50.0 50.0"
ProtoInstance60.addFieldValue([fieldValue61])
Transform56.addChildren([ProtoInstance60])

ProtoInstance62 = ProtoInstance()
ProtoInstance62.DEF = "nodeC"
ProtoInstance62.name = "node"

fieldValue63 = fieldValue()
fieldValue63.name = "position"
fieldValue63.value = "-50.0 -50.0 -50.0"
ProtoInstance62.addFieldValue([fieldValue63])
Transform56.addChildren([ProtoInstance62])

ProtoInstance64 = ProtoInstance()
ProtoInstance64.DEF = "nodeD"
ProtoInstance64.name = "node"

fieldValue65 = fieldValue()
fieldValue65.name = "position"
fieldValue65.value = "50.0 50.0 -50.0"
ProtoInstance64.addFieldValue([fieldValue65])
Transform56.addChildren([ProtoInstance64])

ProtoInstance66 = ProtoInstance()
ProtoInstance66.DEF = "linkA"
ProtoInstance66.name = "cylinder"

fieldValue67 = fieldValue()
fieldValue67.name = "set_positionA"
fieldValue67.value = "0 0 0"
ProtoInstance66.addFieldValue([fieldValue67])

fieldValue68 = fieldValue()
fieldValue68.name = "set_positionB"
fieldValue68.value = "50 50 50"
ProtoInstance66.addFieldValue([fieldValue68])
Transform56.addChildren([ProtoInstance66])

ProtoInstance69 = ProtoInstance()
ProtoInstance69.DEF = "linkB"
ProtoInstance69.name = "cylinder"

fieldValue70 = fieldValue()
fieldValue70.name = "set_positionA"
fieldValue70.value = "0 0 0"
ProtoInstance69.addFieldValue([fieldValue70])

fieldValue71 = fieldValue()
fieldValue71.name = "set_positionB"
fieldValue71.value = "-50 -50 -50"
ProtoInstance69.addFieldValue([fieldValue71])
Transform56.addChildren([ProtoInstance69])

ProtoInstance72 = ProtoInstance()
ProtoInstance72.DEF = "linkC"
ProtoInstance72.name = "cylinder"

fieldValue73 = fieldValue()
fieldValue73.name = "set_positionA"
fieldValue73.value = "50 50 50"
ProtoInstance72.addFieldValue([fieldValue73])

fieldValue74 = fieldValue()
fieldValue74.name = "set_positionB"
fieldValue74.value = "50 50 -50"
ProtoInstance72.addFieldValue([fieldValue74])
Transform56.addChildren([ProtoInstance72])
Scene8.addChildren([Transform56])

Script75 = Script()
Script75.DEF = "clickHandler"

field76 = field()
field76.accessType = "inputOutput"
field76.name = "counter"
field76.value = "0"
field76.type = "SFInt32"
Script75.addField([field76])

field77 = field()
field77.accessType = "outputOnly"
field77.name = "node_changed"
field77.type = "SFNode"
Script75.addField([field77])

field78 = field()
field78.accessType = "inputOnly"
field78.name = "add_node"
field78.value = "false"
field78.type = "SFBool"
Script75.addField([field78])
#
#            <field name=\"ModifiableNode\" type=\"SFNode\" accessType=\"inputOutput\">
#                <Transform USE=\"HoldsContent\"/>
#            </field>
#	    

Script75.setSourceCode('''\n"+
"ecmascript:\n"+
"	function add_node(value) {\n"+
"                // Browser.print('hey ', counter);\n"+
"                counter = counter++;\n"+
"		Browser.appendTo(Browser.getDocument().querySelector(\"field [name=ModifiableNode]\"),\n"+
"			{ \"ProtoInstance\":\n"+
"				{ \"@name\":\"node\",\n"+
"				  \"@DEF\":\"node'+counter+'\",\n"+
"				  \"fieldValue\": [\n"+
"					{\n"+
"						 \"@name\":\"position\",\n"+
"						 \"@value\":[0.0,0.0,0.0]\n"+
"					}\n"+
"				  ]\n"+
"				}\n"+
"			});\n"+
"                \n"+
"        }\n"+
"	''')
Scene8.addChildren([Script75])

ROUTE79 = ROUTE()
ROUTE79.fromNode = "clickGenerator"
ROUTE79.fromField = "isActive"
ROUTE79.toNode = "clickHandler"
ROUTE79.toField = "add_node"
Scene8.addChildren([ROUTE79])

ROUTE80 = ROUTE()
ROUTE80.fromNode = "nodeA"
ROUTE80.fromField = "position"
ROUTE80.toNode = "linkA"
ROUTE80.toField = "set_positionA"
Scene8.addChildren([ROUTE80])

ROUTE81 = ROUTE()
ROUTE81.fromNode = "nodeB"
ROUTE81.fromField = "position"
ROUTE81.toNode = "linkA"
ROUTE81.toField = "set_positionB"
Scene8.addChildren([ROUTE81])

ROUTE82 = ROUTE()
ROUTE82.fromNode = "nodeA"
ROUTE82.fromField = "position"
ROUTE82.toNode = "linkB"
ROUTE82.toField = "set_positionA"
Scene8.addChildren([ROUTE82])

ROUTE83 = ROUTE()
ROUTE83.fromNode = "nodeC"
ROUTE83.fromField = "position"
ROUTE83.toNode = "linkB"
ROUTE83.toField = "set_positionB"
Scene8.addChildren([ROUTE83])

ROUTE84 = ROUTE()
ROUTE84.fromNode = "nodeA"
ROUTE84.fromField = "position"
ROUTE84.toNode = "linkC"
ROUTE84.toField = "set_positionA"
Scene8.addChildren([ROUTE84])

ROUTE85 = ROUTE()
ROUTE85.fromNode = "nodeD"
ROUTE85.fromField = "position"
ROUTE85.toNode = "linkC"
ROUTE85.toField = "set_positionB"
Scene8.addChildren([ROUTE85])
X3D0.scene = Scene8
