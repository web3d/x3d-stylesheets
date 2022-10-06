from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="pp3.x3d"), 
    meta3 = meta(name="creator", content="John Carlson"), 
    meta4 = meta(name="translator", content="John Carlson"), 
    meta5 = meta(name="created", content="5 May 2015"), 
    meta6 = meta(content="05 May 2017", name="modified"), 
    meta7 = meta(name="description", content="A process pipeline between three spheres (try typing on spheres and blue"), 
    meta8 = meta(name="identifier", content="https://coderextreme.net/x3d/pp3.x3d"), 
    meta9 = meta(name="generator", content="manual")), 
   Scene10 = Scene(    ProtoDeclare11 = ProtoDeclare(name="Process",      ProtoBody12 = ProtoBody(      Group13 = Group(       #left

       Transform14 = Transform(scale=[0.5,0.5,0.5],         Shape15 = Shape(         Appearance16 = Appearance(          Material17 = Material(diffuseColor=[0.7,1,0], transparency=0.5)), 
         Extrusion18 = Extrusion(creaseAngle=0.785, crossSection=[1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine=[-2.5,0,0,-1.5,0,0])),         #<Transform translation=\"-2.5 0 0\"> <Shape> <Text DEF=\"LeftString\" string='\"l\"'/> </Shape> </Transform> <StringSensor DEF=\"LeftSensor\" enabled=\"false\"/> <TouchSensor DEF=\"LeftTouch\" enabled=\"true\"/>
),        #right

       Transform19 = Transform(scale=[0.5,0.5,0.5],         Shape20 = Shape(         Appearance21 = Appearance(          Material22 = Material(diffuseColor=[0,0.7,1], transparency=0.5)), 
         Extrusion23 = Extrusion(creaseAngle=0.785, crossSection=[1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine=[1.5,0,0,2.5,0,0])), 
        Transform24 = Transform(translation=[2,0,0],          Shape25 = Shape(          Appearance26 = Appearance(           Material27 = Material(DEF="MaterialLightBlue", diffuseColor=[1,1,1])), 
          Text28 = Text(DEF="RightString", string=["r"]))), 
        StringSensor29 = StringSensor(DEF="RightSensor", enabled=False, deletionAllowed=True), 
        TouchSensor30 = TouchSensor(description="touch to activate", DEF="RightTouch")),        #up

       Transform31 = Transform(scale=[0.5,0.5,0.5],         Shape32 = Shape(         Appearance33 = Appearance(          Material34 = Material(diffuseColor=[0,0.7,1], transparency=0.5)), 
         Extrusion35 = Extrusion(creaseAngle=0.785, crossSection=[1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine=[0,1.5,0,0,2.5,0])), 
        Transform36 = Transform(translation=[-0.5,2,0],          Shape37 = Shape(          Appearance38 = Appearance(           Material39 = Material(USE="MaterialLightBlue")), 
          Text40 = Text(DEF="UpString", string=["u"]))), 
        StringSensor41 = StringSensor(DEF="UpSensor", enabled=False, deletionAllowed=True), 
        TouchSensor42 = TouchSensor(description="touch to activate", DEF="UpTouch")),        #down

       Transform43 = Transform(scale=[0.5,0.5,0.5],         Shape44 = Shape(         Appearance45 = Appearance(          Material46 = Material(diffuseColor=[0.7,1,0], transparency=0.5)), 
         Extrusion47 = Extrusion(creaseAngle=0.785, crossSection=[1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine=[0,-2.5,0,0,-1.5,0])),         #<Transform translation=\"-0.5 -2.5 0\"> <Shape> <Text DEF=\"DownString\" string='\"d\"'/> </Shape> </Transform> <StringSensor DEF=\"DownSensor\" enabled=\"false\"/> <TouchSensor description='touch to activate' DEF=\"DownTouch\" enabled=\"true\"/>
),        #center

       Transform48 = Transform(        Shape49 = Shape(         Appearance50 = Appearance(          Material51 = Material(diffuseColor=[1,0,0.7])), 
         Sphere52 = Sphere()), 
        Transform53 = Transform(scale=[0.5,0.5,0.5], translation=[-0.5,0,1],          Shape54 = Shape(          Appearance55 = Appearance(           Material56 = Material(USE="MaterialLightBlue")), 
          Text57 = Text(DEF="CenterString"))), 
        StringSensor58 = StringSensor(DEF="CenterSensor", enabled=False, deletionAllowed=True), 
        TouchSensor59 = TouchSensor(description="touch to activate", DEF="CenterTouch"))), 
      Script60 = Script(DEF="RightSingleToMultiString",        field61 = field(name="set_rightstring", accessType="inputOnly", type="SFString"), 
       field62 = field(name="rightlines", accessType="outputOnly", type="MFString"),        sourceCode = '''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	rightlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_rightstring(rightstr) {\n"+
"	rightlines = new MFString(rightstr);\n"+
"}''', ), 
      Script63 = Script(DEF="UpSingleToMultiString",        field64 = field(name="set_upstring", accessType="inputOnly", type="SFString"), 
       field65 = field(name="uplines", accessType="outputOnly", type="MFString"),        sourceCode = '''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	uplines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_upstring(upstr) {\n"+
"	uplines = new MFString(upstr);\n"+
"}''', ), 
      Script66 = Script(DEF="CenterSingleToMultiString",        field67 = field(name="set_centerstring", accessType="inputOnly", type="SFString"), 
       field68 = field(name="centerlines", accessType="outputOnly", type="MFString"),        sourceCode = '''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	centerlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_centerstring(centerstr) {\n"+
"	centerlines = new MFString(centerstr);\n"+
"}''', ), 
      ROUTE69 = ROUTE(fromField="enteredText", fromNode="CenterSensor", toField="set_centerstring", toNode="CenterSingleToMultiString"), 
      ROUTE70 = ROUTE(fromField="centerlines", fromNode="CenterSingleToMultiString", toField="set_string", toNode="CenterString"), 
      ROUTE71 = ROUTE(fromField="isOver", fromNode="CenterTouch", toField="set_enabled", toNode="CenterSensor"), 
      ROUTE72 = ROUTE(fromField="enteredText", fromNode="RightSensor", toField="set_rightstring", toNode="RightSingleToMultiString"), 
      ROUTE73 = ROUTE(fromField="rightlines", fromNode="RightSingleToMultiString", toField="set_string", toNode="RightString"), 
      ROUTE74 = ROUTE(fromField="isOver", fromNode="RightTouch", toField="set_enabled", toNode="RightSensor"), 
      ROUTE75 = ROUTE(fromField="enteredText", fromNode="UpSensor", toField="set_upstring", toNode="UpSingleToMultiString"), 
      ROUTE76 = ROUTE(fromField="uplines", fromNode="UpSingleToMultiString", toField="set_string", toNode="UpString"), 
      ROUTE77 = ROUTE(fromField="isOver", fromNode="UpTouch", toField="set_enabled", toNode="UpSensor"))), 
    NavigationInfo78 = NavigationInfo(), 
    Viewpoint79 = Viewpoint(description="Process pipes", orientation=[1,0,0,-0.4], position=[0,5,12]), 
    Transform80 = Transform(translation=[0,-2.5,0],      ProtoInstance81 = ProtoInstance(name="Process")), 
    Transform82 = Transform(     ProtoInstance83 = ProtoInstance(name="Process")), 
    Transform84 = Transform(translation=[0,2.5,0],      ProtoInstance85 = ProtoInstance(name="Process"))))
