import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("CoordinateAxis.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("Unknown, see X3D Resources Archives"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("manual"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/CoordinateAxis.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("a box")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Collision().setDEF("DoNotCollideWithVisualizationWidget").setEnabled(True)
          # Invoke CoordinateAxes in other scenes as an Inline child inside a scaling Transform node, at the topmost level of the scene graph. 

          # This NavigationInfo allows examine mode and will be overridden by any parent scene. 

          # Each arrow goes from +1m to -1m to allow linear scaling to fit a scene 

          # Note each label rotates about the scene's vertical Y axis for consistency, enabling local orientation by user 

          .addChildren(X3Dpackage.Group()
            # Vertical Y arrow and label 

            .addChildren(X3Dpackage.Group().setDEF("ArrowGreen")
              .addChildren(X3Dpackage.Shape()
                .setGeometry(X3Dpackage.Cylinder(setRadius = .025).setDEF("ArrowCylinder").setTop(False))
                .setAppearance(X3Dpackage.Appearance().setDEF("Green")
                  .setMaterial(X3Dpackage.Material().setDiffuseColor([.1,.6,.1]).setEmissiveColor([.05,.2,.05]))))
              .addChildren(X3Dpackage.Transform().setTranslation([0,1,0])
                .addChildren(X3Dpackage.Shape()
                  .setGeometry(X3Dpackage.Cone(setBottomRadius = .05, setHeight = .1).setDEF("ArrowCone"))
                  .setAppearance(X3Dpackage.Appearance().setUSE("Green")))))
            .addChildren(X3Dpackage.Transform().setTranslation([0,1.08,0])
              .addChildren(X3Dpackage.Billboard()
                .addChildren(X3Dpackage.Shape()
                  .setAppearance(X3Dpackage.Appearance().setDEF("LABEL_APPEARANCE")
                    .setMaterial(X3Dpackage.Material().setDiffuseColor([1,1,.3]).setEmissiveColor([.33,.33,.1])))
                  .setGeometry(X3Dpackage.Text().setString(["Y"])
                    .setFontStyle(X3Dpackage.FontStyle(setFamily = ["SANS"], setJustify = ["MIDDLE","MIDDLE"], setSize = .2).setDEF("LABEL_FONT")))))))
          .addChildren(X3Dpackage.Transform().setRotation([0,0,1,-1.57079])
            # Horizontal X arrow and label 

            .addChildren(X3Dpackage.Group()
              .addChildren(X3Dpackage.Group().setDEF("ArrowRed")
                .addChildren(X3Dpackage.Shape()
                  .setGeometry(X3Dpackage.Cylinder().setUSE("ArrowCylinder"))
                  .setAppearance(X3Dpackage.Appearance().setDEF("Red")
                    .setMaterial(X3Dpackage.Material().setDiffuseColor([.7,.1,.1]).setEmissiveColor([.33,0,0]))))
                .addChildren(X3Dpackage.Transform().setTranslation([0,1,0])
                  .addChildren(X3Dpackage.Shape()
                    .setGeometry(X3Dpackage.Cone().setUSE("ArrowCone"))
                    .setAppearance(X3Dpackage.Appearance().setUSE("Red")))))
              .addChildren(X3Dpackage.Transform().setRotation([0,0,1,1.57079]).setTranslation([.072,1.1,0])
                # note label rotated back to original coordinate frame 

                .addChildren(X3Dpackage.Billboard()
                  .addChildren(X3Dpackage.Shape()
                    .setAppearance(X3Dpackage.Appearance().setUSE("LABEL_APPEARANCE"))
                    .setGeometry(X3Dpackage.Text().setString(["X"])
                      .setFontStyle(X3Dpackage.FontStyle().setUSE("LABEL_FONT"))))))))
          .addChildren(X3Dpackage.Transform().setRotation([1,0,0,1.57079])
            # Perpendicular Z arrow and label, note right-hand rule 

            .addChildren(X3Dpackage.Group()
              .addChildren(X3Dpackage.Group().setDEF("ArrowBlue")
                .addChildren(X3Dpackage.Shape()
                  .setGeometry(X3Dpackage.Cylinder().setUSE("ArrowCylinder"))
                  .setAppearance(X3Dpackage.Appearance().setDEF("Blue")
                    .setMaterial(X3Dpackage.Material().setDiffuseColor([.3,.3,1]).setEmissiveColor([.1,.1,.33]))))
                .addChildren(X3Dpackage.Transform().setTranslation([0,1,0])
                  .addChildren(X3Dpackage.Shape()
                    .setGeometry(X3Dpackage.Cone().setUSE("ArrowCone"))
                    .setAppearance(X3Dpackage.Appearance().setUSE("Blue")))))
              .addChildren(X3Dpackage.Transform().setRotation([1,0,0,-1.57079]).setTranslation([0,1.1,.072])
                # note label rotated back to original coordinate frame 

                .addChildren(X3Dpackage.Billboard()
                  .addChildren(X3Dpackage.Shape()
                    .setAppearance(X3Dpackage.Appearance().setUSE("LABEL_APPEARANCE"))
                    .setGeometry(X3Dpackage.Text().setString(["Z"])
                      .setFontStyle(X3Dpackage.FontStyle().setUSE("LABEL_FONT")))))))))))

