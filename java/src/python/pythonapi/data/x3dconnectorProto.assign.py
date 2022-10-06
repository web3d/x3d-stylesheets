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

Transform10 = Transform()
Transform10.DEF = "G1"

Shape11 = Shape()

Appearance12 = Appearance()

Material13 = Material()
Material13.diffuseColor = [0.7,0.2,0.2]
Appearance12.material = Material13
Shape11.appearance = Appearance12

Sphere14 = Sphere(radius = .1)
Shape11.geometry = Sphere14
Transform10.addChildren([Shape11])

PlaneSensor15 = PlaneSensor()
PlaneSensor15.description = "Grab to move"
PlaneSensor15.DEF = "PS1"
Transform10.addChildren([PlaneSensor15])

ROUTE16 = ROUTE()
ROUTE16.fromNode = "PS1"
ROUTE16.fromField = "translation_changed"
ROUTE16.toNode = "G1"
ROUTE16.toField = "set_translation"
Transform10.addChildren([ROUTE16])
Scene7.addChildren([Transform10])

Transform17 = Transform()
Transform17.DEF = "G2"
Transform17.translation = [1,-1,.01]

Shape18 = Shape()

Appearance19 = Appearance()

Material20 = Material()
Material20.diffuseColor = [0.2,0.7,0.2]
Appearance19.material = Material20
Shape18.appearance = Appearance19

Sphere21 = Sphere(radius = .1)
Shape18.geometry = Sphere21
Transform17.addChildren([Shape18])

PlaneSensor22 = PlaneSensor()
PlaneSensor22.description = "Grab to move"
PlaneSensor22.offset = [1,-1,.01]
PlaneSensor22.DEF = "PS2"
Transform17.addChildren([PlaneSensor22])

ROUTE23 = ROUTE()
ROUTE23.fromNode = "PS2"
ROUTE23.fromField = "translation_changed"
ROUTE23.toNode = "G2"
ROUTE23.toField = "set_translation"
Transform17.addChildren([ROUTE23])
Scene7.addChildren([Transform17])

Transform24 = Transform()
Transform24.DEF = "G3"
Transform24.translation = [1,1,.01]

Shape25 = Shape()

Appearance26 = Appearance()

Material27 = Material()
Material27.diffuseColor = [0.2,0.7,0.2]
Appearance26.material = Material27
Shape25.appearance = Appearance26

Sphere28 = Sphere(radius = .1)
Shape25.geometry = Sphere28
Transform24.addChildren([Shape25])

PlaneSensor29 = PlaneSensor()
PlaneSensor29.description = "Grab to move"
PlaneSensor29.offset = [1,1,.01]
PlaneSensor29.DEF = "PS3"
Transform24.addChildren([PlaneSensor29])

ROUTE30 = ROUTE()
ROUTE30.fromNode = "PS3"
ROUTE30.fromField = "translation_changed"
ROUTE30.toNode = "G3"
ROUTE30.toField = "set_translation"
Transform24.addChildren([ROUTE30])
Scene7.addChildren([Transform24])

Transform31 = Transform()
Transform31.DEF = "G4"
Transform31.translation = [-1,1,.01]

Shape32 = Shape()

Appearance33 = Appearance()

Material34 = Material()
Material34.diffuseColor = [0.2,0.7,0.2]
Appearance33.material = Material34
Shape32.appearance = Appearance33

Sphere35 = Sphere(radius = .1)
Shape32.geometry = Sphere35
Transform31.addChildren([Shape32])

PlaneSensor36 = PlaneSensor()
PlaneSensor36.description = "Grab to move"
PlaneSensor36.offset = [-1,1,.01]
PlaneSensor36.DEF = "PS4"
Transform31.addChildren([PlaneSensor36])

ROUTE37 = ROUTE()
ROUTE37.fromNode = "PS4"
ROUTE37.fromField = "translation_changed"
ROUTE37.toNode = "G4"
ROUTE37.toField = "set_translation"
Transform31.addChildren([ROUTE37])
Scene7.addChildren([Transform31])

Transform38 = Transform()
Transform38.DEF = "transC1"

Transform39 = Transform()
Transform39.DEF = "rotscaleC1"

Shape40 = Shape()

Appearance41 = Appearance()

Material42 = Material()
Material42.diffuseColor = [0.2,0.7,0.7]
Material42.transparency = .5
Appearance41.material = Material42
Shape40.appearance = Appearance41

Cylinder43 = Cylinder(radius = .05)
Shape40.geometry = Cylinder43
Transform39.addChildren([Shape40])
Transform38.addChildren([Transform39])
Scene7.addChildren([Transform38])

Transform44 = Transform()
Transform44.DEF = "transC2"

Transform45 = Transform()
Transform45.DEF = "rotscaleC2"

Shape46 = Shape()

Appearance47 = Appearance()

Material48 = Material()
Material48.diffuseColor = [0.2,0.7,0.7]
Material48.transparency = .5
Appearance47.material = Material48
Shape46.appearance = Appearance47

Cylinder49 = Cylinder(radius = .05)
Shape46.geometry = Cylinder49
Transform45.addChildren([Shape46])
Transform44.addChildren([Transform45])
Scene7.addChildren([Transform44])

Transform50 = Transform()
Transform50.DEF = "transC3"

Transform51 = Transform()
Transform51.DEF = "rotscaleC3"

Shape52 = Shape()

Appearance53 = Appearance()

Material54 = Material()
Material54.diffuseColor = [0.2,0.7,0.7]
Material54.transparency = .5
Appearance53.material = Material54
Shape52.appearance = Appearance53

Cylinder55 = Cylinder(radius = .05)
Shape52.geometry = Cylinder55
Transform51.addChildren([Shape52])
Transform50.addChildren([Transform51])
Scene7.addChildren([Transform50])

ProtoDeclare56 = ProtoDeclare()
ProtoDeclare56.name = "x3dconnector"

ProtoInterface57 = ProtoInterface()

field58 = field()
field58.accessType = "initializeOnly"
field58.name = "startnode"
field58.type = "SFNode"
ProtoInterface57.addField([field58])

field59 = field()
field59.accessType = "initializeOnly"
field59.name = "endnode"
field59.type = "SFNode"
ProtoInterface57.addField([field59])

field60 = field()
field60.accessType = "initializeOnly"
field60.name = "transnode"
field60.type = "SFNode"
ProtoInterface57.addField([field60])

field61 = field()
field61.accessType = "initializeOnly"
field61.name = "rotscalenode"
field61.type = "SFNode"
ProtoInterface57.addField([field61])

field62 = field()
field62.accessType = "inputOnly"
field62.name = "set_startpoint"
field62.type = "SFVec3f"
ProtoInterface57.addField([field62])

field63 = field()
field63.accessType = "inputOnly"
field63.name = "set_endpoint"
field63.type = "SFVec3f"
ProtoInterface57.addField([field63])
ProtoDeclare56.protoInterface = ProtoInterface57

ProtoBody64 = ProtoBody()

Script65 = Script()
Script65.DEF = "S1"

field66 = field()
field66.accessType = "initializeOnly"
field66.name = "startnode"
field66.type = "SFNode"
Script65.addField([field66])

field67 = field()
field67.accessType = "initializeOnly"
field67.name = "endnode"
field67.type = "SFNode"
Script65.addField([field67])

field68 = field()
field68.accessType = "initializeOnly"
field68.name = "transnode"
field68.type = "SFNode"
Script65.addField([field68])

field69 = field()
field69.accessType = "initializeOnly"
field69.name = "rotscalenode"
field69.type = "SFNode"
Script65.addField([field69])

field70 = field()
field70.accessType = "inputOnly"
field70.name = "set_startpoint"
field70.type = "SFVec3f"
Script65.addField([field70])

field71 = field()
field71.accessType = "inputOnly"
field71.name = "set_endpoint"
field71.type = "SFVec3f"
Script65.addField([field71])

IS72 = IS()

connect73 = connect()
connect73.nodeField = "startnode"
connect73.protoField = "startnode"
IS72.addConnect([connect73])

connect74 = connect()
connect74.nodeField = "endnode"
connect74.protoField = "endnode"
IS72.addConnect([connect74])

connect75 = connect()
connect75.nodeField = "transnode"
connect75.protoField = "transnode"
IS72.addConnect([connect75])

connect76 = connect()
connect76.nodeField = "rotscalenode"
connect76.protoField = "rotscalenode"
IS72.addConnect([connect76])

connect77 = connect()
connect77.nodeField = "set_startpoint"
connect77.protoField = "set_startpoint"
IS72.addConnect([connect77])

connect78 = connect()
connect78.nodeField = "set_endpoint"
connect78.protoField = "set_endpoint"
IS72.addConnect([connect78])
Script65.IS = IS72

Script65.setSourceCode('''ecmascript:\n"+
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
"	      var trafo = recompute(startpoint, endpoint);\n"+
"	      transnode.translation = trafo.translation;\n"+
"	      rotscalenode.rotation = trafo.rotation;\n"+
"	      rotscalenode.scale = trafo.scale;\n"+
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
ProtoBody64.addChildren([Script65])
ProtoDeclare56.protoBody = ProtoBody64
Scene7.addChildren([ProtoDeclare56])

ProtoInstance79 = ProtoInstance()
ProtoInstance79.name = "x3dconnector"
ProtoInstance79.DEF = "connector1"

fieldValue80 = fieldValue()
fieldValue80.name = "startnode"

Transform81 = Transform()
Transform81.USE = "G1"
fieldValue80.addChildren([Transform81])
ProtoInstance79.addFieldValue([fieldValue80])

fieldValue82 = fieldValue()
fieldValue82.name = "endnode"

Transform83 = Transform()
Transform83.USE = "G2"
fieldValue82.addChildren([Transform83])
ProtoInstance79.addFieldValue([fieldValue82])

fieldValue84 = fieldValue()
fieldValue84.name = "transnode"

Transform85 = Transform()
Transform85.USE = "transC1"
fieldValue84.addChildren([Transform85])
ProtoInstance79.addFieldValue([fieldValue84])

fieldValue86 = fieldValue()
fieldValue86.name = "rotscalenode"

Transform87 = Transform()
Transform87.USE = "rotscaleC1"
fieldValue86.addChildren([Transform87])
ProtoInstance79.addFieldValue([fieldValue86])

fieldValue88 = fieldValue()
fieldValue88.name = "set_startpoint"
ProtoInstance79.addFieldValue([fieldValue88])

fieldValue89 = fieldValue()
fieldValue89.name = "set_endpoint"
ProtoInstance79.addFieldValue([fieldValue89])
Scene7.addChildren([ProtoInstance79])

ProtoInstance90 = ProtoInstance()
ProtoInstance90.name = "x3dconnector"
ProtoInstance90.DEF = "connector2"

fieldValue91 = fieldValue()
fieldValue91.name = "startnode"

Transform92 = Transform()
Transform92.USE = "G1"
fieldValue91.addChildren([Transform92])
ProtoInstance90.addFieldValue([fieldValue91])

fieldValue93 = fieldValue()
fieldValue93.name = "endnode"

Transform94 = Transform()
Transform94.USE = "G3"
fieldValue93.addChildren([Transform94])
ProtoInstance90.addFieldValue([fieldValue93])

fieldValue95 = fieldValue()
fieldValue95.name = "transnode"

Transform96 = Transform()
Transform96.USE = "transC2"
fieldValue95.addChildren([Transform96])
ProtoInstance90.addFieldValue([fieldValue95])

fieldValue97 = fieldValue()
fieldValue97.name = "rotscalenode"

Transform98 = Transform()
Transform98.USE = "rotscaleC2"
fieldValue97.addChildren([Transform98])
ProtoInstance90.addFieldValue([fieldValue97])

fieldValue99 = fieldValue()
fieldValue99.name = "set_startpoint"
ProtoInstance90.addFieldValue([fieldValue99])

fieldValue100 = fieldValue()
fieldValue100.name = "set_endpoint"
ProtoInstance90.addFieldValue([fieldValue100])
Scene7.addChildren([ProtoInstance90])

ProtoInstance101 = ProtoInstance()
ProtoInstance101.name = "x3dconnector"
ProtoInstance101.DEF = "connector3"

fieldValue102 = fieldValue()
fieldValue102.name = "startnode"

Transform103 = Transform()
Transform103.USE = "G1"
fieldValue102.addChildren([Transform103])
ProtoInstance101.addFieldValue([fieldValue102])

fieldValue104 = fieldValue()
fieldValue104.name = "endnode"

Transform105 = Transform()
Transform105.USE = "G4"
fieldValue104.addChildren([Transform105])
ProtoInstance101.addFieldValue([fieldValue104])

fieldValue106 = fieldValue()
fieldValue106.name = "transnode"

Transform107 = Transform()
Transform107.USE = "transC3"
fieldValue106.addChildren([Transform107])
ProtoInstance101.addFieldValue([fieldValue106])

fieldValue108 = fieldValue()
fieldValue108.name = "rotscalenode"

Transform109 = Transform()
Transform109.USE = "rotscaleC3"
fieldValue108.addChildren([Transform109])
ProtoInstance101.addFieldValue([fieldValue108])

fieldValue110 = fieldValue()
fieldValue110.name = "set_startpoint"
ProtoInstance101.addFieldValue([fieldValue110])

fieldValue111 = fieldValue()
fieldValue111.name = "set_endpoint"
ProtoInstance101.addFieldValue([fieldValue111])
Scene7.addChildren([ProtoInstance101])

ROUTE112 = ROUTE()
ROUTE112.fromNode = "G1"
ROUTE112.fromField = "translation_changed"
ROUTE112.toNode = "connector1"
ROUTE112.toField = "set_startpoint"
Scene7.addChildren([ROUTE112])

ROUTE113 = ROUTE()
ROUTE113.fromNode = "G2"
ROUTE113.fromField = "translation_changed"
ROUTE113.toNode = "connector1"
ROUTE113.toField = "set_endpoint"
Scene7.addChildren([ROUTE113])

ROUTE114 = ROUTE()
ROUTE114.fromNode = "G1"
ROUTE114.fromField = "translation_changed"
ROUTE114.toNode = "connector2"
ROUTE114.toField = "set_startpoint"
Scene7.addChildren([ROUTE114])

ROUTE115 = ROUTE()
ROUTE115.fromNode = "G3"
ROUTE115.fromField = "translation_changed"
ROUTE115.toNode = "connector2"
ROUTE115.toField = "set_endpoint"
Scene7.addChildren([ROUTE115])

ROUTE116 = ROUTE()
ROUTE116.fromNode = "G1"
ROUTE116.fromField = "translation_changed"
ROUTE116.toNode = "connector3"
ROUTE116.toField = "set_startpoint"
Scene7.addChildren([ROUTE116])

ROUTE117 = ROUTE()
ROUTE117.fromNode = "G4"
ROUTE117.fromField = "translation_changed"
ROUTE117.toNode = "connector3"
ROUTE117.toField = "set_endpoint"
Scene7.addChildren([ROUTE117])
X3D0.scene = Scene7
