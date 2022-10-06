from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="x3dconnectorProto"), 
    meta3 = meta(name="creator", content="Lost, Doug Sanden I think"), 
    meta4 = meta(name="generator", content="manual"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/x3dconnectorProto.x3d"), 
    meta6 = meta(name="description", content="a generic proto to connect two objects")), 
   Scene7 = Scene(    Viewpoint8 = Viewpoint(position=[0,0,5], description="Only Viewpoint", orientation=[0,0,1,0]), 
    Background9 = Background(skyColor=[0.4,0.4,0.4]), 
    Transform10 = Transform(DEF="G1",      Shape11 = Shape(      Appearance12 = Appearance(       Material13 = Material(diffuseColor=[0.7,0.2,0.2])), 
      Sphere14 = Sphere(radius=.1)), 
     PlaneSensor15 = PlaneSensor(description="Grab to move", DEF="PS1"), 
     ROUTE16 = ROUTE(fromNode="PS1", fromField="translation_changed", toNode="G1", toField="set_translation")), 
    Transform17 = Transform(DEF="G2", translation=[1,-1,.01],      Shape18 = Shape(      Appearance19 = Appearance(       Material20 = Material(diffuseColor=[0.2,0.7,0.2])), 
      Sphere21 = Sphere(radius=.1)), 
     PlaneSensor22 = PlaneSensor(description="Grab to move", offset=[1,-1,.01], DEF="PS2"), 
     ROUTE23 = ROUTE(fromNode="PS2", fromField="translation_changed", toNode="G2", toField="set_translation")), 
    Transform24 = Transform(DEF="transC1",      Transform25 = Transform(DEF="rotscaleC1",       Shape26 = Shape(       Appearance27 = Appearance(        Material28 = Material(diffuseColor=[0.2,0.7,0.7], transparency=.5)), 
       Cylinder29 = Cylinder(radius=.05)))), 
    ProtoDeclare30 = ProtoDeclare(name="x3dconnector",      ProtoInterface31 = ProtoInterface(      field32 = field(accessType="initializeOnly", name="startnode", type="SFNode"), 
      field33 = field(accessType="initializeOnly", name="endnode", type="SFNode"), 
      field34 = field(accessType="initializeOnly", name="transnode", type="SFNode"), 
      field35 = field(accessType="initializeOnly", name="rotscalenode", type="SFNode"), 
      field36 = field(accessType="inputOnly", name="set_startpoint", type="SFVec3f"), 
      field37 = field(accessType="inputOnly", name="set_endpoint", type="SFVec3f")), 
     ProtoBody38 = ProtoBody(      Script39 = Script(DEF="S1",        field40 = field(accessType="initializeOnly", name="startnode", type="SFNode"), 
       field41 = field(accessType="initializeOnly", name="endnode", type="SFNode"), 
       field42 = field(accessType="initializeOnly", name="transnode", type="SFNode"), 
       field43 = field(accessType="initializeOnly", name="rotscalenode", type="SFNode"), 
       field44 = field(accessType="inputOnly", name="set_startpoint", type="SFVec3f"), 
       field45 = field(accessType="inputOnly", name="set_endpoint", type="SFVec3f"), 
       IS46 = IS(        connect47 = connect(nodeField="startnode", protoField="startnode"), 
        connect48 = connect(nodeField="endnode", protoField="endnode"), 
        connect49 = connect(nodeField="transnode", protoField="transnode"), 
        connect50 = connect(nodeField="rotscalenode", protoField="rotscalenode"), 
        connect51 = connect(nodeField="set_startpoint", protoField="set_startpoint"), 
        connect52 = connect(nodeField="set_endpoint", protoField="set_endpoint")),        sourceCode = '''ecmascript:\n"+
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
"            ''', ))), 
    ProtoInstance53 = ProtoInstance(name="x3dconnector", DEF="connector1",      fieldValue54 = fieldValue(name="startnode",       Transform55 = Transform(USE="G1")), 
     fieldValue56 = fieldValue(name="endnode",       Transform57 = Transform(USE="G2")), 
     fieldValue58 = fieldValue(name="transnode",       Transform59 = Transform(USE="transC1")), 
     fieldValue60 = fieldValue(name="rotscalenode",       Transform61 = Transform(USE="rotscaleC1")), 
     fieldValue62 = fieldValue(name="set_startpoint"), 
     fieldValue63 = fieldValue(name="set_endpoint")), 
    ROUTE64 = ROUTE(fromNode="G1", fromField="translation_changed", toNode="connector1", toField="set_startpoint"), 
    ROUTE65 = ROUTE(fromNode="G2", fromField="translation_changed", toNode="connector1", toField="set_endpoint")))
