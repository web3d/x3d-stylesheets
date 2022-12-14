from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.0",    head1 = head(    meta2 = meta(content="TextExamples.x3d", name="title"), 
    meta3 = meta(content="Show different escape-character text examples for embedded quotation marks.", name="description"), 
    meta4 = meta(content="Don Brutzman", name="creator"), 
    meta5 = meta(content="7 April 2001", name="created"), 
    meta6 = meta(content="26 April 2016", name="modified"), 
    meta7 = meta(content="Note that X3D Canonicalization (C14N) will scrub alternate XML character representations, be careful to check original encoding into version control.", name="warning"), 
    meta8 = meta(content="Usually this source document needs to be inspected and edited using a plain-text editor in order to see the differences in these XML-equivalent text representations.", name="warning"), 
    meta9 = meta(content="http://www.web3d.org/x3d/content/examples/Basic/development/TextExamples.x3d", name="identifier"), 
    meta10 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta11 = meta(content="../license.html", name="license")), 
   Scene12 = Scene(    Transform13 = Transform(translation=[0,2,0],      Shape14 = Shape(      Text15 = Text(string=["Compare special character escaping"],        FontStyle16 = FontStyle(DEF="testFontStyle", justify=["MIDDLE","MIDDLE"], size=0.8)), 
      Appearance17 = Appearance(DEF="LightBlueAppearance",        Material18 = Material(diffuseColor=[0.1,0.7,0.7])))), 
    Transform19 = Transform(translation=[-3,0,0],      Shape20 = Shape(      Text21 = Text(string=["I don't think so","","he said \"Hi\""],        FontStyle22 = FontStyle(USE="testFontStyle")), 
      Appearance23 = Appearance(USE="LightBlueAppearance"))), 
    Transform24 = Transform(translation=[3,0,0],      Shape25 = Shape(      Text26 = Text(string=["I don't think so","","he said \"Hi\""],        FontStyle27 = FontStyle(USE="testFontStyle")), 
      Appearance28 = Appearance(USE="LightBlueAppearance")))))
