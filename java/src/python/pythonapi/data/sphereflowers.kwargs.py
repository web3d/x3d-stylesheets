from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="sphereflowers.x3d"), 
    meta3 = meta(name="creator", content="John Carlson"), 
    meta4 = meta(name="description", content="5 or more prismatic flowers"), 
    meta5 = meta(name="generator", content="X3D-Edit, https://savage.nps.edu/X3D-Edit"), 
    meta6 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/sphereflowers.x3d")), 
   Scene7 = Scene(    NavigationInfo8 = NavigationInfo(type=["EXAMINE","ANY"]), 
    Background9 = Background(backUrl=["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"], bottomUrl=["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"], frontUrl=["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"], leftUrl=["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"], rightUrl=["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"], topUrl=["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]), 
    Group10 = Group(     ExternProtoDeclare11 = ExternProtoDeclare(name="FlowerProto", url=["../data/flowerproto.x3d#FlowerProto"],       field12 = field(accessType="inputOutput", name="vertex", type="MFString"), 
      field13 = field(accessType="inputOutput", name="fragment", type="MFString")), 
     ProtoDeclare14 = ProtoDeclare(name="flower",       ProtoBody15 = ProtoBody(       Group16 = Group(        ProtoInstance17 = ProtoInstance(name="FlowerProto",          fieldValue18 = fieldValue(name="vertex", value="\"../shaders/cobweb_flowers_chromatic.vs\""), 
         fieldValue19 = fieldValue(name="fragment", value="\"../shaders/common.fs\""))))), 
     ProtoInstance20 = ProtoInstance(name="flower"), 
     ProtoInstance21 = ProtoInstance(name="flower"), 
     ProtoInstance22 = ProtoInstance(name="flower"), 
     ProtoInstance23 = ProtoInstance(name="flower"), 
     ProtoInstance24 = ProtoInstance(name="flower"), 
     ProtoInstance25 = ProtoInstance(name="flower"), 
     TimeSensor26 = TimeSensor(DEF="SongTime", loop=True), 
     Sound27 = Sound(maxBack=100, maxFront=100, minBack=20, minFront=20,       AudioClip28 = AudioClip(DEF="AudioClip", description="Chandubabamusic #1", url=["../resources/chandubabamusic1.wav"])), 
     ROUTE29 = ROUTE(fromField="cycleTime", fromNode="SongTime", toField="startTime", toNode="AudioClip"))))
