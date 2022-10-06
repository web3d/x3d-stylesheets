from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="SFVec3f.x3d"), 
    meta3 = meta(name="creator", content="John Carlson"), 
    meta4 = meta(name="description", content="3 prismatic spheres"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/SFVec3f.x3d")), 
   Scene6 = Scene(    NavigationInfo7 = NavigationInfo(type=["EXAMINE","ANY"]), 
    Transform8 = Transform(DEF="transform", translation=[0,0,0],      Shape9 = Shape(      Appearance10 = Appearance(       Material11 = Material(diffuseColor=[.7,.7,.7], specularColor=[.5,.5,.5])), 
      Sphere12 = Sphere())), 
    Script13 = Script(DEF="Bounce",      field14 = field(name="set_translation", accessType="inputOnly", type="SFVec3f", value="0 0 0"), 
     field15 = field(name="translation_changed", accessType="outputOnly", type="SFVec3f", value="0 0 0"), 
     field16 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
     field17 = field(name="velocity", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
     field18 = field(name="set_fraction", accessType="inputOnly", type="SFTime"),      sourceCode = '''ecmascript:\n"+
"			function newBubble() {\n"+
"			    translation = new SFVec3f(0, 0, 0);\n"+
"			    velocity = new SFVec3f(\n"+
"			    	Math.random() - 0.5,\n"+
"				Math.random() - 0.5,\n"+
"				Math.random() - 0.5);\n"+
"			}\n"+
"			function set_fraction() {\n"+
"			    translation = new SFVec3f(\n"+
"			    	translation.x + velocity.x,\n"+
"				translation.y + velocity.y,\n"+
"				translation.z + velocity.z);\n"+
"				if (Math.abs(translation.x) > 10) {\n"+
"					newBubble();\n"+
"				} else if (Math.abs(translation.y) > 10) {\n"+
"					newBubble();\n"+
"				} else if (Math.abs(translation.z) > 10) {\n"+
"					newBubble();\n"+
"				} else {\n"+
"					velocity = new SFVec3f(\n"+
"						velocity.x + Math.random() * 0.2 - 0.1,\n"+
"						velocity.y + Math.random() * 0.2 - 0.1,\n"+
"						velocity.z + Math.random() * 0.2 - 0.1\n"+
"					);\n"+
"				}\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     newBubble();\n"+
"			}\n"+
"\n"+
"''', ), 
    TimeSensor19 = TimeSensor(DEF="TourTime", cycleInterval=0.150, loop=True), 
    ROUTE20 = ROUTE(fromNode="TourTime", fromField="cycleTime", toNode="Bounce", toField="set_fraction"), 
    ROUTE21 = ROUTE(fromNode="Bounce", fromField="translation_changed", toNode="transform", toField="set_translation")))
