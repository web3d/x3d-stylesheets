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
meta4.content = "flowers7.x3d"
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
meta7.content = "https://coderextreme.net/X3DJSONLD/flowers7.x3d"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "description"
meta8.content = "a flower"
head1.addMeta([meta8])
X3D0.head = head1

Scene9 = Scene()

NavigationInfo10 = NavigationInfo()
NavigationInfo10.type = ["EXAMINE","ANY"]
Scene9.addChildren([NavigationInfo10])
# Images courtesy of Paul Debevec's Light Probe Image Gallery 

Background11 = Background()
Background11.DEF = "background"
Background11.backUrl = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"]
Background11.bottomUrl = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"]
Background11.frontUrl = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"]
Background11.leftUrl = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"]
Background11.rightUrl = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"]
Background11.topUrl = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"]
Scene9.addChildren([Background11])

Viewpoint12 = Viewpoint()
Viewpoint12.position = [0,0,40]
Viewpoint12.description = "Transparent rose"
Scene9.addChildren([Viewpoint12])

Transform13 = Transform()
Transform13.DEF = "Rose01"

Shape14 = Shape()

Appearance15 = Appearance()

Material16 = Material()
Material16.diffuseColor = [.7,.7,.7]
Material16.specularColor = [.5,.5,.5]
Appearance15.material = Material16

ComposedCubeMapTexture17 = ComposedCubeMapTexture()
ComposedCubeMapTexture17.DEF = "texture"

ImageTexture18 = ImageTexture()
ImageTexture18.DEF = "backShader"
ImageTexture18.url = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"]
ComposedCubeMapTexture17.back = ImageTexture18

ImageTexture19 = ImageTexture()
ImageTexture19.DEF = "bottomShader"
ImageTexture19.url = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"]
ComposedCubeMapTexture17.bottom = ImageTexture19

ImageTexture20 = ImageTexture()
ImageTexture20.DEF = "frontShader"
ImageTexture20.url = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"]
ComposedCubeMapTexture17.front = ImageTexture20

ImageTexture21 = ImageTexture()
ImageTexture21.DEF = "leftShader"
ImageTexture21.url = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"]
ComposedCubeMapTexture17.left = ImageTexture21

ImageTexture22 = ImageTexture()
ImageTexture22.DEF = "rightShader"
ImageTexture22.url = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"]
ComposedCubeMapTexture17.right = ImageTexture22

ImageTexture23 = ImageTexture()
ImageTexture23.DEF = "topShader"
ImageTexture23.url = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"]
ComposedCubeMapTexture17.top = ImageTexture23
Appearance15.texture = ComposedCubeMapTexture17

ComposedShader24 = ComposedShader(language = "GLSL")
ComposedShader24.DEF = "x3dom"

field25 = field()
field25.name = "cube"
field25.type = "SFInt32"
field25.accessType = "inputOutput"
field25.value = "0"
ComposedShader24.addField([field25])
#field name='cube' type='SFNode' accessType=\"inputOutput\">
#			  <ComposedCubeMapTexture USE=\"texture\"/>
#		  </field

field26 = field()
field26.name = "chromaticDispertion"
field26.accessType = "initializeOnly"
field26.type = "SFVec3f"
field26.value = "0.98 1.0 1.033"
ComposedShader24.addField([field26])

field27 = field()
field27.name = "bias"
field27.type = "SFFloat"
field27.accessType = "inputOutput"
field27.value = "0.5"
ComposedShader24.addField([field27])

field28 = field()
field28.name = "scale"
field28.type = "SFFloat"
field28.accessType = "inputOutput"
field28.value = "0.5"
ComposedShader24.addField([field28])

field29 = field()
field29.name = "power"
field29.type = "SFFloat"
field29.accessType = "inputOutput"
field29.value = "2"
ComposedShader24.addField([field29])

field30 = field()
field30.name = "a"
field30.type = "SFFloat"
field30.accessType = "inputOutput"
field30.value = "10"
ComposedShader24.addField([field30])

field31 = field()
field31.name = "b"
field31.type = "SFFloat"
field31.accessType = "inputOutput"
field31.value = "1"
ComposedShader24.addField([field31])

field32 = field()
field32.name = "c"
field32.type = "SFFloat"
field32.accessType = "inputOutput"
field32.value = "20"
ComposedShader24.addField([field32])

field33 = field()
field33.name = "d"
field33.type = "SFFloat"
field33.accessType = "inputOutput"
field33.value = "20"
ComposedShader24.addField([field33])

field34 = field()
field34.name = "tdelta"
field34.type = "SFFloat"
field34.accessType = "inputOutput"
field34.value = "0"
ComposedShader24.addField([field34])

field35 = field()
field35.name = "pdelta"
field35.type = "SFFloat"
field35.accessType = "inputOutput"
field35.value = "0"
ComposedShader24.addField([field35])

ShaderPart36 = ShaderPart()
ShaderPart36.url = ["../shaders/x3dom_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom_flowers_chromatic.vs"]
ShaderPart36.type = "VERTEX"
ComposedShader24.parts = ShaderPart36

ShaderPart37 = ShaderPart()
ShaderPart37.url = ["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"]
ShaderPart37.type = "FRAGMENT"
ComposedShader24.parts = ShaderPart37
Appearance15.addShaders([ComposedShader24])

ComposedShader38 = ComposedShader(language = "GLSL")
ComposedShader38.DEF = "cobweb"

field39 = field()
field39.name = "cube"
field39.type = "SFNode"
field39.accessType = "inputOutput"

ComposedCubeMapTexture40 = ComposedCubeMapTexture()
ComposedCubeMapTexture40.USE = "texture"
field39.addChildren([ComposedCubeMapTexture40])
ComposedShader38.addField([field39])

field41 = field()
field41.name = "chromaticDispertion"
field41.accessType = "initializeOnly"
field41.type = "SFVec3f"
field41.value = "0.98 1.0 1.033"
ComposedShader38.addField([field41])

field42 = field()
field42.name = "bias"
field42.type = "SFFloat"
field42.accessType = "inputOnly"
field42.value = "0.5"
ComposedShader38.addField([field42])

field43 = field()
field43.name = "scale"
field43.type = "SFFloat"
field43.accessType = "inputOnly"
field43.value = "0.5"
ComposedShader38.addField([field43])

field44 = field()
field44.name = "power"
field44.type = "SFFloat"
field44.accessType = "inputOnly"
field44.value = "2"
ComposedShader38.addField([field44])

field45 = field()
field45.name = "a"
field45.type = "SFFloat"
field45.accessType = "inputOnly"
field45.value = "10"
ComposedShader38.addField([field45])

field46 = field()
field46.name = "b"
field46.type = "SFFloat"
field46.accessType = "inputOnly"
field46.value = "1"
ComposedShader38.addField([field46])

field47 = field()
field47.name = "c"
field47.type = "SFFloat"
field47.accessType = "inputOnly"
field47.value = "20"
ComposedShader38.addField([field47])

field48 = field()
field48.name = "d"
field48.type = "SFFloat"
field48.accessType = "inputOnly"
field48.value = "20"
ComposedShader38.addField([field48])

field49 = field()
field49.name = "tdelta"
field49.type = "SFFloat"
field49.accessType = "inputOnly"
field49.value = "0"
ComposedShader38.addField([field49])

field50 = field()
field50.name = "pdelta"
field50.type = "SFFloat"
field50.accessType = "inputOnly"
field50.value = "0"
ComposedShader38.addField([field50])

ShaderPart51 = ShaderPart()
ShaderPart51.url = ["../shaders/cobweb_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb_flowers_chromatic.vs"]
ShaderPart51.type = "VERTEX"
ComposedShader38.parts = ShaderPart51

ShaderPart52 = ShaderPart()
ShaderPart52.url = ["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"]
ShaderPart52.type = "FRAGMENT"
ComposedShader38.parts = ShaderPart52
Appearance15.addShaders([ComposedShader38])
Shape14.appearance = Appearance15

Sphere53 = Sphere(solid = False, radius = 1)
Shape14.geometry = Sphere53
Transform13.addChildren([Shape14])
Scene9.addChildren([Transform13])

Script54 = Script(directOutput = True)
Script54.DEF = "UrlSelector"

field55 = field()
field55.name = "frontUrls"
field55.type = "MFString"
field55.accessType = "initializeOnly"
field55.value = "\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\""
Script54.addField([field55])

field56 = field()
field56.name = "backUrls"
field56.type = "MFString"
field56.accessType = "initializeOnly"
field56.value = "\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\""
Script54.addField([field56])

field57 = field()
field57.name = "leftUrls"
field57.type = "MFString"
field57.accessType = "initializeOnly"
field57.value = "\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\""
Script54.addField([field57])

field58 = field()
field58.name = "rightUrls"
field58.type = "MFString"
field58.accessType = "initializeOnly"
field58.value = "\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\""
Script54.addField([field58])

field59 = field()
field59.name = "topUrls"
field59.type = "MFString"
field59.accessType = "initializeOnly"
field59.value = "\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\""
Script54.addField([field59])

field60 = field()
field60.name = "bottomUrls"
field60.type = "MFString"
field60.accessType = "initializeOnly"
field60.value = "\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\""
Script54.addField([field60])

field61 = field()
field61.name = "front"
field61.type = "MFString"
field61.accessType = "inputOutput"
Script54.addField([field61])

field62 = field()
field62.name = "back"
field62.type = "MFString"
field62.accessType = "inputOutput"
Script54.addField([field62])

field63 = field()
field63.name = "left"
field63.type = "MFString"
field63.accessType = "inputOutput"
Script54.addField([field63])

field64 = field()
field64.name = "right"
field64.type = "MFString"
field64.accessType = "inputOutput"
Script54.addField([field64])

field65 = field()
field65.name = "top"
field65.type = "MFString"
field65.accessType = "inputOutput"
Script54.addField([field65])

field66 = field()
field66.name = "bottom"
field66.type = "MFString"
field66.accessType = "inputOutput"
Script54.addField([field66])

field67 = field()
field67.name = "set_fraction"
field67.type = "SFFloat"
field67.accessType = "inputOnly"
Script54.addField([field67])

field68 = field()
field68.name = "old"
field68.type = "SFInt32"
field68.accessType = "inputOutput"
field68.value = "-1"
Script54.addField([field68])

Script54.setSourceCode('''\n"+
"ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"            var side = Math.floor(f*frontUrls.length);\n"+
"            if (side > frontUrls.length-1) {\n"+
"                side = 0;\n"+
"            }\n"+
"            if (side != old) {\n"+
"                    old = side;\n"+
"                    front[0] = frontUrls[side];\n"+
"                    back[0] = backUrls[side];\n"+
"                    left[0] = leftUrls[side];\n"+
"                    right[0] = rightUrls[side];\n"+
"                    top[0] = topUrls[side];\n"+
"                    bottom[0] = bottomUrls[side];\n"+
"            }\n"+
"        }\n"+
"''')
Scene9.addChildren([Script54])
#
#            <TimeSensor DEF=\"Clock\" cycleInterval=\"45\" loop='true'/>
#            <ROUTE fromNode='Clock' fromField='fraction_changed' toNode='UrlSelector' toField='set_fraction'/>
#            <ROUTE fromNode='UrlSelector' fromField='front' toNode='background' toField='frontUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='back' toNode='background' toField='backUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='left' toNode='background' toField='leftUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='right' toNode='background' toField='rightUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='top' toNode='background' toField='topUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='bottom' toNode='background' toField='bottomUrl'/>
#            <ROUTE fromNode='UrlSelector' fromField='front' toNode='frontShader' toField='url'/>
#            <ROUTE fromNode='UrlSelector' fromField='back' toNode='backShader' toField='url'/>
#            <ROUTE fromNode='UrlSelector' fromField='left' toNode='leftShader' toField='url'/>
#            <ROUTE fromNode='UrlSelector' fromField='right' toNode='rightShader' toField='url'/>
#            <ROUTE fromNode='UrlSelector' fromField='top' toNode='topShader' toField='url'/>
#            <ROUTE fromNode='UrlSelector' fromField='bottom' toNode='bottomShader' toField='url'/>
#	    

Script69 = Script(directOutput = True)
Script69.DEF = "Animate"

field70 = field()
field70.name = "set_fraction"
field70.type = "SFFloat"
field70.accessType = "inputOnly"
Script69.addField([field70])

field71 = field()
field71.name = "a"
field71.type = "SFFloat"
field71.accessType = "inputOutput"
field71.value = "10"
Script69.addField([field71])

field72 = field()
field72.name = "b"
field72.type = "SFFloat"
field72.accessType = "inputOutput"
field72.value = "1"
Script69.addField([field72])

field73 = field()
field73.name = "c"
field73.type = "SFFloat"
field73.accessType = "inputOutput"
field73.value = "20"
Script69.addField([field73])

field74 = field()
field74.name = "d"
field74.type = "SFFloat"
field74.accessType = "inputOutput"
field74.value = "20"
Script69.addField([field74])

field75 = field()
field75.name = "tdelta"
field75.type = "SFFloat"
field75.accessType = "inputOutput"
field75.value = "0"
Script69.addField([field75])

field76 = field()
field76.name = "pdelta"
field76.type = "SFFloat"
field76.accessType = "inputOutput"
field76.value = "0"
Script69.addField([field76])

Script69.setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function set_fraction() {\n"+
"	var choice = Math.floor(Math.random() * 4);\n"+
"	if (choice == 0) {\n"+
"		a = a + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 1) {\n"+
"		b = b + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 2) {\n"+
"		c = c + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 3) {\n"+
"		d = d + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	}\n"+
"	tdelta = tdelta + 0.5;\n"+
"	pdelta = pdelta + 0.5;\n"+
"	if (a < 1) {\n"+
"		a = 10;\n"+
"	}\n"+
"	if (b < 1) {\n"+
"		b = 10;\n"+
"	}\n"+
"	if (c < 1) {\n"+
"		c = 4;\n"+
"	}\n"+
"	if (c > 20) {\n"+
"		c = 4;\n"+
"	}\n"+
"	if (d < 1) {\n"+
"		d = 4;\n"+
"	}\n"+
"	if (d > 20) {\n"+
"		d = 4;\n"+
"	}\n"+
"}\n"+
"''')
Scene9.addChildren([Script69])

TimeSensor77 = TimeSensor()
TimeSensor77.DEF = "TourTime"
TimeSensor77.cycleInterval = 5
TimeSensor77.loop = True
Scene9.addChildren([TimeSensor77])

ROUTE78 = ROUTE()
ROUTE78.fromNode = "TourTime"
ROUTE78.fromField = "fraction_changed"
ROUTE78.toNode = "Animate"
ROUTE78.toField = "set_fraction"
Scene9.addChildren([ROUTE78])

ROUTE79 = ROUTE()
ROUTE79.fromNode = "Animate"
ROUTE79.fromField = "a"
ROUTE79.toNode = "cobweb"
ROUTE79.toField = "a"
Scene9.addChildren([ROUTE79])

ROUTE80 = ROUTE()
ROUTE80.fromNode = "Animate"
ROUTE80.fromField = "b"
ROUTE80.toNode = "cobweb"
ROUTE80.toField = "b"
Scene9.addChildren([ROUTE80])

ROUTE81 = ROUTE()
ROUTE81.fromNode = "Animate"
ROUTE81.fromField = "c"
ROUTE81.toNode = "cobweb"
ROUTE81.toField = "c"
Scene9.addChildren([ROUTE81])

ROUTE82 = ROUTE()
ROUTE82.fromNode = "Animate"
ROUTE82.fromField = "d"
ROUTE82.toNode = "cobweb"
ROUTE82.toField = "d"
Scene9.addChildren([ROUTE82])

ROUTE83 = ROUTE()
ROUTE83.fromNode = "Animate"
ROUTE83.fromField = "pdelta"
ROUTE83.toNode = "cobweb"
ROUTE83.toField = "pdelta"
Scene9.addChildren([ROUTE83])

ROUTE84 = ROUTE()
ROUTE84.fromNode = "Animate"
ROUTE84.fromField = "tdelta"
ROUTE84.toNode = "cobweb"
ROUTE84.toField = "tdelta"
Scene9.addChildren([ROUTE84])

ROUTE85 = ROUTE()
ROUTE85.fromNode = "Animate"
ROUTE85.fromField = "a"
ROUTE85.toNode = "x3dom"
ROUTE85.toField = "a"
Scene9.addChildren([ROUTE85])

ROUTE86 = ROUTE()
ROUTE86.fromNode = "Animate"
ROUTE86.fromField = "b"
ROUTE86.toNode = "x3dom"
ROUTE86.toField = "b"
Scene9.addChildren([ROUTE86])

ROUTE87 = ROUTE()
ROUTE87.fromNode = "Animate"
ROUTE87.fromField = "c"
ROUTE87.toNode = "x3dom"
ROUTE87.toField = "c"
Scene9.addChildren([ROUTE87])

ROUTE88 = ROUTE()
ROUTE88.fromNode = "Animate"
ROUTE88.fromField = "d"
ROUTE88.toNode = "x3dom"
ROUTE88.toField = "d"
Scene9.addChildren([ROUTE88])

ROUTE89 = ROUTE()
ROUTE89.fromNode = "Animate"
ROUTE89.fromField = "pdelta"
ROUTE89.toNode = "x3dom"
ROUTE89.toField = "pdelta"
Scene9.addChildren([ROUTE89])

ROUTE90 = ROUTE()
ROUTE90.fromNode = "Animate"
ROUTE90.fromField = "tdelta"
ROUTE90.toNode = "x3dom"
ROUTE90.toField = "tdelta"
Scene9.addChildren([ROUTE90])
X3D0.scene = Scene9
