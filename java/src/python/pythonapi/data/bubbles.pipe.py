import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addComponent(X3Dpackage.component().setName("EnvironmentalEffects").setLevel(1))
        .addComponent(X3Dpackage.component().setName("EnvironmentalEffects").setLevel(3))
        .addComponent(X3Dpackage.component().setName("Shaders").setLevel(1))
        .addComponent(X3Dpackage.component().setName("CubeMapTexturing").setLevel(1))
        .addMeta(X3Dpackage.meta().setName("title").setContent("bubbles.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("manual"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/bubbles.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("not sure what this is")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.NavigationInfo().setType(["EXAMINE"]))
        .addChildren(X3Dpackage.Viewpoint().setDEF("Tour").setDescription("Tour Views"))
        .addChildren(X3Dpackage.Viewpoint().setPosition([0,0,4]).setDescription("sphere in road"))
        .addChildren(X3Dpackage.Background().setBackUrl(["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"]).setBottomUrl(["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"]).setFrontUrl(["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"]).setLeftUrl(["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"]).setRightUrl(["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"]).setTopUrl(["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"]))
        .addChildren(X3Dpackage.Transform().setDEF("Rose01")
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Sphere())
            .setAppearance(X3Dpackage.Appearance().setDEF("_01_-_Default")
              .setMaterial(X3Dpackage.Material().setDiffuseColor([0.7,0.7,0.7]).setSpecularColor([0.5,0.5,0.5]))
              .setTexture(X3Dpackage.ComposedCubeMapTexture()
                .setBack(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"]))
                .setBottom(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"]))
                .setFront(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"]))
                .setLeft(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"]))
                .setRight(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"]))
                .setTop(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"])))
              .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL").setDEF("cobweb")
                .addField(X3Dpackage.field().setName("cube").setAccessType("inputOutput").setType("SFInt32").setValue("0"))
                .addField(X3Dpackage.field().setName("chromaticDispertion").setAccessType("inputOutput").setType("SFVec3f").setValue("0.98 1 1.033"))
                .addField(X3Dpackage.field().setName("bias").setAccessType("inputOutput").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("scale").setAccessType("inputOutput").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("power").setAccessType("inputOutput").setType("SFFloat").setValue("2"))
                .setParts(X3Dpackage.ShaderPart().setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]).setType("VERTEX"))
                .setParts(X3Dpackage.ShaderPart().setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]).setType("FRAGMENT")))
              .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL").setDEF("x3dom")
                .addField(X3Dpackage.field().setName("cube").setAccessType("inputOutput").setType("SFInt32").setValue("0"))
                .addField(X3Dpackage.field().setName("chromaticDispertion").setAccessType("inputOutput").setType("SFVec3f").setValue("0.98 1 1.033"))
                .addField(X3Dpackage.field().setName("bias").setAccessType("inputOutput").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("scale").setAccessType("inputOutput").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("power").setAccessType("inputOutput").setType("SFFloat").setValue("2"))
                .setParts(X3Dpackage.ShaderPart().setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]).setType("VERTEX"))
                .setParts(X3Dpackage.ShaderPart().setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]).setType("FRAGMENT"))))))
        .addChildren(X3Dpackage.TimeSensor().setDEF("TourTime").setCycleInterval(5).setLoop(True))
        .addChildren(X3Dpackage.PositionInterpolator().setDEF("TourPosition").setKey([0,1]).setKeyValue([0,0,10,0,0,-10]))
        .addChildren(X3Dpackage.OrientationInterpolator().setDEF("TourOrientation").setKey([0,1]).setKeyValue([0,1,0,0,0,1,0,3.1416]))
        .addChildren(X3Dpackage.Script().setDEF("RandomTourTime")
          .addField(X3Dpackage.field().setName("set_cycle").setAccessType("inputOnly").setType("SFTime"))
          .addField(X3Dpackage.field().setName("lastKey").setAccessType("inputOutput").setType("SFFloat").setValue("0"))
          .addField(X3Dpackage.field().setName("orientations").setAccessType("inputOutput").setType("MFRotation").setValue("0 1 0 0 0 1 0 -1.57 0 1 0 3.14 0 1 0 1.57 0 1 0 0 1 0 0 -1.57 0 1 0 0 1 0 0 1.57 0 1 0 0"))
          .addField(X3Dpackage.field().setName("positions").setAccessType("inputOutput").setType("MFVec3f").setValue("0 0 10 -10 0 0 0 0 -10 10 0 0 0 0 10 0 10 0 0 0 10 0 -10 0 0 0 10"))
          .addField(X3Dpackage.field().setName("position_changed").setAccessType("outputOnly").setType("MFVec3f"))
          .addField(X3Dpackage.field().setName("set_orientation").setAccessType("inputOnly").setType("MFRotation"))
          .addField(X3Dpackage.field().setName("orientation_changed").setAccessType("outputOnly").setType("MFRotation")).setSourceCode('''ecmascript:\n"+
"               function set_cycle(value) {\n"+
"                        var ov = lastKey;\n"+
"                        do {\n"+
"                            lastKey = Math.round(Math.random()*(positions.length-1));\n"+
"                        } while (lastKey === ov);\n"+
"                        var vc = lastKey;\n"+
"                        \n"+
"                        orientation_changed = new MFRotation();\n"+
"                        orientation_changed[0] = new SFRotation(orientations[ov].x, orientations[ov].y, orientations[ov].z, orientations[ov].w);\n"+
"                        orientation_changed[1] = new SFRotation(orientations[vc].x, orientations[vc].y, orientations[vc].z, orientations[vc].w);\n"+
"                        position_changed = new MFVec3f();\n"+
"                        position_changed[0] = new SFVec3f(positions[ov].x,positions[ov].y,positions[ov].z);\n"+
"                        position_changed[1] = new SFVec3f(positions[vc].x,positions[vc].y,positions[vc].z);\n"+
"                    // }\n"+
"               }''')
)
        .addChildren(X3Dpackage.ROUTE().setFromNode("TourTime").setFromField("cycleTime_changed").setToNode("RandomTourTime").setToField("set_cycle"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("RandomTourTime").setFromField("orientation_changed").setToNode("TourOrientation").setToField("set_keyValue"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("RandomTourTime").setFromField("position_changed").setToNode("TourPosition").setToField("set_keyValue"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("TourTime").setFromField("fraction_changed").setToNode("TourOrientation").setToField("set_fraction"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("TourOrientation").setFromField("value_changed").setToNode("Tour").setToField("set_orientation"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("TourTime").setFromField("fraction_changed").setToNode("TourPosition").setToField("set_fraction"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("TourPosition").setFromField("value_changed").setToNode("Tour").setToField("set_position"))))

