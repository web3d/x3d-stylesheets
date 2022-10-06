import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addComponent(X3Dpackage.component().setName("Shaders").setLevel(1))
        .addComponent(X3Dpackage.component().setName("CubeMapTexturing").setLevel(1))
        .addMeta(X3Dpackage.meta().setName("title").setContent("mirro2.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("manual"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/mirro2.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("a mirrored sphere")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Viewpoint().setPosition([0,5,100]).setDescription("Switch background and images texture"))
        .addChildren(X3Dpackage.Background().setDEF("cube").setLeftUrl(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]).setRightUrl(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]).setFrontUrl(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]).setBackUrl(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]).setTopUrl(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"]).setBottomUrl(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]))
        .addChildren(X3Dpackage.Transform()
          .addChildren(X3Dpackage.Shape()
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([.7,.7,.7]).setSpecularColor([.5,.5,.5]))
              .setTexture(X3Dpackage.ComposedCubeMapTexture()
                .setBack(X3Dpackage.ImageTexture().setDEF("backShader").setUrl(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]))
                .setBottom(X3Dpackage.ImageTexture().setDEF("bottomShader").setUrl(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]))
                .setFront(X3Dpackage.ImageTexture().setDEF("frontShader").setUrl(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]))
                .setLeft(X3Dpackage.ImageTexture().setDEF("leftShader").setUrl(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]))
                .setRight(X3Dpackage.ImageTexture().setDEF("rightShader").setUrl(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]))
                .setTop(X3Dpackage.ImageTexture().setDEF("topShader").setUrl(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"])))
              .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL").setDEF("cobweb")
                #http://hypertextbook.com/facts/2005/JustinChe.shtml

                .addField(X3Dpackage.field().setName("chromaticDispertion").setAccessType("inputOutput").setType("SFVec3f").setValue("0.98 1 1.033"))
                .addField(X3Dpackage.field().setName("cube").setAccessType("inputOutput").setType("SFInt32").setValue("0"))
                .addField(X3Dpackage.field().setName("bias").setAccessType("inputOutput").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("scale").setAccessType("inputOutput").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("power").setAccessType("inputOutput").setType("SFFloat").setValue("2"))
                .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]).setType("VERTEX"))
                .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"]).setType("FRAGMENT")))
              .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL").setDEF("x3dom")
                #http://hypertextbook.com/facts/2005/JustinChe.shtml

                .addField(X3Dpackage.field().setName("chromaticDispertion").setAccessType("inputOutput").setType("SFVec3f").setValue("0.98 1 1.033"))
                .addField(X3Dpackage.field().setName("cube").setAccessType("inputOutput").setType("SFInt32").setValue("0"))
                .addField(X3Dpackage.field().setName("bias").setAccessType("inputOutput").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("scale").setAccessType("inputOutput").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("power").setAccessType("inputOutput").setType("SFFloat").setValue("2"))
                .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]).setType("VERTEX"))
                .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"]).setType("FRAGMENT"))))
            .setGeometry(X3Dpackage.Sphere(setRadius = 30)))
          .addChildren(X3Dpackage.Script(setDirectOutput = True).setDEF("UrlSelector")
            .addField(X3Dpackage.field().setName("frontUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\""))
            .addField(X3Dpackage.field().setName("backUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\""))
            .addField(X3Dpackage.field().setName("leftUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\""))
            .addField(X3Dpackage.field().setName("rightUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\""))
            .addField(X3Dpackage.field().setName("topUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\""))
            .addField(X3Dpackage.field().setName("bottomUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\""))
            .addField(X3Dpackage.field().setName("front_changed").setType("MFString").setAccessType("outputOnly"))
            .addField(X3Dpackage.field().setName("back_changed").setType("MFString").setAccessType("outputOnly"))
            .addField(X3Dpackage.field().setName("left_changed").setType("MFString").setAccessType("outputOnly"))
            .addField(X3Dpackage.field().setName("right_changed").setType("MFString").setAccessType("outputOnly"))
            .addField(X3Dpackage.field().setName("top_changed").setType("MFString").setAccessType("outputOnly"))
            .addField(X3Dpackage.field().setName("bottom_changed").setType("MFString").setAccessType("outputOnly"))
            .addField(X3Dpackage.field().setName("set_fraction").setType("SFFloat").setAccessType("inputOnly"))
            .addField(X3Dpackage.field().setName("old").setType("SFInt32").setAccessType("inputOutput").setValue("-1")).setSourceCode('''\n"+
"ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"	    var side = Math.floor(f*frontUrls.length);\n"+
"	    if (side > frontUrls.length-1) {\n"+
"	    	side = 0;\n"+
"	    }\n"+
"	    if (side != old) {\n"+
"	    	    // Browser.print(f+\" \"+side);\n"+
"	    	    old = side;\n"+
"		    front_changed[0] = frontUrls[side];\n"+
"		    back_changed[0] = backUrls[side];\n"+
"		    left_changed[0] = leftUrls[side];\n"+
"		    right_changed[0] = rightUrls[side];\n"+
"		    top_changed[0] = topUrls[side];\n"+
"		    bottom_changed[0] = bottomUrls[side];\n"+
"            }\n"+
"        }\n"+
"''')
)
          .addChildren(X3Dpackage.TimeSensor().setDEF("Clock").setCycleInterval(45).setLoop(True))
          .addChildren(X3Dpackage.ROUTE().setFromNode("Clock").setFromField("fraction_changed").setToNode("UrlSelector").setToField("set_fraction"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("front_changed").setToNode("cube").setToField("frontUrl"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("back_changed").setToNode("cube").setToField("backUrl"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("left_changed").setToNode("cube").setToField("leftUrl"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("right_changed").setToNode("cube").setToField("rightUrl"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("top_changed").setToNode("cube").setToField("topUrl"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("bottom_changed").setToNode("cube").setToField("bottomUrl"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("front_changed").setToNode("frontShader").setToField("url"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("back_changed").setToNode("backShader").setToField("url"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("left_changed").setToNode("leftShader").setToField("url"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("right_changed").setToNode("rightShader").setToField("url"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("top_changed").setToNode("topShader").setToField("url"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("UrlSelector").setFromField("bottom_changed").setToNode("bottomShader").setToField("url")))))

