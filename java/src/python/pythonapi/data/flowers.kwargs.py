from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    component2 = component(name="Shaders", level=1), 
    component3 = component(name="CubeMapTexturing", level=1), 
    meta4 = meta(name="title", content="flowers.x3d"), 
    meta5 = meta(name="creator", content="John Carlson"), 
    meta6 = meta(name="description", content="5 or more prismatic flowers"), 
    meta7 = meta(name="generator", content="X3D-Edit, https://savage.nps.edu/X3D-Edit"), 
    meta8 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/flowers.x3d")), 
   Scene9 = Scene(    NavigationInfo10 = NavigationInfo(type=["EXAMINE","ANY"]), 
    Background11 = Background(backUrl=["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"], bottomUrl=["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"], frontUrl=["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"], leftUrl=["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"], rightUrl=["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"], topUrl=["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]), 
    ProtoDeclare12 = ProtoDeclare(name="flower",      ProtoBody13 = ProtoBody(      Transform14 = Transform(DEF="transform", translation=[0,0,0],        Shape15 = Shape(        Appearance16 = Appearance(         Material17 = Material(diffuseColor=[.7,.7,.7], specularColor=[.5,.5,.5]), 
         ComposedCubeMapTexture18 = ComposedCubeMapTexture(DEF="texture",           ImageTexture19 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]), 
          ImageTexture20 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]), 
          ImageTexture21 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]), 
          ImageTexture22 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]), 
          ImageTexture23 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]), 
          ImageTexture24 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])), 
         ComposedShader25 = ComposedShader(language="GLSL",           field26 = field(name="xxxcube", type="SFInt32", accessType="inputOutput", value="0"), 
          field27 = field(name="cube", type="SFNode", accessType="inputOutput",            ComposedCubeMapTexture28 = ComposedCubeMapTexture(USE="texture")), 
          field29 = field(name="chromaticDispertion", type="SFVec3f", accessType="inputOutput", value="0.98 1.0 1.033"), 
          field30 = field(name="bias", type="SFFloat", accessType="inputOutput", value="0.5"), 
          field31 = field(name="scale", type="SFFloat", accessType="inputOutput", value="0.5"), 
          field32 = field(name="power", type="SFFloat", accessType="inputOutput", value="2.0"), 
          ShaderPart33 = ShaderPart(url=["../shaders/common.vs","https://coderextreme.net/X3DJSONLD/shaders/common.vs"], type="VERTEX"), 
          ShaderPart34 = ShaderPart(url=["../shaders/gl_flowers_chromatic.fs","https://coderextreme.net/X3DJSONLD/shaders/gl_flowers_chromatic.fs"], type="FRAGMENT")), 
         ComposedShader35 = ComposedShader(language="GLSL",           field36 = field(name="xxxcube", type="SFInt32", accessType="inputOutput", value="0"), 
          field37 = field(name="cube", type="SFNode", accessType="inputOutput",            ComposedCubeMapTexture38 = ComposedCubeMapTexture(USE="texture")), 
          field39 = field(name="chromaticDispertion", type="SFVec3f", accessType="inputOutput", value="0.98 1.0 1.033"), 
          field40 = field(name="bias", type="SFFloat", accessType="inputOutput", value="0.5"), 
          field41 = field(name="scale", type="SFFloat", accessType="inputOutput", value="0.5"), 
          field42 = field(name="power", type="SFFloat", accessType="inputOutput", value="2.0"), 
          ShaderPart43 = ShaderPart(url=["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"], type="VERTEX"), 
          ShaderPart44 = ShaderPart(url=["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"], type="FRAGMENT")), 
         ComposedShader45 = ComposedShader(DEF="shader", language="GLSL",           field46 = field(name="xxxcube", type="SFInt32", accessType="inputOutput", value="0"), 
          field47 = field(name="cube", type="SFNode", accessType="inputOutput",            ComposedCubeMapTexture48 = ComposedCubeMapTexture(USE="texture")), 
          field49 = field(name="chromaticDispertion", type="SFVec3f", accessType="inputOutput", value="0.98 1.0 1.033"), 
          field50 = field(name="bias", type="SFFloat", accessType="inputOutput", value="10"), 
          field51 = field(name="scale", type="SFFloat", accessType="inputOutput", value="10"), 
          field52 = field(name="power", type="SFFloat", accessType="inputOutput", value="2.0"), 
          ShaderPart53 = ShaderPart(url=["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"], type="VERTEX"), 
          ShaderPart54 = ShaderPart(url=["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"], type="FRAGMENT"))),         #
#			<Sphere></Sphere>
#			

        IndexedFaceSet55 = IndexedFaceSet(convex=False, DEF="Orbit", creaseAngle=0,          Coordinate56 = Coordinate(DEF="OrbitCoordinates")))), 
      Script57 = Script(DEF="Bounce",        field58 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
       field59 = field(name="velocity", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
       field60 = field(name="set_fraction", accessType="inputOnly", type="SFTime"), 
       field61 = field(accessType="inputOutput", name="coordinates", type="MFVec3f"), 
       field62 = field(accessType="outputOnly", name="coordIndexes", type="MFInt32"), 
       field63 = field(name="a", type="SFFloat", accessType="inputOutput", value="0.5"), 
       field64 = field(name="b", type="SFFloat", accessType="inputOutput", value="0.5"), 
       field65 = field(name="c", type="SFFloat", accessType="inputOutput", value="3"), 
       field66 = field(name="d", type="SFFloat", accessType="inputOutput", value="3"), 
       field67 = field(name="tdelta", type="SFFloat", accessType="inputOutput", value="0.5"), 
       field68 = field(name="pdelta", type="SFFloat", accessType="inputOutput", value="0.5"),        sourceCode = '''ecmascript:\n"+
"			function newBubble() {\n"+
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
"					newBubble();\n"+
"			    } else if (Math.abs(translation.y) > 10) {\n"+
"					newBubble();\n"+
"			    } else if (Math.abs(translation.z) > 10) {\n"+
"					newBubble();\n"+
"			    } else {\n"+
"					velocity = new SFVec3f(\n"+
"						velocity.x + Math.random() * 0.2 - 0.1,\n"+
"						velocity.y + Math.random() * 0.2 - 0.1,\n"+
"						velocity.z + Math.random() * 0.2 - 0.1\n"+
"					);\n"+
"			    }\n"+
"			    animate_flowers();\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     var cis = [];\n"+
"			     newBubble();\n"+
"			     resolution = 100;\n"+
"			     updateCoordinates(resolution);\n"+
"			     for ( i = 0; i < resolution-1; i++) {\n"+
"				for ( j = 0; j < resolution-1; j++) {\n"+
"				     cis.push(i*resolution+j);\n"+
"				     cis.push(i*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j);\n"+
"				     cis.push(-1);\n"+
"				}\n"+
"			    }\n"+
"			     coordIndexes = new MFInt32(cis);\n"+
"			}\n"+
"\n"+
"			function updateCoordinates(resolution) {\n"+
"			     theta = 0.0;\n"+
"			     phi = 0.0;\n"+
"			     delta = (2 * 3.141592653) / (resolution-1);\n"+
"			     var crds = [];\n"+
"			     for ( i = 0; i < resolution; i++) {\n"+
"				for ( j = 0; j < resolution; j++) {\n"+
"					rho = a + b * Math.cos(c * theta) * Math.cos(d * phi);\n"+
"					crds.push(new SFVec3f(\n"+
"						rho * Math.cos(phi) * Math.cos(theta),\n"+
"						rho * Math.cos(phi) * Math.sin(theta),\n"+
"						rho * Math.sin(phi)\n"+
"					));\n"+
"					theta += delta;\n"+
"				}\n"+
"				phi += delta;\n"+
"				coordinates = new MFVec3f(crds);\n"+
"			     }\n"+
"			}\n"+
"\n"+
"			function animate_flowers(fraction, eventTime) {\n"+
"				choice = Math.floor(Math.random() * 4);\n"+
"				switch (choice) {\n"+
"				case 0:\n"+
"					a += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 1:\n"+
"					b += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 2:\n"+
"					c += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				case 3:\n"+
"					d += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				}\n"+
"				if (a > 1) {\n"+
"					a =  0.5;\n"+
"				}\n"+
"				if (b > 1) {\n"+
"					b =  0.5;\n"+
"				}\n"+
"				if (c < 1) {\n"+
"					c =  4;\n"+
"				}\n"+
"				if (d < 1) {\n"+
"					d =  4;\n"+
"				}\n"+
"				if (c > 10) {\n"+
"					c = 4;\n"+
"				}\n"+
"				if (d > 10) {\n"+
"					d = 4;\n"+
"				}\n"+
"				resolution = 100;\n"+
"				updateCoordinates(resolution);\n"+
"			}\n"+
"\n"+
"''', ), 
      TimeSensor69 = TimeSensor(DEF="TourTime", cycleInterval=0.150, loop=True), 
      TimeSensor70 = TimeSensor(DEF="SongTime", loop=True), 
      Sound71 = Sound(maxBack=100, maxFront=100, minBack=20, minFront=20,        AudioClip72 = AudioClip(DEF="AudioClip", description="Chandubabamusic #1", url=["../resources/chandubabamusic1.wav"])), 
      ROUTE73 = ROUTE(fromField="cycleTime", fromNode="SongTime", toField="startTime", toNode="AudioClip"), 
      ROUTE74 = ROUTE(fromNode="TourTime", fromField="cycleTime", toNode="Bounce", toField="set_fraction"), 
      ROUTE75 = ROUTE(fromNode="Bounce", fromField="translation", toNode="transform", toField="set_translation"),       #
#		<ROUTE fromField=\"coordIndexes\" fromNode=\"Bounce\" toField=\"set_coordIndex\" toNode=\"Orbit\"/>
#		<ROUTE fromField=\"coordinates\" fromNode=\"Bounce\" toField=\"set_point\" toNode=\"OrbitCoordinates\"/>
#		
)), 
    Transform76 = Transform(     ProtoInstance77 = ProtoInstance(name="flower"),      #
#            <ProtoInstance name=\"flower\"/>
#            <ProtoInstance name=\"flower\"/>
#	    
)))
