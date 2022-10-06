from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.content = "Table5_18PixelTexture"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "PixelTexture example for Table 5.18"
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Leonard Daly and Don Brutzman"
meta4.name = "creator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "18 December 2006"
meta5.name = "created"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "2 April 2017"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "http://X3dGraphics.com"
meta7.name = "reference"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "http://www.web3d.org/x3d/content/examples/X3dResources.html"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "Copyright 2006, Daly Realism and Don Brutzman"
meta9.name = "rights"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "X3D, PixelTexture"
meta10.name = "subject"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter05AppearanceMaterialTextures/Table5_18PixelTexture"
meta11.name = "identifier"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta12.name = "generator"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "../license.html"
meta13.name = "license"
head1.addMeta([meta13])
X3D0.head = head1

Scene14 = Scene()

Background15 = Background()
Background15.skyColor = [0,0,1]
Scene14.addChildren([Background15])

Transform16 = Transform()
Transform16.DEF = "Checkerboard"
Transform16.translation = [0,0,-10]

Shape17 = Shape()

Appearance18 = Appearance()

TextureTransform19 = TextureTransform()
TextureTransform19.scale = [500,500]
Appearance18.textureTransform = TextureTransform19

PixelTexture20 = PixelTexture()
PixelTexture20.image = [2,2,3,0xE6B5FD,0xFFDBB7,0xFFDBB7,0xE6B5FD]
Appearance18.texture = PixelTexture20
Shape17.appearance = Appearance18

Box21 = Box(size = [1000,1000,.01])
Shape17.geometry = Box21
Transform16.addChildren([Shape17])
Scene14.addChildren([Transform16])

Viewpoint22 = Viewpoint()
Viewpoint22.description = "View All"
Viewpoint22.position = [0,0,20]
Scene14.addChildren([Viewpoint22])

Viewpoint23 = Viewpoint()
Viewpoint23.description = "Empty Image"
Viewpoint23.position = [0,5,5]
Scene14.addChildren([Viewpoint23])

Transform24 = Transform()
Transform24.DEF = "EmptyImage"
Transform24.rotation = [1,1,0,1]
Transform24.translation = [0,5,0]

Shape25 = Shape()

Appearance26 = Appearance()

PixelTexture27 = PixelTexture()
Appearance26.texture = PixelTexture27
Shape25.appearance = Appearance26

Box28 = Box()
Box28.DEF = "StandardBox"
Shape25.geometry = Box28
Transform24.addChildren([Shape25])
Scene14.addChildren([Transform24])

Viewpoint29 = Viewpoint()
Viewpoint29.description = "Black and white PixelTexture"
Viewpoint29.position = [-5,0,5]
Scene14.addChildren([Viewpoint29])

Transform30 = Transform()
Transform30.DEF = "BW"
Transform30.rotation = [1,1,0,1]
Transform30.translation = [-5,0,0]

Shape31 = Shape()

Appearance32 = Appearance()

PixelTexture33 = PixelTexture()
PixelTexture33.image = [1,2,1,0xFF,0x00]
Appearance32.texture = PixelTexture33
Shape31.appearance = Appearance32

Box34 = Box()
Box34.USE = "StandardBox"
Shape31.geometry = Box34
Transform30.addChildren([Shape31])
Scene14.addChildren([Transform30])

Viewpoint35 = Viewpoint()
Viewpoint35.description = "Black and white with Alpha PixelTexture"
Viewpoint35.position = [5,0,5]
Scene14.addChildren([Viewpoint35])

Transform36 = Transform()
Transform36.DEF = "AlphaBW"
Transform36.rotation = [1,1,0,1]
Transform36.translation = [5,0,0]

Shape37 = Shape()

Appearance38 = Appearance()

PixelTexture39 = PixelTexture()
PixelTexture39.image = [2,1,2,0xCCFF,0x2277]
Appearance38.texture = PixelTexture39
Shape37.appearance = Appearance38

Box40 = Box()
Box40.USE = "StandardBox"
Shape37.geometry = Box40
Transform36.addChildren([Shape37])
Scene14.addChildren([Transform36])

Viewpoint41 = Viewpoint()
Viewpoint41.description = "RGB PixelTexture"
Viewpoint41.position = [-5,-5,5]
Scene14.addChildren([Viewpoint41])

Transform42 = Transform()
Transform42.DEF = "RGB"
Transform42.rotation = [1,1,0,1]
Transform42.translation = [-5,-5,0]

Shape43 = Shape()

Appearance44 = Appearance()

PixelTexture45 = PixelTexture()
PixelTexture45.image = [2,4,3,0xFF0000,0x00FF00,0,0,0,0,0xFFFFFF,0xFFFF00]
Appearance44.texture = PixelTexture45
Shape43.appearance = Appearance44

Box46 = Box()
Box46.USE = "StandardBox"
Shape43.geometry = Box46
Transform42.addChildren([Shape43])
Scene14.addChildren([Transform42])

Viewpoint47 = Viewpoint()
Viewpoint47.description = "RGB with Alpha PixelTexture"
Viewpoint47.position = [5,-5,5]
Scene14.addChildren([Viewpoint47])

Transform48 = Transform()
Transform48.DEF = "AlphaRGB"
Transform48.rotation = [1,1,0,1]
Transform48.translation = [5,-5,0]

Shape49 = Shape()

Appearance50 = Appearance()

PixelTexture51 = PixelTexture()
PixelTexture51.image = [3,2,4,-16776961,0x00FF00FF,0x0000FFFF,-16777089,0x00FF007F,0x0000FF7F]
Appearance50.texture = PixelTexture51
Shape49.appearance = Appearance50

Box52 = Box()
Box52.USE = "StandardBox"
Shape49.geometry = Box52
Transform48.addChildren([Shape49])
Scene14.addChildren([Transform48])
X3D0.scene = Scene14
