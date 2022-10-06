import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addComponent(X3Dpackage.component().setName("EnvironmentalEffects").setLevel(1))
        .addComponent(X3Dpackage.component().setName("EnvironmentalEffects").setLevel(3))
        .addComponent(X3Dpackage.component().setName("Shaders").setLevel(1))
        .addComponent(X3Dpackage.component().setName("CubeMapTexturing").setLevel(1))
        .addMeta(X3Dpackage.meta().setName("title").setContent("ball.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("manual"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/ball.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("a prismatic sphere")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.NavigationInfo().setType(["ANY","EXAMINE","FLY","LOOKAT"]))
        .addChildren(X3Dpackage.Viewpoint().setDescription("Tour Views"))
        .addChildren(X3Dpackage.Background().setBackUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]).setBottomUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]).setFrontUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]).setLeftUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]).setRightUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]).setTopUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]))
        .addChildren(X3Dpackage.Transform()
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Sphere())
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([0.7,0.7,0.7]).setSpecularColor([0.5,0.5,0.5]))
              .setTexture(X3Dpackage.ComposedCubeMapTexture().setDEF("texture")
                .setBack(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]))
                .setBottom(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]))
                .setFront(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]))
                .setLeft(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]))
                .setRight(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]))
                .setTop(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])))
              #
#                    <ProgramShader DEF='ProgramShader' containerField='shaders' language='GLSL'>
#                        <ShaderProgram url='\"../shaders/freewrl.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/freewrl.vs\"' containerField='programs' type='VERTEX'>
#                        <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'/>
#                        <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'/>
#                        <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'/>
#                        <field name='power' accessType='initializeOnly' type='SFFloat' value='2'/>
#                        </ShaderProgram>
#                        <ShaderProgram url='\"../shaders/freewrl.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/freewrl.fs\"' containerField='programs' type='FRAGMENT'/>
#		    </ProgramShader>
#		

              #
#                <ComposedShader language='GLSL'>
#		  <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'></field>
#		  <field name='fw_Texture_unit0' type='SFNode' accessType=\"initializeOnly\">
#			<ComposedCubeMapTexture USE=\"texture\"></ComposedCubeMapTexture>
#		  </field>
#		  <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'></field>
#		  <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'></field>
#		  <field name='power' accessType='initializeOnly' type='SFFloat' value='2'></field>
#		  <ShaderPart url='\"../shaders/contact.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/contact.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart>
#		  <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart>
#                </ComposedShader>
#		

              #
#                <ComposedShader language='GLSL'>
#		  <field name='chromaticDispertion' accessType='inputOutput' type='SFVec3f' value='0.98 1 1.033'></field>
#		  <field name='cube' type='SFNode' accessType=\"inputOutput\">
#			<ComposedCubeMapTexture USE=\"texture\"></ComposedCubeMapTexture>
#		  </field>
#		  <field name='bias' accessType='inputOutput' type='SFFloat' value='0.5'></field>
#		  <field name='scale' accessType='inputOutput' type='SFFloat' value='0.5'></field>
#		  <field name='power' accessType='inputOutput' type='SFFloat' value='2'></field>
#		  <ShaderPart url='\"../shaders/octaga.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/octaga.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart>
#		  <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart>
#                </ComposedShader>
#		

              #
#                <ComposedShader language='GLSL'>
#		  <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'></field>
#		  <field name='cube' accessType='initializeOnly' type='SFInt32' value='0'></field>
#		  <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'></field>
#		  <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'></field>
#		  <field name='power' accessType='initializeOnly' type='SFFloat' value='2'></field>
#		  <ShaderPart url='\"../shaders/instant.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/instant.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart>
#		  <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart>
#                </ComposedShader>
#		

              #
#		

              .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL")
                .addField(X3Dpackage.field().setName("chromaticDispertion").setAccessType("inputOutput").setType("SFVec3f").setValue("0.98 1 1.033"))
                .addField(X3Dpackage.field().setName("cube").setType("SFNode").setAccessType("inputOutput")
                  .addChildren(X3Dpackage.ComposedCubeMapTexture().setUSE("texture")))
                .addField(X3Dpackage.field().setName("bias").setAccessType("inputOutput").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("scale").setAccessType("inputOutput").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("power").setAccessType("inputOutput").setType("SFFloat").setValue("2"))
                .setParts(X3Dpackage.ShaderPart().setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]).setType("VERTEX"))
                .setParts(X3Dpackage.ShaderPart().setDEF("common").setUrl(["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"]).setType("FRAGMENT")))
              .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL")
                .addField(X3Dpackage.field().setName("chromaticDispertion").setAccessType("initializeOnly").setType("SFVec3f").setValue("0.98 1 1.033"))
                .addField(X3Dpackage.field().setName("cube").setType("SFNode").setAccessType("initializeOnly")
                  .addChildren(X3Dpackage.ComposedCubeMapTexture().setUSE("texture")))
                .addField(X3Dpackage.field().setName("bias").setAccessType("initializeOnly").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("scale").setAccessType("initializeOnly").setType("SFFloat").setValue("0.5"))
                .addField(X3Dpackage.field().setName("power").setAccessType("initializeOnly").setType("SFFloat").setValue("2"))
                .setParts(X3Dpackage.ShaderPart().setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]).setType("VERTEX"))
                .addParts(X3Dpackage.ShaderPart().setUSE("common"))))))))

