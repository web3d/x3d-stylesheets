from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    component2 = component(name="EnvironmentalEffects", level=1), 
    component3 = component(name="EnvironmentalEffects", level=3), 
    component4 = component(name="Shaders", level=1), 
    component5 = component(name="CubeMapTexturing", level=1), 
    meta6 = meta(name="title", content="ball.x3d"), 
    meta7 = meta(name="creator", content="John Carlson"), 
    meta8 = meta(name="generator", content="manual"), 
    meta9 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/ball.x3d"), 
    meta10 = meta(name="description", content="a prismatic sphere")), 
   Scene11 = Scene(    NavigationInfo12 = NavigationInfo(type=["ANY","EXAMINE","FLY","LOOKAT"]), 
    Viewpoint13 = Viewpoint(description="Tour Views"), 
    Background14 = Background(backUrl=["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"], bottomUrl=["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"], frontUrl=["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"], leftUrl=["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"], rightUrl=["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"], topUrl=["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]), 
    Transform15 = Transform(     Shape16 = Shape(      Sphere17 = Sphere(), 
      Appearance18 = Appearance(       Material19 = Material(diffuseColor=[0.7,0.7,0.7], specularColor=[0.5,0.5,0.5]), 
       ComposedCubeMapTexture20 = ComposedCubeMapTexture(DEF="texture",         ImageTexture21 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]), 
        ImageTexture22 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]), 
        ImageTexture23 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]), 
        ImageTexture24 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]), 
        ImageTexture25 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]), 
        ImageTexture26 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])),        #
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

       ComposedShader27 = ComposedShader(language="GLSL",         field28 = field(name="chromaticDispertion", accessType="inputOutput", type="SFVec3f", value="0.98 1 1.033"), 
        field29 = field(name="cube", type="SFNode", accessType="inputOutput",          ComposedCubeMapTexture30 = ComposedCubeMapTexture(USE="texture")), 
        field31 = field(name="bias", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field32 = field(name="scale", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field33 = field(name="power", accessType="inputOutput", type="SFFloat", value="2"), 
        ShaderPart34 = ShaderPart(url=["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"], type="VERTEX"), 
        ShaderPart35 = ShaderPart(DEF="common", url=["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"], type="FRAGMENT")), 
       ComposedShader36 = ComposedShader(language="GLSL",         field37 = field(name="chromaticDispertion", accessType="initializeOnly", type="SFVec3f", value="0.98 1 1.033"), 
        field38 = field(name="cube", type="SFNode", accessType="initializeOnly",          ComposedCubeMapTexture39 = ComposedCubeMapTexture(USE="texture")), 
        field40 = field(name="bias", accessType="initializeOnly", type="SFFloat", value="0.5"), 
        field41 = field(name="scale", accessType="initializeOnly", type="SFFloat", value="0.5"), 
        field42 = field(name="power", accessType="initializeOnly", type="SFFloat", value="2"), 
        ShaderPart43 = ShaderPart(url=["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"], type="VERTEX"), 
        ShaderPart44 = ShaderPart(USE="common")))))))
