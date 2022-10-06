from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(content="StringArrayEncodingExamples.x3d", name="title"), 
    meta3 = meta(content="Demonstrate simple X3D MFString (string array) encoding.", name="description"), 
    meta4 = meta(content="27 May 2017", name="created"), 
    meta5 = meta(content="27 May 2017", name="modified"), 
    meta6 = meta(content="Don Brutzman", name="creator"), 
    meta7 = meta(content="X3dHeaderPrototypeSyntaxExamples.x3d", name="reference"), 
    meta8 = meta(content="X3D encodings, ISO/IEC 19775-1, Part 1: Architecture and base components, 5 Field type reference, 5.3.14 SFString and MFString", name="specificationSection"), 
    meta9 = meta(content="http://www.web3d.org/documents/specifications/19775-1/V3.3/Part01/fieldsDef.html#SFStringAndMFString", name="specificationUrl"), 
    meta10 = meta(content="X3D encodings, ISO/IEC 19776-1.3, Part 1: XML encoding, 5.3.14 SFString and MFString", name="specificationSection"), 
    meta11 = meta(content="http://www.web3d.org/documents/specifications/19776-1/V3.3/Part01/EncodingOfFields.html#SFString", name="specificationUrl"), 
    meta12 = meta(content="X3D encodings, ISO/IEC 19776-2 v3.3, Part 2: Classic VRML encoding, 5.15 SFString and MFString", name="specificationSection"), 
    meta13 = meta(content="http://www.web3d.org/documents/specifications/19776-2/V3.3/Part02/EncodingOfFields.html#SFString", name="specificationUrl"), 
    meta14 = meta(content="http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamples.x3d", name="identifier"), 
    meta15 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta16 = meta(content="../license.html", name="license")), 
   Scene17 = Scene(    Viewpoint18 = Viewpoint(DEF="EntryView", description="Hello MFString syntax"), 
    Background19 = Background(skyColor=[0.6,1,0.8]), 
    Shape20 = Shape(     Text21 = Text(string=["One, Two, Three","","He said, \"Immel did it!\""],       # alternative XML encoding: Text string='\"One, Two, Three\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 
      # alternative Java source: .setString(new String [] {\"One, Two, Three\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 

      FontStyle22 = FontStyle(justify=["MIDDLE","MIDDLE"], style="BOLD")), 
     Appearance23 = Appearance(      Material24 = Material(diffuseColor=[0.6,0.4,0.2])))))
