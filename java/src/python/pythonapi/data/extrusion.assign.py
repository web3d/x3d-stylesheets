from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "creator"
meta2.content = "John W Carlson"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "created"
meta3.content = "December 13 2015"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "title"
meta4.content = "force.x3d"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/force.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "beginnings of a force directed graph in 3D"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "generator"
meta7.content = "Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit"
head1.addMeta([meta7])
X3D0.head = head1

Scene8 = Scene()

Group9 = Group()

Shape10 = Shape()

Extrusion11 = Extrusion(spine = [-50,-50,0,50,50,0], creaseAngle = 0.785, crossSection = [1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00])
Extrusion11.DEF = "extrusion"
Shape10.geometry = Extrusion11

Appearance12 = Appearance()

Material13 = Material()
Material13.diffuseColor = [0,1,0]
Appearance12.material = Material13
Shape10.appearance = Appearance12
Group9.addChildren([Shape10])

TimeSensor14 = TimeSensor()
TimeSensor14.DEF = "TourTime"
TimeSensor14.loop = True
Group9.addChildren([TimeSensor14])

Script15 = Script()
Script15.DEF = "MoveCylinder"

field16 = field()
field16.name = "set_cycle"
field16.accessType = "inputOnly"
field16.type = "SFTime"
Script15.addField([field16])

field17 = field()
field17.name = "spine"
field17.accessType = "inputOutput"
field17.type = "MFVec3f"
field17.value = "-50 -50 0 50 50 0"
Script15.addField([field17])

Script15.setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"                function set_cycle(value) {\n"+
"                        Browser.print(value);\n"+
"                        var endA = new SFVec3f(spine[0].x*Math.random()*2, spine[0].y*Math.random()*2, spine[0].z*Math.random()*2);\n"+
"                        var endB = new SFVec3f(spine[1].x*Math.random()*2, spine[1].y*Math.random()*2, spine[1].z*Math.random()*2);\n"+
"		        spine = new MFVec3f([endA, endB]);\n"+
"                }\n"+
"''')
Group9.addChildren([Script15])

ROUTE18 = ROUTE()
ROUTE18.fromNode = "TourTime"
ROUTE18.fromField = "cycleTime"
ROUTE18.toNode = "MoveCylinder"
ROUTE18.toField = "set_cycle"
Group9.addChildren([ROUTE18])

ROUTE19 = ROUTE()
ROUTE19.fromNode = "MoveCylinder"
ROUTE19.fromField = "spine_changed"
ROUTE19.toNode = "extrusion"
ROUTE19.toField = "spine"
Group9.addChildren([ROUTE19])
Scene8.addChildren([Group9])
X3D0.scene = Scene8
