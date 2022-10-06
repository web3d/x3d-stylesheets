from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.0"

head1 = head()

meta2 = meta()
meta2.content = "ExtrusionHeart.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Simple extrusion of a Valentine heart."
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Class participants in course Introduction to VRML/X3D."
meta4.name = "creator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "14 February 2001"
meta5.name = "created"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "27 November 2015"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "http://www.web3d.org/x3d/content/examples/Basic/course/ExtrusionHeart.x3d"
meta7.name = "identifier"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta8.name = "generator"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "../license.html"
meta9.name = "license"
head1.addMeta([meta9])
X3D0.head = head1

Scene10 = Scene()

Viewpoint11 = Viewpoint()
Viewpoint11.description = "Extrusion Heart"
Viewpoint11.orientation = [1,0,0,1.57]
Viewpoint11.position = [0,-4,0]
Scene10.addChildren([Viewpoint11])

Transform12 = Transform()
Transform12.translation = [0,-0.5,0]

Shape13 = Shape()

Extrusion14 = Extrusion(creaseAngle = 3.14159, crossSection = [0,0.8,0.2,1,0.7,0.95,1,0.5,0.8,0,0.5,-0.3,0,-0.7,-0.5,-0.3,-0.8,0,-1,0.5,-0.7,0.95,-0.2,1,0,0.8], solid = False, spine = [0,0,0,0,0.1,0,0,0.5,0,0,0.9,0,0,1,0])
Extrusion14.scale = [0.01,0.01,0.8,0.8,1,1,0.8,0.8,0.01,0.01]
Shape13.geometry = Extrusion14

Appearance15 = Appearance()

Material16 = Material()
Material16.diffuseColor = [0.8,0.3,0.3]
Appearance15.material = Material16
Shape13.appearance = Appearance15
Transform12.addChildren([Shape13])
Scene10.addChildren([Transform12])
X3D0.scene = Scene10
