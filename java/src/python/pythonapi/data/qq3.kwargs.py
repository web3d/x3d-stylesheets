from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(content="qq3.x3d", name="title"), 
    meta3 = meta(content="John Carlson", name="creator"), 
    meta4 = meta(content="John Carlson", name="translator"), 
    meta5 = meta(content="11 Jan 2015", name="created"), 
    meta6 = meta(content="05 May 2017", name="modified"), 
    meta7 = meta(content="12 extrusions to test prototype expander", name="description"), 
    meta8 = meta(content="https://coderextreme.net/x3d/qq3.x3d", name="identifier"), 
    meta9 = meta(content="manual", name="generator")), 
   Scene10 = Scene(    ProtoDeclare11 = ProtoDeclare(name="Process",      ProtoBody12 = ProtoBody(      Group13 = Group(       # left 

       Transform14 = Transform(scale=[0.5,0.5,0.5],         Shape15 = Shape(DEF="ShapeLeftDown",          Appearance16 = Appearance(          Material17 = Material(diffuseColor=[0.7,1,0])), 
         Extrusion18 = Extrusion(spine=[-2.5,0,0,-1.5,0,0], creaseAngle=0.785, crossSection=[1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00]))),        # right 

       Transform19 = Transform(scale=[0.5,0.5,0.5],         Shape20 = Shape(DEF="ShapeUpRight",          Appearance21 = Appearance(          Material22 = Material(diffuseColor=[0,0.7,1])), 
         Extrusion23 = Extrusion(spine=[1.5,0,0,2.5,0,0], creaseAngle=0.785, crossSection=[1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00]))),        # up 

       Transform24 = Transform(scale=[0.5,0.5,0.5],         Shape25 = Shape(USE="ShapeUpRight")),        # down 

       Transform26 = Transform(scale=[0.5,0.5,0.5],         Shape27 = Shape(USE="ShapeLeftDown"))))), 
    Viewpoint28 = Viewpoint(description="Process pipes", orientation=[1,0,0,-0.4], position=[0,5,12]), 
    Transform29 = Transform(translation=[0,-2.5,0],      ProtoInstance30 = ProtoInstance(name="Process")), 
    Transform31 = Transform(translation=[0,0,0],      ProtoInstance32 = ProtoInstance(name="Process")), 
    Transform33 = Transform(translation=[0,2.5,0],      ProtoInstance34 = ProtoInstance(name="Process"))))
