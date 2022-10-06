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
    Transform24 = Transform(DEF="G3", translation=[1,1,.01],      Shape25 = Shape(      Appearance26 = Appearance(       Material27 = Material(diffuseColor=[0.2,0.7,0.2])), 
      Sphere28 = Sphere(radius=.1)), 
     PlaneSensor29 = PlaneSensor(description="Grab to move", offset=[1,1,.01], DEF="PS3"), 
     ROUTE30 = ROUTE(fromNode="PS3", fromField="translation_changed", toNode="G3", toField="set_translation")), 
    Transform31 = Transform(DEF="G4", translation=[-1,1,.01],      Shape32 = Shape(      Appearance33 = Appearance(       Material34 = Material(diffuseColor=[0.2,0.7,0.2])), 
      Sphere35 = Sphere(radius=.1)), 
     PlaneSensor36 = PlaneSensor(description="Grab to move", offset=[-1,1,.01], DEF="PS4"), 
     ROUTE37 = ROUTE(fromNode="PS4", fromField="translation_changed", toNode="G4", toField="set_translation")), 
    Transform38 = Transform(DEF="transC1",      Transform39 = Transform(DEF="rotscaleC1",       Shape40 = Shape(       Appearance41 = Appearance(        Material42 = Material(diffuseColor=[0.2,0.7,0.7], transparency=.5)), 
       Cylinder43 = Cylinder(radius=.05)))), 
    Transform44 = Transform(DEF="transC2",      Transform45 = Transform(DEF="rotscaleC2",       Shape46 = Shape(       Appearance47 = Appearance(        Material48 = Material(diffuseColor=[0.2,0.7,0.7], transparency=.5)), 
       Cylinder49 = Cylinder(radius=.05)))), 
    Transform50 = Transform(DEF="transC3",      Transform51 = Transform(DEF="rotscaleC3",       Shape52 = Shape(       Appearance53 = Appearance(        Material54 = Material(diffuseColor=[0.2,0.7,0.7], transparency=.5)), 
       Cylinder55 = Cylinder(radius=.05)))), 
    ProtoDeclare56 = ProtoDeclare(name="x3dconnector",      ProtoInterface57 = ProtoInterface(      field58 = field(accessType="initializeOnly", name="startnode", type="SFNode"), 
      field59 = field(accessType="initializeOnly", name="endnode", type="SFNode"), 
      field60 = field(accessType="initializeOnly", name="transnode", type="SFNode"), 
      field61 = field(accessType="initializeOnly", name="rotscalenode", type="SFNode"), 
      field62 = field(accessType="inputOnly", name="set_startpoint", type="SFVec3f"), 
      field63 = field(accessType="inputOnly", name="set_endpoint", type="SFVec3f")), 
     ProtoBody64 = ProtoBody(      Script65 = Script(DEF="S1",        field66 = field(accessType="initializeOnly", name="startnode", type="SFNode"), 
       field67 = field(accessType="initializeOnly", name="endnode", type="SFNode"), 
       field68 = field(accessType="initializeOnly", name="transnode", type="SFNode"), 
       field69 = field(accessType="initializeOnly", name="rotscalenode", type="SFNode"), 
       field70 = field(accessType="inputOnly", name="set_startpoint", type="SFVec3f"), 
       field71 = field(accessType="inputOnly", name="set_endpoint", type="SFVec3f"), 
       IS72 = IS(        connect73 = connect(nodeField="startnode", protoField="startnode"), 
        connect74 = connect(nodeField="endnode", protoField="endnode"), 
        connect75 = connect(nodeField="transnode", protoField="transnode"), 
        connect76 = connect(nodeField="rotscalenode", protoField="rotscalenode"), 
        connect77 = connect(nodeField="set_startpoint", protoField="set_startpoint"), 
        connect78 = connect(nodeField="set_endpoint", protoField="set_endpoint")),        sourceCode = '''ecmascript:\n"+
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
    ProtoInstance79 = ProtoInstance(name="x3dconnector", DEF="connector1",      fieldValue80 = fieldValue(name="startnode",       Transform81 = Transform(USE="G1")), 
     fieldValue82 = fieldValue(name="endnode",       Transform83 = Transform(USE="G2")), 
     fieldValue84 = fieldValue(name="transnode",       Transform85 = Transform(USE="transC1")), 
     fieldValue86 = fieldValue(name="rotscalenode",       Transform87 = Transform(USE="rotscaleC1")), 
     fieldValue88 = fieldValue(name="set_startpoint"), 
     fieldValue89 = fieldValue(name="set_endpoint")), 
    ProtoInstance90 = ProtoInstance(name="x3dconnector", DEF="connector2",      fieldValue91 = fieldValue(name="startnode",       Transform92 = Transform(USE="G1")), 
     fieldValue93 = fieldValue(name="endnode",       Transform94 = Transform(USE="G3")), 
     fieldValue95 = fieldValue(name="transnode",       Transform96 = Transform(USE="transC2")), 
     fieldValue97 = fieldValue(name="rotscalenode",       Transform98 = Transform(USE="rotscaleC2")), 
     fieldValue99 = fieldValue(name="set_startpoint"), 
     fieldValue100 = fieldValue(name="set_endpoint")), 
    ProtoInstance101 = ProtoInstance(name="x3dconnector", DEF="connector3",      fieldValue102 = fieldValue(name="startnode",       Transform103 = Transform(USE="G1")), 
     fieldValue104 = fieldValue(name="endnode",       Transform105 = Transform(USE="G4")), 
     fieldValue106 = fieldValue(name="transnode",       Transform107 = Transform(USE="transC3")), 
     fieldValue108 = fieldValue(name="rotscalenode",       Transform109 = Transform(USE="rotscaleC3")), 
     fieldValue110 = fieldValue(name="set_startpoint"), 
     fieldValue111 = fieldValue(name="set_endpoint")), 
    ROUTE112 = ROUTE(fromNode="G1", fromField="translation_changed", toNode="connector1", toField="set_startpoint"), 
    ROUTE113 = ROUTE(fromNode="G2", fromField="translation_changed", toNode="connector1", toField="set_endpoint"), 
    ROUTE114 = ROUTE(fromNode="G1", fromField="translation_changed", toNode="connector2", toField="set_startpoint"), 
    ROUTE115 = ROUTE(fromNode="G3", fromField="translation_changed", toNode="connector2", toField="set_endpoint"), 
    ROUTE116 = ROUTE(fromNode="G1", fromField="translation_changed", toNode="connector3", toField="set_startpoint"), 
    ROUTE117 = ROUTE(fromNode="G4", fromField="translation_changed", toNode="connector3", toField="set_endpoint")))
