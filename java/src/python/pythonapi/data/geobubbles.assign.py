from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

component2 = component()
component2.level = 1
component2.name = "Geospatial"
head1.addComponent([component2])

meta3 = meta()
meta3.name = "title"
meta3.content = "geobubbles.x3d"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "creator"
meta4.content = "John Carlson"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "generator"
meta5.content = "manual"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "identifier"
meta6.content = "https://coderextreme.net/X3DJSONLD/geobubbles.x3d"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "description"
meta7.content = "geo bubbles"
head1.addMeta([meta7])
X3D0.head = head1

Scene8 = Scene()
#Viewpoint DEF='Tour' position='0 0 4' orientation='1 0 0 0' description='Tour Views'/
#PositionInterpolator DEF='TourPosition' key='0 1' keyValue='-0.5 -0.5 4 -0.5 0.5 4'/

GeoViewpoint9 = GeoViewpoint(geoSystem = ["GD","WE"])
GeoViewpoint9.DEF = "Tour"
GeoViewpoint9.position = [0,0,4]
GeoViewpoint9.orientation = [1,0,0,0]
GeoViewpoint9.description = "Tour Views"
GeoViewpoint9.retainUserOffsets = False
Scene8.children = GeoViewpoint9

Background10 = Background()
Background10.backUrl = ["../resources/images/BK.png","https://coderextreme.net/X3DJSONLD/images/BK.png"]
Background10.bottomUrl = ["../resources/images/BT.png","https://coderextreme.net/X3DJSONLD/images/BT.png"]
Background10.frontUrl = ["../resources/images/FR.png","https://coderextreme.net/X3DJSONLD/images/FR.png"]
Background10.leftUrl = ["../resources/images/LF.png","https://coderextreme.net/X3DJSONLD/images/LF.png"]
Background10.rightUrl = ["../resources/images/RT.png","https://coderextreme.net/X3DJSONLD/images/RT.png"]
Background10.topUrl = ["../resources/images/TP.png","https://coderextreme.net/X3DJSONLD/images/TP.png"]
Scene8.addChildren([Background10])

Transform11 = Transform()

Shape12 = Shape()

Sphere13 = Sphere()
Shape12.geometry = Sphere13

Appearance14 = Appearance()

Material15 = Material()
Material15.diffuseColor = [0.7,0.7,0.7]
Material15.specularColor = [0.5,0.5,0.5]
Appearance14.material = Material15
Shape12.appearance = Appearance14
Transform11.addChildren([Shape12])
Scene8.addChildren([Transform11])

TimeSensor16 = TimeSensor()
TimeSensor16.DEF = "TourTime"
TimeSensor16.cycleInterval = 5
TimeSensor16.loop = True
Scene8.addChildren([TimeSensor16])

GeoPositionInterpolator17 = GeoPositionInterpolator(geoSystem = ["GD","WE"])
GeoPositionInterpolator17.DEF = "TourPosition"
GeoPositionInterpolator17.key = [0,1]
GeoPositionInterpolator17.keyValue = [0.0015708,0,4,0,0.0015708,4]
Scene8.addChildren([GeoPositionInterpolator17])

Script18 = Script()
Script18.DEF = "RandomTourTime"

field19 = field()
field19.name = "set_cycle"
field19.accessType = "inputOnly"
field19.type = "SFTime"
Script18.addField([field19])

field20 = field()
field20.name = "val"
field20.accessType = "inputOutput"
field20.type = "SFFloat"
field20.value = "0"
Script18.addField([field20])

field21 = field()
field21.name = "positions"
field21.accessType = "inputOutput"
field21.type = "MFVec3d"
field21.value = "0.0015708 0 4 0 0.0015708 4"
Script18.addField([field21])

field22 = field()
field22.name = "position"
field22.accessType = "inputOutput"
field22.type = "MFVec3d"
field22.value = "0.0015708 0 4 0 0.0015708 4"
Script18.addField([field22])

Script18.setSourceCode('''ecmascript:\n"+
"\n"+
"               function set_cycle(value) {\n"+
"                        var cartesianMult = -150;  // -150 if cartesian, 1 if geo\n"+
"                        var ov = val;\n"+
"			// Browser.print('old '+ov);\n"+
"                        do {\n"+
"                                val = Math.floor(Math.random()*2);\n"+
"                                var vc = val;\n"+
"                                positions[vc] = new SFVec3d(Math.round(Math.random()*2)*0.0015708*cartesianMult, Math.round(Math.random()*2)*0.0015708*cartesianMult, 4);\n"+
"                        } while ( positions[ov][0] === positions[vc][0] && positions[ov][1] === positions[vc][1] && positions[ov][2] === positions[vc][2]);\n"+
"			// Browser.println(positions[ov]);\n"+
"			// Browser.println(positions[vc]);\n"+
"                        position = new MFVec3d();\n"+
"                        position[0] = new SFVec3d(positions[ov][0],positions[ov][1],positions[ov][2]);\n"+
"                        position[1] = new SFVec3d(positions[vc][0],positions[vc][1],positions[vc][2]);\n"+
"               }''')
Scene8.addChildren([Script18])

ROUTE23 = ROUTE()
ROUTE23.fromNode = "TourTime"
ROUTE23.fromField = "cycleTime"
ROUTE23.toNode = "RandomTourTime"
ROUTE23.toField = "set_cycle"
Scene8.addChildren([ROUTE23])

ROUTE24 = ROUTE()
ROUTE24.fromNode = "RandomTourTime"
ROUTE24.fromField = "position"
ROUTE24.toNode = "TourPosition"
ROUTE24.toField = "keyValue"
Scene8.addChildren([ROUTE24])

ROUTE25 = ROUTE()
ROUTE25.fromNode = "TourTime"
ROUTE25.fromField = "fraction_changed"
ROUTE25.toNode = "TourPosition"
ROUTE25.toField = "set_fraction"
Scene8.addChildren([ROUTE25])

ROUTE26 = ROUTE()
ROUTE26.fromNode = "TourPosition"
ROUTE26.fromField = "geovalue_changed"
ROUTE26.toNode = "Tour"
ROUTE26.toField = "set_position"
Scene8.addChildren([ROUTE26])
X3D0.scene = Scene8
