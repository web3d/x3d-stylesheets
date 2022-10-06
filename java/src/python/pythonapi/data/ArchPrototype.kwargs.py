from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(content="ArchPrototype.x3d", name="title"), 
    meta3 = meta(content="Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.", name="description"), 
    meta4 = meta(content="Possibility to create shapes related to arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information.", name="description"), 
    meta5 = meta(content="Michele Foti, Don Brutzman", name="creator"), 
    meta6 = meta(content="15 December 2014", name="created"), 
    meta7 = meta(content="27 November 2015", name="modified"), 
    meta8 = meta(content="ArchModelingDiagrams.pdf", name="reference"), 
    meta9 = meta(content="https://en.wikipedia.org/wiki/Arch", name="reference"), 
    meta10 = meta(content="http://X3dGraphics.com/examples/X3dForAdvancedModeling/Buildings/ArchPrototype.x3d", name="identifier"), 
    meta11 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta12 = meta(content="../license.html", name="license")), 
   Scene13 = Scene(    ProtoDeclare14 = ProtoDeclare(appinfo="Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. - Possibility to create shapes related to an arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.js.", name="ArchPrototype",      ProtoInterface15 = ProtoInterface(      # COLOR OF ARCH 

      field16 = field(accessType="inputOutput", appinfo="color of arch", name="diffuseColor", type="SFColor", value="0.2 0.8 0.8"), 
      field17 = field(accessType="inputOutput", appinfo="color of arch", name="emissiveColor", type="SFColor", value="0.2 0.8 0.8"),       # INPUT PARAMETERS 
      # General parameters: measures in meters 

      field18 = field(accessType="initializeOnly", appinfo="clearSpanWidth: clearSpanWidth must be double of riseHeight to obtain an half circumference", name="clearSpanWidth", type="SFFloat", value="4"), 
      field19 = field(accessType="initializeOnly", appinfo="riseHeight: riseHeight must be half of clearSpanWidth to obtain an half circumference", name="riseHeight", type="SFFloat", value="2"), 
      field20 = field(accessType="initializeOnly", appinfo="depth", name="depth", type="SFFloat", value="3"), 
      field21 = field(accessType="initializeOnly", appinfo="topAbutmentHeight:topAbutmentHeight=0 means no topAbutment", name="topAbutmentHeight", type="SFFloat", value="0.5"), 
      field22 = field(accessType="initializeOnly", appinfo="pierWidth:pierWidtht=0 means no pierWidth", name="pierWidth", type="SFFloat", value="0.5"), 
      field23 = field(accessType="initializeOnly", appinfo="pierHeight: pierHeight=0 means no pierHeight", name="pierHeight", type="SFFloat", value="1"),       # Parameters to create to create shapes related to arch: put true to apply 

      field24 = field(accessType="initializeOnly", appinfo="archHalf: can modify also clearSpanWidth, riseHeight, depth, pierWidth, pierHeight, topAbutmentHeight, archHalfExtensionWidth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalf width", name="archHalf", type="SFBool", value="false"), 
      field25 = field(accessType="initializeOnly", appinfo="archHalfExtensionWidth: measure in meters, use only if archHalf=true, it is the width of the etension of the abutment of the archHalf. See the reference file ArchModelingDiagrams.pdf to find further information.", name="archHalfExtensionWidth", type="SFFloat", value="0"), 
      field26 = field(accessType="initializeOnly", appinfo="onlyIntrados: note it is a flat curved surface, can modify also clearSpanWidth, riseHeight, depth at purpose, if needed apply archHalf=true.", name="onlyIntrados", type="SFBool", value="false"), 
      field27 = field(accessType="initializeOnly", appinfo="archFilled: note it is an half cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose.", name="archFilled", type="SFBool", value="false"), 
      field28 = field(accessType="initializeOnly", appinfo="archHalfFilled: note it is a quarter cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalfFilled width.", name="archHalfFilled", type="SFBool", value="false"), 
      field29 = field(accessType="initializeOnly", appinfo="lintel: no arc is rendered, but a lintel: topAbutmentHeight on pierHeight, total height is pierHeight + topAbutmentHeight, if needed apply archHalf=true.", name="lintel", type="SFBool", value="false")), 
     ProtoBody30 = ProtoBody(      # First node determines node type of this prototype 
      # IndexedFaceset creates arch 

      Transform31 = Transform(DEF="ArchTransform",        Shape32 = Shape(DEF="Arch",         # note that convex='false' (meaning concave geometry) is crucial for this IFS of a geometric chord to render properly 

        IndexedFaceSet33 = IndexedFaceSet(DEF="ArchIndex", convex=False, creaseAngle=0, solid=False,          Coordinate34 = Coordinate(DEF="ArchChord")), 
        Appearance35 = Appearance(         Material36 = Material(DEF="MaterialNode",           IS37 = IS(           connect38 = connect(nodeField="emissiveColor", protoField="emissiveColor"), 
           connect39 = connect(nodeField="diffuseColor", protoField="diffuseColor")))))),       # Subsequent nodes do not render, but still must be a valid X3D subgraph 
      # This embedded Script provides the X3D author with additional visibility and control over prototype inputs and outputs 

      Script40 = Script(DEF="ArchPrototypeScript", url=["../node/ArchPrototypeScript.js"],        # INPUT PARAMETERS 
       # General parameters 
       # Parameters to create to create shapes related to arch: put true to apply 
       # OUTPUT PARAMETERS 

       field41 = field(accessType="initializeOnly", appinfo="user or default input for clearSpanWidth parameter", name="clearSpanWidth", type="SFFloat"), 
       field42 = field(accessType="initializeOnly", appinfo="user or default input for riseHeight parameter", name="riseHeight", type="SFFloat"), 
       field43 = field(accessType="initializeOnly", appinfo="user or default input for depth parameter", name="depth", type="SFFloat"), 
       field44 = field(accessType="initializeOnly", appinfo="user or default input for topAbutmentHeight parameter", name="topAbutmentHeight", type="SFFloat"), 
       field45 = field(accessType="initializeOnly", appinfo="user or default input for pierWidth parameter", name="pierWidth", type="SFFloat"), 
       field46 = field(accessType="initializeOnly", appinfo="user or default input for pierHeight parameter", name="pierHeight", type="SFFloat"), 
       field47 = field(accessType="initializeOnly", appinfo="user or default input for archHalf parameter", name="archHalf", type="SFBool"), 
       field48 = field(accessType="initializeOnly", appinfo="user or default input for archHalfExtensionWidth parameter", name="archHalfExtensionWidth", type="SFFloat"), 
       field49 = field(accessType="initializeOnly", appinfo="user or default input for onlyIntrados parameter", name="onlyIntrados", type="SFBool"), 
       field50 = field(accessType="initializeOnly", appinfo="user or default input for archFilled parameter", name="archFilled", type="SFBool"), 
       field51 = field(accessType="initializeOnly", appinfo="user or default input for archHalfFilled parameter", name="archHalfFilled", type="SFBool"), 
       field52 = field(accessType="initializeOnly", appinfo="user or default input for lintel parameter", name="lintel", type="SFBool"), 
       field53 = field(accessType="outputOnly", appinfo="computedScale: modify scale field - NOTE it is not used to modify the whole arch, but to modify clearSpanWidth, riseHeight, depth. It does not affect topAbutmentHeight, pierWidth, pierHeight, archHalfExtensionWidth", name="computedScale", type="SFVec3f"), 
       field54 = field(accessType="outputOnly", appinfo="send computed points to the Coordinate node", name="pointOut", type="MFVec3f"), 
       field55 = field(accessType="outputOnly", appinfo="send computed indices to the IndexedFaceSet node", name="indexOut", type="MFInt32"), 
       IS56 = IS(        connect57 = connect(nodeField="clearSpanWidth", protoField="clearSpanWidth"), 
        connect58 = connect(nodeField="riseHeight", protoField="riseHeight"), 
        connect59 = connect(nodeField="depth", protoField="depth"), 
        connect60 = connect(nodeField="pierWidth", protoField="pierWidth"), 
        connect61 = connect(nodeField="topAbutmentHeight", protoField="topAbutmentHeight"), 
        connect62 = connect(nodeField="pierHeight", protoField="pierHeight"), 
        connect63 = connect(nodeField="archHalf", protoField="archHalf"), 
        connect64 = connect(nodeField="archHalfExtensionWidth", protoField="archHalfExtensionWidth"), 
        connect65 = connect(nodeField="onlyIntrados", protoField="onlyIntrados"), 
        connect66 = connect(nodeField="archFilled", protoField="archFilled"), 
        connect67 = connect(nodeField="archHalfFilled", protoField="archHalfFilled"), 
        connect68 = connect(nodeField="lintel", protoField="lintel"))), 
      ROUTE69 = ROUTE(fromField="computedScale", fromNode="ArchPrototypeScript", toField="scale", toNode="ArchTransform"), 
      ROUTE70 = ROUTE(fromField="pointOut", fromNode="ArchPrototypeScript", toField="point", toNode="ArchChord"), 
      ROUTE71 = ROUTE(fromField="indexOut", fromNode="ArchPrototypeScript", toField="set_coordIndex", toNode="ArchIndex"))), 
    ProtoInstance72 = ProtoInstance(DEF="ArchInstance", name="ArchPrototype",      fieldValue73 = fieldValue(name="diffuseColor", value="0.5 0.3 0.6"), 
     fieldValue74 = fieldValue(name="emissiveColor", value="0.5 0.3 0.6"), 
     fieldValue75 = fieldValue(name="clearSpanWidth", value="5"), 
     fieldValue76 = fieldValue(name="riseHeight", value="2.5"), 
     fieldValue77 = fieldValue(name="depth", value="2"), 
     fieldValue78 = fieldValue(name="topAbutmentHeight", value="0.6"), 
     fieldValue79 = fieldValue(name="pierWidth", value="1"), 
     fieldValue80 = fieldValue(name="pierHeight", value="2")),     # Add any ROUTEs here that connect ProtoInstance to/from prior nodes in Scene (and outside of ProtoDeclare) 

    Inline81 = Inline(DEF="CoordinateAxes", url=["../data/CoordinateAxes.x3d"])))
