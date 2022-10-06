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
Scene7.addChildren([Viewpoint8])

Background9 = Background()
Background9.skyColor = [0.4,0.4,0.4]
Scene7.addChildren([Background9])

Transform10 = Transform()
Transform10.DEF = "DECLpoint_G1_node"
Transform10.translation = [0,0,0]

Shape11 = Shape()

Sphere12 = Sphere(radius = 0.1)
Shape11.geometry = Sphere12

Appearance13 = Appearance()

Material14 = Material()
Material14.diffuseColor = [1,0,0]
Appearance13.material = Material14
Shape11.appearance = Appearance13
Transform10.addChildren([Shape11])

PositionInterpolator15 = PositionInterpolator()
PositionInterpolator15.DEF = "DECLpoint_G1_PI1"
PositionInterpolator15.key = [0,1]
PositionInterpolator15.keyValue = [0,0,0,0,5,0]
Transform10.addChildren([PositionInterpolator15])

Script16 = Script()
Script16.DEF = "DECLpoint_G1_MB1"

field17 = field()
field17.name = "translation"
field17.accessType = "inputOutput"
field17.type = "SFVec3f"
field17.value = "0 0 0"
Script16.addField([field17])

field18 = field()
field18.name = "old"
field18.accessType = "inputOutput"
field18.type = "SFVec3f"
field18.value = "0 0 0"
Script16.addField([field18])

field19 = field()
field19.name = "set_location"
field19.accessType = "inputOnly"
field19.type = "SFTime"
Script16.addField([field19])

field20 = field()
field20.name = "keyValue"
field20.accessType = "inputOutput"
field20.type = "MFVec3f"
field20.value = "0 0 0 0 5 0"
Script16.addField([field20])

Script16.setSourceCode('''ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}\n"+
"''')
Transform10.addChildren([Script16])

TimeSensor21 = TimeSensor()
TimeSensor21.DEF = "DECLpoint_G1_CL1"
TimeSensor21.cycleInterval = 3
TimeSensor21.loop = True
Transform10.addChildren([TimeSensor21])

ROUTE22 = ROUTE()
ROUTE22.fromNode = "DECLpoint_G1_CL1"
ROUTE22.fromField = "cycleTime"
ROUTE22.toNode = "DECLpoint_G1_MB1"
ROUTE22.toField = "set_location"
Transform10.addChildren([ROUTE22])

ROUTE23 = ROUTE()
ROUTE23.fromNode = "DECLpoint_G1_CL1"
ROUTE23.fromField = "fraction_changed"
ROUTE23.toNode = "DECLpoint_G1_PI1"
ROUTE23.toField = "set_fraction"
Transform10.addChildren([ROUTE23])

ROUTE24 = ROUTE()
ROUTE24.fromNode = "DECLpoint_G1_MB1"
ROUTE24.fromField = "keyValue"
ROUTE24.toNode = "DECLpoint_G1_PI1"
ROUTE24.toField = "keyValue"
Transform10.addChildren([ROUTE24])

ROUTE25 = ROUTE()
ROUTE25.fromNode = "DECLpoint_G1_PI1"
ROUTE25.fromField = "value_changed"
ROUTE25.toNode = "DECLpoint_G1_node"
ROUTE25.toField = "set_translation"
Transform10.addChildren([ROUTE25])
Scene7.addChildren([Transform10])

Transform26 = Transform()
Transform26.DEF = "DECLpoint_G2_node"
Transform26.translation = [0,0,0]

Shape27 = Shape()

Sphere28 = Sphere(radius = 0.1)
Shape27.geometry = Sphere28

Appearance29 = Appearance()

Material30 = Material()
Material30.diffuseColor = [1,0,0]
Appearance29.material = Material30
Shape27.appearance = Appearance29
Transform26.addChildren([Shape27])

PositionInterpolator31 = PositionInterpolator()
PositionInterpolator31.DEF = "DECLpoint_G2_PI1"
PositionInterpolator31.key = [0,1]
PositionInterpolator31.keyValue = [0,0,0,0,5,0]
Transform26.addChildren([PositionInterpolator31])

Script32 = Script()
Script32.DEF = "DECLpoint_G2_MB1"

field33 = field()
field33.name = "translation"
field33.accessType = "inputOutput"
field33.type = "SFVec3f"
field33.value = "0 0 0"
Script32.addField([field33])

field34 = field()
field34.name = "old"
field34.accessType = "inputOutput"
field34.type = "SFVec3f"
field34.value = "0 0 0"
Script32.addField([field34])

field35 = field()
field35.name = "set_location"
field35.accessType = "inputOnly"
field35.type = "SFTime"
Script32.addField([field35])

field36 = field()
field36.name = "keyValue"
field36.accessType = "inputOutput"
field36.type = "MFVec3f"
field36.value = "0 0 0 0 5 0"
Script32.addField([field36])

Script32.setSourceCode('''ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}\n"+
"''')
Transform26.addChildren([Script32])

TimeSensor37 = TimeSensor()
TimeSensor37.DEF = "DECLpoint_G2_CL1"
TimeSensor37.cycleInterval = 3
TimeSensor37.loop = True
Transform26.addChildren([TimeSensor37])

ROUTE38 = ROUTE()
ROUTE38.fromNode = "DECLpoint_G2_CL1"
ROUTE38.fromField = "cycleTime"
ROUTE38.toNode = "DECLpoint_G2_MB1"
ROUTE38.toField = "set_location"
Transform26.addChildren([ROUTE38])

ROUTE39 = ROUTE()
ROUTE39.fromNode = "DECLpoint_G2_CL1"
ROUTE39.fromField = "fraction_changed"
ROUTE39.toNode = "DECLpoint_G2_PI1"
ROUTE39.toField = "set_fraction"
Transform26.addChildren([ROUTE39])

ROUTE40 = ROUTE()
ROUTE40.fromNode = "DECLpoint_G2_MB1"
ROUTE40.fromField = "keyValue"
ROUTE40.toNode = "DECLpoint_G2_PI1"
ROUTE40.toField = "keyValue"
Transform26.addChildren([ROUTE40])

ROUTE41 = ROUTE()
ROUTE41.fromNode = "DECLpoint_G2_PI1"
ROUTE41.fromField = "value_changed"
ROUTE41.toNode = "DECLpoint_G2_node"
ROUTE41.toField = "set_translation"
Transform26.addChildren([ROUTE41])
Scene7.addChildren([Transform26])

Group42 = Group()

Transform43 = Transform()
Transform43.DEF = "DECLx3dconnector_connector1_trans"

Transform44 = Transform()
Transform44.DEF = "DECLx3dconnector_connector1_rotscale"

Shape45 = Shape()

Appearance46 = Appearance()

Material47 = Material()
Material47.diffuseColor = [0.2,0.7,0.7]
Material47.transparency = 0.5
Appearance46.material = Material47
Shape45.appearance = Appearance46

Cylinder48 = Cylinder(radius = 0.05)
Shape45.geometry = Cylinder48
Transform44.addChildren([Shape45])
Transform43.addChildren([Transform44])
Group42.addChildren([Transform43])

Script49 = Script()
Script49.DEF = "DECLx3dconnector_connector1_S1"

field50 = field()
field50.name = "startnode"
field50.accessType = "initializeOnly"
field50.type = "SFNode"

Group51 = Group()
Group51.USE = "DECLpoint_G1_node"
field50.addChildren([Group51])
Script49.addField([field50])

field52 = field()
field52.name = "endnode"
field52.accessType = "initializeOnly"
field52.type = "SFNode"

Group53 = Group()
Group53.USE = "DECLpoint_G2_node"
field52.addChildren([Group53])
Script49.addField([field52])

field54 = field()
field54.name = "position"
field54.accessType = "inputOutput"
field54.type = "SFNode"

Transform55 = Transform()
Transform55.USE = "DECLx3dconnector_connector1_trans"
field54.addChildren([Transform55])
Script49.addField([field54])

field56 = field()
field56.name = "rotscale"
field56.accessType = "inputOutput"
field56.type = "SFNode"

Transform57 = Transform()
Transform57.USE = "DECLx3dconnector_connector1_rotscale"
field56.addChildren([Transform57])
Script49.addField([field56])

field58 = field()
field58.name = "set_startpoint"
field58.accessType = "inputOnly"
field58.type = "SFVec3f"
Script49.addField([field58])

field59 = field()
field59.name = "set_endpoint"
field59.accessType = "inputOnly"
field59.type = "SFVec3f"
Script49.addField([field59])

Script49.setSourceCode('''ecmascript:\n"+
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
"''')
Group42.addChildren([Script49])
Scene7.addChildren([Group42])

ROUTE60 = ROUTE()
ROUTE60.fromNode = "DECLpoint_G1_node"
ROUTE60.fromField = "translation"
ROUTE60.toNode = "DECLx3dconnector_connector1_S1"
ROUTE60.toField = "set_startpoint"
Scene7.addChildren([ROUTE60])

ROUTE61 = ROUTE()
ROUTE61.fromNode = "DECLpoint_G2_node"
ROUTE61.fromField = "translation"
ROUTE61.toNode = "DECLx3dconnector_connector1_S1"
ROUTE61.toField = "set_endpoint"
Scene7.addChildren([ROUTE61])
X3D0.scene = Scene7
