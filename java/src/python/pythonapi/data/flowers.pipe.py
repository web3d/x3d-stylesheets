import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addComponent(X3Dpackage.component().setName("Shaders").setLevel(1))
        .addComponent(X3Dpackage.component().setName("CubeMapTexturing").setLevel(1))
        .addMeta(X3Dpackage.meta().setName("title").setContent("flowers.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("5 or more prismatic flowers"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/flowers.x3d")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.NavigationInfo().setType(["EXAMINE","ANY"]))
        .addChildren(X3Dpackage.Background().setBackUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]).setBottomUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]).setFrontUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]).setLeftUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]).setRightUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]).setTopUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]))
        .addChildren(X3Dpackage.ProtoDeclare().setName("flower")
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Transform().setDEF("transform").setTranslation([0,0,0])
              .addChildren(X3Dpackage.Shape()
                .setAppearance(X3Dpackage.Appearance()
                  .setMaterial(X3Dpackage.Material().setDiffuseColor([.7,.7,.7]).setSpecularColor([.5,.5,.5]))
                  .setTexture(X3Dpackage.ComposedCubeMapTexture().setDEF("texture")
                    .setBack(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]))
                    .setBottom(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]))
                    .setFront(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]))
                    .setLeft(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]))
                    .setRight(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]))
                    .setTop(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])))
                  .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL")
                    .addField(X3Dpackage.field().setName("xxxcube").setType("SFInt32").setAccessType("inputOutput").setValue("0"))
                    .addField(X3Dpackage.field().setName("cube").setType("SFNode").setAccessType("inputOutput")
                      .addChildren(X3Dpackage.ComposedCubeMapTexture().setUSE("texture")))
                    .addField(X3Dpackage.field().setName("chromaticDispertion").setType("SFVec3f").setAccessType("inputOutput").setValue("0.98 1.0 1.033"))
                    .addField(X3Dpackage.field().setName("bias").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                    .addField(X3Dpackage.field().setName("scale").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                    .addField(X3Dpackage.field().setName("power").setType("SFFloat").setAccessType("inputOutput").setValue("2.0"))
                    .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/common.vs","https://coderextreme.net/X3DJSONLD/shaders/common.vs"]).setType("VERTEX"))
                    .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/gl_flowers_chromatic.fs","https://coderextreme.net/X3DJSONLD/shaders/gl_flowers_chromatic.fs"]).setType("FRAGMENT")))
                  .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL")
                    .addField(X3Dpackage.field().setName("xxxcube").setType("SFInt32").setAccessType("inputOutput").setValue("0"))
                    .addField(X3Dpackage.field().setName("cube").setType("SFNode").setAccessType("inputOutput")
                      .addChildren(X3Dpackage.ComposedCubeMapTexture().setUSE("texture")))
                    .addField(X3Dpackage.field().setName("chromaticDispertion").setType("SFVec3f").setAccessType("inputOutput").setValue("0.98 1.0 1.033"))
                    .addField(X3Dpackage.field().setName("bias").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                    .addField(X3Dpackage.field().setName("scale").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                    .addField(X3Dpackage.field().setName("power").setType("SFFloat").setAccessType("inputOutput").setValue("2.0"))
                    .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]).setType("VERTEX"))
                    .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]).setType("FRAGMENT")))
                  .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL").setDEF("shader")
                    .addField(X3Dpackage.field().setName("xxxcube").setType("SFInt32").setAccessType("inputOutput").setValue("0"))
                    .addField(X3Dpackage.field().setName("cube").setType("SFNode").setAccessType("inputOutput")
                      .addChildren(X3Dpackage.ComposedCubeMapTexture().setUSE("texture")))
                    .addField(X3Dpackage.field().setName("chromaticDispertion").setType("SFVec3f").setAccessType("inputOutput").setValue("0.98 1.0 1.033"))
                    .addField(X3Dpackage.field().setName("bias").setType("SFFloat").setAccessType("inputOutput").setValue("10"))
                    .addField(X3Dpackage.field().setName("scale").setType("SFFloat").setAccessType("inputOutput").setValue("10"))
                    .addField(X3Dpackage.field().setName("power").setType("SFFloat").setAccessType("inputOutput").setValue("2.0"))
                    .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]).setType("VERTEX"))
                    .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]).setType("FRAGMENT"))))
                #
#			<Sphere></Sphere>
#			

                .setGeometry(X3Dpackage.IndexedFaceSet(setConvex = False, setCreaseAngle = 0).setDEF("Orbit")
                  .setCoord(X3Dpackage.Coordinate().setDEF("OrbitCoordinates")))))
            .addChildren(X3Dpackage.Script().setDEF("Bounce")
              .addField(X3Dpackage.field().setName("translation").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
              .addField(X3Dpackage.field().setName("velocity").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
              .addField(X3Dpackage.field().setName("set_fraction").setAccessType("inputOnly").setType("SFTime"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setName("coordinates").setType("MFVec3f"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setName("coordIndexes").setType("MFInt32"))
              .addField(X3Dpackage.field().setName("a").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
              .addField(X3Dpackage.field().setName("b").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
              .addField(X3Dpackage.field().setName("c").setType("SFFloat").setAccessType("inputOutput").setValue("3"))
              .addField(X3Dpackage.field().setName("d").setType("SFFloat").setAccessType("inputOutput").setValue("3"))
              .addField(X3Dpackage.field().setName("tdelta").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
              .addField(X3Dpackage.field().setName("pdelta").setType("SFFloat").setAccessType("inputOutput").setValue("0.5")).setSourceCode('''ecmascript:\n"+
"			function newBubble() {\n"+
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
"			    if (Math.abs(translation.x) > 10) {\n"+
"					newBubble();\n"+
"			    } else if (Math.abs(translation.y) > 10) {\n"+
"					newBubble();\n"+
"			    } else if (Math.abs(translation.z) > 10) {\n"+
"					newBubble();\n"+
"			    } else {\n"+
"					velocity = new SFVec3f(\n"+
"						velocity.x + Math.random() * 0.2 - 0.1,\n"+
"						velocity.y + Math.random() * 0.2 - 0.1,\n"+
"						velocity.z + Math.random() * 0.2 - 0.1\n"+
"					);\n"+
"			    }\n"+
"			    animate_flowers();\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     var cis = [];\n"+
"			     newBubble();\n"+
"			     resolution = 100;\n"+
"			     updateCoordinates(resolution);\n"+
"			     for ( i = 0; i < resolution-1; i++) {\n"+
"				for ( j = 0; j < resolution-1; j++) {\n"+
"				     cis.push(i*resolution+j);\n"+
"				     cis.push(i*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j);\n"+
"				     cis.push(-1);\n"+
"				}\n"+
"			    }\n"+
"			     coordIndexes = new MFInt32(cis);\n"+
"			}\n"+
"\n"+
"			function updateCoordinates(resolution) {\n"+
"			     theta = 0.0;\n"+
"			     phi = 0.0;\n"+
"			     delta = (2 * 3.141592653) / (resolution-1);\n"+
"			     var crds = [];\n"+
"			     for ( i = 0; i < resolution; i++) {\n"+
"				for ( j = 0; j < resolution; j++) {\n"+
"					rho = a + b * Math.cos(c * theta) * Math.cos(d * phi);\n"+
"					crds.push(new SFVec3f(\n"+
"						rho * Math.cos(phi) * Math.cos(theta),\n"+
"						rho * Math.cos(phi) * Math.sin(theta),\n"+
"						rho * Math.sin(phi)\n"+
"					));\n"+
"					theta += delta;\n"+
"				}\n"+
"				phi += delta;\n"+
"				coordinates = new MFVec3f(crds);\n"+
"			     }\n"+
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
"				resolution = 100;\n"+
"				updateCoordinates(resolution);\n"+
"			}\n"+
"\n"+
"''')
)
            .addChildren(X3Dpackage.TimeSensor().setDEF("TourTime").setCycleInterval(0.150).setLoop(True))
            .addChildren(X3Dpackage.TimeSensor().setDEF("SongTime").setLoop(True))
            .addChildren(X3Dpackage.Sound().setMaxBack(100).setMaxFront(100).setMinBack(20).setMinFront(20)
              .setSource(X3Dpackage.AudioClip().setDEF("AudioClip").setDescription("Chandubabamusic #1").setUrl(["../resources/chandubabamusic1.wav"])))
            .addChildren(X3Dpackage.ROUTE().setFromField("cycleTime").setFromNode("SongTime").setToField("startTime").setToNode("AudioClip"))
            .addChildren(X3Dpackage.ROUTE().setFromNode("TourTime").setFromField("cycleTime").setToNode("Bounce").setToField("set_fraction"))
            .addChildren(X3Dpackage.ROUTE().setFromNode("Bounce").setFromField("translation").setToNode("transform").setToField("set_translation"))
            #
#		<ROUTE fromField=\"coordIndexes\" fromNode=\"Bounce\" toField=\"set_coordIndex\" toNode=\"Orbit\"/>
#		<ROUTE fromField=\"coordinates\" fromNode=\"Bounce\" toField=\"set_point\" toNode=\"OrbitCoordinates\"/>
#		

            ))
        .addChildren(X3Dpackage.Transform()
          .addChildren(X3Dpackage.ProtoInstance().setName("flower"))
          #
#            <ProtoInstance name=\"flower\"/>
#            <ProtoInstance name=\"flower\"/>
#	    

          )))

