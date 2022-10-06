from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.0"

head1 = head()

meta2 = meta()
meta2.content = "indexedfaceset_pixeltexture_whole.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "file did not transform to vrml97"
meta3.name = "warning"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "indexedfaceset_pixeltexture_whole-front.jpg"
meta4.name = "Image"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "indexedfaceset_pixeltexture_whole-rear.jpg"
meta5.name = "Image"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "indexedfaceset_pixeltexture_whole-top.jpg"
meta6.name = "Image"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "indexedfaceset_pixeltexture_whole-bottom.jpg"
meta7.name = "Image"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "indexedfaceset_pixeltexture_whole-left.jpg"
meta8.name = "Image"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "indexedfaceset_pixeltexture_whole-right.jpg"
meta9.name = "Image"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "http://www.nist.gov/vrml.html"
meta10.name = "reference"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "http://www.itl.nist.gov/div897/ctg/vrml/vrml.html"
meta11.name = "reference"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "http://www.itl.nist.gov/div897/ctg/vrml/members.html"
meta12.name = "creator"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "This file was provided by the National Institute of Standards and Technology, and is part of the X3D Conformance Test Suite, available at http://www.nist.gov/vrml.html The information contained within this file is provided for use in establishing conformance to the ISO VRML97 Specification. Conformance to this test does not imply recommendation or endorsement by the National Institute of Standards and Technology. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified."
meta13.name = "disclaimer"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "Correct definition and compliance of this conformance scene is maintained by the X3D Working Group, http://www.web3d.org/working-groups/x3d"
meta14.name = "info"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "Michael Kass NIST, Don Brutzman NPS"
meta15.name = "translator"
head1.addMeta([meta15])

meta16 = meta()
meta16.content = "21 January 2001"
meta16.name = "translated"
head1.addMeta([meta16])

meta17 = meta()
meta17.content = "13 January 2014"
meta17.name = "modified"
head1.addMeta([meta17])

meta18 = meta()
meta18.content = "Test of browser ability to map the entire portion of an PixelTexture onto an IndexedFaceSet geometry. Four equal sized red (bottom left), green (bottom right) yellow (top left) and white (top right) squares in the pixel texture map all the faces of the cube."
meta18.name = "description"
head1.addMeta([meta18])

meta19 = meta()
meta19.content = "http://www.web3d.org/x3d/content/examples/ConformanceNist/GeometricProperties/TextureCoordinate/indexedfaceset_pixeltexture_whole.x3d"
meta19.name = "identifier"
head1.addMeta([meta19])

meta20 = meta()
meta20.content = "Vrml97ToX3dNist, http://ovrt.nist.gov/v2_x3d.html"
meta20.name = "generator"
head1.addMeta([meta20])

meta21 = meta()
meta21.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta21.name = "generator"
head1.addMeta([meta21])

meta22 = meta()
meta22.content = "../../license.html"
meta22.name = "license"
head1.addMeta([meta22])
X3D0.head = head1

Scene23 = Scene()

Viewpoint24 = Viewpoint()
Viewpoint24.description = "Front View"
Scene23.addChildren([Viewpoint24])

Viewpoint25 = Viewpoint()
Viewpoint25.description = "Rear View"
Viewpoint25.orientation = [0,1,0,3.14]
Viewpoint25.position = [0,0,-10]
Scene23.addChildren([Viewpoint25])

Viewpoint26 = Viewpoint()
Viewpoint26.description = "Top View"
Viewpoint26.orientation = [1,0,0,-1.57]
Viewpoint26.position = [0,10,0]
Scene23.addChildren([Viewpoint26])

Viewpoint27 = Viewpoint()
Viewpoint27.description = "Bottom View"
Viewpoint27.orientation = [1,0,0,1.57]
Viewpoint27.position = [0,-10,0]
Scene23.addChildren([Viewpoint27])

Viewpoint28 = Viewpoint()
Viewpoint28.description = "Right View"
Viewpoint28.orientation = [0,1,0,1.57]
Viewpoint28.position = [10,0,0]
Scene23.addChildren([Viewpoint28])

Viewpoint29 = Viewpoint()
Viewpoint29.description = "Left View"
Viewpoint29.orientation = [0,1,0,-1.57]
Viewpoint29.position = [-10,0,0]
Scene23.addChildren([Viewpoint29])

NavigationInfo30 = NavigationInfo()
NavigationInfo30.type = ["EXAMINE"]
Scene23.addChildren([NavigationInfo30])

Shape31 = Shape()

Appearance32 = Appearance()

Material33 = Material()
Appearance32.material = Material33

PixelTexture34 = PixelTexture()
PixelTexture34.image = [2,2,4,-16776961,0x00FF00FF,-1,-65281]
Appearance32.texture = PixelTexture34
Shape31.appearance = Appearance32

IndexedFaceSet35 = IndexedFaceSet(colorPerVertex = False, coordIndex = [0,1,3,2,-1,4,5,7,6,-1,6,7,1,0,-1,2,3,5,4,-1,6,0,2,4,-1,1,7,5,3,-1], creaseAngle = 0.5, texCoordIndex = [0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1])

Color36 = Color()
Color36.color = [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0]
IndexedFaceSet35.color = Color36

Coordinate37 = Coordinate()
Coordinate37.point = [-2,1,1,-2,-1,1,2,1,1,2,-1,1,2,1,-1,2,-1,-1,-2,1,-1,-2,-1,-1]
IndexedFaceSet35.coord = Coordinate37

TextureCoordinate38 = TextureCoordinate()
TextureCoordinate38.point = [0,1,0,0,1,1,1,0]
IndexedFaceSet35.texCoord = TextureCoordinate38
Shape31.geometry = IndexedFaceSet35
Scene23.addChildren([Shape31])
X3D0.scene = Scene23
