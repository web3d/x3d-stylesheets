from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.0"

head1 = head()

meta2 = meta()
meta2.content = "rgb_alpha.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "rgb_alpha-front.jpg"
meta3.name = "Image"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "rgb_alpha-rear.jpg"
meta4.name = "Image"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "rgb_alpha-top.jpg"
meta5.name = "Image"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "rgb_alpha-bottom.jpg"
meta6.name = "Image"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "http://www.nist.gov/vrml.html"
meta7.name = "reference"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "http://www.itl.nist.gov/div897/ctg/vrml/vrml.html"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "http://www.itl.nist.gov/div897/ctg/vrml/members.html"
meta9.name = "creator"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "This file was provided by the National Institute of Standards and Technology, and is part of the X3D Conformance Test Suite, available at http://www.nist.gov/vrml.html The information contained within this file is provided for use in establishing conformance to the ISO VRML97 Specification. Conformance to this test does not imply recommendation or endorsement by the National Institute of Standards and Technology. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified."
meta10.name = "disclaimer"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "Correct definition and compliance of this conformance scene is maintained by the X3D Working Group, http://www.web3d.org/working-groups/x3d"
meta11.name = "info"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "Michael Kass NIST, Don Brutzman NPS"
meta12.name = "translator"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "21 January 2001"
meta13.name = "translated"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "16 January 2011"
meta14.name = "modified"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "Test browser ability to map a RGB plus alpha opacity to geometry. A checkerboard of four colored squares: lower left (red), lower right (transparent), uppser left (transparent) and upper right (red) map onto the faces of all geometry. For the sphere, the texture should cover the entire surface, and wrap counterclockwise from the back of the sphere. For the cone, the texture should wrap counterclockwise (from above) starting at the back of the cone. A circle cutout of the texture is applied right side up to the base of the cone when the cone is tilted toward the -z axis. For the cylinder, the texture should wrap counterclockwise (from above) starting at the back of the cylinder. A circle cutout of the texture is applied right side up to the top and bottom caps of the cylinder. For the box, the texture should be applied right side up in its entirety to each face of the box."
meta15.name = "description"
head1.addMeta([meta15])

meta16 = meta()
meta16.content = "http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/PixelTexture/rgb_alpha.x3d"
meta16.name = "identifier"
head1.addMeta([meta16])

meta17 = meta()
meta17.content = "Vrml97ToX3dNist, http://ovrt.nist.gov/v2_x3d.html"
meta17.name = "generator"
head1.addMeta([meta17])

meta18 = meta()
meta18.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta18.name = "generator"
head1.addMeta([meta18])

meta19 = meta()
meta19.content = "../../license.html"
meta19.name = "license"
head1.addMeta([meta19])
X3D0.head = head1

Scene20 = Scene()

NavigationInfo21 = NavigationInfo()
NavigationInfo21.type = ["EXAMINE","WALK","FLY","ANY"]
Scene20.addChildren([NavigationInfo21])

Group22 = Group()

Transform23 = Transform()
Transform23.translation = [6.14221,0.0694613,-0.000999451]

Shape24 = Shape()

Appearance25 = Appearance()

Material26 = Material()
Appearance25.material = Material26

PixelTexture27 = PixelTexture()
PixelTexture27.DEF = "RgbOpacityCheckerboard"
PixelTexture27.image = [2,2,4,-16776961,-65536,-65536,-16776961]
Appearance25.texture = PixelTexture27
Shape24.appearance = Appearance25

Box28 = Box()
Shape24.geometry = Box28
Transform23.addChildren([Shape24])
Group22.addChildren([Transform23])

Transform29 = Transform()
Transform29.translation = [-4.85443,0.0694381,-0.00149918]

Shape30 = Shape()

Appearance31 = Appearance()

Material32 = Material()
Appearance31.material = Material32

PixelTexture33 = PixelTexture()
PixelTexture33.USE = "RgbOpacityCheckerboard"
Appearance31.texture = PixelTexture33
Shape30.appearance = Appearance31

Sphere34 = Sphere()
Shape30.geometry = Sphere34
Transform29.addChildren([Shape30])
Group22.addChildren([Transform29])

Transform35 = Transform()
Transform35.translation = [-1.47341,0.036672,-0.00175095]

Shape36 = Shape()

Appearance37 = Appearance()

Material38 = Material()
Appearance37.material = Material38

PixelTexture39 = PixelTexture()
PixelTexture39.USE = "RgbOpacityCheckerboard"
Appearance37.texture = PixelTexture39
Shape36.appearance = Appearance37

Cone40 = Cone()
Shape36.geometry = Cone40
Transform35.addChildren([Shape36])
Group22.addChildren([Transform35])

Transform41 = Transform()
Transform41.translation = [2.31094,0.0694206,-0.00187683]

Shape42 = Shape()

Appearance43 = Appearance()

Material44 = Material()
Appearance43.material = Material44

PixelTexture45 = PixelTexture()
PixelTexture45.USE = "RgbOpacityCheckerboard"
Appearance43.texture = PixelTexture45
Shape42.appearance = Appearance43

Cylinder46 = Cylinder()
Shape42.geometry = Cylinder46
Transform41.addChildren([Shape42])
Group22.addChildren([Transform41])
Scene20.addChildren([Group22])
X3D0.scene = Scene20
