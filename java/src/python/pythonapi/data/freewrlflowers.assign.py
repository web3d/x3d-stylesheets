from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "sphereflowers.x3d"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "creator"
meta3.content = "John Carlson"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "description"
meta4.content = "5 or more prismatic flowers"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "generator"
meta5.content = "X3D-Edit, https://savage.nps.edu/X3D-Edit"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "identifier"
meta6.content = "https://coderextreme.net/X3DJSONLD/sphereflowers.x3d"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

NavigationInfo8 = NavigationInfo()
NavigationInfo8.type = ["EXAMINE","ANY"]
Scene7.addChildren([NavigationInfo8])

Background9 = Background()
Background9.backUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]
Background9.bottomUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]
Background9.frontUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]
Background9.leftUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]
Background9.rightUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]
Background9.topUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]
Scene7.addChildren([Background9])

Group10 = Group()

ExternProtoDeclare11 = ExternProtoDeclare()
ExternProtoDeclare11.name = "FlowerProto"
ExternProtoDeclare11.url = ["../data/flowerproto.x3d#FlowerProto"]

field12 = field()
field12.accessType = "inputOutput"
field12.name = "vertex"
field12.type = "MFString"
ExternProtoDeclare11.addField([field12])

field13 = field()
field13.accessType = "inputOutput"
field13.name = "fragment"
field13.type = "MFString"
ExternProtoDeclare11.addField([field13])
Group10.addChildren([ExternProtoDeclare11])

ProtoDeclare14 = ProtoDeclare()
ProtoDeclare14.name = "flower"

ProtoBody15 = ProtoBody()

Group16 = Group()

ProtoInstance17 = ProtoInstance()
ProtoInstance17.name = "FlowerProto"

fieldValue18 = fieldValue()
fieldValue18.name = "vertex"
fieldValue18.value = "\"../shaders/freewrl_flowers_chromatic.vs\""
ProtoInstance17.addFieldValue([fieldValue18])

fieldValue19 = fieldValue()
fieldValue19.name = "fragment"
fieldValue19.value = "\"../shaders/freewrl.fs\""
ProtoInstance17.addFieldValue([fieldValue19])
Group16.addChildren([ProtoInstance17])
ProtoBody15.addChildren([Group16])
ProtoDeclare14.protoBody = ProtoBody15
Group10.addChildren([ProtoDeclare14])

ProtoInstance20 = ProtoInstance()
ProtoInstance20.name = "flower"
Group10.addChildren([ProtoInstance20])

ProtoInstance21 = ProtoInstance()
ProtoInstance21.name = "flower"
Group10.addChildren([ProtoInstance21])

ProtoInstance22 = ProtoInstance()
ProtoInstance22.name = "flower"
Group10.addChildren([ProtoInstance22])

ProtoInstance23 = ProtoInstance()
ProtoInstance23.name = "flower"
Group10.addChildren([ProtoInstance23])

ProtoInstance24 = ProtoInstance()
ProtoInstance24.name = "flower"
Group10.addChildren([ProtoInstance24])

ProtoInstance25 = ProtoInstance()
ProtoInstance25.name = "flower"
Group10.addChildren([ProtoInstance25])
Scene7.addChildren([Group10])
X3D0.scene = Scene7
