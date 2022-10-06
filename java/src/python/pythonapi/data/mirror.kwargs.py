from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    component2 = component(name="EnvironmentalEffects", level=3), 
    component3 = component(name="Shaders", level=1), 
    component4 = component(name="CubeMapTexturing", level=1), 
    meta5 = meta(name="title", content="mirror.x3d"), 
    meta6 = meta(name="creator", content="John Carlson"), 
    meta7 = meta(name="generator", content="manual"), 
    meta8 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/mirror.x3d"), 
    meta9 = meta(name="description", content="sphere with alternating backgrounds")), 
   Scene10 = Scene(    Viewpoint11 = Viewpoint(position=[0,5,100], description="Switch background and images texture"), 
    TextureBackground12 = TextureBackground(     ImageTexture13 = ImageTexture(DEF="leftBack", url=["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]), 
     ImageTexture14 = ImageTexture(DEF="rightBack", url=["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]), 
     ImageTexture15 = ImageTexture(DEF="frontBack", url=["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]), 
     ImageTexture16 = ImageTexture(DEF="backBack", url=["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]), 
     ImageTexture17 = ImageTexture(DEF="topBack", url=["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"]), 
     ImageTexture18 = ImageTexture(DEF="bottomBack", url=["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"])), 
    Transform19 = Transform(     Shape20 = Shape(      Appearance21 = Appearance(       Material22 = Material(diffuseColor=[.7,.7,.7], specularColor=[.5,.5,.5]), 
       ComposedCubeMapTexture23 = ComposedCubeMapTexture(        ImageTexture24 = ImageTexture(DEF="backShader", url=["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]), 
        ImageTexture25 = ImageTexture(DEF="bottomShader", url=["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]), 
        ImageTexture26 = ImageTexture(DEF="frontShader", url=["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]), 
        ImageTexture27 = ImageTexture(DEF="leftShader", url=["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]), 
        ImageTexture28 = ImageTexture(DEF="rightShader", url=["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]), 
        ImageTexture29 = ImageTexture(DEF="topShader", url=["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"])), 
       ComposedShader30 = ComposedShader(DEF="x3dom", language="GLSL",         #http://hypertextbook.com/facts/2005/JustinChe.shtml

        field31 = field(name="chromaticDispertion", accessType="inputOutput", type="SFVec3f", value="0.98 1 1.033"), 
        field32 = field(name="cube", accessType="inputOutput", type="SFInt32", value="0"), 
        field33 = field(name="bias", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field34 = field(name="scale", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field35 = field(name="power", accessType="inputOutput", type="SFFloat", value="2"), 
        ShaderPart36 = ShaderPart(url=["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"], type="VERTEX"), 
        ShaderPart37 = ShaderPart(url=["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"], type="FRAGMENT")), 
       ComposedShader38 = ComposedShader(DEF="cobweb", language="GLSL",         #http://hypertextbook.com/facts/2005/JustinChe.shtml

        field39 = field(name="chromaticDispertion", accessType="inputOutput", type="SFVec3f", value="0.98 1 1.033"), 
        field40 = field(name="cube", accessType="inputOutput", type="SFInt32", value="0"), 
        field41 = field(name="bias", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field42 = field(name="scale", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field43 = field(name="power", accessType="inputOutput", type="SFFloat", value="2"), 
        ShaderPart44 = ShaderPart(url=["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"], type="VERTEX"), 
        ShaderPart45 = ShaderPart(url=["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"], type="FRAGMENT"))), 
      Sphere46 = Sphere(radius=30)), 
     Script47 = Script(DEF="UrlSelector", directOutput=True,       field48 = field(name="frontUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\""), 
      field49 = field(name="backUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\""), 
      field50 = field(name="leftUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\""), 
      field51 = field(name="rightUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\""), 
      field52 = field(name="topUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\""), 
      field53 = field(name="bottomUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\""), 
      field54 = field(name="front_changed", type="MFString", accessType="outputOnly"), 
      field55 = field(name="back_changed", type="MFString", accessType="outputOnly"), 
      field56 = field(name="left_changed", type="MFString", accessType="outputOnly"), 
      field57 = field(name="right_changed", type="MFString", accessType="outputOnly"), 
      field58 = field(name="top_changed", type="MFString", accessType="outputOnly"), 
      field59 = field(name="bottom_changed", type="MFString", accessType="outputOnly"), 
      field60 = field(name="set_fraction", type="SFFloat", accessType="inputOnly"), 
      field61 = field(name="old", type="SFInt32", accessType="inputOutput", value="-1"),       sourceCode = '''\n"+
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
"''', ), 
     TimeSensor62 = TimeSensor(DEF="Clock", cycleInterval=45, loop=True), 
     ROUTE63 = ROUTE(fromNode="Clock", fromField="fraction_changed", toNode="UrlSelector", toField="set_fraction"), 
     ROUTE64 = ROUTE(fromNode="UrlSelector", fromField="front_changed", toNode="frontBack", toField="url"), 
     ROUTE65 = ROUTE(fromNode="UrlSelector", fromField="back_changed", toNode="backBack", toField="url"), 
     ROUTE66 = ROUTE(fromNode="UrlSelector", fromField="left_changed", toNode="leftBack", toField="url"), 
     ROUTE67 = ROUTE(fromNode="UrlSelector", fromField="right_changed", toNode="rightBack", toField="url"), 
     ROUTE68 = ROUTE(fromNode="UrlSelector", fromField="top_changed", toNode="topBack", toField="url"), 
     ROUTE69 = ROUTE(fromNode="UrlSelector", fromField="bottom_changed", toNode="bottomBack", toField="url"), 
     ROUTE70 = ROUTE(fromNode="UrlSelector", fromField="front_changed", toNode="frontShader", toField="url"), 
     ROUTE71 = ROUTE(fromNode="UrlSelector", fromField="back_changed", toNode="backShader", toField="url"), 
     ROUTE72 = ROUTE(fromNode="UrlSelector", fromField="left_changed", toNode="leftShader", toField="url"), 
     ROUTE73 = ROUTE(fromNode="UrlSelector", fromField="right_changed", toNode="rightShader", toField="url"), 
     ROUTE74 = ROUTE(fromNode="UrlSelector", fromField="top_changed", toNode="topShader", toField="url"), 
     ROUTE75 = ROUTE(fromNode="UrlSelector", fromField="bottom_changed", toNode="bottomShader", toField="url"))))
