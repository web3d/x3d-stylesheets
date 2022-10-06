from X3Dpackage import *
X3D0 = X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.0")
head1 = head()
meta2 = meta()
meta2.setContent("title")
meta2.setName("flowers2.x3d")
head1.addMeta(meta2)
meta3 = meta()
meta3.setContent("John Carlson")
meta3.setName("author")
head1.addMeta(meta3)
meta4 = meta()
meta4.setContent("John Carlson")
meta4.setName("transcriber")
head1.addMeta(meta4)
meta5 = meta()
meta5.setContent("23 January 2005")
meta5.setName("created")
head1.addMeta(meta5)
meta6 = meta()
meta6.setContent("05 May 2017")
meta6.setName("modified")
head1.addMeta(meta6)
meta7 = meta()
meta7.setContent("2 random mathematical roses in spherical dimensions. rho = a + b * cos(c * theta) * cos(d * phi)")
meta7.setName("description")
head1.addMeta(meta7)
meta8 = meta()
meta8.setContent("https://coderextreme.net/x3d/flowers2.x3d")
meta8.setName("url")
head1.addMeta(meta8)
meta9 = meta()
meta9.setContent("manually written")
meta9.setName("generator")
head1.addMeta(meta9)
X3D0.setHead(head1)
Scene10 = Scene()
NavigationInfo11 = NavigationInfo()
NavigationInfo11.setType(["EXAMINE","ANY"])
Scene10.addChildren(NavigationInfo11)
Viewpoint12 = Viewpoint()
Viewpoint12.setDescription("Two mathematical orbitals")
Viewpoint12.setPosition([0,0,50])
Scene10.addChildren(Viewpoint12)
Group13 = Group()
DirectionalLight14 = DirectionalLight()
DirectionalLight14.setDirection([1,1,1])
Group13.addChildren(DirectionalLight14)
Transform15 = Transform()
Transform15.setDEF("OrbitTransform")
Transform15.setTranslation([8,0,0])
Shape16 = Shape()
Appearance17 = Appearance()
Material18 = Material()
Material18.setDiffuseColor([0,0.5,1])
Material18.setSpecularColor([0,0.5,1])
Appearance17.setMaterial(Material18)
Shape16.setAppearance(Appearance17)
IndexedFaceSet19 = IndexedFaceSet(convex = False, creaseAngle = 0)
IndexedFaceSet19.setDEF("Orbit")
Coordinate20 = Coordinate()
Coordinate20.setDEF("OrbitCoordinates")
IndexedFaceSet19.setCoord(Coordinate20)
Shape16.setGeometry(IndexedFaceSet19)
Transform15.addChildren(Shape16)
Group13.addChildren(Transform15)
Transform21 = Transform()
Transform21.setDEF("OrbitTransform2")
Transform21.setTranslation([-8,0,0])
Shape22 = Shape()
Appearance23 = Appearance()
Material24 = Material()
Material24.setDiffuseColor([1,0.5,0])
Material24.setSpecularColor([1,0.5,0])
Material24.setTransparency(0.75)
Appearance23.setMaterial(Material24)
Shape22.setAppearance(Appearance23)
IndexedFaceSet25 = IndexedFaceSet(creaseAngle = 0)
IndexedFaceSet25.setDEF("Orbit2")
Coordinate26 = Coordinate()
Coordinate26.setDEF("OrbitCoordinates2")
IndexedFaceSet25.setCoord(Coordinate26)
Shape22.setGeometry(IndexedFaceSet25)
Transform21.addChildren(Shape22)
Group13.addChildren(Transform21)
TimeSensor27 = TimeSensor()
TimeSensor27.setDEF("Clock")
TimeSensor27.setCycleInterval(16)
TimeSensor27.setLoop(True)
Group13.addChildren(TimeSensor27)
OrientationInterpolator28 = OrientationInterpolator()
OrientationInterpolator28.setDEF("OrbitPath")
OrientationInterpolator28.setKey([0.0,0.50,1.0])
OrientationInterpolator28.setKeyValue([1.0,0.0,0.0,0.0,1.0,0.0,0.0,3.14,1.0,0.0,0.0,6.28])
Group13.addChildren(OrientationInterpolator28)
Script29 = Script()
Script29.setDEF("OrbitScript")
field30 = field()
field30.setAccessType("inputOnly")
field30.setName("set_fraction")
field30.setType("SFFloat")
Script29.addField(field30)
field31 = field()
field31.setAccessType("outputOnly")
field31.setName("coordinates")
field31.setType("MFVec3f")
Script29.addField(field31)
field32 = field()
field32.setAccessType("outputOnly")
field32.setName("coordIndexes")
field32.setType("MFInt32")
Script29.addField(field32)

Script29.setSourceCode('''\n"+
"\n"+
"ecmascript:\n"+
"\n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"\n"+
"function initialize() {\n"+
"     resolution = 100;\n"+
"     generateCoordinates(resolution);\n"+
"     var localci = [];\n"+
"     for ( i = 0; i < resolution-1; i++) {\n"+
"     	for ( j = 0; j < resolution-1; j++) {\n"+
"	     localci.push(i*resolution+j);\n"+
"	     localci.push(i*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j);\n"+
"	     localci.push(-1);\n"+
"	}\n"+
"    }\n"+
"    coordIndexes = new MFInt32(localci);\n"+
"}\n"+
"\n"+
"function generateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var localc = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta) * Math.cos(h * phi);\n"+
"		localc.push(new SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		));\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     coordinates = new MFVec3f(localc);\n"+
"}\n"+
"\n"+
"function set_fraction(fraction, eventTime) {\n"+
"	choice = Math.floor(Math.random() * 4);\n"+
"	switch (choice) {\n"+
"	case 0:\n"+
"		e += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 1:\n"+
"		f += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 2:\n"+
"		g += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 3:\n"+
"		h += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	}\n"+
"	if (f < 1) {\n"+
"		f = 10;\n"+
"	}\n"+
"	if (g < 1) {\n"+
"		g = 4;\n"+
"	}\n"+
"	if (h < 1) {\n"+
"		h = 4;\n"+
"	}\n"+
"	resolution = 100;\n"+
"	generateCoordinates(resolution);\n"+
"}\n"+
"      ''')
Group13.addChildren(Script29)
Script33 = Script()
Script33.setDEF("OrbitScript2")
field34 = field()
field34.setAccessType("inputOnly")
field34.setName("set_fraction")
field34.setType("SFFloat")
Script33.addField(field34)
field35 = field()
field35.setAccessType("outputOnly")
field35.setName("coordinates")
field35.setType("MFVec3f")
Script33.addField(field35)
field36 = field()
field36.setAccessType("outputOnly")
field36.setName("coordIndexes")
field36.setType("MFInt32")
Script33.addField(field36)

Script33.setSourceCode('''\n"+
"\n"+
"ecmascript:\n"+
"\n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"\n"+
"function initialize() {\n"+
"     resolution = 100;\n"+
"     generateCoordinates(resolution);\n"+
"     var localci = [];\n"+
"     for ( i = 0; i < resolution-1; i++) {\n"+
"     	for ( j = 0; j < resolution-1; j++) {\n"+
"	     localci.push(i*resolution+j);\n"+
"	     localci.push(i*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j);\n"+
"	     localci.push(-1);\n"+
"	}\n"+
"    }\n"+
"    coordIndexes = new MFInt32(localci);\n"+
"}\n"+
"\n"+
"function generateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var localc = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta) * Math.cos(h * phi);\n"+
"		localc.push(new SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		));\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     \n"+
"     coordinates = new MFVec3f(localc);\n"+
"}\n"+
"\n"+
"function set_fraction(fraction, eventTime) {\n"+
"	choice = Math.floor(Math.random() * 4);\n"+
"	switch (choice) {\n"+
"	case 0:\n"+
"		e += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 1:\n"+
"		f += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 2:\n"+
"		g += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 3:\n"+
"		h += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	}\n"+
"	if (f < 1) {\n"+
"		f = 10;\n"+
"	}\n"+
"	if (g < 1) {\n"+
"		g = 4;\n"+
"	}\n"+
"	if (h < 1) {\n"+
"		h = 4;\n"+
"	}\n"+
"	resolution = 100;\n"+
"	generateCoordinates(resolution);\n"+
"}\n"+
"      ''')
Group13.addChildren(Script33)
Scene10.addChildren(Group13)
ROUTE37 = ROUTE()
ROUTE37.setFromField("coordIndexes")
ROUTE37.setFromNode("OrbitScript")
ROUTE37.setToField("coordIndex")
ROUTE37.setToNode("Orbit")
Scene10.addChildren(ROUTE37)
ROUTE38 = ROUTE()
ROUTE38.setFromField("coordinates")
ROUTE38.setFromNode("OrbitScript")
ROUTE38.setToField("point")
ROUTE38.setToNode("OrbitCoordinates")
Scene10.addChildren(ROUTE38)
ROUTE39 = ROUTE()
ROUTE39.setFromField("fraction_changed")
ROUTE39.setFromNode("Clock")
ROUTE39.setToField("set_fraction")
ROUTE39.setToNode("OrbitScript")
Scene10.addChildren(ROUTE39)
ROUTE40 = ROUTE()
ROUTE40.setFromField("coordIndexes")
ROUTE40.setFromNode("OrbitScript2")
ROUTE40.setToField("coordIndex")
ROUTE40.setToNode("Orbit2")
Scene10.addChildren(ROUTE40)
ROUTE41 = ROUTE()
ROUTE41.setFromField("coordinates")
ROUTE41.setFromNode("OrbitScript2")
ROUTE41.setToField("point")
ROUTE41.setToNode("OrbitCoordinates2")
Scene10.addChildren(ROUTE41)
ROUTE42 = ROUTE()
ROUTE42.setFromField("fraction_changed")
ROUTE42.setFromNode("Clock")
ROUTE42.setToField("set_fraction")
ROUTE42.setToNode("OrbitScript2")
Scene10.addChildren(ROUTE42)
ROUTE43 = ROUTE()
ROUTE43.setFromField("fraction_changed")
ROUTE43.setFromNode("Clock")
ROUTE43.setToField("set_fraction")
ROUTE43.setToNode("OrbitPath")
Scene10.addChildren(ROUTE43)
ROUTE44 = ROUTE()
ROUTE44.setFromField("value_changed")
ROUTE44.setFromNode("OrbitPath")
ROUTE44.setToField("rotation")
ROUTE44.setToNode("OrbitTransform")
Scene10.addChildren(ROUTE44)
ROUTE45 = ROUTE()
ROUTE45.setFromField("value_changed")
ROUTE45.setFromNode("OrbitPath")
ROUTE45.setToField("rotation")
ROUTE45.setToNode("OrbitTransform2")
Scene10.addChildren(ROUTE45)
X3D0.setScene(Scene10)
