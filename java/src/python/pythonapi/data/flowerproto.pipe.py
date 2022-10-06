import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addComponent(X3Dpackage.component().setName("Shaders").setLevel(1))
        .addComponent(X3Dpackage.component().setName("CubeMapTexturing").setLevel(1))
        .addMeta(X3Dpackage.meta().setName("title").setContent("flowerproto.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("A flower proto with configurable shaders"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/flowerproto.x3d")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.ProtoDeclare().setName("FlowerProto")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("vertex").setType("MFString").setValue("\"../shaders/gl_flowers_chromatic.vs\""))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("fragment").setType("MFString").setValue("\"../shaders/pc_flowers.fs\"")))
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Transform().setDEF("transform").setTranslation([0,0,0])
              .addChildren(X3Dpackage.Shape()
                .setAppearance(X3Dpackage.Appearance()
                  .setMaterial(X3Dpackage.Material().setDiffuseColor([.7,.7,.7]))
                  .setTexture(X3Dpackage.ComposedCubeMapTexture().setDEF("texture")
                    .setBack(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]))
                    .setBottom(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]))
                    .setFront(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]))
                    .setLeft(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]))
                    .setRight(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]))
                    .setTop(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])))
                  .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL").setDEF("shader")
                    .addField(X3Dpackage.field().setName("cube").setType("SFInt32").setAccessType("inputOutput").setValue("0"))
                    #
#                                <field name='cube' type='SFNode' accessType=\"inputOutput\">
#                                    <ComposedCubeMapTexture USE=\"texture\"/>
#                                </field>
#				

                    .addField(X3Dpackage.field().setName("chromaticDispertion").setType("SFVec3f").setAccessType("inputOutput").setValue("0.98 1.0 1.033"))
                    .addField(X3Dpackage.field().setName("bias").setType("SFFloat").setAccessType("inputOutput").setValue("10"))
                    .addField(X3Dpackage.field().setName("scale").setType("SFFloat").setAccessType("inputOutput").setValue("10"))
                    .addField(X3Dpackage.field().setName("power").setType("SFFloat").setAccessType("inputOutput").setValue("2.0"))
                    .addField(X3Dpackage.field().setName("a").setType("SFFloat").setAccessType("inputOutput").setValue("3"))
                    .addField(X3Dpackage.field().setName("b").setType("SFFloat").setAccessType("inputOutput").setValue("1"))
                    .addField(X3Dpackage.field().setName("c").setType("SFFloat").setAccessType("inputOutput").setValue("3"))
                    .addField(X3Dpackage.field().setName("d").setType("SFFloat").setAccessType("inputOutput").setValue("3"))
                    .addField(X3Dpackage.field().setName("tdelta").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                    .addField(X3Dpackage.field().setName("pdelta").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                    .addParts(X3Dpackage.ShaderPart().setType("VERTEX")
                      .setIS(X3Dpackage.IS()
                        .addConnect(X3Dpackage.connect().setNodeField("url").setProtoField("vertex"))))
                    .addParts(X3Dpackage.ShaderPart().setType("FRAGMENT")
                      .setIS(X3Dpackage.IS()
                        .addConnect(X3Dpackage.connect().setNodeField("url").setProtoField("fragment"))))))
                .setGeometry(X3Dpackage.Sphere()))
              .addChildren(X3Dpackage.Script().setDEF("Bounce")
                .addField(X3Dpackage.field().setName("translation").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
                .addField(X3Dpackage.field().setName("velocity").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
                .addField(X3Dpackage.field().setName("set_fraction").setAccessType("inputOnly").setType("SFTime"))
                .addField(X3Dpackage.field().setName("a").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                .addField(X3Dpackage.field().setName("b").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                .addField(X3Dpackage.field().setName("c").setType("SFFloat").setAccessType("inputOutput").setValue("3"))
                .addField(X3Dpackage.field().setName("d").setType("SFFloat").setAccessType("inputOutput").setValue("3"))
                .addField(X3Dpackage.field().setName("tdelta").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                .addField(X3Dpackage.field().setName("pdelta").setType("SFFloat").setAccessType("inputOutput").setValue("0.5")).setSourceCode('''ecmascript:\n"+
"			function initialize() {\n"+
"			    translation = new SFVec3f(0, 0, 0);\n"+
"			    velocity = new SFVec3f(\n"+
"			    	Math.random() - 0.5,\n"+
"				Math.random() - 0.5,\n"+
"				Math.random() - 0.5);\n"+
"			}\n"+
"			function set_fraction() {\n"+
"			    translation = new SFVec3f(\n"+
"			    	translation.x + velocity.x,\n"+
"				translation.y + velocity.y,\n"+
"				translation.z + velocity.z);\n"+
"			    for (var j = 0; j <= 2; j++) {\n"+
"				    if (Math.abs(translation.x) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.y) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.z) > 10) {\n"+
"					initialize();\n"+
"				    } else {\n"+
"					velocity.x += Math.random() * 0.2 - 0.1;\n"+
"					velocity.y += Math.random() * 0.2 - 0.1;\n"+
"					velocity.z += Math.random() * 0.2 - 0.1;\n"+
"				    }\n"+
"			    }\n"+
"			    animate_flowers();\n"+
"			}\n"+
"\n"+
"			function animate_flowers(fraction, eventTime) {\n"+
"				choice = Math.floor(Math.random() * 4);\n"+
"				switch (choice) {\n"+
"				case 0:\n"+
"					a += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 1:\n"+
"					b += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 2:\n"+
"					c += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				case 3:\n"+
"					d += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				}\n"+
"				tdelta += 0.5;\n"+
"				pdelta += 0.5;\n"+
"				if (a > 1) {\n"+
"					a =  0.5;\n"+
"				}\n"+
"				if (b > 1) {\n"+
"					b =  0.5;\n"+
"				}\n"+
"				if (c < 1) {\n"+
"					c =  4;\n"+
"				}\n"+
"				if (d < 1) {\n"+
"					d =  4;\n"+
"				}\n"+
"				if (c > 10) {\n"+
"					c = 4;\n"+
"				}\n"+
"				if (d > 10) {\n"+
"					d = 4;\n"+
"				}\n"+
"			}\n"+
"\n"+
"''')
)
              .addChildren(X3Dpackage.TimeSensor().setDEF("TourTime").setCycleInterval(0.150).setLoop(True))
              .addChildren(X3Dpackage.ROUTE().setFromNode("TourTime").setFromField("cycleTime").setToNode("Bounce").setToField("set_fraction"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("Bounce").setFromField("translation_changed").setToNode("transform").setToField("set_translation"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("Bounce").setFromField("a").setToNode("shader").setToField("a"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("Bounce").setFromField("b").setToNode("shader").setToField("b"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("Bounce").setFromField("c").setToNode("shader").setToField("c"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("Bounce").setFromField("d").setToNode("shader").setToField("d"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("Bounce").setFromField("tdelta").setToNode("shader").setToField("tdelta"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("Bounce").setFromField("pdelta").setToNode("shader").setToField("pdelta")))))))

