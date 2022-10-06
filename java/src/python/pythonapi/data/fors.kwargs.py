from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="creator", content="John W Carlson"), 
    meta3 = meta(name="created", content="December 13 2015"), 
    meta4 = meta(name="title", content="force.x3d"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/force.x3d"), 
    meta6 = meta(name="description", content="beginnings of a force directed graph in 3D"), 
    meta7 = meta(name="generator", content="Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit")), 
   Scene8 = Scene(    ProtoDeclare9 = ProtoDeclare(name="node",      ProtoInterface10 = ProtoInterface(      field11 = field(name="position", accessType="inputOutput", type="SFVec3f", value="0 0 0")), 
     ProtoBody12 = ProtoBody(      Transform13 = Transform(DEF="transform",        IS14 = IS(        connect15 = connect(nodeField="translation", protoField="position")), 
       Shape16 = Shape(        Sphere17 = Sphere(), 
        Appearance18 = Appearance(         Material19 = Material(diffuseColor=[1,0,0]))), 
       Transform20 = Transform(translation=[1,0,0],         Shape21 = Shape(         Text22 = Text(string=["Node"],           FontStyle23 = FontStyle(family=["SERIF"], justify=["MIDDLE","MIDDLE"], size=5)), 
         Appearance24 = Appearance(          Material25 = Material(diffuseColor=[0,0,1]))))), 
      PositionInterpolator26 = PositionInterpolator(DEF="NodePosition", key=[0,1], keyValue=[0,0,0,0,5,0]), 
      Script27 = Script(DEF="MoveBall",        field28 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="50 50 0"), 
       field29 = field(name="old", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
       field30 = field(name="set_cycle", accessType="inputOnly", type="SFTime"), 
       field31 = field(name="keyValue", accessType="outputOnly", type="MFVec3f"),        sourceCode = '''\n"+
"ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f([old, translation]);\n"+
"						// Browser.println(translation);\n"+
"					}\n"+
"''', ), 
      TimeSensor32 = TimeSensor(DEF="nodeClock", cycleInterval=3, loop=True), 
      ROUTE33 = ROUTE(fromNode="nodeClock", fromField="cycleTime", toNode="MoveBall", toField="set_cycle"), 
      ROUTE34 = ROUTE(fromNode="nodeClock", fromField="fraction_changed", toNode="NodePosition", toField="set_fraction"), 
      ROUTE35 = ROUTE(fromNode="MoveBall", fromField="keyValue", toNode="NodePosition", toField="keyValue"), 
      ROUTE36 = ROUTE(fromNode="NodePosition", fromField="value_changed", toNode="transform", toField="set_translation"))), 
    ProtoDeclare37 = ProtoDeclare(name="cylinder",      ProtoInterface38 = ProtoInterface(      field39 = field(name="set_positionA", accessType="inputOnly", type="SFVec3f"), 
      field40 = field(name="set_positionB", accessType="inputOnly", type="SFVec3f")), 
     ProtoBody41 = ProtoBody(      Shape42 = Shape(       Extrusion43 = Extrusion(DEF="extrusion", creaseAngle=0.785, crossSection=[1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00], spine=[0,-50,0,0,50,0]), 
       Appearance44 = Appearance(        Material45 = Material(diffuseColor=[0,1,0]))), 
      Script46 = Script(DEF="MoveCylinder",        field47 = field(name="spine", accessType="inputOutput", type="MFVec3f", value="0 -50 0 0 50 0"), 
       field48 = field(name="set_endA", accessType="inputOnly", type="SFVec3f"), 
       field49 = field(name="set_endB", accessType="inputOnly", type="SFVec3f"), 
       IS50 = IS(        connect51 = connect(nodeField="set_endA", protoField="set_positionA"), 
        connect52 = connect(nodeField="set_endB", protoField="set_positionB")),        sourceCode = '''\n"+
"ecmascript:\n"+
"\n"+
"                function set_endA(value) {\n"+
"		    if (typeof spine === 'undefined') {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([value, spine[1]]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_endB(value) {\n"+
"		    if (typeof spine === 'undefined') {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([spine[0], value]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_spine(value) {\n"+
"                    spine = value;\n"+
"                }\n"+
"''', ), 
      ROUTE53 = ROUTE(fromNode="MoveCylinder", fromField="spine", toNode="extrusion", toField="set_spine"))), 
    Transform54 = Transform(DEF="HoldsContent", scale=[0.1,0.1,0.1],      PlaneSensor55 = PlaneSensor(DEF="clickGenerator", enabled=True, minPosition=[-50,-50], maxPosition=[50,50], description="click on background to add nodes, click on nodes to add links"), 
     ProtoInstance56 = ProtoInstance(DEF="nodeA", name="node",       fieldValue57 = fieldValue(name="position", value="0.0 0.0 0.0")), 
     ProtoInstance58 = ProtoInstance(DEF="nodeB", name="node",       fieldValue59 = fieldValue(name="position", value="50.0 50.0 50.0")), 
     ProtoInstance60 = ProtoInstance(DEF="linkA", name="cylinder",       fieldValue61 = fieldValue(name="set_positionA", value="0 0 0"), 
      fieldValue62 = fieldValue(name="set_positionB", value="50 50 50"))), 
    ROUTE63 = ROUTE(fromNode="nodeA", fromField="position", toNode="linkA", toField="set_positionA"), 
    ROUTE64 = ROUTE(fromNode="nodeB", fromField="position", toNode="linkA", toField="set_positionB")))
