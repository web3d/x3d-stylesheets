from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.content = "ArchPrototype.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js."
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Possibility to create shapes related to arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information."
meta4.name = "description"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "Michele Foti, Don Brutzman"
meta5.name = "creator"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "15 December 2014"
meta6.name = "created"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "27 November 2015"
meta7.name = "modified"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "ArchModelingDiagrams.pdf"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "https://en.wikipedia.org/wiki/Arch"
meta9.name = "reference"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "http://X3dGraphics.com/examples/X3dForAdvancedModeling/Buildings/ArchPrototype.x3d"
meta10.name = "identifier"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta11.name = "generator"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "../license.html"
meta12.name = "license"
head1.addMeta([meta12])
X3D0.head = head1

Scene13 = Scene()

ProtoDeclare14 = ProtoDeclare()
ProtoDeclare14.appinfo = "Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. - Possibility to create shapes related to an arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.js."
ProtoDeclare14.name = "ArchPrototype"

ProtoInterface15 = ProtoInterface()
# COLOR OF ARCH 

field16 = field()
field16.accessType = "inputOutput"
field16.appinfo = "color of arch"
field16.name = "diffuseColor"
field16.type = "SFColor"
field16.value = "0.2 0.8 0.8"
ProtoInterface15.addField([field16])

field17 = field()
field17.accessType = "inputOutput"
field17.appinfo = "color of arch"
field17.name = "emissiveColor"
field17.type = "SFColor"
field17.value = "0.2 0.8 0.8"
ProtoInterface15.addField([field17])
# INPUT PARAMETERS 
# General parameters: measures in meters 

field18 = field()
field18.accessType = "initializeOnly"
field18.appinfo = "clearSpanWidth: clearSpanWidth must be double of riseHeight to obtain an half circumference"
field18.name = "clearSpanWidth"
field18.type = "SFFloat"
field18.value = "4"
ProtoInterface15.addField([field18])

field19 = field()
field19.accessType = "initializeOnly"
field19.appinfo = "riseHeight: riseHeight must be half of clearSpanWidth to obtain an half circumference"
field19.name = "riseHeight"
field19.type = "SFFloat"
field19.value = "2"
ProtoInterface15.addField([field19])

field20 = field()
field20.accessType = "initializeOnly"
field20.appinfo = "depth"
field20.name = "depth"
field20.type = "SFFloat"
field20.value = "3"
ProtoInterface15.addField([field20])

field21 = field()
field21.accessType = "initializeOnly"
field21.appinfo = "topAbutmentHeight:topAbutmentHeight=0 means no topAbutment"
field21.name = "topAbutmentHeight"
field21.type = "SFFloat"
field21.value = "0.5"
ProtoInterface15.addField([field21])

field22 = field()
field22.accessType = "initializeOnly"
field22.appinfo = "pierWidth:pierWidtht=0 means no pierWidth"
field22.name = "pierWidth"
field22.type = "SFFloat"
field22.value = "0.5"
ProtoInterface15.addField([field22])

field23 = field()
field23.accessType = "initializeOnly"
field23.appinfo = "pierHeight: pierHeight=0 means no pierHeight"
field23.name = "pierHeight"
field23.type = "SFFloat"
field23.value = "1"
ProtoInterface15.addField([field23])
# Parameters to create to create shapes related to arch: put true to apply 

field24 = field()
field24.accessType = "initializeOnly"
field24.appinfo = "archHalf: can modify also clearSpanWidth, riseHeight, depth, pierWidth, pierHeight, topAbutmentHeight, archHalfExtensionWidth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalf width"
field24.name = "archHalf"
field24.type = "SFBool"
field24.value = "false"
ProtoInterface15.addField([field24])

field25 = field()
field25.accessType = "initializeOnly"
field25.appinfo = "archHalfExtensionWidth: measure in meters, use only if archHalf=true, it is the width of the etension of the abutment of the archHalf. See the reference file ArchModelingDiagrams.pdf to find further information."
field25.name = "archHalfExtensionWidth"
field25.type = "SFFloat"
field25.value = "0"
ProtoInterface15.addField([field25])

field26 = field()
field26.accessType = "initializeOnly"
field26.appinfo = "onlyIntrados: note it is a flat curved surface, can modify also clearSpanWidth, riseHeight, depth at purpose, if needed apply archHalf=true."
field26.name = "onlyIntrados"
field26.type = "SFBool"
field26.value = "false"
ProtoInterface15.addField([field26])

field27 = field()
field27.accessType = "initializeOnly"
field27.appinfo = "archFilled: note it is an half cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose."
field27.name = "archFilled"
field27.type = "SFBool"
field27.value = "false"
ProtoInterface15.addField([field27])

field28 = field()
field28.accessType = "initializeOnly"
field28.appinfo = "archHalfFilled: note it is a quarter cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalfFilled width."
field28.name = "archHalfFilled"
field28.type = "SFBool"
field28.value = "false"
ProtoInterface15.addField([field28])

field29 = field()
field29.accessType = "initializeOnly"
field29.appinfo = "lintel: no arc is rendered, but a lintel: topAbutmentHeight on pierHeight, total height is pierHeight + topAbutmentHeight, if needed apply archHalf=true."
field29.name = "lintel"
field29.type = "SFBool"
field29.value = "false"
ProtoInterface15.addField([field29])
ProtoDeclare14.protoInterface = ProtoInterface15

ProtoBody30 = ProtoBody()
# First node determines node type of this prototype 
# IndexedFaceset creates arch 

Transform31 = Transform()
Transform31.DEF = "ArchTransform"

Shape32 = Shape()
Shape32.DEF = "Arch"
# note that convex='false' (meaning concave geometry) is crucial for this IFS of a geometric chord to render properly 

IndexedFaceSet33 = IndexedFaceSet(convex = False, creaseAngle = 0, solid = False)
IndexedFaceSet33.DEF = "ArchIndex"

Coordinate34 = Coordinate()
Coordinate34.DEF = "ArchChord"
IndexedFaceSet33.coord = Coordinate34
Shape32.geometry = IndexedFaceSet33

Appearance35 = Appearance()

Material36 = Material()
Material36.DEF = "MaterialNode"

IS37 = IS()

connect38 = connect()
connect38.nodeField = "emissiveColor"
connect38.protoField = "emissiveColor"
IS37.addConnect([connect38])

connect39 = connect()
connect39.nodeField = "diffuseColor"
connect39.protoField = "diffuseColor"
IS37.addConnect([connect39])
Material36.IS = IS37
Appearance35.material = Material36
Shape32.appearance = Appearance35
Transform31.addChildren([Shape32])
ProtoBody30.addChildren([Transform31])
# Subsequent nodes do not render, but still must be a valid X3D subgraph 
# This embedded Script provides the X3D author with additional visibility and control over prototype inputs and outputs 

Script40 = Script()
Script40.DEF = "ArchPrototypeScript"
Script40.url = ["../node/ArchPrototypeScript.js"]
# INPUT PARAMETERS 
# General parameters 
# Parameters to create to create shapes related to arch: put true to apply 
# OUTPUT PARAMETERS 

field41 = field()
field41.accessType = "initializeOnly"
field41.appinfo = "user or default input for clearSpanWidth parameter"
field41.name = "clearSpanWidth"
field41.type = "SFFloat"
Script40.addField([field41])

field42 = field()
field42.accessType = "initializeOnly"
field42.appinfo = "user or default input for riseHeight parameter"
field42.name = "riseHeight"
field42.type = "SFFloat"
Script40.addField([field42])

field43 = field()
field43.accessType = "initializeOnly"
field43.appinfo = "user or default input for depth parameter"
field43.name = "depth"
field43.type = "SFFloat"
Script40.addField([field43])

field44 = field()
field44.accessType = "initializeOnly"
field44.appinfo = "user or default input for topAbutmentHeight parameter"
field44.name = "topAbutmentHeight"
field44.type = "SFFloat"
Script40.addField([field44])

field45 = field()
field45.accessType = "initializeOnly"
field45.appinfo = "user or default input for pierWidth parameter"
field45.name = "pierWidth"
field45.type = "SFFloat"
Script40.addField([field45])

field46 = field()
field46.accessType = "initializeOnly"
field46.appinfo = "user or default input for pierHeight parameter"
field46.name = "pierHeight"
field46.type = "SFFloat"
Script40.addField([field46])

field47 = field()
field47.accessType = "initializeOnly"
field47.appinfo = "user or default input for archHalf parameter"
field47.name = "archHalf"
field47.type = "SFBool"
Script40.addField([field47])

field48 = field()
field48.accessType = "initializeOnly"
field48.appinfo = "user or default input for archHalfExtensionWidth parameter"
field48.name = "archHalfExtensionWidth"
field48.type = "SFFloat"
Script40.addField([field48])

field49 = field()
field49.accessType = "initializeOnly"
field49.appinfo = "user or default input for onlyIntrados parameter"
field49.name = "onlyIntrados"
field49.type = "SFBool"
Script40.addField([field49])

field50 = field()
field50.accessType = "initializeOnly"
field50.appinfo = "user or default input for archFilled parameter"
field50.name = "archFilled"
field50.type = "SFBool"
Script40.addField([field50])

field51 = field()
field51.accessType = "initializeOnly"
field51.appinfo = "user or default input for archHalfFilled parameter"
field51.name = "archHalfFilled"
field51.type = "SFBool"
Script40.addField([field51])

field52 = field()
field52.accessType = "initializeOnly"
field52.appinfo = "user or default input for lintel parameter"
field52.name = "lintel"
field52.type = "SFBool"
Script40.addField([field52])

field53 = field()
field53.accessType = "outputOnly"
field53.appinfo = "computedScale: modify scale field - NOTE it is not used to modify the whole arch, but to modify clearSpanWidth, riseHeight, depth. It does not affect topAbutmentHeight, pierWidth, pierHeight, archHalfExtensionWidth"
field53.name = "computedScale"
field53.type = "SFVec3f"
Script40.addField([field53])

field54 = field()
field54.accessType = "outputOnly"
field54.appinfo = "send computed points to the Coordinate node"
field54.name = "pointOut"
field54.type = "MFVec3f"
Script40.addField([field54])

field55 = field()
field55.accessType = "outputOnly"
field55.appinfo = "send computed indices to the IndexedFaceSet node"
field55.name = "indexOut"
field55.type = "MFInt32"
Script40.addField([field55])

IS56 = IS()

connect57 = connect()
connect57.nodeField = "clearSpanWidth"
connect57.protoField = "clearSpanWidth"
IS56.addConnect([connect57])

connect58 = connect()
connect58.nodeField = "riseHeight"
connect58.protoField = "riseHeight"
IS56.addConnect([connect58])

connect59 = connect()
connect59.nodeField = "depth"
connect59.protoField = "depth"
IS56.addConnect([connect59])

connect60 = connect()
connect60.nodeField = "pierWidth"
connect60.protoField = "pierWidth"
IS56.addConnect([connect60])

connect61 = connect()
connect61.nodeField = "topAbutmentHeight"
connect61.protoField = "topAbutmentHeight"
IS56.addConnect([connect61])

connect62 = connect()
connect62.nodeField = "pierHeight"
connect62.protoField = "pierHeight"
IS56.addConnect([connect62])

connect63 = connect()
connect63.nodeField = "archHalf"
connect63.protoField = "archHalf"
IS56.addConnect([connect63])

connect64 = connect()
connect64.nodeField = "archHalfExtensionWidth"
connect64.protoField = "archHalfExtensionWidth"
IS56.addConnect([connect64])

connect65 = connect()
connect65.nodeField = "onlyIntrados"
connect65.protoField = "onlyIntrados"
IS56.addConnect([connect65])

connect66 = connect()
connect66.nodeField = "archFilled"
connect66.protoField = "archFilled"
IS56.addConnect([connect66])

connect67 = connect()
connect67.nodeField = "archHalfFilled"
connect67.protoField = "archHalfFilled"
IS56.addConnect([connect67])

connect68 = connect()
connect68.nodeField = "lintel"
connect68.protoField = "lintel"
IS56.addConnect([connect68])
Script40.IS = IS56
ProtoBody30.addChildren([Script40])

ROUTE69 = ROUTE()
ROUTE69.fromField = "computedScale"
ROUTE69.fromNode = "ArchPrototypeScript"
ROUTE69.toField = "scale"
ROUTE69.toNode = "ArchTransform"
ProtoBody30.addChildren([ROUTE69])

ROUTE70 = ROUTE()
ROUTE70.fromField = "pointOut"
ROUTE70.fromNode = "ArchPrototypeScript"
ROUTE70.toField = "point"
ROUTE70.toNode = "ArchChord"
ProtoBody30.addChildren([ROUTE70])

ROUTE71 = ROUTE()
ROUTE71.fromField = "indexOut"
ROUTE71.fromNode = "ArchPrototypeScript"
ROUTE71.toField = "set_coordIndex"
ROUTE71.toNode = "ArchIndex"
ProtoBody30.addChildren([ROUTE71])
ProtoDeclare14.protoBody = ProtoBody30
Scene13.addChildren([ProtoDeclare14])

ProtoInstance72 = ProtoInstance()
ProtoInstance72.DEF = "ArchInstance"
ProtoInstance72.name = "ArchPrototype"

fieldValue73 = fieldValue()
fieldValue73.name = "diffuseColor"
fieldValue73.value = "0.5 0.3 0.6"
ProtoInstance72.addFieldValue([fieldValue73])

fieldValue74 = fieldValue()
fieldValue74.name = "emissiveColor"
fieldValue74.value = "0.5 0.3 0.6"
ProtoInstance72.addFieldValue([fieldValue74])

fieldValue75 = fieldValue()
fieldValue75.name = "clearSpanWidth"
fieldValue75.value = "5"
ProtoInstance72.addFieldValue([fieldValue75])

fieldValue76 = fieldValue()
fieldValue76.name = "riseHeight"
fieldValue76.value = "2.5"
ProtoInstance72.addFieldValue([fieldValue76])

fieldValue77 = fieldValue()
fieldValue77.name = "depth"
fieldValue77.value = "2"
ProtoInstance72.addFieldValue([fieldValue77])

fieldValue78 = fieldValue()
fieldValue78.name = "topAbutmentHeight"
fieldValue78.value = "0.6"
ProtoInstance72.addFieldValue([fieldValue78])

fieldValue79 = fieldValue()
fieldValue79.name = "pierWidth"
fieldValue79.value = "1"
ProtoInstance72.addFieldValue([fieldValue79])

fieldValue80 = fieldValue()
fieldValue80.name = "pierHeight"
fieldValue80.value = "2"
ProtoInstance72.addFieldValue([fieldValue80])
Scene13.addChildren([ProtoInstance72])
# Add any ROUTEs here that connect ProtoInstance to/from prior nodes in Scene (and outside of ProtoDeclare) 

Inline81 = Inline()
Inline81.DEF = "CoordinateAxes"
Inline81.url = ["../data/CoordinateAxes.x3d"]
Scene13.addChildren([Inline81])
X3D0.scene = Scene13
