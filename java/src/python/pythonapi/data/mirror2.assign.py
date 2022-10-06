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
meta4.content = "mirro2.x3d"
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
meta7.content = "https://coderextreme.net/X3DJSONLD/mirro2.x3d"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "description"
meta8.content = "a mirrored sphere"
head1.addMeta([meta8])
X3D0.head = head1

Scene9 = Scene()

Viewpoint10 = Viewpoint()
Viewpoint10.position = [0,5,100]
Viewpoint10.description = "Switch background and images texture"
Scene9.addChildren([Viewpoint10])

Background11 = Background()
Background11.DEF = "cube"
Background11.leftUrl = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]
Background11.rightUrl = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]
Background11.frontUrl = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]
Background11.backUrl = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]
Background11.topUrl = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"]
Background11.bottomUrl = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]
Scene9.addChildren([Background11])

Transform12 = Transform()

Shape13 = Shape()

Appearance14 = Appearance()

Material15 = Material()
Material15.diffuseColor = [.7,.7,.7]
Material15.specularColor = [.5,.5,.5]
Appearance14.material = Material15

ComposedCubeMapTexture16 = ComposedCubeMapTexture()

ImageTexture17 = ImageTexture()
ImageTexture17.DEF = "backShader"
ImageTexture17.url = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]
ComposedCubeMapTexture16.back = ImageTexture17

ImageTexture18 = ImageTexture()
ImageTexture18.DEF = "bottomShader"
ImageTexture18.url = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]
ComposedCubeMapTexture16.bottom = ImageTexture18

ImageTexture19 = ImageTexture()
ImageTexture19.DEF = "frontShader"
ImageTexture19.url = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]
ComposedCubeMapTexture16.front = ImageTexture19

ImageTexture20 = ImageTexture()
ImageTexture20.DEF = "leftShader"
ImageTexture20.url = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]
ComposedCubeMapTexture16.left = ImageTexture20

ImageTexture21 = ImageTexture()
ImageTexture21.DEF = "rightShader"
ImageTexture21.url = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]
ComposedCubeMapTexture16.right = ImageTexture21

ImageTexture22 = ImageTexture()
ImageTexture22.DEF = "topShader"
ImageTexture22.url = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"]
ComposedCubeMapTexture16.top = ImageTexture22
Appearance14.texture = ComposedCubeMapTexture16

ComposedShader23 = ComposedShader(language = "GLSL")
ComposedShader23.DEF = "cobweb"
#http://hypertextbook.com/facts/2005/JustinChe.shtml

field24 = field()
field24.name = "chromaticDispertion"
field24.accessType = "inputOutput"
field24.type = "SFVec3f"
field24.value = "0.98 1 1.033"
ComposedShader23.addField([field24])

field25 = field()
field25.name = "cube"
field25.accessType = "inputOutput"
field25.type = "SFInt32"
field25.value = "0"
ComposedShader23.addField([field25])

field26 = field()
field26.name = "bias"
field26.accessType = "inputOutput"
field26.type = "SFFloat"
field26.value = "0.5"
ComposedShader23.addField([field26])

field27 = field()
field27.name = "scale"
field27.accessType = "inputOutput"
field27.type = "SFFloat"
field27.value = "0.5"
ComposedShader23.addField([field27])

field28 = field()
field28.name = "power"
field28.accessType = "inputOutput"
field28.type = "SFFloat"
field28.value = "2"
ComposedShader23.addField([field28])

ShaderPart29 = ShaderPart()
ShaderPart29.url = ["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]
ShaderPart29.type = "VERTEX"
ComposedShader23.addParts([ShaderPart29])

ShaderPart30 = ShaderPart()
ShaderPart30.url = ["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"]
ShaderPart30.type = "FRAGMENT"
ComposedShader23.addParts([ShaderPart30])
Appearance14.addShaders([ComposedShader23])

ComposedShader31 = ComposedShader(language = "GLSL")
ComposedShader31.DEF = "x3dom"
#http://hypertextbook.com/facts/2005/JustinChe.shtml

field32 = field()
field32.name = "chromaticDispertion"
field32.accessType = "inputOutput"
field32.type = "SFVec3f"
field32.value = "0.98 1 1.033"
ComposedShader31.addField([field32])

field33 = field()
field33.name = "cube"
field33.accessType = "inputOutput"
field33.type = "SFInt32"
field33.value = "0"
ComposedShader31.addField([field33])

field34 = field()
field34.name = "bias"
field34.accessType = "inputOutput"
field34.type = "SFFloat"
field34.value = "0.5"
ComposedShader31.addField([field34])

field35 = field()
field35.name = "scale"
field35.accessType = "inputOutput"
field35.type = "SFFloat"
field35.value = "0.5"
ComposedShader31.addField([field35])

field36 = field()
field36.name = "power"
field36.accessType = "inputOutput"
field36.type = "SFFloat"
field36.value = "2"
ComposedShader31.addField([field36])

ShaderPart37 = ShaderPart()
ShaderPart37.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]
ShaderPart37.type = "VERTEX"
ComposedShader31.addParts([ShaderPart37])

ShaderPart38 = ShaderPart()
ShaderPart38.url = ["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"]
ShaderPart38.type = "FRAGMENT"
ComposedShader31.addParts([ShaderPart38])
Appearance14.addShaders([ComposedShader31])
Shape13.appearance = Appearance14

Sphere39 = Sphere(radius = 30)
Shape13.geometry = Sphere39
Transform12.addChildren([Shape13])

Script40 = Script(directOutput = True)
Script40.DEF = "UrlSelector"

field41 = field()
field41.name = "frontUrls"
field41.type = "MFString"
field41.accessType = "initializeOnly"
field41.value = "\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\""
Script40.addField([field41])

field42 = field()
field42.name = "backUrls"
field42.type = "MFString"
field42.accessType = "initializeOnly"
field42.value = "\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\""
Script40.addField([field42])

field43 = field()
field43.name = "leftUrls"
field43.type = "MFString"
field43.accessType = "initializeOnly"
field43.value = "\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\""
Script40.addField([field43])

field44 = field()
field44.name = "rightUrls"
field44.type = "MFString"
field44.accessType = "initializeOnly"
field44.value = "\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\""
Script40.addField([field44])

field45 = field()
field45.name = "topUrls"
field45.type = "MFString"
field45.accessType = "initializeOnly"
field45.value = "\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\""
Script40.addField([field45])

field46 = field()
field46.name = "bottomUrls"
field46.type = "MFString"
field46.accessType = "initializeOnly"
field46.value = "\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\""
Script40.addField([field46])

field47 = field()
field47.name = "front_changed"
field47.type = "MFString"
field47.accessType = "outputOnly"
Script40.addField([field47])

field48 = field()
field48.name = "back_changed"
field48.type = "MFString"
field48.accessType = "outputOnly"
Script40.addField([field48])

field49 = field()
field49.name = "left_changed"
field49.type = "MFString"
field49.accessType = "outputOnly"
Script40.addField([field49])

field50 = field()
field50.name = "right_changed"
field50.type = "MFString"
field50.accessType = "outputOnly"
Script40.addField([field50])

field51 = field()
field51.name = "top_changed"
field51.type = "MFString"
field51.accessType = "outputOnly"
Script40.addField([field51])

field52 = field()
field52.name = "bottom_changed"
field52.type = "MFString"
field52.accessType = "outputOnly"
Script40.addField([field52])

field53 = field()
field53.name = "set_fraction"
field53.type = "SFFloat"
field53.accessType = "inputOnly"
Script40.addField([field53])

field54 = field()
field54.name = "old"
field54.type = "SFInt32"
field54.accessType = "inputOutput"
field54.value = "-1"
Script40.addField([field54])

Script40.setSourceCode('''\n"+
"ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"	    var side = Math.floor(f*frontUrls.length);\n"+
"	    if (side > frontUrls.length-1) {\n"+
"	    	side = 0;\n"+
"	    }\n"+
"	    if (side != old) {\n"+
"	    	    // Browser.print(f+\" \"+side);\n"+
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
Transform12.addChildren([Script40])

TimeSensor55 = TimeSensor()
TimeSensor55.DEF = "Clock"
TimeSensor55.cycleInterval = 45
TimeSensor55.loop = True
Transform12.addChildren([TimeSensor55])

ROUTE56 = ROUTE()
ROUTE56.fromNode = "Clock"
ROUTE56.fromField = "fraction_changed"
ROUTE56.toNode = "UrlSelector"
ROUTE56.toField = "set_fraction"
Transform12.addChildren([ROUTE56])

ROUTE57 = ROUTE()
ROUTE57.fromNode = "UrlSelector"
ROUTE57.fromField = "front_changed"
ROUTE57.toNode = "cube"
ROUTE57.toField = "frontUrl"
Transform12.addChildren([ROUTE57])

ROUTE58 = ROUTE()
ROUTE58.fromNode = "UrlSelector"
ROUTE58.fromField = "back_changed"
ROUTE58.toNode = "cube"
ROUTE58.toField = "backUrl"
Transform12.addChildren([ROUTE58])

ROUTE59 = ROUTE()
ROUTE59.fromNode = "UrlSelector"
ROUTE59.fromField = "left_changed"
ROUTE59.toNode = "cube"
ROUTE59.toField = "leftUrl"
Transform12.addChildren([ROUTE59])

ROUTE60 = ROUTE()
ROUTE60.fromNode = "UrlSelector"
ROUTE60.fromField = "right_changed"
ROUTE60.toNode = "cube"
ROUTE60.toField = "rightUrl"
Transform12.addChildren([ROUTE60])

ROUTE61 = ROUTE()
ROUTE61.fromNode = "UrlSelector"
ROUTE61.fromField = "top_changed"
ROUTE61.toNode = "cube"
ROUTE61.toField = "topUrl"
Transform12.addChildren([ROUTE61])

ROUTE62 = ROUTE()
ROUTE62.fromNode = "UrlSelector"
ROUTE62.fromField = "bottom_changed"
ROUTE62.toNode = "cube"
ROUTE62.toField = "bottomUrl"
Transform12.addChildren([ROUTE62])

ROUTE63 = ROUTE()
ROUTE63.fromNode = "UrlSelector"
ROUTE63.fromField = "front_changed"
ROUTE63.toNode = "frontShader"
ROUTE63.toField = "url"
Transform12.addChildren([ROUTE63])

ROUTE64 = ROUTE()
ROUTE64.fromNode = "UrlSelector"
ROUTE64.fromField = "back_changed"
ROUTE64.toNode = "backShader"
ROUTE64.toField = "url"
Transform12.addChildren([ROUTE64])

ROUTE65 = ROUTE()
ROUTE65.fromNode = "UrlSelector"
ROUTE65.fromField = "left_changed"
ROUTE65.toNode = "leftShader"
ROUTE65.toField = "url"
Transform12.addChildren([ROUTE65])

ROUTE66 = ROUTE()
ROUTE66.fromNode = "UrlSelector"
ROUTE66.fromField = "right_changed"
ROUTE66.toNode = "rightShader"
ROUTE66.toField = "url"
Transform12.addChildren([ROUTE66])

ROUTE67 = ROUTE()
ROUTE67.fromNode = "UrlSelector"
ROUTE67.fromField = "top_changed"
ROUTE67.toNode = "topShader"
ROUTE67.toField = "url"
Transform12.addChildren([ROUTE67])

ROUTE68 = ROUTE()
ROUTE68.fromNode = "UrlSelector"
ROUTE68.fromField = "bottom_changed"
ROUTE68.toNode = "bottomShader"
ROUTE68.toField = "url"
Transform12.addChildren([ROUTE68])
Scene9.addChildren([Transform12])
X3D0.scene = Scene9
