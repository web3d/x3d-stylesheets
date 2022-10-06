import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John W Carlson"))
        .addMeta(X3Dpackage.meta().setName("created").setContent("December 13 2015"))
        .addMeta(X3Dpackage.meta().setName("title").setContent("force.x3d"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/force.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("beginnings of a force directed graph in 3D"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Group()
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Extrusion(setSpine = [-50,-50,0,50,50,0], setCreaseAngle = 0.785, setCrossSection = [1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00]).setDEF("extrusion"))
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([0,1,0]))))
          .addChildren(X3Dpackage.TimeSensor().setDEF("TourTime").setLoop(True))
          .addChildren(X3Dpackage.Script().setDEF("MoveCylinder")
            .addField(X3Dpackage.field().setName("set_cycle").setAccessType("inputOnly").setType("SFTime"))
            .addField(X3Dpackage.field().setName("spine").setAccessType("inputOutput").setType("MFVec3f").setValue("-50 -50 0 50 50 0")).setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"                function set_cycle(value) {\n"+
"                        Browser.print(value);\n"+
"                        var endA = new SFVec3f(spine[0].x*Math.random()*2, spine[0].y*Math.random()*2, spine[0].z*Math.random()*2);\n"+
"                        var endB = new SFVec3f(spine[1].x*Math.random()*2, spine[1].y*Math.random()*2, spine[1].z*Math.random()*2);\n"+
"		        spine = new MFVec3f([endA, endB]);\n"+
"                }\n"+
"''')
)
          .addChildren(X3Dpackage.ROUTE().setFromNode("TourTime").setFromField("cycleTime").setToNode("MoveCylinder").setToField("set_cycle"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("MoveCylinder").setFromField("spine_changed").setToNode("extrusion").setToField("spine")))))

