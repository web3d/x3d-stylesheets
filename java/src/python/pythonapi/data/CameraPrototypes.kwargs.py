from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.2",    head1 = head(    meta2 = meta(content="CameraPrototypes.x3d", name="title"), 
    meta3 = meta(content="Camera, CameraShot and CameraMovement prototypes that demonstrate storyboard capabilities and precise camera operation. This is a developmental effort for potential X3D Specification improvement.", name="description"), 
    meta4 = meta(content="Don Brutzman and Jeff Weekley", name="creator"), 
    meta5 = meta(content="16 March 2009", name="created"), 
    meta6 = meta(content="25 October 2016", name="modified"), 
    meta7 = meta(content="Schematron rules, backed up by initialize() checks", name="TODO"), 
    meta8 = meta(content="BeyondViewpointCameraNodesWeb3D2009.pdf", name="reference"), 
    meta9 = meta(content="http://www.web3d.org/x3d/specifications/ISO-IEC-FDIS-19775-1.2-X3D-AbstractSpecification/Part01/components/navigation.html", name="reference"), 
    meta10 = meta(content="Camera nodes for Viewpoint navigation control", name="subject"), 
    meta11 = meta(content="CameraExamples.x3d", name="reference"), 
    meta12 = meta(content="http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d", name="identifier"), 
    meta13 = meta(content="http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d", name="reference"), 
    meta14 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta15 = meta(content="../license.html", name="license")), 
   Scene16 = Scene(    # =============== Camera ============== 

    ProtoDeclare17 = ProtoDeclare(appinfo="Camera node provides direct control of scene view to enable cinematic camera animation shot by shot and move by move along with still digital-photography settings for offline rendering of camera images.", name="Camera",      ProtoInterface18 = ProtoInterface(      # Viewpoint-related fields, NavigationInfo-related fields and Camera-unique fields 

      field19 = field(accessType="inputOutput", appinfo="Text description to be displayed for this Camera", name="description", type="SFString"), 
      field20 = field(accessType="inputOutput", appinfo="Camera position in local transformation frame, which is default prior to first CameraShot initialPosition getting activated", name="position", type="SFVec3f", value="0 0 10"), 
      field21 = field(accessType="inputOutput", appinfo="Camera rotation in local transformation frame, which is default prior to first CameraShot initialPosition getting activated", name="orientation", type="SFRotation", value="0 0 1 0"), 
      field22 = field(accessType="inputOutput", appinfo="pi/4", name="fieldOfView", type="SFFloat", value="0.7854"), 
      field23 = field(accessType="inputOnly", appinfo="input fraction drives interpolators", name="set_fraction", type="SFFloat"), 
      field24 = field(accessType="inputOnly", appinfo="input event binds or unbinds this Camera", name="set_bind", type="SFBool"), 
      field25 = field(accessType="outputOnly", appinfo="output event indicates when this Camera is bound", name="bindTime", type="SFTime"), 
      field26 = field(accessType="outputOnly", appinfo="output event indicates whether this Camera is bound or unbound", name="isBound", type="SFBool"), 
      field27 = field(accessType="inputOutput", appinfo="Vector distance to near clipping plane corresponds to NavigationInfo.avatarSize[0]", name="nearClipPlane", type="SFFloat", value="0.25"), 
      field28 = field(accessType="inputOutput", appinfo="Vector distance to far clipping plane corresponds to NavigationInfo.visibilityLimit", name="farClipPlane", type="SFFloat", value="0.0"), 
      field29 = field(accessType="inputOutput", appinfo="Array of CameraShot nodes which in turn contain CameraMovement nodes", name="shots", type="MFNode",        # initialization nodes (if any) go here 
), 
      field30 = field(accessType="inputOutput", appinfo="Whether camera headlight is on or off", name="headlight", type="SFBool", value="true"), 
      field31 = field(accessType="inputOutput", appinfo="Camera headlight color", name="headlightColor", type="SFColor", value="1 1 1"), 
      field32 = field(accessType="inputOutput", appinfo="Camera headlight intensity", name="headlightIntensity", type="SFFloat", value="1"), 
      field33 = field(accessType="inputOutput", appinfo="Camera filter color that modifies virtual lens capture", name="filterColor", type="SFColor", value="1 1 1"), 
      field34 = field(accessType="inputOutput", appinfo="Camera filter transparency that modifies virtual lens capture", name="filterTransparency", type="SFFloat", value="1"), 
      field35 = field(accessType="inputOutput", appinfo="upVector changes modify camera orientation (and possibly vice versa)", name="upVector", type="SFVec3f", value="0 1 0"), 
      field36 = field(accessType="inputOutput", appinfo="Focal length divided effective aperture diameter indicating width of focal plane", name="fStop", type="SFFloat", value="5.6"), 
      field37 = field(accessType="inputOutput", appinfo="Distance to focal plane of sharpest focus", name="focusDistance", type="SFFloat", value="10"), 
      field38 = field(accessType="outputOnly", appinfo="Mark start/stop with true/false output respectively useful to trigger external animations", name="isActive", type="SFBool"), 
      field39 = field(accessType="outputOnly", appinfo="Total duration of contained enabled CameraShot (and thus CameraMovement) move durations", name="totalDuration", type="SFTime"), 
      field40 = field(accessType="inputOutput", appinfo="OfflineRender node", name="offlineRender", type="SFNode",        # initialization node (if any) goes here 
), 
      field41 = field(accessType="initializeOnly", appinfo="enable console output to trace script computations and prototype progress", name="traceEnabled", type="SFBool", value="false")), 
     ProtoBody42 = ProtoBody(      Viewpoint43 = Viewpoint(DEF="CameraViewpoint",        IS44 = IS(        connect45 = connect(nodeField="description", protoField="description"), 
        connect46 = connect(nodeField="position", protoField="position"), 
        connect47 = connect(nodeField="orientation", protoField="orientation"), 
        connect48 = connect(nodeField="fieldOfView", protoField="fieldOfView"), 
        connect49 = connect(nodeField="set_bind", protoField="set_bind"), 
        connect50 = connect(nodeField="bindTime", protoField="bindTime"), 
        connect51 = connect(nodeField="isBound", protoField="isBound"))),       # NavInfo EXAMINE used since some browsers (InstantReality) try to lock view to vertical when flying to avoid disorientation 

      NavigationInfo52 = NavigationInfo(DEF="CameraNavInfo", type=["EXAMINE","FLY","ANY"],        IS53 = IS(        connect54 = connect(nodeField="set_bind", protoField="set_bind"),         # No need to bind outputs bindTime, isBound from NavigationInfo since Viewpoint outputs will suffice. TODO inform BitManagement that bindTime field is missing. 

        connect55 = connect(nodeField="headlight", protoField="headlight"), 
        connect56 = connect(nodeField="visibilityLimit", protoField="farClipPlane"))),       # this DirectionalLight replaces NavigationInfo headlight in order to add color capability 

      DirectionalLight57 = DirectionalLight(DEF="CameraDirectionalLight", Global=True,        # TODO confirm other default field values match NavigationInfo spec 

       IS58 = IS(        connect59 = connect(nodeField="on", protoField="headlight"), 
        connect60 = connect(nodeField="color", protoField="headlightColor"), 
        connect61 = connect(nodeField="intensity", protoField="headlightIntensity"))), 
      PositionInterpolator62 = PositionInterpolator(DEF="CameraPositionInterpolator", key=[0,1], keyValue=[0,0,0,0,0,0],        IS63 = IS(        connect64 = connect(nodeField="set_fraction", protoField="set_fraction"))), 
      OrientationInterpolator65 = OrientationInterpolator(DEF="CameraOrientationInterpolator", key=[0,1], keyValue=[0,1,0,0,0,1,0,0],        IS66 = IS(        connect67 = connect(nodeField="set_fraction", protoField="set_fraction"))), 
      ROUTE68 = ROUTE(fromField="value_changed", fromNode="CameraPositionInterpolator", toField="position", toNode="CameraViewpoint"), 
      ROUTE69 = ROUTE(fromField="value_changed", fromNode="CameraOrientationInterpolator", toField="orientation", toNode="CameraViewpoint"), 
      Script70 = Script(DEF="CameraScript", directOutput=True, mustEvaluate=True,        # binding is controlled externally, all camera operations proceed the same regardless of whether bound or not 

       field71 = field(accessType="inputOutput", appinfo="Text description to be displayed for this Camera", name="description", type="SFString"), 
       field72 = field(accessType="inputOutput", appinfo="Camera position in local transformation frame", name="position", type="SFVec3f"), 
       field73 = field(accessType="inputOutput", appinfo="Camera rotation in local transformation frame", name="orientation", type="SFRotation"), 
       field74 = field(accessType="inputOnly", appinfo="input fraction drives interpolators", name="set_fraction", type="SFFloat"), 
       field75 = field(accessType="inputOnly", appinfo="input event binds or unbinds this Camera", name="set_bind", type="SFBool"), 
       field76 = field(accessType="inputOutput", appinfo="pi/4", name="fieldOfView", type="SFFloat"), 
       field77 = field(accessType="inputOutput", appinfo="Vector distance to near clipping plane", name="nearClipPlane", type="SFFloat"), 
       field78 = field(accessType="inputOutput", appinfo="Vector distance to far clipping plane", name="farClipPlane", type="SFFloat"), 
       field79 = field(accessType="inputOutput", appinfo="Array of CameraShot nodes which in turn contain CameraMovement nodes", name="shots", type="MFNode",         # initialization nodes (if any) go here 
), 
       field80 = field(accessType="inputOutput", appinfo="Camera filter color that modifies virtual lens capture", name="filterColor", type="SFColor"), 
       field81 = field(accessType="inputOutput", appinfo="Camera filter transparency that modifies virtual lens capture", name="filterTransparency", type="SFFloat"), 
       field82 = field(accessType="inputOutput", appinfo="upVector changes modify camera orientation (and possibly vice versa)", name="upVector", type="SFVec3f"), 
       field83 = field(accessType="inputOutput", appinfo="Focal length divided effective aperture diameter indicating width of focal plane", name="fStop", type="SFFloat"), 
       field84 = field(accessType="inputOutput", appinfo="Distance to focal plane of sharpest focus", name="focusDistance", type="SFFloat"), 
       field85 = field(accessType="outputOnly", appinfo="Mark start/stop with true/false output respectively useful to trigger external animations", name="isActive", type="SFBool"), 
       field86 = field(accessType="outputOnly", appinfo="Total duration of contained enabled CameraShot (and thus CameraMovement) move durations", name="totalDuration", type="SFTime"), 
       field87 = field(accessType="inputOutput", appinfo="OfflineRender node", name="offlineRender", type="SFNode",         # initialization node (if any) goes here 
), 
       field88 = field(accessType="initializeOnly", appinfo="node reference to permit getting setting fields from within Script", name="ViewpointNode", type="SFNode",         Viewpoint89 = Viewpoint(USE="CameraViewpoint")), 
       field90 = field(accessType="initializeOnly", appinfo="node reference to permit getting setting fields from within Script", name="NavInfoNode", type="SFNode",         NavigationInfo91 = NavigationInfo(USE="CameraNavInfo")), 
       field92 = field(accessType="initializeOnly", appinfo="node reference to permit getting setting fields from within Script", name="CameraPI", type="SFNode",         PositionInterpolator93 = PositionInterpolator(USE="CameraPositionInterpolator")), 
       field94 = field(accessType="initializeOnly", appinfo="node reference to permit getting setting fields from within Script", name="CameraOI", type="SFNode",         OrientationInterpolator95 = OrientationInterpolator(USE="CameraOrientationInterpolator")), 
       field96 = field(accessType="inputOutput", appinfo="key array for interpolators", name="key", type="MFFloat"), 
       field97 = field(accessType="inputOutput", appinfo="keyValue array for PositionInterpolator", name="keyValuePosition", type="MFVec3f"), 
       field98 = field(accessType="inputOutput", appinfo="keyValue array for OrientationInterpolator", name="keyValueOrientation", type="MFRotation"), 
       field99 = field(accessType="inputOutput", appinfo="whether internal CameraShot and CameraMove nodes are tracking or changed via ROUTE events", name="animated", type="SFBool", value="false"), 
       field100 = field(accessType="initializeOnly", appinfo="perform checkShots() function once immediately after initialization", name="initialized", type="SFBool", value="false"), 
       field101 = field(accessType="initializeOnly", appinfo="how many CameraShot nodes are contained in shots array", name="shotCount", type="SFInt32", value="0"), 
       field102 = field(accessType="initializeOnly", appinfo="how many CameraMove nodes are contained in moves array", name="movesCount", type="SFInt32", value="0"), 
       field103 = field(accessType="initializeOnly", appinfo="how many frames were created in current loop", name="frameCount", type="SFFloat", value="0"), 
       field104 = field(accessType="initializeOnly", appinfo="holding variable", name="startTime", type="SFTime", value="0"), 
       field105 = field(accessType="initializeOnly", appinfo="holding variable", name="priorTraceTime", type="SFTime", value="0"), 
       field106 = field(accessType="initializeOnly", appinfo="enable console output to trace script computations and prototype progress", name="traceEnabled", type="SFBool"), 
       IS107 = IS(        connect108 = connect(nodeField="description", protoField="description"), 
        connect109 = connect(nodeField="position", protoField="position"), 
        connect110 = connect(nodeField="orientation", protoField="orientation"), 
        connect111 = connect(nodeField="set_fraction", protoField="set_fraction"), 
        connect112 = connect(nodeField="set_bind", protoField="set_bind"), 
        connect113 = connect(nodeField="fieldOfView", protoField="fieldOfView"), 
        connect114 = connect(nodeField="nearClipPlane", protoField="nearClipPlane"), 
        connect115 = connect(nodeField="farClipPlane", protoField="farClipPlane"), 
        connect116 = connect(nodeField="shots", protoField="shots"), 
        connect117 = connect(nodeField="filterColor", protoField="filterColor"), 
        connect118 = connect(nodeField="filterTransparency", protoField="filterTransparency"), 
        connect119 = connect(nodeField="upVector", protoField="upVector"), 
        connect120 = connect(nodeField="fStop", protoField="fStop"), 
        connect121 = connect(nodeField="focusDistance", protoField="focusDistance"), 
        connect122 = connect(nodeField="isActive", protoField="isActive"), 
        connect123 = connect(nodeField="totalDuration", protoField="totalDuration"), 
        connect124 = connect(nodeField="offlineRender", protoField="offlineRender"), 
        connect125 = connect(nodeField="traceEnabled", protoField="traceEnabled")),        sourceCode = '''\n"+
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
"''', ), 
      ROUTE126 = ROUTE(fromField="position", fromNode="CameraScript", toField="position", toNode="CameraViewpoint"), 
      ROUTE127 = ROUTE(fromField="orientation", fromNode="CameraScript", toField="orientation", toNode="CameraViewpoint"), 
      ROUTE128 = ROUTE(fromField="isActive", fromNode="CameraScript", toField="set_bind", toNode="CameraViewpoint"), 
      ROUTE129 = ROUTE(fromField="isActive", fromNode="CameraScript", toField="set_bind", toNode="CameraNavInfo"), 
      ROUTE130 = ROUTE(fromField="isActive", fromNode="CameraScript", toField="on", toNode="CameraDirectionalLight"))),     # =============== CameraShot ============== 

    ProtoDeclare131 = ProtoDeclare(appinfo="CameraShot collects a specific set of CameraMovement animations that make up an individual shot.", name="CameraShot",      ProtoInterface132 = ProtoInterface(      field133 = field(accessType="inputOutput", appinfo="Text description to be displayed for this CameraShot", name="description", type="SFString"), 
      field134 = field(accessType="inputOutput", appinfo="Whether this CameraShot can be activated", name="enabled", type="SFBool", value="true"), 
      field135 = field(accessType="inputOutput", appinfo="Set of CameraMovement nodes", name="moves", type="MFNode",        # initializing CameraMovement nodes are inserted here by scene author using ProtoInstance 
), 
      field136 = field(accessType="inputOutput", appinfo="Setup to reinitialize camera position for this shot", name="initialPosition", type="SFVec3f", value="0 0 10"), 
      field137 = field(accessType="inputOutput", appinfo="Setup to reinitialize camera rotation for this shot", name="initialOrientation", type="SFRotation", value="0 0 1 0"), 
      field138 = field(accessType="inputOutput", appinfo="Setup to reinitialize aimpoint (relative location for camera direction) for this shot", name="initialAimPoint", type="SFVec3f", value="0 0 0"), 
      field139 = field(accessType="inputOutput", appinfo="pi/4", name="initialFieldOfView", type="SFFloat", value="0.7854"), 
      field140 = field(accessType="inputOutput", appinfo="Focal length divided effective aperture diameter indicating width of focal plane", name="initialFStop", type="SFFloat", value="5.6"), 
      field141 = field(accessType="inputOutput", appinfo="Distance to focal plane of sharpest focus", name="initialFocusDistance", type="SFFloat", value="10"), 
      field142 = field(accessType="outputOnly", appinfo="Subtotal duration of contained CameraMovement move durations", name="shotDuration", type="SFTime"), 
      field143 = field(accessType="outputOnly", appinfo="Mark start/stop with true/false output respectively useful to trigger external animations", name="isActive", type="SFBool"), 
      field144 = field(accessType="initializeOnly", appinfo="enable console output to trace script computations and prototype progress", name="traceEnabled", type="SFBool", value="false")), 
     ProtoBody145 = ProtoBody(      Script146 = Script(DEF="CameraShotScript", directOutput=True, mustEvaluate=True,        field147 = field(accessType="inputOutput", appinfo="Text description to be displayed for this CameraShot", name="description", type="SFString"), 
       field148 = field(accessType="inputOutput", appinfo="Whether this CameraShot can be activated", name="enabled", type="SFBool"), 
       field149 = field(accessType="inputOutput", appinfo="Set of CameraMovement nodes", name="moves", type="MFNode",         # initialization nodes (if any) go here 
), 
       field150 = field(accessType="inputOutput", appinfo="Setup to reinitialize camera position for this shot", name="initialPosition", type="SFVec3f"), 
       field151 = field(accessType="inputOutput", appinfo="Setup to reinitialize camera rotation for this shot", name="initialOrientation", type="SFRotation"), 
       field152 = field(accessType="inputOutput", appinfo="Setup to reinitialize aimpoint (relative location for camera direction) for this shot", name="initialAimPoint", type="SFVec3f"), 
       field153 = field(accessType="inputOutput", appinfo="pi/4", name="initialFieldOfView", type="SFFloat"), 
       field154 = field(accessType="inputOutput", appinfo="Focal length divided effective aperture diameter indicating width of focal plane", name="initialFStop", type="SFFloat"), 
       field155 = field(accessType="inputOutput", appinfo="Distance to focal plane of sharpest focus", name="initialFocusDistance", type="SFFloat"), 
       field156 = field(accessType="outputOnly", appinfo="Subtotal duration of contained CameraMovement move durations", name="shotDuration", type="SFTime"), 
       field157 = field(accessType="outputOnly", appinfo="Mark start/stop with true/false output respectively useful to trigger external animations", name="isActive", type="SFBool"), 
       field158 = field(accessType="initializeOnly", appinfo="enable console output to trace script computations and prototype progress", name="traceEnabled", type="SFBool"), 
       field159 = field(accessType="inputOutput", appinfo="key array for interpolators", name="key", type="MFFloat"), 
       field160 = field(accessType="inputOutput", appinfo="keyValue array for PositionInterpolator", name="keyValuePosition", type="MFVec3f"), 
       field161 = field(accessType="inputOutput", appinfo="keyValue array for OrientationInterpolator", name="keyValueOrientation", type="MFRotation"), 
       IS162 = IS(        connect163 = connect(nodeField="description", protoField="description"), 
        connect164 = connect(nodeField="enabled", protoField="enabled"), 
        connect165 = connect(nodeField="moves", protoField="moves"), 
        connect166 = connect(nodeField="initialPosition", protoField="initialPosition"), 
        connect167 = connect(nodeField="initialOrientation", protoField="initialOrientation"), 
        connect168 = connect(nodeField="initialAimPoint", protoField="initialAimPoint"), 
        connect169 = connect(nodeField="initialFieldOfView", protoField="initialFieldOfView"), 
        connect170 = connect(nodeField="initialFStop", protoField="initialFStop"), 
        connect171 = connect(nodeField="initialFocusDistance", protoField="initialFocusDistance"), 
        connect172 = connect(nodeField="shotDuration", protoField="shotDuration"), 
        connect173 = connect(nodeField="isActive", protoField="isActive"), 
        connect174 = connect(nodeField="traceEnabled", protoField="traceEnabled")),        sourceCode = '''\n"+
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
"''', ),       # Add any ROUTEs here, going from Script to other nodes within ProtoBody 
)),     # =============== CameraMovement ============== 

    ProtoDeclare175 = ProtoDeclare(appinfo="CameraMovement node defines a single camera movement animation including goalPosition, goalOrientation, goalAimPoint and goalFieldOfView.", name="CameraMovement",      ProtoInterface176 = ProtoInterface(      field177 = field(accessType="inputOutput", appinfo="Text description to be displayed for this CameraMovement", name="description", type="SFString"), 
      field178 = field(accessType="inputOutput", appinfo="Whether this CameraMovement can be activated", name="enabled", type="SFBool", value="true"), 
      field179 = field(accessType="inputOutput", appinfo="Duration in seconds for this move", name="duration", type="SFFloat", value="0"), 
      field180 = field(accessType="inputOutput", appinfo="Goal camera position for this move", name="goalPosition", type="SFVec3f", value="0 0 10"), 
      field181 = field(accessType="inputOutput", appinfo="Goal camera rotation for this move", name="goalOrientation", type="SFRotation", value="0 0 1 0"), 
      field182 = field(accessType="inputOutput", appinfo="Whether or not camera direction is tracking towards the aimPoint", name="tracking", type="SFBool", value="false"), 
      field183 = field(accessType="inputOutput", appinfo="Goal aimPoint for this move, ignored if tracking=false", name="goalAimPoint", type="SFVec3f", value="0 0 0"), 
      field184 = field(accessType="inputOutput", appinfo="Goal fieldOfView for this move", name="goalFieldOfView", type="SFFloat", value="0.7854"), 
      field185 = field(accessType="inputOutput", appinfo="Focal length divided effective aperture diameter indicating width of focal plane", name="goalFStop", type="SFFloat", value="5.6"), 
      field186 = field(accessType="inputOutput", appinfo="Distance to focal plane of sharpest focus", name="goalFocusDistance", type="SFFloat", value="10"), 
      field187 = field(accessType="outputOnly", appinfo="Mark start/stop with true/false output respectively useful to trigger external animations", name="isActive", type="SFBool"), 
      field188 = field(accessType="initializeOnly", appinfo="enable console output to trace script computations and prototype progress", name="traceEnabled", type="SFBool", value="false")), 
     ProtoBody189 = ProtoBody(      # First node determines node type of this prototype 
      # Subsequent nodes do not render, but still must be a valid X3D subgraph 
      # Script holds CameraMovement initialization values for query by parent CameraShot, and also permits changing values via events 

      Script190 = Script(DEF="CameraMovementScript", directOutput=True, mustEvaluate=True,        field191 = field(accessType="inputOutput", appinfo="Text description to be displayed for this CameraMovement", name="description", type="SFString"), 
       field192 = field(accessType="inputOutput", appinfo="Whether this CameraMovement can be activated", name="enabled", type="SFBool"), 
       field193 = field(accessType="inputOutput", appinfo="Duration in seconds for this move", name="duration", type="SFFloat"), 
       field194 = field(accessType="inputOutput", appinfo="Goal camera position for this move", name="goalPosition", type="SFVec3f"), 
       field195 = field(accessType="inputOutput", appinfo="Goal camera rotation for this move", name="goalOrientation", type="SFRotation"), 
       field196 = field(accessType="inputOutput", appinfo="Whether or not camera direction is tracking towards the aimPoint", name="tracking", type="SFBool"), 
       field197 = field(accessType="inputOutput", appinfo="Goal aimPoint for this move, ignored if tracking=false", name="goalAimPoint", type="SFVec3f"), 
       field198 = field(accessType="inputOutput", appinfo="Goal fieldOfView for this move", name="goalFieldOfView", type="SFFloat"), 
       field199 = field(accessType="inputOutput", appinfo="Focal length divided effective aperture diameter indicating width of focal plane", name="goalFStop", type="SFFloat"), 
       field200 = field(accessType="inputOutput", appinfo="Distance to focal plane of sharpest focus", name="goalFocusDistance", type="SFFloat"), 
       field201 = field(accessType="outputOnly", appinfo="Mark start/stop with true/false output respectively useful to trigger external animations", name="isActive", type="SFBool"), 
       field202 = field(accessType="initializeOnly", appinfo="enable console output to trace script computations and prototype progress", name="traceEnabled", type="SFBool"), 
       IS203 = IS(        connect204 = connect(nodeField="description", protoField="description"), 
        connect205 = connect(nodeField="enabled", protoField="enabled"), 
        connect206 = connect(nodeField="duration", protoField="duration"), 
        connect207 = connect(nodeField="goalPosition", protoField="goalPosition"), 
        connect208 = connect(nodeField="goalOrientation", protoField="goalOrientation"), 
        connect209 = connect(nodeField="tracking", protoField="tracking"), 
        connect210 = connect(nodeField="goalAimPoint", protoField="goalAimPoint"), 
        connect211 = connect(nodeField="goalFieldOfView", protoField="goalFieldOfView"), 
        connect212 = connect(nodeField="goalFStop", protoField="goalFStop"), 
        connect213 = connect(nodeField="goalFocusDistance", protoField="goalFocusDistance"), 
        connect214 = connect(nodeField="isActive", protoField="isActive"), 
        connect215 = connect(nodeField="traceEnabled", protoField="traceEnabled")),        sourceCode = '''\n"+
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
"''', ),       # Add any ROUTEs here, going from Script to other nodes within ProtoBody 
)),     # =============== OfflineRender ============== 

    ProtoDeclare216 = ProtoDeclare(appinfo="OfflineRender defines a parameters for offline rendering of Camera animation output to a movie file (or possibly a still shot).", name="OfflineRender",      ProtoInterface217 = ProtoInterface(      # TODO non-photorealistic rendering (NPR) parameters 

      field218 = field(accessType="inputOutput", appinfo="Text description to be displayed for this OfflineRender", name="description", type="SFString"), 
      field219 = field(accessType="inputOutput", appinfo="Whether this OfflineRender can be activated", name="enabled", type="SFBool", value="true"), 
      field220 = field(accessType="inputOutput", appinfo="Frames per second recorded for this rendering", name="frameRate", type="SFFloat", value="30"), 
      field221 = field(accessType="inputOutput", appinfo="Size of frame in number of pixels width and height", name="frameSize", type="SFVec2f", value="640 480"), 
      field222 = field(accessType="inputOutput", appinfo="Relative dimensions of pixel height/width typically 1.33 or 1", name="pixelAspectRatio", type="SFFloat", value="1.33"), 
      field223 = field(accessType="inputOnly", appinfo="Begin render operation", name="set_startTime", type="SFTime"), 
      field224 = field(accessType="outputOnly", appinfo="Progress performing render operation (0..1)", name="progress", type="SFFloat"), 
      field225 = field(accessType="outputOnly", appinfo="Render operation complete", name="renderCompleteTime", type="SFTime"), 
      field226 = field(accessType="initializeOnly", appinfo="Format of rendered output movie (mpeg mp4 etc.), use first supported format", name="movieFormat", type="MFString", value="\"mpeg\""), 
      field227 = field(accessType="initializeOnly", appinfo="Format of rendered output images (png jpeg gif tiff etc.) use first supported format", name="imageFormat", type="MFString", value="\"png\""), 
      field228 = field(accessType="initializeOnly", appinfo="enable console output to trace script computations and prototype progress", name="traceEnabled", type="SFBool", value="false")), 
     ProtoBody229 = ProtoBody(      # First node determines node type of this prototype 
      # Subsequent nodes do not render, but still must be a valid X3D subgraph 

      Script230 = Script(DEF="OfflineRenderScript", mustEvaluate=True,        field231 = field(accessType="inputOutput", appinfo="Text description to be displayed for this OfflineRender", name="description", type="SFString"), 
       field232 = field(accessType="inputOutput", appinfo="Whether this OfflineRender can be activated", name="enabled", type="SFBool"), 
       field233 = field(accessType="inputOutput", appinfo="Frames per second recorded for this rendering", name="frameRate", type="SFFloat"), 
       field234 = field(accessType="inputOutput", appinfo="Size of frame in number of pixels width and height", name="frameSize", type="SFVec2f"), 
       field235 = field(accessType="inputOutput", appinfo="Relative dimensions of pixel height/width typically 1.33 or 1", name="pixelAspectRatio", type="SFFloat"), 
       field236 = field(accessType="inputOnly", appinfo="Begin render operation", name="set_startTime", type="SFTime"), 
       field237 = field(accessType="outputOnly", appinfo="Progress performing render operation (0..1)", name="progress", type="SFFloat"), 
       field238 = field(accessType="outputOnly", appinfo="Render operation complete", name="renderCompleteTime", type="SFTime"), 
       field239 = field(accessType="initializeOnly", appinfo="Format of rendered output movie (mpeg mp4 etc.)", name="movieFormat", type="MFString"), 
       field240 = field(accessType="initializeOnly", appinfo="Format of rendered output images (png jpeg gif tiff etc.)", name="imageFormat", type="MFString"), 
       field241 = field(accessType="initializeOnly", appinfo="enable console output to trace script computations and prototype progress", name="traceEnabled", type="SFBool"), 
       IS242 = IS(        connect243 = connect(nodeField="description", protoField="description"), 
        connect244 = connect(nodeField="enabled", protoField="enabled"), 
        connect245 = connect(nodeField="frameRate", protoField="frameRate"), 
        connect246 = connect(nodeField="frameSize", protoField="frameSize"), 
        connect247 = connect(nodeField="pixelAspectRatio", protoField="pixelAspectRatio"), 
        connect248 = connect(nodeField="set_startTime", protoField="set_startTime"), 
        connect249 = connect(nodeField="progress", protoField="progress"), 
        connect250 = connect(nodeField="renderCompleteTime", protoField="renderCompleteTime"), 
        connect251 = connect(nodeField="movieFormat", protoField="movieFormat"), 
        connect252 = connect(nodeField="imageFormat", protoField="imageFormat"), 
        connect253 = connect(nodeField="traceEnabled", protoField="traceEnabled")),        sourceCode = '''\n"+
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
"''', ),       # Add any ROUTEs here, going from Script to other nodes within ProtoBody 
)),     # =============== Launch Prototype Example ============== 

    Background254 = Background(skyColor=[0.282353,0.380392,0.470588]), 
    Anchor255 = Anchor(description="launch CameraExample scene", url=["CameraExamples.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d","CameraExamples.wrl","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.wrl"],      Transform256 = Transform(      Shape257 = Shape(       Text258 = Text(string=["CameraPrototypes.x3d","defines multiple prototype nodes","","Click on this text to see","CameraExamples.x3d scene"],         FontStyle259 = FontStyle(justify=["MIDDLE","MIDDLE"])), 
       Appearance260 = Appearance(        Material261 = Material(diffuseColor=[1,1,0.2])))))))
