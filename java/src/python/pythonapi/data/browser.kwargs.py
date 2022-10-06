from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="browser.x3d"), 
    meta3 = meta(name="creator", content="John Carlson"), 
    meta4 = meta(name="generator", content="manual"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/browser.x3d"), 
    meta6 = meta(name="description", content="a script test with embedded \\n between single quotes, a double backslash \\\\ a backslash \\ and a closing quote \"")), 
   Scene7 = Scene(    Script8 = Script(DEF="Browser",      sourceCode = '''ecmascript:\n"+
"                function initialize() {\n"+
"		    Browser.print('DUDES\\n'+'\"DUDETTES');\n"+
"                }\n"+
"''', ), 
    Script9 = Script(DEF="Clouds",      sourceCode = '''\n"+
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
"''', )))
