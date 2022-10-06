from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

component2 = component()
component2.name = "EnvironmentalEffects"
component2.level = 1
head1.addComponent([component2])

component3 = component()
component3.name = "EnvironmentalEffects"
component3.level = 3
head1.addComponent([component3])

component4 = component()
component4.name = "Shaders"
component4.level = 1
head1.addComponent([component4])

component5 = component()
component5.name = "CubeMapTexturing"
component5.level = 1
head1.addComponent([component5])

meta6 = meta()
meta6.name = "title"
meta6.content = "ball.x3d"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "creator"
meta7.content = "John Carlson"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "generator"
meta8.content = "manual"
head1.addMeta([meta8])

meta9 = meta()
meta9.name = "identifier"
meta9.content = "https://coderextreme.net/X3DJSONLD/ball.x3d"
head1.addMeta([meta9])

meta10 = meta()
meta10.name = "description"
meta10.content = "a prismatic sphere"
head1.addMeta([meta10])
X3D0.head = head1

Scene11 = Scene()

NavigationInfo12 = NavigationInfo()
NavigationInfo12.type = ["ANY","EXAMINE","FLY","LOOKAT"]
Scene11.addChildren([NavigationInfo12])

Viewpoint13 = Viewpoint()
Viewpoint13.description = "Tour Views"
Scene11.addChildren([Viewpoint13])

Background14 = Background()
Background14.backUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]
Background14.bottomUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]
Background14.frontUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]
Background14.leftUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]
Background14.rightUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]
Background14.topUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]
Scene11.addChildren([Background14])

Transform15 = Transform()

Shape16 = Shape()

Sphere17 = Sphere()
Shape16.geometry = Sphere17

Appearance18 = Appearance()

Material19 = Material()
Material19.diffuseColor = [0.7,0.7,0.7]
Material19.specularColor = [0.5,0.5,0.5]
Appearance18.material = Material19

ComposedCubeMapTexture20 = ComposedCubeMapTexture()
ComposedCubeMapTexture20.DEF = "texture"

ImageTexture21 = ImageTexture()
ImageTexture21.url = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]
ComposedCubeMapTexture20.back = ImageTexture21

ImageTexture22 = ImageTexture()
ImageTexture22.url = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]
ComposedCubeMapTexture20.bottom = ImageTexture22

ImageTexture23 = ImageTexture()
ImageTexture23.url = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]
ComposedCubeMapTexture20.front = ImageTexture23

ImageTexture24 = ImageTexture()
ImageTexture24.url = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]
ComposedCubeMapTexture20.left = ImageTexture24

ImageTexture25 = ImageTexture()
ImageTexture25.url = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]
ComposedCubeMapTexture20.right = ImageTexture25

ImageTexture26 = ImageTexture()
ImageTexture26.url = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]
ComposedCubeMapTexture20.top = ImageTexture26
Appearance18.texture = ComposedCubeMapTexture20
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

ComposedShader27 = ComposedShader(language = "GLSL")

field28 = field()
field28.name = "chromaticDispertion"
field28.accessType = "inputOutput"
field28.type = "SFVec3f"
field28.value = "0.98 1 1.033"
ComposedShader27.addField([field28])

field29 = field()
field29.name = "cube"
field29.type = "SFNode"
field29.accessType = "inputOutput"

ComposedCubeMapTexture30 = ComposedCubeMapTexture()
ComposedCubeMapTexture30.USE = "texture"
field29.addChildren([ComposedCubeMapTexture30])
ComposedShader27.addField([field29])

field31 = field()
field31.name = "bias"
field31.accessType = "inputOutput"
field31.type = "SFFloat"
field31.value = "0.5"
ComposedShader27.addField([field31])

field32 = field()
field32.name = "scale"
field32.accessType = "inputOutput"
field32.type = "SFFloat"
field32.value = "0.5"
ComposedShader27.addField([field32])

field33 = field()
field33.name = "power"
field33.accessType = "inputOutput"
field33.type = "SFFloat"
field33.value = "2"
ComposedShader27.addField([field33])

ShaderPart34 = ShaderPart()
ShaderPart34.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]
ShaderPart34.type = "VERTEX"
ComposedShader27.parts = ShaderPart34

ShaderPart35 = ShaderPart()
ShaderPart35.DEF = "common"
ShaderPart35.url = ["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"]
ShaderPart35.type = "FRAGMENT"
ComposedShader27.parts = ShaderPart35
Appearance18.addShaders([ComposedShader27])

ComposedShader36 = ComposedShader(language = "GLSL")

field37 = field()
field37.name = "chromaticDispertion"
field37.accessType = "initializeOnly"
field37.type = "SFVec3f"
field37.value = "0.98 1 1.033"
ComposedShader36.addField([field37])

field38 = field()
field38.name = "cube"
field38.type = "SFNode"
field38.accessType = "initializeOnly"

ComposedCubeMapTexture39 = ComposedCubeMapTexture()
ComposedCubeMapTexture39.USE = "texture"
field38.addChildren([ComposedCubeMapTexture39])
ComposedShader36.addField([field38])

field40 = field()
field40.name = "bias"
field40.accessType = "initializeOnly"
field40.type = "SFFloat"
field40.value = "0.5"
ComposedShader36.addField([field40])

field41 = field()
field41.name = "scale"
field41.accessType = "initializeOnly"
field41.type = "SFFloat"
field41.value = "0.5"
ComposedShader36.addField([field41])

field42 = field()
field42.name = "power"
field42.accessType = "initializeOnly"
field42.type = "SFFloat"
field42.value = "2"
ComposedShader36.addField([field42])

ShaderPart43 = ShaderPart()
ShaderPart43.url = ["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]
ShaderPart43.type = "VERTEX"
ComposedShader36.parts = ShaderPart43

ShaderPart44 = ShaderPart()
ShaderPart44.USE = "common"
ComposedShader36.addParts([ShaderPart44])
Appearance18.addShaders([ComposedShader36])
Shape16.appearance = Appearance18
Transform15.addChildren([Shape16])
Scene11.addChildren([Transform15])
X3D0.scene = Scene11
