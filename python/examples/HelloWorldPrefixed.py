####################################################################################################
#
# Now available: developmental python x3d.py package on PyPi for import.
#   This approach simplifies Python X3D deployment and use.
#   https://pypi.org/project/x3d
#
# Installation:
#       pip install x3d
# or
#       python -m pip install x3d
#
# Developer options for loading x3d package:
#
#    from x3d import *  # preferred approach, terser source that avoids x3d.* class prefixes
#
# or
#    import x3d         # traditional way to subclass x3d package, all classes require x3d.* prefix,
#                       # but python source is very verbose, for example x3d.Material x3d.Shape etc.
#                       # X3dToPython.xslt stylesheet insertPackagePrefix=true supports this option.
#
####################################################################################################

import x3d

#  comment preceding root node 
newModel=x3d.X3D(profile='Immersive',version='3.3',
  head=x3d.head(
    children=[
    x3d.meta(content='HelloWorld.x3d',name='title'),
    x3d.meta(content='Simple X3D scene example: Hello World!',name='description'),
    x3d.meta(content='30 October 2000',name='created'),
    x3d.meta(content='31 October 2019',name='modified'),
    x3d.meta(content='Don Brutzman',name='creator'),
    x3d.meta(content='HelloWorld.tall.png',name='Image'),
    x3d.meta(content='http://en.wikipedia.org/wiki/Hello_world',name='reference'),
    x3d.meta(content='https://en.wikipedia.org/wiki/Hello#.22Hello.2C_World.22_computer_program',name='reference'),
    x3d.meta(content='https://en.wikipedia.org/wiki/"Hello,_World!"_program',name='reference'),
    x3d.meta(content='http://en.wikibooks.org/w/index.php?title=Computer_Programming/Hello_world',name='reference'),
    x3d.meta(content='http://www.HelloWorldExample.net',name='reference'),
    x3d.meta(content='http://www.web3D.org',name='reference'),
    x3d.meta(content='http://www.web3d.org/realtime-3d/news/internationalization-x3d',name='reference'),
    x3d.meta(content='http://www.web3d.org/x3d/content/examples/HelloWorld.x3d',name='reference'),
    x3d.meta(content='http://X3dGraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes',name='reference'),
    x3d.meta(content='http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter01TechnicalOverview/HelloWorld.x3d',name='identifier'),
    x3d.meta(content='http://www.web3d.org/x3d/content/examples/license.html',name='license'),
    x3d.meta(content='X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit',name='generator'),
    #  Alternate encodings: VRML97, X3D ClassicVRML Encoding, X3D Compressed Binary Encoding (CBE), X3DOM, JSON 
    x3d.meta(content='HelloWorld.wrl',name='reference'),
    x3d.meta(content='HelloWorld.x3dv',name='reference'),
    x3d.meta(content='HelloWorld.x3db',name='reference'),
    x3d.meta(content='HelloWorld.xhtml',name='reference'),
    x3d.meta(content='HelloWorld.json',name='reference')]),
  Scene=x3d.Scene(
    #  Example scene to illustrate X3D nodes and fields (XML elements and attributes) 
    children=[
    x3d.WorldInfo(title='Hello World!'),
    x3d.WorldInfo(title="Hello ' apostrophe 1"),
    x3d.WorldInfo(title="Hello ' apostrophe 2"),
    x3d.WorldInfo(title='Hello " quotation mark 3'),
    x3d.WorldInfo(title='Hello " quotation mark 4'),
    x3d.MetadataSet(name="items'",
      value=[
      x3d.MetadataInteger(name='one',value=[1]),
      x3d.MetadataInteger(name='two',value=[2])]),
    x3d.Group(
      children=[
      x3d.Viewpoint(DEF='ViewUpClose',centerOfRotation=(0,-1,0),description='Hello world!',position=(0,-1,7)),
      #  insert commas to test removal when converted to ttl 
      x3d.Transform(DEF='TestWhitespaceCommas',rotation=(0,1,0,3),
        children=[
        x3d.Shape(
          geometry=x3d.Sphere(),
          appearance=x3d.Appearance(
            material=x3d.Material(DEF='MaterialLightBlue',diffuseColor=(0.1,0.5,1)),
            texture=x3d.ImageTexture(DEF='ImageCloudlessEarth',url=["earth-topo.png","earth-topo.jpg","earth-topo-small.gif","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.png","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.jpg","http://www.web3d.org/x3d/content/examples/Basic/earth-topo-small.gif"])))]),
      x3d.Transform(translation=(0,-2,0),
        children=[
        x3d.Shape(
          geometry=x3d.Text(DEF='TextMessage',string=["Hello","world!"],
            fontStyle=x3d.FontStyle(justify=["MIDDLE","MIDDLE"])),
          appearance=x3d.Appearance(
            material=x3d.Material(USE='MaterialLightBlue')))])])])
) # X3D model complete

####################################################################################################
# Self-test diagnostics
####################################################################################################

print('Self-test diagnostics for HelloWorld.py:')
if        x3d.metaDiagnostics(newModel): # built-in utility method in X3D class to show
    print(x3d.metaDiagnostics(newModel)) # ('info', 'hint', 'warning', 'error', 'TODO')

# print('check newModel.XML() serialization...')
newModelXML= newModel.XML() # test export method XML() for exceptions during export
newModel.XMLvalidate()
# print(newModelXML) # diagnostic

try:
#   print('check newModel.VRML() serialization...')
    newModelVRML=newModel.VRML() # test export method VRML() for exceptions during export
    # print(prependLineNumbers(newModelVRML)) # debug
    print("Python-to-VRML export of VRML output successful", flush=True)
except Exception as err: # usually BaseException
    # https://stackoverflow.com/questions/18176602/how-to-get-the-name-of-an-exception-that-was-caught-in-python
    print("*** Python-to-VRML export of VRML output failed:", type(err).__name__, err)
    if newModelVRML: # may have failed to generate
        print(prependLineNumbers(newModelVRML, err.lineno))

try:
#   print('check newModel.JSON() serialization...')
    newModelJSON=newModel.JSON() # test export method JSON() for exceptions during export
#   print(prependLineNumbers(newModelJSON)) # debug
    print("Python-to-JSON export of JSON output successful (under development)")
except Exception as err: # usually SyntaxError
    print("*** Python-to-JSON export of JSON output failed:", type(err).__name__, err)
    if newModelJSON: # may have failed to generate
        print(prependLineNumbers(newModelJSON,err.lineno))

print("python HelloWorld.py load and self-test diagnostics complete.")
