from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "rubik.x3d"
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
meta5.content = "https://coderextreme.net/X3DJSONLD/rubik.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "a kind of rubik cube with spheres"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

NavigationInfo8 = NavigationInfo()
NavigationInfo8.type = ["EXAMINE"]
Scene7.addChildren([NavigationInfo8])

Viewpoint9 = Viewpoint()
Viewpoint9.description = "Rubiks Cube"
Viewpoint9.position = [0,0,12]
Scene7.addChildren([Viewpoint9])

ProtoDeclare10 = ProtoDeclare()
ProtoDeclare10.name = "sphere"

ProtoInterface11 = ProtoInterface()

field12 = field()
field12.name = "xtranslation"
field12.accessType = "inputOutput"
field12.type = "SFVec3f"
field12.value = "0.0 0.0 0.0"
ProtoInterface11.addField([field12])
ProtoDeclare10.protoInterface = ProtoInterface11

ProtoBody13 = ProtoBody()

Transform14 = Transform()
Transform14.translation = [0,0,0]

IS15 = IS()

connect16 = connect()
connect16.nodeField = "translation"
connect16.protoField = "xtranslation"
IS15.addConnect([connect16])
Transform14.IS = IS15

Shape17 = Shape()

Sphere18 = Sphere()
Shape17.geometry = Sphere18

Appearance19 = Appearance()

Material20 = Material()
Material20.diffuseColor = [1,1,1]
Appearance19.material = Material20
Shape17.appearance = Appearance19
Transform14.addChildren([Shape17])
ProtoBody13.addChildren([Transform14])
ProtoDeclare10.protoBody = ProtoBody13
Scene7.addChildren([ProtoDeclare10])

ProtoDeclare21 = ProtoDeclare()
ProtoDeclare21.name = "three"

ProtoInterface22 = ProtoInterface()

field23 = field()
field23.name = "ytranslation"
field23.accessType = "inputOutput"
field23.type = "SFVec3f"
field23.value = "0.0 0.0 0.0"
ProtoInterface22.addField([field23])
ProtoDeclare21.protoInterface = ProtoInterface22

ProtoBody24 = ProtoBody()

Transform25 = Transform()
Transform25.translation = [0,0,0]

IS26 = IS()

connect27 = connect()
connect27.nodeField = "translation"
connect27.protoField = "ytranslation"
IS26.addConnect([connect27])
Transform25.IS = IS26

ProtoInstance28 = ProtoInstance()
ProtoInstance28.name = "sphere"

fieldValue29 = fieldValue()
fieldValue29.name = "xtranslation"
fieldValue29.value = "0 0 0"
ProtoInstance28.addFieldValue([fieldValue29])
Transform25.addChildren([ProtoInstance28])

ProtoInstance30 = ProtoInstance()
ProtoInstance30.name = "sphere"

fieldValue31 = fieldValue()
fieldValue31.name = "xtranslation"
fieldValue31.value = "2 0 0"
ProtoInstance30.addFieldValue([fieldValue31])
Transform25.addChildren([ProtoInstance30])

ProtoInstance32 = ProtoInstance()
ProtoInstance32.name = "sphere"

fieldValue33 = fieldValue()
fieldValue33.name = "xtranslation"
fieldValue33.value = "-2 0 0"
ProtoInstance32.addFieldValue([fieldValue33])
Transform25.addChildren([ProtoInstance32])
ProtoBody24.addChildren([Transform25])
ProtoDeclare21.protoBody = ProtoBody24
Scene7.addChildren([ProtoDeclare21])

ProtoDeclare34 = ProtoDeclare()
ProtoDeclare34.name = "nine"

ProtoInterface35 = ProtoInterface()

field36 = field()
field36.name = "ztranslation"
field36.accessType = "inputOutput"
field36.type = "SFVec3f"
field36.value = "0.0 0.0 0.0"
ProtoInterface35.addField([field36])
ProtoDeclare34.protoInterface = ProtoInterface35

ProtoBody37 = ProtoBody()

Transform38 = Transform()
Transform38.translation = [0,0,0]

IS39 = IS()

connect40 = connect()
connect40.nodeField = "translation"
connect40.protoField = "ztranslation"
IS39.addConnect([connect40])
Transform38.IS = IS39

ProtoInstance41 = ProtoInstance()
ProtoInstance41.name = "three"

fieldValue42 = fieldValue()
fieldValue42.name = "ytranslation"
fieldValue42.value = "0 0 0"
ProtoInstance41.addFieldValue([fieldValue42])
Transform38.addChildren([ProtoInstance41])

ProtoInstance43 = ProtoInstance()
ProtoInstance43.name = "three"

fieldValue44 = fieldValue()
fieldValue44.name = "ytranslation"
fieldValue44.value = "0 2 0"
ProtoInstance43.addFieldValue([fieldValue44])
Transform38.addChildren([ProtoInstance43])

ProtoInstance45 = ProtoInstance()
ProtoInstance45.name = "three"

fieldValue46 = fieldValue()
fieldValue46.name = "ytranslation"
fieldValue46.value = "0 -2 0"
ProtoInstance45.addFieldValue([fieldValue46])
Transform38.addChildren([ProtoInstance45])
ProtoBody37.addChildren([Transform38])
ProtoDeclare34.protoBody = ProtoBody37
Scene7.addChildren([ProtoDeclare34])

ProtoDeclare47 = ProtoDeclare()
ProtoDeclare47.name = "twentyseven"

ProtoInterface48 = ProtoInterface()

field49 = field()
field49.name = "ttranslation"
field49.accessType = "inputOutput"
field49.type = "SFVec3f"
field49.value = "0.0 0.0 0.0"
ProtoInterface48.addField([field49])
ProtoDeclare47.protoInterface = ProtoInterface48

ProtoBody50 = ProtoBody()

Transform51 = Transform()
Transform51.translation = [0,0,0]

IS52 = IS()

connect53 = connect()
connect53.nodeField = "translation"
connect53.protoField = "ttranslation"
IS52.addConnect([connect53])
Transform51.IS = IS52

ProtoInstance54 = ProtoInstance()
ProtoInstance54.name = "nine"

fieldValue55 = fieldValue()
fieldValue55.name = "ztranslation"
fieldValue55.value = "0 0 0"
ProtoInstance54.addFieldValue([fieldValue55])
Transform51.addChildren([ProtoInstance54])

ProtoInstance56 = ProtoInstance()
ProtoInstance56.name = "nine"

fieldValue57 = fieldValue()
fieldValue57.name = "ztranslation"
fieldValue57.value = "0 0 2"
ProtoInstance56.addFieldValue([fieldValue57])
Transform51.addChildren([ProtoInstance56])

ProtoInstance58 = ProtoInstance()
ProtoInstance58.name = "nine"

fieldValue59 = fieldValue()
fieldValue59.name = "ztranslation"
fieldValue59.value = "0 0 -2"
ProtoInstance58.addFieldValue([fieldValue59])
Transform51.addChildren([ProtoInstance58])
ProtoBody50.addChildren([Transform51])
ProtoDeclare47.protoBody = ProtoBody50
Scene7.addChildren([ProtoDeclare47])

ProtoInstance60 = ProtoInstance()
ProtoInstance60.name = "twentyseven"

fieldValue61 = fieldValue()
fieldValue61.name = "ttranslation"
fieldValue61.value = "0 0 0"
ProtoInstance60.addFieldValue([fieldValue61])
Scene7.addChildren([ProtoInstance60])
X3D0.scene = Scene7
