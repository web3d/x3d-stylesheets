from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="CoordinateAxis.x3d"), 
    meta3 = meta(name="creator", content="Unknown, see X3D Resources Archives"), 
    meta4 = meta(name="generator", content="manual"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/CoordinateAxis.x3d"), 
    meta6 = meta(name="description", content="a box")), 
   Scene7 = Scene(    Collision8 = Collision(DEF="DoNotCollideWithVisualizationWidget", enabled=True,      # Invoke CoordinateAxes in other scenes as an Inline child inside a scaling Transform node, at the topmost level of the scene graph. 
     # This NavigationInfo allows examine mode and will be overridden by any parent scene. 
     # Each arrow goes from +1m to -1m to allow linear scaling to fit a scene 
     # Note each label rotates about the scene's vertical Y axis for consistency, enabling local orientation by user 

     Group9 = Group(      # Vertical Y arrow and label 

      Group10 = Group(DEF="ArrowGreen",        Shape11 = Shape(        Cylinder12 = Cylinder(DEF="ArrowCylinder", radius=.025, top=False), 
        Appearance13 = Appearance(DEF="Green",          Material14 = Material(diffuseColor=[.1,.6,.1], emissiveColor=[.05,.2,.05]))), 
       Transform15 = Transform(translation=[0,1,0],         Shape16 = Shape(         Cone17 = Cone(DEF="ArrowCone", bottomRadius=.05, height=.1), 
         Appearance18 = Appearance(USE="Green")))), 
      Transform19 = Transform(translation=[0,1.08,0],        Billboard20 = Billboard(        Shape21 = Shape(         Appearance22 = Appearance(DEF="LABEL_APPEARANCE",           Material23 = Material(diffuseColor=[1,1,.3], emissiveColor=[.33,.33,.1])), 
         Text24 = Text(string=["Y"],           FontStyle25 = FontStyle(DEF="LABEL_FONT", family=["SANS"], justify=["MIDDLE","MIDDLE"], size=.2)))))), 
     Transform26 = Transform(rotation=[0,0,1,-1.57079],       # Horizontal X arrow and label 

      Group27 = Group(       Group28 = Group(DEF="ArrowRed",         Shape29 = Shape(         Cylinder30 = Cylinder(USE="ArrowCylinder"), 
         Appearance31 = Appearance(DEF="Red",           Material32 = Material(diffuseColor=[.7,.1,.1], emissiveColor=[.33,0,0]))), 
        Transform33 = Transform(translation=[0,1,0],          Shape34 = Shape(          Cone35 = Cone(USE="ArrowCone"), 
          Appearance36 = Appearance(USE="Red")))), 
       Transform37 = Transform(rotation=[0,0,1,1.57079], translation=[.072,1.1,0],         # note label rotated back to original coordinate frame 

        Billboard38 = Billboard(         Shape39 = Shape(          Appearance40 = Appearance(USE="LABEL_APPEARANCE"), 
          Text41 = Text(string=["X"],            FontStyle42 = FontStyle(USE="LABEL_FONT"))))))), 
     Transform43 = Transform(rotation=[1,0,0,1.57079],       # Perpendicular Z arrow and label, note right-hand rule 

      Group44 = Group(       Group45 = Group(DEF="ArrowBlue",         Shape46 = Shape(         Cylinder47 = Cylinder(USE="ArrowCylinder"), 
         Appearance48 = Appearance(DEF="Blue",           Material49 = Material(diffuseColor=[.3,.3,1], emissiveColor=[.1,.1,.33]))), 
        Transform50 = Transform(translation=[0,1,0],          Shape51 = Shape(          Cone52 = Cone(USE="ArrowCone"), 
          Appearance53 = Appearance(USE="Blue")))), 
       Transform54 = Transform(rotation=[1,0,0,-1.57079], translation=[0,1.1,.072],         # note label rotated back to original coordinate frame 

        Billboard55 = Billboard(         Shape56 = Shape(          Appearance57 = Appearance(USE="LABEL_APPEARANCE"), 
          Text58 = Text(string=["Z"],            FontStyle59 = FontStyle(USE="LABEL_FONT"))))))))))
