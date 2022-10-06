from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    component2 = component(name="EnvironmentalEffects", level=1), 
    component3 = component(name="EnvironmentalEffects", level=3), 
    component4 = component(name="Shaders", level=1), 
    component5 = component(name="CubeMapTexturing", level=1), 
    meta6 = meta(name="title", content="bubbles.x3d"), 
    meta7 = meta(name="creator", content="John Carlson"), 
    meta8 = meta(name="generator", content="manual"), 
    meta9 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/bubbles.x3d"), 
    meta10 = meta(name="description", content="not sure what this is")), 
   Scene11 = Scene(    NavigationInfo12 = NavigationInfo(type=["EXAMINE"]), 
    Viewpoint13 = Viewpoint(DEF="Tour", description="Tour Views"), 
    Viewpoint14 = Viewpoint(position=[0,0,4], description="sphere in road"), 
    Background15 = Background(backUrl=["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"], bottomUrl=["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"], frontUrl=["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"], leftUrl=["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"], rightUrl=["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"], topUrl=["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"]), 
    Transform16 = Transform(DEF="Rose01",      Shape17 = Shape(      Sphere18 = Sphere(), 
      Appearance19 = Appearance(DEF="_01_-_Default",        Material20 = Material(diffuseColor=[0.7,0.7,0.7], specularColor=[0.5,0.5,0.5]), 
       ComposedCubeMapTexture21 = ComposedCubeMapTexture(        ImageTexture22 = ImageTexture(url=["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"]), 
        ImageTexture23 = ImageTexture(url=["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"]), 
        ImageTexture24 = ImageTexture(url=["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"]), 
        ImageTexture25 = ImageTexture(url=["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"]), 
        ImageTexture26 = ImageTexture(url=["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"]), 
        ImageTexture27 = ImageTexture(url=["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"])), 
       ComposedShader28 = ComposedShader(DEF="cobweb", language="GLSL",         field29 = field(name="cube", accessType="inputOutput", type="SFInt32", value="0"), 
        field30 = field(name="chromaticDispertion", accessType="inputOutput", type="SFVec3f", value="0.98 1 1.033"), 
        field31 = field(name="bias", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field32 = field(name="scale", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field33 = field(name="power", accessType="inputOutput", type="SFFloat", value="2"), 
        ShaderPart34 = ShaderPart(url=["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"], type="VERTEX"), 
        ShaderPart35 = ShaderPart(url=["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"], type="FRAGMENT")), 
       ComposedShader36 = ComposedShader(DEF="x3dom", language="GLSL",         field37 = field(name="cube", accessType="inputOutput", type="SFInt32", value="0"), 
        field38 = field(name="chromaticDispertion", accessType="inputOutput", type="SFVec3f", value="0.98 1 1.033"), 
        field39 = field(name="bias", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field40 = field(name="scale", accessType="inputOutput", type="SFFloat", value="0.5"), 
        field41 = field(name="power", accessType="inputOutput", type="SFFloat", value="2"), 
        ShaderPart42 = ShaderPart(url=["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"], type="VERTEX"), 
        ShaderPart43 = ShaderPart(url=["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"], type="FRAGMENT"))))), 
    TimeSensor44 = TimeSensor(DEF="TourTime", cycleInterval=5, loop=True), 
    PositionInterpolator45 = PositionInterpolator(DEF="TourPosition", key=[0,1], keyValue=[0,0,10,0,0,-10]), 
    OrientationInterpolator46 = OrientationInterpolator(DEF="TourOrientation", key=[0,1], keyValue=[0,1,0,0,0,1,0,3.1416]), 
    Script47 = Script(DEF="RandomTourTime",      field48 = field(name="set_cycle", accessType="inputOnly", type="SFTime"), 
     field49 = field(name="lastKey", accessType="inputOutput", type="SFFloat", value="0"), 
     field50 = field(name="orientations", accessType="inputOutput", type="MFRotation", value="0 1 0 0 0 1 0 -1.57 0 1 0 3.14 0 1 0 1.57 0 1 0 0 1 0 0 -1.57 0 1 0 0 1 0 0 1.57 0 1 0 0"), 
     field51 = field(name="positions", accessType="inputOutput", type="MFVec3f", value="0 0 10 -10 0 0 0 0 -10 10 0 0 0 0 10 0 10 0 0 0 10 0 -10 0 0 0 10"), 
     field52 = field(name="position_changed", accessType="outputOnly", type="MFVec3f"), 
     field53 = field(name="set_orientation", accessType="inputOnly", type="MFRotation"), 
     field54 = field(name="orientation_changed", accessType="outputOnly", type="MFRotation"),      sourceCode = '''ecmascript:\n"+
"               function set_cycle(value) {\n"+
"                        var ov = lastKey;\n"+
"                        do {\n"+
"                            lastKey = Math.round(Math.random()*(positions.length-1));\n"+
"                        } while (lastKey === ov);\n"+
"                        var vc = lastKey;\n"+
"                        \n"+
"                        orientation_changed = new MFRotation();\n"+
"                        orientation_changed[0] = new SFRotation(orientations[ov].x, orientations[ov].y, orientations[ov].z, orientations[ov].w);\n"+
"                        orientation_changed[1] = new SFRotation(orientations[vc].x, orientations[vc].y, orientations[vc].z, orientations[vc].w);\n"+
"                        position_changed = new MFVec3f();\n"+
"                        position_changed[0] = new SFVec3f(positions[ov].x,positions[ov].y,positions[ov].z);\n"+
"                        position_changed[1] = new SFVec3f(positions[vc].x,positions[vc].y,positions[vc].z);\n"+
"                    // }\n"+
"               }''', ), 
    ROUTE55 = ROUTE(fromNode="TourTime", fromField="cycleTime_changed", toNode="RandomTourTime", toField="set_cycle"), 
    ROUTE56 = ROUTE(fromNode="RandomTourTime", fromField="orientation_changed", toNode="TourOrientation", toField="set_keyValue"), 
    ROUTE57 = ROUTE(fromNode="RandomTourTime", fromField="position_changed", toNode="TourPosition", toField="set_keyValue"), 
    ROUTE58 = ROUTE(fromNode="TourTime", fromField="fraction_changed", toNode="TourOrientation", toField="set_fraction"), 
    ROUTE59 = ROUTE(fromNode="TourOrientation", fromField="value_changed", toNode="Tour", toField="set_orientation"), 
    ROUTE60 = ROUTE(fromNode="TourTime", fromField="fraction_changed", toNode="TourPosition", toField="set_fraction"), 
    ROUTE61 = ROUTE(fromNode="TourPosition", fromField="value_changed", toNode="Tour", toField="set_position")))
