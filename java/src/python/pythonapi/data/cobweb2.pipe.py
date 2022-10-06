import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("geo.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("Tour around a prismatic sphere"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/geo.x3d"))
        .addMeta(X3Dpackage.meta().setName("translated").setContent("13 March 2016"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("X3dToJson.xslt, http://www.web3d.org/x3d/stylesheets/X3dToJson.html")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.NavigationInfo().setType(["EXAMINE"]))
        .addChildren(X3Dpackage.Viewpoint().setPosition([0,0,4]).setOrientation([1,0,0,0]).setDescription("Bubbles in action"))
        .addChildren(X3Dpackage.Background().setBackUrl(["../resources/images/BK.png","https://coderextreme.net/X3DJSONLD/images/BK.png"]).setBottomUrl(["../resources/images/BT.png","https://coderextreme.net/X3DJSONLD/images/BT.png"]).setFrontUrl(["../resources/images/FR.png","https://coderextreme.net/X3DJSONLD/images/FR.png"]).setLeftUrl(["../resources/images/LF.png","https://coderextreme.net/X3DJSONLD/images/LF.png"]).setRightUrl(["../resources/images/RT.png","https://coderextreme.net/X3DJSONLD/images/RT.png"]).setTopUrl(["../resources/images/TP.png","https://coderextreme.net/X3DJSONLD/images/TP.png"]))
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
"    if (typeof translation === 'undefined') {\n"+
"		translation = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof velocity === 'undefined') {\n"+
"		velocity = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof scalevel === 'undefined') {\n"+
"		scalevel = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof scale === 'undefined') {\n"+
"		scale = new SFVec3f(1, 1, 1);\n"+
"    }\n"+
"    translation = new SFVec3f(	translation.x + velocity.x, translation.y + velocity.y, translation.z + velocity.z);\n"+
"    scale = new SFVec3f(scale.x + scalvel.x, scale.y + scalvel.y, scale.z + scalvel.z);\n"+
"    // if you get to far away or too big, explode\n"+
"    if ( Math.abs(translation.x) &gt; 256) {\n"+
"	translation.x = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if ( Math.abs(translation.y) &gt; 256) {\n"+
"	translation.y = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if ( Math.abs(translation.z) &gt; 256) {\n"+
"	translation.z = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.x) &gt; 20) {\n"+
"	scale.x = scale.x/20;\n"+
"	translation.x = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.y) &gt; 20) {\n"+
"	scale.y = scale.y/20;\n"+
"	translation.y = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.z) &gt; 20) {\n"+
"	scale.z = scale.z/20;\n"+
"	translation.z = 0;\n"+
"	initialize();\n"+
"    }\n"+
"}''')
)
              .addChildren(X3Dpackage.TimeSensor().setDEF("bubbleClock").setCycleInterval(10).setLoop(True))
              .addChildren(X3Dpackage.ROUTE().setFromNode("bounce").setFromField("translation_changed").setToNode("transform").setToField("set_translation"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("bounce").setFromField("scale_changed").setToNode("transform").setToField("set_scale"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("bubbleClock").setFromField("fraction_changed").setToNode("bounce").setToField("set_fraction")))))
        .addChildren(X3Dpackage.ProtoInstance().setName("Bubble").setDEF("bubbleA"))
        .addChildren(X3Dpackage.ProtoInstance().setName("Bubble").setDEF("bubbleB"))
        .addChildren(X3Dpackage.ProtoInstance().setName("Bubble").setDEF("bubbleC"))
        .addChildren(X3Dpackage.ProtoInstance().setName("Bubble").setDEF("bubbleD"))))

