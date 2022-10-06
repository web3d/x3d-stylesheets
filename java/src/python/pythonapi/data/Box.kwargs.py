from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="box.x3d"), 
    meta3 = meta(name="creator", content="John Carlson"), 
    meta4 = meta(name="generator", content="manual"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/box.x3d"), 
    meta6 = meta(name="description", content="3 boxes")), 
   Scene7 = Scene(    NavigationInfo8 = NavigationInfo(type=["EXAMINE"]), 
    Viewpoint9 = Viewpoint(description="Cubes on Fire", position=[0,0,12]), 
    ProtoDeclare10 = ProtoDeclare(name="anyShape",      ProtoInterface11 = ProtoInterface(      field12 = field(name="xtranslation", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
      field13 = field(name="myShape", accessType="inputOutput", type="MFNode",        Shape14 = Shape(        Sphere15 = Sphere(), 
        Appearance16 = Appearance(         Material17 = Material(diffuseColor=[1,1,1]))))), 
     ProtoBody18 = ProtoBody(      Transform19 = Transform(       IS20 = IS(        connect21 = connect(nodeField="translation", protoField="xtranslation"), 
        connect22 = connect(nodeField="children", protoField="myShape"))))), 
    ProtoDeclare23 = ProtoDeclare(name="three",      ProtoInterface24 = ProtoInterface(      field25 = field(name="ytranslation", accessType="inputOutput", type="SFVec3f", value="0 0 0"), 
      field26 = field(name="myShape", accessType="inputOutput", type="MFNode",        Shape27 = Shape(        Cylinder28 = Cylinder(), 
        Appearance29 = Appearance(         Material30 = Material(diffuseColor=[1,1,1]))))), 
     ProtoBody31 = ProtoBody(      Transform32 = Transform(       IS33 = IS(        connect34 = connect(nodeField="translation", protoField="ytranslation")), 
       ProtoInstance35 = ProtoInstance(name="anyShape",         fieldValue36 = fieldValue(name="xtranslation", value="0 0 0"), 
        IS37 = IS(         connect38 = connect(nodeField="myShape", protoField="myShape"))), 
       ProtoInstance39 = ProtoInstance(name="anyShape",         fieldValue40 = fieldValue(name="xtranslation", value="2 0 0"), 
        IS41 = IS(         connect42 = connect(nodeField="myShape", protoField="myShape"))), 
       ProtoInstance43 = ProtoInstance(name="anyShape",         fieldValue44 = fieldValue(name="xtranslation", value="-2 0 0"), 
        IS45 = IS(         connect46 = connect(nodeField="myShape", protoField="myShape")))))), 
    ProtoInstance47 = ProtoInstance(name="three",      fieldValue48 = fieldValue(name="ytranslation", value="0 0 0"), 
     fieldValue49 = fieldValue(name="myShape",       Shape50 = Shape(       Box51 = Box(size=[1,1,1]), 
       Appearance52 = Appearance(        Material53 = Material(diffuseColor=[0,1,0])))))))
