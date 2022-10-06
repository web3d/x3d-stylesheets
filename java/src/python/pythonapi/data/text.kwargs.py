from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="creator", content="John W Carlson"), 
    meta3 = meta(name="created", content="December 13 2015"), 
    meta4 = meta(name="title", content="text.x3d"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/text.x3d"), 
    meta6 = meta(name="description", content="test \\n text"), 
    meta7 = meta(name="generator", content="Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit")), 
   Scene8 = Scene(    Transform9 = Transform(     Shape10 = Shape(      Text11 = Text(string=["Node\"\"\""],        FontStyle12 = FontStyle()), 
      Appearance13 = Appearance(       Material14 = Material())), 
     Shape15 = Shape(      Text16 = Text(string=["Node2","\\\\","\\\\\\\\","Node2"],        FontStyle17 = FontStyle()), 
      Appearance18 = Appearance(       Material19 = Material())), 
     Shape20 = Shape(      Text21 = Text(string=["Node3 \\\\\\\\ \\\\ ","Node3\"\"\""],        FontStyle22 = FontStyle()), 
      Appearance23 = Appearance(       Material24 = Material())), 
     Script25 = Script(      field26 = field(name="frontUrls", type="MFString", accessType="initializeOnly", value="\"rnl_front.png\" \"uffizi_front.png\""),       sourceCode = '''ecmascript:\n"+
"			    var me = '\"1\" \"\\\"2\" \"\\n3\"';\n"+
"			    ''', ))))
