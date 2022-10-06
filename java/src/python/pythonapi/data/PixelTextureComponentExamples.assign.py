from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.content = "PixelTextureComponentExamples.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "This example shows the five PixelTexture components, with 0 to 4 components each, shown in Table 5-18."
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Leonard Daly and Don Brutzman"
meta4.name = "creator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "25 August 2008"
meta5.name = "created"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "7 January 2014"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "http://X3dGraphics.com"
meta7.name = "reference"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "X3D for Web Authors, Table 5.18"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "http://www.web3d.org/x3d/content/examples/X3dResources.html"
meta9.name = "reference"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "Copyright (c) 2006, Daly Realism and Don Brutzman"
meta10.name = "rights"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com"
meta11.name = "subject"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter05AppearanceMaterialTextures/PixelTextureComponentExamples.x3d"
meta12.name = "identifier"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta13.name = "generator"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "../license.html"
meta14.name = "license"
head1.addMeta([meta14])
X3D0.head = head1

Scene15 = Scene()

Background16 = Background()
Background16.skyColor = [0.1,0.1,0.4]
Scene15.addChildren([Background16])

Viewpoint17 = Viewpoint()
Viewpoint17.description = "Table 5.18 SFImage component examples"
Viewpoint17.position = [0,0,14]
Scene15.addChildren([Viewpoint17])

Transform18 = Transform()
Transform18.translation = [-6,0,0]

Shape19 = Shape()

Appearance20 = Appearance()

PixelTexture21 = PixelTexture()
PixelTexture21.DEF = "ZeroComponents"
Appearance20.texture = PixelTexture21
Shape19.appearance = Appearance20

Box22 = Box()
Shape19.geometry = Box22
Transform18.addChildren([Shape19])

Transform23 = Transform()
Transform23.translation = [0,-2,0]

Shape24 = Shape()

Text25 = Text()
Text25.string = ["0"]

FontStyle26 = FontStyle(justify = ["MIDDLE","MIDDLE"])
FontStyle26.DEF = "CenterJustify"
Text25.fontStyle = FontStyle26
Shape24.geometry = Text25

Appearance27 = Appearance()
Appearance27.DEF = "TextMaterial"

Material28 = Material()
Material28.diffuseColor = [1,1,1]
Appearance27.material = Material28
Shape24.appearance = Appearance27
Transform23.addChildren([Shape24])
Transform18.addChildren([Transform23])
Scene15.addChildren([Transform18])

Transform29 = Transform()
Transform29.translation = [-3,0,0]

Shape30 = Shape()

Appearance31 = Appearance()

PixelTexture32 = PixelTexture()
PixelTexture32.DEF = "OneComponent"
PixelTexture32.image = [1,2,1,0xFF,0x00]
Appearance31.texture = PixelTexture32
Shape30.appearance = Appearance31

Box33 = Box()
Shape30.geometry = Box33
Transform29.addChildren([Shape30])

Transform34 = Transform()
Transform34.translation = [0,-2,0]

Shape35 = Shape()

Text36 = Text()
Text36.string = ["1"]

FontStyle37 = FontStyle()
FontStyle37.USE = "CenterJustify"
Text36.fontStyle = FontStyle37
Shape35.geometry = Text36

Appearance38 = Appearance()
Appearance38.USE = "TextMaterial"
Shape35.appearance = Appearance38
Transform34.addChildren([Shape35])
Transform29.addChildren([Transform34])
Scene15.addChildren([Transform29])

Transform39 = Transform()

Shape40 = Shape()

Appearance41 = Appearance()

PixelTexture42 = PixelTexture()
PixelTexture42.DEF = "TwoComponents"
PixelTexture42.image = [2,1,2,0xCCFF,0x2277]
Appearance41.texture = PixelTexture42
Shape40.appearance = Appearance41

Box43 = Box()
Shape40.geometry = Box43
Transform39.addChildren([Shape40])

Transform44 = Transform()
Transform44.translation = [0,-2,0]

Shape45 = Shape()

Text46 = Text()
Text46.string = ["2"]

FontStyle47 = FontStyle()
FontStyle47.USE = "CenterJustify"
Text46.fontStyle = FontStyle47
Shape45.geometry = Text46

Appearance48 = Appearance()
Appearance48.USE = "TextMaterial"
Shape45.appearance = Appearance48
Transform44.addChildren([Shape45])
Transform39.addChildren([Transform44])
Scene15.addChildren([Transform39])

Transform49 = Transform()
Transform49.translation = [3,0,0]

Shape50 = Shape()

Appearance51 = Appearance()
# note 0x000000 = 0 

PixelTexture52 = PixelTexture()
PixelTexture52.DEF = "ThreeComponents"
PixelTexture52.image = [2,4,3,0xFF0000,0xFF00,0x000000,0,0,0,0xFFFFFF,0xFFFF00]
Appearance51.texture = PixelTexture52
Shape50.appearance = Appearance51

Box53 = Box()
Shape50.geometry = Box53
Transform49.addChildren([Shape50])

Transform54 = Transform()
Transform54.translation = [0,-2,0]

Shape55 = Shape()

Text56 = Text()
Text56.string = ["3"]

FontStyle57 = FontStyle()
FontStyle57.USE = "CenterJustify"
Text56.fontStyle = FontStyle57
Shape55.geometry = Text56

Appearance58 = Appearance()
Appearance58.USE = "TextMaterial"
Shape55.appearance = Appearance58
Transform54.addChildren([Shape55])
Transform49.addChildren([Transform54])
Scene15.addChildren([Transform49])

Transform59 = Transform()
Transform59.translation = [6,0,0]

Shape60 = Shape()

Appearance61 = Appearance()
# Erroneous value in book: 1 0 0 255, 0 1 0 255, 0 0 1 255, 1 0 0 127, 0 1 0 127, 0 0 1 127 

PixelTexture62 = PixelTexture()
PixelTexture62.DEF = "FourComponents"
PixelTexture62.image = [3,2,4,-16776961,0x00FF00FF,0x0000FFFF,-16777089,0x00FF007F,0x0000FF7F]
Appearance61.texture = PixelTexture62
Shape60.appearance = Appearance61

Box63 = Box()
Shape60.geometry = Box63
Transform59.addChildren([Shape60])

Transform64 = Transform()
Transform64.translation = [0,-2,0]

Shape65 = Shape()

Text66 = Text()
Text66.string = ["4"]

FontStyle67 = FontStyle()
FontStyle67.USE = "CenterJustify"
Text66.fontStyle = FontStyle67
Shape65.geometry = Text66

Appearance68 = Appearance()
Appearance68.USE = "TextMaterial"
Shape65.appearance = Appearance68
Transform64.addChildren([Shape65])
Transform59.addChildren([Transform64])
Scene15.addChildren([Transform59])
# Background from PixelTextureBW.x3d 

Transform69 = Transform()
Transform69.translation = [0,6,-2]

Shape70 = Shape()

Appearance71 = Appearance()

PixelTexture72 = PixelTexture()
PixelTexture72.image = [8,8,1,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc]
Appearance71.texture = PixelTexture72
Shape70.appearance = Appearance71

Box73 = Box(size = [16,16,.1])
Shape70.geometry = Box73
Transform69.addChildren([Shape70])
Scene15.addChildren([Transform69])
X3D0.scene = Scene15
