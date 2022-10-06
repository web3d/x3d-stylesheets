from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.0"

head1 = head()

meta2 = meta()
meta2.content = "TextExamples.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Show different escape-character text examples for embedded quotation marks."
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Don Brutzman"
meta4.name = "creator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "7 April 2001"
meta5.name = "created"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "26 April 2016"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "Note that X3D Canonicalization (C14N) will scrub alternate XML character representations, be careful to check original encoding into version control."
meta7.name = "warning"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "Usually this source document needs to be inspected and edited using a plain-text editor in order to see the differences in these XML-equivalent text representations."
meta8.name = "warning"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "http://www.web3d.org/x3d/content/examples/Basic/development/TextExamples.x3d"
meta9.name = "identifier"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta10.name = "generator"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "../license.html"
meta11.name = "license"
head1.addMeta([meta11])
X3D0.head = head1

Scene12 = Scene()

Transform13 = Transform()
Transform13.translation = [0,2,0]

Shape14 = Shape()

Text15 = Text()
Text15.string = ["Compare special character escaping"]

FontStyle16 = FontStyle(justify = ["MIDDLE","MIDDLE"], size = 0.8)
FontStyle16.DEF = "testFontStyle"
Text15.fontStyle = FontStyle16
Shape14.geometry = Text15

Appearance17 = Appearance()
Appearance17.DEF = "LightBlueAppearance"

Material18 = Material()
Material18.diffuseColor = [0.1,0.7,0.7]
Appearance17.material = Material18
Shape14.appearance = Appearance17
Transform13.addChildren([Shape14])
Scene12.addChildren([Transform13])

Transform19 = Transform()
Transform19.translation = [-3,0,0]

Shape20 = Shape()

Text21 = Text()
Text21.string = ["I don't think so","","he said \"Hi\""]

FontStyle22 = FontStyle()
FontStyle22.USE = "testFontStyle"
Text21.fontStyle = FontStyle22
Shape20.geometry = Text21

Appearance23 = Appearance()
Appearance23.USE = "LightBlueAppearance"
Shape20.appearance = Appearance23
Transform19.addChildren([Shape20])
Scene12.addChildren([Transform19])

Transform24 = Transform()
Transform24.translation = [3,0,0]

Shape25 = Shape()

Text26 = Text()
Text26.string = ["I don't think so","","he said \"Hi\""]

FontStyle27 = FontStyle()
FontStyle27.USE = "testFontStyle"
Text26.fontStyle = FontStyle27
Shape25.geometry = Text26

Appearance28 = Appearance()
Appearance28.USE = "LightBlueAppearance"
Shape25.appearance = Appearance28
Transform24.addChildren([Shape25])
Scene12.addChildren([Transform24])
X3D0.scene = Scene12
