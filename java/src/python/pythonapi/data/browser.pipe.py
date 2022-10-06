import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setName("title").setContent("browser.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("manual"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/browser.x3d"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("a script test with embedded \\n between single quotes, a double backslash \\\\ a backslash \\ and a closing quote \"")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Script().setDEF("Browser").setSourceCode('''ecmascript:\n"+
"                function initialize() {\n"+
"		    Browser.print('DUDES\\n'+'\"DUDETTES');\n"+
"                }\n"+
"''')
)
        .addChildren(X3Dpackage.Script().setDEF("Clouds").setSourceCode('''\n"+
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
)))

