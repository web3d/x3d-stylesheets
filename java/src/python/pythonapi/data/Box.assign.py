from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "box.x3d"
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
meta5.content = "https://coderextreme.net/X3DJSONLD/box.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "3 boxes"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

NavigationInfo8 = NavigationInfo()
NavigationInfo8.type = ["EXAMINE"]
Scene7.addChildren([NavigationInfo8])

Viewpoint9 = Viewpoint()
Viewpoint9.description = "Cubes on Fire"
Viewpoint9.position = [0,0,12]
Scene7.addChildren([Viewpoint9])

ProtoDeclare10 = ProtoDeclare()
ProtoDeclare10.name = "anyShape"

ProtoInterface11 = ProtoInterface()

field12 = field()
field12.name = "xtranslation"
field12.accessType = "inputOutput"
field12.type = "SFVec3f"
field12.value = "0 0 0"
ProtoInterface11.addField([field12])

field13 = field()
field13.name = "myShape"
field13.accessType = "inputOutput"
field13.type = "MFNode"

Shape14 = Shape()

Sphere15 = Sphere()
Shape14.geometry = Sphere15

Appearance16 = Appearance()

Material17 = Material()
Material17.diffuseColor = [1,1,1]
Appearance16.material = Material17
Shape14.appearance = Appearance16
field13.addChildren([Shape14])
ProtoInterface11.addField([field13])
ProtoDeclare10.protoInterface = ProtoInterface11

ProtoBody18 = ProtoBody()

Transform19 = Transform()

IS20 = IS()

connect21 = connect()
connect21.nodeField = "translation"
connect21.protoField = "xtranslation"
IS20.addConnect([connect21])

connect22 = connect()
connect22.nodeField = "children"
connect22.protoField = "myShape"
IS20.addConnect([connect22])
Transform19.IS = IS20
ProtoBody18.addChildren([Transform19])
ProtoDeclare10.protoBody = ProtoBody18
Scene7.addChildren([ProtoDeclare10])

ProtoDeclare23 = ProtoDeclare()
ProtoDeclare23.name = "three"

ProtoInterface24 = ProtoInterface()

field25 = field()
field25.name = "ytranslation"
field25.accessType = "inputOutput"
field25.type = "SFVec3f"
field25.value = "0 0 0"
ProtoInterface24.addField([field25])

field26 = field()
field26.name = "myShape"
field26.accessType = "inputOutput"
field26.type = "MFNode"

Shape27 = Shape()

Cylinder28 = Cylinder()
Shape27.geometry = Cylinder28

Appearance29 = Appearance()

Material30 = Material()
Material30.diffuseColor = [1,1,1]
Appearance29.material = Material30
Shape27.appearance = Appearance29
field26.addChildren([Shape27])
ProtoInterface24.addField([field26])
ProtoDeclare23.protoInterface = ProtoInterface24

ProtoBody31 = ProtoBody()

Transform32 = Transform()

IS33 = IS()

connect34 = connect()
connect34.nodeField = "translation"
connect34.protoField = "ytranslation"
IS33.addConnect([connect34])
Transform32.IS = IS33

ProtoInstance35 = ProtoInstance()
ProtoInstance35.name = "anyShape"

fieldValue36 = fieldValue()
fieldValue36.name = "xtranslation"
fieldValue36.value = "0 0 0"
ProtoInstance35.addFieldValue([fieldValue36])

IS37 = IS()

connect38 = connect()
connect38.nodeField = "myShape"
connect38.protoField = "myShape"
IS37.addConnect([connect38])
ProtoInstance35.IS = IS37
Transform32.addChildren([ProtoInstance35])

ProtoInstance39 = ProtoInstance()
ProtoInstance39.name = "anyShape"

fieldValue40 = fieldValue()
fieldValue40.name = "xtranslation"
fieldValue40.value = "2 0 0"
ProtoInstance39.addFieldValue([fieldValue40])

IS41 = IS()

connect42 = connect()
connect42.nodeField = "myShape"
connect42.protoField = "myShape"
IS41.addConnect([connect42])
ProtoInstance39.IS = IS41
Transform32.addChildren([ProtoInstance39])

ProtoInstance43 = ProtoInstance()
ProtoInstance43.name = "anyShape"

fieldValue44 = fieldValue()
fieldValue44.name = "xtranslation"
fieldValue44.value = "-2 0 0"
ProtoInstance43.addFieldValue([fieldValue44])

IS45 = IS()

connect46 = connect()
connect46.nodeField = "myShape"
connect46.protoField = "myShape"
IS45.addConnect([connect46])
ProtoInstance43.IS = IS45
Transform32.addChildren([ProtoInstance43])
ProtoBody31.addChildren([Transform32])
ProtoDeclare23.protoBody = ProtoBody31
Scene7.addChildren([ProtoDeclare23])

ProtoInstance47 = ProtoInstance()
ProtoInstance47.name = "three"

fieldValue48 = fieldValue()
fieldValue48.name = "ytranslation"
fieldValue48.value = "0 0 0"
ProtoInstance47.addFieldValue([fieldValue48])

fieldValue49 = fieldValue()
fieldValue49.name = "myShape"

Shape50 = Shape()

Box51 = Box(size = [1,1,1])
Shape50.geometry = Box51

Appearance52 = Appearance()

Material53 = Material()
Material53.diffuseColor = [0,1,0]
Appearance52.material = Material53
Shape50.appearance = Appearance52
fieldValue49.addChildren([Shape50])
ProtoInstance47.addFieldValue([fieldValue49])
Scene7.addChildren([ProtoInstance47])
X3D0.scene = Scene7
