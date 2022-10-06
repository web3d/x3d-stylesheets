from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    component2 = component(name="Shaders", level=1), 
    component3 = component(name="CubeMapTexturing", level=1), 
    meta4 = meta(name="title", content="flowers4.x3d"), 
    meta5 = meta(name="creator", content="John Carlson"), 
    meta6 = meta(name="generator", content="manual"), 
    meta7 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/flowers4.x3d"), 
    meta8 = meta(name="description", content="an animated flower")), 
   Scene9 = Scene(    NavigationInfo10 = NavigationInfo(type=["EXAMINE","ANY"]), 
    Background11 = Background(backUrl=["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"], bottomUrl=["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"], frontUrl=["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"], leftUrl=["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"], rightUrl=["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"], topUrl=["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]), 
    Transform12 = Transform(DEF="transform",      Shape13 = Shape(      Appearance14 = Appearance(       Material15 = Material(diffuseColor=[.7,.7,.7], specularColor=[.5,.5,.5]), 
       ComposedCubeMapTexture16 = ComposedCubeMapTexture(        ImageTexture17 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]), 
        ImageTexture18 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]), 
        ImageTexture19 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]), 
        ImageTexture20 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]), 
        ImageTexture21 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]), 
        ImageTexture22 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])), 
       ComposedShader23 = ComposedShader(DEF="shader", language="GLSL",         field24 = field(name="cube", type="SFInt32", accessType="inputOutput", value="0"), 
        field25 = field(name="chromaticDispertion", accessType="inputOutput", type="SFVec3f", value="0.98 1.0 1.033"), 
        field26 = field(name="bias", type="SFFloat", accessType="inputOutput", value="0.5"), 
        field27 = field(name="scale", type="SFFloat", accessType="inputOutput", value="0.5"), 
        field28 = field(name="power", type="SFFloat", accessType="inputOutput", value="2"), 
        ShaderPart29 = ShaderPart(url=["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"], type="VERTEX"), 
        ShaderPart30 = ShaderPart(url=["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"], type="FRAGMENT"))),       #
#                <Sphere>
#		

      IndexedFaceSet31 = IndexedFaceSet(convex=False, DEF="Orbit", creaseAngle=0,        Coordinate32 = Coordinate(DEF="OrbitCoordinates")))), 
    Script33 = Script(DEF="OrbitScript",      field34 = field(accessType="inputOnly", name="set_fraction", type="SFFloat"), 
     field35 = field(accessType="inputOutput", name="coordinates", type="MFVec3f"), 
     field36 = field(accessType="outputOnly", name="coordIndexes", type="MFInt32"),      sourceCode = '''\n"+
"\n"+
"ecmascript:\n"+
"\n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"\n"+
"function initialize() {\n"+
"     resolution = 100;\n"+
"     updateCoordinates(resolution);\n"+
"     var cis = [];\n"+
"     for ( i = 0; i < resolution-1; i++) {\n"+
"     	for ( j = 0; j < resolution-1; j++) {\n"+
"	     cis.push(i*resolution+j);\n"+
"	     cis.push(i*resolution+j+1);\n"+
"	     cis.push((i+1)*resolution+j+1);\n"+
"	     cis.push((i+1)*resolution+j);\n"+
"	     cis.push(-1);\n"+
"	}\n"+
"    }\n"+
"    coordIndexes = new MFInt32(cis);\n"+
"}\n"+
"\n"+
"function updateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var crds = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta) * Math.cos(h * phi);\n"+
"		crds.push(new SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		));\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     coordinates = new MFVec3f(crds);\n"+
"}\n"+
"\n"+
"function set_fraction(fraction, eventTime) {\n"+
"	choice = Math.floor(Math.random() * 4);\n"+
"	switch (choice) {\n"+
"	case 0:\n"+
"		e += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 1:\n"+
"		f += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 2:\n"+
"		g += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 3:\n"+
"		h += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	}\n"+
"	if (f < 1) {\n"+
"		f = 10;\n"+
"	}\n"+
"	if (g < 1) {\n"+
"		g = 4;\n"+
"	}\n"+
"	if (h < 1) {\n"+
"		h = 4;\n"+
"	}\n"+
"	resolution = 100;\n"+
"	updateCoordinates(resolution);\n"+
"}\n"+
"      ''', ), 
    TimeSensor37 = TimeSensor(DEF="Clock", cycleInterval=16, loop=True), 
    ROUTE38 = ROUTE(fromField="coordIndexes", fromNode="OrbitScript", toField="set_coordIndex", toNode="Orbit"), 
    ROUTE39 = ROUTE(fromField="coordinates", fromNode="OrbitScript", toField="set_point", toNode="OrbitCoordinates"), 
    ROUTE40 = ROUTE(fromField="fraction_changed", fromNode="Clock", toField="set_fraction", toNode="OrbitScript")))
