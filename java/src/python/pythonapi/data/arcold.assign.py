from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "arc.x3d"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "creator"
meta3.content = "John Carlson"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "generator"
meta4.content = "manual"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/arc.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "an attempt to implement an arc in a graph"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

Viewpoint8 = Viewpoint()
Viewpoint8.position = [0,0,5]
Viewpoint8.orientation = [0,0,1,0]
Viewpoint8.description = "a moving graph"
Scene7.addChildren([Viewpoint8])

Background9 = Background()
Background9.skyColor = [0.4,0.4,0.4]
Scene7.addChildren([Background9])

Transform10 = Transform()
Transform10.DEF = "trans1"

Transform11 = Transform()
Transform11.DEF = "rotscale1"

Shape12 = Shape()

Appearance13 = Appearance()

Material14 = Material()
Material14.diffuseColor = [0.2,0.7,0.7]
Appearance13.material = Material14
Shape12.appearance = Appearance13

Cylinder15 = Cylinder(radius = 0.1)
Shape12.geometry = Cylinder15
Transform11.addChildren([Shape12])
Transform10.addChildren([Transform11])
Scene7.addChildren([Transform10])

Transform16 = Transform()
Transform16.DEF = "trans2"

Transform17 = Transform()
Transform17.DEF = "rotscale2"

Shape18 = Shape()

Appearance19 = Appearance()

Material20 = Material()
Material20.diffuseColor = [0.2,0.7,0.7]
Appearance19.material = Material20
Shape18.appearance = Appearance19

Cylinder21 = Cylinder(radius = 0.1)
Shape18.geometry = Cylinder21
Transform17.addChildren([Shape18])
Transform16.addChildren([Transform17])
Scene7.addChildren([Transform16])

Transform22 = Transform()
Transform22.DEF = "trans3"

Transform23 = Transform()
Transform23.DEF = "rotscale3"

Shape24 = Shape()

Appearance25 = Appearance()

Material26 = Material()
Material26.diffuseColor = [0.2,0.7,0.7]
Appearance25.material = Material26
Shape24.appearance = Appearance25

Cylinder27 = Cylinder(radius = 0.1)
Shape24.geometry = Cylinder27
Transform23.addChildren([Shape24])
Transform22.addChildren([Transform23])
Scene7.addChildren([Transform22])

ProtoDeclare28 = ProtoDeclare()
ProtoDeclare28.name = "point"

ProtoInterface29 = ProtoInterface()

field30 = field()
field30.accessType = "inputOutput"
field30.name = "translation"
field30.type = "SFVec3f"
field30.value = "0 0 0"
ProtoInterface29.addField([field30])
ProtoDeclare28.protoInterface = ProtoInterface29

ProtoBody31 = ProtoBody()

Transform32 = Transform()
Transform32.DEF = "node"

IS33 = IS()

connect34 = connect()
connect34.nodeField = "translation"
connect34.protoField = "translation"
IS33.addConnect([connect34])
Transform32.IS = IS33

Shape35 = Shape()

Sphere36 = Sphere(radius = 0.1)
Shape35.geometry = Sphere36

Appearance37 = Appearance()

Material38 = Material()
Material38.diffuseColor = [1,0,0]
Appearance37.material = Material38
Shape35.appearance = Appearance37
Transform32.addChildren([Shape35])

PositionInterpolator39 = PositionInterpolator()
PositionInterpolator39.DEF = "PI1"
PositionInterpolator39.key = [0,1]
PositionInterpolator39.keyValue = [0,0,0,0,5,0]
Transform32.addChildren([PositionInterpolator39])

Script40 = Script()
Script40.DEF = "MB1"

field41 = field()
field41.name = "translation"
field41.accessType = "inputOutput"
field41.type = "SFVec3f"
field41.value = "50 50 0"
Script40.addField([field41])

field42 = field()
field42.name = "old"
field42.accessType = "inputOutput"
field42.type = "SFVec3f"
field42.value = "0 0 0"
Script40.addField([field42])

field43 = field()
field43.name = "set_location"
field43.accessType = "inputOnly"
field43.type = "SFTime"
Script40.addField([field43])

field44 = field()
field44.name = "keyValue"
field44.accessType = "outputOnly"
field44.type = "MFVec3f"
Script40.addField([field44])

Script40.setSourceCode('''\n"+
"ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(translation);\n"+
"		}\n"+
"''')
Transform32.addChildren([Script40])

TimeSensor45 = TimeSensor()
TimeSensor45.DEF = "CL1"
TimeSensor45.cycleInterval = 3
TimeSensor45.loop = True
Transform32.addChildren([TimeSensor45])

ROUTE46 = ROUTE()
ROUTE46.fromNode = "CL1"
ROUTE46.fromField = "cycleTime"
ROUTE46.toNode = "MB1"
ROUTE46.toField = "set_location"
Transform32.addChildren([ROUTE46])

ROUTE47 = ROUTE()
ROUTE47.fromNode = "CL1"
ROUTE47.fromField = "fraction_changed"
ROUTE47.toNode = "PI1"
ROUTE47.toField = "set_fraction"
Transform32.addChildren([ROUTE47])

ROUTE48 = ROUTE()
ROUTE48.fromNode = "MB1"
ROUTE48.fromField = "keyValue"
ROUTE48.toNode = "PI1"
ROUTE48.toField = "keyValue"
Transform32.addChildren([ROUTE48])

ROUTE49 = ROUTE()
ROUTE49.fromNode = "PI1"
ROUTE49.fromField = "value_changed"
ROUTE49.toNode = "node"
ROUTE49.toField = "set_translation"
Transform32.addChildren([ROUTE49])
ProtoBody31.addChildren([Transform32])
ProtoDeclare28.protoBody = ProtoBody31
Scene7.addChildren([ProtoDeclare28])
# from doug sanden 

ProtoDeclare50 = ProtoDeclare()
ProtoDeclare50.name = "x3dconnector"

ProtoInterface51 = ProtoInterface()

field52 = field()
field52.accessType = "inputOutput"
field52.name = "startnode"
field52.type = "SFNode"
ProtoInterface51.addField([field52])

field53 = field()
field53.accessType = "inputOutput"
field53.name = "endnode"
field53.type = "SFNode"
ProtoInterface51.addField([field53])

field54 = field()
field54.accessType = "inputOutput"
field54.name = "transnode"
field54.type = "SFNode"
ProtoInterface51.addField([field54])

field55 = field()
field55.accessType = "inputOutput"
field55.name = "rotscalenode"
field55.type = "SFNode"
ProtoInterface51.addField([field55])

field56 = field()
field56.accessType = "inputOnly"
field56.name = "set_startpoint"
field56.type = "SFVec3f"
ProtoInterface51.addField([field56])

field57 = field()
field57.accessType = "inputOnly"
field57.name = "set_endpoint"
field57.type = "SFVec3f"
ProtoInterface51.addField([field57])
ProtoDeclare50.protoInterface = ProtoInterface51

ProtoBody58 = ProtoBody()

Script59 = Script()
Script59.DEF = "S1"

field60 = field()
field60.accessType = "inputOutput"
field60.name = "startnode"
field60.type = "SFNode"
Script59.addField([field60])

field61 = field()
field61.accessType = "inputOutput"
field61.name = "endnode"
field61.type = "SFNode"
Script59.addField([field61])

field62 = field()
field62.accessType = "inputOutput"
field62.name = "transnode"
field62.type = "SFNode"
Script59.addField([field62])

field63 = field()
field63.accessType = "inputOutput"
field63.name = "rotscalenode"
field63.type = "SFNode"
Script59.addField([field63])

field64 = field()
field64.accessType = "inputOnly"
field64.name = "set_startpoint"
field64.type = "SFVec3f"
Script59.addField([field64])

field65 = field()
field65.accessType = "inputOnly"
field65.name = "set_endpoint"
field65.type = "SFVec3f"
Script59.addField([field65])

IS66 = IS()

connect67 = connect()
connect67.nodeField = "startnode"
connect67.protoField = "startnode"
IS66.addConnect([connect67])

connect68 = connect()
connect68.nodeField = "endnode"
connect68.protoField = "endnode"
IS66.addConnect([connect68])

connect69 = connect()
connect69.nodeField = "transnode"
connect69.protoField = "transnode"
IS66.addConnect([connect69])

connect70 = connect()
connect70.nodeField = "rotscalenode"
connect70.protoField = "rotscalenode"
IS66.addConnect([connect70])

connect71 = connect()
connect71.nodeField = "set_startpoint"
connect71.protoField = "set_startpoint"
IS66.addConnect([connect71])

connect72 = connect()
connect72.nodeField = "set_endpoint"
connect72.protoField = "set_endpoint"
IS66.addConnect([connect72])
Script59.IS = IS66

Script59.setSourceCode('''ecmascript:\n"+
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
"	    } else {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new SFRotation(new SFVec3f(0.0,1.0,0.0),norm)\n"+
"		    };\n"+
"	    }\n"+
"	}\n"+
"	function recompute_and_route(startpoint, endpoint) {\n"+
"		var trafo = recompute(startpoint, endpoint);\n"+
"		if (typeof trafo !== 'undefined') {\n"+
"			transnode.translation = trafo.translation;\n"+
"			rotscalenode.rotation = trafo.rotation;\n"+
"			rotscalenode.scale = trafo.scale;\n"+
"		} else {\n"+
"			Browser.print(\"recompute returned undefined\");\n"+
"		}\n"+
"	}\n"+
"        function initialize(){\n"+
"            recompute_and_route(startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_startpoint(val,t){\n"+
"            recompute_and_route(val || startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_endpoint(val,t){\n"+
"            recompute_and_route(startnode.translation,val || endnode.translation);\n"+
"        }\n"+
"''')
ProtoBody58.addChildren([Script59])
ProtoDeclare50.protoBody = ProtoBody58
Scene7.addChildren([ProtoDeclare50])

ProtoInstance73 = ProtoInstance()
ProtoInstance73.DEF = "G1"
ProtoInstance73.name = "point"
Scene7.addChildren([ProtoInstance73])

ProtoInstance74 = ProtoInstance()
ProtoInstance74.DEF = "G2"
ProtoInstance74.name = "point"
Scene7.addChildren([ProtoInstance74])

ProtoInstance75 = ProtoInstance()
ProtoInstance75.DEF = "G3"
ProtoInstance75.name = "point"
Scene7.addChildren([ProtoInstance75])

ProtoInstance76 = ProtoInstance()
ProtoInstance76.DEF = "G4"
ProtoInstance76.name = "point"
Scene7.addChildren([ProtoInstance76])

ProtoInstance77 = ProtoInstance()
ProtoInstance77.name = "x3dconnector"
ProtoInstance77.DEF = "connector1"

fieldValue78 = fieldValue()
fieldValue78.name = "startnode"

ProtoInstance79 = ProtoInstance()
ProtoInstance79.USE = "G1"
fieldValue78.addChildren([ProtoInstance79])
ProtoInstance77.addFieldValue([fieldValue78])

fieldValue80 = fieldValue()
fieldValue80.name = "endnode"

ProtoInstance81 = ProtoInstance()
ProtoInstance81.USE = "G2"
fieldValue80.addChildren([ProtoInstance81])
ProtoInstance77.addFieldValue([fieldValue80])

fieldValue82 = fieldValue()
fieldValue82.name = "transnode"

Transform83 = Transform()
Transform83.USE = "trans1"
fieldValue82.addChildren([Transform83])
ProtoInstance77.addFieldValue([fieldValue82])

fieldValue84 = fieldValue()
fieldValue84.name = "rotscalenode"

Transform85 = Transform()
Transform85.USE = "rotscale1"
fieldValue84.addChildren([Transform85])
ProtoInstance77.addFieldValue([fieldValue84])
Scene7.addChildren([ProtoInstance77])

ProtoInstance86 = ProtoInstance()
ProtoInstance86.name = "x3dconnector"
ProtoInstance86.DEF = "connector2"

fieldValue87 = fieldValue()
fieldValue87.name = "startnode"

ProtoInstance88 = ProtoInstance()
ProtoInstance88.USE = "G1"
fieldValue87.addChildren([ProtoInstance88])
ProtoInstance86.addFieldValue([fieldValue87])

fieldValue89 = fieldValue()
fieldValue89.name = "endnode"

ProtoInstance90 = ProtoInstance()
ProtoInstance90.USE = "G3"
fieldValue89.addChildren([ProtoInstance90])
ProtoInstance86.addFieldValue([fieldValue89])

fieldValue91 = fieldValue()
fieldValue91.name = "transnode"

Transform92 = Transform()
Transform92.USE = "trans2"
fieldValue91.addChildren([Transform92])
ProtoInstance86.addFieldValue([fieldValue91])

fieldValue93 = fieldValue()
fieldValue93.name = "rotscalenode"

Transform94 = Transform()
Transform94.USE = "rotscale2"
fieldValue93.addChildren([Transform94])
ProtoInstance86.addFieldValue([fieldValue93])
Scene7.addChildren([ProtoInstance86])

ProtoInstance95 = ProtoInstance()
ProtoInstance95.name = "x3dconnector"
ProtoInstance95.DEF = "connector3"

fieldValue96 = fieldValue()
fieldValue96.name = "startnode"

ProtoInstance97 = ProtoInstance()
ProtoInstance97.USE = "G1"
fieldValue96.addChildren([ProtoInstance97])
ProtoInstance95.addFieldValue([fieldValue96])

fieldValue98 = fieldValue()
fieldValue98.name = "endnode"

ProtoInstance99 = ProtoInstance()
ProtoInstance99.USE = "G4"
fieldValue98.addChildren([ProtoInstance99])
ProtoInstance95.addFieldValue([fieldValue98])

fieldValue100 = fieldValue()
fieldValue100.name = "transnode"

Transform101 = Transform()
Transform101.USE = "trans3"
fieldValue100.addChildren([Transform101])
ProtoInstance95.addFieldValue([fieldValue100])

fieldValue102 = fieldValue()
fieldValue102.name = "rotscalenode"

Transform103 = Transform()
Transform103.USE = "rotscale3"
fieldValue102.addChildren([Transform103])
ProtoInstance95.addFieldValue([fieldValue102])
Scene7.addChildren([ProtoInstance95])

ROUTE104 = ROUTE()
ROUTE104.fromNode = "G1"
ROUTE104.fromField = "translation_changed"
ROUTE104.toNode = "connector1"
ROUTE104.toField = "set_startpoint"
Scene7.addChildren([ROUTE104])

ROUTE105 = ROUTE()
ROUTE105.fromNode = "G2"
ROUTE105.fromField = "translation_changed"
ROUTE105.toNode = "connector1"
ROUTE105.toField = "set_endpoint"
Scene7.addChildren([ROUTE105])

ROUTE106 = ROUTE()
ROUTE106.fromNode = "G1"
ROUTE106.fromField = "translation_changed"
ROUTE106.toNode = "connector2"
ROUTE106.toField = "set_startpoint"
Scene7.addChildren([ROUTE106])

ROUTE107 = ROUTE()
ROUTE107.fromNode = "G3"
ROUTE107.fromField = "translation_changed"
ROUTE107.toNode = "connector2"
ROUTE107.toField = "set_endpoint"
Scene7.addChildren([ROUTE107])

ROUTE108 = ROUTE()
ROUTE108.fromNode = "G1"
ROUTE108.fromField = "translation_changed"
ROUTE108.toNode = "connector3"
ROUTE108.toField = "set_startpoint"
Scene7.addChildren([ROUTE108])

ROUTE109 = ROUTE()
ROUTE109.fromNode = "G4"
ROUTE109.fromField = "translation_changed"
ROUTE109.toNode = "connector3"
ROUTE109.toField = "set_endpoint"
Scene7.addChildren([ROUTE109])
X3D0.scene = Scene7
