import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setContent("ArchPrototype.x3d").setName("title"))
        .addMeta(X3Dpackage.meta().setContent("Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("Possibility to create shapes related to arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information.").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("Michele Foti, Don Brutzman").setName("creator"))
        .addMeta(X3Dpackage.meta().setContent("15 December 2014").setName("created"))
        .addMeta(X3Dpackage.meta().setContent("27 November 2015").setName("modified"))
        .addMeta(X3Dpackage.meta().setContent("ArchModelingDiagrams.pdf").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("https://en.wikipedia.org/wiki/Arch").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://X3dGraphics.com/examples/X3dForAdvancedModeling/Buildings/ArchPrototype.x3d").setName("identifier"))
        .addMeta(X3Dpackage.meta().setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("../license.html").setName("license")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.ProtoDeclare().setAppinfo("Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. - Possibility to create shapes related to an arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.js.").setName("ArchPrototype")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            # COLOR OF ARCH 

            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("color of arch").setName("diffuseColor").setType("SFColor").setValue("0.2 0.8 0.8"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("color of arch").setName("emissiveColor").setType("SFColor").setValue("0.2 0.8 0.8"))
            # INPUT PARAMETERS 

            # General parameters: measures in meters 

            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("clearSpanWidth: clearSpanWidth must be double of riseHeight to obtain an half circumference").setName("clearSpanWidth").setType("SFFloat").setValue("4"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("riseHeight: riseHeight must be half of clearSpanWidth to obtain an half circumference").setName("riseHeight").setType("SFFloat").setValue("2"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("depth").setName("depth").setType("SFFloat").setValue("3"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("topAbutmentHeight:topAbutmentHeight=0 means no topAbutment").setName("topAbutmentHeight").setType("SFFloat").setValue("0.5"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("pierWidth:pierWidtht=0 means no pierWidth").setName("pierWidth").setType("SFFloat").setValue("0.5"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("pierHeight: pierHeight=0 means no pierHeight").setName("pierHeight").setType("SFFloat").setValue("1"))
            # Parameters to create to create shapes related to arch: put true to apply 

            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("archHalf: can modify also clearSpanWidth, riseHeight, depth, pierWidth, pierHeight, topAbutmentHeight, archHalfExtensionWidth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalf width").setName("archHalf").setType("SFBool").setValue("false"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("archHalfExtensionWidth: measure in meters, use only if archHalf=true, it is the width of the etension of the abutment of the archHalf. See the reference file ArchModelingDiagrams.pdf to find further information.").setName("archHalfExtensionWidth").setType("SFFloat").setValue("0"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("onlyIntrados: note it is a flat curved surface, can modify also clearSpanWidth, riseHeight, depth at purpose, if needed apply archHalf=true.").setName("onlyIntrados").setType("SFBool").setValue("false"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("archFilled: note it is an half cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose.").setName("archFilled").setType("SFBool").setValue("false"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("archHalfFilled: note it is a quarter cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalfFilled width.").setName("archHalfFilled").setType("SFBool").setValue("false"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("lintel: no arc is rendered, but a lintel: topAbutmentHeight on pierHeight, total height is pierHeight + topAbutmentHeight, if needed apply archHalf=true.").setName("lintel").setType("SFBool").setValue("false")))
          .setProtoBody(X3Dpackage.ProtoBody()
            # First node determines node type of this prototype 

            # IndexedFaceset creates arch 

            .addChildren(X3Dpackage.Transform().setDEF("ArchTransform")
              .addChildren(X3Dpackage.Shape().setDEF("Arch")
                # note that convex='false' (meaning concave geometry) is crucial for this IFS of a geometric chord to render properly 

                .setGeometry(X3Dpackage.IndexedFaceSet(setConvex = False, setCreaseAngle = 0, setSolid = False).setDEF("ArchIndex")
                  .setCoord(X3Dpackage.Coordinate().setDEF("ArchChord")))
                .setAppearance(X3Dpackage.Appearance()
                  .setMaterial(X3Dpackage.Material().setDEF("MaterialNode")
                    .setIS(X3Dpackage.IS()
                      .addConnect(X3Dpackage.connect().setNodeField("emissiveColor").setProtoField("emissiveColor"))
                      .addConnect(X3Dpackage.connect().setNodeField("diffuseColor").setProtoField("diffuseColor")))))))
            # Subsequent nodes do not render, but still must be a valid X3D subgraph 

            # This embedded Script provides the X3D author with additional visibility and control over prototype inputs and outputs 

            .addChildren(X3Dpackage.Script().setDEF("ArchPrototypeScript").setUrl(["../node/ArchPrototypeScript.js"])
              # INPUT PARAMETERS 

              # General parameters 

              # Parameters to create to create shapes related to arch: put true to apply 

              # OUTPUT PARAMETERS 

              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for clearSpanWidth parameter").setName("clearSpanWidth").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for riseHeight parameter").setName("riseHeight").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for depth parameter").setName("depth").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for topAbutmentHeight parameter").setName("topAbutmentHeight").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for pierWidth parameter").setName("pierWidth").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for pierHeight parameter").setName("pierHeight").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for archHalf parameter").setName("archHalf").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for archHalfExtensionWidth parameter").setName("archHalfExtensionWidth").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for onlyIntrados parameter").setName("onlyIntrados").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for archFilled parameter").setName("archFilled").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for archHalfFilled parameter").setName("archHalfFilled").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("user or default input for lintel parameter").setName("lintel").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("computedScale: modify scale field - NOTE it is not used to modify the whole arch, but to modify clearSpanWidth, riseHeight, depth. It does not affect topAbutmentHeight, pierWidth, pierHeight, archHalfExtensionWidth").setName("computedScale").setType("SFVec3f"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("send computed points to the Coordinate node").setName("pointOut").setType("MFVec3f"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("send computed indices to the IndexedFaceSet node").setName("indexOut").setType("MFInt32"))
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("clearSpanWidth").setProtoField("clearSpanWidth"))
                .addConnect(X3Dpackage.connect().setNodeField("riseHeight").setProtoField("riseHeight"))
                .addConnect(X3Dpackage.connect().setNodeField("depth").setProtoField("depth"))
                .addConnect(X3Dpackage.connect().setNodeField("pierWidth").setProtoField("pierWidth"))
                .addConnect(X3Dpackage.connect().setNodeField("topAbutmentHeight").setProtoField("topAbutmentHeight"))
                .addConnect(X3Dpackage.connect().setNodeField("pierHeight").setProtoField("pierHeight"))
                .addConnect(X3Dpackage.connect().setNodeField("archHalf").setProtoField("archHalf"))
                .addConnect(X3Dpackage.connect().setNodeField("archHalfExtensionWidth").setProtoField("archHalfExtensionWidth"))
                .addConnect(X3Dpackage.connect().setNodeField("onlyIntrados").setProtoField("onlyIntrados"))
                .addConnect(X3Dpackage.connect().setNodeField("archFilled").setProtoField("archFilled"))
                .addConnect(X3Dpackage.connect().setNodeField("archHalfFilled").setProtoField("archHalfFilled"))
                .addConnect(X3Dpackage.connect().setNodeField("lintel").setProtoField("lintel"))))
            .addChildren(X3Dpackage.ROUTE().setFromField("computedScale").setFromNode("ArchPrototypeScript").setToField("scale").setToNode("ArchTransform"))
            .addChildren(X3Dpackage.ROUTE().setFromField("pointOut").setFromNode("ArchPrototypeScript").setToField("point").setToNode("ArchChord"))
            .addChildren(X3Dpackage.ROUTE().setFromField("indexOut").setFromNode("ArchPrototypeScript").setToField("set_coordIndex").setToNode("ArchIndex"))))
        .addChildren(X3Dpackage.ProtoInstance().setDEF("ArchInstance").setName("ArchPrototype")
          .addFieldValue(X3Dpackage.fieldValue().setName("diffuseColor").setValue("0.5 0.3 0.6"))
          .addFieldValue(X3Dpackage.fieldValue().setName("emissiveColor").setValue("0.5 0.3 0.6"))
          .addFieldValue(X3Dpackage.fieldValue().setName("clearSpanWidth").setValue("5"))
          .addFieldValue(X3Dpackage.fieldValue().setName("riseHeight").setValue("2.5"))
          .addFieldValue(X3Dpackage.fieldValue().setName("depth").setValue("2"))
          .addFieldValue(X3Dpackage.fieldValue().setName("topAbutmentHeight").setValue("0.6"))
          .addFieldValue(X3Dpackage.fieldValue().setName("pierWidth").setValue("1"))
          .addFieldValue(X3Dpackage.fieldValue().setName("pierHeight").setValue("2")))
        # Add any ROUTEs here that connect ProtoInstance to/from prior nodes in Scene (and outside of ProtoDeclare) 

        .addChildren(X3Dpackage.Inline().setDEF("CoordinateAxes").setUrl(["../data/CoordinateAxes.x3d"]))))

