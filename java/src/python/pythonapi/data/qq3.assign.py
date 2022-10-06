from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.content = "qq3.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "John Carlson"
meta3.name = "creator"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "John Carlson"
meta4.name = "translator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "11 Jan 2015"
meta5.name = "created"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "05 May 2017"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "12 extrusions to test prototype expander"
meta7.name = "description"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "https://coderextreme.net/x3d/qq3.x3d"
meta8.name = "identifier"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "manual"
meta9.name = "generator"
head1.addMeta([meta9])
X3D0.head = head1

Scene10 = Scene()

ProtoDeclare11 = ProtoDeclare()
ProtoDeclare11.name = "Process"

ProtoBody12 = ProtoBody()

Group13 = Group()
# left 

Transform14 = Transform()
Transform14.scale = [0.5,0.5,0.5]

Shape15 = Shape()
Shape15.DEF = "ShapeLeftDown"

Appearance16 = Appearance()

Material17 = Material()
Material17.diffuseColor = [0.7,1,0]
Appearance16.material = Material17
Shape15.appearance = Appearance16

Extrusion18 = Extrusion(spine = [-2.5,0,0,-1.5,0,0], creaseAngle = 0.785, crossSection = [1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00])
Shape15.geometry = Extrusion18
Transform14.addChildren([Shape15])
Group13.addChildren([Transform14])
# right 

Transform19 = Transform()
Transform19.scale = [0.5,0.5,0.5]

Shape20 = Shape()
Shape20.DEF = "ShapeUpRight"

Appearance21 = Appearance()

Material22 = Material()
Material22.diffuseColor = [0,0.7,1]
Appearance21.material = Material22
Shape20.appearance = Appearance21

Extrusion23 = Extrusion(spine = [1.5,0,0,2.5,0,0], creaseAngle = 0.785, crossSection = [1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00])
Shape20.geometry = Extrusion23
Transform19.addChildren([Shape20])
Group13.addChildren([Transform19])
# up 

Transform24 = Transform()
Transform24.scale = [0.5,0.5,0.5]

Shape25 = Shape()
Shape25.USE = "ShapeUpRight"
Transform24.addChildren([Shape25])
Group13.addChildren([Transform24])
# down 

Transform26 = Transform()
Transform26.scale = [0.5,0.5,0.5]

Shape27 = Shape()
Shape27.USE = "ShapeLeftDown"
Transform26.addChildren([Shape27])
Group13.addChildren([Transform26])
ProtoBody12.addChildren([Group13])
ProtoDeclare11.protoBody = ProtoBody12
Scene10.addChildren([ProtoDeclare11])

Viewpoint28 = Viewpoint()
Viewpoint28.description = "Process pipes"
Viewpoint28.orientation = [1,0,0,-0.4]
Viewpoint28.position = [0,5,12]
Scene10.addChildren([Viewpoint28])

Transform29 = Transform()
Transform29.translation = [0,-2.5,0]

ProtoInstance30 = ProtoInstance()
ProtoInstance30.name = "Process"
Transform29.addChildren([ProtoInstance30])
Scene10.addChildren([Transform29])

Transform31 = Transform()
Transform31.translation = [0,0,0]

ProtoInstance32 = ProtoInstance()
ProtoInstance32.name = "Process"
Transform31.addChildren([ProtoInstance32])
Scene10.addChildren([Transform31])

Transform33 = Transform()
Transform33.translation = [0,2.5,0]

ProtoInstance34 = ProtoInstance()
ProtoInstance34.name = "Process"
Transform33.addChildren([ProtoInstance34])
Scene10.addChildren([Transform33])
X3D0.scene = Scene10
