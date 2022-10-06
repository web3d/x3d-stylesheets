import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setContent("TextSpecialCharacters.x3d").setName("title"))
        .addMeta(X3Dpackage.meta().setContent("Text node demonstration of quotation, apostrophe, ampersand and backslash characters using X3D MFString escaping for XML character entities").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("Don Brutzman").setName("creator"))
        .addMeta(X3Dpackage.meta().setContent("12 July 2008").setName("created"))
        .addMeta(X3Dpackage.meta().setContent("2 April 2017").setName("modified"))
        .addMeta(X3Dpackage.meta().setContent("Character entity references in HTML 4").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://www.w3.org/TR/REC-html40/sgml/entities.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("Copyright (c) Don Brutzman and Leonard Daly, 2008").setName("rights"))
        .addMeta(X3Dpackage.meta().setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter02GeometryPrimitives/TextSpecialCharacters.x3d").setName("identifier"))
        .addMeta(X3Dpackage.meta().setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("../license.html").setName("license")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Background().setSkyColor([1,1,1]))
        .addChildren(X3Dpackage.Viewpoint().setDescription("Default View").setPosition([0,0,15]))
        .addChildren(X3Dpackage.Shape()
          # Empty string \"\" means to skip a line 

          # The ampersand escape characters are based on XML rules 

          # apostrophe ' is &apos; and needs to be escaped in single-quote delimiters used for string='value' attribute 

          # ampersand & is &amp; and needs to be escaped 

          # quotation \" is &quot; and isn't needed if single-quote delimiters used for string='value' attribute 

          # quotation \" can be used within an X3D string if escaped with backslash \\ as \\\" 

          # backslash \\ is used as escape character for \" (and itself) in X3D 

          # character entities are listed in HTML specification and are good for any XML 

          .setGeometry(X3Dpackage.Text().setDEF("DefaultText").setString(["Character entity substitutions:","empty string \"\" skips a line:","","apostrophe  '  is &apos;","ampersand & is &amp;","quote mark  \"  is &quot;","backslash \\\\ is X3D escape character","double backslash \\\\\\\\ is X3D backslash \\\\ character","Pi Π is &#928; XML character entity"])
            .setFontStyle(X3Dpackage.FontStyle(setJustify = ["MIDDLE","MIDDLE"]).setDEF("CenteredFontStyle")))
          .setAppearance(X3Dpackage.Appearance()
            .setMaterial(X3Dpackage.Material().setDEF("DefaultMaterial").setDiffuseColor([0.2,0.2,0.2]))))))

