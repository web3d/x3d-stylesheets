from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.0"

head1 = head()

meta2 = meta()
meta2.content = "indexedfaceset_pixeltexture_entire.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "http://www.nist.gov/vrml.html"
meta3.name = "reference"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "http://www.itl.nist.gov/div897/ctg/vrml/vrml.html"
meta4.name = "reference"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "http://www.itl.nist.gov/div897/ctg/vrml/members.html"
meta5.name = "creator"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "This file was provided by the National Institute of Standards and Technology, and is part of the X3D Conformance Test Suite, available at http://www.nist.gov/vrml.html The information contained within this file is provided for use in establishing conformance to the ISO VRML97 Specification. Conformance to this test does not imply recommendation or endorsement by the National Institute of Standards and Technology. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified."
meta6.name = "disclaimer"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "Correct definition and compliance of this conformance scene is maintained by the X3D Working Group, http://www.web3d.org/working-groups/x3d"
meta7.name = "info"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "Michael Kass NIST, Don Brutzman NPS"
meta8.name = "translator"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "21 January 2001"
meta9.name = "translated"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "13 January 2014"
meta10.name = "modified"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "Test browser ability to completely map one PixelTexture onto the surface of an IndexedFaceSet geometry. Four colored squares should map onto each face of the IndexedFaceSet. The PixelTexture consists of red quarter (lower left), green quarter (lower right), white quarter (upper left) and yellow quarter (upper right). PixelTexture should map once onto the surface of the IndexedFaceSet, with the S (horizontal) axis of the texture corresponding to the X axis of the geometry."
meta11.name = "description"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "http://www.web3d.org/x3d/content/examples/ConformanceNist/GeometricProperties/TextureCoordinate/indexedfaceset_pixeltexture_entire.x3d"
meta12.name = "identifier"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "Vrml97ToX3dNist, http://ovrt.nist.gov/v2_x3d.html"
meta13.name = "generator"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta14.name = "generator"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "../../license.html"
meta15.name = "license"
head1.addMeta([meta15])
X3D0.head = head1

Scene16 = Scene()

Viewpoint17 = Viewpoint()
Viewpoint17.description = "Front View"
Scene16.addChildren([Viewpoint17])

Viewpoint18 = Viewpoint()
Viewpoint18.description = "Rear View"
Viewpoint18.orientation = [0,1,0,3.14]
Viewpoint18.position = [0,0,-10]
Scene16.addChildren([Viewpoint18])

Viewpoint19 = Viewpoint()
Viewpoint19.description = "Top View"
Viewpoint19.orientation = [1,0,0,-1.57]
Viewpoint19.position = [0,10,0]
Scene16.addChildren([Viewpoint19])

Viewpoint20 = Viewpoint()
Viewpoint20.description = "Bottom View"
Viewpoint20.orientation = [1,0,0,1.57]
Viewpoint20.position = [0,-10,0]
Scene16.addChildren([Viewpoint20])

Viewpoint21 = Viewpoint()
Viewpoint21.description = "Right View"
Viewpoint21.orientation = [0,1,0,1.57]
Viewpoint21.position = [10,0,0]
Scene16.addChildren([Viewpoint21])

Viewpoint22 = Viewpoint()
Viewpoint22.description = "Left View"
Viewpoint22.orientation = [0,1,0,-1.57]
Viewpoint22.position = [-10,0,0]
Scene16.addChildren([Viewpoint22])

NavigationInfo23 = NavigationInfo()
NavigationInfo23.type = ["EXAMINE","WALK","FLY","ANY"]
Scene16.addChildren([NavigationInfo23])

Shape24 = Shape()

Appearance25 = Appearance()

Material26 = Material()
Appearance25.material = Material26

PixelTexture27 = PixelTexture(repeatS = False, repeatT = False)
PixelTexture27.image = [2,2,4,-16776961,0x00FF00FF,-1,-65281]
Appearance25.texture = PixelTexture27
Shape24.appearance = Appearance25

IndexedFaceSet28 = IndexedFaceSet(coordIndex = [0,1,3,2,-1,4,5,7,6,-1,6,7,1,0,-1,2,3,5,4,-1,6,0,2,4,-1,1,7,5,3,-1])

Coordinate29 = Coordinate()
Coordinate29.point = [-2,1.5,1,-2,-1.5,1,2,1.5,1,2,-1.5,1,2,1.5,-1,2,-1.5,-1,-2,1.5,-1,-2,-1.5,-1]
IndexedFaceSet28.coord = Coordinate29
Shape24.geometry = IndexedFaceSet28
Scene16.addChildren([Shape24])
X3D0.scene = Scene16
