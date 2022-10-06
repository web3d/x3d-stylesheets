from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.2"

head1 = head()

meta2 = meta()
meta2.content = "CameraPrototypes.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Camera, CameraShot and CameraMovement prototypes that demonstrate storyboard capabilities and precise camera operation. This is a developmental effort for potential X3D Specification improvement."
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Don Brutzman and Jeff Weekley"
meta4.name = "creator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "16 March 2009"
meta5.name = "created"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "25 October 2016"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "Schematron rules, backed up by initialize() checks"
meta7.name = "TODO"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "BeyondViewpointCameraNodesWeb3D2009.pdf"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "http://www.web3d.org/x3d/specifications/ISO-IEC-FDIS-19775-1.2-X3D-AbstractSpecification/Part01/components/navigation.html"
meta9.name = "reference"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "Camera nodes for Viewpoint navigation control"
meta10.name = "subject"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "CameraExamples.x3d"
meta11.name = "reference"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d"
meta12.name = "identifier"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d"
meta13.name = "reference"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta14.name = "generator"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "../license.html"
meta15.name = "license"
head1.addMeta([meta15])
X3D0.head = head1

Scene16 = Scene()
# =============== Camera ============== 

ProtoDeclare17 = ProtoDeclare()
ProtoDeclare17.appinfo = "Camera node provides direct control of scene view to enable cinematic camera animation shot by shot and move by move along with still digital-photography settings for offline rendering of camera images."
ProtoDeclare17.name = "Camera"

ProtoInterface18 = ProtoInterface()
# Viewpoint-related fields, NavigationInfo-related fields and Camera-unique fields 

field19 = field()
field19.accessType = "inputOutput"
field19.appinfo = "Text description to be displayed for this Camera"
field19.name = "description"
field19.type = "SFString"
ProtoInterface18.addField([field19])

field20 = field()
field20.accessType = "inputOutput"
field20.appinfo = "Camera position in local transformation frame, which is default prior to first CameraShot initialPosition getting activated"
field20.name = "position"
field20.type = "SFVec3f"
field20.value = "0 0 10"
ProtoInterface18.addField([field20])

field21 = field()
field21.accessType = "inputOutput"
field21.appinfo = "Camera rotation in local transformation frame, which is default prior to first CameraShot initialPosition getting activated"
field21.name = "orientation"
field21.type = "SFRotation"
field21.value = "0 0 1 0"
ProtoInterface18.addField([field21])

field22 = field()
field22.accessType = "inputOutput"
field22.appinfo = "pi/4"
field22.name = "fieldOfView"
field22.type = "SFFloat"
field22.value = "0.7854"
ProtoInterface18.addField([field22])

field23 = field()
field23.accessType = "inputOnly"
field23.appinfo = "input fraction drives interpolators"
field23.name = "set_fraction"
field23.type = "SFFloat"
ProtoInterface18.addField([field23])

field24 = field()
field24.accessType = "inputOnly"
field24.appinfo = "input event binds or unbinds this Camera"
field24.name = "set_bind"
field24.type = "SFBool"
ProtoInterface18.addField([field24])

field25 = field()
field25.accessType = "outputOnly"
field25.appinfo = "output event indicates when this Camera is bound"
field25.name = "bindTime"
field25.type = "SFTime"
ProtoInterface18.addField([field25])

field26 = field()
field26.accessType = "outputOnly"
field26.appinfo = "output event indicates whether this Camera is bound or unbound"
field26.name = "isBound"
field26.type = "SFBool"
ProtoInterface18.addField([field26])

field27 = field()
field27.accessType = "inputOutput"
field27.appinfo = "Vector distance to near clipping plane corresponds to NavigationInfo.avatarSize[0]"
field27.name = "nearClipPlane"
field27.type = "SFFloat"
field27.value = "0.25"
ProtoInterface18.addField([field27])

field28 = field()
field28.accessType = "inputOutput"
field28.appinfo = "Vector distance to far clipping plane corresponds to NavigationInfo.visibilityLimit"
field28.name = "farClipPlane"
field28.type = "SFFloat"
field28.value = "0.0"
ProtoInterface18.addField([field28])

field29 = field()
field29.accessType = "inputOutput"
field29.appinfo = "Array of CameraShot nodes which in turn contain CameraMovement nodes"
field29.name = "shots"
field29.type = "MFNode"
# initialization nodes (if any) go here 
ProtoInterface18.addField([field29])

field30 = field()
field30.accessType = "inputOutput"
field30.appinfo = "Whether camera headlight is on or off"
field30.name = "headlight"
field30.type = "SFBool"
field30.value = "true"
ProtoInterface18.addField([field30])

field31 = field()
field31.accessType = "inputOutput"
field31.appinfo = "Camera headlight color"
field31.name = "headlightColor"
field31.type = "SFColor"
field31.value = "1 1 1"
ProtoInterface18.addField([field31])

field32 = field()
field32.accessType = "inputOutput"
field32.appinfo = "Camera headlight intensity"
field32.name = "headlightIntensity"
field32.type = "SFFloat"
field32.value = "1"
ProtoInterface18.addField([field32])

field33 = field()
field33.accessType = "inputOutput"
field33.appinfo = "Camera filter color that modifies virtual lens capture"
field33.name = "filterColor"
field33.type = "SFColor"
field33.value = "1 1 1"
ProtoInterface18.addField([field33])

field34 = field()
field34.accessType = "inputOutput"
field34.appinfo = "Camera filter transparency that modifies virtual lens capture"
field34.name = "filterTransparency"
field34.type = "SFFloat"
field34.value = "1"
ProtoInterface18.addField([field34])

field35 = field()
field35.accessType = "inputOutput"
field35.appinfo = "upVector changes modify camera orientation (and possibly vice versa)"
field35.name = "upVector"
field35.type = "SFVec3f"
field35.value = "0 1 0"
ProtoInterface18.addField([field35])

field36 = field()
field36.accessType = "inputOutput"
field36.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field36.name = "fStop"
field36.type = "SFFloat"
field36.value = "5.6"
ProtoInterface18.addField([field36])

field37 = field()
field37.accessType = "inputOutput"
field37.appinfo = "Distance to focal plane of sharpest focus"
field37.name = "focusDistance"
field37.type = "SFFloat"
field37.value = "10"
ProtoInterface18.addField([field37])

field38 = field()
field38.accessType = "outputOnly"
field38.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field38.name = "isActive"
field38.type = "SFBool"
ProtoInterface18.addField([field38])

field39 = field()
field39.accessType = "outputOnly"
field39.appinfo = "Total duration of contained enabled CameraShot (and thus CameraMovement) move durations"
field39.name = "totalDuration"
field39.type = "SFTime"
ProtoInterface18.addField([field39])

field40 = field()
field40.accessType = "inputOutput"
field40.appinfo = "OfflineRender node"
field40.name = "offlineRender"
field40.type = "SFNode"
# initialization node (if any) goes here 
ProtoInterface18.addField([field40])

field41 = field()
field41.accessType = "initializeOnly"
field41.appinfo = "enable console output to trace script computations and prototype progress"
field41.name = "traceEnabled"
field41.type = "SFBool"
field41.value = "false"
ProtoInterface18.addField([field41])
ProtoDeclare17.protoInterface = ProtoInterface18

ProtoBody42 = ProtoBody()

Viewpoint43 = Viewpoint()
Viewpoint43.DEF = "CameraViewpoint"

IS44 = IS()

connect45 = connect()
connect45.nodeField = "description"
connect45.protoField = "description"
IS44.addConnect([connect45])

connect46 = connect()
connect46.nodeField = "position"
connect46.protoField = "position"
IS44.addConnect([connect46])

connect47 = connect()
connect47.nodeField = "orientation"
connect47.protoField = "orientation"
IS44.addConnect([connect47])

connect48 = connect()
connect48.nodeField = "fieldOfView"
connect48.protoField = "fieldOfView"
IS44.addConnect([connect48])

connect49 = connect()
connect49.nodeField = "set_bind"
connect49.protoField = "set_bind"
IS44.addConnect([connect49])

connect50 = connect()
connect50.nodeField = "bindTime"
connect50.protoField = "bindTime"
IS44.addConnect([connect50])

connect51 = connect()
connect51.nodeField = "isBound"
connect51.protoField = "isBound"
IS44.addConnect([connect51])
Viewpoint43.IS = IS44
ProtoBody42.addChildren([Viewpoint43])
# NavInfo EXAMINE used since some browsers (InstantReality) try to lock view to vertical when flying to avoid disorientation 

NavigationInfo52 = NavigationInfo()
NavigationInfo52.DEF = "CameraNavInfo"
NavigationInfo52.type = ["EXAMINE","FLY","ANY"]

IS53 = IS()

connect54 = connect()
connect54.nodeField = "set_bind"
connect54.protoField = "set_bind"
IS53.addConnect([connect54])
# No need to bind outputs bindTime, isBound from NavigationInfo since Viewpoint outputs will suffice. TODO inform BitManagement that bindTime field is missing. 

connect55 = connect()
connect55.nodeField = "headlight"
connect55.protoField = "headlight"
IS53.addConnect([connect55])

connect56 = connect()
connect56.nodeField = "visibilityLimit"
connect56.protoField = "farClipPlane"
IS53.addConnect([connect56])
NavigationInfo52.IS = IS53
ProtoBody42.addChildren([NavigationInfo52])
# this DirectionalLight replaces NavigationInfo headlight in order to add color capability 

DirectionalLight57 = DirectionalLight()
DirectionalLight57.DEF = "CameraDirectionalLight"
DirectionalLight57.global_ = True
# TODO confirm other default field values match NavigationInfo spec 

IS58 = IS()

connect59 = connect()
connect59.nodeField = "on"
connect59.protoField = "headlight"
IS58.addConnect([connect59])

connect60 = connect()
connect60.nodeField = "color"
connect60.protoField = "headlightColor"
IS58.addConnect([connect60])

connect61 = connect()
connect61.nodeField = "intensity"
connect61.protoField = "headlightIntensity"
IS58.addConnect([connect61])
DirectionalLight57.IS = IS58
ProtoBody42.addChildren([DirectionalLight57])

PositionInterpolator62 = PositionInterpolator()
PositionInterpolator62.DEF = "CameraPositionInterpolator"
PositionInterpolator62.key = [0,1]
PositionInterpolator62.keyValue = [0,0,0,0,0,0]

IS63 = IS()

connect64 = connect()
connect64.nodeField = "set_fraction"
connect64.protoField = "set_fraction"
IS63.addConnect([connect64])
PositionInterpolator62.IS = IS63
ProtoBody42.addChildren([PositionInterpolator62])

OrientationInterpolator65 = OrientationInterpolator()
OrientationInterpolator65.DEF = "CameraOrientationInterpolator"
OrientationInterpolator65.key = [0,1]
OrientationInterpolator65.keyValue = [0,1,0,0,0,1,0,0]

IS66 = IS()

connect67 = connect()
connect67.nodeField = "set_fraction"
connect67.protoField = "set_fraction"
IS66.addConnect([connect67])
OrientationInterpolator65.IS = IS66
ProtoBody42.addChildren([OrientationInterpolator65])

ROUTE68 = ROUTE()
ROUTE68.fromField = "value_changed"
ROUTE68.fromNode = "CameraPositionInterpolator"
ROUTE68.toField = "position"
ROUTE68.toNode = "CameraViewpoint"
ProtoBody42.addChildren([ROUTE68])

ROUTE69 = ROUTE()
ROUTE69.fromField = "value_changed"
ROUTE69.fromNode = "CameraOrientationInterpolator"
ROUTE69.toField = "orientation"
ROUTE69.toNode = "CameraViewpoint"
ProtoBody42.addChildren([ROUTE69])

Script70 = Script(directOutput = True, mustEvaluate = True)
Script70.DEF = "CameraScript"
# binding is controlled externally, all camera operations proceed the same regardless of whether bound or not 

field71 = field()
field71.accessType = "inputOutput"
field71.appinfo = "Text description to be displayed for this Camera"
field71.name = "description"
field71.type = "SFString"
Script70.addField([field71])

field72 = field()
field72.accessType = "inputOutput"
field72.appinfo = "Camera position in local transformation frame"
field72.name = "position"
field72.type = "SFVec3f"
Script70.addField([field72])

field73 = field()
field73.accessType = "inputOutput"
field73.appinfo = "Camera rotation in local transformation frame"
field73.name = "orientation"
field73.type = "SFRotation"
Script70.addField([field73])

field74 = field()
field74.accessType = "inputOnly"
field74.appinfo = "input fraction drives interpolators"
field74.name = "set_fraction"
field74.type = "SFFloat"
Script70.addField([field74])

field75 = field()
field75.accessType = "inputOnly"
field75.appinfo = "input event binds or unbinds this Camera"
field75.name = "set_bind"
field75.type = "SFBool"
Script70.addField([field75])

field76 = field()
field76.accessType = "inputOutput"
field76.appinfo = "pi/4"
field76.name = "fieldOfView"
field76.type = "SFFloat"
Script70.addField([field76])

field77 = field()
field77.accessType = "inputOutput"
field77.appinfo = "Vector distance to near clipping plane"
field77.name = "nearClipPlane"
field77.type = "SFFloat"
Script70.addField([field77])

field78 = field()
field78.accessType = "inputOutput"
field78.appinfo = "Vector distance to far clipping plane"
field78.name = "farClipPlane"
field78.type = "SFFloat"
Script70.addField([field78])

field79 = field()
field79.accessType = "inputOutput"
field79.appinfo = "Array of CameraShot nodes which in turn contain CameraMovement nodes"
field79.name = "shots"
field79.type = "MFNode"
# initialization nodes (if any) go here 
Script70.addField([field79])

field80 = field()
field80.accessType = "inputOutput"
field80.appinfo = "Camera filter color that modifies virtual lens capture"
field80.name = "filterColor"
field80.type = "SFColor"
Script70.addField([field80])

field81 = field()
field81.accessType = "inputOutput"
field81.appinfo = "Camera filter transparency that modifies virtual lens capture"
field81.name = "filterTransparency"
field81.type = "SFFloat"
Script70.addField([field81])

field82 = field()
field82.accessType = "inputOutput"
field82.appinfo = "upVector changes modify camera orientation (and possibly vice versa)"
field82.name = "upVector"
field82.type = "SFVec3f"
Script70.addField([field82])

field83 = field()
field83.accessType = "inputOutput"
field83.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field83.name = "fStop"
field83.type = "SFFloat"
Script70.addField([field83])

field84 = field()
field84.accessType = "inputOutput"
field84.appinfo = "Distance to focal plane of sharpest focus"
field84.name = "focusDistance"
field84.type = "SFFloat"
Script70.addField([field84])

field85 = field()
field85.accessType = "outputOnly"
field85.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field85.name = "isActive"
field85.type = "SFBool"
Script70.addField([field85])

field86 = field()
field86.accessType = "outputOnly"
field86.appinfo = "Total duration of contained enabled CameraShot (and thus CameraMovement) move durations"
field86.name = "totalDuration"
field86.type = "SFTime"
Script70.addField([field86])

field87 = field()
field87.accessType = "inputOutput"
field87.appinfo = "OfflineRender node"
field87.name = "offlineRender"
field87.type = "SFNode"
# initialization node (if any) goes here 
Script70.addField([field87])

field88 = field()
field88.accessType = "initializeOnly"
field88.appinfo = "node reference to permit getting setting fields from within Script"
field88.name = "ViewpointNode"
field88.type = "SFNode"

Viewpoint89 = Viewpoint()
Viewpoint89.USE = "CameraViewpoint"
field88.addChildren([Viewpoint89])
Script70.addField([field88])

field90 = field()
field90.accessType = "initializeOnly"
field90.appinfo = "node reference to permit getting setting fields from within Script"
field90.name = "NavInfoNode"
field90.type = "SFNode"

NavigationInfo91 = NavigationInfo()
NavigationInfo91.USE = "CameraNavInfo"
field90.addChildren([NavigationInfo91])
Script70.addField([field90])

field92 = field()
field92.accessType = "initializeOnly"
field92.appinfo = "node reference to permit getting setting fields from within Script"
field92.name = "CameraPI"
field92.type = "SFNode"

PositionInterpolator93 = PositionInterpolator()
PositionInterpolator93.USE = "CameraPositionInterpolator"
field92.addChildren([PositionInterpolator93])
Script70.addField([field92])

field94 = field()
field94.accessType = "initializeOnly"
field94.appinfo = "node reference to permit getting setting fields from within Script"
field94.name = "CameraOI"
field94.type = "SFNode"

OrientationInterpolator95 = OrientationInterpolator()
OrientationInterpolator95.USE = "CameraOrientationInterpolator"
field94.addChildren([OrientationInterpolator95])
Script70.addField([field94])

field96 = field()
field96.accessType = "inputOutput"
field96.appinfo = "key array for interpolators"
field96.name = "key"
field96.type = "MFFloat"
Script70.addField([field96])

field97 = field()
field97.accessType = "inputOutput"
field97.appinfo = "keyValue array for PositionInterpolator"
field97.name = "keyValuePosition"
field97.type = "MFVec3f"
Script70.addField([field97])

field98 = field()
field98.accessType = "inputOutput"
field98.appinfo = "keyValue array for OrientationInterpolator"
field98.name = "keyValueOrientation"
field98.type = "MFRotation"
Script70.addField([field98])

field99 = field()
field99.accessType = "inputOutput"
field99.appinfo = "whether internal CameraShot and CameraMove nodes are tracking or changed via ROUTE events"
field99.name = "animated"
field99.type = "SFBool"
field99.value = "false"
Script70.addField([field99])

field100 = field()
field100.accessType = "initializeOnly"
field100.appinfo = "perform checkShots() function once immediately after initialization"
field100.name = "initialized"
field100.type = "SFBool"
field100.value = "false"
Script70.addField([field100])

field101 = field()
field101.accessType = "initializeOnly"
field101.appinfo = "how many CameraShot nodes are contained in shots array"
field101.name = "shotCount"
field101.type = "SFInt32"
field101.value = "0"
Script70.addField([field101])

field102 = field()
field102.accessType = "initializeOnly"
field102.appinfo = "how many CameraMove nodes are contained in moves array"
field102.name = "movesCount"
field102.type = "SFInt32"
field102.value = "0"
Script70.addField([field102])

field103 = field()
field103.accessType = "initializeOnly"
field103.appinfo = "how many frames were created in current loop"
field103.name = "frameCount"
field103.type = "SFFloat"
field103.value = "0"
Script70.addField([field103])

field104 = field()
field104.accessType = "initializeOnly"
field104.appinfo = "holding variable"
field104.name = "startTime"
field104.type = "SFTime"
field104.value = "0"
Script70.addField([field104])

field105 = field()
field105.accessType = "initializeOnly"
field105.appinfo = "holding variable"
field105.name = "priorTraceTime"
field105.type = "SFTime"
field105.value = "0"
Script70.addField([field105])

field106 = field()
field106.accessType = "initializeOnly"
field106.appinfo = "enable console output to trace script computations and prototype progress"
field106.name = "traceEnabled"
field106.type = "SFBool"
Script70.addField([field106])

IS107 = IS()

connect108 = connect()
connect108.nodeField = "description"
connect108.protoField = "description"
IS107.addConnect([connect108])

connect109 = connect()
connect109.nodeField = "position"
connect109.protoField = "position"
IS107.addConnect([connect109])

connect110 = connect()
connect110.nodeField = "orientation"
connect110.protoField = "orientation"
IS107.addConnect([connect110])

connect111 = connect()
connect111.nodeField = "set_fraction"
connect111.protoField = "set_fraction"
IS107.addConnect([connect111])

connect112 = connect()
connect112.nodeField = "set_bind"
connect112.protoField = "set_bind"
IS107.addConnect([connect112])

connect113 = connect()
connect113.nodeField = "fieldOfView"
connect113.protoField = "fieldOfView"
IS107.addConnect([connect113])

connect114 = connect()
connect114.nodeField = "nearClipPlane"
connect114.protoField = "nearClipPlane"
IS107.addConnect([connect114])

connect115 = connect()
connect115.nodeField = "farClipPlane"
connect115.protoField = "farClipPlane"
IS107.addConnect([connect115])

connect116 = connect()
connect116.nodeField = "shots"
connect116.protoField = "shots"
IS107.addConnect([connect116])

connect117 = connect()
connect117.nodeField = "filterColor"
connect117.protoField = "filterColor"
IS107.addConnect([connect117])

connect118 = connect()
connect118.nodeField = "filterTransparency"
connect118.protoField = "filterTransparency"
IS107.addConnect([connect118])

connect119 = connect()
connect119.nodeField = "upVector"
connect119.protoField = "upVector"
IS107.addConnect([connect119])

connect120 = connect()
connect120.nodeField = "fStop"
connect120.protoField = "fStop"
IS107.addConnect([connect120])

connect121 = connect()
connect121.nodeField = "focusDistance"
connect121.protoField = "focusDistance"
IS107.addConnect([connect121])

connect122 = connect()
connect122.nodeField = "isActive"
connect122.protoField = "isActive"
IS107.addConnect([connect122])

connect123 = connect()
connect123.nodeField = "totalDuration"
connect123.protoField = "totalDuration"
IS107.addConnect([connect123])

connect124 = connect()
connect124.nodeField = "offlineRender"
connect124.protoField = "offlineRender"
IS107.addConnect([connect124])

connect125 = connect()
connect125.nodeField = "traceEnabled"
connect125.protoField = "traceEnabled"
IS107.addConnect([connect125])
Script70.IS = IS107

Script70.setSourceCode('''\n"+
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
ProtoBody42.addChildren([Script70])

ROUTE126 = ROUTE()
ROUTE126.fromField = "position"
ROUTE126.fromNode = "CameraScript"
ROUTE126.toField = "position"
ROUTE126.toNode = "CameraViewpoint"
ProtoBody42.addChildren([ROUTE126])

ROUTE127 = ROUTE()
ROUTE127.fromField = "orientation"
ROUTE127.fromNode = "CameraScript"
ROUTE127.toField = "orientation"
ROUTE127.toNode = "CameraViewpoint"
ProtoBody42.addChildren([ROUTE127])

ROUTE128 = ROUTE()
ROUTE128.fromField = "isActive"
ROUTE128.fromNode = "CameraScript"
ROUTE128.toField = "set_bind"
ROUTE128.toNode = "CameraViewpoint"
ProtoBody42.addChildren([ROUTE128])

ROUTE129 = ROUTE()
ROUTE129.fromField = "isActive"
ROUTE129.fromNode = "CameraScript"
ROUTE129.toField = "set_bind"
ROUTE129.toNode = "CameraNavInfo"
ProtoBody42.addChildren([ROUTE129])

ROUTE130 = ROUTE()
ROUTE130.fromField = "isActive"
ROUTE130.fromNode = "CameraScript"
ROUTE130.toField = "on"
ROUTE130.toNode = "CameraDirectionalLight"
ProtoBody42.addChildren([ROUTE130])
ProtoDeclare17.protoBody = ProtoBody42
Scene16.addChildren([ProtoDeclare17])
# =============== CameraShot ============== 

ProtoDeclare131 = ProtoDeclare()
ProtoDeclare131.appinfo = "CameraShot collects a specific set of CameraMovement animations that make up an individual shot."
ProtoDeclare131.name = "CameraShot"

ProtoInterface132 = ProtoInterface()

field133 = field()
field133.accessType = "inputOutput"
field133.appinfo = "Text description to be displayed for this CameraShot"
field133.name = "description"
field133.type = "SFString"
ProtoInterface132.addField([field133])

field134 = field()
field134.accessType = "inputOutput"
field134.appinfo = "Whether this CameraShot can be activated"
field134.name = "enabled"
field134.type = "SFBool"
field134.value = "true"
ProtoInterface132.addField([field134])

field135 = field()
field135.accessType = "inputOutput"
field135.appinfo = "Set of CameraMovement nodes"
field135.name = "moves"
field135.type = "MFNode"
# initializing CameraMovement nodes are inserted here by scene author using ProtoInstance 
ProtoInterface132.addField([field135])

field136 = field()
field136.accessType = "inputOutput"
field136.appinfo = "Setup to reinitialize camera position for this shot"
field136.name = "initialPosition"
field136.type = "SFVec3f"
field136.value = "0 0 10"
ProtoInterface132.addField([field136])

field137 = field()
field137.accessType = "inputOutput"
field137.appinfo = "Setup to reinitialize camera rotation for this shot"
field137.name = "initialOrientation"
field137.type = "SFRotation"
field137.value = "0 0 1 0"
ProtoInterface132.addField([field137])

field138 = field()
field138.accessType = "inputOutput"
field138.appinfo = "Setup to reinitialize aimpoint (relative location for camera direction) for this shot"
field138.name = "initialAimPoint"
field138.type = "SFVec3f"
field138.value = "0 0 0"
ProtoInterface132.addField([field138])

field139 = field()
field139.accessType = "inputOutput"
field139.appinfo = "pi/4"
field139.name = "initialFieldOfView"
field139.type = "SFFloat"
field139.value = "0.7854"
ProtoInterface132.addField([field139])

field140 = field()
field140.accessType = "inputOutput"
field140.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field140.name = "initialFStop"
field140.type = "SFFloat"
field140.value = "5.6"
ProtoInterface132.addField([field140])

field141 = field()
field141.accessType = "inputOutput"
field141.appinfo = "Distance to focal plane of sharpest focus"
field141.name = "initialFocusDistance"
field141.type = "SFFloat"
field141.value = "10"
ProtoInterface132.addField([field141])

field142 = field()
field142.accessType = "outputOnly"
field142.appinfo = "Subtotal duration of contained CameraMovement move durations"
field142.name = "shotDuration"
field142.type = "SFTime"
ProtoInterface132.addField([field142])

field143 = field()
field143.accessType = "outputOnly"
field143.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field143.name = "isActive"
field143.type = "SFBool"
ProtoInterface132.addField([field143])

field144 = field()
field144.accessType = "initializeOnly"
field144.appinfo = "enable console output to trace script computations and prototype progress"
field144.name = "traceEnabled"
field144.type = "SFBool"
field144.value = "false"
ProtoInterface132.addField([field144])
ProtoDeclare131.protoInterface = ProtoInterface132

ProtoBody145 = ProtoBody()

Script146 = Script(directOutput = True, mustEvaluate = True)
Script146.DEF = "CameraShotScript"

field147 = field()
field147.accessType = "inputOutput"
field147.appinfo = "Text description to be displayed for this CameraShot"
field147.name = "description"
field147.type = "SFString"
Script146.addField([field147])

field148 = field()
field148.accessType = "inputOutput"
field148.appinfo = "Whether this CameraShot can be activated"
field148.name = "enabled"
field148.type = "SFBool"
Script146.addField([field148])

field149 = field()
field149.accessType = "inputOutput"
field149.appinfo = "Set of CameraMovement nodes"
field149.name = "moves"
field149.type = "MFNode"
# initialization nodes (if any) go here 
Script146.addField([field149])

field150 = field()
field150.accessType = "inputOutput"
field150.appinfo = "Setup to reinitialize camera position for this shot"
field150.name = "initialPosition"
field150.type = "SFVec3f"
Script146.addField([field150])

field151 = field()
field151.accessType = "inputOutput"
field151.appinfo = "Setup to reinitialize camera rotation for this shot"
field151.name = "initialOrientation"
field151.type = "SFRotation"
Script146.addField([field151])

field152 = field()
field152.accessType = "inputOutput"
field152.appinfo = "Setup to reinitialize aimpoint (relative location for camera direction) for this shot"
field152.name = "initialAimPoint"
field152.type = "SFVec3f"
Script146.addField([field152])

field153 = field()
field153.accessType = "inputOutput"
field153.appinfo = "pi/4"
field153.name = "initialFieldOfView"
field153.type = "SFFloat"
Script146.addField([field153])

field154 = field()
field154.accessType = "inputOutput"
field154.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field154.name = "initialFStop"
field154.type = "SFFloat"
Script146.addField([field154])

field155 = field()
field155.accessType = "inputOutput"
field155.appinfo = "Distance to focal plane of sharpest focus"
field155.name = "initialFocusDistance"
field155.type = "SFFloat"
Script146.addField([field155])

field156 = field()
field156.accessType = "outputOnly"
field156.appinfo = "Subtotal duration of contained CameraMovement move durations"
field156.name = "shotDuration"
field156.type = "SFTime"
Script146.addField([field156])

field157 = field()
field157.accessType = "outputOnly"
field157.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field157.name = "isActive"
field157.type = "SFBool"
Script146.addField([field157])

field158 = field()
field158.accessType = "initializeOnly"
field158.appinfo = "enable console output to trace script computations and prototype progress"
field158.name = "traceEnabled"
field158.type = "SFBool"
Script146.addField([field158])

field159 = field()
field159.accessType = "inputOutput"
field159.appinfo = "key array for interpolators"
field159.name = "key"
field159.type = "MFFloat"
Script146.addField([field159])

field160 = field()
field160.accessType = "inputOutput"
field160.appinfo = "keyValue array for PositionInterpolator"
field160.name = "keyValuePosition"
field160.type = "MFVec3f"
Script146.addField([field160])

field161 = field()
field161.accessType = "inputOutput"
field161.appinfo = "keyValue array for OrientationInterpolator"
field161.name = "keyValueOrientation"
field161.type = "MFRotation"
Script146.addField([field161])

IS162 = IS()

connect163 = connect()
connect163.nodeField = "description"
connect163.protoField = "description"
IS162.addConnect([connect163])

connect164 = connect()
connect164.nodeField = "enabled"
connect164.protoField = "enabled"
IS162.addConnect([connect164])

connect165 = connect()
connect165.nodeField = "moves"
connect165.protoField = "moves"
IS162.addConnect([connect165])

connect166 = connect()
connect166.nodeField = "initialPosition"
connect166.protoField = "initialPosition"
IS162.addConnect([connect166])

connect167 = connect()
connect167.nodeField = "initialOrientation"
connect167.protoField = "initialOrientation"
IS162.addConnect([connect167])

connect168 = connect()
connect168.nodeField = "initialAimPoint"
connect168.protoField = "initialAimPoint"
IS162.addConnect([connect168])

connect169 = connect()
connect169.nodeField = "initialFieldOfView"
connect169.protoField = "initialFieldOfView"
IS162.addConnect([connect169])

connect170 = connect()
connect170.nodeField = "initialFStop"
connect170.protoField = "initialFStop"
IS162.addConnect([connect170])

connect171 = connect()
connect171.nodeField = "initialFocusDistance"
connect171.protoField = "initialFocusDistance"
IS162.addConnect([connect171])

connect172 = connect()
connect172.nodeField = "shotDuration"
connect172.protoField = "shotDuration"
IS162.addConnect([connect172])

connect173 = connect()
connect173.nodeField = "isActive"
connect173.protoField = "isActive"
IS162.addConnect([connect173])

connect174 = connect()
connect174.nodeField = "traceEnabled"
connect174.protoField = "traceEnabled"
IS162.addConnect([connect174])
Script146.IS = IS162

Script146.setSourceCode('''\n"+
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
ProtoBody145.addChildren([Script146])
# Add any ROUTEs here, going from Script to other nodes within ProtoBody 
ProtoDeclare131.protoBody = ProtoBody145
Scene16.addChildren([ProtoDeclare131])
# =============== CameraMovement ============== 

ProtoDeclare175 = ProtoDeclare()
ProtoDeclare175.appinfo = "CameraMovement node defines a single camera movement animation including goalPosition, goalOrientation, goalAimPoint and goalFieldOfView."
ProtoDeclare175.name = "CameraMovement"

ProtoInterface176 = ProtoInterface()

field177 = field()
field177.accessType = "inputOutput"
field177.appinfo = "Text description to be displayed for this CameraMovement"
field177.name = "description"
field177.type = "SFString"
ProtoInterface176.addField([field177])

field178 = field()
field178.accessType = "inputOutput"
field178.appinfo = "Whether this CameraMovement can be activated"
field178.name = "enabled"
field178.type = "SFBool"
field178.value = "true"
ProtoInterface176.addField([field178])

field179 = field()
field179.accessType = "inputOutput"
field179.appinfo = "Duration in seconds for this move"
field179.name = "duration"
field179.type = "SFFloat"
field179.value = "0"
ProtoInterface176.addField([field179])

field180 = field()
field180.accessType = "inputOutput"
field180.appinfo = "Goal camera position for this move"
field180.name = "goalPosition"
field180.type = "SFVec3f"
field180.value = "0 0 10"
ProtoInterface176.addField([field180])

field181 = field()
field181.accessType = "inputOutput"
field181.appinfo = "Goal camera rotation for this move"
field181.name = "goalOrientation"
field181.type = "SFRotation"
field181.value = "0 0 1 0"
ProtoInterface176.addField([field181])

field182 = field()
field182.accessType = "inputOutput"
field182.appinfo = "Whether or not camera direction is tracking towards the aimPoint"
field182.name = "tracking"
field182.type = "SFBool"
field182.value = "false"
ProtoInterface176.addField([field182])

field183 = field()
field183.accessType = "inputOutput"
field183.appinfo = "Goal aimPoint for this move, ignored if tracking=false"
field183.name = "goalAimPoint"
field183.type = "SFVec3f"
field183.value = "0 0 0"
ProtoInterface176.addField([field183])

field184 = field()
field184.accessType = "inputOutput"
field184.appinfo = "Goal fieldOfView for this move"
field184.name = "goalFieldOfView"
field184.type = "SFFloat"
field184.value = "0.7854"
ProtoInterface176.addField([field184])

field185 = field()
field185.accessType = "inputOutput"
field185.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field185.name = "goalFStop"
field185.type = "SFFloat"
field185.value = "5.6"
ProtoInterface176.addField([field185])

field186 = field()
field186.accessType = "inputOutput"
field186.appinfo = "Distance to focal plane of sharpest focus"
field186.name = "goalFocusDistance"
field186.type = "SFFloat"
field186.value = "10"
ProtoInterface176.addField([field186])

field187 = field()
field187.accessType = "outputOnly"
field187.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field187.name = "isActive"
field187.type = "SFBool"
ProtoInterface176.addField([field187])

field188 = field()
field188.accessType = "initializeOnly"
field188.appinfo = "enable console output to trace script computations and prototype progress"
field188.name = "traceEnabled"
field188.type = "SFBool"
field188.value = "false"
ProtoInterface176.addField([field188])
ProtoDeclare175.protoInterface = ProtoInterface176

ProtoBody189 = ProtoBody()
# First node determines node type of this prototype 
# Subsequent nodes do not render, but still must be a valid X3D subgraph 
# Script holds CameraMovement initialization values for query by parent CameraShot, and also permits changing values via events 

Script190 = Script(directOutput = True, mustEvaluate = True)
Script190.DEF = "CameraMovementScript"

field191 = field()
field191.accessType = "inputOutput"
field191.appinfo = "Text description to be displayed for this CameraMovement"
field191.name = "description"
field191.type = "SFString"
Script190.addField([field191])

field192 = field()
field192.accessType = "inputOutput"
field192.appinfo = "Whether this CameraMovement can be activated"
field192.name = "enabled"
field192.type = "SFBool"
Script190.addField([field192])

field193 = field()
field193.accessType = "inputOutput"
field193.appinfo = "Duration in seconds for this move"
field193.name = "duration"
field193.type = "SFFloat"
Script190.addField([field193])

field194 = field()
field194.accessType = "inputOutput"
field194.appinfo = "Goal camera position for this move"
field194.name = "goalPosition"
field194.type = "SFVec3f"
Script190.addField([field194])

field195 = field()
field195.accessType = "inputOutput"
field195.appinfo = "Goal camera rotation for this move"
field195.name = "goalOrientation"
field195.type = "SFRotation"
Script190.addField([field195])

field196 = field()
field196.accessType = "inputOutput"
field196.appinfo = "Whether or not camera direction is tracking towards the aimPoint"
field196.name = "tracking"
field196.type = "SFBool"
Script190.addField([field196])

field197 = field()
field197.accessType = "inputOutput"
field197.appinfo = "Goal aimPoint for this move, ignored if tracking=false"
field197.name = "goalAimPoint"
field197.type = "SFVec3f"
Script190.addField([field197])

field198 = field()
field198.accessType = "inputOutput"
field198.appinfo = "Goal fieldOfView for this move"
field198.name = "goalFieldOfView"
field198.type = "SFFloat"
Script190.addField([field198])

field199 = field()
field199.accessType = "inputOutput"
field199.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field199.name = "goalFStop"
field199.type = "SFFloat"
Script190.addField([field199])

field200 = field()
field200.accessType = "inputOutput"
field200.appinfo = "Distance to focal plane of sharpest focus"
field200.name = "goalFocusDistance"
field200.type = "SFFloat"
Script190.addField([field200])

field201 = field()
field201.accessType = "outputOnly"
field201.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field201.name = "isActive"
field201.type = "SFBool"
Script190.addField([field201])

field202 = field()
field202.accessType = "initializeOnly"
field202.appinfo = "enable console output to trace script computations and prototype progress"
field202.name = "traceEnabled"
field202.type = "SFBool"
Script190.addField([field202])

IS203 = IS()

connect204 = connect()
connect204.nodeField = "description"
connect204.protoField = "description"
IS203.addConnect([connect204])

connect205 = connect()
connect205.nodeField = "enabled"
connect205.protoField = "enabled"
IS203.addConnect([connect205])

connect206 = connect()
connect206.nodeField = "duration"
connect206.protoField = "duration"
IS203.addConnect([connect206])

connect207 = connect()
connect207.nodeField = "goalPosition"
connect207.protoField = "goalPosition"
IS203.addConnect([connect207])

connect208 = connect()
connect208.nodeField = "goalOrientation"
connect208.protoField = "goalOrientation"
IS203.addConnect([connect208])

connect209 = connect()
connect209.nodeField = "tracking"
connect209.protoField = "tracking"
IS203.addConnect([connect209])

connect210 = connect()
connect210.nodeField = "goalAimPoint"
connect210.protoField = "goalAimPoint"
IS203.addConnect([connect210])

connect211 = connect()
connect211.nodeField = "goalFieldOfView"
connect211.protoField = "goalFieldOfView"
IS203.addConnect([connect211])

connect212 = connect()
connect212.nodeField = "goalFStop"
connect212.protoField = "goalFStop"
IS203.addConnect([connect212])

connect213 = connect()
connect213.nodeField = "goalFocusDistance"
connect213.protoField = "goalFocusDistance"
IS203.addConnect([connect213])

connect214 = connect()
connect214.nodeField = "isActive"
connect214.protoField = "isActive"
IS203.addConnect([connect214])

connect215 = connect()
connect215.nodeField = "traceEnabled"
connect215.protoField = "traceEnabled"
IS203.addConnect([connect215])
Script190.IS = IS203

Script190.setSourceCode('''\n"+
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
ProtoBody189.addChildren([Script190])
# Add any ROUTEs here, going from Script to other nodes within ProtoBody 
ProtoDeclare175.protoBody = ProtoBody189
Scene16.addChildren([ProtoDeclare175])
# =============== OfflineRender ============== 

ProtoDeclare216 = ProtoDeclare()
ProtoDeclare216.appinfo = "OfflineRender defines a parameters for offline rendering of Camera animation output to a movie file (or possibly a still shot)."
ProtoDeclare216.name = "OfflineRender"

ProtoInterface217 = ProtoInterface()
# TODO non-photorealistic rendering (NPR) parameters 

field218 = field()
field218.accessType = "inputOutput"
field218.appinfo = "Text description to be displayed for this OfflineRender"
field218.name = "description"
field218.type = "SFString"
ProtoInterface217.addField([field218])

field219 = field()
field219.accessType = "inputOutput"
field219.appinfo = "Whether this OfflineRender can be activated"
field219.name = "enabled"
field219.type = "SFBool"
field219.value = "true"
ProtoInterface217.addField([field219])

field220 = field()
field220.accessType = "inputOutput"
field220.appinfo = "Frames per second recorded for this rendering"
field220.name = "frameRate"
field220.type = "SFFloat"
field220.value = "30"
ProtoInterface217.addField([field220])

field221 = field()
field221.accessType = "inputOutput"
field221.appinfo = "Size of frame in number of pixels width and height"
field221.name = "frameSize"
field221.type = "SFVec2f"
field221.value = "640 480"
ProtoInterface217.addField([field221])

field222 = field()
field222.accessType = "inputOutput"
field222.appinfo = "Relative dimensions of pixel height/width typically 1.33 or 1"
field222.name = "pixelAspectRatio"
field222.type = "SFFloat"
field222.value = "1.33"
ProtoInterface217.addField([field222])

field223 = field()
field223.accessType = "inputOnly"
field223.appinfo = "Begin render operation"
field223.name = "set_startTime"
field223.type = "SFTime"
ProtoInterface217.addField([field223])

field224 = field()
field224.accessType = "outputOnly"
field224.appinfo = "Progress performing render operation (0..1)"
field224.name = "progress"
field224.type = "SFFloat"
ProtoInterface217.addField([field224])

field225 = field()
field225.accessType = "outputOnly"
field225.appinfo = "Render operation complete"
field225.name = "renderCompleteTime"
field225.type = "SFTime"
ProtoInterface217.addField([field225])

field226 = field()
field226.accessType = "initializeOnly"
field226.appinfo = "Format of rendered output movie (mpeg mp4 etc.), use first supported format"
field226.name = "movieFormat"
field226.type = "MFString"
field226.value = "\"mpeg\""
ProtoInterface217.addField([field226])

field227 = field()
field227.accessType = "initializeOnly"
field227.appinfo = "Format of rendered output images (png jpeg gif tiff etc.) use first supported format"
field227.name = "imageFormat"
field227.type = "MFString"
field227.value = "\"png\""
ProtoInterface217.addField([field227])

field228 = field()
field228.accessType = "initializeOnly"
field228.appinfo = "enable console output to trace script computations and prototype progress"
field228.name = "traceEnabled"
field228.type = "SFBool"
field228.value = "false"
ProtoInterface217.addField([field228])
ProtoDeclare216.protoInterface = ProtoInterface217

ProtoBody229 = ProtoBody()
# First node determines node type of this prototype 
# Subsequent nodes do not render, but still must be a valid X3D subgraph 

Script230 = Script(mustEvaluate = True)
Script230.DEF = "OfflineRenderScript"

field231 = field()
field231.accessType = "inputOutput"
field231.appinfo = "Text description to be displayed for this OfflineRender"
field231.name = "description"
field231.type = "SFString"
Script230.addField([field231])

field232 = field()
field232.accessType = "inputOutput"
field232.appinfo = "Whether this OfflineRender can be activated"
field232.name = "enabled"
field232.type = "SFBool"
Script230.addField([field232])

field233 = field()
field233.accessType = "inputOutput"
field233.appinfo = "Frames per second recorded for this rendering"
field233.name = "frameRate"
field233.type = "SFFloat"
Script230.addField([field233])

field234 = field()
field234.accessType = "inputOutput"
field234.appinfo = "Size of frame in number of pixels width and height"
field234.name = "frameSize"
field234.type = "SFVec2f"
Script230.addField([field234])

field235 = field()
field235.accessType = "inputOutput"
field235.appinfo = "Relative dimensions of pixel height/width typically 1.33 or 1"
field235.name = "pixelAspectRatio"
field235.type = "SFFloat"
Script230.addField([field235])

field236 = field()
field236.accessType = "inputOnly"
field236.appinfo = "Begin render operation"
field236.name = "set_startTime"
field236.type = "SFTime"
Script230.addField([field236])

field237 = field()
field237.accessType = "outputOnly"
field237.appinfo = "Progress performing render operation (0..1)"
field237.name = "progress"
field237.type = "SFFloat"
Script230.addField([field237])

field238 = field()
field238.accessType = "outputOnly"
field238.appinfo = "Render operation complete"
field238.name = "renderCompleteTime"
field238.type = "SFTime"
Script230.addField([field238])

field239 = field()
field239.accessType = "initializeOnly"
field239.appinfo = "Format of rendered output movie (mpeg mp4 etc.)"
field239.name = "movieFormat"
field239.type = "MFString"
Script230.addField([field239])

field240 = field()
field240.accessType = "initializeOnly"
field240.appinfo = "Format of rendered output images (png jpeg gif tiff etc.)"
field240.name = "imageFormat"
field240.type = "MFString"
Script230.addField([field240])

field241 = field()
field241.accessType = "initializeOnly"
field241.appinfo = "enable console output to trace script computations and prototype progress"
field241.name = "traceEnabled"
field241.type = "SFBool"
Script230.addField([field241])

IS242 = IS()

connect243 = connect()
connect243.nodeField = "description"
connect243.protoField = "description"
IS242.addConnect([connect243])

connect244 = connect()
connect244.nodeField = "enabled"
connect244.protoField = "enabled"
IS242.addConnect([connect244])

connect245 = connect()
connect245.nodeField = "frameRate"
connect245.protoField = "frameRate"
IS242.addConnect([connect245])

connect246 = connect()
connect246.nodeField = "frameSize"
connect246.protoField = "frameSize"
IS242.addConnect([connect246])

connect247 = connect()
connect247.nodeField = "pixelAspectRatio"
connect247.protoField = "pixelAspectRatio"
IS242.addConnect([connect247])

connect248 = connect()
connect248.nodeField = "set_startTime"
connect248.protoField = "set_startTime"
IS242.addConnect([connect248])

connect249 = connect()
connect249.nodeField = "progress"
connect249.protoField = "progress"
IS242.addConnect([connect249])

connect250 = connect()
connect250.nodeField = "renderCompleteTime"
connect250.protoField = "renderCompleteTime"
IS242.addConnect([connect250])

connect251 = connect()
connect251.nodeField = "movieFormat"
connect251.protoField = "movieFormat"
IS242.addConnect([connect251])

connect252 = connect()
connect252.nodeField = "imageFormat"
connect252.protoField = "imageFormat"
IS242.addConnect([connect252])

connect253 = connect()
connect253.nodeField = "traceEnabled"
connect253.protoField = "traceEnabled"
IS242.addConnect([connect253])
Script230.IS = IS242

Script230.setSourceCode('''\n"+
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
ProtoBody229.addChildren([Script230])
# Add any ROUTEs here, going from Script to other nodes within ProtoBody 
ProtoDeclare216.protoBody = ProtoBody229
Scene16.addChildren([ProtoDeclare216])
# =============== Launch Prototype Example ============== 

Background254 = Background()
Background254.skyColor = [0.282353,0.380392,0.470588]
Scene16.addChildren([Background254])

Anchor255 = Anchor()
Anchor255.description = "launch CameraExample scene"
Anchor255.url = ["CameraExamples.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d","CameraExamples.wrl","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.wrl"]

Transform256 = Transform()

Shape257 = Shape()

Text258 = Text()
Text258.string = ["CameraPrototypes.x3d","defines multiple prototype nodes","","Click on this text to see","CameraExamples.x3d scene"]

FontStyle259 = FontStyle(justify = ["MIDDLE","MIDDLE"])
Text258.fontStyle = FontStyle259
Shape257.geometry = Text258

Appearance260 = Appearance()

Material261 = Material()
Material261.diffuseColor = [1,1,0.2]
Appearance260.material = Material261
Shape257.appearance = Appearance260
Transform256.addChildren([Shape257])
Anchor255.addChildren([Transform256])
Scene16.addChildren([Anchor255])
X3D0.scene = Scene16
