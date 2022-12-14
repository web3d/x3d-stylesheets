import x3dpsail as x3d


X3D0 = (x3d.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(x3d.head()
        .addMeta(x3d.meta().setName("title").setContent("abox.x3d"))
        .addMeta(x3d.meta().setName("creator").setContent("John Carlson"))
        .addMeta(x3d.meta().setName("generator").setContent("manual"))
        .addMeta(x3d.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/abox.x3d"))
        .addMeta(x3d.meta().setName("description").setContent("a box")))
      .setScene(x3d.Scene()
        .addChild(x3d.ProtoDeclare().setName("anyShape")
          .setProtoInterface(x3d.ProtoInterface()
            .addField(x3d.field().setName("myShape").setAccessType("inputOutput").setType("MFNode")
              .addChild(x3d.Shape()
                .setGeometry(x3d.Sphere()))))
          .setProtoBody(x3d.ProtoBody()
            .addChild(x3d.Transform()
              .setIS(x3d.IS()
                .addConnect(x3d.connect().setNodeField("children").setProtoField("myShape"))))))
        .addChild(x3d.ProtoDeclare().setName("one")
          .setProtoInterface(x3d.ProtoInterface()
            .addField(x3d.field().setName("myShape").setAccessType("inputOutput").setType("MFNode")
              .addChild(x3d.Shape()
                .setGeometry(x3d.Cylinder()))))
          .setProtoBody(x3d.ProtoBody()
            .addChild(x3d.Transform()
              .addChild(x3d.ProtoInstance().setName("anyShape")
                .setIS(x3d.IS()
                  .addConnect(x3d.connect().setNodeField("myShape").setProtoField("myShape")))))))
        .addChild(x3d.ProtoInstance().setName("one")
          .addFieldValue(x3d.fieldValue().setName("myShape")
            .addChild(x3d.Shape()
              .setGeometry(x3d.Box().setSize([140,140,140])))))))

X3D0.toFileX3D("abox_RoundTrip.x3d")
