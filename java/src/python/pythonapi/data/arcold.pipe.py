import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("arc.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("manual"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/arc.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("an attempt to implement an arc in a graph")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Viewpoint().setPosition([0,0,5]).setOrientation([0,0,1,0]).setDescription("a moving graph"))
        .addChildren(X3Dpackage.Background().setSkyColor([0.4,0.4,0.4]))
        .addChildren(X3Dpackage.Transform().setDEF("trans1")
          .addChildren(X3Dpackage.Transform().setDEF("rotscale1")
            .addChildren(X3Dpackage.Shape()
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDiffuseColor([0.2,0.7,0.7])))
              .setGeometry(X3Dpackage.Cylinder(setRadius = 0.1)))))
        .addChildren(X3Dpackage.Transform().setDEF("trans2")
          .addChildren(X3Dpackage.Transform().setDEF("rotscale2")
            .addChildren(X3Dpackage.Shape()
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDiffuseColor([0.2,0.7,0.7])))
              .setGeometry(X3Dpackage.Cylinder(setRadius = 0.1)))))
        .addChildren(X3Dpackage.Transform().setDEF("trans3")
          .addChildren(X3Dpackage.Transform().setDEF("rotscale3")
            .addChildren(X3Dpackage.Shape()
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDiffuseColor([0.2,0.7,0.7])))
              .setGeometry(X3Dpackage.Cylinder(setRadius = 0.1)))))
        .addChildren(X3Dpackage.ProtoDeclare().setName("point")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("translation").setType("SFVec3f").setValue("0 0 0")))
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Transform().setDEF("node")
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("translation").setProtoField("translation")))
              .addChildren(X3Dpackage.Shape()
                .setGeometry(X3Dpackage.Sphere(setRadius = 0.1))
                .setAppearance(X3Dpackage.Appearance()
                  .setMaterial(X3Dpackage.Material().setDiffuseColor([1,0,0]))))
              .addChildren(X3Dpackage.PositionInterpolator().setDEF("PI1").setKey([0,1]).setKeyValue([0,0,0,0,5,0]))
              .addChildren(X3Dpackage.Script().setDEF("MB1")
                .addField(X3Dpackage.field().setName("translation").setAccessType("inputOutput").setType("SFVec3f").setValue("50 50 0"))
                .addField(X3Dpackage.field().setName("old").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
                .addField(X3Dpackage.field().setName("set_location").setAccessType("inputOnly").setType("SFTime"))
                .addField(X3Dpackage.field().setName("keyValue").setAccessType("outputOnly").setType("MFVec3f")).setSourceCode('''\n"+
"ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(translation);\n"+
"		}\n"+
"''')
)
              .addChildren(X3Dpackage.TimeSensor().setDEF("CL1").setCycleInterval(3).setLoop(True))
              .addChildren(X3Dpackage.ROUTE().setFromNode("CL1").setFromField("cycleTime").setToNode("MB1").setToField("set_location"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("CL1").setFromField("fraction_changed").setToNode("PI1").setToField("set_fraction"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("MB1").setFromField("keyValue").setToNode("PI1").setToField("keyValue"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("PI1").setFromField("value_changed").setToNode("node").setToField("set_translation")))))
        # from doug sanden 

        .addChildren(X3Dpackage.ProtoDeclare().setName("x3dconnector")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("startnode").setType("SFNode"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("endnode").setType("SFNode"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("transnode").setType("SFNode"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("rotscalenode").setType("SFNode"))
            .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_startpoint").setType("SFVec3f"))
            .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_endpoint").setType("SFVec3f")))
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Script().setDEF("S1")
              .addField(X3Dpackage.field().setAccessType("inputOutput").setName("startnode").setType("SFNode"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setName("endnode").setType("SFNode"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setName("transnode").setType("SFNode"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setName("rotscalenode").setType("SFNode"))
              .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_startpoint").setType("SFVec3f"))
              .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_endpoint").setType("SFVec3f"))
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("startnode").setProtoField("startnode"))
                .addConnect(X3Dpackage.connect().setNodeField("endnode").setProtoField("endnode"))
                .addConnect(X3Dpackage.connect().setNodeField("transnode").setProtoField("transnode"))
                .addConnect(X3Dpackage.connect().setNodeField("rotscalenode").setProtoField("rotscalenode"))
                .addConnect(X3Dpackage.connect().setNodeField("set_startpoint").setProtoField("set_startpoint"))
                .addConnect(X3Dpackage.connect().setNodeField("set_endpoint").setProtoField("set_endpoint"))).setSourceCode('''ecmascript:\n"+
"        function recompute(startpoint,endpoint){\n"+
"	    if (typeof endpoint === 'undefined') {\n"+
"		return;\n"+
"	    }\n"+
"            var dif = endpoint.subtract(startpoint);\n"+
"            var dist = dif.length()*0.5;\n"+
"            var dif2 = dif.multiply(0.5);\n"+
"            var norm = dif.normalize();\n"+
"            var transl = startpoint.add(dif2);\n"+
"	    if (typeof Quaternion !== 'undefined') {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new Quaternion.rotateFromTo(new SFVec3f(0.0,1.0,0.0), norm)\n"+
"		    };\n"+
"	    } else {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new SFRotation(new SFVec3f(0.0,1.0,0.0),norm)\n"+
"		    };\n"+
"	    }\n"+
"	}\n"+
"	function recompute_and_route(startpoint, endpoint) {\n"+
"		var trafo = recompute(startpoint, endpoint);\n"+
"		if (typeof trafo !== 'undefined') {\n"+
"			transnode.translation = trafo.translation;\n"+
"			rotscalenode.rotation = trafo.rotation;\n"+
"			rotscalenode.scale = trafo.scale;\n"+
"		} else {\n"+
"			Browser.print(\"recompute returned undefined\");\n"+
"		}\n"+
"	}\n"+
"        function initialize(){\n"+
"            recompute_and_route(startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_startpoint(val,t){\n"+
"            recompute_and_route(val || startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_endpoint(val,t){\n"+
"            recompute_and_route(startnode.translation,val || endnode.translation);\n"+
"        }\n"+
"''')
)))
        .addChildren(X3Dpackage.ProtoInstance().setDEF("G1").setName("point"))
        .addChildren(X3Dpackage.ProtoInstance().setDEF("G2").setName("point"))
        .addChildren(X3Dpackage.ProtoInstance().setDEF("G3").setName("point"))
        .addChildren(X3Dpackage.ProtoInstance().setDEF("G4").setName("point"))
        .addChildren(X3Dpackage.ProtoInstance().setName("x3dconnector").setDEF("connector1")
          .addFieldValue(X3Dpackage.fieldValue().setName("startnode")
            .addChildren(X3Dpackage.ProtoInstance().setUSE("G1")))
          .addFieldValue(X3Dpackage.fieldValue().setName("endnode")
            .addChildren(X3Dpackage.ProtoInstance().setUSE("G2")))
          .addFieldValue(X3Dpackage.fieldValue().setName("transnode")
            .addChildren(X3Dpackage.Transform().setUSE("trans1")))
          .addFieldValue(X3Dpackage.fieldValue().setName("rotscalenode")
            .addChildren(X3Dpackage.Transform().setUSE("rotscale1"))))
        .addChildren(X3Dpackage.ProtoInstance().setName("x3dconnector").setDEF("connector2")
          .addFieldValue(X3Dpackage.fieldValue().setName("startnode")
            .addChildren(X3Dpackage.ProtoInstance().setUSE("G1")))
          .addFieldValue(X3Dpackage.fieldValue().setName("endnode")
            .addChildren(X3Dpackage.ProtoInstance().setUSE("G3")))
          .addFieldValue(X3Dpackage.fieldValue().setName("transnode")
            .addChildren(X3Dpackage.Transform().setUSE("trans2")))
          .addFieldValue(X3Dpackage.fieldValue().setName("rotscalenode")
            .addChildren(X3Dpackage.Transform().setUSE("rotscale2"))))
        .addChildren(X3Dpackage.ProtoInstance().setName("x3dconnector").setDEF("connector3")
          .addFieldValue(X3Dpackage.fieldValue().setName("startnode")
            .addChildren(X3Dpackage.ProtoInstance().setUSE("G1")))
          .addFieldValue(X3Dpackage.fieldValue().setName("endnode")
            .addChildren(X3Dpackage.ProtoInstance().setUSE("G4")))
          .addFieldValue(X3Dpackage.fieldValue().setName("transnode")
            .addChildren(X3Dpackage.Transform().setUSE("trans3")))
          .addFieldValue(X3Dpackage.fieldValue().setName("rotscalenode")
            .addChildren(X3Dpackage.Transform().setUSE("rotscale3"))))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G1").setFromField("translation_changed").setToNode("connector1").setToField("set_startpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G2").setFromField("translation_changed").setToNode("connector1").setToField("set_endpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G1").setFromField("translation_changed").setToNode("connector2").setToField("set_startpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G3").setFromField("translation_changed").setToNode("connector2").setToField("set_endpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G1").setFromField("translation_changed").setToNode("connector3").setToField("set_startpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G4").setFromField("translation_changed").setToNode("connector3").setToField("set_endpoint"))))

