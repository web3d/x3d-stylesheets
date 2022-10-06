from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

component2 = component()
component2.name = "EnvironmentalEffects"
component2.level = 3
head1.addComponent([component2])

component3 = component()
component3.name = "Shaders"
component3.level = 1
head1.addComponent([component3])

component4 = component()
component4.name = "CubeMapTexturing"
component4.level = 1
head1.addComponent([component4])

meta5 = meta()
meta5.name = "title"
meta5.content = "mirror.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "creator"
meta6.content = "John Carlson"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "generator"
meta7.content = "manual"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "identifier"
meta8.content = "https://coderextreme.net/X3DJSONLD/mirror.x3d"
head1.addMeta([meta8])

meta9 = meta()
meta9.name = "description"
meta9.content = "sphere with alternating backgrounds"
head1.addMeta([meta9])
X3D0.head = head1

Scene10 = Scene()

Viewpoint11 = Viewpoint()
Viewpoint11.position = [0,5,100]
Viewpoint11.description = "Switch background and images texture"
Scene10.addChildren([Viewpoint11])

TextureBackground12 = TextureBackground()

ImageTexture13 = ImageTexture()
ImageTexture13.DEF = "leftBack"
ImageTexture13.url = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]
TextureBackground12.leftTexture = ImageTexture13

ImageTexture14 = ImageTexture()
ImageTexture14.DEF = "rightBack"
ImageTexture14.url = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]
TextureBackground12.rightTexture = ImageTexture14

ImageTexture15 = ImageTexture()
ImageTexture15.DEF = "frontBack"
ImageTexture15.url = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]
TextureBackground12.frontTexture = ImageTexture15

ImageTexture16 = ImageTexture()
ImageTexture16.DEF = "backBack"
ImageTexture16.url = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]
TextureBackground12.backTexture = ImageTexture16

ImageTexture17 = ImageTexture()
ImageTexture17.DEF = "topBack"
ImageTexture17.url = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"]
TextureBackground12.topTexture = ImageTexture17

ImageTexture18 = ImageTexture()
ImageTexture18.DEF = "bottomBack"
ImageTexture18.url = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]
TextureBackground12.bottomTexture = ImageTexture18
Scene10.addChildren([TextureBackground12])

Transform19 = Transform()

Shape20 = Shape()

Appearance21 = Appearance()

Material22 = Material()
Material22.diffuseColor = [.7,.7,.7]
Material22.specularColor = [.5,.5,.5]
Appearance21.material = Material22

ComposedCubeMapTexture23 = ComposedCubeMapTexture()

ImageTexture24 = ImageTexture()
ImageTexture24.DEF = "backShader"
ImageTexture24.url = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]
ComposedCubeMapTexture23.back = ImageTexture24

ImageTexture25 = ImageTexture()
ImageTexture25.DEF = "bottomShader"
ImageTexture25.url = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]
ComposedCubeMapTexture23.bottom = ImageTexture25

ImageTexture26 = ImageTexture()
ImageTexture26.DEF = "frontShader"
ImageTexture26.url = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]
ComposedCubeMapTexture23.front = ImageTexture26

ImageTexture27 = ImageTexture()
ImageTexture27.DEF = "leftShader"
ImageTexture27.url = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]
ComposedCubeMapTexture23.left = ImageTexture27

ImageTexture28 = ImageTexture()
ImageTexture28.DEF = "rightShader"
ImageTexture28.url = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]
ComposedCubeMapTexture23.right = ImageTexture28

ImageTexture29 = ImageTexture()
ImageTexture29.DEF = "topShader"
ImageTexture29.url = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"]
ComposedCubeMapTexture23.top = ImageTexture29
Appearance21.texture = ComposedCubeMapTexture23

ComposedShader30 = ComposedShader(language = "GLSL")
ComposedShader30.DEF = "x3dom"
#http://hypertextbook.com/facts/2005/JustinChe.shtml

field31 = field()
field31.name = "chromaticDispertion"
field31.accessType = "inputOutput"
field31.type = "SFVec3f"
field31.value = "0.98 1 1.033"
ComposedShader30.addField([field31])

field32 = field()
field32.name = "cube"
field32.accessType = "inputOutput"
field32.type = "SFInt32"
field32.value = "0"
ComposedShader30.addField([field32])

field33 = field()
field33.name = "bias"
field33.accessType = "inputOutput"
field33.type = "SFFloat"
field33.value = "0.5"
ComposedShader30.addField([field33])

field34 = field()
field34.name = "scale"
field34.accessType = "inputOutput"
field34.type = "SFFloat"
field34.value = "0.5"
ComposedShader30.addField([field34])

field35 = field()
field35.name = "power"
field35.accessType = "inputOutput"
field35.type = "SFFloat"
field35.value = "2"
ComposedShader30.addField([field35])

ShaderPart36 = ShaderPart()
ShaderPart36.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]
ShaderPart36.type = "VERTEX"
ComposedShader30.addParts([ShaderPart36])

ShaderPart37 = ShaderPart()
ShaderPart37.url = ["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"]
ShaderPart37.type = "FRAGMENT"
ComposedShader30.addParts([ShaderPart37])
Appearance21.addShaders([ComposedShader30])

ComposedShader38 = ComposedShader(language = "GLSL")
ComposedShader38.DEF = "cobweb"
#http://hypertextbook.com/facts/2005/JustinChe.shtml

field39 = field()
field39.name = "chromaticDispertion"
field39.accessType = "inputOutput"
field39.type = "SFVec3f"
field39.value = "0.98 1 1.033"
ComposedShader38.addField([field39])

field40 = field()
field40.name = "cube"
field40.accessType = "inputOutput"
field40.type = "SFInt32"
field40.value = "0"
ComposedShader38.addField([field40])

field41 = field()
field41.name = "bias"
field41.accessType = "inputOutput"
field41.type = "SFFloat"
field41.value = "0.5"
ComposedShader38.addField([field41])

field42 = field()
field42.name = "scale"
field42.accessType = "inputOutput"
field42.type = "SFFloat"
field42.value = "0.5"
ComposedShader38.addField([field42])

field43 = field()
field43.name = "power"
field43.accessType = "inputOutput"
field43.type = "SFFloat"
field43.value = "2"
ComposedShader38.addField([field43])

ShaderPart44 = ShaderPart()
ShaderPart44.url = ["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]
ShaderPart44.type = "VERTEX"
ComposedShader38.addParts([ShaderPart44])

ShaderPart45 = ShaderPart()
ShaderPart45.url = ["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"]
ShaderPart45.type = "FRAGMENT"
ComposedShader38.addParts([ShaderPart45])
Appearance21.addShaders([ComposedShader38])
Shape20.appearance = Appearance21

Sphere46 = Sphere(radius = 30)
Shape20.geometry = Sphere46
Transform19.addChildren([Shape20])

Script47 = Script(directOutput = True)
Script47.DEF = "UrlSelector"

field48 = field()
field48.name = "frontUrls"
field48.type = "MFString"
field48.accessType = "initializeOnly"
field48.value = "\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\""
Script47.addField([field48])

field49 = field()
field49.name = "backUrls"
field49.type = "MFString"
field49.accessType = "initializeOnly"
field49.value = "\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\""
Script47.addField([field49])

field50 = field()
field50.name = "leftUrls"
field50.type = "MFString"
field50.accessType = "initializeOnly"
field50.value = "\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\""
Script47.addField([field50])

field51 = field()
field51.name = "rightUrls"
field51.type = "MFString"
field51.accessType = "initializeOnly"
field51.value = "\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\""
Script47.addField([field51])

field52 = field()
field52.name = "topUrls"
field52.type = "MFString"
field52.accessType = "initializeOnly"
field52.value = "\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\""
Script47.addField([field52])

field53 = field()
field53.name = "bottomUrls"
field53.type = "MFString"
field53.accessType = "initializeOnly"
field53.value = "\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\""
Script47.addField([field53])

field54 = field()
field54.name = "front_changed"
field54.type = "MFString"
field54.accessType = "outputOnly"
Script47.addField([field54])

field55 = field()
field55.name = "back_changed"
field55.type = "MFString"
field55.accessType = "outputOnly"
Script47.addField([field55])

field56 = field()
field56.name = "left_changed"
field56.type = "MFString"
field56.accessType = "outputOnly"
Script47.addField([field56])

field57 = field()
field57.name = "right_changed"
field57.type = "MFString"
field57.accessType = "outputOnly"
Script47.addField([field57])

field58 = field()
field58.name = "top_changed"
field58.type = "MFString"
field58.accessType = "outputOnly"
Script47.addField([field58])

field59 = field()
field59.name = "bottom_changed"
field59.type = "MFString"
field59.accessType = "outputOnly"
Script47.addField([field59])

field60 = field()
field60.name = "set_fraction"
field60.type = "SFFloat"
field60.accessType = "inputOnly"
Script47.addField([field60])

field61 = field()
field61.name = "old"
field61.type = "SFInt32"
field61.accessType = "inputOutput"
field61.value = "-1"
Script47.addField([field61])

Script47.setSourceCode('''\n"+
"ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"	    var side = Math.floor(f*frontUrls.length);\n"+
"	    if (side > frontUrls.length-1) {\n"+
"	    	side = 0;\n"+
"	    }\n"+
"	    if (side != old) {\n"+
"	    	    Browser.print(f+\" \"+side);\n"+
"	    	    old = side;\n"+
"		    front_changed[0] = frontUrls[side];\n"+
"		    back_changed[0] = backUrls[side];\n"+
"		    left_changed[0] = leftUrls[side];\n"+
"		    right_changed[0] = rightUrls[side];\n"+
"		    top_changed[0] = topUrls[side];\n"+
"		    bottom_changed[0] = bottomUrls[side];\n"+
"            }\n"+
"        }\n"+
"''')
Transform19.addChildren([Script47])

TimeSensor62 = TimeSensor()
TimeSensor62.DEF = "Clock"
TimeSensor62.cycleInterval = 45
TimeSensor62.loop = True
Transform19.addChildren([TimeSensor62])

ROUTE63 = ROUTE()
ROUTE63.fromNode = "Clock"
ROUTE63.fromField = "fraction_changed"
ROUTE63.toNode = "UrlSelector"
ROUTE63.toField = "set_fraction"
Transform19.addChildren([ROUTE63])

ROUTE64 = ROUTE()
ROUTE64.fromNode = "UrlSelector"
ROUTE64.fromField = "front_changed"
ROUTE64.toNode = "frontBack"
ROUTE64.toField = "url"
Transform19.addChildren([ROUTE64])

ROUTE65 = ROUTE()
ROUTE65.fromNode = "UrlSelector"
ROUTE65.fromField = "back_changed"
ROUTE65.toNode = "backBack"
ROUTE65.toField = "url"
Transform19.addChildren([ROUTE65])

ROUTE66 = ROUTE()
ROUTE66.fromNode = "UrlSelector"
ROUTE66.fromField = "left_changed"
ROUTE66.toNode = "leftBack"
ROUTE66.toField = "url"
Transform19.addChildren([ROUTE66])

ROUTE67 = ROUTE()
ROUTE67.fromNode = "UrlSelector"
ROUTE67.fromField = "right_changed"
ROUTE67.toNode = "rightBack"
ROUTE67.toField = "url"
Transform19.addChildren([ROUTE67])

ROUTE68 = ROUTE()
ROUTE68.fromNode = "UrlSelector"
ROUTE68.fromField = "top_changed"
ROUTE68.toNode = "topBack"
ROUTE68.toField = "url"
Transform19.addChildren([ROUTE68])

ROUTE69 = ROUTE()
ROUTE69.fromNode = "UrlSelector"
ROUTE69.fromField = "bottom_changed"
ROUTE69.toNode = "bottomBack"
ROUTE69.toField = "url"
Transform19.addChildren([ROUTE69])

ROUTE70 = ROUTE()
ROUTE70.fromNode = "UrlSelector"
ROUTE70.fromField = "front_changed"
ROUTE70.toNode = "frontShader"
ROUTE70.toField = "url"
Transform19.addChildren([ROUTE70])

ROUTE71 = ROUTE()
ROUTE71.fromNode = "UrlSelector"
ROUTE71.fromField = "back_changed"
ROUTE71.toNode = "backShader"
ROUTE71.toField = "url"
Transform19.addChildren([ROUTE71])

ROUTE72 = ROUTE()
ROUTE72.fromNode = "UrlSelector"
ROUTE72.fromField = "left_changed"
ROUTE72.toNode = "leftShader"
ROUTE72.toField = "url"
Transform19.addChildren([ROUTE72])

ROUTE73 = ROUTE()
ROUTE73.fromNode = "UrlSelector"
ROUTE73.fromField = "right_changed"
ROUTE73.toNode = "rightShader"
ROUTE73.toField = "url"
Transform19.addChildren([ROUTE73])

ROUTE74 = ROUTE()
ROUTE74.fromNode = "UrlSelector"
ROUTE74.fromField = "top_changed"
ROUTE74.toNode = "topShader"
ROUTE74.toField = "url"
Transform19.addChildren([ROUTE74])

ROUTE75 = ROUTE()
ROUTE75.fromNode = "UrlSelector"
ROUTE75.fromField = "bottom_changed"
ROUTE75.toNode = "bottomShader"
ROUTE75.toField = "url"
Transform19.addChildren([ROUTE75])
Scene10.addChildren([Transform19])
X3D0.scene = Scene10
