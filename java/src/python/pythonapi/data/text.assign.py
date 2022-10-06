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
meta4.content = "text.x3d"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/text.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "test \\n text"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "generator"
meta7.content = "Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit"
head1.addMeta([meta7])
X3D0.head = head1

Scene8 = Scene()

Transform9 = Transform()

Shape10 = Shape()

Text11 = Text()
Text11.string = ["Node\"\"\""]

FontStyle12 = FontStyle()
Text11.fontStyle = FontStyle12
Shape10.geometry = Text11

Appearance13 = Appearance()

Material14 = Material()
Appearance13.material = Material14
Shape10.appearance = Appearance13
Transform9.addChildren([Shape10])

Shape15 = Shape()

Text16 = Text()
Text16.string = ["Node2","\\\\","\\\\\\\\","Node2"]

FontStyle17 = FontStyle()
Text16.fontStyle = FontStyle17
Shape15.geometry = Text16

Appearance18 = Appearance()

Material19 = Material()
Appearance18.material = Material19
Shape15.appearance = Appearance18
Transform9.addChildren([Shape15])

Shape20 = Shape()

Text21 = Text()
Text21.string = ["Node3 \\\\\\\\ \\\\ ","Node3\"\"\""]

FontStyle22 = FontStyle()
Text21.fontStyle = FontStyle22
Shape20.geometry = Text21

Appearance23 = Appearance()

Material24 = Material()
Appearance23.material = Material24
Shape20.appearance = Appearance23
Transform9.addChildren([Shape20])

Script25 = Script()

field26 = field()
field26.name = "frontUrls"
field26.type = "MFString"
field26.accessType = "initializeOnly"
field26.value = "\"rnl_front.png\" \"uffizi_front.png\""
Script25.addField([field26])

Script25.setSourceCode('''ecmascript:\n"+
"			    var me = '\"1\" \"\\\"2\" \"\\n3\"';\n"+
"			    ''')
Transform9.addChildren([Script25])
Scene8.addChildren([Transform9])
X3D0.scene = Scene8
