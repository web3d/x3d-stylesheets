import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.2")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setContent("CameraPrototypes.x3d").setName("title"))
        .addMeta(X3Dpackage.meta().setContent("Camera, CameraShot and CameraMovement prototypes that demonstrate storyboard capabilities and precise camera operation. This is a developmental effort for potential X3D Specification improvement.").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("Don Brutzman and Jeff Weekley").setName("creator"))
        .addMeta(X3Dpackage.meta().setContent("16 March 2009").setName("created"))
        .addMeta(X3Dpackage.meta().setContent("25 October 2016").setName("modified"))
        .addMeta(X3Dpackage.meta().setContent("Schematron rules, backed up by initialize() checks").setName("TODO"))
        .addMeta(X3Dpackage.meta().setContent("BeyondViewpointCameraNodesWeb3D2009.pdf").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/x3d/specifications/ISO-IEC-FDIS-19775-1.2-X3D-AbstractSpecification/Part01/components/navigation.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("Camera nodes for Viewpoint navigation control").setName("subject"))
        .addMeta(X3Dpackage.meta().setContent("CameraExamples.x3d").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d").setName("identifier"))
        .addMeta(X3Dpackage.meta().setContent("http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("../license.html").setName("license")))
      .setScene(X3Dpackage.Scene()
        # =============== Camera ============== 

        .addChildren(X3Dpackage.ProtoDeclare().setAppinfo("Camera node provides direct control of scene view to enable cinematic camera animation shot by shot and move by move along with still digital-photography settings for offline rendering of camera images.").setName("Camera")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            # Viewpoint-related fields, NavigationInfo-related fields and Camera-unique fields 

            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Text description to be displayed for this Camera").setName("description").setType("SFString"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Camera position in local transformation frame, which is default prior to first CameraShot initialPosition getting activated").setName("position").setType("SFVec3f").setValue("0 0 10"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Camera rotation in local transformation frame, which is default prior to first CameraShot initialPosition getting activated").setName("orientation").setType("SFRotation").setValue("0 0 1 0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("pi/4").setName("fieldOfView").setType("SFFloat").setValue("0.7854"))
            .addField(X3Dpackage.field().setAccessType("inputOnly").setAppinfo("input fraction drives interpolators").setName("set_fraction").setType("SFFloat"))
            .addField(X3Dpackage.field().setAccessType("inputOnly").setAppinfo("input event binds or unbinds this Camera").setName("set_bind").setType("SFBool"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("output event indicates when this Camera is bound").setName("bindTime").setType("SFTime"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("output event indicates whether this Camera is bound or unbound").setName("isBound").setType("SFBool"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Vector distance to near clipping plane corresponds to NavigationInfo.avatarSize[0]").setName("nearClipPlane").setType("SFFloat").setValue("0.25"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Vector distance to far clipping plane corresponds to NavigationInfo.visibilityLimit").setName("farClipPlane").setType("SFFloat").setValue("0.0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Array of CameraShot nodes which in turn contain CameraMovement nodes").setName("shots").setType("MFNode")
              # initialization nodes (if any) go here 

              )
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Whether camera headlight is on or off").setName("headlight").setType("SFBool").setValue("true"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Camera headlight color").setName("headlightColor").setType("SFColor").setValue("1 1 1"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Camera headlight intensity").setName("headlightIntensity").setType("SFFloat").setValue("1"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Camera filter color that modifies virtual lens capture").setName("filterColor").setType("SFColor").setValue("1 1 1"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Camera filter transparency that modifies virtual lens capture").setName("filterTransparency").setType("SFFloat").setValue("1"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("upVector changes modify camera orientation (and possibly vice versa)").setName("upVector").setType("SFVec3f").setValue("0 1 0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane").setName("fStop").setType("SFFloat").setValue("5.6"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Distance to focal plane of sharpest focus").setName("focusDistance").setType("SFFloat").setValue("10"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations").setName("isActive").setType("SFBool"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Total duration of contained enabled CameraShot (and thus CameraMovement) move durations").setName("totalDuration").setType("SFTime"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("OfflineRender node").setName("offlineRender").setType("SFNode")
              # initialization node (if any) goes here 

              )
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("enable console output to trace script computations and prototype progress").setName("traceEnabled").setType("SFBool").setValue("false")))
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Viewpoint().setDEF("CameraViewpoint")
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("description").setProtoField("description"))
                .addConnect(X3Dpackage.connect().setNodeField("position").setProtoField("position"))
                .addConnect(X3Dpackage.connect().setNodeField("orientation").setProtoField("orientation"))
                .addConnect(X3Dpackage.connect().setNodeField("fieldOfView").setProtoField("fieldOfView"))
                .addConnect(X3Dpackage.connect().setNodeField("set_bind").setProtoField("set_bind"))
                .addConnect(X3Dpackage.connect().setNodeField("bindTime").setProtoField("bindTime"))
                .addConnect(X3Dpackage.connect().setNodeField("isBound").setProtoField("isBound"))))
            # NavInfo EXAMINE used since some browsers (InstantReality) try to lock view to vertical when flying to avoid disorientation 

            .addChildren(X3Dpackage.NavigationInfo().setDEF("CameraNavInfo").setType(["EXAMINE","FLY","ANY"])
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("set_bind").setProtoField("set_bind"))
                # No need to bind outputs bindTime, isBound from NavigationInfo since Viewpoint outputs will suffice. TODO inform BitManagement that bindTime field is missing. 

                .addConnect(X3Dpackage.connect().setNodeField("headlight").setProtoField("headlight"))
                .addConnect(X3Dpackage.connect().setNodeField("visibilityLimit").setProtoField("farClipPlane"))))
            # this DirectionalLight replaces NavigationInfo headlight in order to add color capability 

            .addChildren(X3Dpackage.DirectionalLight().setDEF("CameraDirectionalLight").setGlobal(True)
              # TODO confirm other default field values match NavigationInfo spec 

              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("on").setProtoField("headlight"))
                .addConnect(X3Dpackage.connect().setNodeField("color").setProtoField("headlightColor"))
                .addConnect(X3Dpackage.connect().setNodeField("intensity").setProtoField("headlightIntensity"))))
            .addChildren(X3Dpackage.PositionInterpolator().setDEF("CameraPositionInterpolator").setKey([0,1]).setKeyValue([0,0,0,0,0,0])
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("set_fraction").setProtoField("set_fraction"))))
            .addChildren(X3Dpackage.OrientationInterpolator().setDEF("CameraOrientationInterpolator").setKey([0,1]).setKeyValue([0,1,0,0,0,1,0,0])
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("set_fraction").setProtoField("set_fraction"))))
            .addChildren(X3Dpackage.ROUTE().setFromField("value_changed").setFromNode("CameraPositionInterpolator").setToField("position").setToNode("CameraViewpoint"))
            .addChildren(X3Dpackage.ROUTE().setFromField("value_changed").setFromNode("CameraOrientationInterpolator").setToField("orientation").setToNode("CameraViewpoint"))
            .addChildren(X3Dpackage.Script(setDirectOutput = True, setMustEvaluate = True).setDEF("CameraScript")
              # binding is controlled externally, all camera operations proceed the same regardless of whether bound or not 

              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Text description to be displayed for this Camera").setName("description").setType("SFString"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Camera position in local transformation frame").setName("position").setType("SFVec3f"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Camera rotation in local transformation frame").setName("orientation").setType("SFRotation"))
              .addField(X3Dpackage.field().setAccessType("inputOnly").setAppinfo("input fraction drives interpolators").setName("set_fraction").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOnly").setAppinfo("input event binds or unbinds this Camera").setName("set_bind").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("pi/4").setName("fieldOfView").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Vector distance to near clipping plane").setName("nearClipPlane").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Vector distance to far clipping plane").setName("farClipPlane").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Array of CameraShot nodes which in turn contain CameraMovement nodes").setName("shots").setType("MFNode")
                # initialization nodes (if any) go here 

                )
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Camera filter color that modifies virtual lens capture").setName("filterColor").setType("SFColor"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Camera filter transparency that modifies virtual lens capture").setName("filterTransparency").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("upVector changes modify camera orientation (and possibly vice versa)").setName("upVector").setType("SFVec3f"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane").setName("fStop").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Distance to focal plane of sharpest focus").setName("focusDistance").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations").setName("isActive").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Total duration of contained enabled CameraShot (and thus CameraMovement) move durations").setName("totalDuration").setType("SFTime"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("OfflineRender node").setName("offlineRender").setType("SFNode")
                # initialization node (if any) goes here 

                )
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("node reference to permit getting setting fields from within Script").setName("ViewpointNode").setType("SFNode")
                .addChildren(X3Dpackage.Viewpoint().setUSE("CameraViewpoint")))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("node reference to permit getting setting fields from within Script").setName("NavInfoNode").setType("SFNode")
                .addChildren(X3Dpackage.NavigationInfo().setUSE("CameraNavInfo")))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("node reference to permit getting setting fields from within Script").setName("CameraPI").setType("SFNode")
                .addChildren(X3Dpackage.PositionInterpolator().setUSE("CameraPositionInterpolator")))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("node reference to permit getting setting fields from within Script").setName("CameraOI").setType("SFNode")
                .addChildren(X3Dpackage.OrientationInterpolator().setUSE("CameraOrientationInterpolator")))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("key array for interpolators").setName("key").setType("MFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("keyValue array for PositionInterpolator").setName("keyValuePosition").setType("MFVec3f"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("keyValue array for OrientationInterpolator").setName("keyValueOrientation").setType("MFRotation"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("whether internal CameraShot and CameraMove nodes are tracking or changed via ROUTE events").setName("animated").setType("SFBool").setValue("false"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("perform checkShots() function once immediately after initialization").setName("initialized").setType("SFBool").setValue("false"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("how many CameraShot nodes are contained in shots array").setName("shotCount").setType("SFInt32").setValue("0"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("how many CameraMove nodes are contained in moves array").setName("movesCount").setType("SFInt32").setValue("0"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("how many frames were created in current loop").setName("frameCount").setType("SFFloat").setValue("0"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("holding variable").setName("startTime").setType("SFTime").setValue("0"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("holding variable").setName("priorTraceTime").setType("SFTime").setValue("0"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("enable console output to trace script computations and prototype progress").setName("traceEnabled").setType("SFBool"))
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("description").setProtoField("description"))
                .addConnect(X3Dpackage.connect().setNodeField("position").setProtoField("position"))
                .addConnect(X3Dpackage.connect().setNodeField("orientation").setProtoField("orientation"))
                .addConnect(X3Dpackage.connect().setNodeField("set_fraction").setProtoField("set_fraction"))
                .addConnect(X3Dpackage.connect().setNodeField("set_bind").setProtoField("set_bind"))
                .addConnect(X3Dpackage.connect().setNodeField("fieldOfView").setProtoField("fieldOfView"))
                .addConnect(X3Dpackage.connect().setNodeField("nearClipPlane").setProtoField("nearClipPlane"))
                .addConnect(X3Dpackage.connect().setNodeField("farClipPlane").setProtoField("farClipPlane"))
                .addConnect(X3Dpackage.connect().setNodeField("shots").setProtoField("shots"))
                .addConnect(X3Dpackage.connect().setNodeField("filterColor").setProtoField("filterColor"))
                .addConnect(X3Dpackage.connect().setNodeField("filterTransparency").setProtoField("filterTransparency"))
                .addConnect(X3Dpackage.connect().setNodeField("upVector").setProtoField("upVector"))
                .addConnect(X3Dpackage.connect().setNodeField("fStop").setProtoField("fStop"))
                .addConnect(X3Dpackage.connect().setNodeField("focusDistance").setProtoField("focusDistance"))
                .addConnect(X3Dpackage.connect().setNodeField("isActive").setProtoField("isActive"))
                .addConnect(X3Dpackage.connect().setNodeField("totalDuration").setProtoField("totalDuration"))
                .addConnect(X3Dpackage.connect().setNodeField("offlineRender").setProtoField("offlineRender"))
                .addConnect(X3Dpackage.connect().setNodeField("traceEnabled").setProtoField("traceEnabled"))).setSourceCode('''\n"+
"ecmascript:\n"+
"function initialize () // CameraScript\n"+
"{\n"+
"//  tracePrint ('initialize start...');\n"+
"\n"+
"    NavInfoNode.avatarSize[0]   = nearClipPlane;\n"+
"\n"+
"    // remaining setups deferred to invocation of checkShots() method\n"+
"    // thanks to Yvonne Jung Fraunhofer for diagnosing better approach to function initialization\n"+
"    alwaysPrint ('initialize complete');\n"+
"}\n"+
"\n"+
"function checkShots (eventValue)\n"+
"{\n"+
"    tracePrint ('checkShots() method should only occur after initialize() methods in all other Scripts are complete');\n"+
"\n"+
"    // compute totalDuration by summing durations from contained CameraShot and CameraMovement nodes\n"+
"    totalDuration= 0;\n"+
"    shotCount  = shots.length;\n"+
"    movesCount = 0;\n"+
"    for (i = 0; i < shotCount; i++) // shots index\n"+
"    {\n"+
"       tracePrint ('shots[' + i + '].moves.length=' + shots[i].moves.length);\n"+
"       movesCount   += shots[i].moves.length;\n"+
"       totalDuration = totalDuration + shots[i].shotDuration;\n"+
"       if (shots[i].moves.length == 0)\n"+
"       {\n"+
"          alwaysPrint ('warning: CameraShot[' + i + '][' + shots[i].description + '] has no contained CameraMove nodes');\n"+
"       }\n"+
"    }\n"+
"    // size checks before proceeding\n"+
"    if (shotCount == 0)\n"+
"    {\n"+
"       alwaysPrint ('warning: no CameraShot nodes found for the shots, nothing to do!');\n"+
"       return;\n"+
"    }\n"+
"    else if (movesCount == 0)\n"+
"    {\n"+
"       alwaysPrint ('warning: no CameraMove nodes found for the shots, nothing to do!');\n"+
"       return;\n"+
"    }\n"+
"    else if (totalDuration == 0)\n"+
"    {\n"+
"       alwaysPrint ('warning: totalDuration = 0 seconds, nothing to do!');\n"+
"       return;\n"+
"    }\n"+
"    tracePrint ('number of contained CameraShot nodes=' + shotCount);\n"+
"    tracePrint ('number of contained CameraMove nodes=' + movesCount);\n"+
"    tracePrint ('totalDuration=' + totalDuration + ' seconds for all shots and moves');\n"+
"\n"+
"    // compute interpolators\n"+
"    var k = 0; // index for latest key, keyValuePosition, keyValueOrientation\n"+
"    for (i = 0; i < shotCount; i++) // shots index\n"+
"    {\n"+
"        if (i==0) // initial entries\n"+
"        {\n"+
"           key[0]                   = 0.0; // no previous move\n"+
"           keyValuePosition[0]      = shots[i].initialPosition;\n"+
"           keyValueOrientation[0]   = shots[i].initialOrientation;\n"+
"        }\n"+
"        else     // new shot repositions, reorients camera as clean break from preceding shot/move\n"+
"        {\n"+
"           key[k+1]                 = key[k]; // start from end from previous move\n"+
"           keyValuePosition[k+1]    = shots[i].initialPosition;\n"+
"           keyValueOrientation[k+1] = shots[i].initialOrientation;\n"+
"           k++;\n"+
"        }\n"+
"        tracePrint (shots[i].description);\n"+
"        tracePrint ('shots[i].moves.length=' + shots[i].moves.length);\n"+
"\n"+
"        for (j = 0; j < shots[i].moves.length; j++) // moves index\n"+
"        {\n"+
"            var durationFloat =              shots[i].moves[j].duration;  // implicit type conversion from SFTime\n"+
"            //  durationFloat = new SFFloat (shots[i].moves[j].duration); // explicit type conversion from SFTime\n"+
"            //  tracePrint ('durationFloat=' + durationFloat);\n"+
"            key[k+1]               = key[k] + (durationFloat / totalDuration);\n"+
"            keyValuePosition[k+1]  = shots[i].moves[j].goalPosition;\n"+
"            if (!animated)\n"+
"            {\n"+
"                 keyValueOrientation[k+1] = shots[i].moves[j].goalOrientation;\n"+
"            }\n"+
"            else\n"+
"            {\n"+
"                // using constructor SFRotation (SFVec3f fromVector, SFVec3f toVector)\n"+
"                // see X3D ECMAScript binding Table 7.18 — SFRotation instance creation functions\n"+
"\n"+
"                // test if difference vector is zero, if so maintain previous rotation\n"+
"                var shotVector = ViewpointNode.position.subtract(shots[i].moves[j].goalAimPoint).normalize();\n"+
"                if (shotVector.length() >= 0)\n"+
"                {\n"+
"                    // default view direction is along -Z axis\n"+
"                    shots[i].moves[j].goalOrientation = new SFRotation (new SFVec3f (0, 0, 1), shotVector);\n"+
"                    keyValueOrientation[k+1] = shots[i].moves[j].goalOrientation;\n"+
"                }\n"+
"                else // note (k > 0)\n"+
"                {\n"+
"                    keyValueOrientation[k+1] = keyValueOrientation[k];  // no change\n"+
"                }\n"+
"\n"+
"                tracePrint ('shots[' + i + '].moves[' + j + '].goalAimPoint=' + shots[i].moves[j].goalAimPoint.toString());\n"+
"                tracePrint ('        ViewpointNode.position=' + ViewpointNode.position.toString());\n"+
"                tracePrint ('          shotVector     delta=' + ViewpointNode.position.subtract(shots[i].moves[j].goalAimPoint).toString());\n"+
"                tracePrint ('          shotVector normalize=' + ViewpointNode.position.subtract(shots[i].moves[j].goalAimPoint).normalize().toString());\n"+
"                tracePrint ('               goalOrientation=' + shots[i].moves[j].goalOrientation.toString());\n"+
"                tracePrint ('      keyValueOrientation[k+1]=' + keyValueOrientation[k+1].toString() + '\\n');\n"+
"            }\n"+
"            k++; // update index to match latest key, keyValuePosition, keyValueOrientation\n"+
"\n"+
"            // check animated parameter:  set true if any of moves are tracking moves\n"+
"            if (!animated)  animated = shots[i].moves[j].tracking; // once true, remains true\n"+
"         // tracePrint ('shots[' + i + '].moves[' + j + '].tracking=' + shots[i].moves[j].tracking + ', animated=' + animated);\n"+
"\n"+
"            // intermediate trace\n"+
"            tracePrint ('                key=' + key);\n"+
"            tracePrint ('   keyValuePosition=' + keyValuePosition);\n"+
"            tracePrint ('keyValueOrientation=' + keyValueOrientation);\n"+
"            tracePrint ('- ' + shots[i].moves[j].description);\n"+
"        }\n"+
"    }\n"+
"    tracePrint ('                key=' + key);\n"+
"    tracePrint ('   keyValuePosition=' + keyValuePosition);\n"+
"    tracePrint ('keyValueOrientation=' + keyValueOrientation);\n"+
"    if (key.length != keyValuePosition.length)\n"+
"    {\n"+
"      alwaysPrint ('warning: internal error during array construction, ' +\n"+
"                  'key.length=' + key.length + ' must equal ' +\n"+
"                  'keyValuePosition.length=' + keyValuePosition.length);\n"+
"    }\n"+
"    if (key.length != keyValueOrientation.length)\n"+
"    {\n"+
"      alwaysPrint ('warning: internal error during array construction, ' +\n"+
"                  'key.length=' + key.length + ' must equal ' +\n"+
"                  'keyValueOrientation.length=' + keyValueOrientation.length);\n"+
"    }\n"+
"    if (key.length != (shotCount + movesCount))\n"+
"    {\n"+
"      alwaysPrint ('warning: internal error during array construction, ' +\n"+
"                  'key.length=' + key.length + ' must equal ' +\n"+
"                  '(shotCount + movesCount)=' + (shotCount + movesCount));\n"+
"    }\n"+
"    tracePrint ('           animated=' + animated);\n"+
"    // set node values\n"+
"    CameraPI.key      = key;\n"+
"    CameraOI.key      = key;\n"+
"    CameraPI.keyValue = keyValuePosition;\n"+
"    CameraOI.keyValue = keyValueOrientation;\n"+
"\n"+
"    if (!animated) // output results\n"+
"    {\n"+
"        tracePrint ('<PositionInterpolator    DEF=\\'CameraPositionInterpolator\\'    key=\\'' + stripBrackets(CameraPI.key) + '\\' keyValue=\\'' + stripBrackets(CameraPI.keyValue) + '\\'/>');\n"+
"        tracePrint ('<OrientationInterpolator DEF=\\'CameraOrientationInterpolator\\' key=\\'' + stripBrackets(CameraOI.key) + '\\' keyValue=\\'' + stripBrackets(CameraOI.keyValue) + '\\'/>');\n"+
"    }\n"+
"    tracePrint ('checkShots() complete');\n"+
"}\n"+
"\n"+
"function stripBrackets (fieldArray)\n"+
"{\n"+
"    // some browsers add brackets to array output strings, this function strips them\n"+
"    outputString = '';\n"+
"    for (i = 0; i < fieldArray.length; i++)\n"+
"    {\n"+
"       outputString += fieldArray[i].toString();\n"+
"       if (i < fieldArray.length - 1) outputString += ' ';\n"+
"    }\n"+
"    return outputString;\n"+
"}\n"+
"\n"+
"function set_fraction (eventValue, timestamp) // input event received for inputOnly field\n"+
"{\n"+
"   // traceEnabled = false;  // for testing purposes\n"+
"\n"+
"   // if Camera is being animated, immediately recompute interpolator settings\n"+
"   if (animated) checkShots (true);\n"+
"\n"+
"   // trace progress on console with reduced output frequency\n"+
"   if (frameCount == 0)\n"+
"   {\n"+
"      alwaysPrint ('Animation loop commencing, timestamp=' + timestamp);\n"+
"      startTime      = timestamp;\n"+
"      priorTraceTime = timestamp;\n"+
"      alwaysPrint ('shotClock=' + (timestamp - startTime) + ' seconds, frameCount=' + frameCount + ', fraction=' + eventValue + ', position=' + ViewpointNode.position.toString() + ', orientation=' + ViewpointNode.orientation.toString());\n"+
"\n"+
"      if (animated) // output results\n"+
"      {\n"+
"        // TODO how to report or speed up response?  alwaysPrint ('  aimPoint=' + aimPoint.toString());\n"+
"        tracePrint ('  <PositionInterpolator    DEF=\\'CameraPositionInterpolator\\'    key=\\'' + stripBrackets(CameraPI.key) + '\\' keyValue=\\'' + stripBrackets(CameraPI.keyValue) + '\\'/>');\n"+
"        tracePrint ('  <OrientationInterpolator DEF=\\'CameraOrientationInterpolator\\' key=\\'' + stripBrackets(CameraOI.key) + '\\' keyValue=\\'' + stripBrackets(CameraOI.keyValue) + '\\'/>');\n"+
"      }\n"+
"   }\n"+
"   else if ((timestamp - priorTraceTime) >= 1.0) // 1 second trace interval\n"+
"   {\n"+
"      alwaysPrint ('shotClock=' + (timestamp - startTime) + ' seconds, frameCount=' + frameCount + ', fraction=' + eventValue + ', position=' + ViewpointNode.position.toString() + ', orientation=' + ViewpointNode.orientation.toString());\n"+
"      priorTraceTime = timestamp;\n"+
"\n"+
"      if (animated) // output results\n"+
"      {\n"+
"        // TODO how to report or speed up response?  alwaysPrint ('  aimPoint=' + aimPoint.toString());\n"+
"        tracePrint ('  <PositionInterpolator    DEF=\\'CameraPositionInterpolator\\'    key=\\'' + stripBrackets(CameraPI.key) + '\\' keyValue=\\'' + stripBrackets(CameraPI.keyValue) + '\\'/>');\n"+
"        alwaysPrint ('  <OrientationInterpolator DEF=\\'CameraOrientationInterpolator\\' key=\\'' + stripBrackets(CameraOI.key) + '\\' keyValue=\\'' + stripBrackets(CameraOI.keyValue) + '\\'/>');\n"+
"      }\n"+
"   }\n"+
"   if (eventValue == 0)\n"+
"   {\n"+
"      // note that zero value is not necessarily sent first by TimeSensor, so otherwise ignored\n"+
"      frameCount++;\n"+
"   }\n"+
"   else if (eventValue == 1)\n"+
"   {\n"+
"      alwaysPrint ('shotClock=' + (timestamp - startTime) + ', frameCount=' + frameCount + ', fraction=' + eventValue + ', position=' + ViewpointNode.position.toString() + ', orientation=' + ViewpointNode.orientation.toString());\n"+
"      if (animated) // output results\n"+
"      {\n"+
"        // TODO how to report or speed up response?  alwaysPrint ('  aimPoint=' + aimPoint.toString());\n"+
"      }\n"+
"      alwaysPrint ('Animation loop complete.');\n"+
"      // do not unbind the Viewpoint and NavigationInfo nodes, let that be controlled externally\n"+
"   }\n"+
"   else\n"+
"   {\n"+
"      frameCount++;\n"+
"   }\n"+
"}\n"+
"\n"+
"function set_bind (eventValue) // input event received for inputOnly field\n"+
"{\n"+
"   // need to ensure CameraShot nodes are properly initialized\n"+
"   if (initialized == false)\n"+
"   {\n"+
"      checkShots (true);\n"+
"      initialized = true;\n"+
"   }\n"+
"   if (eventValue)\n"+
"   {\n"+
"       tracePrint ('Camera has been bound');\n"+
"   }\n"+
"   else\n"+
"   {\n"+
"       tracePrint ('Camera has been unbound');\n"+
"   }\n"+
"}\n"+
"\n"+
"function set_description (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    description = eventValue;\n"+
"}\n"+
"\n"+
"function set_position (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    position = eventValue;\n"+
"}\n"+
"\n"+
"function set_orientation (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    orientation = eventValue;\n"+
"}\n"+
"\n"+
"function set_fieldOfView (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    fieldOfView = eventValue;\n"+
"}\n"+
"\n"+
"function set_nearClipPlane (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    nearClipPlane = eventValue;\n"+
"}\n"+
"\n"+
"function set_farClipPlane (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    farClipPlane = eventValue;\n"+
"}\n"+
"\n"+
"function set_shots (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    shots = eventValue;\n"+
"}\n"+
"\n"+
"function set_filterColor (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    filterColor = eventValue;\n"+
"}\n"+
"\n"+
"function set_filterTransparency (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    filterTransparency = eventValue;\n"+
"}\n"+
"\n"+
"function set_upVector (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    upVector = eventValue;\n"+
"}\n"+
"\n"+
"function set_fStop (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    fStop = eventValue;\n"+
"}\n"+
"\n"+
"function set_focusDistance (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    focusDistance = eventValue;\n"+
"}\n"+
"\n"+
"function set_offlineRender (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    offlineRender = eventValue;\n"+
"}\n"+
"\n"+
"function set_key (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    key = eventValue;\n"+
"}\n"+
"\n"+
"function set_keyValuePosition (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    keyValuePosition = eventValue;\n"+
"}\n"+
"\n"+
"function set_keyValueOrientation (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    keyValueOrientation = eventValue;\n"+
"}\n"+
"\n"+
"function set_animated (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    animated = eventValue;\n"+
"}\n"+
"\n"+
"function tracePrint (outputValue)\n"+
"{\n"+
"	if (traceEnabled) alwaysPrint (outputValue);\n"+
"}\n"+
"function alwaysPrint (outputValue)\n"+
"{\n"+
"    // try to ensure outputValue is converted to string despite Browser.println idiosyncracies\n"+
"    var outputString = outputValue.toString(); // utility function according to spec\n"+
"    if (outputString == null) outputString = outputValue; // direct cast\n"+
"\n"+
"    if  (description.length > 0)\n"+
"         Browser.print ('[Camera: ' + description + '] ' + outputString + '\\n');\n"+
"    else\n"+
"         Browser.print ('[Camera] ' + outputString + '\\n');\n"+
"}\n"+
"''')
)
            .addChildren(X3Dpackage.ROUTE().setFromField("position").setFromNode("CameraScript").setToField("position").setToNode("CameraViewpoint"))
            .addChildren(X3Dpackage.ROUTE().setFromField("orientation").setFromNode("CameraScript").setToField("orientation").setToNode("CameraViewpoint"))
            .addChildren(X3Dpackage.ROUTE().setFromField("isActive").setFromNode("CameraScript").setToField("set_bind").setToNode("CameraViewpoint"))
            .addChildren(X3Dpackage.ROUTE().setFromField("isActive").setFromNode("CameraScript").setToField("set_bind").setToNode("CameraNavInfo"))
            .addChildren(X3Dpackage.ROUTE().setFromField("isActive").setFromNode("CameraScript").setToField("on").setToNode("CameraDirectionalLight"))))
        # =============== CameraShot ============== 

        .addChildren(X3Dpackage.ProtoDeclare().setAppinfo("CameraShot collects a specific set of CameraMovement animations that make up an individual shot.").setName("CameraShot")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Text description to be displayed for this CameraShot").setName("description").setType("SFString"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Whether this CameraShot can be activated").setName("enabled").setType("SFBool").setValue("true"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Set of CameraMovement nodes").setName("moves").setType("MFNode")
              # initializing CameraMovement nodes are inserted here by scene author using ProtoInstance 

              )
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Setup to reinitialize camera position for this shot").setName("initialPosition").setType("SFVec3f").setValue("0 0 10"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Setup to reinitialize camera rotation for this shot").setName("initialOrientation").setType("SFRotation").setValue("0 0 1 0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Setup to reinitialize aimpoint (relative location for camera direction) for this shot").setName("initialAimPoint").setType("SFVec3f").setValue("0 0 0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("pi/4").setName("initialFieldOfView").setType("SFFloat").setValue("0.7854"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane").setName("initialFStop").setType("SFFloat").setValue("5.6"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Distance to focal plane of sharpest focus").setName("initialFocusDistance").setType("SFFloat").setValue("10"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Subtotal duration of contained CameraMovement move durations").setName("shotDuration").setType("SFTime"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations").setName("isActive").setType("SFBool"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("enable console output to trace script computations and prototype progress").setName("traceEnabled").setType("SFBool").setValue("false")))
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Script(setDirectOutput = True, setMustEvaluate = True).setDEF("CameraShotScript")
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Text description to be displayed for this CameraShot").setName("description").setType("SFString"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Whether this CameraShot can be activated").setName("enabled").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Set of CameraMovement nodes").setName("moves").setType("MFNode")
                # initialization nodes (if any) go here 

                )
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Setup to reinitialize camera position for this shot").setName("initialPosition").setType("SFVec3f"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Setup to reinitialize camera rotation for this shot").setName("initialOrientation").setType("SFRotation"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Setup to reinitialize aimpoint (relative location for camera direction) for this shot").setName("initialAimPoint").setType("SFVec3f"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("pi/4").setName("initialFieldOfView").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane").setName("initialFStop").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Distance to focal plane of sharpest focus").setName("initialFocusDistance").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Subtotal duration of contained CameraMovement move durations").setName("shotDuration").setType("SFTime"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations").setName("isActive").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("enable console output to trace script computations and prototype progress").setName("traceEnabled").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("key array for interpolators").setName("key").setType("MFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("keyValue array for PositionInterpolator").setName("keyValuePosition").setType("MFVec3f"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("keyValue array for OrientationInterpolator").setName("keyValueOrientation").setType("MFRotation"))
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("description").setProtoField("description"))
                .addConnect(X3Dpackage.connect().setNodeField("enabled").setProtoField("enabled"))
                .addConnect(X3Dpackage.connect().setNodeField("moves").setProtoField("moves"))
                .addConnect(X3Dpackage.connect().setNodeField("initialPosition").setProtoField("initialPosition"))
                .addConnect(X3Dpackage.connect().setNodeField("initialOrientation").setProtoField("initialOrientation"))
                .addConnect(X3Dpackage.connect().setNodeField("initialAimPoint").setProtoField("initialAimPoint"))
                .addConnect(X3Dpackage.connect().setNodeField("initialFieldOfView").setProtoField("initialFieldOfView"))
                .addConnect(X3Dpackage.connect().setNodeField("initialFStop").setProtoField("initialFStop"))
                .addConnect(X3Dpackage.connect().setNodeField("initialFocusDistance").setProtoField("initialFocusDistance"))
                .addConnect(X3Dpackage.connect().setNodeField("shotDuration").setProtoField("shotDuration"))
                .addConnect(X3Dpackage.connect().setNodeField("isActive").setProtoField("isActive"))
                .addConnect(X3Dpackage.connect().setNodeField("traceEnabled").setProtoField("traceEnabled"))).setSourceCode('''\n"+
"ecmascript:\n"+
"function initialize () // CameraShotScript\n"+
"{\n"+
"//  tracePrint ('initialize start...');\n"+
"\n"+
"    // compute shotDuration by summing durations from contained CameraMovement nodes\n"+
"    shotDuration = 0;\n"+
"    for (i = 0; i < moves.length; i++)\n"+
"    {\n"+
"        shotDuration = shotDuration + moves[i].duration;\n"+
"    }\n"+
"    alwaysPrint ('number of contained CameraMove nodes=' + moves.length + ', shotDuration=' + shotDuration + ' seconds');\n"+
"\n"+
"//  tracePrint ('... initialize() complete');\n"+
"}\n"+
"\n"+
"function set_description (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    description = eventValue;\n"+
"}\n"+
"\n"+
"function set_enabled (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    enabled = eventValue;\n"+
"}\n"+
"\n"+
"function set_moves (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    moves = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialPosition (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialPosition = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialOrientation (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialOrientation = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialAimPoint (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialAimPoint = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialFieldOfView (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialFieldOfView = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialFStop (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialFStop = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialFocusDistance (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialFocusDistance = eventValue;\n"+
"}\n"+
"\n"+
"function set_key (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    key = eventValue;\n"+
"}\n"+
"\n"+
"function set_keyValuePosition (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    keyValuePosition = eventValue;\n"+
"}\n"+
"\n"+
"function set_keyValueOrientation (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    keyValueOrientation = eventValue;\n"+
"}\n"+
"\n"+
"// TODO consider method set_active for constructed Camera node BooleanSequencer to send isActive\n"+
"\n"+
"function tracePrint (outputValue)\n"+
"{\n"+
"	if (traceEnabled) alwaysPrint (outputValue);\n"+
"}\n"+
"function alwaysPrint (outputValue)\n"+
"{\n"+
"	// try to ensure outputValue is converted to string despite browser idiosyncracies\n"+
"    var outputString = outputValue.toString(); // utility function according to spec\n"+
"    if (outputString == null) outputString = outputValue; // direct cast\n"+
"\n"+
"    if  (description.length > 0)\n"+
"         Browser.print ('[CameraShot: ' + description + '] ' + outputString + '\\n');\n"+
"    else\n"+
"         Browser.print ('[CameraShot] ' + outputString + '\\n');\n"+
"}\n"+
"''')
)
            # Add any ROUTEs here, going from Script to other nodes within ProtoBody 

            ))
        # =============== CameraMovement ============== 

        .addChildren(X3Dpackage.ProtoDeclare().setAppinfo("CameraMovement node defines a single camera movement animation including goalPosition, goalOrientation, goalAimPoint and goalFieldOfView.").setName("CameraMovement")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Text description to be displayed for this CameraMovement").setName("description").setType("SFString"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Whether this CameraMovement can be activated").setName("enabled").setType("SFBool").setValue("true"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Duration in seconds for this move").setName("duration").setType("SFFloat").setValue("0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Goal camera position for this move").setName("goalPosition").setType("SFVec3f").setValue("0 0 10"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Goal camera rotation for this move").setName("goalOrientation").setType("SFRotation").setValue("0 0 1 0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Whether or not camera direction is tracking towards the aimPoint").setName("tracking").setType("SFBool").setValue("false"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Goal aimPoint for this move, ignored if tracking=false").setName("goalAimPoint").setType("SFVec3f").setValue("0 0 0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Goal fieldOfView for this move").setName("goalFieldOfView").setType("SFFloat").setValue("0.7854"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane").setName("goalFStop").setType("SFFloat").setValue("5.6"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Distance to focal plane of sharpest focus").setName("goalFocusDistance").setType("SFFloat").setValue("10"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations").setName("isActive").setType("SFBool"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("enable console output to trace script computations and prototype progress").setName("traceEnabled").setType("SFBool").setValue("false")))
          .setProtoBody(X3Dpackage.ProtoBody()
            # First node determines node type of this prototype 

            # Subsequent nodes do not render, but still must be a valid X3D subgraph 

            # Script holds CameraMovement initialization values for query by parent CameraShot, and also permits changing values via events 

            .addChildren(X3Dpackage.Script(setDirectOutput = True, setMustEvaluate = True).setDEF("CameraMovementScript")
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Text description to be displayed for this CameraMovement").setName("description").setType("SFString"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Whether this CameraMovement can be activated").setName("enabled").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Duration in seconds for this move").setName("duration").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Goal camera position for this move").setName("goalPosition").setType("SFVec3f"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Goal camera rotation for this move").setName("goalOrientation").setType("SFRotation"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Whether or not camera direction is tracking towards the aimPoint").setName("tracking").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Goal aimPoint for this move, ignored if tracking=false").setName("goalAimPoint").setType("SFVec3f"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Goal fieldOfView for this move").setName("goalFieldOfView").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane").setName("goalFStop").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Distance to focal plane of sharpest focus").setName("goalFocusDistance").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations").setName("isActive").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("enable console output to trace script computations and prototype progress").setName("traceEnabled").setType("SFBool"))
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("description").setProtoField("description"))
                .addConnect(X3Dpackage.connect().setNodeField("enabled").setProtoField("enabled"))
                .addConnect(X3Dpackage.connect().setNodeField("duration").setProtoField("duration"))
                .addConnect(X3Dpackage.connect().setNodeField("goalPosition").setProtoField("goalPosition"))
                .addConnect(X3Dpackage.connect().setNodeField("goalOrientation").setProtoField("goalOrientation"))
                .addConnect(X3Dpackage.connect().setNodeField("tracking").setProtoField("tracking"))
                .addConnect(X3Dpackage.connect().setNodeField("goalAimPoint").setProtoField("goalAimPoint"))
                .addConnect(X3Dpackage.connect().setNodeField("goalFieldOfView").setProtoField("goalFieldOfView"))
                .addConnect(X3Dpackage.connect().setNodeField("goalFStop").setProtoField("goalFStop"))
                .addConnect(X3Dpackage.connect().setNodeField("goalFocusDistance").setProtoField("goalFocusDistance"))
                .addConnect(X3Dpackage.connect().setNodeField("isActive").setProtoField("isActive"))
                .addConnect(X3Dpackage.connect().setNodeField("traceEnabled").setProtoField("traceEnabled"))).setSourceCode('''\n"+
"ecmascript:\n"+
"function initialize () // CameraMovementScript\n"+
"{\n"+
"//  tracePrint ('initialize start...');\n"+
"    alwaysPrint ('initialize goalPosition=' + goalPosition.toString() + ', goalOrientation=' + goalOrientation.toString() +\n"+
"                           ', goalAimPoint=' + goalAimPoint.toString() // + ', tracking=' + tracking.toString()\n"+
"                           );\n"+
"    if (duration < 0)\n"+
"    {\n"+
"       alwaysPrint ('error: negative duration=' + duration + ', reset to 0 and ignored');\n"+
"       duration = 0;\n"+
"    }\n"+
"    else if (duration == 0)\n"+
"    {\n"+
"       alwaysPrint ('warning: duration=0, nothing to do!');\n"+
"    }\n"+
"    tracePrint ('... initialize complete');\n"+
"}\n"+
"\n"+
"function set_goalAimPoint (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalAimPoint_changed = eventValue;\n"+
"    tracePrint ('goalAimPoint=' + goalAimPoint.toString());\n"+
"\n"+
"    // updated goalOrientation tracking is handled by Camera recomputing the OrientationInterpolator\n"+
"}\n"+
"\n"+
"function set_description (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    description = eventValue;\n"+
"}\n"+
"\n"+
"function set_enabled (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    enabled = eventValue;\n"+
"}\n"+
"\n"+
"function set_duration (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    duration = eventValue;\n"+
"}\n"+
"\n"+
"function set_goalPosition (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalPosition = eventValue;\n"+
"}\n"+
"\n"+
"function set_goalOrientation (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalOrientation = eventValue;\n"+
"}\n"+
"\n"+
"function set_tracking (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    tracking = eventValue;\n"+
"}\n"+
"\n"+
"function set_goalFieldOfView (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalFieldOfView = eventValue;\n"+
"}\n"+
"\n"+
"function set_goalFStop (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalFStop = eventValue;\n"+
"}\n"+
"\n"+
"function set_goalFocusDistance (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalFocusDistance = eventValue;\n"+
"}\n"+
"\n"+
"// TODO consider method set_active for constructed Camera node BooleanSequencer to send isActive\n"+
"\n"+
"function tracePrint (outputValue)\n"+
"{\n"+
"	if (traceEnabled) alwaysPrint (outputValue);\n"+
"}\n"+
"\n"+
"function alwaysPrint (outputValue)\n"+
"{\n"+
"	// try to ensure outputValue is converted to string despite browser idiosyncracies\n"+
"    var outputString = outputValue.toString(); // utility function according to spec\n"+
"    if (outputString == null) outputString = outputValue; // direct cast\n"+
"\n"+
"    if  (description.length > 0)\n"+
"         Browser.print ('[CameraMovement: ' + description + '] ' + outputString + '\\n');\n"+
"    else\n"+
"         Browser.print ('[CameraMovement] ' + outputString + '\\n');\n"+
"}\n"+
"''')
)
            # Add any ROUTEs here, going from Script to other nodes within ProtoBody 

            ))
        # =============== OfflineRender ============== 

        .addChildren(X3Dpackage.ProtoDeclare().setAppinfo("OfflineRender defines a parameters for offline rendering of Camera animation output to a movie file (or possibly a still shot).").setName("OfflineRender")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            # TODO non-photorealistic rendering (NPR) parameters 

            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Text description to be displayed for this OfflineRender").setName("description").setType("SFString"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Whether this OfflineRender can be activated").setName("enabled").setType("SFBool").setValue("true"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Frames per second recorded for this rendering").setName("frameRate").setType("SFFloat").setValue("30"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Size of frame in number of pixels width and height").setName("frameSize").setType("SFVec2f").setValue("640 480"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Relative dimensions of pixel height/width typically 1.33 or 1").setName("pixelAspectRatio").setType("SFFloat").setValue("1.33"))
            .addField(X3Dpackage.field().setAccessType("inputOnly").setAppinfo("Begin render operation").setName("set_startTime").setType("SFTime"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Progress performing render operation (0..1)").setName("progress").setType("SFFloat"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Render operation complete").setName("renderCompleteTime").setType("SFTime"))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("Format of rendered output movie (mpeg mp4 etc.), use first supported format").setName("movieFormat").setType("MFString").setValue("\"mpeg\""))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("Format of rendered output images (png jpeg gif tiff etc.) use first supported format").setName("imageFormat").setType("MFString").setValue("\"png\""))
            .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("enable console output to trace script computations and prototype progress").setName("traceEnabled").setType("SFBool").setValue("false")))
          .setProtoBody(X3Dpackage.ProtoBody()
            # First node determines node type of this prototype 

            # Subsequent nodes do not render, but still must be a valid X3D subgraph 

            .addChildren(X3Dpackage.Script(setMustEvaluate = True).setDEF("OfflineRenderScript")
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Text description to be displayed for this OfflineRender").setName("description").setType("SFString"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Whether this OfflineRender can be activated").setName("enabled").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Frames per second recorded for this rendering").setName("frameRate").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Size of frame in number of pixels width and height").setName("frameSize").setType("SFVec2f"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("Relative dimensions of pixel height/width typically 1.33 or 1").setName("pixelAspectRatio").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("inputOnly").setAppinfo("Begin render operation").setName("set_startTime").setType("SFTime"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Progress performing render operation (0..1)").setName("progress").setType("SFFloat"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("Render operation complete").setName("renderCompleteTime").setType("SFTime"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("Format of rendered output movie (mpeg mp4 etc.)").setName("movieFormat").setType("MFString"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("Format of rendered output images (png jpeg gif tiff etc.)").setName("imageFormat").setType("MFString"))
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("enable console output to trace script computations and prototype progress").setName("traceEnabled").setType("SFBool"))
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("description").setProtoField("description"))
                .addConnect(X3Dpackage.connect().setNodeField("enabled").setProtoField("enabled"))
                .addConnect(X3Dpackage.connect().setNodeField("frameRate").setProtoField("frameRate"))
                .addConnect(X3Dpackage.connect().setNodeField("frameSize").setProtoField("frameSize"))
                .addConnect(X3Dpackage.connect().setNodeField("pixelAspectRatio").setProtoField("pixelAspectRatio"))
                .addConnect(X3Dpackage.connect().setNodeField("set_startTime").setProtoField("set_startTime"))
                .addConnect(X3Dpackage.connect().setNodeField("progress").setProtoField("progress"))
                .addConnect(X3Dpackage.connect().setNodeField("renderCompleteTime").setProtoField("renderCompleteTime"))
                .addConnect(X3Dpackage.connect().setNodeField("movieFormat").setProtoField("movieFormat"))
                .addConnect(X3Dpackage.connect().setNodeField("imageFormat").setProtoField("imageFormat"))
                .addConnect(X3Dpackage.connect().setNodeField("traceEnabled").setProtoField("traceEnabled"))).setSourceCode('''\n"+
"ecmascript:\n"+
"function initialize () // OfflineRenderScript\n"+
"{\n"+
"//  tracePrint ('initialize start...');\n"+
"\n"+
"    tracePrint ('... initialize complete');\n"+
"}\n"+
"\n"+
"function set_description (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    description = eventValue;\n"+
"}\n"+
"\n"+
"function set_enabled (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    enabled = eventValue;\n"+
"}\n"+
"\n"+
"function set_frameRate (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    frameRate = eventValue;\n"+
"}\n"+
"\n"+
"function set_frameSize (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    frameSize = eventValue;\n"+
"}\n"+
"\n"+
"function set_pixelAspectRatio (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    pixelAspectRatio = eventValue;\n"+
"}\n"+
"\n"+
"function set_startTime (eventValue) // input event received for inputOnly field\n"+
"{\n"+
"   // do something with input eventValue;\n"+
"}\n"+
"\n"+
"function tracePrint (outputValue)\n"+
"{\n"+
"	if (traceEnabled) alwaysPrint (outputValue);\n"+
"}\n"+
"\n"+
"function alwaysPrint (outputValue)\n"+
"{\n"+
"	// try to ensure outputValue is converted to string despite browser idiosyncracies\n"+
"    var outputString = outputValue.toString(); // utility function according to spec\n"+
"    if (outputString == null) outputString = outputValue; // direct cast\n"+
"\n"+
"    if  (description.length > 0)\n"+
"         Browser.print ('[OfflineRender: ' + description + '] ' + outputString + '\\n');\n"+
"    else\n"+
"         Browser.print ('[OfflineRender] ' + outputString + '\\n');\n"+
"}\n"+
"''')
)
            # Add any ROUTEs here, going from Script to other nodes within ProtoBody 

            ))
        # =============== Launch Prototype Example ============== 

        .addChildren(X3Dpackage.Background().setSkyColor([0.282353,0.380392,0.470588]))
        .addChildren(X3Dpackage.Anchor().setDescription("launch CameraExample scene").setUrl(["CameraExamples.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d","CameraExamples.wrl","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.wrl"])
          .addChildren(X3Dpackage.Transform()
            .addChildren(X3Dpackage.Shape()
              .setGeometry(X3Dpackage.Text().setString(["CameraPrototypes.x3d","defines multiple prototype nodes","","Click on this text to see","CameraExamples.x3d scene"])
                .setFontStyle(X3Dpackage.FontStyle(setJustify = ["MIDDLE","MIDDLE"])))
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDiffuseColor([1,1,0.2]))))))))

