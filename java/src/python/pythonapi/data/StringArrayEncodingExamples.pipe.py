import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setContent("StringArrayEncodingExamples.x3d").setName("title"))
        .addMeta(X3Dpackage.meta().setContent("Demonstrate simple X3D MFString (string array) encoding.").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("27 May 2017").setName("created"))
        .addMeta(X3Dpackage.meta().setContent("27 May 2017").setName("modified"))
        .addMeta(X3Dpackage.meta().setContent("Don Brutzman").setName("creator"))
        .addMeta(X3Dpackage.meta().setContent("X3dHeaderPrototypeSyntaxExamples.x3d").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("X3D encodings, ISO/IEC 19775-1, Part 1: Architecture and base components, 5 Field type reference, 5.3.14 SFString and MFString").setName("specificationSection"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/documents/specifications/19775-1/V3.3/Part01/fieldsDef.html#SFStringAndMFString").setName("specificationUrl"))
        .addMeta(X3Dpackage.meta().setContent("X3D encodings, ISO/IEC 19776-1.3, Part 1: XML encoding, 5.3.14 SFString and MFString").setName("specificationSection"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/documents/specifications/19776-1/V3.3/Part01/EncodingOfFields.html#SFString").setName("specificationUrl"))
        .addMeta(X3Dpackage.meta().setContent("X3D encodings, ISO/IEC 19776-2 v3.3, Part 2: Classic VRML encoding, 5.15 SFString and MFString").setName("specificationSection"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/documents/specifications/19776-2/V3.3/Part02/EncodingOfFields.html#SFString").setName("specificationUrl"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamples.x3d").setName("identifier"))
        .addMeta(X3Dpackage.meta().setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("../license.html").setName("license")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Viewpoint().setDEF("EntryView").setDescription("Hello MFString syntax"))
        .addChildren(X3Dpackage.Background().setSkyColor([0.6,1,0.8]))
        .addChildren(X3Dpackage.Shape()
          .setGeometry(X3Dpackage.Text().setString(["One, Two, Three","","He said, \"Immel did it!\""])
            # alternative XML encoding: Text string='\"One, Two, Three\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 

            # alternative Java source: .setString(new String [] {\"One, Two, Three\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 

            .setFontStyle(X3Dpackage.FontStyle(setJustify = ["MIDDLE","MIDDLE"], setStyle = "BOLD")))
          .setAppearance(X3Dpackage.Appearance()
            .setMaterial(X3Dpackage.Material().setDiffuseColor([0.6,0.4,0.2]))))))

