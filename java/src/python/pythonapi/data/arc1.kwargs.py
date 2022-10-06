from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="x3dconnectorProto"), 
    meta3 = meta(name="creator", content="Lost, Doug Sanden I think"), 
    meta4 = meta(name="generator", content="manual"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/x3dconnectorProto.x3d"), 
    meta6 = meta(name="description", content="a generic proto to connect two objects")), 
   Scene7 = Scene(    Viewpoint8 = Viewpoint(position=[0,0,5], description="Only Viewpoint", orientation=[0,0,1,0]), 
    Background9 = Background(skyColor=[0.4,0.4,0.4]), 
    ProtoDeclare10 = ProtoDeclare(name="point",      ProtoInterface11 = ProtoInterface(      field12 = field(accessType="inputOutput", name="translation", type="SFVec3f", value="0 0 0")), 
     ProtoBody13 = ProtoBody(      Transform14 = Transform(DEF="node",        IS15 = IS(        connect16 = connect(nodeField="translation", protoField="translation")), 
       Shape17 = Shape(        Sphere18 = Sphere(radius=0.1), 
        Appearance19 = Appearance(         Material20 = Material(diffuseColor=[1,0,0]))), 
       PositionInterpolator21 = PositionInterpolator(DEF="PI1", key=[0,1], keyValue=[0,0,0,0,5,0]), 
       Script22 = Script(DEF="MB1",         field23 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="50 50 0"), 
        field24 = field(name="old", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
        field25 = field(name="set_location", accessType="inputOnly", type="SFTime"), 
        field26 = field(name="keyValue", accessType="inputOutput", type="MFVec3f", value="0 0 0 0 5 0"),         sourceCode = '''\n"+
"ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}\n"+
"''', ), 
       TimeSensor27 = TimeSensor(DEF="CL1", cycleInterval=3, loop=True), 
       ROUTE28 = ROUTE(fromNode="CL1", fromField="cycleTime", toNode="MB1", toField="set_location"), 
       ROUTE29 = ROUTE(fromNode="CL1", fromField="fraction_changed", toNode="PI1", toField="set_fraction"), 
       ROUTE30 = ROUTE(fromNode="MB1", fromField="keyValue", toNode="PI1", toField="keyValue"), 
       ROUTE31 = ROUTE(fromNode="PI1", fromField="value_changed", toNode="node", toField="set_translation")))), 
    ProtoDeclare32 = ProtoDeclare(name="x3dconnector",      ProtoInterface33 = ProtoInterface(      field34 = field(accessType="initializeOnly", name="startnode", type="SFNode"), 
      field35 = field(accessType="initializeOnly", name="endnode", type="SFNode"), 
      field36 = field(accessType="inputOnly", name="set_startpoint", type="SFVec3f"), 
      field37 = field(accessType="inputOnly", name="set_endpoint", type="SFVec3f")), 
     ProtoBody38 = ProtoBody(      Group39 = Group(       Transform40 = Transform(DEF="trans", translation=[0,0,0],         Transform41 = Transform(DEF="rotscale",          Shape42 = Shape(          Appearance43 = Appearance(           Material44 = Material(diffuseColor=[0.2,0.7,0.7], transparency=.5)), 
          Cylinder45 = Cylinder(radius=.05)))), 
       Script46 = Script(DEF="S1",         field47 = field(accessType="initializeOnly", name="startnode", type="SFNode"), 
        field48 = field(accessType="initializeOnly", name="endnode", type="SFNode"), 
        field49 = field(accessType="inputOutput", name="position", type="SFNode",          Transform50 = Transform(USE="trans")), 
        field51 = field(accessType="inputOutput", name="rotscale", type="SFNode",          Transform52 = Transform(USE="rotscale")), 
        field53 = field(accessType="inputOnly", name="set_startpoint", type="SFVec3f"), 
        field54 = field(accessType="inputOnly", name="set_endpoint", type="SFVec3f"), 
        IS55 = IS(         connect56 = connect(nodeField="startnode", protoField="startnode"), 
         connect57 = connect(nodeField="endnode", protoField="endnode"), 
         connect58 = connect(nodeField="set_startpoint", protoField="set_startpoint"), 
         connect59 = connect(nodeField="set_endpoint", protoField="set_endpoint")),         sourceCode = '''ecmascript:\n"+
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
"            ''', )))), 
    ProtoInstance60 = ProtoInstance(DEF="G1", name="point"), 
    ProtoInstance61 = ProtoInstance(DEF="G2", name="point"), 
    ProtoInstance62 = ProtoInstance(name="x3dconnector", DEF="connector1",      fieldValue63 = fieldValue(name="startnode",       ProtoInstance64 = ProtoInstance(USE="G1")), 
     fieldValue65 = fieldValue(name="endnode",       ProtoInstance66 = ProtoInstance(USE="G2")), 
     fieldValue67 = fieldValue(name="set_startpoint"), 
     fieldValue68 = fieldValue(name="set_endpoint")), 
    ROUTE69 = ROUTE(fromNode="G1", fromField="translation", toNode="connector1", toField="set_startpoint"), 
    ROUTE70 = ROUTE(fromNode="G2", fromField="translation", toNode="connector1", toField="set_endpoint")))
