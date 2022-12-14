from X3Dpackage import *
X3D0 = X3D(profile="Interchange", version="3.0",    head1 = head(    meta2 = meta(content="indexedfaceset_pixeltexture_entire.x3d", name="title"), 
    meta3 = meta(content="http://www.nist.gov/vrml.html", name="reference"), 
    meta4 = meta(content="http://www.itl.nist.gov/div897/ctg/vrml/vrml.html", name="reference"), 
    meta5 = meta(content="http://www.itl.nist.gov/div897/ctg/vrml/members.html", name="creator"), 
    meta6 = meta(content="This file was provided by the National Institute of Standards and Technology, and is part of the X3D Conformance Test Suite, available at http://www.nist.gov/vrml.html The information contained within this file is provided for use in establishing conformance to the ISO VRML97 Specification. Conformance to this test does not imply recommendation or endorsement by the National Institute of Standards and Technology. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.", name="disclaimer"), 
    meta7 = meta(content="Correct definition and compliance of this conformance scene is maintained by the X3D Working Group, http://www.web3d.org/working-groups/x3d", name="info"), 
    meta8 = meta(content="Michael Kass NIST, Don Brutzman NPS", name="translator"), 
    meta9 = meta(content="21 January 2001", name="translated"), 
    meta10 = meta(content="13 January 2014", name="modified"), 
    meta11 = meta(content="Test browser ability to completely map one PixelTexture onto the surface of an IndexedFaceSet geometry. Four colored squares should map onto each face of the IndexedFaceSet. The PixelTexture consists of red quarter (lower left), green quarter (lower right), white quarter (upper left) and yellow quarter (upper right). PixelTexture should map once onto the surface of the IndexedFaceSet, with the S (horizontal) axis of the texture corresponding to the X axis of the geometry.", name="description"), 
    meta12 = meta(content="http://www.web3d.org/x3d/content/examples/ConformanceNist/GeometricProperties/TextureCoordinate/indexedfaceset_pixeltexture_entire.x3d", name="identifier"), 
    meta13 = meta(content="Vrml97ToX3dNist, http://ovrt.nist.gov/v2_x3d.html", name="generator"), 
    meta14 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta15 = meta(content="../../license.html", name="license")), 
   Scene16 = Scene(    Viewpoint17 = Viewpoint(description="Front View"), 
    Viewpoint18 = Viewpoint(description="Rear View", orientation=[0,1,0,3.14], position=[0,0,-10]), 
    Viewpoint19 = Viewpoint(description="Top View", orientation=[1,0,0,-1.57], position=[0,10,0]), 
    Viewpoint20 = Viewpoint(description="Bottom View", orientation=[1,0,0,1.57], position=[0,-10,0]), 
    Viewpoint21 = Viewpoint(description="Right View", orientation=[0,1,0,1.57], position=[10,0,0]), 
    Viewpoint22 = Viewpoint(description="Left View", orientation=[0,1,0,-1.57], position=[-10,0,0]), 
    NavigationInfo23 = NavigationInfo(type=["EXAMINE","WALK","FLY","ANY"]), 
    Shape24 = Shape(     Appearance25 = Appearance(      Material26 = Material(), 
      PixelTexture27 = PixelTexture(image=[2,2,4,-16776961,0x00FF00FF,-1,-65281], repeatS=False, repeatT=False)), 
     IndexedFaceSet28 = IndexedFaceSet(coordIndex=[0,1,3,2,-1,4,5,7,6,-1,6,7,1,0,-1,2,3,5,4,-1,6,0,2,4,-1,1,7,5,3,-1],       Coordinate29 = Coordinate(point=[-2,1.5,1,-2,-1.5,1,2,1.5,1,2,-1.5,1,2,1.5,-1,2,-1.5,-1,-2,1.5,-1,-2,-1.5,-1])))))
