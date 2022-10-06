from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="creator", content="John W Carlson"), 
    meta3 = meta(name="created", content="December 13 2015"), 
    meta4 = meta(name="title", content="force.x3d"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/force.x3d"), 
    meta6 = meta(name="description", content="beginnings of a force directed graph in 3D"), 
    meta7 = meta(name="generator", content="Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit")), 
   Scene8 = Scene(    ProtoDeclare9 = ProtoDeclare(name="node",      ProtoInterface10 = ProtoInterface(      field11 = field(name="position", accessType="inputOutput", type="SFVec3f", value="0 0 0")), 
     ProtoBody12 = ProtoBody(      Group13 = Group(       Transform14 = Transform(DEF="transform",         IS15 = IS(         connect16 = connect(nodeField="translation", protoField="position")), 
        Shape17 = Shape(         Sphere18 = Sphere(), 
         Appearance19 = Appearance(          Material20 = Material(diffuseColor=[1,0,0]))), 
        Transform21 = Transform(translation=[1,0,0],          Shape22 = Shape(          Text23 = Text(string=["Node"],            FontStyle24 = FontStyle(family=["SERIF"], justify=["MIDDLE","MIDDLE"], size=5)), 
          Appearance25 = Appearance(           Material26 = Material(diffuseColor=[0,0,1]))))), 
       PositionInterpolator27 = PositionInterpolator(DEF="NodePosition", key=[0,1], keyValue=[0,0,0,0,5,0]), 
       Script28 = Script(DEF="MoveBall",         field29 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="50 50 0"), 
        field30 = field(name="old", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
        field31 = field(name="set_cycle", accessType="inputOnly", type="SFTime"), 
        field32 = field(name="keyValue", accessType="outputOnly", type="MFVec3f"),         sourceCode = '''\n"+
"ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f([old, translation]);\n"+
"						// Browser.println(translation);\n"+
"					}\n"+
"''', ), 
       TimeSensor33 = TimeSensor(DEF="nodeClock", cycleInterval=3, loop=True), 
       ROUTE34 = ROUTE(fromNode="nodeClock", fromField="cycleTime", toNode="MoveBall", toField="set_cycle"), 
       ROUTE35 = ROUTE(fromNode="nodeClock", fromField="fraction_changed", toNode="NodePosition", toField="set_fraction"), 
       ROUTE36 = ROUTE(fromNode="MoveBall", fromField="keyValue", toNode="NodePosition", toField="keyValue"), 
       ROUTE37 = ROUTE(fromNode="NodePosition", fromField="value_changed", toNode="transform", toField="set_translation")))), 
    ProtoDeclare38 = ProtoDeclare(name="cylinder",      ProtoInterface39 = ProtoInterface(      field40 = field(name="set_positionA", accessType="inputOnly", type="SFVec3f"), 
      field41 = field(name="set_positionB", accessType="inputOnly", type="SFVec3f")), 
     ProtoBody42 = ProtoBody(      Group43 = Group(       Shape44 = Shape(        Extrusion45 = Extrusion(DEF="extrusion", creaseAngle=0.785, crossSection=[1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00], spine=[0,-50,0,0,50,0]), 
        Appearance46 = Appearance(         Material47 = Material(diffuseColor=[0,1,0]))), 
       Script48 = Script(DEF="MoveCylinder",         field49 = field(name="spine", accessType="inputOutput", type="MFVec3f", value="0 -50 0 0 50 0"), 
        field50 = field(name="set_endA", accessType="inputOnly", type="SFVec3f"), 
        field51 = field(name="set_endB", accessType="inputOnly", type="SFVec3f"), 
        IS52 = IS(         connect53 = connect(nodeField="set_endA", protoField="set_positionA"), 
         connect54 = connect(nodeField="set_endB", protoField="set_positionB")),         sourceCode = '''\n"+
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
       ROUTE55 = ROUTE(fromNode="MoveCylinder", fromField="spine", toNode="extrusion", toField="set_spine")))), 
    Transform56 = Transform(DEF="HoldsContent", scale=[0.1,0.1,0.1],      PlaneSensor57 = PlaneSensor(DEF="clickGenerator", enabled=True, minPosition=[-50,-50], maxPosition=[50,50], description="click on background to add nodes, click on nodes to add links"), 
     ProtoInstance58 = ProtoInstance(DEF="nodeA", name="node",       fieldValue59 = fieldValue(name="position", value="0.0 0.0 0.0")), 
     ProtoInstance60 = ProtoInstance(DEF="nodeB", name="node",       fieldValue61 = fieldValue(name="position", value="50.0 50.0 50.0")), 
     ProtoInstance62 = ProtoInstance(DEF="nodeC", name="node",       fieldValue63 = fieldValue(name="position", value="-50.0 -50.0 -50.0")), 
     ProtoInstance64 = ProtoInstance(DEF="nodeD", name="node",       fieldValue65 = fieldValue(name="position", value="50.0 50.0 -50.0")), 
     ProtoInstance66 = ProtoInstance(DEF="linkA", name="cylinder",       fieldValue67 = fieldValue(name="set_positionA", value="0 0 0"), 
      fieldValue68 = fieldValue(name="set_positionB", value="50 50 50")), 
     ProtoInstance69 = ProtoInstance(DEF="linkB", name="cylinder",       fieldValue70 = fieldValue(name="set_positionA", value="0 0 0"), 
      fieldValue71 = fieldValue(name="set_positionB", value="-50 -50 -50")), 
     ProtoInstance72 = ProtoInstance(DEF="linkC", name="cylinder",       fieldValue73 = fieldValue(name="set_positionA", value="50 50 50"), 
      fieldValue74 = fieldValue(name="set_positionB", value="50 50 -50"))), 
    Script75 = Script(DEF="clickHandler",      field76 = field(accessType="inputOutput", name="counter", value="0", type="SFInt32"), 
     field77 = field(accessType="outputOnly", name="node_changed", type="SFNode"), 
     field78 = field(accessType="inputOnly", name="add_node", value="false", type="SFBool"),      #
#            <field name=\"ModifiableNode\" type=\"SFNode\" accessType=\"inputOutput\">
#                <Transform USE=\"HoldsContent\"/>
#            </field>
#	    
     sourceCode = '''\n"+
"ecmascript:\n"+
"	function add_node(value) {\n"+
"                // Browser.print('hey ', counter);\n"+
"                counter = counter++;\n"+
"		Browser.appendTo(Browser.getDocument().querySelector(\"field [name=ModifiableNode]\"),\n"+
"			{ \"ProtoInstance\":\n"+
"				{ \"@name\":\"node\",\n"+
"				  \"@DEF\":\"node'+counter+'\",\n"+
"				  \"fieldValue\": [\n"+
"					{\n"+
"						 \"@name\":\"position\",\n"+
"						 \"@value\":[0.0,0.0,0.0]\n"+
"					}\n"+
"				  ]\n"+
"				}\n"+
"			});\n"+
"                \n"+
"        }\n"+
"	''', ), 
    ROUTE79 = ROUTE(fromNode="clickGenerator", fromField="isActive", toNode="clickHandler", toField="add_node"), 
    ROUTE80 = ROUTE(fromNode="nodeA", fromField="position", toNode="linkA", toField="set_positionA"), 
    ROUTE81 = ROUTE(fromNode="nodeB", fromField="position", toNode="linkA", toField="set_positionB"), 
    ROUTE82 = ROUTE(fromNode="nodeA", fromField="position", toNode="linkB", toField="set_positionA"), 
    ROUTE83 = ROUTE(fromNode="nodeC", fromField="position", toNode="linkB", toField="set_positionB"), 
    ROUTE84 = ROUTE(fromNode="nodeA", fromField="position", toNode="linkC", toField="set_positionA"), 
    ROUTE85 = ROUTE(fromNode="nodeD", fromField="position", toNode="linkC", toField="set_positionB")))
