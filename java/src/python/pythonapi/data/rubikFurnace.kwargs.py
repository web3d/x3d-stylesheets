from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="rubikFurnace.x3d"), 
    meta3 = meta(name="creator", content="John Carlson"), 
    meta4 = meta(name="generator", content="manual"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/rubikFurnace.x3d"), 
    meta6 = meta(name="description", content="a green rubik cube")), 
   Scene7 = Scene(    NavigationInfo8 = NavigationInfo(type=["EXAMINE"]), 
    Viewpoint9 = Viewpoint(description="Rubiks Cube on Fire", position=[0,0,12]), 
    ProtoDeclare10 = ProtoDeclare(name="anyShape",      ProtoInterface11 = ProtoInterface(      field12 = field(name="xtranslation", accessType="inputOutput", type="SFVec3f", value="0.0 0.0 0.0"), 
      field13 = field(name="myShape", accessType="inputOutput", type="MFNode",        Shape14 = Shape(        Sphere15 = Sphere(), 
        Appearance16 = Appearance(         Material17 = Material(diffuseColor=[1,1,1]))))), 
     ProtoBody18 = ProtoBody(      Transform19 = Transform(translation=[0,0,0],        IS20 = IS(        connect21 = connect(nodeField="translation", protoField="xtranslation"), 
        connect22 = connect(nodeField="children", protoField="myShape"))))), 
    ProtoDeclare23 = ProtoDeclare(name="three",      ProtoInterface24 = ProtoInterface(      field25 = field(name="ytranslation", accessType="inputOutput", type="SFVec3f", value="0.0 0.0 0.0"), 
      field26 = field(name="myShape", accessType="inputOutput", type="MFNode",        Shape27 = Shape(        Sphere28 = Sphere(), 
        Appearance29 = Appearance(         Material30 = Material(diffuseColor=[1,1,1]))))), 
     ProtoBody31 = ProtoBody(      Transform32 = Transform(translation=[0,0,0],        IS33 = IS(        connect34 = connect(nodeField="translation", protoField="ytranslation")), 
       ProtoInstance35 = ProtoInstance(name="anyShape",         fieldValue36 = fieldValue(name="xtranslation", value="0 0 0"), 
        IS37 = IS(         connect38 = connect(nodeField="myShape", protoField="myShape"))), 
       ProtoInstance39 = ProtoInstance(name="anyShape",         fieldValue40 = fieldValue(name="xtranslation", value="2 0 0"), 
        IS41 = IS(         connect42 = connect(nodeField="myShape", protoField="myShape"))), 
       ProtoInstance43 = ProtoInstance(name="anyShape",         fieldValue44 = fieldValue(name="xtranslation", value="-2 0 0"), 
        IS45 = IS(         connect46 = connect(nodeField="myShape", protoField="myShape")))))), 
    ProtoDeclare47 = ProtoDeclare(name="nine",      ProtoInterface48 = ProtoInterface(      field49 = field(name="ztranslation", accessType="inputOutput", type="SFVec3f", value="0.0 0.0 0.0"), 
      field50 = field(name="myShape", accessType="inputOutput", type="MFNode",        Shape51 = Shape(        Sphere52 = Sphere(), 
        Appearance53 = Appearance(         Material54 = Material(diffuseColor=[1,1,1]))))), 
     ProtoBody55 = ProtoBody(      Transform56 = Transform(translation=[0,0,0],        IS57 = IS(        connect58 = connect(nodeField="translation", protoField="ztranslation")), 
       ProtoInstance59 = ProtoInstance(name="three",         fieldValue60 = fieldValue(name="ytranslation", value="0 0 0"), 
        IS61 = IS(         connect62 = connect(nodeField="myShape", protoField="myShape"))), 
       ProtoInstance63 = ProtoInstance(name="three",         fieldValue64 = fieldValue(name="ytranslation", value="0 2 0"), 
        IS65 = IS(         connect66 = connect(nodeField="myShape", protoField="myShape"))), 
       ProtoInstance67 = ProtoInstance(name="three",         fieldValue68 = fieldValue(name="ytranslation", value="0 -2 0"), 
        IS69 = IS(         connect70 = connect(nodeField="myShape", protoField="myShape")))))), 
    ProtoDeclare71 = ProtoDeclare(name="twentyseven",      ProtoInterface72 = ProtoInterface(      field73 = field(name="ttranslation", accessType="inputOutput", type="SFVec3f", value="0.0 0.0 0.0"), 
      field74 = field(name="myShape", accessType="inputOutput", type="MFNode",        Shape75 = Shape(        Sphere76 = Sphere(), 
        Appearance77 = Appearance(         Material78 = Material(diffuseColor=[1,1,1]))))), 
     ProtoBody79 = ProtoBody(      Transform80 = Transform(translation=[0,0,0],        IS81 = IS(        connect82 = connect(nodeField="translation", protoField="ttranslation")), 
       ProtoInstance83 = ProtoInstance(name="nine",         fieldValue84 = fieldValue(name="ztranslation", value="0 0 0"), 
        IS85 = IS(         connect86 = connect(nodeField="myShape", protoField="myShape"))), 
       ProtoInstance87 = ProtoInstance(name="nine",         fieldValue88 = fieldValue(name="ztranslation", value="0 0 2"), 
        IS89 = IS(         connect90 = connect(nodeField="myShape", protoField="myShape"))), 
       ProtoInstance91 = ProtoInstance(name="nine",         fieldValue92 = fieldValue(name="ztranslation", value="0 0 -2"), 
        IS93 = IS(         connect94 = connect(nodeField="myShape", protoField="myShape")))))), 
    ProtoInstance95 = ProtoInstance(name="twentyseven",      fieldValue96 = fieldValue(name="ttranslation", value="0 0 0"), 
     fieldValue97 = fieldValue(name="myShape",       Shape98 = Shape(       Box99 = Box(size=[1,1,1]), 
       Appearance100 = Appearance(        Material101 = Material(diffuseColor=[0,1,0])))))))