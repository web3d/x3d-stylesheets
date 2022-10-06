from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(content="HeadsUpDisplayExample.x3d", name="title"), 
    meta3 = meta(content="Prototype definition that demonstrates use of a simple HeadsUpDisplay (HUD) prototype that maintains a stable position for its children on the screen.", name="description"), 
    meta4 = meta(content="Leonard Daly and Don Brutzman", name="creator"), 
    meta5 = meta(content="15 July 2006", name="created"), 
    meta6 = meta(content="24 October 2016", name="modified"), 
    meta7 = meta(content="HeadsUpDisplayPrototype.x3d", name="reference"), 
    meta8 = meta(content="http://X3dGraphics.com", name="reference"), 
    meta9 = meta(content="http://www.web3d.org/x3d/content/examples/X3dResources.html", name="reference"), 
    meta10 = meta(content="Copyright 2006, Daly Realism and Don Brutzman", name="rights"), 
    meta11 = meta(content="X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com", name="subject"), 
    meta12 = meta(content="http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayExample.x3d", name="identifier"), 
    meta13 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta14 = meta(content="../license.html", name="license")), 
   Scene15 = Scene(    # Simple Heads-Up Display (HUD) Prototype\\n \\n Manages the display of a HUD and maintains its position on the screen.\\n Changes to fieldOfView (in Viewpoint node) will change screen position\\n \\n Fields:\\n hudSize Size of HUD (initializeOnly - SFVec3f) default=\"1 1 .01\"\\n hudColor Color of HUD (inputOutput - SFColor) default=\"1 1 1\"\\n screenOffset Offset of HUD. This field positions the HUD on the display screen (inputOutput - SFVec3f) default=\"0 0 0\"\\n hudGeometry Geometry to be placed on the HUD. Origin is center of HUD. (inputOutput - MFNode) default = []\\n position_changed Current viewer location (outputOnly - SFVec3f)\\n orientation_changed Current viewer orientation (outputOnly - SFRotation)\\n \\n \\n 

    ExternProtoDeclare16 = ExternProtoDeclare(appinfo="Heads-up display (HUD) keeps child geometry aligned on screen in a consistent location", name="HeadsUpDisplay", url=["HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","HeadsUpDisplayPrototype.wrl#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.wrl#HeadsUpDisplay"],      field17 = field(accessType="inputOutput", appinfo="offset position for HUD relative to current view location, default 0 0 -5", name="screenOffset", type="SFVec3f"), 
     field18 = field(accessType="inputOutput", appinfo="X3D content positioned at HUD offset", name="children", type="MFNode"), 
     field19 = field(accessType="outputOnly", appinfo="HUD position update (in world coordinates) relative to original location", name="position_changed", type="SFVec3f"), 
     field20 = field(accessType="outputOnly", appinfo="HUD orientation update relative to original location", name="orientation_changed", type="SFRotation")), 
    Background21 = Background(DEF="SandyShallowBottom", groundAngle=[0.05,1.52,1.56,1.5707], groundColor=[0.2,0.2,0,0.3,0.3,0,0.5,0.5,0.3,0.1,0.3,0.4,0,0.2,0.4], skyAngle=[0.04,0.05,0.1,1.309,1.570], skyColor=[0.8,0.8,0.2,0.8,0.8,0.2,0.1,0.1,0.6,0.1,0.1,0.6,0.1,0.25,0.8,0.6,0.6,0.9]), 
    Viewpoint22 = Viewpoint(description="Heads-up display (HUD)"),     # ProtoDeclare is the \"cookie cutter\" template, ProtoInstance creates an actual occurrence 

    ProtoInstance23 = ProtoInstance(DEF="HeadsUpDisplayInstance", name="HeadsUpDisplay",      # example: upper left-hand corner of screen (x=-2, y=1) and set back z=-5 from user view 

     fieldValue24 = fieldValue(name="screenOffset", value="-0.75 1 -5"), 
     fieldValue25 = fieldValue(name="children",       Shape26 = Shape(       Text27 = Text(string=["HUD text stays fixed","while user navigates"],         FontStyle28 = FontStyle(justify=["MIDDLE","MIDDLE"], size=0.3)), 
       Appearance29 = Appearance(        Material30 = Material(diffuseColor=[0.894118,0.819608,1]))))), 
    Inline31 = Inline(url=["../HelloWorld.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.x3d","../HelloWorld.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.wrl"])))
