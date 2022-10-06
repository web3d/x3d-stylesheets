from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(content="PixelTextureComponentExamples.x3d", name="title"), 
    meta3 = meta(content="This example shows the five PixelTexture components, with 0 to 4 components each, shown in Table 5-18.", name="description"), 
    meta4 = meta(content="Leonard Daly and Don Brutzman", name="creator"), 
    meta5 = meta(content="25 August 2008", name="created"), 
    meta6 = meta(content="7 January 2014", name="modified"), 
    meta7 = meta(content="http://X3dGraphics.com", name="reference"), 
    meta8 = meta(content="X3D for Web Authors, Table 5.18", name="reference"), 
    meta9 = meta(content="http://www.web3d.org/x3d/content/examples/X3dResources.html", name="reference"), 
    meta10 = meta(content="Copyright (c) 2006, Daly Realism and Don Brutzman", name="rights"), 
    meta11 = meta(content="X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com", name="subject"), 
    meta12 = meta(content="http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter05AppearanceMaterialTextures/PixelTextureComponentExamples.x3d", name="identifier"), 
    meta13 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta14 = meta(content="../license.html", name="license")), 
   Scene15 = Scene(    Background16 = Background(skyColor=[0.1,0.1,0.4]), 
    Viewpoint17 = Viewpoint(description="Table 5.18 SFImage component examples", position=[0,0,14]), 
    Transform18 = Transform(translation=[-6,0,0],      Shape19 = Shape(      Appearance20 = Appearance(       PixelTexture21 = PixelTexture(DEF="ZeroComponents")), 
      Box22 = Box()), 
     Transform23 = Transform(translation=[0,-2,0],       Shape24 = Shape(       Text25 = Text(string=["0"],         FontStyle26 = FontStyle(DEF="CenterJustify", justify=["MIDDLE","MIDDLE"])), 
       Appearance27 = Appearance(DEF="TextMaterial",         Material28 = Material(diffuseColor=[1,1,1]))))), 
    Transform29 = Transform(translation=[-3,0,0],      Shape30 = Shape(      Appearance31 = Appearance(       PixelTexture32 = PixelTexture(DEF="OneComponent", image=[1,2,1,0xFF,0x00])), 
      Box33 = Box()), 
     Transform34 = Transform(translation=[0,-2,0],       Shape35 = Shape(       Text36 = Text(string=["1"],         FontStyle37 = FontStyle(USE="CenterJustify")), 
       Appearance38 = Appearance(USE="TextMaterial")))), 
    Transform39 = Transform(     Shape40 = Shape(      Appearance41 = Appearance(       PixelTexture42 = PixelTexture(DEF="TwoComponents", image=[2,1,2,0xCCFF,0x2277])), 
      Box43 = Box()), 
     Transform44 = Transform(translation=[0,-2,0],       Shape45 = Shape(       Text46 = Text(string=["2"],         FontStyle47 = FontStyle(USE="CenterJustify")), 
       Appearance48 = Appearance(USE="TextMaterial")))), 
    Transform49 = Transform(translation=[3,0,0],      Shape50 = Shape(      Appearance51 = Appearance(       # note 0x000000 = 0 

       PixelTexture52 = PixelTexture(DEF="ThreeComponents", image=[2,4,3,0xFF0000,0xFF00,0x000000,0,0,0,0xFFFFFF,0xFFFF00])), 
      Box53 = Box()), 
     Transform54 = Transform(translation=[0,-2,0],       Shape55 = Shape(       Text56 = Text(string=["3"],         FontStyle57 = FontStyle(USE="CenterJustify")), 
       Appearance58 = Appearance(USE="TextMaterial")))), 
    Transform59 = Transform(translation=[6,0,0],      Shape60 = Shape(      Appearance61 = Appearance(       # Erroneous value in book: 1 0 0 255, 0 1 0 255, 0 0 1 255, 1 0 0 127, 0 1 0 127, 0 0 1 127 

       PixelTexture62 = PixelTexture(DEF="FourComponents", image=[3,2,4,-16776961,0x00FF00FF,0x0000FFFF,-16777089,0x00FF007F,0x0000FF7F])), 
      Box63 = Box()), 
     Transform64 = Transform(translation=[0,-2,0],       Shape65 = Shape(       Text66 = Text(string=["4"],         FontStyle67 = FontStyle(USE="CenterJustify")), 
       Appearance68 = Appearance(USE="TextMaterial")))),     # Background from PixelTextureBW.x3d 

    Transform69 = Transform(translation=[0,6,-2],      Shape70 = Shape(      Appearance71 = Appearance(       PixelTexture72 = PixelTexture(image=[8,8,1,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0x00,0xcc,0x00,0xcc,0x00,0xcc,0x00,0xcc])), 
      Box73 = Box(size=[16,16,.1])))))
