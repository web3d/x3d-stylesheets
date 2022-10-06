from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(content="TextSpecialCharacters.x3d", name="title"), 
    meta3 = meta(content="Text node demonstration of quotation, apostrophe, ampersand and backslash characters using X3D MFString escaping for XML character entities", name="description"), 
    meta4 = meta(content="Don Brutzman", name="creator"), 
    meta5 = meta(content="12 July 2008", name="created"), 
    meta6 = meta(content="2 April 2017", name="modified"), 
    meta7 = meta(content="Character entity references in HTML 4", name="reference"), 
    meta8 = meta(content="http://www.w3.org/TR/REC-html40/sgml/entities.html", name="reference"), 
    meta9 = meta(content="Copyright (c) Don Brutzman and Leonard Daly, 2008", name="rights"), 
    meta10 = meta(content="http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter02GeometryPrimitives/TextSpecialCharacters.x3d", name="identifier"), 
    meta11 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta12 = meta(content="../license.html", name="license")), 
   Scene13 = Scene(    Background14 = Background(skyColor=[1,1,1]), 
    Viewpoint15 = Viewpoint(description="Default View", position=[0,0,15]), 
    Shape16 = Shape(     # Empty string \"\" means to skip a line 
     # The ampersand escape characters are based on XML rules 
     # apostrophe ' is &apos; and needs to be escaped in single-quote delimiters used for string='value' attribute 
     # ampersand & is &amp; and needs to be escaped 
     # quotation \" is &quot; and isn't needed if single-quote delimiters used for string='value' attribute 
     # quotation \" can be used within an X3D string if escaped with backslash \\ as \\\" 
     # backslash \\ is used as escape character for \" (and itself) in X3D 
     # character entities are listed in HTML specification and are good for any XML 

     Text17 = Text(DEF="DefaultText", string=["Character entity substitutions:","empty string \"\" skips a line:","","apostrophe  '  is &apos;","ampersand & is &amp;","quote mark  \"  is &quot;","backslash \\\\ is X3D escape character","double backslash \\\\\\\\ is X3D backslash \\\\ character","Pi Π is &#928; XML character entity"],       FontStyle18 = FontStyle(DEF="CenteredFontStyle", justify=["MIDDLE","MIDDLE"])), 
     Appearance19 = Appearance(      Material20 = Material(DEF="DefaultMaterial", diffuseColor=[0.2,0.2,0.2])))))
