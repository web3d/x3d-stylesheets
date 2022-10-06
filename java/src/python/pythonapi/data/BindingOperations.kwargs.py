from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(content="BindingOperations.x3d", name="title"), 
    meta3 = meta(content="Illustrate Viewpoint binding operations (in gory detail!) as described in Chapter 4 concepts. Scene design: a TimeSensor clock drives and IntegerSequencer for each t0/t1/etc. event, and a customized Script node sends bind/unbind events to the correct Viewpoint. Display the browser console to see occurrence of each event.", name="description"), 
    meta4 = meta(content="Don Brutzman", name="creator"), 
    meta5 = meta(content="5 January 2008", name="created"), 
    meta6 = meta(content="22 July 2013", name="modified"), 
    meta7 = meta(content="BindingOperations.console.txt", name="reference"), 
    meta8 = meta(content="BindingStackOperations.png", name="reference"), 
    meta9 = meta(content="X3D for Web Authors, Section 2.5.1, Figure 4.1", name="reference"), 
    meta10 = meta(content="http://X3dGraphics.com", name="reference"), 
    meta11 = meta(content="http://www.web3d.org/x3d/content/examples/X3dResources.html", name="reference"), 
    meta12 = meta(content="Copyright Don Brutzman and Leonard Daly 2007", name="rights"), 
    meta13 = meta(content="X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com", name="subject"), 
    meta14 = meta(content="http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter04ViewingNavigation/BindingOperations.x3d", name="identifier"), 
    meta15 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta16 = meta(content="../license.html", name="license")), 
   Scene17 = Scene(    Viewpoint18 = Viewpoint(DEF="View1", centerOfRotation=[-6,0,0], description="Viewpoint 1", position=[-6,0,5]), 
    Viewpoint19 = Viewpoint(DEF="View2", centerOfRotation=[-2,0,0], description="Viewpoint 2", position=[-2,0,5]), 
    Viewpoint20 = Viewpoint(DEF="View3", centerOfRotation=[2,0,0], description="Viewpoint 3", position=[2,0,5]), 
    Viewpoint21 = Viewpoint(DEF="View4", centerOfRotation=[6,0,0], description="Viewpoint 4", position=[6,0,5]),     # Script initialization ought to first bind view5 below. 

    Group22 = Group(     Transform23 = Transform(DEF="Text1", translation=[-6,0,0],       Shape24 = Shape(       Text25 = Text(string=["View","# 1"],         FontStyle26 = FontStyle(DEF="CenterJustify", justify=["MIDDLE","MIDDLE"])), 
       Appearance27 = Appearance(        Material28 = Material(diffuseColor=[1,0,0])))), 
     Transform29 = Transform(DEF="Text2", translation=[-2,0,0],       Shape30 = Shape(       Text31 = Text(string=["View","# 2"],         FontStyle32 = FontStyle(USE="CenterJustify")), 
       Appearance33 = Appearance(        Material34 = Material(diffuseColor=[0,1,0])))), 
     Transform35 = Transform(DEF="Text3", translation=[2,0,0],       Shape36 = Shape(       Text37 = Text(string=["View","# 3"],         FontStyle38 = FontStyle(USE="CenterJustify")), 
       Appearance39 = Appearance(        Material40 = Material(diffuseColor=[0,0,1])))), 
     Transform41 = Transform(DEF="Text4", translation=[6,0,0],       Shape42 = Shape(       Text43 = Text(string=["View","# 4"],         FontStyle44 = FontStyle(USE="CenterJustify")), 
       Appearance45 = Appearance(        Material46 = Material())))),     # The following advanced animation sequence uses nodes covered in Chapters 7, 8 and 9. 
    # It does not need to be studied in this chapter. 

    Transform47 = Transform(translation=[0,-3,8],      # notice this next Viewpoint has been transformed with the text, so its position is relative. it is called view5 in the Script. 

     Viewpoint48 = Viewpoint(DEF="ClickToAnimateView", description="Select animation sequence", position=[0,0,7]), 
     Shape49 = Shape(      Text50 = Text(string=["Click here to animate"],        FontStyle51 = FontStyle(justify=["MIDDLE","BEGIN"])), 
      Appearance52 = Appearance(       Material53 = Material(diffuseColor=[0.8,0.4,0]))), 
     Shape54 = Shape(      Box55 = Box(size=[7,1,0.02]), 
      Appearance56 = Appearance(       Material57 = Material(transparency=1))), 
     TouchSensor58 = TouchSensor(DEF="TextTouchSensor", description="Click to begin animating viewpoint selections"), 
     TimeSensor59 = TimeSensor(DEF="Clock", cycleInterval=10), 
     ROUTE60 = ROUTE(fromField="touchTime", fromNode="TextTouchSensor", toField="set_startTime", toNode="Clock"), 
     IntegerSequencer61 = IntegerSequencer(DEF="TimingSequencer", key=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,1.0], keyValue=[0,1,2,3,4,5,6,7,8,10]), 
     ROUTE62 = ROUTE(fromField="fraction_changed", fromNode="Clock", toField="set_fraction", toNode="TimingSequencer"), 
     Script63 = Script(DEF="BindingSequencerEngine",       field64 = field(accessType="inputOnly", name="set_timeEvent", type="SFInt32"), 
      field65 = field(accessType="outputOnly", name="bindView1", type="SFBool"), 
      field66 = field(accessType="outputOnly", name="bindView2", type="SFBool"), 
      field67 = field(accessType="outputOnly", name="bindView3", type="SFBool"), 
      field68 = field(accessType="outputOnly", name="bindView4", type="SFBool"), 
      field69 = field(accessType="outputOnly", name="bindView5", type="SFBool"), 
      field70 = field(accessType="inputOnly", name="view1Bound", type="SFBool"), 
      field71 = field(accessType="inputOnly", name="view2Bound", type="SFBool"), 
      field72 = field(accessType="inputOnly", name="view3Bound", type="SFBool"), 
      field73 = field(accessType="inputOnly", name="view4Bound", type="SFBool"), 
      field74 = field(accessType="initializeOnly", name="priorInputvalue", type="SFInt32", value="-1"),       sourceCode = '''\n"+
"ecmascript:\n"+
"\n"+
"function initialize ()\n"+
"{\n"+
"    bindView5 = true;\n"+
"    Browser.print ('Timing script initialized and ready for activation');\n"+
"}\n"+
"function set_timeEvent (inputValue)\n"+
"{\n"+
"    if (inputValue == priorInputvalue)\n"+
"    {\n"+
"        return; // ignore repeated inputs\n"+
"    }\n"+
"    // new value provided\n"+
"    priorInputvalue = inputValue;\n"+
"    // Browser.print ('\\ntimeEvent inputValue=' + inputValue);\n"+
"        \n"+
"    // mimics user execution of Figure 4.1 steps t_0 through t_8\n"+
"    if (inputValue == 0)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t0');\n"+
"        bindView1 = true;\n"+
"    }\n"+
"    else if (inputValue == 1)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t1');\n"+
"        bindView2 = true;\n"+
"    }\n"+
"    else if (inputValue == 2)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t2');\n"+
"        bindView3 = true;\n"+
"    }\n"+
"    else if (inputValue == 3)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t3');\n"+
"        bindView3 = false;\n"+
"    }\n"+
"    else if (inputValue == 4)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t4');\n"+
"        bindView1 = true;\n"+
"    }\n"+
"    else if (inputValue == 5)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t5');\n"+
"        bindView2 = false;\n"+
"    }\n"+
"    else if (inputValue == 6)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t6');\n"+
"        bindView1 = false;\n"+
"    }\n"+
"    else if (inputValue == 7)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t7');\n"+
"        bindView4 = true;\n"+
"\n"+
"    }\n"+
"    else if (inputValue == 8)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t8');\n"+
"        Browser.print (', no action, all done');\n"+
"        Browser.print ('\\n\\n');\n"+
"    }\n"+
"}\n"+
"\n"+
"function view1Bound (inputValue)\n"+
"{\n"+
"    Browser.print (', view1Bound ' + (inputValue));\n"+
"    if (priorInputvalue == -1) Browser.print ('\\n');\n"+
"}\n"+
"function view2Bound (inputValue)\n"+
"{\n"+
"    Browser.print (', view2Bound ' + (inputValue));\n"+
"}\n"+
"function view3Bound (inputValue)\n"+
"{\n"+
"    Browser.print (', view3Bound ' + (inputValue));\n"+
"}\n"+
"function view4Bound (inputValue)\n"+
"{\n"+
"    Browser.print (', view4Bound ' + (inputValue));\n"+
"}\n"+
"function view5Bound (inputValue)\n"+
"{\n"+
"    Browser.print (', view5Bound ' + (inputValue));\n"+
"}\n"+
"''', ),      # drive Script with TimeSensor clock 

     ROUTE75 = ROUTE(fromField="value_changed", fromNode="TimingSequencer", toField="set_timeEvent", toNode="BindingSequencerEngine"),      # Script will bind and unbind Viewpoint nodes 

     ROUTE76 = ROUTE(fromField="bindView1", fromNode="BindingSequencerEngine", toField="set_bind", toNode="View1"), 
     ROUTE77 = ROUTE(fromField="bindView2", fromNode="BindingSequencerEngine", toField="set_bind", toNode="View2"), 
     ROUTE78 = ROUTE(fromField="bindView3", fromNode="BindingSequencerEngine", toField="set_bind", toNode="View3"), 
     ROUTE79 = ROUTE(fromField="bindView4", fromNode="BindingSequencerEngine", toField="set_bind", toNode="View4"), 
     ROUTE80 = ROUTE(fromField="bindView5", fromNode="BindingSequencerEngine", toField="set_bind", toNode="ClickToAnimateView"),      # Viewpoint nodes report bind and unbind events 

     ROUTE81 = ROUTE(fromField="isBound", fromNode="View1", toField="view1Bound", toNode="BindingSequencerEngine"), 
     ROUTE82 = ROUTE(fromField="isBound", fromNode="View2", toField="view2Bound", toNode="BindingSequencerEngine"), 
     ROUTE83 = ROUTE(fromField="isBound", fromNode="View3", toField="view3Bound", toNode="BindingSequencerEngine"), 
     ROUTE84 = ROUTE(fromField="isBound", fromNode="View4", toField="view4Bound", toNode="BindingSequencerEngine"))))
