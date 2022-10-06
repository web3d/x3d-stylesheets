from X3Dpackage import *
X3D0 = X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = head()
component2 = component()
component2.setLevel(1)
component2.setName("Geospatial")
head1.addComponent(component2)
component3 = component()
component3.setLevel(2)
component3.setName("NURBS")
head1.addComponent(component3)
component4 = component()
component4.setLevel(2)
component4.setName("Core")
head1.addComponent(component4)
component5 = component()
component5.setLevel(1)
component5.setName("Navigation")
head1.addComponent(component5)
component6 = component()
component6.setLevel(1)
component6.setName("Text")
head1.addComponent(component6)
meta7 = meta()
meta7.setContent("X3dHeaderPrototypeSyntaxExamples.x3d")
meta7.setName("title")
head1.addMeta(meta7)
meta8 = meta()
meta8.setContent("X3D scene header and prototype syntax examples. This example header indicates that the content is XML encoded, follows the Interactive Profile and explicitly lists additional necessary components. The X3D header may also contain additional semantic information. Used for specification EXAMPLE excerpts in 19776:1 XML Encoding.")
meta8.setName("description")
head1.addMeta(meta8)
meta9 = meta()
meta9.setContent("14 October 2002")
meta9.setName("created")
head1.addMeta(meta9)
meta10 = meta()
meta10.setContent("7 May 2017")
meta10.setName("modified")
head1.addMeta(meta10)
meta11 = meta()
meta11.setContent("Don Brutzman")
meta11.setName("creator")
head1.addMeta(meta11)
meta12 = meta()
meta12.setContent("X3D encodings, ISO/IEC 19776-1.3, Part 1: XML encoding, 4.3 XML file syntax")
meta12.setName("specificationSection")
head1.addMeta(meta12)
meta13 = meta()
meta13.setContent("http://www.web3d.org/documents/specifications/19776-1/V3.3/Part01/concepts.html#XMLFileSyntax")
meta13.setName("specificationUrl")
head1.addMeta(meta13)
meta14 = meta()
meta14.setContent("http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/X3dHeaderPrototypeSyntaxExamples.x3d")
meta14.setName("identifier")
head1.addMeta(meta14)
meta15 = meta()
meta15.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")
meta15.setName("generator")
head1.addMeta(meta15)
meta16 = meta()
meta16.setContent("../license.html")
meta16.setName("license")
head1.addMeta(meta16)
X3D0.setHead(head1)
Scene17 = Scene()
ExternProtoDeclare18 = ExternProtoDeclare()
ExternProtoDeclare18.setName("ViewPositionOrientation")
ExternProtoDeclare18.setUrl(["../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation"])
field19 = field()
field19.setAccessType("inputOutput")
field19.setName("enabled")
field19.setType("SFBool")
ExternProtoDeclare18.addField(field19)
field20 = field()
field20.setAccessType("initializeOnly")
field20.setName("traceEnabled")
field20.setType("SFBool")
ExternProtoDeclare18.addField(field20)
field21 = field()
field21.setAccessType("inputOnly")
field21.setName("set_traceEnabled")
field21.setType("SFBool")
ExternProtoDeclare18.addField(field21)
field22 = field()
field22.setAccessType("outputOnly")
field22.setName("position_changed")
field22.setType("SFVec3f")
ExternProtoDeclare18.addField(field22)
field23 = field()
field23.setAccessType("outputOnly")
field23.setName("orientation_changed")
field23.setType("SFRotation")
ExternProtoDeclare18.addField(field23)
field24 = field()
field24.setAccessType("outputOnly")
field24.setName("outputViewpointString")
field24.setType("MFString")
ExternProtoDeclare18.addField(field24)
Scene17.addChildren(ExternProtoDeclare18)
ProtoDeclare25 = ProtoDeclare()
ProtoDeclare25.setName("NewWorldInfoNode")
ProtoBody26 = ProtoBody()
WorldInfo27 = WorldInfo()
WorldInfo27.setDEF("ExamplePrototypeBody")
ProtoBody26.addChildren(WorldInfo27)
ProtoDeclare25.setProtoBody(ProtoBody26)
Scene17.addChildren(ProtoDeclare25)
ProtoInstance28 = ProtoInstance()
ProtoInstance28.setName("NewWorldInfoNode")
Scene17.addChildren(ProtoInstance28)
ProtoDeclare29 = ProtoDeclare()
ProtoDeclare29.setName("EmissiveMaterial")
ProtoInterface30 = ProtoInterface()
field31 = field()
field31.setAccessType("inputOutput")
field31.setName("onlyColor")
field31.setType("SFColor")
field31.setValue("1 0 0")
ProtoInterface30.addField(field31)
ProtoDeclare29.setProtoInterface(ProtoInterface30)
ProtoBody32 = ProtoBody()
# Override default diffuseColor value 0.8 0.8 0.8 
Material33 = Material()
Material33.setDiffuseColor([0,0,0])
# Connect emissiveColor field of current node to onlyColor field of parent ProtoDeclare. 
IS34 = IS()
connect35 = connect()
connect35.setNodeField("emissiveColor")
connect35.setProtoField("onlyColor")
IS34.addConnect(connect35)
Material33.IS = IS34
ProtoBody32.addChildren(Material33)
ProtoDeclare29.setProtoBody(ProtoBody32)
Scene17.addChildren(ProtoDeclare29)
ProtoDeclare36 = ProtoDeclare()
ProtoDeclare36.setName("ShiftGroupUp2m")
ProtoInterface37 = ProtoInterface()
field38 = field()
field38.setAccessType("inputOutput")
field38.setName("children")
field38.setType("MFNode")
Group39 = Group(bboxSize = [2,2,2])
Group39.setDEF("DefaultNodeValue")
# Authors need to override this node when creating the ProtoInstance fieldValue name=\"children\" 
field38.addChildren(Group39)
ProtoInterface37.addField(field38)
ProtoDeclare36.setProtoInterface(ProtoInterface37)
ProtoBody40 = ProtoBody()
Transform41 = Transform()
Transform41.setTranslation([0,2,0])
Group42 = Group()
IS43 = IS()
connect44 = connect()
connect44.setNodeField("children")
connect44.setProtoField("children")
IS43.addConnect(connect44)
Group42.IS = IS43
Transform41.addChildren(Group42)
ProtoBody40.addChildren(Transform41)
ProtoDeclare36.setProtoBody(ProtoBody40)
Scene17.addChildren(ProtoDeclare36)
ProtoInstance45 = ProtoInstance()
ProtoInstance45.setName("ShiftGroupUp2m")
Scene17.addChildren(ProtoInstance45)
# ==================== 
Viewpoint46 = Viewpoint()
Viewpoint46.setDEF("ExampleSingleElement")
Viewpoint46.setDescription("Hello syntax")
Scene17.addChildren(Viewpoint46)
Group47 = Group()
Group47.setDEF("ExampleChildElement")
Shape48 = Shape()
Box49 = Box()
Shape48.setGeometry(Box49)
Appearance50 = Appearance()
Material51 = Material()
Material51.setDiffuseColor([0.6,0.4,0.2])
Appearance50.setMaterial(Material51)
Shape48.setAppearance(Appearance50)
Group47.addChildren(Shape48)
Scene17.addChildren(Group47)
Transform52 = Transform()
Transform52.setDEF("TransformExampleUSE")
Transform52.setRotation([0,1,0,0.78])
Transform52.setTranslation([0,2.5,0])
Group53 = Group()
Group53.setUSE("ExampleChildElement")
Transform52.addChildren(Group53)
Scene17.addChildren(Transform52)
Collision54 = Collision()
Shape55 = Shape(proxy = Collision54)
# note that Collision proxy Shape is not rendered 
Text56 = Text()
Text56.setString(["He said, \"Immel did it!\""])
Shape55.setGeometry(Text56)
# alternative: Text string='\"He said, \\&quot;Immel did it!\\&quot;\"' 
Appearance57 = Appearance()
Material58 = Material()
Appearance57.setMaterial(Material58)
Shape55.setAppearance(Appearance57)
Collision54.setProxy(Shape55)
Group59 = Group()
Group59.setUSE("ExampleChildElement")
Collision54.addChildren(Group59)
Scene17.addChildren(Collision54)
Transform60 = Transform()
Transform60.setTranslation([0,-2.5,0])
Shape61 = Shape()
Appearance62 = Appearance()
ProtoInstance63 = ProtoInstance()
ProtoInstance63.setName("EmissiveMaterial")
fieldValue64 = fieldValue()
fieldValue64.setName("onlyColor")
fieldValue64.setValue("0.2 0.6 0.6")
ProtoInstance63.addFieldValue(fieldValue64)
Appearance62.setMaterial(ProtoInstance63)
Shape61.setAppearance(Appearance62)
Text65 = Text()
Text65.setString(["X3D Header Prototype syntax examples","(view console for EXTERNPROTO output)"])
FontStyle66 = FontStyle(justify = ["MIDDLE","MIDDLE"], size = 0.6)
Text65.setFontStyle(FontStyle66)
Shape61.setGeometry(Text65)
Transform60.addChildren(Shape61)
Scene17.addChildren(Transform60)
ProtoInstance67 = ProtoInstance()
ProtoInstance67.setName("ViewPositionOrientation")
fieldValue68 = fieldValue()
fieldValue68.setName("enabled")
fieldValue68.setValue("true")
ProtoInstance67.addFieldValue(fieldValue68)
Scene17.addChildren(ProtoInstance67)
TimeSensor69 = TimeSensor()
TimeSensor69.setDEF("Clock")
TimeSensor69.setCycleInterval(4)
TimeSensor69.setLoop(True)
Scene17.addChildren(TimeSensor69)
OrientationInterpolator70 = OrientationInterpolator()
OrientationInterpolator70.setDEF("Spinner")
OrientationInterpolator70.setKey([0,0.5,1])
OrientationInterpolator70.setKeyValue([0,1,0,0,0,1,0,3.14159,0,1,0,6.28318])
Scene17.addChildren(OrientationInterpolator70)
ROUTE71 = ROUTE()
ROUTE71.setFromField("fraction_changed")
ROUTE71.setFromNode("Clock")
ROUTE71.setToField("set_fraction")
ROUTE71.setToNode("Spinner")
Scene17.addChildren(ROUTE71)
ROUTE72 = ROUTE()
ROUTE72.setFromField("value_changed")
ROUTE72.setFromNode("Spinner")
ROUTE72.setToField("rotation")
ROUTE72.setToNode("TransformExampleUSE")
Scene17.addChildren(ROUTE72)
Inline73 = Inline()
Inline73.setDEF("someInline")
Inline73.setUrl(["someUrl.x3d","http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/someUrl.x3d"])
Scene17.addChildren(Inline73)
IMPORT74 = IMPORT()
IMPORT74.setAS("someInlineRoot")
IMPORT74.setImportedDEF("someName")
IMPORT74.setInlineDEF("someInline")
Scene17.addChildren(IMPORT74)
PositionInterpolator75 = PositionInterpolator()
PositionInterpolator75.setDEF("StayInPlace")
PositionInterpolator75.setKey([0,1])
PositionInterpolator75.setKeyValue([0,0,0,0,0,0])
Scene17.addChildren(PositionInterpolator75)
ROUTE76 = ROUTE()
ROUTE76.setFromField("fraction_changed")
ROUTE76.setFromNode("Clock")
ROUTE76.setToField("set_fraction")
ROUTE76.setToNode("StayInPlace")
Scene17.addChildren(ROUTE76)
ROUTE77 = ROUTE()
ROUTE77.setFromField("value_changed")
ROUTE77.setFromNode("StayInPlace")
ROUTE77.setToField("set_translation")
ROUTE77.setToNode("someInlineRoot")
Scene17.addChildren(ROUTE77)
X3D0.setScene(Scene17)