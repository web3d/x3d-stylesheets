import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("pp3.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("translator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("created").setContent("5 May 2015"))
        .addMeta(X3Dpackage.meta().setContent("05 May 2017").setName("modified"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("A process pipeline between three spheres (try typing on spheres and blue"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/x3d/pp3.x3d"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("manual")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.ProtoDeclare().setName("Process")
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Group()
              #left

              .addChildren(X3Dpackage.Transform().setScale([0.5,0.5,0.5])
                .addChildren(X3Dpackage.Shape()
                  .setAppearance(X3Dpackage.Appearance()
                    .setMaterial(X3Dpackage.Material().setDiffuseColor([0.7,1,0]).setTransparency(0.5)))
                  .setGeometry(X3Dpackage.Extrusion(setCreaseAngle = 0.785, setCrossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], setSpine = [-2.5,0,0,-1.5,0,0])))
                #<Transform translation=\"-2.5 0 0\"> <Shape> <Text DEF=\"LeftString\" string='\"l\"'/> </Shape> </Transform> <StringSensor DEF=\"LeftSensor\" enabled=\"false\"/> <TouchSensor DEF=\"LeftTouch\" enabled=\"true\"/>

                )
              #right

              .addChildren(X3Dpackage.Transform().setScale([0.5,0.5,0.5])
                .addChildren(X3Dpackage.Shape()
                  .setAppearance(X3Dpackage.Appearance()
                    .setMaterial(X3Dpackage.Material().setDiffuseColor([0,0.7,1]).setTransparency(0.5)))
                  .setGeometry(X3Dpackage.Extrusion(setCreaseAngle = 0.785, setCrossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], setSpine = [1.5,0,0,2.5,0,0])))
                .addChildren(X3Dpackage.Transform().setTranslation([2,0,0])
                  .addChildren(X3Dpackage.Shape()
                    .setAppearance(X3Dpackage.Appearance()
                      .setMaterial(X3Dpackage.Material().setDEF("MaterialLightBlue").setDiffuseColor([1,1,1])))
                    .setGeometry(X3Dpackage.Text().setDEF("RightString").setString(["r"]))))
                .addChildren(X3Dpackage.StringSensor().setDEF("RightSensor").setEnabled(False).setDeletionAllowed(True))
                .addChildren(X3Dpackage.TouchSensor().setDescription("touch to activate").setDEF("RightTouch")))
              #up

              .addChildren(X3Dpackage.Transform().setScale([0.5,0.5,0.5])
                .addChildren(X3Dpackage.Shape()
                  .setAppearance(X3Dpackage.Appearance()
                    .setMaterial(X3Dpackage.Material().setDiffuseColor([0,0.7,1]).setTransparency(0.5)))
                  .setGeometry(X3Dpackage.Extrusion(setCreaseAngle = 0.785, setCrossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], setSpine = [0,1.5,0,0,2.5,0])))
                .addChildren(X3Dpackage.Transform().setTranslation([-0.5,2,0])
                  .addChildren(X3Dpackage.Shape()
                    .setAppearance(X3Dpackage.Appearance()
                      .setMaterial(X3Dpackage.Material().setUSE("MaterialLightBlue")))
                    .setGeometry(X3Dpackage.Text().setDEF("UpString").setString(["u"]))))
                .addChildren(X3Dpackage.StringSensor().setDEF("UpSensor").setEnabled(False).setDeletionAllowed(True))
                .addChildren(X3Dpackage.TouchSensor().setDescription("touch to activate").setDEF("UpTouch")))
              #down

              .addChildren(X3Dpackage.Transform().setScale([0.5,0.5,0.5])
                .addChildren(X3Dpackage.Shape()
                  .setAppearance(X3Dpackage.Appearance()
                    .setMaterial(X3Dpackage.Material().setDiffuseColor([0.7,1,0]).setTransparency(0.5)))
                  .setGeometry(X3Dpackage.Extrusion(setCreaseAngle = 0.785, setCrossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], setSpine = [0,-2.5,0,0,-1.5,0])))
                #<Transform translation=\"-0.5 -2.5 0\"> <Shape> <Text DEF=\"DownString\" string='\"d\"'/> </Shape> </Transform> <StringSensor DEF=\"DownSensor\" enabled=\"false\"/> <TouchSensor description='touch to activate' DEF=\"DownTouch\" enabled=\"true\"/>

                )
              #center

              .addChildren(X3Dpackage.Transform()
                .addChildren(X3Dpackage.Shape()
                  .setAppearance(X3Dpackage.Appearance()
                    .setMaterial(X3Dpackage.Material().setDiffuseColor([1,0,0.7])))
                  .setGeometry(X3Dpackage.Sphere()))
                .addChildren(X3Dpackage.Transform().setScale([0.5,0.5,0.5]).setTranslation([-0.5,0,1])
                  .addChildren(X3Dpackage.Shape()
                    .setAppearance(X3Dpackage.Appearance()
                      .setMaterial(X3Dpackage.Material().setUSE("MaterialLightBlue")))
                    .setGeometry(X3Dpackage.Text().setDEF("CenterString"))))
                .addChildren(X3Dpackage.StringSensor().setDEF("CenterSensor").setEnabled(False).setDeletionAllowed(True))
                .addChildren(X3Dpackage.TouchSensor().setDescription("touch to activate").setDEF("CenterTouch"))))
            .addChildren(X3Dpackage.Script().setDEF("RightSingleToMultiString")
              .addField(X3Dpackage.field().setName("set_rightstring").setAccessType("inputOnly").setType("SFString"))
              .addField(X3Dpackage.field().setName("rightlines").setAccessType("outputOnly").setType("MFString")).setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	rightlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_rightstring(rightstr) {\n"+
"	rightlines = new MFString(rightstr);\n"+
"}''')
)
            .addChildren(X3Dpackage.Script().setDEF("UpSingleToMultiString")
              .addField(X3Dpackage.field().setName("set_upstring").setAccessType("inputOnly").setType("SFString"))
              .addField(X3Dpackage.field().setName("uplines").setAccessType("outputOnly").setType("MFString")).setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	uplines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_upstring(upstr) {\n"+
"	uplines = new MFString(upstr);\n"+
"}''')
)
            .addChildren(X3Dpackage.Script().setDEF("CenterSingleToMultiString")
              .addField(X3Dpackage.field().setName("set_centerstring").setAccessType("inputOnly").setType("SFString"))
              .addField(X3Dpackage.field().setName("centerlines").setAccessType("outputOnly").setType("MFString")).setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	centerlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_centerstring(centerstr) {\n"+
"	centerlines = new MFString(centerstr);\n"+
"}''')
)
            .addChildren(X3Dpackage.ROUTE().setFromField("enteredText").setFromNode("CenterSensor").setToField("set_centerstring").setToNode("CenterSingleToMultiString"))
            .addChildren(X3Dpackage.ROUTE().setFromField("centerlines").setFromNode("CenterSingleToMultiString").setToField("set_string").setToNode("CenterString"))
            .addChildren(X3Dpackage.ROUTE().setFromField("isOver").setFromNode("CenterTouch").setToField("set_enabled").setToNode("CenterSensor"))
            .addChildren(X3Dpackage.ROUTE().setFromField("enteredText").setFromNode("RightSensor").setToField("set_rightstring").setToNode("RightSingleToMultiString"))
            .addChildren(X3Dpackage.ROUTE().setFromField("rightlines").setFromNode("RightSingleToMultiString").setToField("set_string").setToNode("RightString"))
            .addChildren(X3Dpackage.ROUTE().setFromField("isOver").setFromNode("RightTouch").setToField("set_enabled").setToNode("RightSensor"))
            .addChildren(X3Dpackage.ROUTE().setFromField("enteredText").setFromNode("UpSensor").setToField("set_upstring").setToNode("UpSingleToMultiString"))
            .addChildren(X3Dpackage.ROUTE().setFromField("uplines").setFromNode("UpSingleToMultiString").setToField("set_string").setToNode("UpString"))
            .addChildren(X3Dpackage.ROUTE().setFromField("isOver").setFromNode("UpTouch").setToField("set_enabled").setToNode("UpSensor"))))
        .addChildren(X3Dpackage.NavigationInfo())
        .addChildren(X3Dpackage.Viewpoint().setDescription("Process pipes").setOrientation([1,0,0,-0.4]).setPosition([0,5,12]))
        .addChildren(X3Dpackage.Transform().setTranslation([0,-2.5,0])
          .addChildren(X3Dpackage.ProtoInstance().setName("Process")))
        .addChildren(X3Dpackage.Transform()
          .addChildren(X3Dpackage.ProtoInstance().setName("Process")))
        .addChildren(X3Dpackage.Transform().setTranslation([0,2.5,0])
          .addChildren(X3Dpackage.ProtoInstance().setName("Process")))))

