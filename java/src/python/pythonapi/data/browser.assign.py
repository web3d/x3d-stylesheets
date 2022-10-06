from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "browser.x3d"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "creator"
meta3.content = "John Carlson"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "generator"
meta4.content = "manual"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/browser.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "a script test with embedded \\n between single quotes, a double backslash \\\\ a backslash \\ and a closing quote \""
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

Script8 = Script()
Script8.DEF = "Browser"

Script8.setSourceCode('''ecmascript:\n"+
"                function initialize() {\n"+
"		    Browser.print('DUDES\\n'+'\"DUDETTES');\n"+
"                }\n"+
"''')
Scene7.addChildren([Script8])

Script9 = Script()
Script9.DEF = "Clouds"

Script9.setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"\n"+
"function cumulustranslation() // These values designate the boundary location of the cloud\n"+
"{\n"+
"var xxx = ' '+' '+\n"+
"'	Transform		\\n'+\n"+
"'    ' + '               	\\n';\n"+
"\n"+
"}\n"+
"''')
Scene7.addChildren([Script9])
X3D0.scene = Scene7
