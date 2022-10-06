from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

component2 = component()
component2.name = "Shaders"
component2.level = 1
head1.addComponent([component2])

component3 = component()
component3.name = "CubeMapTexturing"
component3.level = 1
head1.addComponent([component3])

meta4 = meta()
meta4.name = "title"
meta4.content = "geo.x3d"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "creator"
meta5.content = "John Carlson"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "generator"
meta6.content = "manual"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "identifier"
meta7.content = "https://coderextreme.net/X3DJSONLD/geo.x3d"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "description"
meta8.content = "a sphere"
head1.addMeta([meta8])
X3D0.head = head1

Scene9 = Scene()

NavigationInfo10 = NavigationInfo()
NavigationInfo10.type = ["ANY","EXAMINE","FLY","LOOKAT"]
Scene9.addChildren([NavigationInfo10])

Viewpoint11 = Viewpoint()
Viewpoint11.DEF = "Tour"
Viewpoint11.description = "Tour Views"
Scene9.addChildren([Viewpoint11])
#Viewpoint position='0 0 4' description='sphere in road'/

Background12 = Background()
Background12.backUrl = ["resources/images/bBK.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBK.png"]
Background12.bottomUrl = ["resources/images/bBT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBT.png"]
Background12.frontUrl = ["resources/images/bFR.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bFR.png"]
Background12.leftUrl = ["resources/images/bLF.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bLF.png"]
Background12.rightUrl = ["resources/images/bRT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bRT.png"]
Background12.topUrl = ["resources/images/bTP.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bTP.png"]
Scene9.addChildren([Background12])

Transform13 = Transform()

Shape14 = Shape()

Sphere15 = Sphere()
Shape14.geometry = Sphere15

Appearance16 = Appearance()

Material17 = Material()
Material17.diffuseColor = [0.7,0.7,0.7]
Material17.specularColor = [0.5,0.5,0.5]
Appearance16.material = Material17

ComposedCubeMapTexture18 = ComposedCubeMapTexture()
ComposedCubeMapTexture18.DEF = "texture"

ImageTexture19 = ImageTexture()
ImageTexture19.url = ["resources/images/bBK.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBK.png"]
ComposedCubeMapTexture18.back = ImageTexture19

ImageTexture20 = ImageTexture()
ImageTexture20.url = ["resources/images/bBT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBT.png"]
ComposedCubeMapTexture18.bottom = ImageTexture20

ImageTexture21 = ImageTexture()
ImageTexture21.url = ["resources/images/bFR.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bFR.png"]
ComposedCubeMapTexture18.front = ImageTexture21

ImageTexture22 = ImageTexture()
ImageTexture22.url = ["resources/images/bLF.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bLF.png"]
ComposedCubeMapTexture18.left = ImageTexture22

ImageTexture23 = ImageTexture()
ImageTexture23.url = ["resources/images/bRT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bRT.png"]
ComposedCubeMapTexture18.right = ImageTexture23

ImageTexture24 = ImageTexture()
ImageTexture24.url = ["resources/images/bTP.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bTP.png"]
ComposedCubeMapTexture18.top = ImageTexture24
Appearance16.texture = ComposedCubeMapTexture18

ComposedShader25 = ComposedShader(language = "GLSL")

field26 = field()
field26.name = "chromaticDispertion"
field26.accessType = "inputOutput"
field26.type = "SFVec3f"
field26.value = "0.98 1 1.033"
ComposedShader25.addField([field26])

field27 = field()
field27.name = "cube"
field27.type = "SFNode"
field27.accessType = "inputOutput"

ComposedCubeMapTexture28 = ComposedCubeMapTexture()
ComposedCubeMapTexture28.USE = "texture"
field27.addChildren([ComposedCubeMapTexture28])
ComposedShader25.addField([field27])

field29 = field()
field29.name = "bias"
field29.accessType = "inputOutput"
field29.type = "SFFloat"
field29.value = "0.5"
ComposedShader25.addField([field29])

field30 = field()
field30.name = "scale"
field30.accessType = "inputOutput"
field30.type = "SFFloat"
field30.value = "0.5"
ComposedShader25.addField([field30])

field31 = field()
field31.name = "power"
field31.accessType = "inputOutput"
field31.type = "SFFloat"
field31.value = "2"
ComposedShader25.addField([field31])

ShaderPart32 = ShaderPart()
ShaderPart32.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]
ShaderPart32.type = "VERTEX"
ComposedShader25.parts = ShaderPart32

ShaderPart33 = ShaderPart()
ShaderPart33.DEF = "common"
ShaderPart33.url = ["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"]
ShaderPart33.type = "FRAGMENT"
ComposedShader25.parts = ShaderPart33
Appearance16.addShaders([ComposedShader25])

ComposedShader34 = ComposedShader(language = "GLSL")

field35 = field()
field35.name = "chromaticDispertion"
field35.accessType = "initializeOnly"
field35.type = "SFVec3f"
field35.value = "0.98 1 1.033"
ComposedShader34.addField([field35])

field36 = field()
field36.name = "cube"
field36.type = "SFNode"
field36.accessType = "initializeOnly"

ComposedCubeMapTexture37 = ComposedCubeMapTexture()
ComposedCubeMapTexture37.USE = "texture"
field36.addChildren([ComposedCubeMapTexture37])
ComposedShader34.addField([field36])

field38 = field()
field38.name = "bias"
field38.accessType = "initializeOnly"
field38.type = "SFFloat"
field38.value = "0.5"
ComposedShader34.addField([field38])

field39 = field()
field39.name = "scale"
field39.accessType = "initializeOnly"
field39.type = "SFFloat"
field39.value = "0.5"
ComposedShader34.addField([field39])

field40 = field()
field40.name = "power"
field40.accessType = "initializeOnly"
field40.type = "SFFloat"
field40.value = "2"
ComposedShader34.addField([field40])

ShaderPart41 = ShaderPart()
ShaderPart41.url = ["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]
ShaderPart41.type = "VERTEX"
ComposedShader34.parts = ShaderPart41

ShaderPart42 = ShaderPart()
ShaderPart42.USE = "common"
ComposedShader34.addParts([ShaderPart42])
Appearance16.addShaders([ComposedShader34])
Shape14.appearance = Appearance16
Transform13.addChildren([Shape14])
Scene9.addChildren([Transform13])
X3D0.scene = Scene9
