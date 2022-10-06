from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "x3dconnectorProto"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "creator"
meta3.content = "Lost, Doug Sanden I think"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "generator"
meta4.content = "manual"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/x3dconnectorProto.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "a generic proto to connect two objects"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

Viewpoint8 = Viewpoint()
Viewpoint8.position = [0,0,5]
Viewpoint8.description = "Only Viewpoint"
Viewpoint8.orientation = [0,0,1,0]
Scene7.addChildren([Viewpoint8])

Background9 = Background()
Background9.skyColor = [0.4,0.4,0.4]
Scene7.addChildren([Background9])

ProtoDeclare10 = ProtoDeclare()
ProtoDeclare10.name = "point"

ProtoInterface11 = ProtoInterface()

field12 = field()
field12.accessType = "inputOutput"
field12.name = "translation"
field12.type = "SFVec3f"
field12.value = "0 0 0"
ProtoInterface11.addField([field12])
ProtoDeclare10.protoInterface = ProtoInterface11

ProtoBody13 = ProtoBody()

Transform14 = Transform()
Transform14.DEF = "node"

IS15 = IS()

connect16 = connect()
connect16.nodeField = "translation"
connect16.protoField = "translation"
IS15.addConnect([connect16])
Transform14.IS = IS15

Shape17 = Shape()

Sphere18 = Sphere(radius = 0.1)
Shape17.geometry = Sphere18

Appearance19 = Appearance()

Material20 = Material()
Material20.diffuseColor = [1,0,0]
Appearance19.material = Material20
Shape17.appearance = Appearance19
Transform14.addChildren([Shape17])

PositionInterpolator21 = PositionInterpolator()
PositionInterpolator21.DEF = "PI1"
PositionInterpolator21.key = [0,1]
PositionInterpolator21.keyValue = [0,0,0,0,5,0]
Transform14.addChildren([PositionInterpolator21])

Script22 = Script()
Script22.DEF = "MB1"

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
field25.name = "set_location"
field25.accessType = "inputOnly"
field25.type = "SFTime"
Script22.addField([field25])

field26 = field()
field26.name = "keyValue"
field26.accessType = "inputOutput"
field26.type = "MFVec3f"
field26.value = "0 0 0 0 5 0"
Script22.addField([field26])

Script22.setSourceCode('''\n"+
"ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}\n"+
"''')
Transform14.addChildren([Script22])

TimeSensor27 = TimeSensor()
TimeSensor27.DEF = "CL1"
TimeSensor27.cycleInterval = 3
TimeSensor27.loop = True
Transform14.addChildren([TimeSensor27])

ROUTE28 = ROUTE()
ROUTE28.fromNode = "CL1"
ROUTE28.fromField = "cycleTime"
ROUTE28.toNode = "MB1"
ROUTE28.toField = "set_location"
Transform14.addChildren([ROUTE28])

ROUTE29 = ROUTE()
ROUTE29.fromNode = "CL1"
ROUTE29.fromField = "fraction_changed"
ROUTE29.toNode = "PI1"
ROUTE29.toField = "set_fraction"
Transform14.addChildren([ROUTE29])

ROUTE30 = ROUTE()
ROUTE30.fromNode = "MB1"
ROUTE30.fromField = "keyValue"
ROUTE30.toNode = "PI1"
ROUTE30.toField = "keyValue"
Transform14.addChildren([ROUTE30])

ROUTE31 = ROUTE()
ROUTE31.fromNode = "PI1"
ROUTE31.fromField = "value_changed"
ROUTE31.toNode = "node"
ROUTE31.toField = "set_translation"
Transform14.addChildren([ROUTE31])
ProtoBody13.addChildren([Transform14])
ProtoDeclare10.protoBody = ProtoBody13
Scene7.addChildren([ProtoDeclare10])

ProtoDeclare32 = ProtoDeclare()
ProtoDeclare32.name = "x3dconnector"

ProtoInterface33 = ProtoInterface()

field34 = field()
field34.accessType = "initializeOnly"
field34.name = "startnode"
field34.type = "SFNode"
ProtoInterface33.addField([field34])

field35 = field()
field35.accessType = "initializeOnly"
field35.name = "endnode"
field35.type = "SFNode"
ProtoInterface33.addField([field35])

field36 = field()
field36.accessType = "inputOnly"
field36.name = "set_startpoint"
field36.type = "SFVec3f"
ProtoInterface33.addField([field36])

field37 = field()
field37.accessType = "inputOnly"
field37.name = "set_endpoint"
field37.type = "SFVec3f"
ProtoInterface33.addField([field37])
ProtoDeclare32.protoInterface = ProtoInterface33

ProtoBody38 = ProtoBody()

Group39 = Group()

Transform40 = Transform()
Transform40.DEF = "trans"
Transform40.translation = [0,0,0]

Transform41 = Transform()
Transform41.DEF = "rotscale"

Shape42 = Shape()

Appearance43 = Appearance()

Material44 = Material()
Material44.diffuseColor = [0.2,0.7,0.7]
Material44.transparency = .5
Appearance43.material = Material44
Shape42.appearance = Appearance43

Cylinder45 = Cylinder(radius = .05)
Shape42.geometry = Cylinder45
Transform41.addChildren([Shape42])
Transform40.addChildren([Transform41])
Group39.addChildren([Transform40])

Script46 = Script()
Script46.DEF = "S1"

field47 = field()
field47.accessType = "initializeOnly"
field47.name = "startnode"
field47.type = "SFNode"
Script46.addField([field47])

field48 = field()
field48.accessType = "initializeOnly"
field48.name = "endnode"
field48.type = "SFNode"
Script46.addField([field48])

field49 = field()
field49.accessType = "inputOutput"
field49.name = "position"
field49.type = "SFNode"

Transform50 = Transform()
Transform50.USE = "trans"
field49.addChildren([Transform50])
Script46.addField([field49])

field51 = field()
field51.accessType = "inputOutput"
field51.name = "rotscale"
field51.type = "SFNode"

Transform52 = Transform()
Transform52.USE = "rotscale"
field51.addChildren([Transform52])
Script46.addField([field51])

field53 = field()
field53.accessType = "inputOnly"
field53.name = "set_startpoint"
field53.type = "SFVec3f"
Script46.addField([field53])

field54 = field()
field54.accessType = "inputOnly"
field54.name = "set_endpoint"
field54.type = "SFVec3f"
Script46.addField([field54])

IS55 = IS()

connect56 = connect()
connect56.nodeField = "startnode"
connect56.protoField = "startnode"
IS55.addConnect([connect56])

connect57 = connect()
connect57.nodeField = "endnode"
connect57.protoField = "endnode"
IS55.addConnect([connect57])

connect58 = connect()
connect58.nodeField = "set_startpoint"
connect58.protoField = "set_startpoint"
IS55.addConnect([connect58])

connect59 = connect()
connect59.nodeField = "set_endpoint"
connect59.protoField = "set_endpoint"
IS55.addConnect([connect59])
Script46.IS = IS55

Script46.setSourceCode('''ecmascript:\n"+
"        function recompute(startpoint,endpoint){\n"+
"	    if (typeof endpoint === 'undefined') {\n"+
"		return;\n"+
"	    }\n"+
"            var dif = endpoint.subtract(startpoint);\n"+
"            var dist = dif.length()*0.5;\n"+
"            var dif2 = dif.multiply(0.5);\n"+
"            var norm = dif.normalize();\n"+
"            var transl = startpoint.add(dif2);\n"+
"	    if (typeof Quaternion !== 'undefined') {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new Quaternion.rotateFromTo(new SFVec3f(0.0,1.0,0.0), norm)\n"+
"		    };\n"+
"	    } else if (typeof SFRotation !== 'undefined') {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new SFRotation(new SFVec3f(0.0,1.0,0.0),norm)\n"+
"		    };\n"+
"	    } else {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl\n"+
"		    };\n"+
"	    }\n"+
"	}\n"+
"	function recompute_and_route(startpoint, endpoint) {\n"+
"	      var trafo = recompute(startpoint, endpoint);\n"+
"	      position.translation = trafo.translation;\n"+
"	      rotscale.rotation = trafo.rotation;\n"+
"	      rotscale.scale = trafo.scale;\n"+
"	}\n"+
"        function initialize(){\n"+
"            recompute_and_route(startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_startpoint(val,t){\n"+
"            recompute_and_route(val,endnode.translation);\n"+
"        }\n"+
"        function set_endpoint(val,t){\n"+
"            recompute_and_route(startnode.translation,val);\n"+
"        }\n"+
"            ''')
Group39.addChildren([Script46])
ProtoBody38.addChildren([Group39])
ProtoDeclare32.protoBody = ProtoBody38
Scene7.addChildren([ProtoDeclare32])

ProtoInstance60 = ProtoInstance()
ProtoInstance60.DEF = "G1"
ProtoInstance60.name = "point"
Scene7.addChildren([ProtoInstance60])

ProtoInstance61 = ProtoInstance()
ProtoInstance61.DEF = "G2"
ProtoInstance61.name = "point"
Scene7.addChildren([ProtoInstance61])

ProtoInstance62 = ProtoInstance()
ProtoInstance62.DEF = "G3"
ProtoInstance62.name = "point"
Scene7.addChildren([ProtoInstance62])

ProtoInstance63 = ProtoInstance()
ProtoInstance63.DEF = "G4"
ProtoInstance63.name = "point"
Scene7.addChildren([ProtoInstance63])

ProtoInstance64 = ProtoInstance()
ProtoInstance64.name = "x3dconnector"
ProtoInstance64.DEF = "connector1"

fieldValue65 = fieldValue()
fieldValue65.name = "startnode"

ProtoInstance66 = ProtoInstance()
ProtoInstance66.USE = "G1"
fieldValue65.addChildren([ProtoInstance66])
ProtoInstance64.addFieldValue([fieldValue65])

fieldValue67 = fieldValue()
fieldValue67.name = "endnode"

ProtoInstance68 = ProtoInstance()
ProtoInstance68.USE = "G2"
fieldValue67.addChildren([ProtoInstance68])
ProtoInstance64.addFieldValue([fieldValue67])

fieldValue69 = fieldValue()
fieldValue69.name = "set_startpoint"
ProtoInstance64.addFieldValue([fieldValue69])

fieldValue70 = fieldValue()
fieldValue70.name = "set_endpoint"
ProtoInstance64.addFieldValue([fieldValue70])
Scene7.addChildren([ProtoInstance64])

ProtoInstance71 = ProtoInstance()
ProtoInstance71.name = "x3dconnector"
ProtoInstance71.DEF = "connector2"

fieldValue72 = fieldValue()
fieldValue72.name = "startnode"

ProtoInstance73 = ProtoInstance()
ProtoInstance73.USE = "G1"
fieldValue72.addChildren([ProtoInstance73])
ProtoInstance71.addFieldValue([fieldValue72])

fieldValue74 = fieldValue()
fieldValue74.name = "endnode"

ProtoInstance75 = ProtoInstance()
ProtoInstance75.USE = "G3"
fieldValue74.addChildren([ProtoInstance75])
ProtoInstance71.addFieldValue([fieldValue74])

fieldValue76 = fieldValue()
fieldValue76.name = "set_startpoint"
ProtoInstance71.addFieldValue([fieldValue76])

fieldValue77 = fieldValue()
fieldValue77.name = "set_endpoint"
ProtoInstance71.addFieldValue([fieldValue77])
Scene7.addChildren([ProtoInstance71])

ProtoInstance78 = ProtoInstance()
ProtoInstance78.name = "x3dconnector"
ProtoInstance78.DEF = "connector3"

fieldValue79 = fieldValue()
fieldValue79.name = "startnode"

ProtoInstance80 = ProtoInstance()
ProtoInstance80.USE = "G1"
fieldValue79.addChildren([ProtoInstance80])
ProtoInstance78.addFieldValue([fieldValue79])

fieldValue81 = fieldValue()
fieldValue81.name = "endnode"

ProtoInstance82 = ProtoInstance()
ProtoInstance82.USE = "G4"
fieldValue81.addChildren([ProtoInstance82])
ProtoInstance78.addFieldValue([fieldValue81])

fieldValue83 = fieldValue()
fieldValue83.name = "set_startpoint"
ProtoInstance78.addFieldValue([fieldValue83])

fieldValue84 = fieldValue()
fieldValue84.name = "set_endpoint"
ProtoInstance78.addFieldValue([fieldValue84])
Scene7.addChildren([ProtoInstance78])

ROUTE85 = ROUTE()
ROUTE85.fromNode = "G1"
ROUTE85.fromField = "translation"
ROUTE85.toNode = "connector1"
ROUTE85.toField = "set_startpoint"
Scene7.addChildren([ROUTE85])

ROUTE86 = ROUTE()
ROUTE86.fromNode = "G2"
ROUTE86.fromField = "translation"
ROUTE86.toNode = "connector1"
ROUTE86.toField = "set_endpoint"
Scene7.addChildren([ROUTE86])

ROUTE87 = ROUTE()
ROUTE87.fromNode = "G1"
ROUTE87.fromField = "translation"
ROUTE87.toNode = "connector2"
ROUTE87.toField = "set_startpoint"
Scene7.addChildren([ROUTE87])

ROUTE88 = ROUTE()
ROUTE88.fromNode = "G3"
ROUTE88.fromField = "translation"
ROUTE88.toNode = "connector2"
ROUTE88.toField = "set_endpoint"
Scene7.addChildren([ROUTE88])

ROUTE89 = ROUTE()
ROUTE89.fromNode = "G1"
ROUTE89.fromField = "translation"
ROUTE89.toNode = "connector3"
ROUTE89.toField = "set_startpoint"
Scene7.addChildren([ROUTE89])

ROUTE90 = ROUTE()
ROUTE90.fromNode = "G4"
ROUTE90.fromField = "translation"
ROUTE90.toNode = "connector3"
ROUTE90.toField = "set_endpoint"
Scene7.addChildren([ROUTE90])
X3D0.scene = Scene7
