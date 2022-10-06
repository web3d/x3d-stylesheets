from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    component2 = component(name="Shaders", level=1), 
    component3 = component(name="CubeMapTexturing", level=1), 
    meta4 = meta(name="title", content="flowerproto.x3d"), 
    meta5 = meta(name="creator", content="John Carlson"), 
    meta6 = meta(name="description", content="A flower proto with configurable shaders"), 
    meta7 = meta(name="generator", content="X3D-Edit, https://savage.nps.edu/X3D-Edit"), 
    meta8 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/flowerproto.x3d")), 
   Scene9 = Scene(    ProtoDeclare10 = ProtoDeclare(name="FlowerProto",      ProtoInterface11 = ProtoInterface(      field12 = field(accessType="inputOutput", name="vertex", type="MFString", value="\"../shaders/gl_flowers_chromatic.vs\""), 
      field13 = field(accessType="inputOutput", name="fragment", type="MFString", value="\"../shaders/pc_flowers.fs\"")), 
     ProtoBody14 = ProtoBody(      Transform15 = Transform(DEF="transform", translation=[0,0,0],        Shape16 = Shape(        Appearance17 = Appearance(         Material18 = Material(diffuseColor=[.7,.7,.7]), 
         ComposedCubeMapTexture19 = ComposedCubeMapTexture(DEF="texture",           ImageTexture20 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]), 
          ImageTexture21 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]), 
          ImageTexture22 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]), 
          ImageTexture23 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]), 
          ImageTexture24 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]), 
          ImageTexture25 = ImageTexture(url=["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])), 
         ComposedShader26 = ComposedShader(DEF="shader", language="GLSL",           field27 = field(name="cube", type="SFInt32", accessType="inputOutput", value="0"),           #
#                                <field name='cube' type='SFNode' accessType=\"inputOutput\">
#                                    <ComposedCubeMapTexture USE=\"texture\"/>
#                                </field>
#				

          field28 = field(name="chromaticDispertion", type="SFVec3f", accessType="inputOutput", value="0.98 1.0 1.033"), 
          field29 = field(name="bias", type="SFFloat", accessType="inputOutput", value="10"), 
          field30 = field(name="scale", type="SFFloat", accessType="inputOutput", value="10"), 
          field31 = field(name="power", type="SFFloat", accessType="inputOutput", value="2.0"), 
          field32 = field(name="a", type="SFFloat", accessType="inputOutput", value="3"), 
          field33 = field(name="b", type="SFFloat", accessType="inputOutput", value="1"), 
          field34 = field(name="c", type="SFFloat", accessType="inputOutput", value="3"), 
          field35 = field(name="d", type="SFFloat", accessType="inputOutput", value="3"), 
          field36 = field(name="tdelta", type="SFFloat", accessType="inputOutput", value="0.5"), 
          field37 = field(name="pdelta", type="SFFloat", accessType="inputOutput", value="0.5"), 
          ShaderPart38 = ShaderPart(type="VERTEX",            IS39 = IS(            connect40 = connect(nodeField="url", protoField="vertex"))), 
          ShaderPart41 = ShaderPart(type="FRAGMENT",            IS42 = IS(            connect43 = connect(nodeField="url", protoField="fragment"))))), 
        Sphere44 = Sphere()), 
       Script45 = Script(DEF="Bounce",         field46 = field(name="translation", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
        field47 = field(name="velocity", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
        field48 = field(name="set_fraction", accessType="inputOnly", type="SFTime"), 
        field49 = field(name="a", type="SFFloat", accessType="inputOutput", value="0.5"), 
        field50 = field(name="b", type="SFFloat", accessType="inputOutput", value="0.5"), 
        field51 = field(name="c", type="SFFloat", accessType="inputOutput", value="3"), 
        field52 = field(name="d", type="SFFloat", accessType="inputOutput", value="3"), 
        field53 = field(name="tdelta", type="SFFloat", accessType="inputOutput", value="0.5"), 
        field54 = field(name="pdelta", type="SFFloat", accessType="inputOutput", value="0.5"),         sourceCode = '''ecmascript:\n"+
"			function initialize() {\n"+
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
"			    for (var j = 0; j <= 2; j++) {\n"+
"				    if (Math.abs(translation.x) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.y) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.z) > 10) {\n"+
"					initialize();\n"+
"				    } else {\n"+
"					velocity.x += Math.random() * 0.2 - 0.1;\n"+
"					velocity.y += Math.random() * 0.2 - 0.1;\n"+
"					velocity.z += Math.random() * 0.2 - 0.1;\n"+
"				    }\n"+
"			    }\n"+
"			    animate_flowers();\n"+
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
"				tdelta += 0.5;\n"+
"				pdelta += 0.5;\n"+
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
"			}\n"+
"\n"+
"''', ), 
       TimeSensor55 = TimeSensor(DEF="TourTime", cycleInterval=0.150, loop=True), 
       ROUTE56 = ROUTE(fromNode="TourTime", fromField="cycleTime", toNode="Bounce", toField="set_fraction"), 
       ROUTE57 = ROUTE(fromNode="Bounce", fromField="translation_changed", toNode="transform", toField="set_translation"), 
       ROUTE58 = ROUTE(fromNode="Bounce", fromField="a", toNode="shader", toField="a"), 
       ROUTE59 = ROUTE(fromNode="Bounce", fromField="b", toNode="shader", toField="b"), 
       ROUTE60 = ROUTE(fromNode="Bounce", fromField="c", toNode="shader", toField="c"), 
       ROUTE61 = ROUTE(fromNode="Bounce", fromField="d", toNode="shader", toField="d"), 
       ROUTE62 = ROUTE(fromNode="Bounce", fromField="tdelta", toNode="shader", toField="tdelta"), 
       ROUTE63 = ROUTE(fromNode="Bounce", fromField="pdelta", toNode="shader", toField="pdelta"))))))
