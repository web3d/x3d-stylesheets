import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setContent("qq3.x3d").setName("title"))
        .addMeta(X3Dpackage.meta().setContent("John Carlson").setName("creator"))
        .addMeta(X3Dpackage.meta().setContent("John Carlson").setName("translator"))
        .addMeta(X3Dpackage.meta().setContent("11 Jan 2015").setName("created"))
        .addMeta(X3Dpackage.meta().setContent("05 May 2017").setName("modified"))
        .addMeta(X3Dpackage.meta().setContent("12 extrusions to test prototype expander").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("https://coderextreme.net/x3d/qq3.x3d").setName("identifier"))
        .addMeta(X3Dpackage.meta().setContent("manual").setName("generator")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.ProtoDeclare().setName("Process")
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Group()
              # left 

              .addChildren(X3Dpackage.Transform().setScale([0.5,0.5,0.5])
                .addChildren(X3Dpackage.Shape().setDEF("ShapeLeftDown")
                  .setAppearance(X3Dpackage.Appearance()
                    .setMaterial(X3Dpackage.Material().setDiffuseColor([0.7,1,0])))
                  .setGeometry(X3Dpackage.Extrusion(setSpine = [-2.5,0,0,-1.5,0,0], setCreaseAngle = 0.785, setCrossSection = [1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00]))))
              # right 

              .addChildren(X3Dpackage.Transform().setScale([0.5,0.5,0.5])
                .addChildren(X3Dpackage.Shape().setDEF("ShapeUpRight")
                  .setAppearance(X3Dpackage.Appearance()
                    .setMaterial(X3Dpackage.Material().setDiffuseColor([0,0.7,1])))
                  .setGeometry(X3Dpackage.Extrusion(setSpine = [1.5,0,0,2.5,0,0], setCreaseAngle = 0.785, setCrossSection = [1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00]))))
              # up 

              .addChildren(X3Dpackage.Transform().setScale([0.5,0.5,0.5])
                .addChildren(X3Dpackage.Shape().setUSE("ShapeUpRight")))
              # down 

              .addChildren(X3Dpackage.Transform().setScale([0.5,0.5,0.5])
                .addChildren(X3Dpackage.Shape().setUSE("ShapeLeftDown"))))))
        .addChildren(X3Dpackage.Viewpoint().setDescription("Process pipes").setOrientation([1,0,0,-0.4]).setPosition([0,5,12]))
        .addChildren(X3Dpackage.Transform().setTranslation([0,-2.5,0])
          .addChildren(X3Dpackage.ProtoInstance().setName("Process")))
        .addChildren(X3Dpackage.Transform().setTranslation([0,0,0])
          .addChildren(X3Dpackage.ProtoInstance().setName("Process")))
        .addChildren(X3Dpackage.Transform().setTranslation([0,2.5,0])
          .addChildren(X3Dpackage.ProtoInstance().setName("Process")))))

