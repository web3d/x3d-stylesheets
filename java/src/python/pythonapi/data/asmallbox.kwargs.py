from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="abox.x3d"), 
    meta3 = meta(name="creator", content="John Carlson"), 
    meta4 = meta(name="generator", content="manual"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/abox.x3d"), 
    meta6 = meta(name="description", content="a box")), 
   Scene7 = Scene(    ProtoDeclare8 = ProtoDeclare(name="anyShape", appinfo="", documentation="",      ProtoInterface9 = ProtoInterface(      field10 = field(name="myShape", accessType="inputOutput", appinfo="", documentation="", type="MFNode",        Shape11 = Shape(bboxCenter=[0,0,0], bboxSize=[-1,-1,-1],         Sphere12 = Sphere(radius=1.0, solid=True)))), 
     ProtoBody13 = ProtoBody(      Transform14 = Transform(bboxCenter=[0,0,0], bboxSize=[-1,-1,-1], center=[0,0,0], rotation=[0,0,1,0], scale=[1,1,1], scaleOrientation=[0,0,1,0], translation=[0,0,0],        IS15 = IS(        connect16 = connect(nodeField="children", protoField="myShape"))))), 
    ProtoDeclare17 = ProtoDeclare(name="one", appinfo="", documentation="",      ProtoInterface18 = ProtoInterface(      field19 = field(name="myShape", accessType="inputOutput", appinfo="", documentation="", type="MFNode",        Shape20 = Shape(bboxCenter=[0,0,0], bboxSize=[-1,-1,-1],         Cylinder21 = Cylinder(bottom=True, height=2.0, radius=1.0, side=True, solid=True, top=True)))), 
     ProtoBody22 = ProtoBody(      Transform23 = Transform(bboxCenter=[0,0,0], bboxSize=[-1,-1,-1], center=[0,0,0], rotation=[0,0,1,0], scale=[1,1,1], scaleOrientation=[0,0,1,0], translation=[0,0,0],        ProtoInstance24 = ProtoInstance(name="anyShape",         IS25 = IS(         connect26 = connect(nodeField="myShape", protoField="myShape")))))), 
    ProtoInstance27 = ProtoInstance(name="one",      fieldValue28 = fieldValue(name="myShape",       Shape29 = Shape(bboxCenter=[0,0,0], bboxSize=[-1,-1,-1],        Box30 = Box(size=[0.125,0.125,0.125], solid=True))))))
