from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "sphere.x3d"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "creator"
meta3.content = "John Carlson"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "generator"
meta4.content = "manual"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/sphere.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "a sphere"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

Group8 = Group()

Shape9 = Shape()

Appearance10 = Appearance()

Material11 = Material()
Material11.diffuseColor = [1,1,1]
Appearance10.material = Material11
Shape9.appearance = Appearance10

Sphere12 = Sphere(radius = 1)
Shape9.geometry = Sphere12
Group8.addChildren([Shape9])
Scene7.addChildren([Group8])
X3D0.scene = Scene7
