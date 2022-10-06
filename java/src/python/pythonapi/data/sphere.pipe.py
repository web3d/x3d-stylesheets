import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Interchange").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("sphere.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("manual"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/sphere.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("a sphere")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Group()
          .addChildren(X3Dpackage.Shape()
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([1,1,1])))
            .setGeometry(X3Dpackage.Sphere(setRadius = 1))))))

