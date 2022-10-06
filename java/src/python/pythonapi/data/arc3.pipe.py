import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("x3dconnectorProto"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("Lost, Doug Sanden I think"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("manual"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/x3dconnectorProto.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("a generic proto to connect two objects")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Viewpoint().setPosition([0,0,5]).setDescription("Only Viewpoint"))
        .addChildren(X3Dpackage.Background().setSkyColor([0.4,0.4,0.4]))
        .addChildren(X3Dpackage.Transform().setDEF("DECLpoint_G1_node").setTranslation([0,0,0])
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Sphere(setRadius = 0.1))
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([1,0,0]))))
          .addChildren(X3Dpackage.PositionInterpolator().setDEF("DECLpoint_G1_PI1").setKey([0,1]).setKeyValue([0,0,0,0,5,0]))
          .addChildren(X3Dpackage.Script().setDEF("DECLpoint_G1_MB1")
            .addField(X3Dpackage.field().setName("translation").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
            .addField(X3Dpackage.field().setName("old").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
            .addField(X3Dpackage.field().setName("set_location").setAccessType("inputOnly").setType("SFTime"))
            .addField(X3Dpackage.field().setName("keyValue").setAccessType("inputOutput").setType("MFVec3f").setValue("0 0 0 0 5 0")).setSourceCode('''ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}\n"+
"''')
)
          .addChildren(X3Dpackage.TimeSensor().setDEF("DECLpoint_G1_CL1").setCycleInterval(3).setLoop(True))
          .addChildren(X3Dpackage.ROUTE().setFromNode("DECLpoint_G1_CL1").setFromField("cycleTime").setToNode("DECLpoint_G1_MB1").setToField("set_location"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("DECLpoint_G1_CL1").setFromField("fraction_changed").setToNode("DECLpoint_G1_PI1").setToField("set_fraction"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("DECLpoint_G1_MB1").setFromField("keyValue").setToNode("DECLpoint_G1_PI1").setToField("keyValue"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("DECLpoint_G1_PI1").setFromField("value_changed").setToNode("DECLpoint_G1_node").setToField("set_translation")))
        .addChildren(X3Dpackage.Transform().setDEF("DECLpoint_G2_node").setTranslation([0,0,0])
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Sphere(setRadius = 0.1))
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([1,0,0]))))
          .addChildren(X3Dpackage.PositionInterpolator().setDEF("DECLpoint_G2_PI1").setKey([0,1]).setKeyValue([0,0,0,0,5,0]))
          .addChildren(X3Dpackage.Script().setDEF("DECLpoint_G2_MB1")
            .addField(X3Dpackage.field().setName("translation").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
            .addField(X3Dpackage.field().setName("old").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
            .addField(X3Dpackage.field().setName("set_location").setAccessType("inputOnly").setType("SFTime"))
            .addField(X3Dpackage.field().setName("keyValue").setAccessType("inputOutput").setType("MFVec3f").setValue("0 0 0 0 5 0")).setSourceCode('''ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}\n"+
"''')
)
          .addChildren(X3Dpackage.TimeSensor().setDEF("DECLpoint_G2_CL1").setCycleInterval(3).setLoop(True))
          .addChildren(X3Dpackage.ROUTE().setFromNode("DECLpoint_G2_CL1").setFromField("cycleTime").setToNode("DECLpoint_G2_MB1").setToField("set_location"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("DECLpoint_G2_CL1").setFromField("fraction_changed").setToNode("DECLpoint_G2_PI1").setToField("set_fraction"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("DECLpoint_G2_MB1").setFromField("keyValue").setToNode("DECLpoint_G2_PI1").setToField("keyValue"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("DECLpoint_G2_PI1").setFromField("value_changed").setToNode("DECLpoint_G2_node").setToField("set_translation")))
        .addChildren(X3Dpackage.Group()
          .addChildren(X3Dpackage.Transform().setDEF("DECLx3dconnector_connector1_trans")
            .addChildren(X3Dpackage.Transform().setDEF("DECLx3dconnector_connector1_rotscale")
              .addChildren(X3Dpackage.Shape()
                .setAppearance(X3Dpackage.Appearance()
                  .setMaterial(X3Dpackage.Material().setDiffuseColor([0.2,0.7,0.7]).setTransparency(0.5)))
                .setGeometry(X3Dpackage.Cylinder(setRadius = 0.05)))))
          .addChildren(X3Dpackage.Script().setDEF("DECLx3dconnector_connector1_S1")
            .addField(X3Dpackage.field().setName("startnode").setAccessType("initializeOnly").setType("SFNode")
              .addChildren(X3Dpackage.Group().setUSE("DECLpoint_G1_node")))
            .addField(X3Dpackage.field().setName("endnode").setAccessType("initializeOnly").setType("SFNode")
              .addChildren(X3Dpackage.Group().setUSE("DECLpoint_G2_node")))
            .addField(X3Dpackage.field().setName("position").setAccessType("inputOutput").setType("SFNode")
              .addChildren(X3Dpackage.Transform().setUSE("DECLx3dconnector_connector1_trans")))
            .addField(X3Dpackage.field().setName("rotscale").setAccessType("inputOutput").setType("SFNode")
              .addChildren(X3Dpackage.Transform().setUSE("DECLx3dconnector_connector1_rotscale")))
            .addField(X3Dpackage.field().setName("set_startpoint").setAccessType("inputOnly").setType("SFVec3f"))
            .addField(X3Dpackage.field().setName("set_endpoint").setAccessType("inputOnly").setType("SFVec3f")).setSourceCode('''ecmascript:\n"+
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
"	    } else if (typeof SFRotation !== 'undefined') {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new SFRotation(new SFVec3f(0.0,1.0,0.0),norm)\n"+
"		    };\n"+
"	    } else {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl\n"+
"		    };\n"+
"	    }\n"+
"	}\n"+
"	function recompute_and_route(startpoint, endpoint) {\n"+
"	      var trafo = recompute(startpoint, endpoint);\n"+
"	      position.translation = trafo.translation;\n"+
"	      rotscale.rotation = trafo.rotation;\n"+
"	      rotscale.scale = trafo.scale;\n"+
"	}\n"+
"        function initialize(){\n"+
"            recompute_and_route(startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_startpoint(val,t){\n"+
"            recompute_and_route(val,endnode.translation);\n"+
"        }\n"+
"        function set_endpoint(val,t){\n"+
"            recompute_and_route(startnode.translation,val);\n"+
"        }\n"+
"''')
))
        .addChildren(X3Dpackage.ROUTE().setFromNode("DECLpoint_G1_node").setFromField("translation").setToNode("DECLx3dconnector_connector1_S1").setToField("set_startpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("DECLpoint_G2_node").setFromField("translation").setToNode("DECLx3dconnector_connector1_S1").setToField("set_endpoint"))))

