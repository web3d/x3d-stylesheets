from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.content = "BindingOperations.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Illustrate Viewpoint binding operations (in gory detail!) as described in Chapter 4 concepts. Scene design: a TimeSensor clock drives and IntegerSequencer for each t0/t1/etc. event, and a customized Script node sends bind/unbind events to the correct Viewpoint. Display the browser console to see occurrence of each event."
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Don Brutzman"
meta4.name = "creator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "5 January 2008"
meta5.name = "created"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "22 July 2013"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "BindingOperations.console.txt"
meta7.name = "reference"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "BindingStackOperations.png"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "X3D for Web Authors, Section 2.5.1, Figure 4.1"
meta9.name = "reference"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "http://X3dGraphics.com"
meta10.name = "reference"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "http://www.web3d.org/x3d/content/examples/X3dResources.html"
meta11.name = "reference"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "Copyright Don Brutzman and Leonard Daly 2007"
meta12.name = "rights"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com"
meta13.name = "subject"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter04ViewingNavigation/BindingOperations.x3d"
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

Viewpoint18 = Viewpoint()
Viewpoint18.DEF = "View1"
Viewpoint18.centerOfRotation = [-6,0,0]
Viewpoint18.description = "Viewpoint 1"
Viewpoint18.position = [-6,0,5]
Scene17.addChildren([Viewpoint18])

Viewpoint19 = Viewpoint()
Viewpoint19.DEF = "View2"
Viewpoint19.centerOfRotation = [-2,0,0]
Viewpoint19.description = "Viewpoint 2"
Viewpoint19.position = [-2,0,5]
Scene17.addChildren([Viewpoint19])

Viewpoint20 = Viewpoint()
Viewpoint20.DEF = "View3"
Viewpoint20.centerOfRotation = [2,0,0]
Viewpoint20.description = "Viewpoint 3"
Viewpoint20.position = [2,0,5]
Scene17.addChildren([Viewpoint20])

Viewpoint21 = Viewpoint()
Viewpoint21.DEF = "View4"
Viewpoint21.centerOfRotation = [6,0,0]
Viewpoint21.description = "Viewpoint 4"
Viewpoint21.position = [6,0,5]
Scene17.addChildren([Viewpoint21])
# Script initialization ought to first bind view5 below. 

Group22 = Group()

Transform23 = Transform()
Transform23.DEF = "Text1"
Transform23.translation = [-6,0,0]

Shape24 = Shape()

Text25 = Text()
Text25.string = ["View","# 1"]

FontStyle26 = FontStyle(justify = ["MIDDLE","MIDDLE"])
FontStyle26.DEF = "CenterJustify"
Text25.fontStyle = FontStyle26
Shape24.geometry = Text25

Appearance27 = Appearance()

Material28 = Material()
Material28.diffuseColor = [1,0,0]
Appearance27.material = Material28
Shape24.appearance = Appearance27
Transform23.addChildren([Shape24])
Group22.addChildren([Transform23])

Transform29 = Transform()
Transform29.DEF = "Text2"
Transform29.translation = [-2,0,0]

Shape30 = Shape()

Text31 = Text()
Text31.string = ["View","# 2"]

FontStyle32 = FontStyle()
FontStyle32.USE = "CenterJustify"
Text31.fontStyle = FontStyle32
Shape30.geometry = Text31

Appearance33 = Appearance()

Material34 = Material()
Material34.diffuseColor = [0,1,0]
Appearance33.material = Material34
Shape30.appearance = Appearance33
Transform29.addChildren([Shape30])
Group22.addChildren([Transform29])

Transform35 = Transform()
Transform35.DEF = "Text3"
Transform35.translation = [2,0,0]

Shape36 = Shape()

Text37 = Text()
Text37.string = ["View","# 3"]

FontStyle38 = FontStyle()
FontStyle38.USE = "CenterJustify"
Text37.fontStyle = FontStyle38
Shape36.geometry = Text37

Appearance39 = Appearance()

Material40 = Material()
Material40.diffuseColor = [0,0,1]
Appearance39.material = Material40
Shape36.appearance = Appearance39
Transform35.addChildren([Shape36])
Group22.addChildren([Transform35])

Transform41 = Transform()
Transform41.DEF = "Text4"
Transform41.translation = [6,0,0]

Shape42 = Shape()

Text43 = Text()
Text43.string = ["View","# 4"]

FontStyle44 = FontStyle()
FontStyle44.USE = "CenterJustify"
Text43.fontStyle = FontStyle44
Shape42.geometry = Text43

Appearance45 = Appearance()

Material46 = Material()
Appearance45.material = Material46
Shape42.appearance = Appearance45
Transform41.addChildren([Shape42])
Group22.addChildren([Transform41])
Scene17.addChildren([Group22])
# The following advanced animation sequence uses nodes covered in Chapters 7, 8 and 9. 
# It does not need to be studied in this chapter. 

Transform47 = Transform()
Transform47.translation = [0,-3,8]
# notice this next Viewpoint has been transformed with the text, so its position is relative. it is called view5 in the Script. 

Viewpoint48 = Viewpoint()
Viewpoint48.DEF = "ClickToAnimateView"
Viewpoint48.description = "Select animation sequence"
Viewpoint48.position = [0,0,7]
Transform47.addChildren([Viewpoint48])

Shape49 = Shape()

Text50 = Text()
Text50.string = ["Click here to animate"]

FontStyle51 = FontStyle(justify = ["MIDDLE","BEGIN"])
Text50.fontStyle = FontStyle51
Shape49.geometry = Text50

Appearance52 = Appearance()

Material53 = Material()
Material53.diffuseColor = [0.8,0.4,0]
Appearance52.material = Material53
Shape49.appearance = Appearance52
Transform47.addChildren([Shape49])

Shape54 = Shape()

Box55 = Box(size = [7,1,0.02])
Shape54.geometry = Box55

Appearance56 = Appearance()

Material57 = Material()
Material57.transparency = 1
Appearance56.material = Material57
Shape54.appearance = Appearance56
Transform47.addChildren([Shape54])

TouchSensor58 = TouchSensor()
TouchSensor58.DEF = "TextTouchSensor"
TouchSensor58.description = "Click to begin animating viewpoint selections"
Transform47.addChildren([TouchSensor58])

TimeSensor59 = TimeSensor()
TimeSensor59.DEF = "Clock"
TimeSensor59.cycleInterval = 10
Transform47.addChildren([TimeSensor59])

ROUTE60 = ROUTE()
ROUTE60.fromField = "touchTime"
ROUTE60.fromNode = "TextTouchSensor"
ROUTE60.toField = "set_startTime"
ROUTE60.toNode = "Clock"
Transform47.addChildren([ROUTE60])

IntegerSequencer61 = IntegerSequencer()
IntegerSequencer61.DEF = "TimingSequencer"
IntegerSequencer61.key = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,1.0]
IntegerSequencer61.keyValue = [0,1,2,3,4,5,6,7,8,10]
Transform47.addChildren([IntegerSequencer61])

ROUTE62 = ROUTE()
ROUTE62.fromField = "fraction_changed"
ROUTE62.fromNode = "Clock"
ROUTE62.toField = "set_fraction"
ROUTE62.toNode = "TimingSequencer"
Transform47.addChildren([ROUTE62])

Script63 = Script()
Script63.DEF = "BindingSequencerEngine"

field64 = field()
field64.accessType = "inputOnly"
field64.name = "set_timeEvent"
field64.type = "SFInt32"
Script63.addField([field64])

field65 = field()
field65.accessType = "outputOnly"
field65.name = "bindView1"
field65.type = "SFBool"
Script63.addField([field65])

field66 = field()
field66.accessType = "outputOnly"
field66.name = "bindView2"
field66.type = "SFBool"
Script63.addField([field66])

field67 = field()
field67.accessType = "outputOnly"
field67.name = "bindView3"
field67.type = "SFBool"
Script63.addField([field67])

field68 = field()
field68.accessType = "outputOnly"
field68.name = "bindView4"
field68.type = "SFBool"
Script63.addField([field68])

field69 = field()
field69.accessType = "outputOnly"
field69.name = "bindView5"
field69.type = "SFBool"
Script63.addField([field69])

field70 = field()
field70.accessType = "inputOnly"
field70.name = "view1Bound"
field70.type = "SFBool"
Script63.addField([field70])

field71 = field()
field71.accessType = "inputOnly"
field71.name = "view2Bound"
field71.type = "SFBool"
Script63.addField([field71])

field72 = field()
field72.accessType = "inputOnly"
field72.name = "view3Bound"
field72.type = "SFBool"
Script63.addField([field72])

field73 = field()
field73.accessType = "inputOnly"
field73.name = "view4Bound"
field73.type = "SFBool"
Script63.addField([field73])

field74 = field()
field74.accessType = "initializeOnly"
field74.name = "priorInputvalue"
field74.type = "SFInt32"
field74.value = "-1"
Script63.addField([field74])

Script63.setSourceCode('''\n"+
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
"''')
Transform47.addChildren([Script63])
# drive Script with TimeSensor clock 

ROUTE75 = ROUTE()
ROUTE75.fromField = "value_changed"
ROUTE75.fromNode = "TimingSequencer"
ROUTE75.toField = "set_timeEvent"
ROUTE75.toNode = "BindingSequencerEngine"
Transform47.addChildren([ROUTE75])
# Script will bind and unbind Viewpoint nodes 

ROUTE76 = ROUTE()
ROUTE76.fromField = "bindView1"
ROUTE76.fromNode = "BindingSequencerEngine"
ROUTE76.toField = "set_bind"
ROUTE76.toNode = "View1"
Transform47.addChildren([ROUTE76])

ROUTE77 = ROUTE()
ROUTE77.fromField = "bindView2"
ROUTE77.fromNode = "BindingSequencerEngine"
ROUTE77.toField = "set_bind"
ROUTE77.toNode = "View2"
Transform47.addChildren([ROUTE77])

ROUTE78 = ROUTE()
ROUTE78.fromField = "bindView3"
ROUTE78.fromNode = "BindingSequencerEngine"
ROUTE78.toField = "set_bind"
ROUTE78.toNode = "View3"
Transform47.addChildren([ROUTE78])

ROUTE79 = ROUTE()
ROUTE79.fromField = "bindView4"
ROUTE79.fromNode = "BindingSequencerEngine"
ROUTE79.toField = "set_bind"
ROUTE79.toNode = "View4"
Transform47.addChildren([ROUTE79])

ROUTE80 = ROUTE()
ROUTE80.fromField = "bindView5"
ROUTE80.fromNode = "BindingSequencerEngine"
ROUTE80.toField = "set_bind"
ROUTE80.toNode = "ClickToAnimateView"
Transform47.addChildren([ROUTE80])
# Viewpoint nodes report bind and unbind events 

ROUTE81 = ROUTE()
ROUTE81.fromField = "isBound"
ROUTE81.fromNode = "View1"
ROUTE81.toField = "view1Bound"
ROUTE81.toNode = "BindingSequencerEngine"
Transform47.addChildren([ROUTE81])

ROUTE82 = ROUTE()
ROUTE82.fromField = "isBound"
ROUTE82.fromNode = "View2"
ROUTE82.toField = "view2Bound"
ROUTE82.toNode = "BindingSequencerEngine"
Transform47.addChildren([ROUTE82])

ROUTE83 = ROUTE()
ROUTE83.fromField = "isBound"
ROUTE83.fromNode = "View3"
ROUTE83.toField = "view3Bound"
ROUTE83.toNode = "BindingSequencerEngine"
Transform47.addChildren([ROUTE83])

ROUTE84 = ROUTE()
ROUTE84.fromField = "isBound"
ROUTE84.fromNode = "View4"
ROUTE84.toField = "view4Bound"
ROUTE84.toNode = "BindingSequencerEngine"
Transform47.addChildren([ROUTE84])
Scene17.addChildren([Transform47])
X3D0.scene = Scene17
