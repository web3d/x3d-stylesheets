from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.0",    head1 = head(    meta2 = meta(content="ExtrusionHeart.x3d", name="title"), 
    meta3 = meta(content="Simple extrusion of a Valentine heart.", name="description"), 
    meta4 = meta(content="Class participants in course Introduction to VRML/X3D.", name="creator"), 
    meta5 = meta(content="14 February 2001", name="created"), 
    meta6 = meta(content="27 November 2015", name="modified"), 
    meta7 = meta(content="http://www.web3d.org/x3d/content/examples/Basic/course/ExtrusionHeart.x3d", name="identifier"), 
    meta8 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta9 = meta(content="../license.html", name="license")), 
   Scene10 = Scene(    Viewpoint11 = Viewpoint(description="Extrusion Heart", orientation=[1,0,0,1.57], position=[0,-4,0]), 
    Transform12 = Transform(translation=[0,-0.5,0],      Shape13 = Shape(      Extrusion14 = Extrusion(creaseAngle=3.14159, crossSection=[0,0.8,0.2,1,0.7,0.95,1,0.5,0.8,0,0.5,-0.3,0,-0.7,-0.5,-0.3,-0.8,0,-1,0.5,-0.7,0.95,-0.2,1,0,0.8], scale=[0.01,0.01,0.8,0.8,1,1,0.8,0.8,0.01,0.01], solid=False, spine=[0,0,0,0,0.1,0,0,0.5,0,0,0.9,0,0,1,0]), 
      Appearance15 = Appearance(       Material16 = Material(diffuseColor=[0.8,0.3,0.3]))))))
