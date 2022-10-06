from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "rubikFurnace.x3d"
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
meta5.content = "https://coderextreme.net/X3DJSONLD/rubikFurnace.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "a green rubik cube"
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
Transform19.translation = [0,0,0]

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
field25.value = "0.0 0.0 0.0"
ProtoInterface24.addField([field25])

field26 = field()
field26.name = "myShape"
field26.accessType = "inputOutput"
field26.type = "MFNode"

Shape27 = Shape()

Sphere28 = Sphere()
Shape27.geometry = Sphere28

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
Transform32.translation = [0,0,0]

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

ProtoDeclare47 = ProtoDeclare()
ProtoDeclare47.name = "nine"

ProtoInterface48 = ProtoInterface()

field49 = field()
field49.name = "ztranslation"
field49.accessType = "inputOutput"
field49.type = "SFVec3f"
field49.value = "0.0 0.0 0.0"
ProtoInterface48.addField([field49])

field50 = field()
field50.name = "myShape"
field50.accessType = "inputOutput"
field50.type = "MFNode"

Shape51 = Shape()

Sphere52 = Sphere()
Shape51.geometry = Sphere52

Appearance53 = Appearance()

Material54 = Material()
Material54.diffuseColor = [1,1,1]
Appearance53.material = Material54
Shape51.appearance = Appearance53
field50.addChildren([Shape51])
ProtoInterface48.addField([field50])
ProtoDeclare47.protoInterface = ProtoInterface48

ProtoBody55 = ProtoBody()

Transform56 = Transform()
Transform56.translation = [0,0,0]

IS57 = IS()

connect58 = connect()
connect58.nodeField = "translation"
connect58.protoField = "ztranslation"
IS57.addConnect([connect58])
Transform56.IS = IS57

ProtoInstance59 = ProtoInstance()
ProtoInstance59.name = "three"

fieldValue60 = fieldValue()
fieldValue60.name = "ytranslation"
fieldValue60.value = "0 0 0"
ProtoInstance59.addFieldValue([fieldValue60])

IS61 = IS()

connect62 = connect()
connect62.nodeField = "myShape"
connect62.protoField = "myShape"
IS61.addConnect([connect62])
ProtoInstance59.IS = IS61
Transform56.addChildren([ProtoInstance59])

ProtoInstance63 = ProtoInstance()
ProtoInstance63.name = "three"

fieldValue64 = fieldValue()
fieldValue64.name = "ytranslation"
fieldValue64.value = "0 2 0"
ProtoInstance63.addFieldValue([fieldValue64])

IS65 = IS()

connect66 = connect()
connect66.nodeField = "myShape"
connect66.protoField = "myShape"
IS65.addConnect([connect66])
ProtoInstance63.IS = IS65
Transform56.addChildren([ProtoInstance63])

ProtoInstance67 = ProtoInstance()
ProtoInstance67.name = "three"

fieldValue68 = fieldValue()
fieldValue68.name = "ytranslation"
fieldValue68.value = "0 -2 0"
ProtoInstance67.addFieldValue([fieldValue68])

IS69 = IS()

connect70 = connect()
connect70.nodeField = "myShape"
connect70.protoField = "myShape"
IS69.addConnect([connect70])
ProtoInstance67.IS = IS69
Transform56.addChildren([ProtoInstance67])
ProtoBody55.addChildren([Transform56])
ProtoDeclare47.protoBody = ProtoBody55
Scene7.addChildren([ProtoDeclare47])

ProtoDeclare71 = ProtoDeclare()
ProtoDeclare71.name = "twentyseven"

ProtoInterface72 = ProtoInterface()

field73 = field()
field73.name = "ttranslation"
field73.accessType = "inputOutput"
field73.type = "SFVec3f"
field73.value = "0.0 0.0 0.0"
ProtoInterface72.addField([field73])

field74 = field()
field74.name = "myShape"
field74.accessType = "inputOutput"
field74.type = "MFNode"

Shape75 = Shape()

Sphere76 = Sphere()
Shape75.geometry = Sphere76

Appearance77 = Appearance()

Material78 = Material()
Material78.diffuseColor = [1,1,1]
Appearance77.material = Material78
Shape75.appearance = Appearance77
field74.addChildren([Shape75])
ProtoInterface72.addField([field74])
ProtoDeclare71.protoInterface = ProtoInterface72

ProtoBody79 = ProtoBody()

Transform80 = Transform()
Transform80.translation = [0,0,0]

IS81 = IS()

connect82 = connect()
connect82.nodeField = "translation"
connect82.protoField = "ttranslation"
IS81.addConnect([connect82])
Transform80.IS = IS81

ProtoInstance83 = ProtoInstance()
ProtoInstance83.name = "nine"

fieldValue84 = fieldValue()
fieldValue84.name = "ztranslation"
fieldValue84.value = "0 0 0"
ProtoInstance83.addFieldValue([fieldValue84])

IS85 = IS()

connect86 = connect()
connect86.nodeField = "myShape"
connect86.protoField = "myShape"
IS85.addConnect([connect86])
ProtoInstance83.IS = IS85
Transform80.addChildren([ProtoInstance83])

ProtoInstance87 = ProtoInstance()
ProtoInstance87.name = "nine"

fieldValue88 = fieldValue()
fieldValue88.name = "ztranslation"
fieldValue88.value = "0 0 2"
ProtoInstance87.addFieldValue([fieldValue88])

IS89 = IS()

connect90 = connect()
connect90.nodeField = "myShape"
connect90.protoField = "myShape"
IS89.addConnect([connect90])
ProtoInstance87.IS = IS89
Transform80.addChildren([ProtoInstance87])

ProtoInstance91 = ProtoInstance()
ProtoInstance91.name = "nine"

fieldValue92 = fieldValue()
fieldValue92.name = "ztranslation"
fieldValue92.value = "0 0 -2"
ProtoInstance91.addFieldValue([fieldValue92])

IS93 = IS()

connect94 = connect()
connect94.nodeField = "myShape"
connect94.protoField = "myShape"
IS93.addConnect([connect94])
ProtoInstance91.IS = IS93
Transform80.addChildren([ProtoInstance91])
ProtoBody79.addChildren([Transform80])
ProtoDeclare71.protoBody = ProtoBody79
Scene7.addChildren([ProtoDeclare71])

ProtoInstance95 = ProtoInstance()
ProtoInstance95.name = "twentyseven"

fieldValue96 = fieldValue()
fieldValue96.name = "ttranslation"
fieldValue96.value = "0 0 0"
ProtoInstance95.addFieldValue([fieldValue96])

fieldValue97 = fieldValue()
fieldValue97.name = "myShape"

Shape98 = Shape()

Box99 = Box(size = [1,1,1])
Shape98.geometry = Box99

Appearance100 = Appearance()

Material101 = Material()
Material101.diffuseColor = [0,1,0]
Appearance100.material = Material101
Shape98.appearance = Appearance100
fieldValue97.addChildren([Shape98])
ProtoInstance95.addFieldValue([fieldValue97])
Scene7.addChildren([ProtoInstance95])
X3D0.scene = Scene7
