import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Interchange").setVersion("3.0")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setContent("indexedfaceset_pixeltexture_part.x3d").setName("title"))
        .addMeta(X3Dpackage.meta().setContent("indexedfaceset_pixeltexture_part-front.jpg").setName("Image"))
        .addMeta(X3Dpackage.meta().setContent("indexedfaceset_pixeltexture_part-rear.jpg").setName("Image"))
        .addMeta(X3Dpackage.meta().setContent("indexedfaceset_pixeltexture_part-top.jpg").setName("Image"))
        .addMeta(X3Dpackage.meta().setContent("indexedfaceset_pixeltexture_part-bottom.jpg").setName("Image"))
        .addMeta(X3Dpackage.meta().setContent("indexedfaceset_pixeltexture_part-left.jpg").setName("Image"))
        .addMeta(X3Dpackage.meta().setContent("indexedfaceset_pixeltexture_part-right.jpg").setName("Image"))
        .addMeta(X3Dpackage.meta().setContent("http://www.nist.gov/vrml.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://www.itl.nist.gov/div897/ctg/vrml/vrml.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://www.itl.nist.gov/div897/ctg/vrml/members.html").setName("creator"))
        .addMeta(X3Dpackage.meta().setContent("This file was provided by the National Institute of Standards and Technology, and is part of the X3D Conformance Test Suite, available at http://www.nist.gov/vrml.html The information contained within this file is provided for use in establishing conformance to the ISO VRML97 Specification. Conformance to this test does not imply recommendation or endorsement by the National Institute of Standards and Technology. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.").setName("disclaimer"))
        .addMeta(X3Dpackage.meta().setContent("Correct definition and compliance of this conformance scene is maintained by the X3D Working Group, http://www.web3d.org/working-groups/x3d").setName("info"))
        .addMeta(X3Dpackage.meta().setContent("Michael Kass NIST, Don Brutzman NPS").setName("translator"))
        .addMeta(X3Dpackage.meta().setContent("21 January 2001").setName("translated"))
        .addMeta(X3Dpackage.meta().setContent("13 January 2014").setName("modified"))
        .addMeta(X3Dpackage.meta().setContent("Test of browser ability to map a partial portion of an PixelTexture onto an IndexedFaceSet geometry. Only the yellow portion of four equal sized red, green, yellow and white squares in the pixel texture map all the faces of the cube.").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/x3d/content/examples/ConformanceNist/GeometricProperties/TextureCoordinate/indexedfaceset_pixeltexture_part.x3d").setName("identifier"))
        .addMeta(X3Dpackage.meta().setContent("Vrml97ToX3dNist, http://ovrt.nist.gov/v2_x3d.html").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("../../license.html").setName("license")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Viewpoint().setDescription("Front View"))
        .addChildren(X3Dpackage.Viewpoint().setDescription("Rear View").setOrientation([0,1,0,3.14]).setPosition([0,0,-10]))
        .addChildren(X3Dpackage.Viewpoint().setDescription("Top View").setOrientation([1,0,0,-1.57]).setPosition([0,10,0]))
        .addChildren(X3Dpackage.Viewpoint().setDescription("Bottom View").setOrientation([1,0,0,1.57]).setPosition([0,-10,0]))
        .addChildren(X3Dpackage.Viewpoint().setDescription("Right View").setOrientation([0,1,0,1.57]).setPosition([10,0,0]))
        .addChildren(X3Dpackage.Viewpoint().setDescription("Left View").setOrientation([0,1,0,-1.57]).setPosition([-10,0,0]))
        .addChildren(X3Dpackage.NavigationInfo().setType(["EXAMINE","WALK","FLY","ANY"]))
        .addChildren(X3Dpackage.Shape()
          .setAppearance(X3Dpackage.Appearance()
            .setMaterial(X3Dpackage.Material())
            .setTexture(X3Dpackage.PixelTexture().setImage([2,2,4,-16776961,0x00FF00FF,-1,-65281])))
          .setGeometry(X3Dpackage.IndexedFaceSet(setColorPerVertex = False, setCoordIndex = [0,1,3,2,-1,4,5,7,6,-1,6,7,1,0,-1,2,3,5,4,-1,6,0,2,4,-1,1,7,5,3,-1], setCreaseAngle = 0.5, setTexCoordIndex = [0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1])
            .setColor(X3Dpackage.Color().setColor([0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0]))
            .setCoord(X3Dpackage.Coordinate().setPoint([-2,1,1,-2,-1,1,2,1,1,2,-1,1,2,1,-1,2,-1,-1,-2,1,-1,-2,-1,-1]))
            .setTexCoord(X3Dpackage.TextureCoordinate().setPoint([0.5,1,0.5,0.5,1,1,1,0.5]))))))

