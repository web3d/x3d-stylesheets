from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.content = "TextSpecialCharacters.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Text node demonstration of quotation, apostrophe, ampersand and backslash characters using X3D MFString escaping for XML character entities"
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Don Brutzman"
meta4.name = "creator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "12 July 2008"
meta5.name = "created"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "2 April 2017"
meta6.name = "modified"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "Character entity references in HTML 4"
meta7.name = "reference"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "http://www.w3.org/TR/REC-html40/sgml/entities.html"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "Copyright (c) Don Brutzman and Leonard Daly, 2008"
meta9.name = "rights"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter02GeometryPrimitives/TextSpecialCharacters.x3d"
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

Background14 = Background()
Background14.skyColor = [1,1,1]
Scene13.addChildren([Background14])

Viewpoint15 = Viewpoint()
Viewpoint15.description = "Default View"
Viewpoint15.position = [0,0,15]
Scene13.addChildren([Viewpoint15])

Shape16 = Shape()
# Empty string \"\" means to skip a line 
# The ampersand escape characters are based on XML rules 
# apostrophe ' is &apos; and needs to be escaped in single-quote delimiters used for string='value' attribute 
# ampersand & is &amp; and needs to be escaped 
# quotation \" is &quot; and isn't needed if single-quote delimiters used for string='value' attribute 
# quotation \" can be used within an X3D string if escaped with backslash \\ as \\\" 
# backslash \\ is used as escape character for \" (and itself) in X3D 
# character entities are listed in HTML specification and are good for any XML 

Text17 = Text()
Text17.DEF = "DefaultText"
Text17.string = ["Character entity substitutions:","empty string \"\" skips a line:","","apostrophe  '  is &apos;","ampersand & is &amp;","quote mark  \"  is &quot;","backslash \\\\ is X3D escape character","double backslash \\\\\\\\ is X3D backslash \\\\ character","Pi Π is &#928; XML character entity"]

FontStyle18 = FontStyle(justify = ["MIDDLE","MIDDLE"])
FontStyle18.DEF = "CenteredFontStyle"
Text17.fontStyle = FontStyle18
Shape16.geometry = Text17

Appearance19 = Appearance()

Material20 = Material()
Material20.DEF = "DefaultMaterial"
Material20.diffuseColor = [0.2,0.2,0.2]
Appearance19.material = Material20
Shape16.appearance = Appearance19
Scene13.addChildren([Shape16])
X3D0.scene = Scene13
