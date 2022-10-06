from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "CoordinateAxis.x3d"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "creator"
meta3.content = "Unknown, see X3D Resources Archives"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "generator"
meta4.content = "manual"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/CoordinateAxis.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "a box"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

Collision8 = Collision()
Collision8.DEF = "DoNotCollideWithVisualizationWidget"
Collision8.enabled = True
# Invoke CoordinateAxes in other scenes as an Inline child inside a scaling Transform node, at the topmost level of the scene graph. 
# This NavigationInfo allows examine mode and will be overridden by any parent scene. 
# Each arrow goes from +1m to -1m to allow linear scaling to fit a scene 
# Note each label rotates about the scene's vertical Y axis for consistency, enabling local orientation by user 

Group9 = Group()
# Vertical Y arrow and label 

Group10 = Group()
Group10.DEF = "ArrowGreen"

Shape11 = Shape()

Cylinder12 = Cylinder(radius = .025)
Cylinder12.DEF = "ArrowCylinder"
Cylinder12.top = False
Shape11.geometry = Cylinder12

Appearance13 = Appearance()
Appearance13.DEF = "Green"

Material14 = Material()
Material14.diffuseColor = [.1,.6,.1]
Material14.emissiveColor = [.05,.2,.05]
Appearance13.material = Material14
Shape11.appearance = Appearance13
Group10.addChildren([Shape11])

Transform15 = Transform()
Transform15.translation = [0,1,0]

Shape16 = Shape()

Cone17 = Cone(bottomRadius = .05, height = .1)
Cone17.DEF = "ArrowCone"
Shape16.geometry = Cone17

Appearance18 = Appearance()
Appearance18.USE = "Green"
Shape16.appearance = Appearance18
Transform15.addChildren([Shape16])
Group10.addChildren([Transform15])
Group9.addChildren([Group10])

Transform19 = Transform()
Transform19.translation = [0,1.08,0]

Billboard20 = Billboard()

Shape21 = Shape()

Appearance22 = Appearance()
Appearance22.DEF = "LABEL_APPEARANCE"

Material23 = Material()
Material23.diffuseColor = [1,1,.3]
Material23.emissiveColor = [.33,.33,.1]
Appearance22.material = Material23
Shape21.appearance = Appearance22

Text24 = Text()
Text24.string = ["Y"]

FontStyle25 = FontStyle(family = ["SANS"], justify = ["MIDDLE","MIDDLE"], size = .2)
FontStyle25.DEF = "LABEL_FONT"
Text24.fontStyle = FontStyle25
Shape21.geometry = Text24
Billboard20.addChildren([Shape21])
Transform19.addChildren([Billboard20])
Group9.addChildren([Transform19])
Collision8.addChildren([Group9])

Transform26 = Transform()
Transform26.rotation = [0,0,1,-1.57079]
# Horizontal X arrow and label 

Group27 = Group()

Group28 = Group()
Group28.DEF = "ArrowRed"

Shape29 = Shape()

Cylinder30 = Cylinder()
Cylinder30.USE = "ArrowCylinder"
Shape29.geometry = Cylinder30

Appearance31 = Appearance()
Appearance31.DEF = "Red"

Material32 = Material()
Material32.diffuseColor = [.7,.1,.1]
Material32.emissiveColor = [.33,0,0]
Appearance31.material = Material32
Shape29.appearance = Appearance31
Group28.addChildren([Shape29])

Transform33 = Transform()
Transform33.translation = [0,1,0]

Shape34 = Shape()

Cone35 = Cone()
Cone35.USE = "ArrowCone"
Shape34.geometry = Cone35

Appearance36 = Appearance()
Appearance36.USE = "Red"
Shape34.appearance = Appearance36
Transform33.addChildren([Shape34])
Group28.addChildren([Transform33])
Group27.addChildren([Group28])

Transform37 = Transform()
Transform37.rotation = [0,0,1,1.57079]
Transform37.translation = [.072,1.1,0]
# note label rotated back to original coordinate frame 

Billboard38 = Billboard()

Shape39 = Shape()

Appearance40 = Appearance()
Appearance40.USE = "LABEL_APPEARANCE"
Shape39.appearance = Appearance40

Text41 = Text()
Text41.string = ["X"]

FontStyle42 = FontStyle()
FontStyle42.USE = "LABEL_FONT"
Text41.fontStyle = FontStyle42
Shape39.geometry = Text41
Billboard38.addChildren([Shape39])
Transform37.addChildren([Billboard38])
Group27.addChildren([Transform37])
Transform26.addChildren([Group27])
Collision8.addChildren([Transform26])

Transform43 = Transform()
Transform43.rotation = [1,0,0,1.57079]
# Perpendicular Z arrow and label, note right-hand rule 

Group44 = Group()

Group45 = Group()
Group45.DEF = "ArrowBlue"

Shape46 = Shape()

Cylinder47 = Cylinder()
Cylinder47.USE = "ArrowCylinder"
Shape46.geometry = Cylinder47

Appearance48 = Appearance()
Appearance48.DEF = "Blue"

Material49 = Material()
Material49.diffuseColor = [.3,.3,1]
Material49.emissiveColor = [.1,.1,.33]
Appearance48.material = Material49
Shape46.appearance = Appearance48
Group45.addChildren([Shape46])

Transform50 = Transform()
Transform50.translation = [0,1,0]

Shape51 = Shape()

Cone52 = Cone()
Cone52.USE = "ArrowCone"
Shape51.geometry = Cone52

Appearance53 = Appearance()
Appearance53.USE = "Blue"
Shape51.appearance = Appearance53
Transform50.addChildren([Shape51])
Group45.addChildren([Transform50])
Group44.addChildren([Group45])

Transform54 = Transform()
Transform54.rotation = [1,0,0,-1.57079]
Transform54.translation = [0,1.1,.072]
# note label rotated back to original coordinate frame 

Billboard55 = Billboard()

Shape56 = Shape()

Appearance57 = Appearance()
Appearance57.USE = "LABEL_APPEARANCE"
Shape56.appearance = Appearance57

Text58 = Text()
Text58.string = ["Z"]

FontStyle59 = FontStyle()
FontStyle59.USE = "LABEL_FONT"
Text58.fontStyle = FontStyle59
Shape56.geometry = Text58
Billboard55.addChildren([Shape56])
Transform54.addChildren([Billboard55])
Group44.addChildren([Transform54])
Transform43.addChildren([Group44])
Collision8.addChildren([Transform43])
Scene7.addChildren([Collision8])
X3D0.scene = Scene7
