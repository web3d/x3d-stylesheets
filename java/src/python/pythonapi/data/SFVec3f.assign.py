from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "SFVec3f.x3d"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "creator"
meta3.content = "John Carlson"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "description"
meta4.content = "3 prismatic spheres"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/SFVec3f.x3d"
head1.addMeta([meta5])
X3D0.head = head1

Scene6 = Scene()

NavigationInfo7 = NavigationInfo()
NavigationInfo7.type = ["EXAMINE","ANY"]
Scene6.addChildren([NavigationInfo7])

Transform8 = Transform()
Transform8.DEF = "transform"
Transform8.translation = [0,0,0]

Shape9 = Shape()

Appearance10 = Appearance()

Material11 = Material()
Material11.diffuseColor = [.7,.7,.7]
Material11.specularColor = [.5,.5,.5]
Appearance10.material = Material11
Shape9.appearance = Appearance10

Sphere12 = Sphere()
Shape9.geometry = Sphere12
Transform8.addChildren([Shape9])
Scene6.addChildren([Transform8])

Script13 = Script()
Script13.DEF = "Bounce"

field14 = field()
field14.name = "set_translation"
field14.accessType = "inputOnly"
field14.type = "SFVec3f"
field14.value = "0 0 0"
Script13.addField([field14])

field15 = field()
field15.name = "translation_changed"
field15.accessType = "outputOnly"
field15.type = "SFVec3f"
field15.value = "0 0 0"
Script13.addField([field15])

field16 = field()
field16.name = "translation"
field16.accessType = "inputOutput"
field16.type = "SFVec3f"
field16.value = "0 0 0"
Script13.addField([field16])

field17 = field()
field17.name = "velocity"
field17.accessType = "inputOutput"
field17.type = "SFVec3f"
field17.value = "0 0 0"
Script13.addField([field17])

field18 = field()
field18.name = "set_fraction"
field18.accessType = "inputOnly"
field18.type = "SFTime"
Script13.addField([field18])

Script13.setSourceCode('''ecmascript:\n"+
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
"''')
Scene6.addChildren([Script13])

TimeSensor19 = TimeSensor()
TimeSensor19.DEF = "TourTime"
TimeSensor19.cycleInterval = 0.150
TimeSensor19.loop = True
Scene6.addChildren([TimeSensor19])

ROUTE20 = ROUTE()
ROUTE20.fromNode = "TourTime"
ROUTE20.fromField = "cycleTime"
ROUTE20.toNode = "Bounce"
ROUTE20.toField = "set_fraction"
Scene6.addChildren([ROUTE20])

ROUTE21 = ROUTE()
ROUTE21.fromNode = "Bounce"
ROUTE21.fromField = "translation_changed"
ROUTE21.toNode = "transform"
ROUTE21.toField = "set_translation"
Scene6.addChildren([ROUTE21])
X3D0.scene = Scene6
