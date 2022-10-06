from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "rubikOnFire.x3d"
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
meta5.content = "https://coderextreme.net/X3DJSONLD/rubikOnFire.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "a white rubik cube"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

NavigationInfo8 = NavigationInfo()
NavigationInfo8.type = ["EXAMINE"]
Scene7.addChildren([NavigationInfo8])

Viewpoint9 = Viewpoint()
Viewpoint9.description = "Rubiks Cube on Fire"
Viewpoint9.position = [0,0,12]
Scene7.addChildren([Viewpoint9])

ProtoDeclare10 = ProtoDeclare()
ProtoDeclare10.name = "anyShape"

ProtoInterface11 = ProtoInterface()

field12 = field()
field12.name = "xtranslation"
field12.accessType = "inputOutput"
field12.type = "SFVec3f"
field12.value = "0.0 0.0 0.0"
ProtoInterface11.addField([field12])

field13 = field()
field13.name = "myShape"
field13.accessType = "inputOutput"
field13.type = "SFNode"

Sphere14 = Sphere()
field13.addChildren([Sphere14])
ProtoInterface11.addField([field13])
ProtoDeclare10.protoInterface = ProtoInterface11

ProtoBody15 = ProtoBody()

Transform16 = Transform()
Transform16.translation = [0,0,0]

IS17 = IS()

connect18 = connect()
connect18.nodeField = "translation"
connect18.protoField = "xtranslation"
IS17.addConnect([connect18])
Transform16.IS = IS17

Shape19 = Shape()

IS20 = IS()

connect21 = connect()
connect21.nodeField = "geometry"
connect21.protoField = "myShape"
IS20.addConnect([connect21])
Shape19.IS = IS20

Appearance22 = Appearance()

Material23 = Material()
Material23.diffuseColor = [1,1,1]
Appearance22.material = Material23
Shape19.appearance = Appearance22
Transform16.addChildren([Shape19])
ProtoBody15.addChildren([Transform16])
ProtoDeclare10.protoBody = ProtoBody15
Scene7.addChildren([ProtoDeclare10])

ProtoDeclare24 = ProtoDeclare()
ProtoDeclare24.name = "three"

ProtoInterface25 = ProtoInterface()

field26 = field()
field26.name = "ytranslation"
field26.accessType = "inputOutput"
field26.type = "SFVec3f"
field26.value = "0.0 0.0 0.0"
ProtoInterface25.addField([field26])

field27 = field()
field27.name = "myShape"
field27.accessType = "inputOutput"
field27.type = "SFNode"

Sphere28 = Sphere()
field27.addChildren([Sphere28])
ProtoInterface25.addField([field27])
ProtoDeclare24.protoInterface = ProtoInterface25

ProtoBody29 = ProtoBody()

Transform30 = Transform()
Transform30.translation = [0,0,0]

IS31 = IS()

connect32 = connect()
connect32.nodeField = "translation"
connect32.protoField = "ytranslation"
IS31.addConnect([connect32])
Transform30.IS = IS31

ProtoInstance33 = ProtoInstance()
ProtoInstance33.name = "anyShape"

fieldValue34 = fieldValue()
fieldValue34.name = "xtranslation"
fieldValue34.value = "0 0 0"
ProtoInstance33.addFieldValue([fieldValue34])

IS35 = IS()

connect36 = connect()
connect36.nodeField = "myShape"
connect36.protoField = "myShape"
IS35.addConnect([connect36])
ProtoInstance33.IS = IS35
Transform30.addChildren([ProtoInstance33])

ProtoInstance37 = ProtoInstance()
ProtoInstance37.name = "anyShape"

fieldValue38 = fieldValue()
fieldValue38.name = "xtranslation"
fieldValue38.value = "2 0 0"
ProtoInstance37.addFieldValue([fieldValue38])

IS39 = IS()

connect40 = connect()
connect40.nodeField = "myShape"
connect40.protoField = "myShape"
IS39.addConnect([connect40])
ProtoInstance37.IS = IS39
Transform30.addChildren([ProtoInstance37])

ProtoInstance41 = ProtoInstance()
ProtoInstance41.name = "anyShape"

fieldValue42 = fieldValue()
fieldValue42.name = "xtranslation"
fieldValue42.value = "-2 0 0"
ProtoInstance41.addFieldValue([fieldValue42])

IS43 = IS()

connect44 = connect()
connect44.nodeField = "myShape"
connect44.protoField = "myShape"
IS43.addConnect([connect44])
ProtoInstance41.IS = IS43
Transform30.addChildren([ProtoInstance41])
ProtoBody29.addChildren([Transform30])
ProtoDeclare24.protoBody = ProtoBody29
Scene7.addChildren([ProtoDeclare24])

ProtoDeclare45 = ProtoDeclare()
ProtoDeclare45.name = "nine"

ProtoInterface46 = ProtoInterface()

field47 = field()
field47.name = "ztranslation"
field47.accessType = "inputOutput"
field47.type = "SFVec3f"
field47.value = "0.0 0.0 0.0"
ProtoInterface46.addField([field47])

field48 = field()
field48.name = "myShape"
field48.accessType = "inputOutput"
field48.type = "SFNode"

Sphere49 = Sphere()
field48.addChildren([Sphere49])
ProtoInterface46.addField([field48])
ProtoDeclare45.protoInterface = ProtoInterface46

ProtoBody50 = ProtoBody()

Transform51 = Transform()
Transform51.translation = [0,0,0]

IS52 = IS()

connect53 = connect()
connect53.nodeField = "translation"
connect53.protoField = "ztranslation"
IS52.addConnect([connect53])
Transform51.IS = IS52

ProtoInstance54 = ProtoInstance()
ProtoInstance54.name = "three"

fieldValue55 = fieldValue()
fieldValue55.name = "ytranslation"
fieldValue55.value = "0 0 0"
ProtoInstance54.addFieldValue([fieldValue55])

IS56 = IS()

connect57 = connect()
connect57.nodeField = "myShape"
connect57.protoField = "myShape"
IS56.addConnect([connect57])
ProtoInstance54.IS = IS56
Transform51.addChildren([ProtoInstance54])

ProtoInstance58 = ProtoInstance()
ProtoInstance58.name = "three"

fieldValue59 = fieldValue()
fieldValue59.name = "ytranslation"
fieldValue59.value = "0 2 0"
ProtoInstance58.addFieldValue([fieldValue59])

IS60 = IS()

connect61 = connect()
connect61.nodeField = "myShape"
connect61.protoField = "myShape"
IS60.addConnect([connect61])
ProtoInstance58.IS = IS60
Transform51.addChildren([ProtoInstance58])

ProtoInstance62 = ProtoInstance()
ProtoInstance62.name = "three"

fieldValue63 = fieldValue()
fieldValue63.name = "ytranslation"
fieldValue63.value = "0 -2 0"
ProtoInstance62.addFieldValue([fieldValue63])

IS64 = IS()

connect65 = connect()
connect65.nodeField = "myShape"
connect65.protoField = "myShape"
IS64.addConnect([connect65])
ProtoInstance62.IS = IS64
Transform51.addChildren([ProtoInstance62])
ProtoBody50.addChildren([Transform51])
ProtoDeclare45.protoBody = ProtoBody50
Scene7.addChildren([ProtoDeclare45])

ProtoDeclare66 = ProtoDeclare()
ProtoDeclare66.name = "twentyseven"

ProtoInterface67 = ProtoInterface()

field68 = field()
field68.name = "ttranslation"
field68.accessType = "inputOutput"
field68.type = "SFVec3f"
field68.value = "0.0 0.0 0.0"
ProtoInterface67.addField([field68])

field69 = field()
field69.name = "myShape"
field69.accessType = "inputOutput"
field69.type = "SFNode"

Sphere70 = Sphere()
field69.addChildren([Sphere70])
ProtoInterface67.addField([field69])
ProtoDeclare66.protoInterface = ProtoInterface67

ProtoBody71 = ProtoBody()

Transform72 = Transform()
Transform72.translation = [0,0,0]

IS73 = IS()

connect74 = connect()
connect74.nodeField = "translation"
connect74.protoField = "ttranslation"
IS73.addConnect([connect74])
Transform72.IS = IS73

ProtoInstance75 = ProtoInstance()
ProtoInstance75.name = "nine"

fieldValue76 = fieldValue()
fieldValue76.name = "ztranslation"
fieldValue76.value = "0 0 0"
ProtoInstance75.addFieldValue([fieldValue76])

IS77 = IS()

connect78 = connect()
connect78.nodeField = "myShape"
connect78.protoField = "myShape"
IS77.addConnect([connect78])
ProtoInstance75.IS = IS77
Transform72.addChildren([ProtoInstance75])

ProtoInstance79 = ProtoInstance()
ProtoInstance79.name = "nine"

fieldValue80 = fieldValue()
fieldValue80.name = "ztranslation"
fieldValue80.value = "0 0 2"
ProtoInstance79.addFieldValue([fieldValue80])

IS81 = IS()

connect82 = connect()
connect82.nodeField = "myShape"
connect82.protoField = "myShape"
IS81.addConnect([connect82])
ProtoInstance79.IS = IS81
Transform72.addChildren([ProtoInstance79])

ProtoInstance83 = ProtoInstance()
ProtoInstance83.name = "nine"

fieldValue84 = fieldValue()
fieldValue84.name = "ztranslation"
fieldValue84.value = "0 0 -2"
ProtoInstance83.addFieldValue([fieldValue84])

IS85 = IS()

connect86 = connect()
connect86.nodeField = "myShape"
connect86.protoField = "myShape"
IS85.addConnect([connect86])
ProtoInstance83.IS = IS85
Transform72.addChildren([ProtoInstance83])
ProtoBody71.addChildren([Transform72])
ProtoDeclare66.protoBody = ProtoBody71
Scene7.addChildren([ProtoDeclare66])

ProtoInstance87 = ProtoInstance()
ProtoInstance87.name = "twentyseven"

fieldValue88 = fieldValue()
fieldValue88.name = "ttranslation"
fieldValue88.value = "0 0 0"
ProtoInstance87.addFieldValue([fieldValue88])

fieldValue89 = fieldValue()
fieldValue89.name = "myShape"

Box90 = Box(size = [1,1,1])
fieldValue89.addChildren([Box90])
ProtoInstance87.addFieldValue([fieldValue89])
Scene7.addChildren([ProtoInstance87])
X3D0.scene = Scene7
