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
Transform24.DEF = "transC1"

Transform25 = Transform()
Transform25.DEF = "rotscaleC1"

Shape26 = Shape()

Appearance27 = Appearance()

Material28 = Material()
Material28.diffuseColor = [0.2,0.7,0.7]
Material28.transparency = .5
Appearance27.material = Material28
Shape26.appearance = Appearance27

Cylinder29 = Cylinder(radius = .05)
Shape26.geometry = Cylinder29
Transform25.addChildren([Shape26])
Transform24.addChildren([Transform25])
Scene7.addChildren([Transform24])

ProtoDeclare30 = ProtoDeclare()
ProtoDeclare30.name = "x3dconnector"

ProtoInterface31 = ProtoInterface()

field32 = field()
field32.accessType = "initializeOnly"
field32.name = "startnode"
field32.type = "SFNode"
ProtoInterface31.addField([field32])

field33 = field()
field33.accessType = "initializeOnly"
field33.name = "endnode"
field33.type = "SFNode"
ProtoInterface31.addField([field33])

field34 = field()
field34.accessType = "initializeOnly"
field34.name = "transnode"
field34.type = "SFNode"
ProtoInterface31.addField([field34])

field35 = field()
field35.accessType = "initializeOnly"
field35.name = "rotscalenode"
field35.type = "SFNode"
ProtoInterface31.addField([field35])

field36 = field()
field36.accessType = "inputOnly"
field36.name = "set_startpoint"
field36.type = "SFVec3f"
ProtoInterface31.addField([field36])

field37 = field()
field37.accessType = "inputOnly"
field37.name = "set_endpoint"
field37.type = "SFVec3f"
ProtoInterface31.addField([field37])
ProtoDeclare30.protoInterface = ProtoInterface31

ProtoBody38 = ProtoBody()

Script39 = Script()
Script39.DEF = "S1"

field40 = field()
field40.accessType = "initializeOnly"
field40.name = "startnode"
field40.type = "SFNode"
Script39.addField([field40])

field41 = field()
field41.accessType = "initializeOnly"
field41.name = "endnode"
field41.type = "SFNode"
Script39.addField([field41])

field42 = field()
field42.accessType = "initializeOnly"
field42.name = "transnode"
field42.type = "SFNode"
Script39.addField([field42])

field43 = field()
field43.accessType = "initializeOnly"
field43.name = "rotscalenode"
field43.type = "SFNode"
Script39.addField([field43])

field44 = field()
field44.accessType = "inputOnly"
field44.name = "set_startpoint"
field44.type = "SFVec3f"
Script39.addField([field44])

field45 = field()
field45.accessType = "inputOnly"
field45.name = "set_endpoint"
field45.type = "SFVec3f"
Script39.addField([field45])

IS46 = IS()

connect47 = connect()
connect47.nodeField = "startnode"
connect47.protoField = "startnode"
IS46.addConnect([connect47])

connect48 = connect()
connect48.nodeField = "endnode"
connect48.protoField = "endnode"
IS46.addConnect([connect48])

connect49 = connect()
connect49.nodeField = "transnode"
connect49.protoField = "transnode"
IS46.addConnect([connect49])

connect50 = connect()
connect50.nodeField = "rotscalenode"
connect50.protoField = "rotscalenode"
IS46.addConnect([connect50])

connect51 = connect()
connect51.nodeField = "set_startpoint"
connect51.protoField = "set_startpoint"
IS46.addConnect([connect51])

connect52 = connect()
connect52.nodeField = "set_endpoint"
connect52.protoField = "set_endpoint"
IS46.addConnect([connect52])
Script39.IS = IS46

Script39.setSourceCode('''ecmascript:\n"+
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
ProtoBody38.addChildren([Script39])
ProtoDeclare30.protoBody = ProtoBody38
Scene7.addChildren([ProtoDeclare30])

ProtoInstance53 = ProtoInstance()
ProtoInstance53.name = "x3dconnector"
ProtoInstance53.DEF = "connector1"

fieldValue54 = fieldValue()
fieldValue54.name = "startnode"

Transform55 = Transform()
Transform55.USE = "G1"
fieldValue54.addChildren([Transform55])
ProtoInstance53.addFieldValue([fieldValue54])

fieldValue56 = fieldValue()
fieldValue56.name = "endnode"

Transform57 = Transform()
Transform57.USE = "G2"
fieldValue56.addChildren([Transform57])
ProtoInstance53.addFieldValue([fieldValue56])

fieldValue58 = fieldValue()
fieldValue58.name = "transnode"

Transform59 = Transform()
Transform59.USE = "transC1"
fieldValue58.addChildren([Transform59])
ProtoInstance53.addFieldValue([fieldValue58])

fieldValue60 = fieldValue()
fieldValue60.name = "rotscalenode"

Transform61 = Transform()
Transform61.USE = "rotscaleC1"
fieldValue60.addChildren([Transform61])
ProtoInstance53.addFieldValue([fieldValue60])

fieldValue62 = fieldValue()
fieldValue62.name = "set_startpoint"
ProtoInstance53.addFieldValue([fieldValue62])

fieldValue63 = fieldValue()
fieldValue63.name = "set_endpoint"
ProtoInstance53.addFieldValue([fieldValue63])
Scene7.addChildren([ProtoInstance53])

ROUTE64 = ROUTE()
ROUTE64.fromNode = "G1"
ROUTE64.fromField = "translation_changed"
ROUTE64.toNode = "connector1"
ROUTE64.toField = "set_startpoint"
Scene7.addChildren([ROUTE64])

ROUTE65 = ROUTE()
ROUTE65.fromNode = "G2"
ROUTE65.fromField = "translation_changed"
ROUTE65.toNode = "connector1"
ROUTE65.toField = "set_endpoint"
Scene7.addChildren([ROUTE65])
X3D0.scene = Scene7
