import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Interchange").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("template.json"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("http://coderextreme.net/X3DJSONLD/template.json"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("Template for an Indexed Face Set"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("created").setContent("4 April 2017")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Group()
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.IndexedFaceSet(setCreaseAngle = 1.57, setCoordIndex = [0,0,1,-1,0,1,1,-1,2,2,3,3,-1,0,3,3,0,-1,0,3,2,1,-1,1,2,2,1,-1,1,2,3,0,-1], setNormalIndex = [0,-1,0,-1,1,-1,2,-1,3,-1,4,-1,5,-1], setNormalPerVertex = False, setColorIndex = [0,0,0,-1,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1]).setDEF("IndexedFaceSet")
              .setCoord(X3Dpackage.Coordinate().setPoint([0,0,1,0,1,1,1,1,1,1,0,1]))
              .setNormal(X3Dpackage.Normal().setVector([1,0,0,-1,0,0,0,1,0,0,0,-1,0,-1,0,0,0,1]))
              .setColor(X3Dpackage.Color().setColor([0,1,0])))))))

