from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "template.json"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "identifier"
meta3.content = "http://coderextreme.net/X3DJSONLD/template.json"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "description"
meta4.content = "Template for an Indexed Face Set"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "creator"
meta5.content = "John Carlson"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "created"
meta6.content = "4 April 2017"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

Group8 = Group()

Shape9 = Shape()

IndexedFaceSet10 = IndexedFaceSet(creaseAngle = 1.57, coordIndex = [0,0,1,-1,0,1,1,-1,2,2,3,3,-1,0,3,3,0,-1,0,3,2,1,-1,1,2,2,1,-1,1,2,3,0,-1], normalIndex = [0,-1,0,-1,1,-1,2,-1,3,-1,4,-1,5,-1], normalPerVertex = False, colorIndex = [0,0,0,-1,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1])
IndexedFaceSet10.DEF = "IndexedFaceSet"

Coordinate11 = Coordinate()
Coordinate11.point = [0,0,1,0,1,1,1,1,1,1,0,1]
IndexedFaceSet10.coord = Coordinate11

Normal12 = Normal()
Normal12.vector = [1,0,0,-1,0,0,0,1,0,0,0,-1,0,-1,0,0,0,1]
IndexedFaceSet10.normal = Normal12

Color13 = Color()
Color13.color = [0,1,0]
IndexedFaceSet10.color = Color13
Shape9.geometry = IndexedFaceSet10
Group8.addChildren([Shape9])
Scene7.addChildren([Group8])
X3D0.scene = Scene7
