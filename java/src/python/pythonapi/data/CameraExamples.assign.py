from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.content = "CameraExamples.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Camera, CameraShot and CameraMove examples that demonstrate storyboard capabilities and precise camera operation. This is a developmental effort for potential X3D Specification improvement."
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Two demos are found in the scene, click the \"red text\" on left or right to start. (a) SimpleShotsTest shows Zoom in/out, Pan left/right, Boom up/down, Tilt left/right, with each is defined by a CameraShot collecting a series of CameraMovements. (b) AimPointTest gradually slews the camera view to look at the sliding cube, then follows it around before returning to original viewpoint."
meta4.name = "documentation"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "Don Brutzman and Jeff Weekley"
meta5.name = "creator"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "18 June 2009"
meta6.name = "created"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "12 January 2014"
meta7.name = "modified"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "Schematron rules, backed up by initialize() checks"
meta8.name = "TODO"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "BeyondViewpointCameraNodesWeb3D2009.pdf"
meta9.name = "reference"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "CameraExamplesDemo.mp4"
meta10.name = "MovingImage"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "http://www.web3d.org/x3d/specifications/ISO-IEC-FDIS-19775-1.2-X3D-AbstractSpecification/Part01/components/navigation.html"
meta11.name = "reference"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "Camera nodes for Viewpoint navigation control"
meta12.name = "subject"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "CameraPrototypes.x3d"
meta13.name = "reference"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "CameraExamplesConsoleLog.txt"
meta14.name = "reference"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.avi"
meta15.name = "reference"
head1.addMeta([meta15])

meta16 = meta()
meta16.content = "http://www.web3d.org/x3d/content/examples/Basic/UniversalMediaMaterials/gridBack.x3d"
meta16.name = "reference"
head1.addMeta([meta16])
# TODO warn if more than one identifier present 

meta17 = meta()
meta17.content = "http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d"
meta17.name = "identifier"
head1.addMeta([meta17])

meta18 = meta()
meta18.content = "http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d"
meta18.name = "identifier"
head1.addMeta([meta18])

meta19 = meta()
meta19.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta19.name = "generator"
head1.addMeta([meta19])

meta20 = meta()
meta20.content = "../license.html"
meta20.name = "license"
head1.addMeta([meta20])
X3D0.head = head1

Scene21 = Scene()
# =============== Camera ============== 

ExternProtoDeclare22 = ExternProtoDeclare()
ExternProtoDeclare22.appinfo = "Camera node provides direct control of scene view to enable cinematic camera animation shot by shot and move by move along with still digital-photography settings for offline rendering of camera images"
ExternProtoDeclare22.name = "Camera"
ExternProtoDeclare22.url = ["CameraPrototypes.x3d#Camera","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#Camera","CameraPrototypes.wrl#Camera","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#Camera"]
# Viewpoint-related fields, NavigationInfo-related fields and Camera-unique fields 

field23 = field()
field23.accessType = "inputOutput"
field23.appinfo = "Text description to be displayed for this Camera"
field23.name = "description"
field23.type = "SFString"
ExternProtoDeclare22.addField([field23])

field24 = field()
field24.accessType = "inputOutput"
field24.appinfo = "Camera position in local transformation frame, which is default prior to first CameraShot initialPosition getting activated"
field24.name = "position"
field24.type = "SFVec3f"
ExternProtoDeclare22.addField([field24])

field25 = field()
field25.accessType = "inputOutput"
field25.appinfo = "Camera rotation in local transformation frame, which is default prior to first CameraShot initialPosition getting activated"
field25.name = "orientation"
field25.type = "SFRotation"
ExternProtoDeclare22.addField([field25])

field26 = field()
field26.accessType = "inputOutput"
field26.appinfo = "pi/4"
field26.name = "fieldOfView"
field26.type = "SFFloat"
ExternProtoDeclare22.addField([field26])

field27 = field()
field27.accessType = "inputOnly"
field27.appinfo = "input fraction drives interpolators"
field27.name = "set_fraction"
field27.type = "SFFloat"
ExternProtoDeclare22.addField([field27])

field28 = field()
field28.accessType = "inputOnly"
field28.appinfo = "input event binds or unbinds this Camera"
field28.name = "set_bind"
field28.type = "SFBool"
ExternProtoDeclare22.addField([field28])

field29 = field()
field29.accessType = "outputOnly"
field29.appinfo = "output event indicates when this Camera is bound"
field29.name = "bindTime"
field29.type = "SFTime"
ExternProtoDeclare22.addField([field29])

field30 = field()
field30.accessType = "outputOnly"
field30.appinfo = "output event indicates whether this Camera is bound or unbound"
field30.name = "isBound"
field30.type = "SFBool"
ExternProtoDeclare22.addField([field30])

field31 = field()
field31.accessType = "inputOutput"
field31.appinfo = "Vector distance to near clipping plane corresponds to NavigationInfo.avatarSize[0]"
field31.name = "nearClipPlane"
field31.type = "SFFloat"
ExternProtoDeclare22.addField([field31])

field32 = field()
field32.accessType = "inputOutput"
field32.appinfo = "Vector distance to far clipping plane corresponds to NavigationInfo.visibilityLimit"
field32.name = "farClipPlane"
field32.type = "SFFloat"
ExternProtoDeclare22.addField([field32])

field33 = field()
field33.accessType = "inputOutput"
field33.appinfo = "Array of CameraShot nodes which in turn contain CameraMovement nodes"
field33.name = "shots"
field33.type = "MFNode"
ExternProtoDeclare22.addField([field33])

field34 = field()
field34.accessType = "inputOutput"
field34.appinfo = "Whether camera headlight is on or off"
field34.name = "headlight"
field34.type = "SFBool"
ExternProtoDeclare22.addField([field34])

field35 = field()
field35.accessType = "inputOutput"
field35.appinfo = "Camera headlight color"
field35.name = "headlightColor"
field35.type = "SFColor"
ExternProtoDeclare22.addField([field35])

field36 = field()
field36.accessType = "inputOutput"
field36.appinfo = "Camera headlight intensity"
field36.name = "headlightIntensity"
field36.type = "SFFloat"
ExternProtoDeclare22.addField([field36])

field37 = field()
field37.accessType = "inputOutput"
field37.appinfo = "Camera filter color that modifies virtual lens capture"
field37.name = "filterColor"
field37.type = "SFColor"
ExternProtoDeclare22.addField([field37])

field38 = field()
field38.accessType = "inputOutput"
field38.appinfo = "Camera filter transparency that modifies virtual lens capture"
field38.name = "filterTransparency"
field38.type = "SFFloat"
ExternProtoDeclare22.addField([field38])

field39 = field()
field39.accessType = "inputOutput"
field39.appinfo = "upVector changes modify camera orientation (and possibly vice versa)"
field39.name = "upVector"
field39.type = "SFVec3f"
ExternProtoDeclare22.addField([field39])

field40 = field()
field40.accessType = "inputOutput"
field40.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field40.name = "fStop"
field40.type = "SFFloat"
ExternProtoDeclare22.addField([field40])

field41 = field()
field41.accessType = "inputOutput"
field41.appinfo = "Distance to focal plane of sharpest focus"
field41.name = "focusDistance"
field41.type = "SFFloat"
ExternProtoDeclare22.addField([field41])

field42 = field()
field42.accessType = "outputOnly"
field42.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field42.name = "isActive"
field42.type = "SFBool"
ExternProtoDeclare22.addField([field42])

field43 = field()
field43.accessType = "outputOnly"
field43.appinfo = "Total duration of contained enabled CameraShot (and thus CameraMovement) move durations"
field43.name = "totalDuration"
field43.type = "SFTime"
ExternProtoDeclare22.addField([field43])

field44 = field()
field44.accessType = "inputOutput"
field44.appinfo = "OfflineRender node"
field44.name = "offlineRender"
field44.type = "SFNode"
ExternProtoDeclare22.addField([field44])

field45 = field()
field45.accessType = "initializeOnly"
field45.appinfo = "enable console output to trace script computations and prototype progress"
field45.name = "traceEnabled"
field45.type = "SFBool"
ExternProtoDeclare22.addField([field45])
Scene21.addChildren([ExternProtoDeclare22])
# =============== CameraShot ============== 

ExternProtoDeclare46 = ExternProtoDeclare()
ExternProtoDeclare46.appinfo = "CameraShot collects a specific set of CameraMovement animations that make up an individual shot"
ExternProtoDeclare46.name = "CameraShot"
ExternProtoDeclare46.url = ["CameraPrototypes.x3d#CameraShot","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#CameraShot","CameraPrototypes.wrl#CameraShot","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#CameraShot"]

field47 = field()
field47.accessType = "inputOutput"
field47.appinfo = "Text description to be displayed for this CameraShot"
field47.name = "description"
field47.type = "SFString"
ExternProtoDeclare46.addField([field47])

field48 = field()
field48.accessType = "inputOutput"
field48.appinfo = "Whether this CameraShot can be activated"
field48.name = "enabled"
field48.type = "SFBool"
ExternProtoDeclare46.addField([field48])

field49 = field()
field49.accessType = "inputOutput"
field49.appinfo = "Set of CameraMovement nodes"
field49.name = "moves"
field49.type = "MFNode"
# initializing CameraMovement nodes are inserted here by scene author using ProtoInstance 
ExternProtoDeclare46.addField([field49])

field50 = field()
field50.accessType = "inputOutput"
field50.appinfo = "Setup to reinitialize camera position for this shot"
field50.name = "initialPosition"
field50.type = "SFVec3f"
ExternProtoDeclare46.addField([field50])

field51 = field()
field51.accessType = "inputOutput"
field51.appinfo = "Setup to reinitialize camera rotation for this shot"
field51.name = "initialOrientation"
field51.type = "SFRotation"
ExternProtoDeclare46.addField([field51])

field52 = field()
field52.accessType = "inputOutput"
field52.appinfo = "Setup to reinitialize aimpoint (relative location for camera direction) for this shot"
field52.name = "initialAimPoint"
field52.type = "SFVec3f"
ExternProtoDeclare46.addField([field52])

field53 = field()
field53.accessType = "inputOutput"
field53.appinfo = "pi/4"
field53.name = "initialFieldOfView"
field53.type = "SFFloat"
ExternProtoDeclare46.addField([field53])

field54 = field()
field54.accessType = "inputOutput"
field54.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field54.name = "initialFStop"
field54.type = "SFFloat"
ExternProtoDeclare46.addField([field54])

field55 = field()
field55.accessType = "inputOutput"
field55.appinfo = "Distance to focal plane of sharpest focus"
field55.name = "initialFocusDistance"
field55.type = "SFFloat"
ExternProtoDeclare46.addField([field55])

field56 = field()
field56.accessType = "outputOnly"
field56.appinfo = "Subtotal duration of contained CameraMovement move durations"
field56.name = "shotDuration"
field56.type = "SFTime"
ExternProtoDeclare46.addField([field56])

field57 = field()
field57.accessType = "outputOnly"
field57.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field57.name = "isActive"
field57.type = "SFBool"
ExternProtoDeclare46.addField([field57])

field58 = field()
field58.accessType = "initializeOnly"
field58.appinfo = "enable console output to trace script computations and prototype progress"
field58.name = "traceEnabled"
field58.type = "SFBool"
ExternProtoDeclare46.addField([field58])
Scene21.addChildren([ExternProtoDeclare46])
# =============== CameraMovement ============== 

ExternProtoDeclare59 = ExternProtoDeclare()
ExternProtoDeclare59.appinfo = "CameraMovement defines a single camera movement animation"
ExternProtoDeclare59.name = "CameraMovement"
ExternProtoDeclare59.url = ["CameraPrototypes.x3d#CameraMovement","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#CameraMovement","CameraPrototypes.wrl#CameraMovement","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#CameraMovement"]

field60 = field()
field60.accessType = "inputOutput"
field60.appinfo = "Text description to be displayed for this CameraMovement"
field60.name = "description"
field60.type = "SFString"
ExternProtoDeclare59.addField([field60])

field61 = field()
field61.accessType = "inputOutput"
field61.appinfo = "Whether this CameraMovement can be activated"
field61.name = "enabled"
field61.type = "SFBool"
ExternProtoDeclare59.addField([field61])

field62 = field()
field62.accessType = "inputOutput"
field62.appinfo = "Duration in seconds for this move"
field62.name = "duration"
field62.type = "SFFloat"
ExternProtoDeclare59.addField([field62])

field63 = field()
field63.accessType = "inputOutput"
field63.appinfo = "Goal camera position for this move"
field63.name = "goalPosition"
field63.type = "SFVec3f"
ExternProtoDeclare59.addField([field63])

field64 = field()
field64.accessType = "inputOutput"
field64.appinfo = "Goal camera rotation for this move"
field64.name = "goalOrientation"
field64.type = "SFRotation"
ExternProtoDeclare59.addField([field64])

field65 = field()
field65.accessType = "inputOutput"
field65.appinfo = "Whether or not camera direction is tracking towards the aimPoint"
field65.name = "tracking"
field65.type = "SFBool"
ExternProtoDeclare59.addField([field65])

field66 = field()
field66.accessType = "inputOutput"
field66.appinfo = "Goal aimPoint for this move, ignored if tracking=false"
field66.name = "goalAimPoint"
field66.type = "SFVec3f"
ExternProtoDeclare59.addField([field66])

field67 = field()
field67.accessType = "inputOutput"
field67.appinfo = "Goal fieldOfView for this move"
field67.name = "goalFieldOfView"
field67.type = "SFFloat"
ExternProtoDeclare59.addField([field67])

field68 = field()
field68.accessType = "inputOutput"
field68.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field68.name = "goalFStop"
field68.type = "SFFloat"
ExternProtoDeclare59.addField([field68])

field69 = field()
field69.accessType = "inputOutput"
field69.appinfo = "Distance to focal plane of sharpest focus"
field69.name = "goalFocusDistance"
field69.type = "SFFloat"
ExternProtoDeclare59.addField([field69])

field70 = field()
field70.accessType = "outputOnly"
field70.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field70.name = "isActive"
field70.type = "SFBool"
ExternProtoDeclare59.addField([field70])

field71 = field()
field71.accessType = "initializeOnly"
field71.appinfo = "enable console output to trace script computations and prototype progress"
field71.name = "traceEnabled"
field71.type = "SFBool"
ExternProtoDeclare59.addField([field71])
Scene21.addChildren([ExternProtoDeclare59])
# =============== OfflineRender ============== 

ExternProtoDeclare72 = ExternProtoDeclare()
ExternProtoDeclare72.appinfo = "OfflineRender defines a parameters for offline rendering of Camera animation output to a movie file (or possibly a still shot)"
ExternProtoDeclare72.name = "OfflineRender"
ExternProtoDeclare72.url = ["CameraPrototypes.x3d#OfflineRender","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#OfflineRender","CameraPrototypes.wrl#OfflineRender","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#OfflineRender"]
# TODO non-photorealistic rendering (NPR) parameters 

field73 = field()
field73.accessType = "inputOutput"
field73.appinfo = "Text description to be displayed for this OfflineRender"
field73.name = "description"
field73.type = "SFString"
ExternProtoDeclare72.addField([field73])

field74 = field()
field74.accessType = "inputOutput"
field74.appinfo = "Whether this OfflineRender can be activated"
field74.name = "enabled"
field74.type = "SFBool"
ExternProtoDeclare72.addField([field74])

field75 = field()
field75.accessType = "inputOutput"
field75.appinfo = "Frames per second recorded for this rendering"
field75.name = "frameRate"
field75.type = "SFFloat"
ExternProtoDeclare72.addField([field75])

field76 = field()
field76.accessType = "inputOutput"
field76.appinfo = "Size of frame in number of pixels width and height"
field76.name = "frameSize"
field76.type = "SFVec2f"
ExternProtoDeclare72.addField([field76])

field77 = field()
field77.accessType = "inputOutput"
field77.appinfo = "Relative dimensions of pixel height/width typically 1.33 or 1"
field77.name = "pixelAspectRatio"
field77.type = "SFFloat"
ExternProtoDeclare72.addField([field77])

field78 = field()
field78.accessType = "inputOnly"
field78.appinfo = "Begin render operation"
field78.name = "set_startTime"
field78.type = "SFTime"
ExternProtoDeclare72.addField([field78])

field79 = field()
field79.accessType = "outputOnly"
field79.appinfo = "Progress performing render operation (0..1)"
field79.name = "progress"
field79.type = "SFFloat"
ExternProtoDeclare72.addField([field79])

field80 = field()
field80.accessType = "outputOnly"
field80.appinfo = "Render operation complete"
field80.name = "renderCompleteTime"
field80.type = "SFTime"
ExternProtoDeclare72.addField([field80])

field81 = field()
field81.accessType = "initializeOnly"
field81.appinfo = "Format of rendered output movie (mpeg mp4 etc.), use first supported format"
field81.name = "movieFormat"
field81.type = "MFString"
ExternProtoDeclare72.addField([field81])

field82 = field()
field82.accessType = "initializeOnly"
field82.appinfo = "Format of rendered output images (png jpeg gif tiff etc.) use first supported format"
field82.name = "imageFormat"
field82.type = "MFString"
ExternProtoDeclare72.addField([field82])

field83 = field()
field83.accessType = "initializeOnly"
field83.appinfo = "enable console output to trace script computations and prototype progress"
field83.name = "traceEnabled"
field83.type = "SFBool"
ExternProtoDeclare72.addField([field83])
Scene21.addChildren([ExternProtoDeclare72])
# =============== Lights, camera, action! ============== 

DirectionalLight84 = DirectionalLight()
DirectionalLight84.direction = [0,-1,0]
DirectionalLight84.global_ = True
DirectionalLight84.intensity = 0.8
Scene21.addChildren([DirectionalLight84])

NavigationInfo85 = NavigationInfo()
NavigationInfo85.type = ["EXAMINE","FLY","ANY"]
Scene21.addChildren([NavigationInfo85])

Viewpoint86 = Viewpoint()
Viewpoint86.description = "Camera test scene entry view"
Viewpoint86.position = [0,2,12]
Scene21.addChildren([Viewpoint86])

Viewpoint87 = Viewpoint()
Viewpoint87.description = "Camera test scene from above"
Viewpoint87.orientation = [1,0,0,-1.57079]
Viewpoint87.position = [0,150,0]
Scene21.addChildren([Viewpoint87])
# Keep prototype instances in same file while developing, then move later 
# We will create examples matching those in the paper 
# =============== Camera.SimpleShotsTest ============== 

ProtoInstance88 = ProtoInstance()
ProtoInstance88.DEF = "Camera.SimpleShotsTest"
ProtoInstance88.name = "Camera"

fieldValue89 = fieldValue()
fieldValue89.name = "description"
fieldValue89.value = "SimpleShotsTest for camera Zoom Dolly Pan Boom and Tilt"
ProtoInstance88.addFieldValue([fieldValue89])

fieldValue90 = fieldValue()
fieldValue90.name = "headlight"
fieldValue90.value = "true"
ProtoInstance88.addFieldValue([fieldValue90])

fieldValue91 = fieldValue()
fieldValue91.name = "position"
fieldValue91.value = "-4 4 10"
ProtoInstance88.addFieldValue([fieldValue91])

fieldValue92 = fieldValue()
fieldValue92.name = "shots"

ProtoInstance93 = ProtoInstance()
ProtoInstance93.DEF = "Zoom"
ProtoInstance93.name = "CameraShot"

fieldValue94 = fieldValue()
fieldValue94.name = "description"
fieldValue94.value = "Simple shot of Camera Zoom"
ProtoInstance93.addFieldValue([fieldValue94])

fieldValue95 = fieldValue()
fieldValue95.name = "initialPosition"
fieldValue95.value = "-50 1 -10"
ProtoInstance93.addFieldValue([fieldValue95])

fieldValue96 = fieldValue()
fieldValue96.name = "initialOrientation"
fieldValue96.value = "0 1 0 0"
ProtoInstance93.addFieldValue([fieldValue96])

fieldValue97 = fieldValue()
fieldValue97.name = "moves"

ProtoInstance98 = ProtoInstance()
ProtoInstance98.name = "CameraMovement"

fieldValue99 = fieldValue()
fieldValue99.name = "description"
fieldValue99.value = "Camera Zoom In"
ProtoInstance98.addFieldValue([fieldValue99])

fieldValue100 = fieldValue()
fieldValue100.name = "duration"
fieldValue100.value = "3"
ProtoInstance98.addFieldValue([fieldValue100])

fieldValue101 = fieldValue()
fieldValue101.name = "goalPosition"
fieldValue101.value = "-50 1 -15"
ProtoInstance98.addFieldValue([fieldValue101])

fieldValue102 = fieldValue()
fieldValue102.name = "goalOrientation"
fieldValue102.value = "0 1 0 0"
ProtoInstance98.addFieldValue([fieldValue102])
fieldValue97.addChildren([ProtoInstance98])

ProtoInstance103 = ProtoInstance()
ProtoInstance103.name = "CameraMovement"

fieldValue104 = fieldValue()
fieldValue104.name = "description"
fieldValue104.value = "Camera Zoom Out"
ProtoInstance103.addFieldValue([fieldValue104])

fieldValue105 = fieldValue()
fieldValue105.name = "duration"
fieldValue105.value = "3"
ProtoInstance103.addFieldValue([fieldValue105])

fieldValue106 = fieldValue()
fieldValue106.name = "goalPosition"
fieldValue106.value = "-50 1 -10"
ProtoInstance103.addFieldValue([fieldValue106])

fieldValue107 = fieldValue()
fieldValue107.name = "goalOrientation"
fieldValue107.value = "0 1 0 0"
ProtoInstance103.addFieldValue([fieldValue107])
fieldValue97.addChildren([ProtoInstance103])

ProtoInstance108 = ProtoInstance()
ProtoInstance108.name = "CameraMovement"

fieldValue109 = fieldValue()
fieldValue109.name = "description"
fieldValue109.value = "Camera Pause"
ProtoInstance108.addFieldValue([fieldValue109])

fieldValue110 = fieldValue()
fieldValue110.name = "duration"
fieldValue110.value = "1"
ProtoInstance108.addFieldValue([fieldValue110])

fieldValue111 = fieldValue()
fieldValue111.name = "goalPosition"
fieldValue111.value = "-50 1 -10"
ProtoInstance108.addFieldValue([fieldValue111])

fieldValue112 = fieldValue()
fieldValue112.name = "goalOrientation"
fieldValue112.value = "0 1 0 0"
ProtoInstance108.addFieldValue([fieldValue112])
fieldValue97.addChildren([ProtoInstance108])
ProtoInstance93.addFieldValue([fieldValue97])
fieldValue92.addChildren([ProtoInstance93])

ProtoInstance113 = ProtoInstance()
ProtoInstance113.DEF = "Dolly"
ProtoInstance113.name = "CameraShot"

fieldValue114 = fieldValue()
fieldValue114.name = "description"
fieldValue114.value = "Simple shot of Camera Dolly"
ProtoInstance113.addFieldValue([fieldValue114])

fieldValue115 = fieldValue()
fieldValue115.name = "initialPosition"
fieldValue115.value = "-40 1 -10"
ProtoInstance113.addFieldValue([fieldValue115])

fieldValue116 = fieldValue()
fieldValue116.name = "initialOrientation"
fieldValue116.value = "0 1 0 0"
ProtoInstance113.addFieldValue([fieldValue116])

fieldValue117 = fieldValue()
fieldValue117.name = "moves"

ProtoInstance118 = ProtoInstance()
ProtoInstance118.DEF = "DollyMove1"
ProtoInstance118.name = "CameraMovement"

fieldValue119 = fieldValue()
fieldValue119.name = "description"
fieldValue119.value = "Camera Dolly from Right to Left"
ProtoInstance118.addFieldValue([fieldValue119])

fieldValue120 = fieldValue()
fieldValue120.name = "duration"
fieldValue120.value = "3"
ProtoInstance118.addFieldValue([fieldValue120])

fieldValue121 = fieldValue()
fieldValue121.name = "goalPosition"
fieldValue121.value = "-45 1 -10"
ProtoInstance118.addFieldValue([fieldValue121])

fieldValue122 = fieldValue()
fieldValue122.name = "goalOrientation"
fieldValue122.value = "0 1 0 0"
ProtoInstance118.addFieldValue([fieldValue122])
fieldValue117.addChildren([ProtoInstance118])

ProtoInstance123 = ProtoInstance()
ProtoInstance123.name = "CameraMovement"

fieldValue124 = fieldValue()
fieldValue124.name = "description"
fieldValue124.value = "Camera Dolly from Left to Right"
ProtoInstance123.addFieldValue([fieldValue124])

fieldValue125 = fieldValue()
fieldValue125.name = "duration"
fieldValue125.value = "3"
ProtoInstance123.addFieldValue([fieldValue125])

fieldValue126 = fieldValue()
fieldValue126.name = "goalPosition"
fieldValue126.value = "-40 1 -10"
ProtoInstance123.addFieldValue([fieldValue126])

fieldValue127 = fieldValue()
fieldValue127.name = "goalOrientation"
fieldValue127.value = "0 1 0 0"
ProtoInstance123.addFieldValue([fieldValue127])
fieldValue117.addChildren([ProtoInstance123])

ProtoInstance128 = ProtoInstance()
ProtoInstance128.name = "CameraMovement"

fieldValue129 = fieldValue()
fieldValue129.name = "description"
fieldValue129.value = "Camera Pause"
ProtoInstance128.addFieldValue([fieldValue129])

fieldValue130 = fieldValue()
fieldValue130.name = "duration"
fieldValue130.value = "1"
ProtoInstance128.addFieldValue([fieldValue130])

fieldValue131 = fieldValue()
fieldValue131.name = "goalPosition"
fieldValue131.value = "-40 1 -10"
ProtoInstance128.addFieldValue([fieldValue131])

fieldValue132 = fieldValue()
fieldValue132.name = "goalOrientation"
fieldValue132.value = "0 1 0 0"
ProtoInstance128.addFieldValue([fieldValue132])
fieldValue117.addChildren([ProtoInstance128])
ProtoInstance113.addFieldValue([fieldValue117])
fieldValue92.addChildren([ProtoInstance113])

ProtoInstance133 = ProtoInstance()
ProtoInstance133.DEF = "Pan"
ProtoInstance133.name = "CameraShot"

fieldValue134 = fieldValue()
fieldValue134.name = "description"
fieldValue134.value = "Simple shot of Camera Pan left right and back to center"
ProtoInstance133.addFieldValue([fieldValue134])

fieldValue135 = fieldValue()
fieldValue135.name = "initialPosition"
fieldValue135.value = "-30 1 -10"
ProtoInstance133.addFieldValue([fieldValue135])

fieldValue136 = fieldValue()
fieldValue136.name = "initialOrientation"
fieldValue136.value = "0 1 0 0"
ProtoInstance133.addFieldValue([fieldValue136])

fieldValue137 = fieldValue()
fieldValue137.name = "moves"

ProtoInstance138 = ProtoInstance()
ProtoInstance138.DEF = "PanLeft"
ProtoInstance138.name = "CameraMovement"

fieldValue139 = fieldValue()
fieldValue139.name = "description"
fieldValue139.value = "Pan Left"
ProtoInstance138.addFieldValue([fieldValue139])

fieldValue140 = fieldValue()
fieldValue140.name = "duration"
fieldValue140.value = "2"
ProtoInstance138.addFieldValue([fieldValue140])

fieldValue141 = fieldValue()
fieldValue141.name = "goalPosition"
fieldValue141.value = "-30 1 -10"
ProtoInstance138.addFieldValue([fieldValue141])

fieldValue142 = fieldValue()
fieldValue142.name = "goalOrientation"
fieldValue142.value = "0 1 0 0.4"
ProtoInstance138.addFieldValue([fieldValue142])
fieldValue137.addChildren([ProtoInstance138])

ProtoInstance143 = ProtoInstance()
ProtoInstance143.DEF = "PanRight"
ProtoInstance143.name = "CameraMovement"

fieldValue144 = fieldValue()
fieldValue144.name = "description"
fieldValue144.value = "Pan Right"
ProtoInstance143.addFieldValue([fieldValue144])

fieldValue145 = fieldValue()
fieldValue145.name = "duration"
fieldValue145.value = "3"
ProtoInstance143.addFieldValue([fieldValue145])

fieldValue146 = fieldValue()
fieldValue146.name = "goalPosition"
fieldValue146.value = "-30 1 -10"
ProtoInstance143.addFieldValue([fieldValue146])

fieldValue147 = fieldValue()
fieldValue147.name = "goalOrientation"
fieldValue147.value = "0 1 0 -0.4"
ProtoInstance143.addFieldValue([fieldValue147])
fieldValue137.addChildren([ProtoInstance143])

ProtoInstance148 = ProtoInstance()
ProtoInstance148.name = "CameraMovement"

fieldValue149 = fieldValue()
fieldValue149.name = "description"
fieldValue149.value = "Camera Pan back to Center"
ProtoInstance148.addFieldValue([fieldValue149])

fieldValue150 = fieldValue()
fieldValue150.name = "duration"
fieldValue150.value = "2"
ProtoInstance148.addFieldValue([fieldValue150])

fieldValue151 = fieldValue()
fieldValue151.name = "goalPosition"
fieldValue151.value = "-30 1 -10"
ProtoInstance148.addFieldValue([fieldValue151])

fieldValue152 = fieldValue()
fieldValue152.name = "goalOrientation"
fieldValue152.value = "0 1 0 0"
ProtoInstance148.addFieldValue([fieldValue152])
fieldValue137.addChildren([ProtoInstance148])

ProtoInstance153 = ProtoInstance()
ProtoInstance153.name = "CameraMovement"

fieldValue154 = fieldValue()
fieldValue154.name = "description"
fieldValue154.value = "Camera Pause"
ProtoInstance153.addFieldValue([fieldValue154])

fieldValue155 = fieldValue()
fieldValue155.name = "duration"
fieldValue155.value = "2"
ProtoInstance153.addFieldValue([fieldValue155])

fieldValue156 = fieldValue()
fieldValue156.name = "goalPosition"
fieldValue156.value = "-30 1 -10"
ProtoInstance153.addFieldValue([fieldValue156])

fieldValue157 = fieldValue()
fieldValue157.name = "goalOrientation"
fieldValue157.value = "0 1 0 0"
ProtoInstance153.addFieldValue([fieldValue157])
fieldValue137.addChildren([ProtoInstance153])
ProtoInstance133.addFieldValue([fieldValue137])
fieldValue92.addChildren([ProtoInstance133])

ProtoInstance158 = ProtoInstance()
ProtoInstance158.DEF = "CameraBoom"
ProtoInstance158.name = "CameraShot"

fieldValue159 = fieldValue()
fieldValue159.name = "description"
fieldValue159.value = "Camera Boom"
ProtoInstance158.addFieldValue([fieldValue159])

fieldValue160 = fieldValue()
fieldValue160.name = "initialPosition"
fieldValue160.value = "-20 1 -10"
ProtoInstance158.addFieldValue([fieldValue160])

fieldValue161 = fieldValue()
fieldValue161.name = "initialOrientation"
fieldValue161.value = "0 1 0 0"
ProtoInstance158.addFieldValue([fieldValue161])

fieldValue162 = fieldValue()
fieldValue162.name = "moves"

ProtoInstance163 = ProtoInstance()
ProtoInstance163.DEF = "CameraBoomUp"
ProtoInstance163.name = "CameraMovement"

fieldValue164 = fieldValue()
fieldValue164.name = "description"
fieldValue164.value = "Camera Boom Up"
ProtoInstance163.addFieldValue([fieldValue164])

fieldValue165 = fieldValue()
fieldValue165.name = "duration"
fieldValue165.value = "3"
ProtoInstance163.addFieldValue([fieldValue165])

fieldValue166 = fieldValue()
fieldValue166.name = "goalPosition"
fieldValue166.value = "-20 5 -10"
ProtoInstance163.addFieldValue([fieldValue166])

fieldValue167 = fieldValue()
fieldValue167.name = "goalOrientation"
fieldValue167.value = "0 1 0 0"
ProtoInstance163.addFieldValue([fieldValue167])
fieldValue162.addChildren([ProtoInstance163])

ProtoInstance168 = ProtoInstance()
ProtoInstance168.DEF = "BoomDown"
ProtoInstance168.name = "CameraMovement"

fieldValue169 = fieldValue()
fieldValue169.name = "description"
fieldValue169.value = "Camera Boom Down"
ProtoInstance168.addFieldValue([fieldValue169])

fieldValue170 = fieldValue()
fieldValue170.name = "duration"
fieldValue170.value = "3"
ProtoInstance168.addFieldValue([fieldValue170])

fieldValue171 = fieldValue()
fieldValue171.name = "goalPosition"
fieldValue171.value = "-20 1 -10"
ProtoInstance168.addFieldValue([fieldValue171])

fieldValue172 = fieldValue()
fieldValue172.name = "goalOrientation"
fieldValue172.value = "0 1 0 0"
ProtoInstance168.addFieldValue([fieldValue172])
fieldValue162.addChildren([ProtoInstance168])

ProtoInstance173 = ProtoInstance()
ProtoInstance173.DEF = "BoomPause"
ProtoInstance173.name = "CameraMovement"

fieldValue174 = fieldValue()
fieldValue174.name = "description"
fieldValue174.value = "Camera Pause"
ProtoInstance173.addFieldValue([fieldValue174])

fieldValue175 = fieldValue()
fieldValue175.name = "duration"
fieldValue175.value = "2"
ProtoInstance173.addFieldValue([fieldValue175])

fieldValue176 = fieldValue()
fieldValue176.name = "goalPosition"
fieldValue176.value = "-20 1 -10"
ProtoInstance173.addFieldValue([fieldValue176])

fieldValue177 = fieldValue()
fieldValue177.name = "goalOrientation"
fieldValue177.value = "0 1 0 0"
ProtoInstance173.addFieldValue([fieldValue177])
fieldValue162.addChildren([ProtoInstance173])
ProtoInstance158.addFieldValue([fieldValue162])
fieldValue92.addChildren([ProtoInstance158])

ProtoInstance178 = ProtoInstance()
ProtoInstance178.DEF = "CameraTilt"
ProtoInstance178.name = "CameraShot"

fieldValue179 = fieldValue()
fieldValue179.name = "description"
fieldValue179.value = "Camera Tilt"
ProtoInstance178.addFieldValue([fieldValue179])

fieldValue180 = fieldValue()
fieldValue180.name = "initialPosition"
fieldValue180.value = "-10 1 -10"
ProtoInstance178.addFieldValue([fieldValue180])

fieldValue181 = fieldValue()
fieldValue181.name = "initialOrientation"
fieldValue181.value = "0 0 1 0"
ProtoInstance178.addFieldValue([fieldValue181])

fieldValue182 = fieldValue()
fieldValue182.name = "traceEnabled"
fieldValue182.value = "true"
ProtoInstance178.addFieldValue([fieldValue182])

fieldValue183 = fieldValue()
fieldValue183.name = "moves"

ProtoInstance184 = ProtoInstance()
ProtoInstance184.name = "CameraMovement"

fieldValue185 = fieldValue()
fieldValue185.name = "description"
fieldValue185.value = "Camera Tilt Pause"
ProtoInstance184.addFieldValue([fieldValue185])

fieldValue186 = fieldValue()
fieldValue186.name = "duration"
fieldValue186.value = "1"
ProtoInstance184.addFieldValue([fieldValue186])

fieldValue187 = fieldValue()
fieldValue187.name = "goalPosition"
fieldValue187.value = "-10 1 -10"
ProtoInstance184.addFieldValue([fieldValue187])

fieldValue188 = fieldValue()
fieldValue188.name = "goalOrientation"
fieldValue188.value = "0 0 1 0"
ProtoInstance184.addFieldValue([fieldValue188])
fieldValue183.addChildren([ProtoInstance184])

ProtoInstance189 = ProtoInstance()
ProtoInstance189.DEF = "TiltDown"
ProtoInstance189.name = "CameraMovement"

fieldValue190 = fieldValue()
fieldValue190.name = "description"
fieldValue190.value = "Camera Tilt Left"
ProtoInstance189.addFieldValue([fieldValue190])

fieldValue191 = fieldValue()
fieldValue191.name = "duration"
fieldValue191.value = "3"
ProtoInstance189.addFieldValue([fieldValue191])

fieldValue192 = fieldValue()
fieldValue192.name = "goalPosition"
fieldValue192.value = "-10 1 -10"
ProtoInstance189.addFieldValue([fieldValue192])

fieldValue193 = fieldValue()
fieldValue193.name = "goalOrientation"
fieldValue193.value = "0 0 1 0.785"
ProtoInstance189.addFieldValue([fieldValue193])
fieldValue183.addChildren([ProtoInstance189])

ProtoInstance194 = ProtoInstance()
ProtoInstance194.DEF = "TiltPause"
ProtoInstance194.name = "CameraMovement"

fieldValue195 = fieldValue()
fieldValue195.name = "description"
fieldValue195.value = "Camera Tilt Pause"
ProtoInstance194.addFieldValue([fieldValue195])

fieldValue196 = fieldValue()
fieldValue196.name = "duration"
fieldValue196.value = "1"
ProtoInstance194.addFieldValue([fieldValue196])

fieldValue197 = fieldValue()
fieldValue197.name = "goalPosition"
fieldValue197.value = "-10 1 -10"
ProtoInstance194.addFieldValue([fieldValue197])

fieldValue198 = fieldValue()
fieldValue198.name = "goalOrientation"
fieldValue198.value = "0 0 1 0.785"
ProtoInstance194.addFieldValue([fieldValue198])
fieldValue183.addChildren([ProtoInstance194])

ProtoInstance199 = ProtoInstance()
ProtoInstance199.name = "CameraMovement"

fieldValue200 = fieldValue()
fieldValue200.name = "description"
fieldValue200.value = "Camera Tilt Right"
ProtoInstance199.addFieldValue([fieldValue200])

fieldValue201 = fieldValue()
fieldValue201.name = "duration"
fieldValue201.value = "3"
ProtoInstance199.addFieldValue([fieldValue201])

fieldValue202 = fieldValue()
fieldValue202.name = "goalPosition"
fieldValue202.value = "-10 1 -10"
ProtoInstance199.addFieldValue([fieldValue202])

fieldValue203 = fieldValue()
fieldValue203.name = "goalOrientation"
fieldValue203.value = "0 0 1 -0.785"
ProtoInstance199.addFieldValue([fieldValue203])
fieldValue183.addChildren([ProtoInstance199])

ProtoInstance204 = ProtoInstance()
ProtoInstance204.name = "CameraMovement"

fieldValue205 = fieldValue()
fieldValue205.name = "description"
fieldValue205.value = "Camera Tilt Pause"
ProtoInstance204.addFieldValue([fieldValue205])

fieldValue206 = fieldValue()
fieldValue206.name = "duration"
fieldValue206.value = "1"
ProtoInstance204.addFieldValue([fieldValue206])

fieldValue207 = fieldValue()
fieldValue207.name = "goalPosition"
fieldValue207.value = "-10 1 -10"
ProtoInstance204.addFieldValue([fieldValue207])

fieldValue208 = fieldValue()
fieldValue208.name = "goalOrientation"
fieldValue208.value = "0 0 1 -0.785"
ProtoInstance204.addFieldValue([fieldValue208])
fieldValue183.addChildren([ProtoInstance204])

ProtoInstance209 = ProtoInstance()
ProtoInstance209.DEF = "TiltReset"
ProtoInstance209.name = "CameraMovement"

fieldValue210 = fieldValue()
fieldValue210.name = "description"
fieldValue210.value = "Camera Tilt Reset"
ProtoInstance209.addFieldValue([fieldValue210])

fieldValue211 = fieldValue()
fieldValue211.name = "duration"
fieldValue211.value = "1"
ProtoInstance209.addFieldValue([fieldValue211])

fieldValue212 = fieldValue()
fieldValue212.name = "goalPosition"
fieldValue212.value = "-10 1 -10"
ProtoInstance209.addFieldValue([fieldValue212])

fieldValue213 = fieldValue()
fieldValue213.name = "goalOrientation"
fieldValue213.value = "0 0 1 0"
ProtoInstance209.addFieldValue([fieldValue213])
fieldValue183.addChildren([ProtoInstance209])

ProtoInstance214 = ProtoInstance()
ProtoInstance214.DEF = "TiltUp"
ProtoInstance214.name = "CameraMovement"

fieldValue215 = fieldValue()
fieldValue215.name = "description"
fieldValue215.value = "Return to home"
ProtoInstance214.addFieldValue([fieldValue215])

fieldValue216 = fieldValue()
fieldValue216.name = "duration"
fieldValue216.value = "2"
ProtoInstance214.addFieldValue([fieldValue216])

fieldValue217 = fieldValue()
fieldValue217.name = "goalPosition"
fieldValue217.value = "0 2 12"
ProtoInstance214.addFieldValue([fieldValue217])

fieldValue218 = fieldValue()
fieldValue218.name = "goalOrientation"
fieldValue218.value = "0 0 1 0"
ProtoInstance214.addFieldValue([fieldValue218])
fieldValue183.addChildren([ProtoInstance214])
ProtoInstance178.addFieldValue([fieldValue183])
fieldValue92.addChildren([ProtoInstance178])
ProtoInstance88.addFieldValue([fieldValue92])
Scene21.addChildren([ProtoInstance88])

Group219 = Group()
Group219.DEF = "AnimationGroup.SimpleShots"

TimeSensor220 = TimeSensor()
TimeSensor220.DEF = "CameraTimer.SimpleShots"
Group219.addChildren([TimeSensor220])
# initialize clock to match totalDuration of combined Shot Moves 

ROUTE221 = ROUTE()
ROUTE221.fromField = "totalDuration"
ROUTE221.fromNode = "Camera.SimpleShotsTest"
ROUTE221.toField = "cycleInterval"
ROUTE221.toNode = "CameraTimer.SimpleShots"
Group219.addChildren([ROUTE221])
# TimeSensor animates the CameraClock since that maintains the computed PositionInterpolator and OrientationInterpolator 

ROUTE222 = ROUTE()
ROUTE222.fromField = "fraction_changed"
ROUTE222.fromNode = "CameraTimer.SimpleShots"
ROUTE222.toField = "set_fraction"
ROUTE222.toNode = "Camera.SimpleShotsTest"
Group219.addChildren([ROUTE222])

Transform223 = Transform()
Transform223.DEF = "Trigger.SimpleShots"
Transform223.translation = [-4,4,0]

BooleanFilter224 = BooleanFilter()
BooleanFilter224.DEF = "TextTouchActive.SimpleShotsFilter"
Transform223.addChildren([BooleanFilter224])

TouchSensor225 = TouchSensor()
TouchSensor225.DEF = "TextTouch.SimpleShots"
TouchSensor225.description = "touch to animate Camera SimpleShotsTest"
Transform223.addChildren([TouchSensor225])

ROUTE226 = ROUTE()
ROUTE226.fromField = "inputTrue"
ROUTE226.fromNode = "TextTouchActive.SimpleShotsFilter"
ROUTE226.toField = "set_bind"
ROUTE226.toNode = "Camera.SimpleShotsTest"
Transform223.addChildren([ROUTE226])

ROUTE227 = ROUTE()
ROUTE227.fromField = "isActive"
ROUTE227.fromNode = "TextTouch.SimpleShots"
ROUTE227.toField = "set_boolean"
ROUTE227.toNode = "TextTouchActive.SimpleShotsFilter"
Transform223.addChildren([ROUTE227])

ROUTE228 = ROUTE()
ROUTE228.fromField = "touchTime"
ROUTE228.fromNode = "TextTouch.SimpleShots"
ROUTE228.toField = "startTime"
ROUTE228.toNode = "CameraTimer.SimpleShots"
Transform223.addChildren([ROUTE228])

Shape229 = Shape()

Text230 = Text()
Text230.string = ["Click to animate","SimpleShotsTest"]

FontStyle231 = FontStyle(justify = ["MIDDLE","MIDDLE"])
Text230.fontStyle = FontStyle231
Shape229.geometry = Text230

Appearance232 = Appearance()

Material233 = Material()
Material233.DEF = "ArtDeco5"
Material233.ambientIntensity = 0.24
Material233.diffuseColor = [0.945455,0.318988,0.321717]
Material233.shininess = 0.01
Material233.specularColor = [0.072727,0.021705,0.010732]
# Universal Media Library: ArtDeco 5 
Appearance232.material = Material233
Shape229.appearance = Appearance232
Transform223.addChildren([Shape229])
# Simplify intersection test for user selecting text 

Shape234 = Shape()
Shape234.DEF = "TransparentBox"

Appearance235 = Appearance()

Material236 = Material()
Material236.transparency = 1
Appearance235.material = Material236
Shape234.appearance = Appearance235

Box237 = Box(size = [6,2,0.0001])
Shape234.geometry = Box237
Transform223.addChildren([Shape234])
Group219.addChildren([Transform223])
Scene21.addChildren([Group219])

Group238 = Group()
Group238.DEF = "SimpleShotsTargets"

Transform239 = Transform()
Transform239.DEF = "TargetBoxZoom"
Transform239.translation = [-50,1,-20]

Shape240 = Shape()

Box241 = Box()
Shape240.geometry = Box241

Appearance242 = Appearance()

Material243 = Material()
Appearance242.material = Material243

ImageTexture244 = ImageTexture()
ImageTexture244.url = ["images/CameraMoveZoom.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveZoom.png"]
Appearance242.texture = ImageTexture244
Shape240.appearance = Appearance242
Transform239.addChildren([Shape240])

Transform245 = Transform()
Transform245.translation = [0,2,0]

Shape246 = Shape()

Text247 = Text()
Text247.string = ["Zoom in, out"]

FontStyle248 = FontStyle(justify = ["MIDDLE","MIDDLE"])
Text247.fontStyle = FontStyle248
Shape246.geometry = Text247

Appearance249 = Appearance()

Material250 = Material()
Appearance249.material = Material250
Shape246.appearance = Appearance249
Transform245.addChildren([Shape246])
Transform239.addChildren([Transform245])
Group238.addChildren([Transform239])

Transform251 = Transform()
Transform251.DEF = "TargetBoxDolly"
Transform251.translation = [-40,1,-20]

Shape252 = Shape()

Box253 = Box()
Shape252.geometry = Box253

Appearance254 = Appearance()

Material255 = Material()
Appearance254.material = Material255

ImageTexture256 = ImageTexture()
ImageTexture256.url = ["images/CameraMoveDolly.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveDolly.png"]
Appearance254.texture = ImageTexture256
Shape252.appearance = Appearance254
Transform251.addChildren([Shape252])

Transform257 = Transform()
Transform257.translation = [0,2,0]

Shape258 = Shape()

Text259 = Text()
Text259.string = ["Dolly left, right"]

FontStyle260 = FontStyle(justify = ["MIDDLE","MIDDLE"])
Text259.fontStyle = FontStyle260
Shape258.geometry = Text259

Appearance261 = Appearance()

Material262 = Material()
Appearance261.material = Material262
Shape258.appearance = Appearance261
Transform257.addChildren([Shape258])
Transform251.addChildren([Transform257])
Group238.addChildren([Transform251])

Transform263 = Transform()
Transform263.DEF = "TargetBoxPan"
Transform263.translation = [-30,1,-20]

Shape264 = Shape()

Box265 = Box()
Shape264.geometry = Box265

Appearance266 = Appearance()

Material267 = Material()
Appearance266.material = Material267

ImageTexture268 = ImageTexture()
ImageTexture268.url = ["images/CameraMovePan.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMovePan.png"]
Appearance266.texture = ImageTexture268
Shape264.appearance = Appearance266
Transform263.addChildren([Shape264])

Transform269 = Transform()
Transform269.translation = [0,2,0]

Shape270 = Shape()

Text271 = Text()
Text271.string = ["Pan left, right"]

FontStyle272 = FontStyle(justify = ["MIDDLE","MIDDLE"])
Text271.fontStyle = FontStyle272
Shape270.geometry = Text271

Appearance273 = Appearance()

Material274 = Material()
Appearance273.material = Material274
Shape270.appearance = Appearance273
Transform269.addChildren([Shape270])
Transform263.addChildren([Transform269])
Group238.addChildren([Transform263])

Transform275 = Transform()
Transform275.DEF = "TargetBoxBoom"
Transform275.translation = [-20,1,-20]

Shape276 = Shape()

Box277 = Box()
Shape276.geometry = Box277

Appearance278 = Appearance()

Material279 = Material()
Appearance278.material = Material279

ImageTexture280 = ImageTexture()
ImageTexture280.url = ["images/CameraMoveBoom.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveBoom.png"]
Appearance278.texture = ImageTexture280
Shape276.appearance = Appearance278
Transform275.addChildren([Shape276])

Transform281 = Transform()
Transform281.translation = [0,2,0]

Shape282 = Shape()

Text283 = Text()
Text283.string = ["Boom up, down"]

FontStyle284 = FontStyle(justify = ["MIDDLE","MIDDLE"])
Text283.fontStyle = FontStyle284
Shape282.geometry = Text283

Appearance285 = Appearance()

Material286 = Material()
Appearance285.material = Material286
Shape282.appearance = Appearance285
Transform281.addChildren([Shape282])
Transform275.addChildren([Transform281])
Group238.addChildren([Transform275])

Transform287 = Transform()
Transform287.DEF = "TargetBoxTilt"
Transform287.translation = [-10,1,-20]

Shape288 = Shape()

Box289 = Box()
Shape288.geometry = Box289

Appearance290 = Appearance()

Material291 = Material()
Appearance290.material = Material291

ImageTexture292 = ImageTexture()
ImageTexture292.url = ["images/CameraMoveTilt.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveTilt.png"]
Appearance290.texture = ImageTexture292
Shape288.appearance = Appearance290
Transform287.addChildren([Shape288])

Transform293 = Transform()
Transform293.translation = [0,2,0]

Shape294 = Shape()

Text295 = Text()
Text295.string = ["Tilt left, right"]

FontStyle296 = FontStyle(justify = ["MIDDLE","MIDDLE"])
Text295.fontStyle = FontStyle296
Shape294.geometry = Text295

Appearance297 = Appearance()

Material298 = Material()
Appearance297.material = Material298
Shape294.appearance = Appearance297
Transform293.addChildren([Shape294])
Transform287.addChildren([Transform293])
Group238.addChildren([Transform287])
Scene21.addChildren([Group238])
# =============== Camera.AimPointTest ============== 

ProtoInstance299 = ProtoInstance()
ProtoInstance299.DEF = "Camera.AimPointTest"
ProtoInstance299.name = "Camera"

fieldValue300 = fieldValue()
fieldValue300.name = "description"
fieldValue300.value = "AimPointTest for moving camera tracking moving target"
ProtoInstance299.addFieldValue([fieldValue300])

fieldValue301 = fieldValue()
fieldValue301.name = "position"
fieldValue301.value = "4 4 10"
ProtoInstance299.addFieldValue([fieldValue301])

fieldValue302 = fieldValue()
fieldValue302.name = "shots"

ProtoInstance303 = ProtoInstance()
ProtoInstance303.DEF = "Shot5"
ProtoInstance303.name = "CameraShot"

fieldValue304 = fieldValue()
fieldValue304.name = "description"
fieldValue304.value = "#3 Tracking shot"
ProtoInstance303.addFieldValue([fieldValue304])

fieldValue305 = fieldValue()
fieldValue305.name = "initialPosition"
fieldValue305.value = "6 6 10"
ProtoInstance303.addFieldValue([fieldValue305])

fieldValue306 = fieldValue()
fieldValue306.name = "initialOrientation"
fieldValue306.value = "0 1 0 0"
ProtoInstance303.addFieldValue([fieldValue306])

fieldValue307 = fieldValue()
fieldValue307.name = "moves"

ProtoInstance308 = ProtoInstance()
ProtoInstance308.DEF = "MoveAimPoint3.1"
ProtoInstance308.name = "CameraMovement"

fieldValue309 = fieldValue()
fieldValue309.name = "description"
fieldValue309.value = "AimPoint 3.1 moving BoxPath"
ProtoInstance308.addFieldValue([fieldValue309])

fieldValue310 = fieldValue()
fieldValue310.name = "tracking"
fieldValue310.value = "true"
ProtoInstance308.addFieldValue([fieldValue310])

fieldValue311 = fieldValue()
fieldValue311.name = "duration"
fieldValue311.value = "8"
ProtoInstance308.addFieldValue([fieldValue311])

fieldValue312 = fieldValue()
fieldValue312.name = "goalPosition"
fieldValue312.value = "6 6 10"
ProtoInstance308.addFieldValue([fieldValue312])
# goalAimPoint modified by ROUTE to match moving Box 
fieldValue307.addChildren([ProtoInstance308])

ProtoInstance313 = ProtoInstance()
ProtoInstance313.DEF = "MoveAimPoint3.2"
ProtoInstance313.name = "CameraMovement"

fieldValue314 = fieldValue()
fieldValue314.name = "description"
fieldValue314.value = "AimPoint 3.2 pan right while tracking"
ProtoInstance313.addFieldValue([fieldValue314])

fieldValue315 = fieldValue()
fieldValue315.name = "tracking"
fieldValue315.value = "true"
ProtoInstance313.addFieldValue([fieldValue315])

fieldValue316 = fieldValue()
fieldValue316.name = "duration"
fieldValue316.value = "8"
ProtoInstance313.addFieldValue([fieldValue316])

fieldValue317 = fieldValue()
fieldValue317.name = "goalPosition"
fieldValue317.value = "40 6 12"
ProtoInstance313.addFieldValue([fieldValue317])
# goalAimPoint modified by ROUTE to match moving Box 
fieldValue307.addChildren([ProtoInstance313])

ProtoInstance318 = ProtoInstance()
ProtoInstance318.DEF = "MoveAimPoint3.3"
ProtoInstance318.name = "CameraMovement"

fieldValue319 = fieldValue()
fieldValue319.name = "description"
fieldValue319.value = "AimPoint 3.3 boom up while tracking"
ProtoInstance318.addFieldValue([fieldValue319])

fieldValue320 = fieldValue()
fieldValue320.name = "tracking"
fieldValue320.value = "true"
ProtoInstance318.addFieldValue([fieldValue320])

fieldValue321 = fieldValue()
fieldValue321.name = "duration"
fieldValue321.value = "3"
ProtoInstance318.addFieldValue([fieldValue321])

fieldValue322 = fieldValue()
fieldValue322.name = "goalPosition"
fieldValue322.value = "40 20 13"
ProtoInstance318.addFieldValue([fieldValue322])
# goalAimPoint modified by ROUTE to match moving Box 
fieldValue307.addChildren([ProtoInstance318])

ProtoInstance323 = ProtoInstance()
ProtoInstance323.DEF = "MoveAimPoint3.4"
ProtoInstance323.name = "CameraMovement"

fieldValue324 = fieldValue()
fieldValue324.name = "description"
fieldValue324.value = "AimPoint 3.4 restore camera back to home"
ProtoInstance323.addFieldValue([fieldValue324])
# can test tracking or not using following values 

fieldValue325 = fieldValue()
fieldValue325.name = "tracking"
fieldValue325.value = "true"
ProtoInstance323.addFieldValue([fieldValue325])

fieldValue326 = fieldValue()
fieldValue326.name = "duration"
fieldValue326.value = "5"
ProtoInstance323.addFieldValue([fieldValue326])

fieldValue327 = fieldValue()
fieldValue327.name = "goalPosition"
fieldValue327.value = "4 4 10"
ProtoInstance323.addFieldValue([fieldValue327])

fieldValue328 = fieldValue()
fieldValue328.name = "goalAimPoint"
fieldValue328.value = "4 4 0"
ProtoInstance323.addFieldValue([fieldValue328])

fieldValue329 = fieldValue()
fieldValue329.name = "goalOrientation"
fieldValue329.value = "0 1 0 0"
ProtoInstance323.addFieldValue([fieldValue329])
fieldValue307.addChildren([ProtoInstance323])
ProtoInstance303.addFieldValue([fieldValue307])
fieldValue302.addChildren([ProtoInstance303])
ProtoInstance299.addFieldValue([fieldValue302])
Scene21.addChildren([ProtoInstance299])

Group330 = Group()
Group330.DEF = "AnimationGroup.AimPointTest"

TimeSensor331 = TimeSensor()
TimeSensor331.DEF = "CameraTimer.AimPointTest"
Group330.addChildren([TimeSensor331])
# initialize clock to match totalDuration of combined Shot Moves 

ROUTE332 = ROUTE()
ROUTE332.fromField = "totalDuration"
ROUTE332.fromNode = "Camera.AimPointTest"
ROUTE332.toField = "cycleInterval"
ROUTE332.toNode = "CameraTimer.AimPointTest"
Group330.addChildren([ROUTE332])
# TimeSensor animates the CameraClock since that maintains the computed PositionInterpolator and OrientationInterpolator 

ROUTE333 = ROUTE()
ROUTE333.fromField = "fraction_changed"
ROUTE333.fromNode = "CameraTimer.AimPointTest"
ROUTE333.toField = "set_fraction"
ROUTE333.toNode = "Camera.AimPointTest"
Group330.addChildren([ROUTE333])

Transform334 = Transform()
Transform334.DEF = "Trigger.AimPointTest"
Transform334.translation = [4,4,0]

BooleanFilter335 = BooleanFilter()
BooleanFilter335.DEF = "TextTouchActive.AimPointFilter"
Transform334.addChildren([BooleanFilter335])

TouchSensor336 = TouchSensor()
TouchSensor336.DEF = "TextTouch.AimPointTest"
TouchSensor336.description = "touch to animate Camera AimPointTest"
Transform334.addChildren([TouchSensor336])

ROUTE337 = ROUTE()
ROUTE337.fromField = "inputTrue"
ROUTE337.fromNode = "TextTouchActive.AimPointFilter"
ROUTE337.toField = "set_bind"
ROUTE337.toNode = "Camera.AimPointTest"
Transform334.addChildren([ROUTE337])

ROUTE338 = ROUTE()
ROUTE338.fromField = "isActive"
ROUTE338.fromNode = "TextTouch.AimPointTest"
ROUTE338.toField = "set_boolean"
ROUTE338.toNode = "TextTouchActive.AimPointFilter"
Transform334.addChildren([ROUTE338])

ROUTE339 = ROUTE()
ROUTE339.fromField = "touchTime"
ROUTE339.fromNode = "TextTouch.AimPointTest"
ROUTE339.toField = "startTime"
ROUTE339.toNode = "CameraTimer.AimPointTest"
Transform334.addChildren([ROUTE339])

Shape340 = Shape()

Text341 = Text()
Text341.string = ["Click to animate","AimPointTest"]

FontStyle342 = FontStyle(justify = ["MIDDLE","MIDDLE"])
Text341.fontStyle = FontStyle342
Shape340.geometry = Text341

Appearance343 = Appearance()

Material344 = Material()
Material344.USE = "ArtDeco5"
Appearance343.material = Material344
Shape340.appearance = Appearance343
Transform334.addChildren([Shape340])

Shape345 = Shape()
Shape345.USE = "TransparentBox"
Transform334.addChildren([Shape345])
Group330.addChildren([Transform334])
Scene21.addChildren([Group330])
# TODO build a test once implemented 

ProtoInstance346 = ProtoInstance()
ProtoInstance346.name = "OfflineRender"
Scene21.addChildren([ProtoInstance346])
# =============== animate a camera shape to visualize view changes ============== 

Transform347 = Transform()
Transform347.DEF = "CameraShapeTransform"
Transform347.translation = [0,0.5,0]
# move CameraShape using active Camera 

ROUTE348 = ROUTE()
ROUTE348.fromField = "position_changed"
ROUTE348.fromNode = "Camera.SimpleShotsTest"
ROUTE348.toField = "translation"
ROUTE348.toNode = "CameraShapeTransform"
Transform347.addChildren([ROUTE348])

ROUTE349 = ROUTE()
ROUTE349.fromField = "orientation_changed"
ROUTE349.fromNode = "Camera.SimpleShotsTest"
ROUTE349.toField = "rotation"
ROUTE349.toNode = "CameraShapeTransform"
Transform347.addChildren([ROUTE349])

ROUTE350 = ROUTE()
ROUTE350.fromField = "position"
ROUTE350.fromNode = "Camera.AimPointTest"
ROUTE350.toField = "translation"
ROUTE350.toNode = "CameraShapeTransform"
Transform347.addChildren([ROUTE350])

ROUTE351 = ROUTE()
ROUTE351.fromField = "orientation_changed"
ROUTE351.fromNode = "Camera.AimPointTest"
ROUTE351.toField = "rotation"
ROUTE351.toNode = "CameraShapeTransform"
Transform347.addChildren([ROUTE351])

Transform352 = Transform()
Transform352.DEF = "CameraOffsetTransform"
Transform352.translation = [0,0,0.25]

TouchSensor353 = TouchSensor()
TouchSensor353.DEF = "CameraShapeTouched"
Transform352.addChildren([TouchSensor353])

Inline354 = Inline()
Inline354.DEF = "CameraShape"
Inline354.url = ["CameraShape.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraShape.x3d"]
Transform352.addChildren([Inline354])

Shape355 = Shape()
Shape355.DEF = "SightLine"

IndexedLineSet356 = IndexedLineSet(coordIndex = [0,1])

Coordinate357 = Coordinate()
Coordinate357.point = [0,0,0,0,0,-100]
IndexedLineSet356.coord = Coordinate357
Shape355.geometry = IndexedLineSet356

Appearance358 = Appearance()

Material359 = Material()
Material359.emissiveColor = [0.8,0.8,0.4]
Appearance358.material = Material359
Shape355.appearance = Appearance358
Transform352.addChildren([Shape355])
Transform347.addChildren([Transform352])
# Display frustum to show camera view within the scene, toggled by user selecting CameraShape 

ExternProtoDeclare360 = ExternProtoDeclare()
ExternProtoDeclare360.appinfo = "Display view frustum associated with a given pair of Viewpoint NavigationInfo nodes"
ExternProtoDeclare360.name = "ViewFrustum"
ExternProtoDeclare360.url = ["../../X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.x3d#ViewFrustum","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.x3d#ViewFrustum","../../X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.wrl#ViewFrustum","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.wrl#ViewFrustum"]

field361 = field()
field361.accessType = "initializeOnly"
field361.appinfo = "required: insert Viewpoint DEF or USE node for view of interest"
field361.name = "ViewpointNode"
field361.type = "SFNode"
ExternProtoDeclare360.addField([field361])

field362 = field()
field362.accessType = "initializeOnly"
field362.appinfo = "required: insert NavigationInfo DEF or USE node of interest"
field362.name = "NavigationInfoNode"
field362.type = "SFNode"
ExternProtoDeclare360.addField([field362])

field363 = field()
field363.accessType = "inputOutput"
field363.appinfo = "whether or not frustum geometry is rendered"
field363.name = "visible"
field363.type = "SFBool"
ExternProtoDeclare360.addField([field363])

field364 = field()
field364.accessType = "inputOutput"
field364.appinfo = "RGB color of ViewFrustum outline, default value 0.9 0.9 0.9"
field364.name = "lineColor"
field364.type = "SFColor"
ExternProtoDeclare360.addField([field364])

field365 = field()
field365.accessType = "inputOutput"
field365.appinfo = "RGB color of ViewFrustum hull geometry, default value 0.8 0.8 0.8"
field365.name = "frustumColor"
field365.type = "SFColor"
ExternProtoDeclare360.addField([field365])

field366 = field()
field366.accessType = "inputOutput"
field366.appinfo = "transparency of ViewFrustum hull geometry, default value 0.5"
field366.name = "transparency"
field366.type = "SFFloat"
ExternProtoDeclare360.addField([field366])

field367 = field()
field367.accessType = "inputOutput"
field367.appinfo = "assumed ratio height/width, default value 0.75"
field367.name = "aspectRatio"
field367.type = "SFFloat"
ExternProtoDeclare360.addField([field367])

field368 = field()
field368.accessType = "initializeOnly"
field368.appinfo = "debug support, default false"
field368.name = "trace"
field368.type = "SFBool"
ExternProtoDeclare360.addField([field368])
Transform347.addChildren([ExternProtoDeclare360])

ProtoInstance369 = ProtoInstance()
ProtoInstance369.DEF = "ViewFrustumNode"
ProtoInstance369.name = "ViewFrustum"

fieldValue370 = fieldValue()
fieldValue370.name = "ViewpointNode"

Viewpoint371 = Viewpoint()
Viewpoint371.DEF = "FrustumViewpoint"
Viewpoint371.description = "viewpoint for ViewFrustum"
Viewpoint371.position = [0,0,0]
fieldValue370.addChildren([Viewpoint371])
ProtoInstance369.addFieldValue([fieldValue370])

fieldValue372 = fieldValue()
fieldValue372.name = "NavigationInfoNode"

NavigationInfo373 = NavigationInfo()
NavigationInfo373.DEF = "TestNavigationInfo"
NavigationInfo373.transitionType = ["ANIMATE"]
NavigationInfo373.visibilityLimit = 100
fieldValue372.addChildren([NavigationInfo373])
ProtoInstance369.addFieldValue([fieldValue372])

fieldValue374 = fieldValue()
fieldValue374.name = "visible"
fieldValue374.value = "false"
ProtoInstance369.addFieldValue([fieldValue374])

fieldValue375 = fieldValue()
fieldValue375.name = "lineColor"
fieldValue375.value = "0.9 0.9 0.9"
ProtoInstance369.addFieldValue([fieldValue375])

fieldValue376 = fieldValue()
fieldValue376.name = "frustumColor"
fieldValue376.value = "0.8 0.8 0.8"
ProtoInstance369.addFieldValue([fieldValue376])

fieldValue377 = fieldValue()
fieldValue377.name = "transparency"
fieldValue377.value = "0.95"
ProtoInstance369.addFieldValue([fieldValue377])
Transform347.addChildren([ProtoInstance369])

BooleanToggle378 = BooleanToggle()
BooleanToggle378.DEF = "ViewFrustumToggle"
Transform347.addChildren([BooleanToggle378])

ROUTE379 = ROUTE()
ROUTE379.fromField = "isActive"
ROUTE379.fromNode = "CameraShapeTouched"
ROUTE379.toField = "set_boolean"
ROUTE379.toNode = "ViewFrustumToggle"
Transform347.addChildren([ROUTE379])

ROUTE380 = ROUTE()
ROUTE380.fromField = "toggle"
ROUTE380.fromNode = "ViewFrustumToggle"
ROUTE380.toField = "set_visible"
ROUTE380.toNode = "ViewFrustumNode"
Transform347.addChildren([ROUTE380])
Scene21.addChildren([Transform347])
# =============== add checkerboard, axes and other things to look at while animating ============== 

Background381 = Background()
Background381.skyColor = [0.282353,0.380392,0.470588]
Scene21.addChildren([Background381])

Transform382 = Transform()
Transform382.rotation = [1,0,0,-1.57079]
Transform382.scale = [10,10,10]

Shape383 = Shape()

Appearance384 = Appearance()

Material385 = Material()
Material385.ambientIntensity = 0.01
Material385.diffuseColor = [1.0,1.0,1.0]
Material385.shininess = 0.05
Appearance384.material = Material385
Shape383.appearance = Appearance384

IndexedFaceSet386 = IndexedFaceSet(colorIndex = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], colorPerVertex = False, coordIndex = [0,8,9,1,-1,1,9,10,2,-1,2,10,11,3,-1,3,11,12,4,-1,4,12,13,5,-1,5,13,14,6,-1,6,14,15,7,-1,8,16,17,9,-1,9,17,18,10,-1,10,18,19,11,-1,11,19,20,12,-1,12,20,21,13,-1,13,21,22,14,-1,14,22,23,15,-1,16,24,25,17,-1,17,25,26,18,-1,18,26,27,19,-1,19,27,28,20,-1,20,28,29,21,-1,21,29,30,22,-1,22,30,31,23,-1,24,32,33,25,-1,25,33,34,26,-1,26,34,35,27,-1,27,35,36,28,-1,28,36,37,29,-1,29,37,38,30,-1,30,38,39,31,-1,32,40,41,33,-1,33,41,42,34,-1,34,42,43,35,-1,35,43,44,36,-1,36,44,45,37,-1,37,45,46,38,-1,38,46,47,39,-1,40,48,49,41,-1,41,49,50,42,-1,42,50,51,43,-1,43,51,52,44,-1,44,52,53,45,-1,45,53,54,46,-1,46,54,55,47,-1,48,56,57,49,-1,49,57,58,50,-1,50,58,59,51,-1,51,59,60,52,-1,52,60,61,53,-1,53,61,62,54,-1,54,62,63,55,-1], normalPerVertex = False, solid = False)

Coordinate387 = Coordinate()
Coordinate387.point = [-5.25,5.25,0.0,-3.75,5.25,0.0,-2.25,5.25,0.0,-0.75,5.25,0.0,0.75,5.25,0.0,2.25,5.25,0.0,3.75,5.25,0.0,5.25,5.25,0.0,-5.25,3.75,0.0,-3.75,3.75,0.0,-2.25,3.75,0.0,-0.75,3.75,0.0,0.75,3.75,0.0,2.25,3.75,0.0,3.75,3.75,0.0,5.25,3.75,0.0,-5.25,2.25,0.0,-3.75,2.25,0.0,-2.25,2.25,0.0,-0.75,2.25,0.0,0.75,2.25,0.0,2.25,2.25,0.0,3.75,2.25,0.0,5.25,2.25,0.0,-5.25,0.75,0.0,-3.75,0.75,0.0,-2.25,0.75,0.0,-0.75,0.75,0.0,0.75,0.75,0.0,2.25,0.75,0.0,3.75,0.75,0.0,5.25,0.75,0.0,-5.25,-0.75,0.0,-3.75,-0.75,0.0,-2.25,-0.75,0.0,-0.75,-0.75,0.0,0.75,-0.75,0.0,2.25,-0.75,0.0,3.75,-0.75,0.0,5.25,-0.75,0.0,-5.25,-2.25,0.0,-3.75,-2.25,0.0,-2.25,-2.25,0.0,-0.75,-2.25,0.0,0.75,-2.25,0.0,2.25,-2.25,0.0,3.75,-2.25,0.0,5.25,-2.25,0.0,-5.25,-3.75,0.0,-3.75,-3.75,0.0,-2.25,-3.75,0.0,-0.75,-3.75,0.0,0.75,-3.75,0.0,2.25,-3.75,0.0,3.75,-3.75,0.0,5.25,-3.75,0.0,-5.25,-5.25,0.0,-3.75,-5.25,0.0,-2.25,-5.25,0.0,-0.75,-5.25,0.0,0.75,-5.25,0.0,2.25,-5.25,0.0,3.75,-5.25,0.0,5.25,-5.25,0.0]
IndexedFaceSet386.coord = Coordinate387

Color388 = Color()
Color388.color = [0.435294,0.741176,0,0,0.560784,0.580392]
IndexedFaceSet386.color = Color388
Shape383.geometry = IndexedFaceSet386
Transform382.addChildren([Shape383])
Scene21.addChildren([Transform382])

Transform389 = Transform()
Transform389.scale = [3,3,3]
Transform389.translation = [0,0.25,0]

Inline390 = Inline()
Inline390.DEF = "CoordinateAxes"
Inline390.url = ["../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","../../Savage/Tools/Authoring/CoordinateAxes.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.x3d","../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","../../Savage/Tools/Authoring/CoordinateAxes.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.wrl"]
Transform389.addChildren([Inline390])
Scene21.addChildren([Transform389])

Transform391 = Transform()
Transform391.DEF = "MovingBoxTransform"

PositionInterpolator392 = PositionInterpolator()
PositionInterpolator392.DEF = "BoxPath"
PositionInterpolator392.key = [0,0.25,0.5,0.75,1]
PositionInterpolator392.keyValue = [-5,1,5,45,1,5,45,1,-45,-5,1,-45,-5,1,5]
Transform391.addChildren([PositionInterpolator392])

TimeSensor393 = TimeSensor()
TimeSensor393.DEF = "BoxTimer"
TimeSensor393.cycleInterval = 10
TimeSensor393.loop = True
Transform391.addChildren([TimeSensor393])

ROUTE394 = ROUTE()
ROUTE394.fromField = "value_changed"
ROUTE394.fromNode = "BoxPath"
ROUTE394.toField = "translation"
ROUTE394.toNode = "MovingBoxTransform"
Transform391.addChildren([ROUTE394])

ROUTE395 = ROUTE()
ROUTE395.fromField = "value_changed"
ROUTE395.fromNode = "BoxPath"
ROUTE395.toField = "goalAimPoint"
ROUTE395.toNode = "MoveAimPoint3.1"
Transform391.addChildren([ROUTE395])

ROUTE396 = ROUTE()
ROUTE396.fromField = "value_changed"
ROUTE396.fromNode = "BoxPath"
ROUTE396.toField = "goalAimPoint"
ROUTE396.toNode = "MoveAimPoint3.2"
Transform391.addChildren([ROUTE396])

ROUTE397 = ROUTE()
ROUTE397.fromField = "value_changed"
ROUTE397.fromNode = "BoxPath"
ROUTE397.toField = "goalAimPoint"
ROUTE397.toNode = "MoveAimPoint3.3"
Transform391.addChildren([ROUTE397])

ROUTE398 = ROUTE()
ROUTE398.fromField = "fraction_changed"
ROUTE398.fromNode = "BoxTimer"
ROUTE398.toField = "set_fraction"
ROUTE398.toNode = "BoxPath"
Transform391.addChildren([ROUTE398])

Shape399 = Shape()

Box400 = Box()
Shape399.geometry = Box400

Appearance401 = Appearance()

Material402 = Material()
Appearance401.material = Material402

ImageTexture403 = ImageTexture()
ImageTexture403.url = ["../earth-topo.png","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.png"]
Appearance401.texture = ImageTexture403
Shape399.appearance = Appearance401
Transform391.addChildren([Shape399])
Scene21.addChildren([Transform391])
# ================ CrossHair visualization for center of screen ================ 

ExternProtoDeclare404 = ExternProtoDeclare()
ExternProtoDeclare404.appinfo = "CrossHair prototype provides a heads-up display (HUD) crosshair at the view center, which is useful for assessing NavigationInfo lookAt point"
ExternProtoDeclare404.name = "CrossHair"
ExternProtoDeclare404.url = ["../../Savage/Tools/HeadsUpDisplays/CrossHairPrototype.x3d#CrossHair","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/CrossHairPrototype.x3d#CrossHair","../../Savage/Tools/HeadsUpDisplays/CrossHairPrototype.wrl#CrossHair","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/CrossHairPrototype.wrl#CrossHair"]

field405 = field()
field405.accessType = "initializeOnly"
field405.appinfo = "whether CrissHair orititype is enabled or not"
field405.name = "enabled"
field405.type = "SFBool"
ExternProtoDeclare404.addField([field405])

field406 = field()
field406.accessType = "inputOnly"
field406.appinfo = "control whether enabled/disabled"
field406.name = "set_enabled"
field406.type = "SFBool"
ExternProtoDeclare404.addField([field406])

field407 = field()
field407.accessType = "inputOutput"
field407.appinfo = "color of CrossHair marker"
field407.name = "markerColor"
field407.type = "SFColor"
ExternProtoDeclare404.addField([field407])

field408 = field()
field408.accessType = "inputOutput"
field408.appinfo = "size of CrossHair in meters"
field408.name = "scale"
field408.type = "SFVec3f"
ExternProtoDeclare404.addField([field408])

field409 = field()
field409.accessType = "inputOutput"
field409.appinfo = "distance in front of HUD viewpoint"
field409.name = "positionOffsetFromCamera"
field409.type = "SFVec3f"
ExternProtoDeclare404.addField([field409])
Scene21.addChildren([ExternProtoDeclare404])

ProtoInstance410 = ProtoInstance()
ProtoInstance410.DEF = "CrossHairInstance"
ProtoInstance410.name = "CrossHair"

fieldValue411 = fieldValue()
fieldValue411.name = "enabled"
fieldValue411.value = "true"
ProtoInstance410.addFieldValue([fieldValue411])

fieldValue412 = fieldValue()
fieldValue412.name = "markerColor"
fieldValue412.value = "1 0.5 0"
ProtoInstance410.addFieldValue([fieldValue412])

fieldValue413 = fieldValue()
fieldValue413.name = "scale"
fieldValue413.value = "1 1 1"
ProtoInstance410.addFieldValue([fieldValue413])

fieldValue414 = fieldValue()
fieldValue414.name = "positionOffsetFromCamera"
fieldValue414.value = "0 0 -6"
ProtoInstance410.addFieldValue([fieldValue414])
Scene21.addChildren([ProtoInstance410])
# turn on CrossHairInstance when animated camera viewpoints are bound 

ROUTE415 = ROUTE()
ROUTE415.fromField = "isBound"
ROUTE415.fromNode = "Camera.SimpleShotsTest"
ROUTE415.toField = "set_enabled"
ROUTE415.toNode = "CrossHairInstance"
Scene21.addChildren([ROUTE415])

ROUTE416 = ROUTE()
ROUTE416.fromField = "isBound"
ROUTE416.fromNode = "Camera.AimPointTest"
ROUTE416.toField = "set_enabled"
ROUTE416.toNode = "CrossHairInstance"
Scene21.addChildren([ROUTE416])
# turn off CrossHairInstance when animated camera viewpoints are unbound <BooleanFilter DEF='NegateCrossHair'/> <ROUTE fromField='isBound' fromNode='Camera.SimpleShotsTest' toField='set_boolean' toNode='NegateCrossHair'/> <ROUTE fromField='isBound' fromNode='Camera.AimPointTest' toField='set_boolean' toNode='NegateCrossHair'/> <ROUTE fromField='inputNegate' fromNode='NegateCrossHair' toField='set_enabled' toNode='CrossHairInstance'/> 
# =============== TODO Launch Prototype Example ============== 

Anchor417 = Anchor()
Anchor417.description = "launch CameraExample scene"
Anchor417.parameter = ["target=_blank"]
Anchor417.url = ["CameraExample.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExample.x3d","CameraExample.wrl","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExample.wrl"]

Transform418 = Transform()
Transform418.translation = [0,-3,0]

Shape419 = Shape()

Text420 = Text()
Text420.string = ["CameraPrototype","defines a prototype","","Click on this text to see","CameraExample scene"]

FontStyle421 = FontStyle(justify = ["MIDDLE","MIDDLE"], size = 0.5)
Text420.fontStyle = FontStyle421
Shape419.geometry = Text420

Appearance422 = Appearance()

Material423 = Material()
Material423.diffuseColor = [1,1,0.2]
Appearance422.material = Material423
Shape419.appearance = Appearance422
Transform418.addChildren([Shape419])
Anchor417.addChildren([Transform418])
Scene21.addChildren([Anchor417])
X3D0.scene = Scene21
