from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    component2 = component(name="Shaders", level=1), 
    component3 = component(name="CubeMapTexturing", level=1), 
    meta4 = meta(name="title", content="flowers7.x3d"), 
    meta5 = meta(name="creator", content="John Carlson"), 
    meta6 = meta(name="generator", content="manual"), 
    meta7 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/flowers7.x3d"), 
    meta8 = meta(name="description", content="a flower")), 
   Scene9 = Scene(    NavigationInfo10 = NavigationInfo(type=["EXAMINE","ANY"]),     # Images courtesy of Paul Debevec's Light Probe Image Gallery 

    Background11 = Background(DEF="background", backUrl=["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"], bottomUrl=["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"], frontUrl=["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"], leftUrl=["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"], rightUrl=["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"], topUrl=["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"]), 
    Viewpoint12 = Viewpoint(position=[0,0,40], description="Transparent rose"), 
    Transform13 = Transform(DEF="Rose01",      Shape14 = Shape(      Appearance15 = Appearance(       Material16 = Material(diffuseColor=[.7,.7,.7], specularColor=[.5,.5,.5]), 
       ComposedCubeMapTexture17 = ComposedCubeMapTexture(DEF="texture",         ImageTexture18 = ImageTexture(DEF="backShader", url=["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"]), 
        ImageTexture19 = ImageTexture(DEF="bottomShader", url=["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"]), 
        ImageTexture20 = ImageTexture(DEF="frontShader", url=["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"]), 
        ImageTexture21 = ImageTexture(DEF="leftShader", url=["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"]), 
        ImageTexture22 = ImageTexture(DEF="rightShader", url=["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"]), 
        ImageTexture23 = ImageTexture(DEF="topShader", url=["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"])), 
       ComposedShader24 = ComposedShader(DEF="x3dom", language="GLSL",         field25 = field(name="cube", type="SFInt32", accessType="inputOutput", value="0"),         #field name='cube' type='SFNode' accessType=\"inputOutput\">
#			  <ComposedCubeMapTexture USE=\"texture\"/>
#		  </field

        field26 = field(name="chromaticDispertion", accessType="initializeOnly", type="SFVec3f", value="0.98 1.0 1.033"), 
        field27 = field(name="bias", type="SFFloat", accessType="inputOutput", value="0.5"), 
        field28 = field(name="scale", type="SFFloat", accessType="inputOutput", value="0.5"), 
        field29 = field(name="power", type="SFFloat", accessType="inputOutput", value="2"), 
        field30 = field(name="a", type="SFFloat", accessType="inputOutput", value="10"), 
        field31 = field(name="b", type="SFFloat", accessType="inputOutput", value="1"), 
        field32 = field(name="c", type="SFFloat", accessType="inputOutput", value="20"), 
        field33 = field(name="d", type="SFFloat", accessType="inputOutput", value="20"), 
        field34 = field(name="tdelta", type="SFFloat", accessType="inputOutput", value="0"), 
        field35 = field(name="pdelta", type="SFFloat", accessType="inputOutput", value="0"), 
        ShaderPart36 = ShaderPart(url=["../shaders/x3dom_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom_flowers_chromatic.vs"], type="VERTEX"), 
        ShaderPart37 = ShaderPart(url=["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"], type="FRAGMENT")), 
       ComposedShader38 = ComposedShader(DEF="cobweb", language="GLSL",         field39 = field(name="cube", type="SFNode", accessType="inputOutput",          ComposedCubeMapTexture40 = ComposedCubeMapTexture(USE="texture")), 
        field41 = field(name="chromaticDispertion", accessType="initializeOnly", type="SFVec3f", value="0.98 1.0 1.033"), 
        field42 = field(name="bias", type="SFFloat", accessType="inputOnly", value="0.5"), 
        field43 = field(name="scale", type="SFFloat", accessType="inputOnly", value="0.5"), 
        field44 = field(name="power", type="SFFloat", accessType="inputOnly", value="2"), 
        field45 = field(name="a", type="SFFloat", accessType="inputOnly", value="10"), 
        field46 = field(name="b", type="SFFloat", accessType="inputOnly", value="1"), 
        field47 = field(name="c", type="SFFloat", accessType="inputOnly", value="20"), 
        field48 = field(name="d", type="SFFloat", accessType="inputOnly", value="20"), 
        field49 = field(name="tdelta", type="SFFloat", accessType="inputOnly", value="0"), 
        field50 = field(name="pdelta", type="SFFloat", accessType="inputOnly", value="0"), 
        ShaderPart51 = ShaderPart(url=["../shaders/cobweb_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb_flowers_chromatic.vs"], type="VERTEX"), 
        ShaderPart52 = ShaderPart(url=["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"], type="FRAGMENT"))), 
      Sphere53 = Sphere(solid=False, radius=1))), 
    Script54 = Script(DEF="UrlSelector", directOutput=True,      field55 = field(name="frontUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\""), 
     field56 = field(name="backUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\""), 
     field57 = field(name="leftUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\""), 
     field58 = field(name="rightUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\""), 
     field59 = field(name="topUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\""), 
     field60 = field(name="bottomUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\""), 
     field61 = field(name="front", type="MFString", accessType="inputOutput"), 
     field62 = field(name="back", type="MFString", accessType="inputOutput"), 
     field63 = field(name="left", type="MFString", accessType="inputOutput"), 
     field64 = field(name="right", type="MFString", accessType="inputOutput"), 
     field65 = field(name="top", type="MFString", accessType="inputOutput"), 
     field66 = field(name="bottom", type="MFString", accessType="inputOutput"), 
     field67 = field(name="set_fraction", type="SFFloat", accessType="inputOnly"), 
     field68 = field(name="old", type="SFInt32", accessType="inputOutput", value="-1"),      sourceCode = '''\n"+
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
"''', ),     #
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

    Script69 = Script(DEF="Animate", directOutput=True,      field70 = field(name="set_fraction", type="SFFloat", accessType="inputOnly"), 
     field71 = field(name="a", type="SFFloat", accessType="inputOutput", value="10"), 
     field72 = field(name="b", type="SFFloat", accessType="inputOutput", value="1"), 
     field73 = field(name="c", type="SFFloat", accessType="inputOutput", value="20"), 
     field74 = field(name="d", type="SFFloat", accessType="inputOutput", value="20"), 
     field75 = field(name="tdelta", type="SFFloat", accessType="inputOutput", value="0"), 
     field76 = field(name="pdelta", type="SFFloat", accessType="inputOutput", value="0"),      sourceCode = '''\n"+
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
"''', ), 
    TimeSensor77 = TimeSensor(DEF="TourTime", cycleInterval=5, loop=True), 
    ROUTE78 = ROUTE(fromNode="TourTime", fromField="fraction_changed", toNode="Animate", toField="set_fraction"), 
    ROUTE79 = ROUTE(fromNode="Animate", fromField="a", toNode="cobweb", toField="a"), 
    ROUTE80 = ROUTE(fromNode="Animate", fromField="b", toNode="cobweb", toField="b"), 
    ROUTE81 = ROUTE(fromNode="Animate", fromField="c", toNode="cobweb", toField="c"), 
    ROUTE82 = ROUTE(fromNode="Animate", fromField="d", toNode="cobweb", toField="d"), 
    ROUTE83 = ROUTE(fromNode="Animate", fromField="pdelta", toNode="cobweb", toField="pdelta"), 
    ROUTE84 = ROUTE(fromNode="Animate", fromField="tdelta", toNode="cobweb", toField="tdelta"), 
    ROUTE85 = ROUTE(fromNode="Animate", fromField="a", toNode="x3dom", toField="a"), 
    ROUTE86 = ROUTE(fromNode="Animate", fromField="b", toNode="x3dom", toField="b"), 
    ROUTE87 = ROUTE(fromNode="Animate", fromField="c", toNode="x3dom", toField="c"), 
    ROUTE88 = ROUTE(fromNode="Animate", fromField="d", toNode="x3dom", toField="d"), 
    ROUTE89 = ROUTE(fromNode="Animate", fromField="pdelta", toNode="x3dom", toField="pdelta"), 
    ROUTE90 = ROUTE(fromNode="Animate", fromField="tdelta", toNode="x3dom", toField="tdelta")))
