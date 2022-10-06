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
        .addChildren(X3Dpackage.Transform().setDEF("G1")
          .addChildren(X3Dpackage.Shape()
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([0.7,0.2,0.2])))
            .setGeometry(X3Dpackage.Sphere(setRadius = .1)))
          .addChildren(X3Dpackage.PlaneSensor().setDescription("Grab to move").setDEF("PS1"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("PS1").setFromField("translation_changed").setToNode("G1").setToField("set_translation")))
        .addChildren(X3Dpackage.Transform().setDEF("G2").setTranslation([1,-1,.01])
          .addChildren(X3Dpackage.Shape()
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([0.2,0.7,0.2])))
            .setGeometry(X3Dpackage.Sphere(setRadius = .1)))
          .addChildren(X3Dpackage.PlaneSensor().setDescription("Grab to move").setOffset([1,-1,.01]).setDEF("PS2"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("PS2").setFromField("translation_changed").setToNode("G2").setToField("set_translation")))
        .addChildren(X3Dpackage.Transform().setDEF("G3").setTranslation([1,1,.01])
          .addChildren(X3Dpackage.Shape()
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([0.2,0.7,0.2])))
            .setGeometry(X3Dpackage.Sphere(setRadius = .1)))
          .addChildren(X3Dpackage.PlaneSensor().setDescription("Grab to move").setOffset([1,1,.01]).setDEF("PS3"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("PS3").setFromField("translation_changed").setToNode("G3").setToField("set_translation")))
        .addChildren(X3Dpackage.Transform().setDEF("G4").setTranslation([-1,1,.01])
          .addChildren(X3Dpackage.Shape()
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([0.2,0.7,0.2])))
            .setGeometry(X3Dpackage.Sphere(setRadius = .1)))
          .addChildren(X3Dpackage.PlaneSensor().setDescription("Grab to move").setOffset([-1,1,.01]).setDEF("PS4"))
          .addChildren(X3Dpackage.ROUTE().setFromNode("PS4").setFromField("translation_changed").setToNode("G4").setToField("set_translation")))
        .addChildren(X3Dpackage.Transform().setDEF("transC1")
          .addChildren(X3Dpackage.Transform().setDEF("rotscaleC1")
            .addChildren(X3Dpackage.Shape()
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDiffuseColor([0.2,0.7,0.7]).setTransparency(.5)))
              .setGeometry(X3Dpackage.Cylinder(setRadius = .05)))))
        .addChildren(X3Dpackage.Transform().setDEF("transC2")
          .addChildren(X3Dpackage.Transform().setDEF("rotscaleC2")
            .addChildren(X3Dpackage.Shape()
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDiffuseColor([0.2,0.7,0.7]).setTransparency(.5)))
              .setGeometry(X3Dpackage.Cylinder(setRadius = .05)))))
        .addChildren(X3Dpackage.Transform().setDEF("transC3")
          .addChildren(X3Dpackage.Transform().setDEF("rotscaleC3")
            .addChildren(X3Dpackage.Shape()
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDiffuseColor([0.2,0.7,0.7]).setTransparency(.5)))
              .setGeometry(X3Dpackage.Cylinder(setRadius = .05)))))
        .addChildren(X3Dpackage.ProtoDeclare().setName("x3dconnector")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("startnode").setType("SFNode"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("endnode").setType("SFNode"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("transnode").setType("SFNode"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("rotscalenode").setType("SFNode"))
            .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_startpoint").setType("SFVec3f"))
            .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_endpoint").setType("SFVec3f")))
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Script().setDEF("S1")
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("startnode").setType("SFNode"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("endnode").setType("SFNode"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("transnode").setType("SFNode"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("rotscalenode").setType("SFNode"))
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
"	      var trafo = recompute(startpoint, endpoint);\n"+
"	      transnode.translation = trafo.translation;\n"+
"	      rotscalenode.rotation = trafo.rotation;\n"+
"	      rotscalenode.scale = trafo.scale;\n"+
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
)))
        .addChildren(X3Dpackage.ProtoInstance().setName("x3dconnector").setDEF("connector1")
          .addFieldValue(X3Dpackage.fieldValue().setName("startnode")
            .addChildren(X3Dpackage.Transform().setUSE("G1")))
          .addFieldValue(X3Dpackage.fieldValue().setName("endnode")
            .addChildren(X3Dpackage.Transform().setUSE("G2")))
          .addFieldValue(X3Dpackage.fieldValue().setName("transnode")
            .addChildren(X3Dpackage.Transform().setUSE("transC1")))
          .addFieldValue(X3Dpackage.fieldValue().setName("rotscalenode")
            .addChildren(X3Dpackage.Transform().setUSE("rotscaleC1")))
          .addFieldValue(X3Dpackage.fieldValue().setName("set_startpoint"))
          .addFieldValue(X3Dpackage.fieldValue().setName("set_endpoint")))
        .addChildren(X3Dpackage.ProtoInstance().setName("x3dconnector").setDEF("connector2")
          .addFieldValue(X3Dpackage.fieldValue().setName("startnode")
            .addChildren(X3Dpackage.Transform().setUSE("G1")))
          .addFieldValue(X3Dpackage.fieldValue().setName("endnode")
            .addChildren(X3Dpackage.Transform().setUSE("G3")))
          .addFieldValue(X3Dpackage.fieldValue().setName("transnode")
            .addChildren(X3Dpackage.Transform().setUSE("transC2")))
          .addFieldValue(X3Dpackage.fieldValue().setName("rotscalenode")
            .addChildren(X3Dpackage.Transform().setUSE("rotscaleC2")))
          .addFieldValue(X3Dpackage.fieldValue().setName("set_startpoint"))
          .addFieldValue(X3Dpackage.fieldValue().setName("set_endpoint")))
        .addChildren(X3Dpackage.ProtoInstance().setName("x3dconnector").setDEF("connector3")
          .addFieldValue(X3Dpackage.fieldValue().setName("startnode")
            .addChildren(X3Dpackage.Transform().setUSE("G1")))
          .addFieldValue(X3Dpackage.fieldValue().setName("endnode")
            .addChildren(X3Dpackage.Transform().setUSE("G4")))
          .addFieldValue(X3Dpackage.fieldValue().setName("transnode")
            .addChildren(X3Dpackage.Transform().setUSE("transC3")))
          .addFieldValue(X3Dpackage.fieldValue().setName("rotscalenode")
            .addChildren(X3Dpackage.Transform().setUSE("rotscaleC3")))
          .addFieldValue(X3Dpackage.fieldValue().setName("set_startpoint"))
          .addFieldValue(X3Dpackage.fieldValue().setName("set_endpoint")))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G1").setFromField("translation_changed").setToNode("connector1").setToField("set_startpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G2").setFromField("translation_changed").setToNode("connector1").setToField("set_endpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G1").setFromField("translation_changed").setToNode("connector2").setToField("set_startpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G3").setFromField("translation_changed").setToNode("connector2").setToField("set_endpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G1").setFromField("translation_changed").setToNode("connector3").setToField("set_startpoint"))
        .addChildren(X3Dpackage.ROUTE().setFromNode("G4").setFromField("translation_changed").setToNode("connector3").setToField("set_endpoint"))))

