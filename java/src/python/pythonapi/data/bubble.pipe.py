import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("bubble.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("Tour around a prismatic sphere"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/bubble.x3d")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.NavigationInfo().setType(["EXAMINE"]))
        .addChildren(X3Dpackage.Viewpoint().setPosition([0,0,4]).setOrientation([1,0,0,0]).setDescription("Bubble in action"))
        .addChildren(X3Dpackage.ProtoDeclare().setName("Bubble")
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Transform().setDEF("transform")
              .addChildren(X3Dpackage.Shape()
                .setGeometry(X3Dpackage.Sphere(setRadius = 0.25))
                .setAppearance(X3Dpackage.Appearance()
                  .setMaterial(X3Dpackage.Material().setDiffuseColor([1,0,0]).setTransparency(0.2))))
              .addChildren(X3Dpackage.Script().setDEF("bounce")
                .addField(X3Dpackage.field().setName("scale").setAccessType("inputOutput").setType("SFVec3f").setValue("1 1 1"))
                .addField(X3Dpackage.field().setName("translation").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
                .addField(X3Dpackage.field().setName("velocity").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
                .addField(X3Dpackage.field().setName("scalvel").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
                .addField(X3Dpackage.field().setName("set_fraction").setAccessType("inputOnly").setType("SFFloat")).setSourceCode('''ecmascript:\n"+
"function initialize() {\n"+
"    velocity = new SFVec3f(Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125);\n"+
"\n"+
"    scalvel = new SFVec3f(Math.random() * 0.4, Math.random() * 0.4, Math.random() * 0.4);\n"+
"}\n"+
"\n"+
"function set_fraction(value) {\n"+
"	translation = new SFVec3f(\n"+
"		translation.x + velocity.x,\n"+
"		translation.y + velocity.y,\n"+
"		translation.z + velocity.z);\n"+
"	scale = new SFVec3f(\n"+
"		scale.x + scalvel.x,\n"+
"		scale.y + scalvel.y,\n"+
"		scale.z + scalvel.z);\n"+
"        // if you get to far away or too big, explode\n"+
"        if ( Math.abs(translation.x) > 256) {\n"+
"		translation.x = 0;\n"+
"		initialize();\n"+
"	}\n"+
"        if ( Math.abs(translation.y) > 256) {\n"+
"		translation.y = 0;\n"+
"		initialize();\n"+
"	}\n"+
"        if ( Math.abs(translation.z) > 256) {\n"+
"		translation.z = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.x) > 20) {\n"+
"		scale.x = scale.x/2;\n"+
"		translation.x = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.y) > 20) {\n"+
"		scale.y = scale.y/2;\n"+
"		translation.y = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.z) > 20) {\n"+
"		scale.z = scale.z/2;\n"+
"		translation.z = 0;\n"+
"		initialize();\n"+
"	}\n"+
"}\n"+
"''')
)
              .addChildren(X3Dpackage.TimeSensor().setDEF("bubbleClock").setCycleInterval(10).setLoop(True))
              .addChildren(X3Dpackage.ROUTE().setFromNode("bounce").setFromField("translation_changed").setToNode("transform").setToField("set_translation"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("bounce").setFromField("scale_changed").setToNode("transform").setToField("set_scale"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("bubbleClock").setFromField("fraction_changed").setToNode("bounce").setToField("set_fraction")))))
        .addChildren(X3Dpackage.ProtoInstance().setName("Bubble").setDEF("bubbleA"))))

