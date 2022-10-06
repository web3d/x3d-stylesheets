from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="arc.x3d"), 
    meta3 = meta(name="creator", content="John Carlson"), 
    meta4 = meta(name="generator", content="manual"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/arc.x3d"), 
    meta6 = meta(name="description", content="an attempt to implement an arc in a graph")), 
   Scene7 = Scene(    Viewpoint8 = Viewpoint(position=[0,0,5], orientation=[0,0,1,0], description="a moving graph"), 
    Background9 = Background(skyColor=[0.4,0.4,0.4]), 
    Transform10 = Transform(DEF="trans1",      Transform11 = Transform(DEF="rotscale1",       Shape12 = Shape(       Appearance13 = Appearance(        Material14 = Material(diffuseColor=[0.2,0.7,0.7])), 
       Cylinder15 = Cylinder(radius=0.1)))), 
    Transform16 = Transform(DEF="trans2",      Transform17 = Transform(DEF="rotscale2",       Shape18 = Shape(       Appearance19 = Appearance(        Material20 = Material(diffuseColor=[0.2,0.7,0.7])), 
       Cylinder21 = Cylinder(radius=0.1)))), 
    Transform22 = Transform(DEF="trans3",      Transform23 = Transform(DEF="rotscale3",       Shape24 = Shape(       Appearance25 = Appearance(        Material26 = Material(diffuseColor=[0.2,0.7,0.7])), 
       Cylinder27 = Cylinder(radius=0.1)))), 
    ProtoDeclare28 = ProtoDeclare(name="point",      ProtoInterface29 = ProtoInterface(      field30 = field(accessType="inputOutput", name="translation", type="SFVec3f", value="0 0 0")), 
     ProtoBody31 = ProtoBody(      Transform32 = Transform(DEF="node",        IS33 = IS(        connect34 = connect(nodeField="translation", protoField="translation")), 
       Shape35 = Shape(        Sphere36 = Sphere(radius=0.1), 
        Appearance37 = Appearance(         Material38 = Material(diffuseColor=[1,0,0]))), 
       PositionInterpolator39 = PositionInterpolator(DEF="PI1", key=[0,1], keyValue=[0,0,0,0,5,0]), 
       Script40 = Script(DEF="MB1",         field41 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="50 50 0"), 
        field42 = field(name="old", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
        field43 = field(name="set_location", accessType="inputOnly", type="SFTime"), 
        field44 = field(name="keyValue", accessType="outputOnly", type="MFVec3f"),         sourceCode = '''\n"+
"ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(translation);\n"+
"		}\n"+
"''', ), 
       TimeSensor45 = TimeSensor(DEF="CL1", cycleInterval=3, loop=True), 
       ROUTE46 = ROUTE(fromNode="CL1", fromField="cycleTime", toNode="MB1", toField="set_location"), 
       ROUTE47 = ROUTE(fromNode="CL1", fromField="fraction_changed", toNode="PI1", toField="set_fraction"), 
       ROUTE48 = ROUTE(fromNode="MB1", fromField="keyValue", toNode="PI1", toField="keyValue"), 
       ROUTE49 = ROUTE(fromNode="PI1", fromField="value_changed", toNode="node", toField="set_translation")))),     # from doug sanden 

    ProtoDeclare50 = ProtoDeclare(name="x3dconnector",      ProtoInterface51 = ProtoInterface(      field52 = field(accessType="inputOutput", name="startnode", type="SFNode"), 
      field53 = field(accessType="inputOutput", name="endnode", type="SFNode"), 
      field54 = field(accessType="inputOutput", name="transnode", type="SFNode"), 
      field55 = field(accessType="inputOutput", name="rotscalenode", type="SFNode"), 
      field56 = field(accessType="inputOnly", name="set_startpoint", type="SFVec3f"), 
      field57 = field(accessType="inputOnly", name="set_endpoint", type="SFVec3f")), 
     ProtoBody58 = ProtoBody(      Script59 = Script(DEF="S1",        field60 = field(accessType="inputOutput", name="startnode", type="SFNode"), 
       field61 = field(accessType="inputOutput", name="endnode", type="SFNode"), 
       field62 = field(accessType="inputOutput", name="transnode", type="SFNode"), 
       field63 = field(accessType="inputOutput", name="rotscalenode", type="SFNode"), 
       field64 = field(accessType="inputOnly", name="set_startpoint", type="SFVec3f"), 
       field65 = field(accessType="inputOnly", name="set_endpoint", type="SFVec3f"), 
       IS66 = IS(        connect67 = connect(nodeField="startnode", protoField="startnode"), 
        connect68 = connect(nodeField="endnode", protoField="endnode"), 
        connect69 = connect(nodeField="transnode", protoField="transnode"), 
        connect70 = connect(nodeField="rotscalenode", protoField="rotscalenode"), 
        connect71 = connect(nodeField="set_startpoint", protoField="set_startpoint"), 
        connect72 = connect(nodeField="set_endpoint", protoField="set_endpoint")),        sourceCode = '''ecmascript:\n"+
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
"''', ))), 
    ProtoInstance73 = ProtoInstance(DEF="G1", name="point"), 
    ProtoInstance74 = ProtoInstance(DEF="G2", name="point"), 
    ProtoInstance75 = ProtoInstance(DEF="G3", name="point"), 
    ProtoInstance76 = ProtoInstance(DEF="G4", name="point"), 
    ProtoInstance77 = ProtoInstance(name="x3dconnector", DEF="connector1",      fieldValue78 = fieldValue(name="startnode",       ProtoInstance79 = ProtoInstance(USE="G1")), 
     fieldValue80 = fieldValue(name="endnode",       ProtoInstance81 = ProtoInstance(USE="G2")), 
     fieldValue82 = fieldValue(name="transnode",       Transform83 = Transform(USE="trans1")), 
     fieldValue84 = fieldValue(name="rotscalenode",       Transform85 = Transform(USE="rotscale1"))), 
    ProtoInstance86 = ProtoInstance(name="x3dconnector", DEF="connector2",      fieldValue87 = fieldValue(name="startnode",       ProtoInstance88 = ProtoInstance(USE="G1")), 
     fieldValue89 = fieldValue(name="endnode",       ProtoInstance90 = ProtoInstance(USE="G3")), 
     fieldValue91 = fieldValue(name="transnode",       Transform92 = Transform(USE="trans2")), 
     fieldValue93 = fieldValue(name="rotscalenode",       Transform94 = Transform(USE="rotscale2"))), 
    ProtoInstance95 = ProtoInstance(name="x3dconnector", DEF="connector3",      fieldValue96 = fieldValue(name="startnode",       ProtoInstance97 = ProtoInstance(USE="G1")), 
     fieldValue98 = fieldValue(name="endnode",       ProtoInstance99 = ProtoInstance(USE="G4")), 
     fieldValue100 = fieldValue(name="transnode",       Transform101 = Transform(USE="trans3")), 
     fieldValue102 = fieldValue(name="rotscalenode",       Transform103 = Transform(USE="rotscale3"))), 
    ROUTE104 = ROUTE(fromNode="G1", fromField="translation_changed", toNode="connector1", toField="set_startpoint"), 
    ROUTE105 = ROUTE(fromNode="G2", fromField="translation_changed", toNode="connector1", toField="set_endpoint"), 
    ROUTE106 = ROUTE(fromNode="G1", fromField="translation_changed", toNode="connector2", toField="set_startpoint"), 
    ROUTE107 = ROUTE(fromNode="G3", fromField="translation_changed", toNode="connector2", toField="set_endpoint"), 
    ROUTE108 = ROUTE(fromNode="G1", fromField="translation_changed", toNode="connector3", toField="set_startpoint"), 
    ROUTE109 = ROUTE(fromNode="G4", fromField="translation_changed", toNode="connector3", toField="set_endpoint")))
