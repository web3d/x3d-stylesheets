from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

component2 = component()
component2.level = 1
component2.name = "Geospatial"
head1.addComponent([component2])

component3 = component()
component3.level = 2
component3.name = "NURBS"
head1.addComponent([component3])

component4 = component()
component4.level = 2
component4.name = "Core"
head1.addComponent([component4])

component5 = component()
component5.level = 1
component5.name = "Navigation"
head1.addComponent([component5])

component6 = component()
component6.level = 1
component6.name = "Text"
head1.addComponent([component6])

meta7 = meta()
meta7.content = "X3dHeaderPrototypeSyntaxExamples.x3d"
meta7.name = "title"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "X3D scene header and prototype syntax examples. This example header indicates that the content is XML encoded, follows the Interactive Profile and explicitly lists additional necessary components. The X3D header may also contain additional semantic information. Used for specification EXAMPLE excerpts in 19776:1 XML Encoding."
meta8.name = "description"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "14 October 2002"
meta9.name = "created"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "7 May 2017"
meta10.name = "modified"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "Don Brutzman"
meta11.name = "creator"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "X3D encodings, ISO/IEC 19776-1.3, Part 1: XML encoding, 4.3 XML file syntax"
meta12.name = "specificationSection"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "http://www.web3d.org/documents/specifications/19776-1/V3.3/Part01/concepts.html#XMLFileSyntax"
meta13.name = "specificationUrl"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/X3dHeaderPrototypeSyntaxExamples.x3d"
meta14.name = "identifier"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta15.name = "generator"
head1.addMeta([meta15])

meta16 = meta()
meta16.content = "../license.html"
meta16.name = "license"
head1.addMeta([meta16])
X3D0.head = head1

Scene17 = Scene()

ExternProtoDeclare18 = ExternProtoDeclare()
ExternProtoDeclare18.name = "ViewPositionOrientation"
ExternProtoDeclare18.url = ["../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation"]

field19 = field()
field19.accessType = "inputOutput"
field19.name = "enabled"
field19.type = "SFBool"
ExternProtoDeclare18.addField([field19])

field20 = field()
field20.accessType = "initializeOnly"
field20.name = "traceEnabled"
field20.type = "SFBool"
ExternProtoDeclare18.addField([field20])

field21 = field()
field21.accessType = "inputOnly"
field21.name = "set_traceEnabled"
field21.type = "SFBool"
ExternProtoDeclare18.addField([field21])

field22 = field()
field22.accessType = "outputOnly"
field22.name = "position_changed"
field22.type = "SFVec3f"
ExternProtoDeclare18.addField([field22])

field23 = field()
field23.accessType = "outputOnly"
field23.name = "orientation_changed"
field23.type = "SFRotation"
ExternProtoDeclare18.addField([field23])

field24 = field()
field24.accessType = "outputOnly"
field24.name = "outputViewpointString"
field24.type = "MFString"
ExternProtoDeclare18.addField([field24])
Scene17.addChildren([ExternProtoDeclare18])

ProtoDeclare25 = ProtoDeclare()
ProtoDeclare25.name = "NewWorldInfoNode"

ProtoBody26 = ProtoBody()

WorldInfo27 = WorldInfo()
WorldInfo27.DEF = "ExamplePrototypeBody"
ProtoBody26.addChildren([WorldInfo27])
ProtoDeclare25.protoBody = ProtoBody26
Scene17.addChildren([ProtoDeclare25])

ProtoInstance28 = ProtoInstance()
ProtoInstance28.name = "NewWorldInfoNode"
Scene17.addChildren([ProtoInstance28])

ProtoDeclare29 = ProtoDeclare()
ProtoDeclare29.name = "EmissiveMaterial"

ProtoInterface30 = ProtoInterface()

field31 = field()
field31.accessType = "inputOutput"
field31.name = "onlyColor"
field31.type = "SFColor"
field31.value = "1 0 0"
ProtoInterface30.addField([field31])
ProtoDeclare29.protoInterface = ProtoInterface30

ProtoBody32 = ProtoBody()
# Override default diffuseColor value 0.8 0.8 0.8 

Material33 = Material()
Material33.diffuseColor = [0,0,0]
# Connect emissiveColor field of current node to onlyColor field of parent ProtoDeclare. 

IS34 = IS()

connect35 = connect()
connect35.nodeField = "emissiveColor"
connect35.protoField = "onlyColor"
IS34.addConnect([connect35])
Material33.IS = IS34
ProtoBody32.addChildren([Material33])
ProtoDeclare29.protoBody = ProtoBody32
Scene17.addChildren([ProtoDeclare29])

ProtoDeclare36 = ProtoDeclare()
ProtoDeclare36.name = "ShiftGroupUp2m"

ProtoInterface37 = ProtoInterface()

field38 = field()
field38.accessType = "inputOutput"
field38.name = "children"
field38.type = "MFNode"

Group39 = Group(bboxSize = [2,2,2])
Group39.DEF = "DefaultNodeValue"
# Authors need to override this node when creating the ProtoInstance fieldValue name=\"children\" 
field38.addChildren([Group39])
ProtoInterface37.addField([field38])
ProtoDeclare36.protoInterface = ProtoInterface37

ProtoBody40 = ProtoBody()

Transform41 = Transform()
Transform41.translation = [0,2,0]

Group42 = Group()

IS43 = IS()

connect44 = connect()
connect44.nodeField = "children"
connect44.protoField = "children"
IS43.addConnect([connect44])
Group42.IS = IS43
Transform41.addChildren([Group42])
ProtoBody40.addChildren([Transform41])
ProtoDeclare36.protoBody = ProtoBody40
Scene17.addChildren([ProtoDeclare36])

ProtoInstance45 = ProtoInstance()
ProtoInstance45.name = "ShiftGroupUp2m"
Scene17.addChildren([ProtoInstance45])
# ==================== 

Viewpoint46 = Viewpoint()
Viewpoint46.DEF = "ExampleSingleElement"
Viewpoint46.description = "Hello syntax"
Scene17.addChildren([Viewpoint46])

Group47 = Group()
Group47.DEF = "ExampleChildElement"

Shape48 = Shape()

Box49 = Box()
Shape48.geometry = Box49

Appearance50 = Appearance()

Material51 = Material()
Material51.diffuseColor = [0.6,0.4,0.2]
Appearance50.material = Material51
Shape48.appearance = Appearance50
Group47.addChildren([Shape48])
Scene17.addChildren([Group47])

Transform52 = Transform()
Transform52.DEF = "TransformExampleUSE"
Transform52.rotation = [0,1,0,0.78]
Transform52.translation = [0,2.5,0]

Group53 = Group()
Group53.USE = "ExampleChildElement"
Transform52.addChildren([Group53])
Scene17.addChildren([Transform52])

Collision54 = Collision()

Shape55 = Shape()
# note that Collision proxy Shape is not rendered 

Text56 = Text()
Text56.string = ["He said, \"Immel did it!\""]
Shape55.geometry = Text56
# alternative: Text string='\"He said, \\&quot;Immel did it!\\&quot;\"' 

Appearance57 = Appearance()

Material58 = Material()
Appearance57.material = Material58
Shape55.appearance = Appearance57
Collision54.proxy = Shape55

Group59 = Group()
Group59.USE = "ExampleChildElement"
Collision54.addChildren([Group59])
Scene17.addChildren([Collision54])

Transform60 = Transform()
Transform60.translation = [0,-2.5,0]

Shape61 = Shape()

Appearance62 = Appearance()

ProtoInstance63 = ProtoInstance()
ProtoInstance63.name = "EmissiveMaterial"

fieldValue64 = fieldValue()
fieldValue64.name = "onlyColor"
fieldValue64.value = "0.2 0.6 0.6"
ProtoInstance63.addFieldValue([fieldValue64])
Appearance62.material = ProtoInstance63
Shape61.appearance = Appearance62

Text65 = Text()
Text65.string = ["X3D Header Prototype syntax examples","(view console for EXTERNPROTO output)"]

FontStyle66 = FontStyle(justify = ["MIDDLE","MIDDLE"], size = 0.6)
Text65.fontStyle = FontStyle66
Shape61.geometry = Text65
Transform60.addChildren([Shape61])
Scene17.addChildren([Transform60])

ProtoInstance67 = ProtoInstance()
ProtoInstance67.name = "ViewPositionOrientation"

fieldValue68 = fieldValue()
fieldValue68.name = "enabled"
fieldValue68.value = "true"
ProtoInstance67.addFieldValue([fieldValue68])
Scene17.addChildren([ProtoInstance67])

TimeSensor69 = TimeSensor()
TimeSensor69.DEF = "Clock"
TimeSensor69.cycleInterval = 4
TimeSensor69.loop = True
Scene17.addChildren([TimeSensor69])

OrientationInterpolator70 = OrientationInterpolator()
OrientationInterpolator70.DEF = "Spinner"
OrientationInterpolator70.key = [0,0.5,1]
OrientationInterpolator70.keyValue = [0,1,0,0,0,1,0,3.14159,0,1,0,6.28318]
Scene17.addChildren([OrientationInterpolator70])

ROUTE71 = ROUTE()
ROUTE71.fromField = "fraction_changed"
ROUTE71.fromNode = "Clock"
ROUTE71.toField = "set_fraction"
ROUTE71.toNode = "Spinner"
Scene17.addChildren([ROUTE71])

ROUTE72 = ROUTE()
ROUTE72.fromField = "value_changed"
ROUTE72.fromNode = "Spinner"
ROUTE72.toField = "rotation"
ROUTE72.toNode = "TransformExampleUSE"
Scene17.addChildren([ROUTE72])

Inline73 = Inline()
Inline73.DEF = "someInline"
Inline73.url = ["someUrl.x3d","http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/someUrl.x3d"]
Scene17.addChildren([Inline73])

IMPORT74 = IMPORT()
IMPORT74.AS = "someInlineRoot"
IMPORT74.importedDEF = "someName"
IMPORT74.inlineDEF = "someInline"
Scene17.addChildren([IMPORT74])

PositionInterpolator75 = PositionInterpolator()
PositionInterpolator75.DEF = "StayInPlace"
PositionInterpolator75.key = [0,1]
PositionInterpolator75.keyValue = [0,0,0,0,0,0]
Scene17.addChildren([PositionInterpolator75])

ROUTE76 = ROUTE()
ROUTE76.fromField = "fraction_changed"
ROUTE76.fromNode = "Clock"
ROUTE76.toField = "set_fraction"
ROUTE76.toNode = "StayInPlace"
Scene17.addChildren([ROUTE76])

ROUTE77 = ROUTE()
ROUTE77.fromField = "value_changed"
ROUTE77.fromNode = "StayInPlace"
ROUTE77.toField = "set_translation"
ROUTE77.toNode = "someInlineRoot"
Scene17.addChildren([ROUTE77])
X3D0.scene = Scene17
