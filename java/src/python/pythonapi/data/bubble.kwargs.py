from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="bubble.x3d"), 
    meta3 = meta(name="creator", content="John Carlson"), 
    meta4 = meta(name="description", content="Tour around a prismatic sphere"), 
    meta5 = meta(name="generator", content="X3D-Edit, https://savage.nps.edu/X3D-Edit"), 
    meta6 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/bubble.x3d")), 
   Scene7 = Scene(    NavigationInfo8 = NavigationInfo(type=["EXAMINE"]), 
    Viewpoint9 = Viewpoint(position=[0,0,4], orientation=[1,0,0,0], description="Bubble in action"), 
    ProtoDeclare10 = ProtoDeclare(name="Bubble",      ProtoBody11 = ProtoBody(      Transform12 = Transform(DEF="transform",        Shape13 = Shape(        Sphere14 = Sphere(radius=0.25), 
        Appearance15 = Appearance(         Material16 = Material(diffuseColor=[1,0,0], transparency=0.2))), 
       Script17 = Script(DEF="bounce",         field18 = field(name="scale", accessType="inputOutput", type="SFVec3f", value="1 1 1"), 
        field19 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
        field20 = field(name="velocity", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
        field21 = field(name="scalvel", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
        field22 = field(name="set_fraction", accessType="inputOnly", type="SFFloat"),         sourceCode = '''ecmascript:\n"+
"function initialize() {\n"+
"    velocity = new SFVec3f(Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125);\n"+
"\n"+
"    scalvel = new SFVec3f(Math.random() * 0.4, Math.random() * 0.4, Math.random() * 0.4);\n"+
"}\n"+
"\n"+
"function set_fraction(value) {\n"+
"	translation = new SFVec3f(\n"+
"		translation.x + velocity.x,\n"+
"		translation.y + velocity.y,\n"+
"		translation.z + velocity.z);\n"+
"	scale = new SFVec3f(\n"+
"		scale.x + scalvel.x,\n"+
"		scale.y + scalvel.y,\n"+
"		scale.z + scalvel.z);\n"+
"        // if you get to far away or too big, explode\n"+
"        if ( Math.abs(translation.x) > 256) {\n"+
"		translation.x = 0;\n"+
"		initialize();\n"+
"	}\n"+
"        if ( Math.abs(translation.y) > 256) {\n"+
"		translation.y = 0;\n"+
"		initialize();\n"+
"	}\n"+
"        if ( Math.abs(translation.z) > 256) {\n"+
"		translation.z = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.x) > 20) {\n"+
"		scale.x = scale.x/2;\n"+
"		translation.x = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.y) > 20) {\n"+
"		scale.y = scale.y/2;\n"+
"		translation.y = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.z) > 20) {\n"+
"		scale.z = scale.z/2;\n"+
"		translation.z = 0;\n"+
"		initialize();\n"+
"	}\n"+
"}\n"+
"''', ), 
       TimeSensor23 = TimeSensor(DEF="bubbleClock", cycleInterval=10, loop=True), 
       ROUTE24 = ROUTE(fromNode="bounce", fromField="translation_changed", toNode="transform", toField="set_translation"), 
       ROUTE25 = ROUTE(fromNode="bounce", fromField="scale_changed", toNode="transform", toField="set_scale"), 
       ROUTE26 = ROUTE(fromNode="bubbleClock", fromField="fraction_changed", toNode="bounce", toField="set_fraction")))), 
    ProtoInstance27 = ProtoInstance(name="Bubble", DEF="bubbleA")))
