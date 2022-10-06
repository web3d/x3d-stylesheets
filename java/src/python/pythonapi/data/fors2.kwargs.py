from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="creator", content="John W Carlson"), 
    meta3 = meta(name="created", content="December 13 2015"), 
    meta4 = meta(name="modified", content="April 18 2017"), 
    meta5 = meta(name="title", content="fors2.x3d"), 
    meta6 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/fors2.x3d"), 
    meta7 = meta(name="description", content="beginnings of a force directed graph in 3D"), 
    meta8 = meta(name="generator", content="Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit")), 
   Scene9 = Scene(    ProtoDeclare10 = ProtoDeclare(name="node",      ProtoInterface11 = ProtoInterface(      field12 = field(name="position", accessType="inputOutput", type="SFVec3f", value="0 0 0")), 
     ProtoBody13 = ProtoBody(      Transform14 = Transform(DEF="transform",        IS15 = IS(        connect16 = connect(nodeField="translation", protoField="position")), 
       Shape17 = Shape(        #comment before Sphere
        #comment after Sphere
        #comment after Appearance

        Sphere18 = Sphere(), 
        Appearance19 = Appearance(         #comment before Material
         #comment after Material

         Material20 = Material(diffuseColor=[1,0,0])))), 
      PositionInterpolator21 = PositionInterpolator(DEF="NodePosition", key=[0,1], keyValue=[0,0,0,0,5,0]), 
      Script22 = Script(DEF="MoveBall",        field23 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="50 50 0"), 
       field24 = field(name="old", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
       field25 = field(name="set_cycle", accessType="inputOnly", type="SFTime"), 
       field26 = field(name="keyValue", accessType="outputOnly", type="MFVec3f"),        sourceCode = ''' ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f([old, translation]);\n"+
"						// Browser.println(translation);\n"+
"					}\n"+
" ''', ), 
      TimeSensor27 = TimeSensor(DEF="nodeClock", cycleInterval=3, loop=True), 
      ROUTE28 = ROUTE(fromNode="nodeClock", fromField="cycleTime", toNode="MoveBall", toField="set_cycle"), 
      ROUTE29 = ROUTE(fromNode="nodeClock", fromField="fraction_changed", toNode="NodePosition", toField="set_fraction"), 
      ROUTE30 = ROUTE(fromNode="MoveBall", fromField="keyValue", toNode="NodePosition", toField="keyValue"), 
      ROUTE31 = ROUTE(fromNode="NodePosition", fromField="value_changed", toNode="transform", toField="set_translation"))), 
    ProtoDeclare32 = ProtoDeclare(name="cylinder",      ProtoInterface33 = ProtoInterface(      field34 = field(name="positionA", accessType="inputOnly", type="SFVec3f"), 
      field35 = field(name="positionB", accessType="inputOnly", type="SFVec3f")), 
     ProtoBody36 = ProtoBody(      Shape37 = Shape(       Extrusion38 = Extrusion(DEF="extrusion", creaseAngle=0.785, crossSection=[1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine=[0,-50,0,0,0,0,0,50,0]), 
       Appearance39 = Appearance(        Material40 = Material(diffuseColor=[0,1,0]))), 
      Script41 = Script(DEF="MoveCylinder",        field42 = field(name="spine", accessType="inputOutput", type="MFVec3f", value="0 -50 0 0 0 0 0 50 0"), 
       field43 = field(name="set_endA", accessType="inputOnly", type="SFVec3f"), 
       field44 = field(name="set_endB", accessType="inputOnly", type="SFVec3f"), 
       IS45 = IS(        connect46 = connect(nodeField="set_endA", protoField="positionA"), 
        connect47 = connect(nodeField="set_endB", protoField="positionB")),        sourceCode = ''' ecmascript:\n"+
"\n"+
"                function set_endA(value) {\n"+
"		    if (typeof spine === \"undefined\") {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([value, spine[1]]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_endB(value) {\n"+
"		    if (typeof spine === \"undefined\") {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([spine[0], value]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_spine(value) {\n"+
"		    Browser.print('\\n'+'\"');\n"+
"                    spine = value;\n"+
"                }\n"+
" ''', ), 
      ROUTE48 = ROUTE(fromNode="MoveCylinder", fromField="spine", toNode="extrusion", toField="set_spine"))), 
    Transform49 = Transform(scale=[0.1,0.1,0.1],      ProtoInstance50 = ProtoInstance(name="node", DEF="nodeA",       fieldValue51 = fieldValue(name="position", value="-50 -50 -50")), 
     ProtoInstance52 = ProtoInstance(name="node", DEF="nodeB",       fieldValue53 = fieldValue(name="position", value="50 50 50")), 
     ProtoInstance54 = ProtoInstance(name="cylinder", DEF="linkA",       fieldValue55 = fieldValue(name="positionA", value="0 0 0"), 
      fieldValue56 = fieldValue(name="positionB", value="50 50 50"))), 
    ROUTE57 = ROUTE(fromNode="nodeA", fromField="position", toNode="linkA", toField="positionA"), 
    ROUTE58 = ROUTE(fromNode="nodeB", fromField="position", toNode="linkA", toField="positionB")))
