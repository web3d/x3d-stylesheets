from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.content = "HeadsUpDisplayExample.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Prototype definition that demonstrates use of a simple HeadsUpDisplay (HUD) prototype that maintains a stable position for its children on the screen."
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Leonard Daly and Don Brutzman"
meta4.name = "creator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "15 July 2006"
meta5.name = "created"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "24 October 2016"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "HeadsUpDisplayPrototype.x3d"
meta7.name = "reference"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "http://X3dGraphics.com"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "http://www.web3d.org/x3d/content/examples/X3dResources.html"
meta9.name = "reference"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "Copyright 2006, Daly Realism and Don Brutzman"
meta10.name = "rights"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com"
meta11.name = "subject"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayExample.x3d"
meta12.name = "identifier"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta13.name = "generator"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "../license.html"
meta14.name = "license"
head1.addMeta([meta14])
X3D0.head = head1

Scene15 = Scene()
# Simple Heads-Up Display (HUD) Prototype\\n \\n Manages the display of a HUD and maintains its position on the screen.\\n Changes to fieldOfView (in Viewpoint node) will change screen position\\n \\n Fields:\\n hudSize Size of HUD (initializeOnly - SFVec3f) default=\"1 1 .01\"\\n hudColor Color of HUD (inputOutput - SFColor) default=\"1 1 1\"\\n screenOffset Offset of HUD. This field positions the HUD on the display screen (inputOutput - SFVec3f) default=\"0 0 0\"\\n hudGeometry Geometry to be placed on the HUD. Origin is center of HUD. (inputOutput - MFNode) default = []\\n position_changed Current viewer location (outputOnly - SFVec3f)\\n orientation_changed Current viewer orientation (outputOnly - SFRotation)\\n \\n \\n 

ExternProtoDeclare16 = ExternProtoDeclare()
ExternProtoDeclare16.appinfo = "Heads-up display (HUD) keeps child geometry aligned on screen in a consistent location"
ExternProtoDeclare16.name = "HeadsUpDisplay"
ExternProtoDeclare16.url = ["HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","HeadsUpDisplayPrototype.wrl#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.wrl#HeadsUpDisplay"]

field17 = field()
field17.accessType = "inputOutput"
field17.appinfo = "offset position for HUD relative to current view location, default 0 0 -5"
field17.name = "screenOffset"
field17.type = "SFVec3f"
ExternProtoDeclare16.addField([field17])

field18 = field()
field18.accessType = "inputOutput"
field18.appinfo = "X3D content positioned at HUD offset"
field18.name = "children"
field18.type = "MFNode"
ExternProtoDeclare16.addField([field18])

field19 = field()
field19.accessType = "outputOnly"
field19.appinfo = "HUD position update (in world coordinates) relative to original location"
field19.name = "position_changed"
field19.type = "SFVec3f"
ExternProtoDeclare16.addField([field19])

field20 = field()
field20.accessType = "outputOnly"
field20.appinfo = "HUD orientation update relative to original location"
field20.name = "orientation_changed"
field20.type = "SFRotation"
ExternProtoDeclare16.addField([field20])
Scene15.addChildren([ExternProtoDeclare16])

Background21 = Background()
Background21.DEF = "SandyShallowBottom"
Background21.groundAngle = [0.05,1.52,1.56,1.5707]
Background21.groundColor = [0.2,0.2,0,0.3,0.3,0,0.5,0.5,0.3,0.1,0.3,0.4,0,0.2,0.4]
Background21.skyAngle = [0.04,0.05,0.1,1.309,1.570]
Background21.skyColor = [0.8,0.8,0.2,0.8,0.8,0.2,0.1,0.1,0.6,0.1,0.1,0.6,0.1,0.25,0.8,0.6,0.6,0.9]
Scene15.addChildren([Background21])

Viewpoint22 = Viewpoint()
Viewpoint22.description = "Heads-up display (HUD)"
Scene15.addChildren([Viewpoint22])
# ProtoDeclare is the \"cookie cutter\" template, ProtoInstance creates an actual occurrence 

ProtoInstance23 = ProtoInstance()
ProtoInstance23.DEF = "HeadsUpDisplayInstance"
ProtoInstance23.name = "HeadsUpDisplay"
# example: upper left-hand corner of screen (x=-2, y=1) and set back z=-5 from user view 

fieldValue24 = fieldValue()
fieldValue24.name = "screenOffset"
fieldValue24.value = "-0.75 1 -5"
ProtoInstance23.addFieldValue([fieldValue24])

fieldValue25 = fieldValue()
fieldValue25.name = "children"

Shape26 = Shape()

Text27 = Text()
Text27.string = ["HUD text stays fixed","while user navigates"]

FontStyle28 = FontStyle(justify = ["MIDDLE","MIDDLE"], size = 0.3)
Text27.fontStyle = FontStyle28
Shape26.geometry = Text27

Appearance29 = Appearance()

Material30 = Material()
Material30.diffuseColor = [0.894118,0.819608,1]
Appearance29.material = Material30
Shape26.appearance = Appearance29
fieldValue25.addChildren([Shape26])
ProtoInstance23.addFieldValue([fieldValue25])
Scene15.addChildren([ProtoInstance23])

Inline31 = Inline()
Inline31.url = ["../HelloWorld.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.x3d","../HelloWorld.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.wrl"]
Scene15.addChildren([Inline31])
X3D0.scene = Scene15
