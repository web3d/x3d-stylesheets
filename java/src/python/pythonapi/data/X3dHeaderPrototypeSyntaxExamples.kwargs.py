from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    component2 = component(level=1, name="Geospatial"), 
    component3 = component(level=2, name="NURBS"), 
    component4 = component(level=2, name="Core"), 
    component5 = component(level=1, name="Navigation"), 
    component6 = component(level=1, name="Text"), 
    meta7 = meta(content="X3dHeaderPrototypeSyntaxExamples.x3d", name="title"), 
    meta8 = meta(content="X3D scene header and prototype syntax examples. This example header indicates that the content is XML encoded, follows the Interactive Profile and explicitly lists additional necessary components. The X3D header may also contain additional semantic information. Used for specification EXAMPLE excerpts in 19776:1 XML Encoding.", name="description"), 
    meta9 = meta(content="14 October 2002", name="created"), 
    meta10 = meta(content="7 May 2017", name="modified"), 
    meta11 = meta(content="Don Brutzman", name="creator"), 
    meta12 = meta(content="X3D encodings, ISO/IEC 19776-1.3, Part 1: XML encoding, 4.3 XML file syntax", name="specificationSection"), 
    meta13 = meta(content="http://www.web3d.org/documents/specifications/19776-1/V3.3/Part01/concepts.html#XMLFileSyntax", name="specificationUrl"), 
    meta14 = meta(content="http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/X3dHeaderPrototypeSyntaxExamples.x3d", name="identifier"), 
    meta15 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta16 = meta(content="../license.html", name="license")), 
   Scene17 = Scene(    ExternProtoDeclare18 = ExternProtoDeclare(name="ViewPositionOrientation", url=["../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation"],      field19 = field(accessType="inputOutput", name="enabled", type="SFBool"), 
     field20 = field(accessType="initializeOnly", name="traceEnabled", type="SFBool"), 
     field21 = field(accessType="inputOnly", name="set_traceEnabled", type="SFBool"), 
     field22 = field(accessType="outputOnly", name="position_changed", type="SFVec3f"), 
     field23 = field(accessType="outputOnly", name="orientation_changed", type="SFRotation"), 
     field24 = field(accessType="outputOnly", name="outputViewpointString", type="MFString")), 
    ProtoDeclare25 = ProtoDeclare(name="NewWorldInfoNode",      ProtoBody26 = ProtoBody(      WorldInfo27 = WorldInfo(DEF="ExamplePrototypeBody"))), 
    ProtoInstance28 = ProtoInstance(name="NewWorldInfoNode"), 
    ProtoDeclare29 = ProtoDeclare(name="EmissiveMaterial",      ProtoInterface30 = ProtoInterface(      field31 = field(accessType="inputOutput", name="onlyColor", type="SFColor", value="1 0 0")), 
     ProtoBody32 = ProtoBody(      # Override default diffuseColor value 0.8 0.8 0.8 

      Material33 = Material(diffuseColor=[0,0,0],        # Connect emissiveColor field of current node to onlyColor field of parent ProtoDeclare. 

       IS34 = IS(        connect35 = connect(nodeField="emissiveColor", protoField="onlyColor"))))), 
    ProtoDeclare36 = ProtoDeclare(name="ShiftGroupUp2m",      ProtoInterface37 = ProtoInterface(      field38 = field(accessType="inputOutput", name="children", type="MFNode",        Group39 = Group(DEF="DefaultNodeValue", bboxSize=[2,2,2],         # Authors need to override this node when creating the ProtoInstance fieldValue name=\"children\" 
))), 
     ProtoBody40 = ProtoBody(      Transform41 = Transform(translation=[0,2,0],        Group42 = Group(        IS43 = IS(         connect44 = connect(nodeField="children", protoField="children")))))), 
    ProtoInstance45 = ProtoInstance(name="ShiftGroupUp2m"),     # ==================== 

    Viewpoint46 = Viewpoint(DEF="ExampleSingleElement", description="Hello syntax"), 
    Group47 = Group(DEF="ExampleChildElement",      Shape48 = Shape(      Box49 = Box(), 
      Appearance50 = Appearance(       Material51 = Material(diffuseColor=[0.6,0.4,0.2])))), 
    Transform52 = Transform(DEF="TransformExampleUSE", rotation=[0,1,0,0.78], translation=[0,2.5,0],      Group53 = Group(USE="ExampleChildElement")), 
    Collision54 = Collision(     Shape55 = Shape(      # note that Collision proxy Shape is not rendered 

      Text56 = Text(string=["He said, \"Immel did it!\""]),       # alternative: Text string='\"He said, \\&quot;Immel did it!\\&quot;\"' 

      Appearance57 = Appearance(       Material58 = Material())), 
     Group59 = Group(USE="ExampleChildElement")), 
    Transform60 = Transform(translation=[0,-2.5,0],      Shape61 = Shape(      Appearance62 = Appearance(       ProtoInstance63 = ProtoInstance(name="EmissiveMaterial",         fieldValue64 = fieldValue(name="onlyColor", value="0.2 0.6 0.6"))), 
      Text65 = Text(string=["X3D Header Prototype syntax examples","(view console for EXTERNPROTO output)"],        FontStyle66 = FontStyle(justify=["MIDDLE","MIDDLE"], size=0.6)))), 
    ProtoInstance67 = ProtoInstance(name="ViewPositionOrientation",      fieldValue68 = fieldValue(name="enabled", value="true")), 
    TimeSensor69 = TimeSensor(DEF="Clock", cycleInterval=4, loop=True), 
    OrientationInterpolator70 = OrientationInterpolator(DEF="Spinner", key=[0,0.5,1], keyValue=[0,1,0,0,0,1,0,3.14159,0,1,0,6.28318]), 
    ROUTE71 = ROUTE(fromField="fraction_changed", fromNode="Clock", toField="set_fraction", toNode="Spinner"), 
    ROUTE72 = ROUTE(fromField="value_changed", fromNode="Spinner", toField="rotation", toNode="TransformExampleUSE"), 
    Inline73 = Inline(DEF="someInline", url=["someUrl.x3d","http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/someUrl.x3d"]), 
    IMPORT74 = IMPORT(AS="someInlineRoot", importedDEF="someName", inlineDEF="someInline"), 
    PositionInterpolator75 = PositionInterpolator(DEF="StayInPlace", key=[0,1], keyValue=[0,0,0,0,0,0]), 
    ROUTE76 = ROUTE(fromField="fraction_changed", fromNode="Clock", toField="set_fraction", toNode="StayInPlace"), 
    ROUTE77 = ROUTE(fromField="value_changed", fromNode="StayInPlace", toField="set_translation", toNode="someInlineRoot")))
