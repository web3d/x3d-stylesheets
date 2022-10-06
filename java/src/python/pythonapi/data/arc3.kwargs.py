from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="x3dconnectorProto"), 
    meta3 = meta(name="creator", content="Lost, Doug Sanden I think"), 
    meta4 = meta(name="generator", content="manual"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/x3dconnectorProto.x3d"), 
    meta6 = meta(name="description", content="a generic proto to connect two objects")), 
   Scene7 = Scene(    Viewpoint8 = Viewpoint(position=[0,0,5], description="Only Viewpoint"), 
    Background9 = Background(skyColor=[0.4,0.4,0.4]), 
    Transform10 = Transform(DEF="DECLpoint_G1_node", translation=[0,0,0],      Shape11 = Shape(      Sphere12 = Sphere(radius=0.1), 
      Appearance13 = Appearance(       Material14 = Material(diffuseColor=[1,0,0]))), 
     PositionInterpolator15 = PositionInterpolator(DEF="DECLpoint_G1_PI1", key=[0,1], keyValue=[0,0,0,0,5,0]), 
     Script16 = Script(DEF="DECLpoint_G1_MB1",       field17 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
      field18 = field(name="old", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
      field19 = field(name="set_location", accessType="inputOnly", type="SFTime"), 
      field20 = field(name="keyValue", accessType="inputOutput", type="MFVec3f", value="0 0 0 0 5 0"),       sourceCode = '''ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}\n"+
"''', ), 
     TimeSensor21 = TimeSensor(DEF="DECLpoint_G1_CL1", cycleInterval=3, loop=True), 
     ROUTE22 = ROUTE(fromNode="DECLpoint_G1_CL1", fromField="cycleTime", toNode="DECLpoint_G1_MB1", toField="set_location"), 
     ROUTE23 = ROUTE(fromNode="DECLpoint_G1_CL1", fromField="fraction_changed", toNode="DECLpoint_G1_PI1", toField="set_fraction"), 
     ROUTE24 = ROUTE(fromNode="DECLpoint_G1_MB1", fromField="keyValue", toNode="DECLpoint_G1_PI1", toField="keyValue"), 
     ROUTE25 = ROUTE(fromNode="DECLpoint_G1_PI1", fromField="value_changed", toNode="DECLpoint_G1_node", toField="set_translation")), 
    Transform26 = Transform(DEF="DECLpoint_G2_node", translation=[0,0,0],      Shape27 = Shape(      Sphere28 = Sphere(radius=0.1), 
      Appearance29 = Appearance(       Material30 = Material(diffuseColor=[1,0,0]))), 
     PositionInterpolator31 = PositionInterpolator(DEF="DECLpoint_G2_PI1", key=[0,1], keyValue=[0,0,0,0,5,0]), 
     Script32 = Script(DEF="DECLpoint_G2_MB1",       field33 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
      field34 = field(name="old", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
      field35 = field(name="set_location", accessType="inputOnly", type="SFTime"), 
      field36 = field(name="keyValue", accessType="inputOutput", type="MFVec3f", value="0 0 0 0 5 0"),       sourceCode = '''ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}\n"+
"''', ), 
     TimeSensor37 = TimeSensor(DEF="DECLpoint_G2_CL1", cycleInterval=3, loop=True), 
     ROUTE38 = ROUTE(fromNode="DECLpoint_G2_CL1", fromField="cycleTime", toNode="DECLpoint_G2_MB1", toField="set_location"), 
     ROUTE39 = ROUTE(fromNode="DECLpoint_G2_CL1", fromField="fraction_changed", toNode="DECLpoint_G2_PI1", toField="set_fraction"), 
     ROUTE40 = ROUTE(fromNode="DECLpoint_G2_MB1", fromField="keyValue", toNode="DECLpoint_G2_PI1", toField="keyValue"), 
     ROUTE41 = ROUTE(fromNode="DECLpoint_G2_PI1", fromField="value_changed", toNode="DECLpoint_G2_node", toField="set_translation")), 
    Group42 = Group(     Transform43 = Transform(DEF="DECLx3dconnector_connector1_trans",       Transform44 = Transform(DEF="DECLx3dconnector_connector1_rotscale",        Shape45 = Shape(        Appearance46 = Appearance(         Material47 = Material(diffuseColor=[0.2,0.7,0.7], transparency=0.5)), 
        Cylinder48 = Cylinder(radius=0.05)))), 
     Script49 = Script(DEF="DECLx3dconnector_connector1_S1",       field50 = field(name="startnode", accessType="initializeOnly", type="SFNode",        Group51 = Group(USE="DECLpoint_G1_node")), 
      field52 = field(name="endnode", accessType="initializeOnly", type="SFNode",        Group53 = Group(USE="DECLpoint_G2_node")), 
      field54 = field(name="position", accessType="inputOutput", type="SFNode",        Transform55 = Transform(USE="DECLx3dconnector_connector1_trans")), 
      field56 = field(name="rotscale", accessType="inputOutput", type="SFNode",        Transform57 = Transform(USE="DECLx3dconnector_connector1_rotscale")), 
      field58 = field(name="set_startpoint", accessType="inputOnly", type="SFVec3f"), 
      field59 = field(name="set_endpoint", accessType="inputOnly", type="SFVec3f"),       sourceCode = '''ecmascript:\n"+
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
"''', )), 
    ROUTE60 = ROUTE(fromNode="DECLpoint_G1_node", fromField="translation", toNode="DECLx3dconnector_connector1_S1", toField="set_startpoint"), 
    ROUTE61 = ROUTE(fromNode="DECLpoint_G2_node", fromField="translation", toNode="DECLx3dconnector_connector1_S1", toField="set_endpoint")))
