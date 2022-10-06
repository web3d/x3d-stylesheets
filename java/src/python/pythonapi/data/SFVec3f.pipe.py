import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("SFVec3f.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("3 prismatic spheres"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/SFVec3f.x3d")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.NavigationInfo().setType(["EXAMINE","ANY"]))
        .addChildren(X3Dpackage.Transform().setDEF("transform").setTranslation([0,0,0])
          .addChildren(X3Dpackage.Shape()
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([.7,.7,.7]).setSpecularColor([.5,.5,.5])))
            .setGeometry(X3Dpackage.Sphere())))
        .addChildren(X3Dpackage.Script().setDEF("Bounce")
          .addField(X3Dpackage.field().setName("set_translation").setAccessType("inputOnly").setType("SFVec3f").setValue("0 0 0"))
          .addField(X3Dpackage.field().setName("translation_changed").setAccessType("outputOnly").setType("SFVec3f").setValue("0 0 0"))
          .addField(X3Dpackage.field().setName("translation").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
          .addField(X3Dpackage.field().setName("velocity").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
          .addField(X3Dpackage.field().setName("set_fraction").setAccessType("inputOnly").setType("SFTime")).setSourceCode('''ecmascript:\n"+
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
"				if (Math.abs(translation.x) > 10) {\n"+
"					newBubble();\n"+
"				} else if (Math.abs(translation.y) > 10) {\n"+
"					newBubble();\n"+
"				} else if (Math.abs(translation.z) > 10) {\n"+
"					newBubble();\n"+
"				} else {\n"+
"					velocity = new SFVec3f(\n"+
"						velocity.x + Math.random() * 0.2 - 0.1,\n"+
"						velocity.y + Math.random() * 0.2 - 0.1,\n"+
"						velocity.z + Math.random() * 0.2 - 0.1\n"+
"					);\n"+
"				}\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     newBubble();\n"+
"			}\n"+
"\n"+
"''')
)
        .addChildren(X3Dpackage.TimeSensor().setDEF("TourTime").setCycleInterval(0.150).setLoop(True))
        .addChildren(X3Dpackage.ROUTE().setFromNode("TourTime").setFromField("cycleTime").setToNode("Bounce").setToField("set_fraction"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("Bounce").setFromField("translation_changed").setToNode("transform").setToField("set_translation"))))

