import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John W Carlson"))
        .addMeta(X3Dpackage.meta().setName("created").setContent("December 13 2015"))
        .addMeta(X3Dpackage.meta().setName("modified").setContent("April 18 2017"))
        .addMeta(X3Dpackage.meta().setName("title").setContent("fors2.x3d"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/fors2.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("beginnings of a force directed graph in 3D"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.ProtoDeclare().setName("node")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            .addField(X3Dpackage.field().setName("position").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0")))
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Transform().setDEF("transform")
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("translation").setProtoField("position")))
              .addChildren(X3Dpackage.Shape()
                #comment before Sphere

                #comment after Sphere

                #comment after Appearance

                .setGeometry(X3Dpackage.Sphere())
                .setAppearance(X3Dpackage.Appearance()
                  #comment before Material

                  #comment after Material

                  .setMaterial(X3Dpackage.Material().setDiffuseColor([1,0,0])))))
            .addChildren(X3Dpackage.PositionInterpolator().setDEF("NodePosition").setKey([0,1]).setKeyValue([0,0,0,0,5,0]))
            .addChildren(X3Dpackage.Script().setDEF("MoveBall")
              .addField(X3Dpackage.field().setName("translation").setAccessType("inputOutput").setType("SFVec3f").setValue("50 50 0"))
              .addField(X3Dpackage.field().setName("old").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
              .addField(X3Dpackage.field().setName("set_cycle").setAccessType("inputOnly").setType("SFTime"))
              .addField(X3Dpackage.field().setName("keyValue").setAccessType("outputOnly").setType("MFVec3f")).setSourceCode(''' ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f([old, translation]);\n"+
"						// Browser.println(translation);\n"+
"					}\n"+
" ''')
)
            .addChildren(X3Dpackage.TimeSensor().setDEF("nodeClock").setCycleInterval(3).setLoop(True))
            .addChildren(X3Dpackage.ROUTE().setFromNode("nodeClock").setFromField("cycleTime").setToNode("MoveBall").setToField("set_cycle"))
            .addChildren(X3Dpackage.ROUTE().setFromNode("nodeClock").setFromField("fraction_changed").setToNode("NodePosition").setToField("set_fraction"))
            .addChildren(X3Dpackage.ROUTE().setFromNode("MoveBall").setFromField("keyValue").setToNode("NodePosition").setToField("keyValue"))
            .addChildren(X3Dpackage.ROUTE().setFromNode("NodePosition").setFromField("value_changed").setToNode("transform").setToField("set_translation"))))
        .addChildren(X3Dpackage.ProtoDeclare().setName("cylinder")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            .addField(X3Dpackage.field().setName("positionA").setAccessType("inputOnly").setType("SFVec3f"))
            .addField(X3Dpackage.field().setName("positionB").setAccessType("inputOnly").setType("SFVec3f")))
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Shape()
              .setGeometry(X3Dpackage.Extrusion(setCreaseAngle = 0.785, setCrossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], setSpine = [0,-50,0,0,0,0,0,50,0]).setDEF("extrusion"))
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDiffuseColor([0,1,0]))))
            .addChildren(X3Dpackage.Script().setDEF("MoveCylinder")
              .addField(X3Dpackage.field().setName("spine").setAccessType("inputOutput").setType("MFVec3f").setValue("0 -50 0 0 0 0 0 50 0"))
              .addField(X3Dpackage.field().setName("set_endA").setAccessType("inputOnly").setType("SFVec3f"))
              .addField(X3Dpackage.field().setName("set_endB").setAccessType("inputOnly").setType("SFVec3f"))
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("set_endA").setProtoField("positionA"))
                .addConnect(X3Dpackage.connect().setNodeField("set_endB").setProtoField("positionB"))).setSourceCode(''' ecmascript:\n"+
"\n"+
"                function set_endA(value) {\n"+
"		    if (typeof spine === \"undefined\") {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([value, spine[1]]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_endB(value) {\n"+
"		    if (typeof spine === \"undefined\") {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([spine[0], value]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_spine(value) {\n"+
"		    Browser.print('\\n'+'\"');\n"+
"                    spine = value;\n"+
"                }\n"+
" ''')
)
            .addChildren(X3Dpackage.ROUTE().setFromNode("MoveCylinder").setFromField("spine").setToNode("extrusion").setToField("set_spine"))))
        .addChildren(X3Dpackage.Transform().setScale([0.1,0.1,0.1])
          .addChildren(X3Dpackage.ProtoInstance().setName("node").setDEF("nodeA")
            .addFieldValue(X3Dpackage.fieldValue().setName("position").setValue("-50 -50 -50")))
          .addChildren(X3Dpackage.ProtoInstance().setName("node").setDEF("nodeB")
            .addFieldValue(X3Dpackage.fieldValue().setName("position").setValue("50 50 50")))
          .addChildren(X3Dpackage.ProtoInstance().setName("cylinder").setDEF("linkA")
            .addFieldValue(X3Dpackage.fieldValue().setName("positionA").setValue("0 0 0"))
            .addFieldValue(X3Dpackage.fieldValue().setName("positionB").setValue("50 50 50"))))
        .addChildren(X3Dpackage.ROUTE().setFromNode("nodeA").setFromField("position").setToNode("linkA").setToField("positionA"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("nodeB").setFromField("position").setToNode("linkA").setToField("positionB"))))

