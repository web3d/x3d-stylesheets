from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.content = "ObliqueStrategies.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Text scripting and animation example using Oblique Strategies card set by Brian Eno."
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Don Brutzman, John Kelly, Ben Cheng"
meta4.name = "creator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "3 November 2013"
meta5.name = "created"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "18 October 2015"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "oblique.html"
meta7.name = "reference"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "ObliqueStrategies.txt"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "ObliqueStrategiesScript.js"
meta9.name = "reference"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "http://music.hyperreal.org/artists/brian_eno/oblique/oblique.html"
meta10.name = "reference"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "http://www.eno-web.co.uk/obliques.html"
meta11.name = "reference"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "http://gothpunk.com/haiku-intro.html"
meta12.name = "reference"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "http://www.rtqe.net/ObliqueStrategies/OSintro.html"
meta13.name = "reference"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "https://en.wikipedia.org/wiki/Oblique_Strategies"
meta14.name = "reference"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "Brian Eno, Oblique Strategies"
meta15.name = "subject"
head1.addMeta([meta15])

meta16 = meta()
meta16.content = "images/ObliqueStrategiesEntryScreen.png"
meta16.name = "Image"
head1.addMeta([meta16])

meta17 = meta()
meta17.content = "http://translate.google.com/translate_tts?tl=en&q=hello%20X3D"
meta17.name = "audio"
head1.addMeta([meta17])

meta18 = meta()
meta18.content = "translate_tts_HelloX3D.mp3"
meta18.name = "audio"
head1.addMeta([meta18])

meta19 = meta()
meta19.content = "translate_tts_HelloX3D.wav"
meta19.name = "audio"
head1.addMeta([meta19])

meta20 = meta()
meta20.content = "multiliingual translation parameter"
meta20.name = "TODO"
head1.addMeta([meta20])

meta21 = meta()
meta21.content = "http://stackoverflow.com/questions/9163988/download-mp3-from-google-translate-text-to-speech"
meta21.name = "reference"
head1.addMeta([meta21])

meta22 = meta()
meta22.content = "http://www.greenbot.com/article/2105862/how-to-get-started-with-google-text-to-speech.html"
meta22.name = "reference"
head1.addMeta([meta22])

meta23 = meta()
meta23.content = "under development, scene Sound/AudioClip triggering (or retrieved file format) not working"
meta23.name = "warning"
head1.addMeta([meta23])

meta24 = meta()
meta24.content = "BSContact error: Script node TextScript: parse error: line 15 \" var strategy = [];"
meta24.name = "warning"
head1.addMeta([meta24])

meta25 = meta()
meta25.content = "http://X3dGraphics.com/examples/X3dForAdvancedModeling/Inspiration/ObliqueStrategies.x3d"
meta25.name = "identifier"
head1.addMeta([meta25])

meta26 = meta()
meta26.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta26.name = "generator"
head1.addMeta([meta26])

meta27 = meta()
meta27.content = "../license.html"
meta27.name = "license"
head1.addMeta([meta27])
X3D0.head = head1

Scene28 = Scene()

NavigationInfo29 = NavigationInfo()
NavigationInfo29.type = ["EXAMINE","ANY"]
Scene28.addChildren([NavigationInfo29])

Background30 = Background()
Background30.skyColor = [0.419608,0.427451,1]
Scene28.addChildren([Background30])

Transform31 = Transform()
Transform31.scale = [0.4,0.4,0.4]
Transform31.translation = [0,1,0]

TouchSensor32 = TouchSensor()
TouchSensor32.DEF = "RandomTextClickedSensor"
TouchSensor32.description = "Select to see a new strategy"
Transform31.addChildren([TouchSensor32])

Shape33 = Shape()

Text34 = Text()
Text34.string = ["Oblique Strategies","","(Over One Hundred Worthwhile Dilemmas)","","by Brian Eno and Peter Schmidt"]

FontStyle35 = FontStyle(family = ["SANS"], justify = ["MIDDLE","MIDDLE"], style = "BOLD")
FontStyle35.DEF = "MessageFont"
Text34.fontStyle = FontStyle35
Shape33.geometry = Text34

Appearance36 = Appearance()

Material37 = Material()
Material37.diffuseColor = [1,1,1]
Appearance36.material = Material37
Shape33.appearance = Appearance36
Transform31.addChildren([Shape33])

Transform38 = Transform()
Transform38.scale = [10,3,1]

Shape39 = Shape()
Shape39.DEF = "HeadlineClickSurface"

IndexedFaceSet40 = IndexedFaceSet(coordIndex = [0,1,2,3,-1], solid = False)

Coordinate41 = Coordinate()
Coordinate41.point = [1,1,0,1,-1,0,-1,-1,0,-1,1,0]
IndexedFaceSet40.coord = Coordinate41
Shape39.geometry = IndexedFaceSet40

Appearance42 = Appearance()

Material43 = Material()
Material43.ambientIntensity = 0.245763
Material43.diffuseColor = [0.34773,0.090909,0.005289]
Material43.shininess = 0.07
Material43.specularColor = [0.336735,0.051091,0.051091]
Material43.transparency = 0.8
Appearance42.material = Material43
Shape39.appearance = Appearance42
Transform38.addChildren([Shape39])
Transform31.addChildren([Transform38])
Scene28.addChildren([Transform31])

Script44 = Script()
Script44.DEF = "TextScript"
Script44.url = ["./ObliqueStrategiesScript.js"]
# initialize() method includes unit test to printAllStrategies() to console 
# TODO insert field definitions here (index string_changed previous next random) and then animate! 

field45 = field()
field45.accessType = "initializeOnly"
field45.appinfo = "index for active strategy card, -1 means no selection"
field45.name = "index"
field45.type = "SFInt32"
field45.value = "0"
Script44.addField([field45])

field46 = field()
field46.accessType = "outputOnly"
field46.appinfo = "latest strategy card value"
field46.name = "string_changed"
field46.type = "MFString"
Script44.addField([field46])

field47 = field()
field47.accessType = "outputOnly"
field47.appinfo = "url to invoke Google Translate"
field47.name = "textToSpeechUrl"
field47.type = "MFString"
Script44.addField([field47])

field48 = field()
field48.accessType = "outputOnly"
field48.appinfo = "activate Sound node"
field48.name = "newCardTime"
field48.type = "SFTime"
Script44.addField([field48])

field49 = field()
field49.accessType = "inputOnly"
field49.name = "selectPreviousCard"
field49.type = "SFBool"
Script44.addField([field49])

field50 = field()
field50.accessType = "inputOnly"
field50.name = "selectNextCard"
field50.type = "SFBool"
Script44.addField([field50])

field51 = field()
field51.accessType = "inputOnly"
field51.name = "selectRandomCard"
field51.type = "SFBool"
Script44.addField([field51])

field52 = field()
field52.accessType = "initializeOnly"
field52.appinfo = "controls console tracing"
field52.name = "traceEnabled"
field52.type = "SFBool"
field52.value = "true"
Script44.addField([field52])
Scene28.addChildren([Script44])

Transform53 = Transform()
Transform53.DEF = "CardTransform"
Transform53.scale = [0.4,0.4,0.4]
Transform53.translation = [0,-1.5,0]

Shape54 = Shape()

Text55 = Text()
Text55.DEF = "CardText"

FontStyle56 = FontStyle(family = ["SANS"], justify = ["MIDDLE","MIDDLE"], style = "BOLD")
Text55.fontStyle = FontStyle56
Shape54.geometry = Text55

Appearance57 = Appearance()

Material58 = Material()
Material58.diffuseColor = [1,1,1]
Appearance57.material = Material58
Shape54.appearance = Appearance57
Transform53.addChildren([Shape54])

ROUTE59 = ROUTE()
ROUTE59.fromField = "string_changed"
ROUTE59.fromNode = "TextScript"
ROUTE59.toField = "string"
ROUTE59.toNode = "CardText"
Transform53.addChildren([ROUTE59])

Sound60 = Sound()
Sound60.DEF = "CardSoundSpatialization"
Sound60.maxBack = 100
Sound60.maxFront = 100
Sound60.minBack = 20
Sound60.minFront = 20
# Make sure the sound source AudioClip is audible at the user location 
# Not all X3D players seem to use the .mp3 
# &#38; is ampersand character, avoids escaping problems and inconsistencies in browsers and X3D players 
# %20 is space character used in uri/url encoding 

AudioClip61 = AudioClip()
AudioClip61.DEF = "TextToSpeechAudioClip"
AudioClip61.description = "sends strategy text google translate"
AudioClip61.url = ["http://translate.google.com/translate_tts?tl=en&q=Feed%20the%20recording%20back%20out%20of%20the%20medium","translate_tts_mp3FileFormatNotSupported.wav"]
Sound60.source = AudioClip61
Transform53.addChildren([Sound60])

ROUTE62 = ROUTE()
ROUTE62.fromField = "textToSpeechUrl"
ROUTE62.fromNode = "TextScript"
ROUTE62.toField = "url"
ROUTE62.toNode = "TextToSpeechAudioClip"
Transform53.addChildren([ROUTE62])

ROUTE63 = ROUTE()
ROUTE63.fromField = "newCardTime"
ROUTE63.fromNode = "TextScript"
ROUTE63.toField = "startTime"
ROUTE63.toNode = "TextToSpeechAudioClip"
Transform53.addChildren([ROUTE63])
Scene28.addChildren([Transform53])

Transform64 = Transform()
Transform64.scale = [0.4,0.4,0.4]
Transform64.translation = [-3.2,2.5,0]

TouchSensor65 = TouchSensor()
TouchSensor65.DEF = "PreviousTextClickedSensor"
TouchSensor65.description = "Select to see previous strategy"
Transform64.addChildren([TouchSensor65])

ROUTE66 = ROUTE()
ROUTE66.fromField = "isActive"
ROUTE66.fromNode = "PreviousTextClickedSensor"
ROUTE66.toField = "selectPreviousCard"
ROUTE66.toNode = "TextScript"
Transform64.addChildren([ROUTE66])

Shape67 = Shape()

Text68 = Text()
Text68.string = ["previous"]

FontStyle69 = FontStyle()
FontStyle69.USE = "MessageFont"
Text68.fontStyle = FontStyle69
Shape67.geometry = Text68

Appearance70 = Appearance()
Appearance70.DEF = "InterfaceAppearance"

Material71 = Material()
Material71.diffuseColor = [1,0,0.6]
Appearance70.material = Material71
Shape67.appearance = Appearance70
Transform64.addChildren([Shape67])

Transform72 = Transform()
Transform72.scale = [2,0.6,1]

Shape73 = Shape()
Shape73.DEF = "TransparentClickSurface"
# support Selectable Text with a scalable IFS 

IndexedFaceSet74 = IndexedFaceSet(coordIndex = [0,1,2,3,-1], solid = False)

Coordinate75 = Coordinate()
Coordinate75.point = [1,1,0,1,-1,0,-1,-1,0,-1,1,0]
IndexedFaceSet74.coord = Coordinate75
Shape73.geometry = IndexedFaceSet74

Appearance76 = Appearance()

Material77 = Material()
Material77.transparency = 1
Appearance76.material = Material77
Shape73.appearance = Appearance76
Transform72.addChildren([Shape73])
Transform64.addChildren([Transform72])
Scene28.addChildren([Transform64])

Transform78 = Transform()
Transform78.scale = [0.4,0.4,0.4]
Transform78.translation = [3.5,2.5,0]

TouchSensor79 = TouchSensor()
TouchSensor79.DEF = "NextTextClickedSensor"
TouchSensor79.description = "Select to see next strategy"
Transform78.addChildren([TouchSensor79])

ROUTE80 = ROUTE()
ROUTE80.fromField = "isActive"
ROUTE80.fromNode = "NextTextClickedSensor"
ROUTE80.toField = "selectNextCard"
ROUTE80.toNode = "TextScript"
Transform78.addChildren([ROUTE80])

Shape81 = Shape()

Text82 = Text()
Text82.string = ["next"]

FontStyle83 = FontStyle()
FontStyle83.USE = "MessageFont"
Text82.fontStyle = FontStyle83
Shape81.geometry = Text82

Appearance84 = Appearance()
Appearance84.USE = "InterfaceAppearance"
Shape81.appearance = Appearance84
Transform78.addChildren([Shape81])

Transform85 = Transform()
Transform85.scale = [1.2,0.6,1]

Shape86 = Shape()
Shape86.USE = "TransparentClickSurface"
Transform85.addChildren([Shape86])
Transform78.addChildren([Transform85])
Scene28.addChildren([Transform78])

Transform87 = Transform()
Transform87.scale = [0.4,0.4,0.4]
Transform87.translation = [-3.3,-0.5,0]

TouchSensor88 = TouchSensor()
TouchSensor88.USE = "RandomTextClickedSensor"
Transform87.addChildren([TouchSensor88])

ROUTE89 = ROUTE()
ROUTE89.fromField = "isActive"
ROUTE89.fromNode = "RandomTextClickedSensor"
ROUTE89.toField = "selectRandomCard"
ROUTE89.toNode = "TextScript"
Transform87.addChildren([ROUTE89])

Shape90 = Shape()

Text91 = Text()
Text91.string = ["random"]

FontStyle92 = FontStyle()
FontStyle92.USE = "MessageFont"
Text91.fontStyle = FontStyle92
Shape90.geometry = Text91

Appearance93 = Appearance()
Appearance93.USE = "InterfaceAppearance"
Shape90.appearance = Appearance93
Transform87.addChildren([Shape90])

Transform94 = Transform()
Transform94.scale = [1.8,0.6,1]

Shape95 = Shape()
Shape95.USE = "TransparentClickSurface"
Transform94.addChildren([Shape95])
Transform87.addChildren([Transform94])
Scene28.addChildren([Transform87])

Transform96 = Transform()
Transform96.scale = [0.4,0.4,0.4]
Transform96.translation = [3.3,-0.5,0]

Anchor97 = Anchor()
Anchor97.DEF = "TextToSpeechAnchor"
Anchor97.description = "text to speech in browser"
Anchor97.parameter = ["target=_blank"]
Anchor97.url = ["http://translate.google.com/translate_tts?tl=en&q=Overtly%20resist%20change"]

ROUTE98 = ROUTE()
ROUTE98.fromField = "textToSpeechUrl"
ROUTE98.fromNode = "TextScript"
ROUTE98.toField = "url"
ROUTE98.toNode = "TextToSpeechAnchor"
Anchor97.addChildren([ROUTE98])

Shape99 = Shape()

Text100 = Text()
Text100.string = ["speech"]

FontStyle101 = FontStyle()
FontStyle101.USE = "MessageFont"
Text100.fontStyle = FontStyle101
Shape99.geometry = Text100

Appearance102 = Appearance()
Appearance102.USE = "InterfaceAppearance"
Shape99.appearance = Appearance102
Anchor97.addChildren([Shape99])

Transform103 = Transform()
Transform103.scale = [1.8,0.6,1]

Shape104 = Shape()
Shape104.USE = "TransparentClickSurface"
Transform103.addChildren([Shape104])
Anchor97.addChildren([Transform103])
Transform96.addChildren([Anchor97])
Scene28.addChildren([Transform96])
X3D0.scene = Scene28
