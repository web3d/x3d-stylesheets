import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.0")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setContent("title").setName("flowers2.x3d"))
        .addMeta(X3Dpackage.meta().setContent("John Carlson").setName("author"))
        .addMeta(X3Dpackage.meta().setContent("John Carlson").setName("transcriber"))
        .addMeta(X3Dpackage.meta().setContent("23 January 2005").setName("created"))
        .addMeta(X3Dpackage.meta().setContent("05 May 2017").setName("modified"))
        .addMeta(X3Dpackage.meta().setContent("2 random mathematical roses in spherical dimensions. rho = a + b * cos(c * theta) * cos(d * phi)").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("https://coderextreme.net/x3d/flowers2.x3d").setName("url"))
        .addMeta(X3Dpackage.meta().setContent("manually written").setName("generator")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.NavigationInfo().setType(["EXAMINE","ANY"]))
        .addChildren(X3Dpackage.Viewpoint().setDescription("Two mathematical orbitals").setPosition([0,0,50]))
        .addChildren(X3Dpackage.Group()
          .addChildren(X3Dpackage.DirectionalLight().setDirection([1,1,1]))
          .addChildren(X3Dpackage.Transform().setDEF("OrbitTransform").setTranslation([8,0,0])
            .addChildren(X3Dpackage.Shape()
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDiffuseColor([0,0.5,1]).setSpecularColor([0,0.5,1])))
              .setGeometry(X3Dpackage.IndexedFaceSet(setConvex = False, setCreaseAngle = 0).setDEF("Orbit")
                .setCoord(X3Dpackage.Coordinate().setDEF("OrbitCoordinates")))))
          .addChildren(X3Dpackage.Transform().setDEF("OrbitTransform2").setTranslation([-8,0,0])
            .addChildren(X3Dpackage.Shape()
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDiffuseColor([1,0.5,0]).setSpecularColor([1,0.5,0]).setTransparency(0.75)))
              .setGeometry(X3Dpackage.IndexedFaceSet(setCreaseAngle = 0).setDEF("Orbit2")
                .setCoord(X3Dpackage.Coordinate().setDEF("OrbitCoordinates2")))))
          .addChildren(X3Dpackage.TimeSensor().setDEF("Clock").setCycleInterval(16).setLoop(True))
          .addChildren(X3Dpackage.OrientationInterpolator().setDEF("OrbitPath").setKey([0.0,0.50,1.0]).setKeyValue([1.0,0.0,0.0,0.0,1.0,0.0,0.0,3.14,1.0,0.0,0.0,6.28]))
          .addChildren(X3Dpackage.Script().setDEF("OrbitScript")
            .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_fraction").setType("SFFloat"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setName("coordinates").setType("MFVec3f"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setName("coordIndexes").setType("MFInt32")).setSourceCode('''\n"+
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
)
          .addChildren(X3Dpackage.Script().setDEF("OrbitScript2")
            .addField(X3Dpackage.field().setAccessType("inputOnly").setName("set_fraction").setType("SFFloat"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setName("coordinates").setType("MFVec3f"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setName("coordIndexes").setType("MFInt32")).setSourceCode('''\n"+
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
))
        .addChildren(X3Dpackage.ROUTE().setFromField("coordIndexes").setFromNode("OrbitScript").setToField("coordIndex").setToNode("Orbit"))
        .addChildren(X3Dpackage.ROUTE().setFromField("coordinates").setFromNode("OrbitScript").setToField("point").setToNode("OrbitCoordinates"))
        .addChildren(X3Dpackage.ROUTE().setFromField("fraction_changed").setFromNode("Clock").setToField("set_fraction").setToNode("OrbitScript"))
        .addChildren(X3Dpackage.ROUTE().setFromField("coordIndexes").setFromNode("OrbitScript2").setToField("coordIndex").setToNode("Orbit2"))
        .addChildren(X3Dpackage.ROUTE().setFromField("coordinates").setFromNode("OrbitScript2").setToField("point").setToNode("OrbitCoordinates2"))
        .addChildren(X3Dpackage.ROUTE().setFromField("fraction_changed").setFromNode("Clock").setToField("set_fraction").setToNode("OrbitScript2"))
        .addChildren(X3Dpackage.ROUTE().setFromField("fraction_changed").setFromNode("Clock").setToField("set_fraction").setToNode("OrbitPath"))
        .addChildren(X3Dpackage.ROUTE().setFromField("value_changed").setFromNode("OrbitPath").setToField("rotation").setToNode("OrbitTransform"))
        .addChildren(X3Dpackage.ROUTE().setFromField("value_changed").setFromNode("OrbitPath").setToField("rotation").setToNode("OrbitTransform2"))))

