from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    component2 = component(name="Shaders", level=1), 
    component3 = component(name="CubeMapTexturing", level=1), 
    meta4 = meta(name="title", content="bub.x3d"), 
    meta5 = meta(name="creator", content="John Carlson"), 
    meta6 = meta(name="description", content="3 prismatic spheres"), 
    meta7 = meta(name="generator", content="X3D-Edit, https://savage.nps.edu/X3D-Edit"), 
    meta8 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/bub.x3d")), 
   Scene9 = Scene(    NavigationInfo10 = NavigationInfo(type=["EXAMINE","ANY"]), 
    Background11 = Background(backUrl=["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"], bottomUrl=["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"], frontUrl=["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"], leftUrl=["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"], rightUrl=["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"], topUrl=["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]), 
    Viewpoint12 = Viewpoint(position=[0,0,20], description="Look at the bubbles flying"), 
    ProtoDeclare13 = ProtoDeclare(name="Bubble",      ProtoBody14 = ProtoBody(      Transform15 = Transform(DEF="transform", translation=[0,0,0],        Shape16 = Shape(DEF="myShape",         Appearance17 = Appearance(         Material18 = Material(diffuseColor=[.7,.7,.7], specularColor=[.5,.5,.5]), 
         ComposedCubeMapTexture19 = ComposedCubeMapTexture(DEF="texture",           ImageTexture20 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]), 
          ImageTexture21 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]), 
          ImageTexture22 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]), 
          ImageTexture23 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]), 
          ImageTexture24 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]), 
          ImageTexture25 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])),          #
#					<ComposedShader DEF='gl' language=\"GLSL\">
#					  <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/>
#					  <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/>
#					  <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/>
#
#					  <ShaderPart url='\"../shaders/gl.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/gl.vs\"' type='VERTEX'></ShaderPart>
#					  <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart>
#					</ComposedShader>
#					<ComposedShader DEF='freewrl' language=\"GLSL\">
#					  <field name='fw_textureCoodGenType' type='SFInt32' accessType=\"inputOutput\" value='0'/>
#					  <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/>
#					  <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/>
#
#					  <ShaderPart url='\"../shaders/freewrl.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/freewrl.vs\"' type='VERTEX'></ShaderPart>
#					  <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart>
#					</ComposedShader>
#					

         ComposedShader26 = ComposedShader(DEF="x3dom", language="GLSL",           field27 = field(name="cube", type="SFInt32", accessType="inputOutput", value="0"), 
          field28 = field(name="chromaticDispertion", type="SFVec3f", accessType="inputOutput", value="0.98 1.0 1.033"), 
          field29 = field(name="bias", type="SFFloat", accessType="inputOutput", value="0.5"), 
          field30 = field(name="scale", type="SFFloat", accessType="inputOutput", value="0.5"), 
          field31 = field(name="power", type="SFFloat", accessType="inputOutput", value="2.0"), 
          ShaderPart32 = ShaderPart(url=["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"], type="VERTEX"), 
          ShaderPart33 = ShaderPart(url=["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"], type="FRAGMENT")),          #
#					<ComposedShader DEF='instant' language=\"GLSL\">
#					  <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/>
#					  <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/>
#					  <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/>
#
#                              <ShaderPart url='\"../shaders/instant.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/instant.vs\"' type='VERTEX'></ShaderPart>
#                              <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart>
#                            </ComposedShader>
#                            

         ComposedShader34 = ComposedShader(DEF="cobweb", language="GLSL",           field35 = field(name="cube", type="SFNode", accessType="inputOutput",            ComposedCubeMapTexture36 = ComposedCubeMapTexture(USE="texture")), 
          field37 = field(name="chromaticDispertion", type="SFVec3f", accessType="inputOutput", value="0.98 1.0 1.033"), 
          field38 = field(name="bias", type="SFFloat", accessType="inputOutput", value="0.5"), 
          field39 = field(name="scale", type="SFFloat", accessType="inputOutput", value="0.5"), 
          field40 = field(name="power", type="SFFloat", accessType="inputOutput", value="2.0"), 
          ShaderPart41 = ShaderPart(url=["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"], type="VERTEX"), 
          ShaderPart42 = ShaderPart(url=["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc.fs"], type="FRAGMENT"))), 
        Sphere43 = Sphere())), 
      Script44 = Script(DEF="Bounce",        field45 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
       field46 = field(name="velocity", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
       field47 = field(name="set_fraction", accessType="inputOnly", type="SFTime"),        sourceCode = '''ecmascript:\n"+
"			function initialize() {\n"+
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
"			    if (Math.abs(translation.x) > 10) {\n"+
"				initialize();\n"+
"			    } else if (Math.abs(translation.y) > 10) {\n"+
"				initialize();\n"+
"			    } else if (Math.abs(translation.z) > 10) {\n"+
"				initialize();\n"+
"			    } else {\n"+
"				velocity.x += Math.random() * 0.2 - 0.1;\n"+
"				velocity.y += Math.random() * 0.2 - 0.1;\n"+
"				velocity.z += Math.random() * 0.2 - 0.1;\n"+
"			    }\n"+
"			}\n"+
"               ''', ), 
      TimeSensor48 = TimeSensor(DEF="TourTime", cycleInterval=0.150, loop=True), 
      ROUTE49 = ROUTE(fromNode="TourTime", fromField="cycleTime", toNode="Bounce", toField="set_fraction"), 
      ROUTE50 = ROUTE(fromNode="Bounce", fromField="translation_changed", toNode="transform", toField="set_translation"))), 
    ProtoInstance51 = ProtoInstance(name="Bubble"), 
    ProtoInstance52 = ProtoInstance(name="Bubble"), 
    ProtoInstance53 = ProtoInstance(name="Bubble")))
