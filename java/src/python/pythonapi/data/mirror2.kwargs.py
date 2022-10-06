from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    component2 = component(name="Shaders", level=1), 
    component3 = component(name="CubeMapTexturing", level=1), 
    meta4 = meta(name="title", content="mirro2.x3d"), 
    meta5 = meta(name="creator", content="John Carlson"), 
    meta6 = meta(name="generator", content="manual"), 
    meta7 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/mirro2.x3d"), 
    meta8 = meta(name="description", content="a mirrored sphere")), 
   Scene9 = Scene(    Viewpoint10 = Viewpoint(position=[0,5,100], description="Switch background and images texture"), 
    Background11 = Background(DEF="cube", leftUrl=["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"], rightUrl=["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"], frontUrl=["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"], backUrl=["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"], topUrl=["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"], bottomUrl=["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]), 
    Transform12 = Transform(     Shape13 = Shape(      Appearance14 = Appearance(       Material15 = Material(diffuseColor=[.7,.7,.7], specularColor=[.5,.5,.5]), 
       ComposedCubeMapTexture16 = ComposedCubeMapTexture(        ImageTexture17 = ImageTexture(DEF="backShader", url=["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]), 
        ImageTexture18 = ImageTexture(DEF="bottomShader", url=["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]), 
        ImageTexture19 = ImageTexture(DEF="frontShader", url=["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]), 
        ImageTexture20 = ImageTexture(DEF="leftShader", url=["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]), 
        ImageTexture21 = ImageTexture(DEF="rightShader", url=["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]), 
        ImageTexture22 = ImageTexture(DEF="topShader", url=["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"])), 
       ComposedShader23 = ComposedShader(DEF="cobweb", language="GLSL",         #http://hypertextbook.com/facts/2005/JustinChe.shtml

        field24 = field(name="chromaticDispertion", accessType="inputOutput", type="SFVec3f", value="0.98 1 1.033"), 
        field25 = field(name="cube", accessType="inputOutput", type="SFInt32", value="0"), 
        field26 = field(name="bias", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field27 = field(name="scale", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field28 = field(name="power", accessType="inputOutput", type="SFFloat", value="2"), 
        ShaderPart29 = ShaderPart(url=["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"], type="VERTEX"), 
        ShaderPart30 = ShaderPart(url=["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"], type="FRAGMENT")), 
       ComposedShader31 = ComposedShader(DEF="x3dom", language="GLSL",         #http://hypertextbook.com/facts/2005/JustinChe.shtml

        field32 = field(name="chromaticDispertion", accessType="inputOutput", type="SFVec3f", value="0.98 1 1.033"), 
        field33 = field(name="cube", accessType="inputOutput", type="SFInt32", value="0"), 
        field34 = field(name="bias", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field35 = field(name="scale", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field36 = field(name="power", accessType="inputOutput", type="SFFloat", value="2"), 
        ShaderPart37 = ShaderPart(url=["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"], type="VERTEX"), 
        ShaderPart38 = ShaderPart(url=["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"], type="FRAGMENT"))), 
      Sphere39 = Sphere(radius=30)), 
     Script40 = Script(DEF="UrlSelector", directOutput=True,       field41 = field(name="frontUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\""), 
      field42 = field(name="backUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\""), 
      field43 = field(name="leftUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\""), 
      field44 = field(name="rightUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\""), 
      field45 = field(name="topUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\""), 
      field46 = field(name="bottomUrls", type="MFString", accessType="initializeOnly", value="\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\""), 
      field47 = field(name="front_changed", type="MFString", accessType="outputOnly"), 
      field48 = field(name="back_changed", type="MFString", accessType="outputOnly"), 
      field49 = field(name="left_changed", type="MFString", accessType="outputOnly"), 
      field50 = field(name="right_changed", type="MFString", accessType="outputOnly"), 
      field51 = field(name="top_changed", type="MFString", accessType="outputOnly"), 
      field52 = field(name="bottom_changed", type="MFString", accessType="outputOnly"), 
      field53 = field(name="set_fraction", type="SFFloat", accessType="inputOnly"), 
      field54 = field(name="old", type="SFInt32", accessType="inputOutput", value="-1"),       sourceCode = '''\n"+
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
"''', ), 
     TimeSensor55 = TimeSensor(DEF="Clock", cycleInterval=45, loop=True), 
     ROUTE56 = ROUTE(fromNode="Clock", fromField="fraction_changed", toNode="UrlSelector", toField="set_fraction"), 
     ROUTE57 = ROUTE(fromNode="UrlSelector", fromField="front_changed", toNode="cube", toField="frontUrl"), 
     ROUTE58 = ROUTE(fromNode="UrlSelector", fromField="back_changed", toNode="cube", toField="backUrl"), 
     ROUTE59 = ROUTE(fromNode="UrlSelector", fromField="left_changed", toNode="cube", toField="leftUrl"), 
     ROUTE60 = ROUTE(fromNode="UrlSelector", fromField="right_changed", toNode="cube", toField="rightUrl"), 
     ROUTE61 = ROUTE(fromNode="UrlSelector", fromField="top_changed", toNode="cube", toField="topUrl"), 
     ROUTE62 = ROUTE(fromNode="UrlSelector", fromField="bottom_changed", toNode="cube", toField="bottomUrl"), 
     ROUTE63 = ROUTE(fromNode="UrlSelector", fromField="front_changed", toNode="frontShader", toField="url"), 
     ROUTE64 = ROUTE(fromNode="UrlSelector", fromField="back_changed", toNode="backShader", toField="url"), 
     ROUTE65 = ROUTE(fromNode="UrlSelector", fromField="left_changed", toNode="leftShader", toField="url"), 
     ROUTE66 = ROUTE(fromNode="UrlSelector", fromField="right_changed", toNode="rightShader", toField="url"), 
     ROUTE67 = ROUTE(fromNode="UrlSelector", fromField="top_changed", toNode="topShader", toField="url"), 
     ROUTE68 = ROUTE(fromNode="UrlSelector", fromField="bottom_changed", toNode="bottomShader", toField="url"))))
