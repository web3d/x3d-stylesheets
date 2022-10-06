import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addComponent(X3Dpackage.component().setName("Shaders").setLevel(1))
        .addComponent(X3Dpackage.component().setName("CubeMapTexturing").setLevel(1))
        .addMeta(X3Dpackage.meta().setName("title").setContent("flowers7.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("manual"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/flowers7.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("a flower")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.NavigationInfo().setType(["EXAMINE","ANY"]))
        # Images courtesy of Paul Debevec's Light Probe Image Gallery 

        .addChildren(X3Dpackage.Background().setDEF("background").setBackUrl(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"]).setBottomUrl(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"]).setFrontUrl(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"]).setLeftUrl(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"]).setRightUrl(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"]).setTopUrl(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"]))
        .addChildren(X3Dpackage.Viewpoint().setPosition([0,0,40]).setDescription("Transparent rose"))
        .addChildren(X3Dpackage.Transform().setDEF("Rose01")
          .addChildren(X3Dpackage.Shape()
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([.7,.7,.7]).setSpecularColor([.5,.5,.5]))
              .setTexture(X3Dpackage.ComposedCubeMapTexture().setDEF("texture")
                .setBack(X3Dpackage.ImageTexture().setDEF("backShader").setUrl(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"]))
                .setBottom(X3Dpackage.ImageTexture().setDEF("bottomShader").setUrl(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"]))
                .setFront(X3Dpackage.ImageTexture().setDEF("frontShader").setUrl(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"]))
                .setLeft(X3Dpackage.ImageTexture().setDEF("leftShader").setUrl(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"]))
                .setRight(X3Dpackage.ImageTexture().setDEF("rightShader").setUrl(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"]))
                .setTop(X3Dpackage.ImageTexture().setDEF("topShader").setUrl(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"])))
              .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL").setDEF("x3dom")
                .addField(X3Dpackage.field().setName("cube").setType("SFInt32").setAccessType("inputOutput").setValue("0"))
                #field name='cube' type='SFNode' accessType=\"inputOutput\">
#			  <ComposedCubeMapTexture USE=\"texture\"/>
#		  </field

                .addField(X3Dpackage.field().setName("chromaticDispertion").setAccessType("initializeOnly").setType("SFVec3f").setValue("0.98 1.0 1.033"))
                .addField(X3Dpackage.field().setName("bias").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                .addField(X3Dpackage.field().setName("scale").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                .addField(X3Dpackage.field().setName("power").setType("SFFloat").setAccessType("inputOutput").setValue("2"))
                .addField(X3Dpackage.field().setName("a").setType("SFFloat").setAccessType("inputOutput").setValue("10"))
                .addField(X3Dpackage.field().setName("b").setType("SFFloat").setAccessType("inputOutput").setValue("1"))
                .addField(X3Dpackage.field().setName("c").setType("SFFloat").setAccessType("inputOutput").setValue("20"))
                .addField(X3Dpackage.field().setName("d").setType("SFFloat").setAccessType("inputOutput").setValue("20"))
                .addField(X3Dpackage.field().setName("tdelta").setType("SFFloat").setAccessType("inputOutput").setValue("0"))
                .addField(X3Dpackage.field().setName("pdelta").setType("SFFloat").setAccessType("inputOutput").setValue("0"))
                .setParts(X3Dpackage.ShaderPart().setUrl(["../shaders/x3dom_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom_flowers_chromatic.vs"]).setType("VERTEX"))
                .setParts(X3Dpackage.ShaderPart().setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"]).setType("FRAGMENT")))
              .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL").setDEF("cobweb")
                .addField(X3Dpackage.field().setName("cube").setType("SFNode").setAccessType("inputOutput")
                  .addChildren(X3Dpackage.ComposedCubeMapTexture().setUSE("texture")))
                .addField(X3Dpackage.field().setName("chromaticDispertion").setAccessType("initializeOnly").setType("SFVec3f").setValue("0.98 1.0 1.033"))
                .addField(X3Dpackage.field().setName("bias").setType("SFFloat").setAccessType("inputOnly").setValue("0.5"))
                .addField(X3Dpackage.field().setName("scale").setType("SFFloat").setAccessType("inputOnly").setValue("0.5"))
                .addField(X3Dpackage.field().setName("power").setType("SFFloat").setAccessType("inputOnly").setValue("2"))
                .addField(X3Dpackage.field().setName("a").setType("SFFloat").setAccessType("inputOnly").setValue("10"))
                .addField(X3Dpackage.field().setName("b").setType("SFFloat").setAccessType("inputOnly").setValue("1"))
                .addField(X3Dpackage.field().setName("c").setType("SFFloat").setAccessType("inputOnly").setValue("20"))
                .addField(X3Dpackage.field().setName("d").setType("SFFloat").setAccessType("inputOnly").setValue("20"))
                .addField(X3Dpackage.field().setName("tdelta").setType("SFFloat").setAccessType("inputOnly").setValue("0"))
                .addField(X3Dpackage.field().setName("pdelta").setType("SFFloat").setAccessType("inputOnly").setValue("0"))
                .setParts(X3Dpackage.ShaderPart().setUrl(["../shaders/cobweb_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb_flowers_chromatic.vs"]).setType("VERTEX"))
                .setParts(X3Dpackage.ShaderPart().setUrl(["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"]).setType("FRAGMENT"))))
            .setGeometry(X3Dpackage.Sphere(setSolid = False, setRadius = 1))))
        .addChildren(X3Dpackage.Script(setDirectOutput = True).setDEF("UrlSelector")
          .addField(X3Dpackage.field().setName("frontUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\""))
          .addField(X3Dpackage.field().setName("backUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\""))
          .addField(X3Dpackage.field().setName("leftUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\""))
          .addField(X3Dpackage.field().setName("rightUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\""))
          .addField(X3Dpackage.field().setName("topUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\""))
          .addField(X3Dpackage.field().setName("bottomUrls").setType("MFString").setAccessType("initializeOnly").setValue("\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\""))
          .addField(X3Dpackage.field().setName("front").setType("MFString").setAccessType("inputOutput"))
          .addField(X3Dpackage.field().setName("back").setType("MFString").setAccessType("inputOutput"))
          .addField(X3Dpackage.field().setName("left").setType("MFString").setAccessType("inputOutput"))
          .addField(X3Dpackage.field().setName("right").setType("MFString").setAccessType("inputOutput"))
          .addField(X3Dpackage.field().setName("top").setType("MFString").setAccessType("inputOutput"))
          .addField(X3Dpackage.field().setName("bottom").setType("MFString").setAccessType("inputOutput"))
          .addField(X3Dpackage.field().setName("set_fraction").setType("SFFloat").setAccessType("inputOnly"))
          .addField(X3Dpackage.field().setName("old").setType("SFInt32").setAccessType("inputOutput").setValue("-1")).setSourceCode('''\n"+
"ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"            var side = Math.floor(f*frontUrls.length);\n"+
"            if (side > frontUrls.length-1) {\n"+
"                side = 0;\n"+
"            }\n"+
"            if (side != old) {\n"+
"                    old = side;\n"+
"                    front[0] = frontUrls[side];\n"+
"                    back[0] = backUrls[side];\n"+
"                    left[0] = leftUrls[side];\n"+
"                    right[0] = rightUrls[side];\n"+
"                    top[0] = topUrls[side];\n"+
"                    bottom[0] = bottomUrls[side];\n"+
"            }\n"+
"        }\n"+
"''')
)
        #
#            <TimeSensor DEF=\"Clock\" cycleInterval=\"45\" loop='true'/>
#            <ROUTE fromNode='Clock' fromField='fraction_changed' toNode='UrlSelector' toField='set_fraction'/>
#            <ROUTE fromNode='UrlSelector' fromField='front' toNode='background' toField='frontUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='back' toNode='background' toField='backUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='left' toNode='background' toField='leftUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='right' toNode='background' toField='rightUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='top' toNode='background' toField='topUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='bottom' toNode='background' toField='bottomUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='front' toNode='frontShader' toField='url'/>
#            <ROUTE fromNode='UrlSelector' fromField='back' toNode='backShader' toField='url'/>
#            <ROUTE fromNode='UrlSelector' fromField='left' toNode='leftShader' toField='url'/>
#            <ROUTE fromNode='UrlSelector' fromField='right' toNode='rightShader' toField='url'/>
#            <ROUTE fromNode='UrlSelector' fromField='top' toNode='topShader' toField='url'/>
#            <ROUTE fromNode='UrlSelector' fromField='bottom' toNode='bottomShader' toField='url'/>
#	    

        .addChildren(X3Dpackage.Script(setDirectOutput = True).setDEF("Animate")
          .addField(X3Dpackage.field().setName("set_fraction").setType("SFFloat").setAccessType("inputOnly"))
          .addField(X3Dpackage.field().setName("a").setType("SFFloat").setAccessType("inputOutput").setValue("10"))
          .addField(X3Dpackage.field().setName("b").setType("SFFloat").setAccessType("inputOutput").setValue("1"))
          .addField(X3Dpackage.field().setName("c").setType("SFFloat").setAccessType("inputOutput").setValue("20"))
          .addField(X3Dpackage.field().setName("d").setType("SFFloat").setAccessType("inputOutput").setValue("20"))
          .addField(X3Dpackage.field().setName("tdelta").setType("SFFloat").setAccessType("inputOutput").setValue("0"))
          .addField(X3Dpackage.field().setName("pdelta").setType("SFFloat").setAccessType("inputOutput").setValue("0")).setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function set_fraction() {\n"+
"	var choice = Math.floor(Math.random() * 4);\n"+
"	if (choice == 0) {\n"+
"		a = a + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 1) {\n"+
"		b = b + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 2) {\n"+
"		c = c + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 3) {\n"+
"		d = d + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	}\n"+
"	tdelta = tdelta + 0.5;\n"+
"	pdelta = pdelta + 0.5;\n"+
"	if (a < 1) {\n"+
"		a = 10;\n"+
"	}\n"+
"	if (b < 1) {\n"+
"		b = 10;\n"+
"	}\n"+
"	if (c < 1) {\n"+
"		c = 4;\n"+
"	}\n"+
"	if (c > 20) {\n"+
"		c = 4;\n"+
"	}\n"+
"	if (d < 1) {\n"+
"		d = 4;\n"+
"	}\n"+
"	if (d > 20) {\n"+
"		d = 4;\n"+
"	}\n"+
"}\n"+
"''')
)
        .addChildren(X3Dpackage.TimeSensor().setDEF("TourTime").setCycleInterval(5).setLoop(True))
        .addChildren(X3Dpackage.ROUTE().setFromNode("TourTime").setFromField("fraction_changed").setToNode("Animate").setToField("set_fraction"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("a").setToNode("cobweb").setToField("a"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("b").setToNode("cobweb").setToField("b"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("c").setToNode("cobweb").setToField("c"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("d").setToNode("cobweb").setToField("d"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("pdelta").setToNode("cobweb").setToField("pdelta"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("tdelta").setToNode("cobweb").setToField("tdelta"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("a").setToNode("x3dom").setToField("a"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("b").setToNode("x3dom").setToField("b"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("c").setToNode("x3dom").setToField("c"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("d").setToNode("x3dom").setToField("d"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("pdelta").setToNode("x3dom").setToField("pdelta"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Animate").setFromField("tdelta").setToNode("x3dom").setToField("tdelta"))))

