from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.0"

head1 = head()

meta2 = meta()
meta2.content = "indexedfaceset_pixeltexture_part.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "indexedfaceset_pixeltexture_part-front.jpg"
meta3.name = "Image"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "indexedfaceset_pixeltexture_part-rear.jpg"
meta4.name = "Image"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "indexedfaceset_pixeltexture_part-top.jpg"
meta5.name = "Image"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "indexedfaceset_pixeltexture_part-bottom.jpg"
meta6.name = "Image"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "indexedfaceset_pixeltexture_part-left.jpg"
meta7.name = "Image"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "indexedfaceset_pixeltexture_part-right.jpg"
meta8.name = "Image"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "http://www.nist.gov/vrml.html"
meta9.name = "reference"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "http://www.itl.nist.gov/div897/ctg/vrml/vrml.html"
meta10.name = "reference"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "http://www.itl.nist.gov/div897/ctg/vrml/members.html"
meta11.name = "creator"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "This file was provided by the National Institute of Standards and Technology, and is part of the X3D Conformance Test Suite, available at http://www.nist.gov/vrml.html The information contained within this file is provided for use in establishing conformance to the ISO VRML97 Specification. Conformance to this test does not imply recommendation or endorsement by the National Institute of Standards and Technology. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified."
meta12.name = "disclaimer"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "Correct definition and compliance of this conformance scene is maintained by the X3D Working Group, http://www.web3d.org/working-groups/x3d"
meta13.name = "info"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "Michael Kass NIST, Don Brutzman NPS"
meta14.name = "translator"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "21 January 2001"
meta15.name = "translated"
head1.addMeta([meta15])

meta16 = meta()
meta16.content = "13 January 2014"
meta16.name = "modified"
head1.addMeta([meta16])

meta17 = meta()
meta17.content = "Test of browser ability to map a partial portion of an PixelTexture onto an IndexedFaceSet geometry. Only the yellow portion of four equal sized red, green, yellow and white squares in the pixel texture map all the faces of the cube."
meta17.name = "description"
head1.addMeta([meta17])

meta18 = meta()
meta18.content = "http://www.web3d.org/x3d/content/examples/ConformanceNist/GeometricProperties/TextureCoordinate/indexedfaceset_pixeltexture_part.x3d"
meta18.name = "identifier"
head1.addMeta([meta18])

meta19 = meta()
meta19.content = "Vrml97ToX3dNist, http://ovrt.nist.gov/v2_x3d.html"
meta19.name = "generator"
head1.addMeta([meta19])

meta20 = meta()
meta20.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta20.name = "generator"
head1.addMeta([meta20])

meta21 = meta()
meta21.content = "../../license.html"
meta21.name = "license"
head1.addMeta([meta21])
X3D0.head = head1

Scene22 = Scene()

Viewpoint23 = Viewpoint()
Viewpoint23.description = "Front View"
Scene22.addChildren([Viewpoint23])

Viewpoint24 = Viewpoint()
Viewpoint24.description = "Rear View"
Viewpoint24.orientation = [0,1,0,3.14]
Viewpoint24.position = [0,0,-10]
Scene22.addChildren([Viewpoint24])

Viewpoint25 = Viewpoint()
Viewpoint25.description = "Top View"
Viewpoint25.orientation = [1,0,0,-1.57]
Viewpoint25.position = [0,10,0]
Scene22.addChildren([Viewpoint25])

Viewpoint26 = Viewpoint()
Viewpoint26.description = "Bottom View"
Viewpoint26.orientation = [1,0,0,1.57]
Viewpoint26.position = [0,-10,0]
Scene22.addChildren([Viewpoint26])

Viewpoint27 = Viewpoint()
Viewpoint27.description = "Right View"
Viewpoint27.orientation = [0,1,0,1.57]
Viewpoint27.position = [10,0,0]
Scene22.addChildren([Viewpoint27])

Viewpoint28 = Viewpoint()
Viewpoint28.description = "Left View"
Viewpoint28.orientation = [0,1,0,-1.57]
Viewpoint28.position = [-10,0,0]
Scene22.addChildren([Viewpoint28])

NavigationInfo29 = NavigationInfo()
NavigationInfo29.type = ["EXAMINE","WALK","FLY","ANY"]
Scene22.addChildren([NavigationInfo29])

Shape30 = Shape()

Appearance31 = Appearance()

Material32 = Material()
Appearance31.material = Material32

PixelTexture33 = PixelTexture()
PixelTexture33.image = [2,2,4,-16776961,0x00FF00FF,-1,-65281]
Appearance31.texture = PixelTexture33
Shape30.appearance = Appearance31

IndexedFaceSet34 = IndexedFaceSet(colorPerVertex = False, coordIndex = [0,1,3,2,-1,4,5,7,6,-1,6,7,1,0,-1,2,3,5,4,-1,6,0,2,4,-1,1,7,5,3,-1], creaseAngle = 0.5, texCoordIndex = [0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1])

Color35 = Color()
Color35.color = [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0]
IndexedFaceSet34.color = Color35

Coordinate36 = Coordinate()
Coordinate36.point = [-2,1,1,-2,-1,1,2,1,1,2,-1,1,2,1,-1,2,-1,-1,-2,1,-1,-2,-1,-1]
IndexedFaceSet34.coord = Coordinate36

TextureCoordinate37 = TextureCoordinate()
TextureCoordinate37.point = [0.5,1,0.5,0.5,1,1,1,0.5]
IndexedFaceSet34.texCoord = TextureCoordinate37
Shape30.geometry = IndexedFaceSet34
Scene22.addChildren([Shape30])
X3D0.scene = Scene22
