import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("x3dconnectorProto"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("Lost, Doug Sanden I think"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("manual"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/x3dconnectorProto.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("a generic proto to connect two objects")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Viewpoint().setPosition([0,0,5]).setDescription("Only Viewpoint").setOrientation([0,0,1,0]))
        .addChildren(X3Dpackage.Background().setSkyColor([0.4,0.4,0.4]))
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
                .addField(X3Dpackage.field().setName("keyValue").setAccessType("inputOutput").setType("MFVec3f").setValue("0 0 0 0 5 0")).setSourceCode('''\n"+
"ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}\n"+
"''')
)
              .addChildren(X3Dpackage.TimeSensor().setDEF("CL1").setCycleInterval(3).setLoop(True))
              .addChildren(X3Dpackage.ROUTE().setFromNode("CL1").setFromField("cycleTime").setToNode("MB1").setToField("set_location"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("CL1").setFromField("fraction_changed").setToNode("PI1").setToField("set_fraction"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("MB1").setFromField("keyValue").setToNode("PI1").setToField("keyValue"))
              .addChildren(X3Dpackage.ROUTE().setFromNode("PI1").setFromField("value_changed").setToNode("node").setToField("set_translation")))))
        .addChildren(X3Dpackage.ProtoDeclare().setName("x3dconnector")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("startnode").setType("SFNode"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("endnode").setType("SFNode"))
            .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_startpoint").setType("SFVec3f"))
            .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_endpoint").setType("SFVec3f")))
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Group()
              .addChildren(X3Dpackage.Transform().setDEF("trans").setTranslation([0,0,0])
                .addChildren(X3Dpackage.Transform().setDEF("rotscale")
                  .addChildren(X3Dpackage.Shape()
                    .setAppearance(X3Dpackage.Appearance()
                      .setMaterial(X3Dpackage.Material().setDiffuseColor([0.2,0.7,0.7]).setTransparency(.5)))
                    .setGeometry(X3Dpackage.Cylinder(setRadius = .05)))))
              .addChildren(X3Dpackage.Script().setDEF("S1")
                .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("startnode").setType("SFNode"))
                .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("endnode").setType("SFNode"))
                .addField(X3Dpackage.field().setAccessType("inputOutput").setName("position").setType("SFNode")
                  .addChildren(X3Dpackage.Transform().setUSE("trans")))
                .addField(X3Dpackage.field().setAccessType("inputOutput").setName("rotscale").setType("SFNode")
                  .addChildren(X3Dpackage.Transform().setUSE("rotscale")))
                .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_startpoint").setType("SFVec3f"))
                .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_endpoint").setType("SFVec3f"))
                .setIS(X3Dpackage.IS()
                  .addConnect(X3Dpackage.connect().setNodeField("startnode").setProtoField("startnode"))
                  .addConnect(X3Dpackage.connect().setNodeField("endnode").setProtoField("endnode"))
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
"            ''')
))))
        .addChildren(X3Dpackage.ProtoInstance().setDEF("G1").setName("point"))
        .addChildren(X3Dpackage.ProtoInstance().setDEF("G2").setName("point"))
        .addChildren(X3Dpackage.ProtoInstance().setName("x3dconnector").setDEF("connector1")
          .addFieldValue(X3Dpackage.fieldValue().setName("startnode")
            .addChildren(X3Dpackage.ProtoInstance().setUSE("G1")))
          .addFieldValue(X3Dpackage.fieldValue().setName("endnode")
            .addChildren(X3Dpackage.ProtoInstance().setUSE("G2")))
          .addFieldValue(X3Dpackage.fieldValue().setName("set_startpoint"))
          .addFieldValue(X3Dpackage.fieldValue().setName("set_endpoint")))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G1").setFromField("translation").setToNode("connector1").setToField("set_startpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G2").setFromField("translation").setToNode("connector1").setToField("set_endpoint"))))

