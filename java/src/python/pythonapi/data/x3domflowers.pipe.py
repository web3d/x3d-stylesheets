import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("sphereflowers.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("5 or more prismatic flowers"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/sphereflowers.x3d")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.NavigationInfo().setType(["EXAMINE","ANY"]))
        .addChildren(X3Dpackage.Background().setBackUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]).setBottomUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]).setFrontUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]).setLeftUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]).setRightUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]).setTopUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]))
        .addChildren(X3Dpackage.Group()
          .addChildren(X3Dpackage.ExternProtoDeclare().setName("FlowerProto").setUrl(["../data/flowerproto.json#FlowerProto"])
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("vertex").setType("MFString"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("fragment").setType("MFString")))
          .addChildren(X3Dpackage.ProtoDeclare().setName("flower")
            .setProtoBody(X3Dpackage.ProtoBody()
              .addChildren(X3Dpackage.Group()
                .addChildren(X3Dpackage.ProtoInstance().setName("FlowerProto")
                  .addFieldValue(X3Dpackage.fieldValue().setName("vertex").setValue("\"../shaders/x3dom_flowers_chromatic.vs\""))
                  .addFieldValue(X3Dpackage.fieldValue().setName("fragment").setValue("\"../shaders/common.fs\""))))))
          .addChildren(X3Dpackage.ProtoInstance().setName("flower"))
          .addChildren(X3Dpackage.ProtoInstance().setName("flower"))
          .addChildren(X3Dpackage.ProtoInstance().setName("flower"))
          .addChildren(X3Dpackage.ProtoInstance().setName("flower"))
          .addChildren(X3Dpackage.ProtoInstance().setName("flower"))
          .addChildren(X3Dpackage.ProtoInstance().setName("flower")))))

