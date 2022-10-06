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

from x3d import *

newModel=X3D(profile='Immersive',version='4.0',
  head=head(
    children=[
    meta(content='HelloWorldX3D4.x3d',name='title'),
    meta(content='Test X3D version 4 with simple X3D model example: Hello World!',name='description'),
    meta(content='10 June 2021',name='created'),
    meta(content='18 September 2021',name='modified'),
    meta(content='Don Brutzman',name='creator'),
    meta(content='HelloWorld.tall.png',name='Image'),
    meta(content='https://en.wikipedia.org/wiki/Hello_world',name='reference'),
    meta(content='https://en.wikipedia.org/wiki/Hello#.22Hello.2C_World.22_computer_program',name='reference'),
    meta(content='https://en.wikipedia.org/wiki/"Hello,_World!"_program',name='reference'),
    meta(content='https://en.wikibooks.org/w/index.php?title=Computer_Programming/Hello_world',name='reference'),
    meta(content='https://www.HelloWorldExample.net',name='reference'),
    meta(content='https://www.web3d.org',name='reference'),
    meta(content='https://www.web3d.org/realtime-3d/news/internationalization-x3d',name='reference'),
    meta(content='https://www.web3d.org/x3d/content/examples/HelloWorld.x3d',name='reference'),
    meta(content='https://X3dGraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes/HelloWorld.x3d',name='reference'),
    meta(content='https://X3dGraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes/HelloWorldX3D4.x3d',name='identifier'),
    meta(content='https://www.web3d.org/x3d/content/examples/license.html',name='license'),
    meta(content='X3D-Edit 4.0, https://savage.nps.edu/X3D-Edit',name='generator'),
    meta(content='HelloWorld.wrl',name='reference'),
    meta(content='HelloWorldX3D4.x3dv',name='reference'),
    meta(content='HelloWorldX3D4.x3db',name='reference'),
    meta(content='HelloWorldX3D4.xhtml',name='reference'),
    meta(content='HelloWorldX3D4.json',name='reference')]),
  Scene=Scene(
    #  Example scene to illustrate X3D nodes and fields (XML elements and attributes) 
    children=[
    WorldInfo(DEF='WorldInfoPrimary',info=["Example scene to illustrate a simple X3D4 model"],title='Hello World!'),
    WorldInfo(DEF='WorldInfoSecondary',class_='TestClass',id_='TestID',style_='TestStyle',title='test HTML CSS fields'),
    Group(
      children=[
      Viewpoint(DEF='ViewUpClose',centerOfRotation=(0,-1,0),description='Hello world!',position=(0,-1,7)),
      Transform(rotation=(0,1,0,3),
        children=[
        Shape(
          geometry=Sphere(),
          appearance=Appearance(
            #  https://htmlcolorcodes.com/colors/off-white 
            material=Material(DEF='MaterialOffWhite',diffuseColor=(0.980392,0.976471,0.964706)),
            texture=ImageTexture(DEF='ImageCloudlessEarth',url=["earth-topo.png","earth-topo.jpg","earth-topo-small.gif","https://www.web3d.org/x3d/content/examples/Basic/earth-topo.png","https://www.web3d.org/x3d/content/examples/Basic/earth-topo.jpg","https://www.web3d.org/x3d/content/examples/Basic/earth-topo-small.gif"])))]),
      Transform(translation=(0,-2,0),
        children=[
        Shape(
          geometry=Text(DEF='TextMessage',string=["Hello","X3D 4!"],
            fontStyle=FontStyle(justify=["MIDDLE","MIDDLE"])),
          appearance=Appearance(
            material=Material(USE='MaterialOffWhite')))])])])
) # X3D model complete

####################################################################################################
# Self-test diagnostics
####################################################################################################

print('Self-test diagnostics for HelloWorldX3D4.py:')
if        metaDiagnostics(newModel): # built-in utility method in X3D class
    print(metaDiagnostics(newModel)) # display meta info, hint, warning, error, TODO values in this model
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

print("python HelloWorldX3D4.py load and self-test diagnostics complete.")
