import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.0")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setContent("ExtrusionHeart.x3d").setName("title"))
        .addMeta(X3Dpackage.meta().setContent("Simple extrusion of a Valentine heart.").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("Class participants in course Introduction to VRML/X3D.").setName("creator"))
        .addMeta(X3Dpackage.meta().setContent("14 February 2001").setName("created"))
        .addMeta(X3Dpackage.meta().setContent("27 November 2015").setName("modified"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/x3d/content/examples/Basic/course/ExtrusionHeart.x3d").setName("identifier"))
        .addMeta(X3Dpackage.meta().setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("../license.html").setName("license")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Viewpoint().setDescription("Extrusion Heart").setOrientation([1,0,0,1.57]).setPosition([0,-4,0]))
        .addChildren(X3Dpackage.Transform().setTranslation([0,-0.5,0])
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Extrusion(setCreaseAngle = 3.14159, setCrossSection = [0,0.8,0.2,1,0.7,0.95,1,0.5,0.8,0,0.5,-0.3,0,-0.7,-0.5,-0.3,-0.8,0,-1,0.5,-0.7,0.95,-0.2,1,0,0.8], setSolid = False, setSpine = [0,0,0,0,0.1,0,0,0.5,0,0,0.9,0,0,1,0]).setScale([0.01,0.01,0.8,0.8,1,1,0.8,0.8,0.01,0.01]))
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([0.8,0.3,0.3])))))))

