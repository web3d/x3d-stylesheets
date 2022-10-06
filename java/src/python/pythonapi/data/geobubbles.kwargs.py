from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    component2 = component(level=1, name="Geospatial"), 
    meta3 = meta(name="title", content="geobubbles.x3d"), 
    meta4 = meta(name="creator", content="John Carlson"), 
    meta5 = meta(name="generator", content="manual"), 
    meta6 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/geobubbles.x3d"), 
    meta7 = meta(name="description", content="geo bubbles")), 
   Scene8 = Scene(    #Viewpoint DEF='Tour' position='0 0 4' orientation='1 0 0 0' description='Tour Views'/
    #PositionInterpolator DEF='TourPosition' key='0 1' keyValue='-0.5 -0.5 4 -0.5 0.5 4'/

    GeoViewpoint9 = GeoViewpoint(geoSystem=["GD","WE"], DEF="Tour", position=[0,0,4], orientation=[1,0,0,0], description="Tour Views", retainUserOffsets=False), 
    Background10 = Background(backUrl=["../resources/images/BK.png","https://coderextreme.net/X3DJSONLD/images/BK.png"], bottomUrl=["../resources/images/BT.png","https://coderextreme.net/X3DJSONLD/images/BT.png"], frontUrl=["../resources/images/FR.png","https://coderextreme.net/X3DJSONLD/images/FR.png"], leftUrl=["../resources/images/LF.png","https://coderextreme.net/X3DJSONLD/images/LF.png"], rightUrl=["../resources/images/RT.png","https://coderextreme.net/X3DJSONLD/images/RT.png"], topUrl=["../resources/images/TP.png","https://coderextreme.net/X3DJSONLD/images/TP.png"]), 
    Transform11 = Transform(     Shape12 = Shape(      Sphere13 = Sphere(), 
      Appearance14 = Appearance(       Material15 = Material(diffuseColor=[0.7,0.7,0.7], specularColor=[0.5,0.5,0.5])))), 
    TimeSensor16 = TimeSensor(DEF="TourTime", cycleInterval=5, loop=True), 
    GeoPositionInterpolator17 = GeoPositionInterpolator(geoSystem=["GD","WE"], DEF="TourPosition", key=[0,1], keyValue=[0.0015708,0,4,0,0.0015708,4]), 
    Script18 = Script(DEF="RandomTourTime",      field19 = field(name="set_cycle", accessType="inputOnly", type="SFTime"), 
     field20 = field(name="val", accessType="inputOutput", type="SFFloat", value="0"), 
     field21 = field(name="positions", accessType="inputOutput", type="MFVec3d", value="0.0015708 0 4 0 0.0015708 4"), 
     field22 = field(name="position", accessType="inputOutput", type="MFVec3d", value="0.0015708 0 4 0 0.0015708 4"),      sourceCode = '''ecmascript:\n"+
"\n"+
"               function set_cycle(value) {\n"+
"                        var cartesianMult = -150;  // -150 if cartesian, 1 if geo\n"+
"                        var ov = val;\n"+
"			// Browser.print('old '+ov);\n"+
"                        do {\n"+
"                                val = Math.floor(Math.random()*2);\n"+
"                                var vc = val;\n"+
"                                positions[vc] = new SFVec3d(Math.round(Math.random()*2)*0.0015708*cartesianMult, Math.round(Math.random()*2)*0.0015708*cartesianMult, 4);\n"+
"                        } while ( positions[ov][0] === positions[vc][0] && positions[ov][1] === positions[vc][1] && positions[ov][2] === positions[vc][2]);\n"+
"			// Browser.println(positions[ov]);\n"+
"			// Browser.println(positions[vc]);\n"+
"                        position = new MFVec3d();\n"+
"                        position[0] = new SFVec3d(positions[ov][0],positions[ov][1],positions[ov][2]);\n"+
"                        position[1] = new SFVec3d(positions[vc][0],positions[vc][1],positions[vc][2]);\n"+
"               }''', ), 
    ROUTE23 = ROUTE(fromNode="TourTime", fromField="cycleTime", toNode="RandomTourTime", toField="set_cycle"), 
    ROUTE24 = ROUTE(fromNode="RandomTourTime", fromField="position", toNode="TourPosition", toField="keyValue"), 
    ROUTE25 = ROUTE(fromNode="TourTime", fromField="fraction_changed", toNode="TourPosition", toField="set_fraction"), 
    ROUTE26 = ROUTE(fromNode="TourPosition", fromField="geovalue_changed", toNode="Tour", toField="set_position")))
