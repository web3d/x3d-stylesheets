import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John W Carlson"))
        .addMeta(X3Dpackage.meta().setName("created").setContent("December 13 2015"))
        .addMeta(X3Dpackage.meta().setName("title").setContent("text.x3d"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/text.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("test \\n text"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Transform()
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Text().setString(["Node\"\"\""])
              .setFontStyle(X3Dpackage.FontStyle()))
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material())))
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Text().setString(["Node2","\\\\","\\\\\\\\","Node2"])
              .setFontStyle(X3Dpackage.FontStyle()))
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material())))
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Text().setString(["Node3 \\\\\\\\ \\\\ ","Node3\"\"\""])
              .setFontStyle(X3Dpackage.FontStyle()))
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material())))
          .addChildren(X3Dpackage.Script()
            .addField(X3Dpackage.field().setName("frontUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"rnl_front.png\" \"uffizi_front.png\"")).setSourceCode('''ecmascript:\n"+
"			    var me = '\"1\" \"\\\"2\" \"\\n3\"';\n"+
"			    ''')
))))

