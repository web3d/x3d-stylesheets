from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.0"

head1 = head()

meta2 = meta()
meta2.content = "F16.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "F-16, The Fighting Falcon, Turkish Air Force (TUAF), Turkey"
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "Murat ONDER, LTJG, Turkish Navy"
meta4.name = "creator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "The coordinates of the main body (Except landing gears, nose antenna, flag, weapons, missile holders, cockpit, cockpit seat and fuel tanks) are mostly similar to the model of Soji Yamakawa and used with permission."
meta5.name = "creator"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "13 July 2003"
meta6.name = "created"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "27 November 2015"
meta7.name = "modified"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "http://www.fas.org/man/dod-101/sys/ac/f-16.htm"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "Here is a copy of the permission for the usage of the main hull; -----Original Message----- From: Soji Yamakawa [mailto:soji@andrew.cmu.edu] Sent: Tuesday, September 16, 2003 8:00 PM To: Onder, Murat TUR Subject: Re: VRML model points usage permission Sure. No problem. Soji ----- Original Message ----- From: \"Murat Onder\" <monder@nps.navy.mil> To: <Soji_Yamakawa@cmu.edu>; <PEB01130@nifty.ne.jp> Sent: Monday, September 15, 2003 3:50 PM Subject: VRML model points usage permission Hi Sir, I&apos;m a MS student in Naval Postgraduate School. I'm making a model of Turkish F-16 for my project in a VRML course. For the main hull of the F-16, I want to use the coordinate points of your VRML model since I think that model represents well enough F-16. This is going to be only a student project and will not be used for any commercial purposes. Of course I'll make the citation and put the reference links to your page in the meta files of x3d file. I'd like to know if you can give permission to use those points in my model. V/R, Murat Onder LTJG, TU NAVY"
meta9.name = "permission"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "The landing gears are taken from the Savage Archive, from F18 Blue Angel, then modified and re-animated."
meta10.name = "reference"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "\"Drawing.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Drawing.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Drawing.jpg\""
meta11.name = "drawing"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "\"FrontView.jpg\" \"FrontView2.jpg\" \"Missiles.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView2.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView2.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Missiles.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Missiles.jpg\""
meta12.name = "Image"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/F16.x3d"
meta13.name = "identifier"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "F16, F-16, Fighting Falcon"
meta14.name = "subject"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta15.name = "generator"
head1.addMeta([meta15])

meta16 = meta()
meta16.content = "../../license.html"
meta16.name = "license"
head1.addMeta([meta16])
X3D0.head = head1

Scene17 = Scene()

Transform18 = Transform()
Transform18.DEF = "F16Transform"

Transform19 = Transform()
Transform19.DEF = "MainFrameTransform"
Transform19.scale = [3,3,3]

Shape20 = Shape()
Shape20.DEF = "Nose"

Appearance21 = Appearance()

Material22 = Material()
Material22.diffuseColor = [.25,.25,.25]
Appearance21.material = Material22
Shape20.appearance = Appearance21

IndexedFaceSet23 = IndexedFaceSet(coordIndex = [24,0,3,-1,4,0,24,-1,25,26,27,-1,28,25,27,-1,27,29,28,-1,27,30,29,-1,27,31,30,-1,3,18,24,-1], creaseAngle = 0.5, normalIndex = [16,0,3,-1,4,0,16,-1,17,17,17,-1,18,18,18,-1,19,19,19,-1,20,20,20,-1,21,21,21,-1,3,14,16,-1], solid = False)

Coordinate24 = Coordinate()
Coordinate24.DEF = "coordinates"
Coordinate24.point = [-0.32,0.36,-4.91,-0.38,0.43,-4.21,0,0.6,-4.2,0,0.5,-4.9,-0.5,0,-4.9,-0.6,0,-4.2,1,0,5.8,1,0,5.3,2.8,-0.4,6.3,2.8,-0.4,6.61,0.31,-0.36,-4.9,0.4,-0.35,-4.2,0,-0.4,-4.2,0,-0.4,-4.9,-0.31,-0.36,-4.9,-0.4,-0.35,-4.2,0.5,0,-4.9,0.6,0,-4.2,0.32,0.36,-4.91,0.38,0.43,-4.21,-1,0,5.8,-1,0,5.3,-2.8,-0.4,6.3,-2.8,-0.4,6.61,0,-0.1,-7,-0.31,-0.36,-4.9,-0.5,0,-4.9,0,-0.1,-7,0,-0.4,-4.9,0.31,-0.36,-4.9,0.5,0,-4.9,0.32,0.36,-4.91,-0.27,0.93,-3.51,0,1.1,-3.6,-0.33,0.5,-3.41,-0.34,0.9,-1.73,0,0.9,-1,0,1.1,-1.8,-0.38,0.64,-1.68,0.34,0.9,-1.73,0,0.9,-1,0.38,0.64,-1.68,0.34,0.9,-1.73,0.27,0.93,-3.51,0.33,0.5,-3.41,0,1.3,-2.8,0.45,1.02,-2.68,0.38,0.64,-1.68,0.53,0.5,-2.56,-0.53,0.5,-2.56,-0.45,1.02,-2.68,-0.53,0.75,0,-0.56,0.66,2.8,0,0.7,2.8,0,0.8,0,-1.1,0.3,0,-1,0.3,2.8,-0.37,0.57,4.9,0,0.59,4.9,-0.7,0.3,4.9,-0.7,0.3,4.9,-0.7,0,7,-0.5,0.49,7,-0.5,0.49,7,0,0.7,7,-1.4,0,0,-1.4,0,3.9,-1.4,0,3.9,-1,0,3.9,-1,0.3,2.8,-1,0.3,4.9,-0.59,0.65,-0.77,-0.8,0.3,-0.6,-1.4,0,-0.7,-1,-0.1,2.8,-0.7,-0.7,-2.5,-0.5,-0.9,-2.5,-0.5,-0.9,-0.6,-0.7,-0.7,-0.6,0,-1,-2.5,0,-1,-0.6,-0.72,-0.12,-2.5,-0.8,-0.3,-2.5,-0.8,-0.3,-0.6,-0.8,-0.3,-2.5,-0.8,-0.3,-0.6,-1.4,0,0,-1.4,0,-0.7,-0.7,-0.1,4.9,-1,-0.1,4.9,-0.5,-0.9,4.9,-0.7,-0.7,4.9,0,-1,4.9,-0.7,-0.1,4.9,-0.5,-0.5,7,-0.7,0,7,0,-0.7,7,-1,0,7.4,-2.8,-0.4,7.1,-2.57,-0.32,7.42,-4.9,0.1,4,-5.1,0.1,4,-5.1,-0.1,4,-4.9,-0.1,4,-5.1,0.1,1.6,-5.1,-0.1,1.6,-4.9,0.1,2.8,-4.9,-0.1,2.8,-0.58,-0.83,3.6,-0.72,-1.4,3.9,-0.69,-1.32,4.9,-0.58,-0.83,4.9,0.58,-0.83,3.6,0.72,-1.4,3.9,0.69,-1.32,4.9,0.58,-0.83,4.9,4.9,-0.1,2.8,5.1,-0.1,1.6,5.1,-0.1,4,4.9,-0.1,4,-0.8,0,-2.5,4.9,0.1,4,5.1,0.1,4,5.1,0.1,1.6,4.9,0.1,2.8,0.59,0.65,-0.77,0.8,0.3,-0.6,0.8,0,-2.5,-0.8,0,-2.5,0.8,-0.3,-0.6,0.72,-0.12,-2.5,0.8,0,-2.5,1,0,7.4,2.8,-0.4,7.1,2.57,-0.32,7.42,-0.7,0,7.4,0.5,-0.9,4.9,0.7,-0.7,4.9,0.5,-0.5,7,-4.9,0,2.8,-4.9,0,3.9,0.7,-0.1,4.9,0.7,0,7,1.4,0,0,4.9,0,2.8,4.9,0,3.9,1.4,0,3.9,1.4,0,-0.7,1.4,0,-0.7,0.7,-0.7,-0.6,0.8,-0.3,-0.6,0.5,-0.9,-0.6,1,-0.1,4.9,1,0.3,4.9,0.7,0,7.4,0.7,0.3,4.9,0.7,-0.1,4.9,0.56,0.66,2.8,0.53,0.75,0,1,0.3,2.8,1.1,0.3,0,0.37,0.57,4.9,0.7,0.3,4.9,0.5,0.49,7,0.7,0,7,0.5,0.49,7,1.4,0,3.9,1.4,0,0,1,0.3,2.8,1,0,3.9,1,-0.1,2.8,0.5,-0.9,-2.5,0.7,-0.7,-2.5,0.8,-0.3,-2.5,0.8,-0.3,-2.5,1,0.3,3.9,0.59,0.65,-0.77,0,0.7,2.8,0,1.4,4.5,0,0.59,4.9,0,3.5,6.8,0,3.5,8.1,0,1.4,7.3,0,0.7,7,0,0.7,7.3,-1,0.3,3.9,0,0.35,7.7,-0.25,0.24,7.7,-0.35,0,7.7,-0.25,-0.25,7.7,0,-0.35,7.7,0.25,-0.25,7.7,0.35,0,7.7,0.25,0.24,7.7,0,-0.2,-2.5,0.7,-0.7,-2.5,0.5,-0.9,-2.5,0,-1,-2.5,-0.5,-0.9,-2.5,-0.7,-0.7,-2.5,0,-0.2,-2.5,-0.72,-0.12,-2.5,0.72,-0.12,-2.5,0.25,0.24,7.7,0.35,0,7.7,-0.35,0,7.7,-0.25,0.24,7.7]
IndexedFaceSet23.coord = Coordinate24

Normal25 = Normal()
Normal25.DEF = "normalVector"
Normal25.vector = [-0.68,0.714,-0.166,-0.689,0.721,-0.072,0,0.965,-0.26,0,0.985,-0.175,-0.99,-0.016,-0.138,-0.999,-0.022,-0.037,0.567,-0.819,-0.093,0.561,-0.828,0,0,-1,0,0,-0.997,-0.071,-0.567,-0.819,-0.093,-0.561,-0.828,0,0.99,-0.016,-0.138,0.999,-0.022,-0.037,0.68,0.714,-0.166,0.689,0.721,-0.072,-0.351,0.889,-0.294,-0.868,-0.459,-0.19,-0.13,-0.982,-0.14,0.13,-0.982,-0.14,0.868,-0.459,-0.19,0.872,0.431,-0.231,-0.834,0.445,-0.327,0,0.929,-0.369,-0.88,0.401,-0.256,-0.799,0.577,0.169,-0.58,0.798,0.164,0,0.998,0.065,-0.862,0.486,0.146,0.886,0.219,0.408,0.799,0.577,0.169,0.834,0.445,-0.327,0.88,0.401,-0.256,-0,0.995,-0.096,0.842,0.534,-0.08,0.862,0.486,0.146,0.833,0.549,-0.073,-0.833,0.549,-0.073,-0.842,0.534,-0.08,-0.485,0.87,-0.089,-0.37,0.929,0,0,1,0,-0,1,-0.01,-0.592,0.796,-0.125,-0.573,0.818,0.05,-0.37,0.929,-0.01,0,1,-0.025,-0.487,0.873,0.036,-0.923,0.381,0.05,-0.683,0.704,0.195,0,0.99,0.14,-0.707,0.707,0,-0.385,0.912,0.141,0,0.966,0.259,-0.563,0.826,-0.037,-0.661,0.738,-0.138,-0.521,0.846,-0.115,0,-0.996,0.09,-0.773,-0.436,-0.461,-0.42,-0.781,-0.463,-0.474,-0.881,0,-0.871,-0.492,0,0,-0.891,-0.455,-0.917,0.399,0,-0.881,0.074,-0.467,-0.902,-0.429,-0.039,-0.09,-0.995,0.05,-0.451,-0.892,0,-0.28,-0.959,0.04,-0.468,-0.878,0.097,-0.877,-0.474,0.085,0,-0.997,0.072,-0.693,-0.72,0.045,-0.79,-0.562,0.244,-0.968,0.003,0.25,0,-0.966,0.257,0,0,1,-1,0,0,0.987,0,-0.16,1,0,0,-0.831,-0.551,-0.08,0.563,0.826,-0.037,0.661,0.738,-0.138,0.998,-0.037,-0.049,-0.987,0,-0.16,-0.998,-0.037,-0.049,0.831,-0.551,-0.08,0,-0.999,0.04,0,0.993,0.12,0.468,-0.878,0.097,0.877,-0.474,0.085,0.79,-0.562,0.244,-0.419,-0.897,-0.14,0.693,-0.72,0.045,0.968,0.003,0.25,0.521,0.846,-0.115,0.419,-0.897,-0.14,0.871,-0.492,0,0.902,-0.429,-0.039,0.474,-0.881,0,0.37,0.929,0,0.485,0.87,-0.089,0.573,0.818,0.05,0.592,0.796,-0.125,0.37,0.929,-0.01,0.487,0.873,0.036,0.923,0.381,0.05,0.683,0.704,0.195,0.385,0.912,0.141,0.707,0.707,0,0.42,-0.781,-0.463,0.773,-0.436,-0.461,0.917,0.399,0,0.881,0.074,-0.467,0.09,-0.995,0.05,0.451,-0.892,0,0.28,-0.959,0.04,0.42,0.901,-0.11,0,0.666,0.746,-0.481,0.468,0.741,-0.674,0,0.738,-0.475,-0.475,0.741,0,-0.674,0.738,0.475,-0.475,0.741,0.674,0,0.738,0.481,0.468,0.741,0,0,-1,0,-0.893,-0.45,-0.901,-0.224,-0.372,0.901,-0.224,-0.372,0.841,0.34,0.421,-0.841,0.34,0.421]
IndexedFaceSet23.normal = Normal25
Shape20.geometry = IndexedFaceSet23
Transform19.addChildren([Shape20])

Shape26 = Shape()
Shape26.DEF = "Canopy"

Appearance27 = Appearance()

Material28 = Material()
Material28.diffuseColor = [.25,.25,.25]
Material28.transparency = 0.8
Appearance27.material = Material28
Shape26.appearance = Appearance27

IndexedFaceSet29 = IndexedFaceSet(coordIndex = [2,32,33,-1,34,32,2,-1,35,36,37,-1,38,36,35,-1,39,40,41,-1,37,36,42,-1,2,43,44,-1,33,43,2,-1,45,37,42,46,-1,46,42,47,48,-1,33,45,46,43,-1,43,46,48,44,-1,34,49,50,32,-1,32,50,45,33,-1,49,38,35,50,-1,50,35,37,45,-1], creaseAngle = 0.5, normalIndex = [2,22,23,-1,24,22,2,-1,25,26,27,-1,28,26,25,-1,29,29,29,-1,27,26,30,-1,2,31,32,-1,23,31,2,-1,33,27,30,34,-1,34,30,35,36,-1,23,33,34,31,-1,31,34,36,32,-1,24,37,38,22,-1,22,38,33,23,-1,37,28,25,38,-1,38,25,27,33,-1], solid = False)

Coordinate30 = Coordinate()
Coordinate30.USE = "coordinates"
IndexedFaceSet29.coord = Coordinate30

Normal31 = Normal()
Normal31.USE = "normalVector"
IndexedFaceSet29.normal = Normal31
Shape26.geometry = IndexedFaceSet29
Transform19.addChildren([Shape26])

Shape32 = Shape()
Shape32.DEF = "MainBodyAndWingEdges"

Appearance33 = Appearance()

Material34 = Material()
Material34.diffuseColor = [.1796,.1914,.2382]
Appearance33.material = Material34
Shape32.appearance = Appearance33

IndexedFaceSet35 = IndexedFaceSet(coordIndex = [51,52,53,54,-1,55,56,52,51,-1,52,57,58,53,-1,56,59,57,52,-1,60,61,62,-1,57,59,63,-1,57,63,64,-1,58,57,64,-1,56,55,65,66,-1,67,68,69,-1,69,70,60,-1,71,54,36,-1,51,54,71,-1,72,51,71,-1,55,51,72,-1,72,73,55,-1,65,55,73,-1,68,67,74,-1,75,76,77,78,-1,76,79,80,77,-1,81,82,83,-1,84,75,78,85,-1,83,74,67,-1,67,86,87,83,-1,74,88,89,-1,88,74,83,-1,78,77,90,91,-1,77,80,92,90,-1,85,91,93,-1,85,78,91,-1,94,95,93,-1,94,93,91,-1,91,96,94,-1,96,91,90,-1,90,92,96,-1,100,101,102,103,-1,101,104,105,102,-1,104,106,107,105,-1,106,100,103,107,-1,106,104,101,100,-1,103,102,105,107,-1,116,117,118,119,-1,120,81,83,-1,121,122,123,124,-1,116,119,121,124,-1,48,125,126,127,-1,117,116,124,123,-1,128,72,71,49,-1,118,117,123,122,-1,119,118,122,121,-1,129,130,131,-1,89,88,135,97,-1,60,70,97,135,-1,70,89,97,-1,96,92,136,-1,136,137,96,-1,138,96,137,-1,120,83,87,-1,128,73,72,-1,137,141,138,-1,141,142,138,-1,126,147,127,-1,148,129,131,-1,137,149,150,-1,141,137,150,-1,136,92,80,151,-1,137,136,151,149,-1,132,152,153,-1,154,132,153,155,-1,132,154,156,152,-1,54,53,157,158,-1,158,157,159,160,-1,53,58,161,157,-1,157,161,162,159,-1,163,164,155,-1,165,162,161,-1,64,165,161,-1,64,161,58,-1,166,167,160,159,-1,168,169,146,-1,155,153,168,-1,36,54,125,-1,125,54,158,-1,125,158,126,-1,126,158,160,-1,160,147,126,-1,147,160,167,-1,170,146,169,-1,149,151,171,172,-1,151,80,79,171,-1,129,173,130,-1,150,149,172,174,-1,146,170,129,-1,129,148,143,146,-1,152,156,170,-1,129,170,156,-1,156,154,164,-1,154,155,164,-1,168,175,169,-1,175,153,152,169,-1,152,170,169,-1,48,47,125,-1,41,40,176,-1,71,38,49,-1,71,36,38,-1,61,135,88,-1,61,60,135,-1,68,185,69,-1,68,74,89,-1,68,89,70,185,-1], creaseAngle = 0.5, normalIndex = [39,40,41,42,-1,43,44,40,39,-1,40,45,46,41,-1,44,47,45,40,-1,48,48,48,-1,45,47,49,-1,45,49,50,-1,46,45,50,-1,44,43,51,52,-1,53,53,53,-1,41,41,41,-1,54,42,26,-1,39,42,54,-1,55,39,54,-1,43,39,55,-1,55,56,43,-1,51,43,56,-1,57,57,57,-1,58,59,60,61,-1,59,62,8,60,-1,63,63,63,-1,64,58,61,65,-1,66,66,66,-1,67,67,67,67,-1,8,8,8,-1,68,68,68,-1,61,60,69,70,-1,60,8,71,69,-1,65,70,72,-1,65,61,70,-1,73,74,72,-1,73,72,70,-1,70,75,73,-1,75,70,69,-1,69,71,75,-1,76,76,76,76,-1,77,77,77,77,-1,78,78,78,78,-1,79,79,79,79,-1,41,41,41,41,-1,8,8,8,8,-1,8,8,8,8,-1,80,80,80,-1,41,41,41,41,-1,77,77,77,77,-1,36,81,82,83,-1,84,84,84,84,-1,85,55,54,37,-1,79,79,79,79,-1,76,76,76,76,-1,86,86,86,-1,87,87,87,87,-1,88,88,88,88,-1,77,77,77,-1,75,71,89,-1,89,90,75,-1,91,75,90,-1,92,92,92,-1,85,56,55,-1,90,93,91,-1,93,94,91,-1,82,95,83,-1,96,96,96,-1,90,97,98,-1,93,90,98,-1,89,71,8,99,-1,90,89,99,97,-1,79,79,79,-1,88,88,88,88,-1,87,87,87,87,-1,42,41,100,101,-1,101,100,102,103,-1,41,46,104,100,-1,100,104,105,102,-1,106,106,106,-1,107,105,104,-1,50,107,104,-1,50,104,46,-1,108,109,103,102,-1,53,53,53,-1,41,41,41,-1,26,42,81,-1,81,42,101,-1,81,101,82,-1,82,101,103,-1,103,95,82,-1,95,103,109,-1,57,57,57,-1,97,99,110,111,-1,99,8,62,110,-1,112,112,112,-1,98,97,111,113,-1,114,114,114,-1,115,115,115,115,-1,8,8,8,-1,116,116,116,-1,77,77,77,-1,77,77,77,-1,79,79,79,-1,79,79,79,79,-1,79,79,79,-1,36,35,81,-1,117,117,117,-1,54,28,37,-1,54,26,28,-1,79,79,79,-1,79,79,79,-1,77,77,77,-1,77,77,77,-1,77,77,77,77,-1], solid = False)

Coordinate36 = Coordinate()
Coordinate36.USE = "coordinates"
IndexedFaceSet35.coord = Coordinate36

Normal37 = Normal()
Normal37.USE = "normalVector"
IndexedFaceSet35.normal = Normal37
Shape32.geometry = IndexedFaceSet35
Transform19.addChildren([Shape32])

Shape38 = Shape()
Shape38.DEF = "ExhaustExitFlatPanel"

Appearance39 = Appearance()

Material40 = Material()
Material40.diffuseColor = [.5,.5,.5]
Appearance39.material = Material40
Shape38.appearance = Appearance39

IndexedFaceSet41 = IndexedFaceSet(coordIndex = [186,187,188,189,190,-1,190,191,192,193,186,-1], creaseAngle = 0.5, normalIndex = [118,119,120,121,122,-1,122,123,124,125,118,-1], solid = False)

Coordinate42 = Coordinate()
Coordinate42.USE = "coordinates"
IndexedFaceSet41.coord = Coordinate42

Normal43 = Normal()
Normal43.USE = "normalVector"
IndexedFaceSet41.normal = Normal43
Shape38.geometry = IndexedFaceSet41
Transform19.addChildren([Shape38])

Shape44 = Shape()
Shape44.DEF = "ExhaustEntranceFrontBottomPart"

Appearance45 = Appearance()

Material46 = Material()
Material46.diffuseColor = [.2304,.2304,.2304]
Appearance45.material = Material46
Shape44.appearance = Appearance45

IndexedFaceSet47 = IndexedFaceSet(coordIndex = [194,130,173,195,196,197,-1,197,198,199,82,81,194,-1], creaseAngle = 0.5, normalIndex = [126,126,126,126,126,126,-1,126,126,126,126,126,126,-1], solid = False)

Coordinate48 = Coordinate()
Coordinate48.USE = "coordinates"
IndexedFaceSet47.coord = Coordinate48

Normal49 = Normal()
Normal49.USE = "normalVector"
IndexedFaceSet47.normal = Normal49
Shape44.geometry = IndexedFaceSet47
Transform19.addChildren([Shape44])

Shape50 = Shape()
Shape50.DEF = "ThirdPartFromNoseUnderCanopy"

Appearance51 = Appearance()

Material52 = Material()
Material52.diffuseColor = [.6,.6,.6]
Appearance51.material = Material52
Shape50.appearance = Appearance51

IndexedFaceSet53 = IndexedFaceSet(coordIndex = [12,200,201,15,-1,19,48,127,17,-1,15,201,128,5,-1,17,127,202,11,-1,11,202,200,12,-1,5,128,49,1,-1,48,19,44,-1,19,2,44,-1,34,1,49,-1,34,2,1,-1], creaseAngle = 0.5, normalIndex = [8,127,128,11,-1,15,36,83,13,-1,11,128,85,5,-1,13,83,129,7,-1,7,129,127,8,-1,5,85,37,1,-1,36,15,32,-1,15,2,32,-1,24,1,37,-1,24,2,1,-1], solid = False)

Coordinate54 = Coordinate()
Coordinate54.USE = "coordinates"
IndexedFaceSet53.coord = Coordinate54

Normal55 = Normal()
Normal55.USE = "normalVector"
IndexedFaceSet53.normal = Normal55
Shape50.geometry = IndexedFaceSet53
Transform19.addChildren([Shape50])

Shape56 = Shape()
Shape56.DEF = "RearExhaustExitPartLastPartOfMainBody"

Appearance57 = Appearance()

Material58 = Material()
Material58.diffuseColor = [.37,.37,.37]
Material58.shininess = .5
Appearance57.material = Material58
Shape56.appearance = Appearance57

IndexedFaceSet59 = IndexedFaceSet(coordIndex = [64,186,193,165,-1,203,204,164,163,-1,192,191,138,142,-1,191,190,96,138,-1,94,96,190,189,-1,95,94,189,188,-1,63,187,186,64,-1,62,61,205,206,-1], creaseAngle = 0.5, normalIndex = [50,118,125,107,-1,130,130,130,130,-1,124,123,91,94,-1,123,122,75,91,-1,73,75,122,121,-1,74,73,121,120,-1,49,119,118,50,-1,131,131,131,131,-1], solid = False)

Coordinate60 = Coordinate()
Coordinate60.USE = "coordinates"
IndexedFaceSet59.coord = Coordinate60

Normal61 = Normal()
Normal61.USE = "normalVector"
IndexedFaceSet59.normal = Normal61
Shape56.geometry = IndexedFaceSet59
Transform19.addChildren([Shape56])

Shape62 = Shape()
Shape62.DEF = "WingsAndTail"

Appearance63 = Appearance()

Material64 = Material()
Material64.emissiveColor = [.1796,.1914,.2382]
Appearance63.material = Material64
Shape62.appearance = Appearance63

IndexedFaceSet65 = IndexedFaceSet(colorPerVertex = False, coordIndex = [6,7,8,9,-1,9,8,7,6,-1,20,21,22,23,-1,23,22,21,20,-1,97,20,23,98,99,-1,99,98,23,20,97,-1,108,109,110,111,-1,111,110,109,108,-1,112,113,114,115,-1,115,114,113,112,-1,132,6,9,133,134,-1,134,133,9,6,132,-1,86,139,140,67,-1,67,140,139,86,-1,143,144,145,146,-1,146,145,144,143,-1,177,178,179,-1,179,178,177,-1,178,180,181,182,183,179,-1,179,183,182,181,180,178,-1,182,184,183,-1,183,184,182,-1,177,178,179,-1,179,178,177,-1,178,180,181,182,183,179,-1,179,183,182,181,180,178,-1,182,184,183,-1,183,184,182,-1], creaseAngle = 0.5, normalIndex = [50,118,125,107,-1,130,130,130,130,-1,124,123,91,94,-1,123,122,75,91,-1,73,75,122,121,-1,74,73,121,120,-1,49,119,118,50,-1,131,131,131,131,-1], solid = False)

Coordinate66 = Coordinate()
Coordinate66.USE = "coordinates"
IndexedFaceSet65.coord = Coordinate66

Normal67 = Normal()
Normal67.USE = "normalVector"
IndexedFaceSet65.normal = Normal67
Shape62.geometry = IndexedFaceSet65
Transform19.addChildren([Shape62])

Shape68 = Shape()
Shape68.DEF = "SecondPartAfterNose"

Appearance69 = Appearance()

Material70 = Material()
Material70.diffuseColor = [.6,.6,.6]
Appearance69.material = Material70
Shape68.appearance = Appearance69

IndexedFaceSet71 = IndexedFaceSet(coordIndex = [0,1,2,3,-1,4,5,1,0,-1,10,11,12,13,-1,14,15,5,4,-1,13,12,15,14,-1,16,17,11,10,-1,18,19,17,16,-1,3,2,19,18,-1], creaseAngle = 0.5, normalIndex = [0,1,2,3,-1,4,5,1,0,-1,6,7,8,9,-1,10,11,5,4,-1,9,8,11,10,-1,12,13,7,6,-1,14,15,13,12,-1,3,2,15,14,-1], solid = False)

Coordinate72 = Coordinate()
Coordinate72.USE = "coordinates"
IndexedFaceSet71.coord = Coordinate72

Normal73 = Normal()
Normal73.USE = "normalVector"
IndexedFaceSet71.normal = Normal73
Shape68.geometry = IndexedFaceSet71
Transform19.addChildren([Shape68])
Transform18.addChildren([Transform19])

Transform74 = Transform()
Transform74.DEF = "CockpitTransform"
Transform74.rotation = [1,0,0,-0.1]
Transform74.scale = [0.045,0.045,0.045]
Transform74.translation = [0,1,-10]

Inline75 = Inline()
Inline75.url = ["Cockpit.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Cockpit.x3d","Cockpit.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Cockpit.wrl"]
Transform74.addChildren([Inline75])
Transform18.addChildren([Transform74])

Transform76 = Transform()
Transform76.DEF = "SeatTransform"
Transform76.rotation = [-1,0,0,-0.1]
Transform76.scale = [0.9,0.9,0.9]
Transform76.translation = [0,0,-8.3]

Inline77 = Inline()
Inline77.url = ["Seat.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Seat.x3d","Seat.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Seat.wrl"]
Transform76.addChildren([Inline77])
Transform18.addChildren([Transform76])

Transform78 = Transform()
Transform78.DEF = "FrontWheelTransform"
Transform78.center = [0,2.5,0]
Transform78.rotation = [-1,0,0,1.92]
Transform78.translation = [0.7,-5.2,-6.5]
# Front wheel is taken from the Savage Library, modified and re-animated.(from F18 Blue Angel) 

Inline79 = Inline()
Inline79.url = ["FrontWheel.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontWheel.x3d","FrontWheel.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontWheel.wrl"]
Transform78.addChildren([Inline79])
Transform18.addChildren([Transform78])

Transform80 = Transform()
Transform80.DEF = "RearLeftWheelTransform"
Transform80.center = [0,2.5,0]
Transform80.rotation = [1,0,1,1.92]
Transform80.translation = [-2.95,-5,7]
# Rear wheels are taken from the Savage Library and re-animated (from F18 Blue Angel) 

Inline81 = Inline()
Inline81.url = ["RearLeftWheel.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearLeftWheel.x3d","RearLeftWheel.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearLeftWheel.wrl"]
Transform80.addChildren([Inline81])
Transform18.addChildren([Transform80])

Transform82 = Transform()
Transform82.DEF = "RearRightWheelTransform"
Transform82.center = [0,2.5,0]
Transform82.rotation = [-1,0,-1,1.92]
Transform82.translation = [2.95,-5,7]
# Rear wheels are taken from the Savage Library and re-animated (from F18 Blue Angel) 

Inline83 = Inline()
Inline83.url = ["RearRightWheel.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearRightWheel.x3d","RearRightWheel.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearRightWheel.wrl"]
Transform82.addChildren([Inline83])
Transform18.addChildren([Transform82])

Transform84 = Transform()
Transform84.DEF = "CockpitButtonsTransform"

Transform85 = Transform()
Transform85.DEF = "UpButtonTransform"
Transform85.rotation = [1,0,0,1.57]
Transform85.scale = [.008,.008,.008]
Transform85.translation = [-0.95,1.05,-10]

Shape86 = Shape()

Cylinder87 = Cylinder(height = 1, radius = 4)
Shape86.geometry = Cylinder87

Appearance88 = Appearance()

Material89 = Material()
Material89.diffuseColor = [1,0,0]
Material89.shininess = .8
Appearance88.material = Material89
Shape86.appearance = Appearance88
Transform85.addChildren([Shape86])

TouchSensor90 = TouchSensor()
TouchSensor90.DEF = "TouchSensorUp"
TouchSensor90.description = "click for gears up"
Transform85.addChildren([TouchSensor90])
Transform84.addChildren([Transform85])

Transform91 = Transform()
Transform91.DEF = "DownButtonTransform"
Transform91.rotation = [1,0,0,1.57]
Transform91.scale = [.008,.008,.008]
Transform91.translation = [-0.83,1.05,-10]

Shape92 = Shape()

Cylinder93 = Cylinder(height = 1, radius = 4)
Shape92.geometry = Cylinder93

Appearance94 = Appearance()

Material95 = Material()
Material95.diffuseColor = [1,1,0]
Material95.shininess = .8
Appearance94.material = Material95
Shape92.appearance = Appearance94
Transform91.addChildren([Shape92])

TouchSensor96 = TouchSensor()
TouchSensor96.DEF = "TouchSensorDown"
TouchSensor96.description = "click for gears down"
Transform91.addChildren([TouchSensor96])
Transform84.addChildren([Transform91])

Transform97 = Transform()
Transform97.DEF = "GearUpTextTransform"
Transform97.scale = [.06,.06,.06]
Transform97.translation = [-.65,1.55,-10]

Shape98 = Shape()

Text99 = Text()
Text99.string = ["RED Button","Gear Up"]
Shape98.geometry = Text99

Appearance100 = Appearance()

Material101 = Material()
Material101.diffuseColor = [1,0,0]
Appearance100.material = Material101
Shape98.appearance = Appearance100
Transform97.addChildren([Shape98])
Transform84.addChildren([Transform97])

Transform102 = Transform()
Transform102.DEF = "GearDownTextTransform"
Transform102.scale = [.06,.06,.06]
Transform102.translation = [-.65,1.35,-10]

Shape103 = Shape()

Text104 = Text()
Text104.length = [5.5]
Text104.string = ["YELLOW Button","Gear Down"]
Shape103.geometry = Text104

Appearance105 = Appearance()

Material106 = Material()
Material106.diffuseColor = [1,1,0]
Appearance105.material = Material106
Shape103.appearance = Appearance105
Transform102.addChildren([Shape103])
Transform84.addChildren([Transform102])

Transform107 = Transform()
Transform107.DEF = "FireButtonTransform"
Transform107.rotation = [1,0,0,1.57]
Transform107.scale = [.008,.008,.008]
Transform107.translation = [.52,1.6,-10]

Shape108 = Shape()

Cylinder109 = Cylinder(height = 1, radius = 4)
Shape108.geometry = Cylinder109

Appearance110 = Appearance()

Material111 = Material()
Material111.diffuseColor = [0,.75,.18]
Material111.shininess = .8
Appearance110.material = Material111
Shape108.appearance = Appearance110
Transform107.addChildren([Shape108])

TouchSensor112 = TouchSensor()
TouchSensor112.DEF = "FireSensor"
TouchSensor112.description = "click to fire"
Transform107.addChildren([TouchSensor112])
Transform84.addChildren([Transform107])

Transform113 = Transform()
Transform113.DEF = "FireTextTransform"
Transform113.scale = [.06,.06,.06]
Transform113.translation = [.36,1.5,-10]

Shape114 = Shape()

Text115 = Text()
Text115.string = ["Target Locked","      FIRE!..","(Green Button)"]
Shape114.geometry = Text115

Appearance116 = Appearance()

Material117 = Material()
Material117.diffuseColor = [0,.75,.18]
Appearance116.material = Material117
Shape114.appearance = Appearance116
Transform113.addChildren([Shape114])
Transform84.addChildren([Transform113])
Transform18.addChildren([Transform84])

Viewpoint118 = Viewpoint()
Viewpoint118.description = "F16 Close Look-up"
Viewpoint118.orientation = [-0.559,-0.827,-0.057,1.3534]
Viewpoint118.position = [-28.7,19.9,17.4]
Transform18.addChildren([Viewpoint118])

Viewpoint119 = Viewpoint()
Viewpoint119.description = "Cockpit"
Viewpoint119.orientation = [-1,0,0,0.1249]
Viewpoint119.position = [0,1.5,-7.9]
Transform18.addChildren([Viewpoint119])

Viewpoint120 = Viewpoint()
Viewpoint120.DEF = "LandingGearAnimationView"
Viewpoint120.description = "Landing Gear Animation View"
Viewpoint120.orientation = [-0.003,1,-0.012,2.5741]
Viewpoint120.position = [16.1,-5.8,-24.6]
Transform18.addChildren([Viewpoint120])

Viewpoint121 = Viewpoint()
Viewpoint121.description = "Cockpit Left View"
Viewpoint121.orientation = [-0.276,-0.922,-0.271,1.2338]
Viewpoint121.position = [-6.7,6.1,-3.9]
Transform18.addChildren([Viewpoint121])

Viewpoint122 = Viewpoint()
Viewpoint122.description = "F-16 Front View"
Viewpoint122.orientation = [-0.007,0.995,0.102,3.1152]
Viewpoint122.position = [-0.1,13.4,-65]
Transform18.addChildren([Viewpoint122])

Viewpoint123 = Viewpoint()
Viewpoint123.description = "Cockpit Target View"
Viewpoint123.orientation = [-0.834,-0.523,-0.176,0.0875]
Viewpoint123.position = [0,2.4,-7.9]
Transform18.addChildren([Viewpoint123])

Transform124 = Transform()
Transform124.DEF = "NoseAntennaTransform"
Transform124.rotation = [1,0,0,1.57]
Transform124.translation = [0,-.275,-21]

Shape125 = Shape()

Cylinder126 = Cylinder(radius = .05)
Shape125.geometry = Cylinder126

Appearance127 = Appearance()

Material128 = Material()
Material128.diffuseColor = [.5,.5,.5]
Material128.shininess = .5
Appearance127.material = Material128
Shape125.appearance = Appearance127
Transform124.addChildren([Shape125])
Transform18.addChildren([Transform124])
Scene17.addChildren([Transform18])

TimeSensor129 = TimeSensor()
TimeSensor129.DEF = "WheelUp"
TimeSensor129.cycleInterval = 8
Scene17.addChildren([TimeSensor129])

OrientationInterpolator130 = OrientationInterpolator()
OrientationInterpolator130.DEF = "GearUpInterpolator"
OrientationInterpolator130.key = [0,0.5,1.0]
OrientationInterpolator130.keyValue = [1,0,0,0.0,1,0,0,-0.79,1,0,0,-1.92]
Scene17.addChildren([OrientationInterpolator130])

ROUTE131 = ROUTE()
ROUTE131.fromField = "touchTime"
ROUTE131.fromNode = "TouchSensorUp"
ROUTE131.toField = "set_startTime"
ROUTE131.toNode = "WheelUp"
Scene17.addChildren([ROUTE131])

ROUTE132 = ROUTE()
ROUTE132.fromField = "fraction_changed"
ROUTE132.fromNode = "WheelUp"
ROUTE132.toField = "set_fraction"
ROUTE132.toNode = "GearUpInterpolator"
Scene17.addChildren([ROUTE132])

ROUTE133 = ROUTE()
ROUTE133.fromField = "value_changed"
ROUTE133.fromNode = "GearUpInterpolator"
ROUTE133.toField = "set_rotation"
ROUTE133.toNode = "FrontWheelTransform"
Scene17.addChildren([ROUTE133])

TimeSensor134 = TimeSensor()
TimeSensor134.DEF = "WheelDown"
TimeSensor134.cycleInterval = 8
Scene17.addChildren([TimeSensor134])

OrientationInterpolator135 = OrientationInterpolator()
OrientationInterpolator135.DEF = "GearDownInterpolator"
OrientationInterpolator135.key = [0,0.5,1.0]
OrientationInterpolator135.keyValue = [1,0,0,-1.92,1,0,0,-0.79,1,0,0,0.0]
Scene17.addChildren([OrientationInterpolator135])

ROUTE136 = ROUTE()
ROUTE136.fromField = "touchTime"
ROUTE136.fromNode = "TouchSensorDown"
ROUTE136.toField = "set_startTime"
ROUTE136.toNode = "WheelDown"
Scene17.addChildren([ROUTE136])

ROUTE137 = ROUTE()
ROUTE137.fromField = "fraction_changed"
ROUTE137.fromNode = "WheelDown"
ROUTE137.toField = "set_fraction"
ROUTE137.toNode = "GearDownInterpolator"
Scene17.addChildren([ROUTE137])

ROUTE138 = ROUTE()
ROUTE138.fromField = "value_changed"
ROUTE138.fromNode = "GearDownInterpolator"
ROUTE138.toField = "set_rotation"
ROUTE138.toNode = "FrontWheelTransform"
Scene17.addChildren([ROUTE138])
# Animation commands for Rear Right Wheel Starts 

TimeSensor139 = TimeSensor()
TimeSensor139.DEF = "RRearUp1"
TimeSensor139.cycleInterval = 8
Scene17.addChildren([TimeSensor139])

TimeSensor140 = TimeSensor()
TimeSensor140.DEF = "RRearDown1"
TimeSensor140.cycleInterval = 8
Scene17.addChildren([TimeSensor140])

OrientationInterpolator141 = OrientationInterpolator()
OrientationInterpolator141.DEF = "RRearInterUp1"
OrientationInterpolator141.key = [0,0.5,1.0]
OrientationInterpolator141.keyValue = [-1,0,-1,0.0,-1,0,-1,0.44,-1,0,-1,1.92]
Scene17.addChildren([OrientationInterpolator141])

OrientationInterpolator142 = OrientationInterpolator()
OrientationInterpolator142.DEF = "RRearInterDown1"
OrientationInterpolator142.key = [0,0.5,1.0]
OrientationInterpolator142.keyValue = [-1,0,-1,1.92,-1,0,-1,0.44,-1,0,-1,0.0]
Scene17.addChildren([OrientationInterpolator142])

ROUTE143 = ROUTE()
ROUTE143.fromField = "touchTime"
ROUTE143.fromNode = "TouchSensorDown"
ROUTE143.toField = "set_startTime"
ROUTE143.toNode = "RRearDown1"
Scene17.addChildren([ROUTE143])

ROUTE144 = ROUTE()
ROUTE144.fromField = "touchTime"
ROUTE144.fromNode = "TouchSensorUp"
ROUTE144.toField = "set_startTime"
ROUTE144.toNode = "RRearUp1"
Scene17.addChildren([ROUTE144])

ROUTE145 = ROUTE()
ROUTE145.fromField = "fraction_changed"
ROUTE145.fromNode = "RRearDown1"
ROUTE145.toField = "set_fraction"
ROUTE145.toNode = "RRearInterDown1"
Scene17.addChildren([ROUTE145])

ROUTE146 = ROUTE()
ROUTE146.fromField = "fraction_changed"
ROUTE146.fromNode = "RRearUp1"
ROUTE146.toField = "set_fraction"
ROUTE146.toNode = "RRearInterUp1"
Scene17.addChildren([ROUTE146])

ROUTE147 = ROUTE()
ROUTE147.fromField = "value_changed"
ROUTE147.fromNode = "RRearInterDown1"
ROUTE147.toField = "set_rotation"
ROUTE147.toNode = "RearRightWheelTransform"
Scene17.addChildren([ROUTE147])

ROUTE148 = ROUTE()
ROUTE148.fromField = "value_changed"
ROUTE148.fromNode = "RRearInterUp1"
ROUTE148.toField = "set_rotation"
ROUTE148.toNode = "RearRightWheelTransform"
Scene17.addChildren([ROUTE148])
# Animation commands for Rear Left Wheel 

TimeSensor149 = TimeSensor()
TimeSensor149.DEF = "LRearUp1"
TimeSensor149.cycleInterval = 8
Scene17.addChildren([TimeSensor149])

TimeSensor150 = TimeSensor()
TimeSensor150.DEF = "LRearDown1"
TimeSensor150.cycleInterval = 8
Scene17.addChildren([TimeSensor150])

OrientationInterpolator151 = OrientationInterpolator()
OrientationInterpolator151.DEF = "LRearInterUp1"
OrientationInterpolator151.key = [0,0.5,1.0]
OrientationInterpolator151.keyValue = [1,0,1,0.0,1,0,1,0.44,1,0,1,1.92]
Scene17.addChildren([OrientationInterpolator151])

OrientationInterpolator152 = OrientationInterpolator()
OrientationInterpolator152.DEF = "LRearInterDown1"
OrientationInterpolator152.key = [0,0.5,1.0]
OrientationInterpolator152.keyValue = [1,0,1,1.92,1,0,1,0.44,1,0,1,0.0]
Scene17.addChildren([OrientationInterpolator152])

ROUTE153 = ROUTE()
ROUTE153.fromField = "touchTime"
ROUTE153.fromNode = "TouchSensorDown"
ROUTE153.toField = "set_startTime"
ROUTE153.toNode = "LRearDown1"
Scene17.addChildren([ROUTE153])

ROUTE154 = ROUTE()
ROUTE154.fromField = "touchTime"
ROUTE154.fromNode = "TouchSensorUp"
ROUTE154.toField = "set_startTime"
ROUTE154.toNode = "LRearUp1"
Scene17.addChildren([ROUTE154])

ROUTE155 = ROUTE()
ROUTE155.fromField = "fraction_changed"
ROUTE155.fromNode = "LRearDown1"
ROUTE155.toField = "set_fraction"
ROUTE155.toNode = "LRearInterDown1"
Scene17.addChildren([ROUTE155])

ROUTE156 = ROUTE()
ROUTE156.fromField = "fraction_changed"
ROUTE156.fromNode = "LRearUp1"
ROUTE156.toField = "set_fraction"
ROUTE156.toNode = "LRearInterUp1"
Scene17.addChildren([ROUTE156])

ROUTE157 = ROUTE()
ROUTE157.fromField = "value_changed"
ROUTE157.fromNode = "LRearInterDown1"
ROUTE157.toField = "set_rotation"
ROUTE157.toNode = "RearLeftWheelTransform"
Scene17.addChildren([ROUTE157])

ROUTE158 = ROUTE()
ROUTE158.fromField = "value_changed"
ROUTE158.fromNode = "LRearInterUp1"
ROUTE158.toField = "set_rotation"
ROUTE158.toNode = "RearLeftWheelTransform"
Scene17.addChildren([ROUTE158])

Background159 = Background()
Background159.groundAngle = [1.309,1.570796]
Background159.groundColor = [0,0.3,.7,0,0.35,0.75,0,0.4,0.8]
Background159.skyAngle = [1.309,1.571]
Background159.skyColor = [0,0.3,0.8,0,0.5,1,1,1,1]
Scene17.addChildren([Background159])

Transform160 = Transform()
Transform160.DEF = "RightmostAmraamTransform"
Transform160.rotation = [-1,0,0,1.57]
Transform160.scale = [1.4,1.4,1.4]
Transform160.translation = [15.65,0,4.5]

Inline161 = Inline()
Inline161.DEF = "Amraam"
Inline161.url = ["../../Weapons/Missiles/Amraam.x3d","https://savage.nps.edu/Savage/Weapons/Missiles/Amraam.x3d","../../Weapons/Missiles/Amraam.wrl","https://savage.nps.edu/Savage/Weapons/Missiles/Amraam.wrl"]
Transform160.addChildren([Inline161])
Scene17.addChildren([Transform160])

Transform162 = Transform()
Transform162.DEF = "LeftmostAmraamTransform"
Transform162.rotation = [-1,0,0,1.57]
Transform162.scale = [1.4,1.4,1.4]
Transform162.translation = [-15.65,0,4.5]

Inline163 = Inline()
Inline163.USE = "Amraam"
Transform162.addChildren([Inline163])
Scene17.addChildren([Transform162])

Transform164 = Transform()
Transform164.DEF = "SidewinderHolderTransformRight"
Transform164.rotation = [0,1,0,1.57]
Transform164.scale = [6,3,3]
Transform164.translation = [9,-1.125,8]

Inline165 = Inline()
Inline165.DEF = "SidewinderHolder"
Inline165.url = ["SidewinderHolder.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/SidewinderHolder.x3d","SidewinderHolder.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/SidewinderHolder.wrl"]
Transform164.addChildren([Inline165])
Scene17.addChildren([Transform164])

Transform166 = Transform()
Transform166.DEF = "SidewinderHolderTransformLeft"
Transform166.rotation = [0,1,0,1.57]
Transform166.scale = [6,3,3]
Transform166.translation = [-8.45,-1.125,8]

Inline167 = Inline()
Inline167.USE = "SidewinderHolder"
Transform166.addChildren([Inline167])
Scene17.addChildren([Transform166])

Transform168 = Transform()
Transform168.DEF = "TurkishFlagTransformLeft"
Transform168.rotation = [0,-1,0,1.57]
Transform168.scale = [.3,.25,.3]
Transform168.translation = [-.01,8,19.5]

Inline169 = Inline()
Inline169.url = ["TurkishFlagLeft.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagLeft.x3d","TurkishFlagLeft.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagLeft.wrl"]
Transform168.addChildren([Inline169])
Scene17.addChildren([Transform168])

Transform170 = Transform()
Transform170.DEF = "TurkishFlagTransformRight"
Transform170.rotation = [0,1,0,1.57]
Transform170.scale = [.3,.25,.3]
Transform170.translation = [.01,8,20.5]

Inline171 = Inline()
Inline171.url = ["TurkishFlagRight.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagRight.x3d","TurkishFlagRight.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagRight.wrl"]
Transform170.addChildren([Inline171])
Scene17.addChildren([Transform170])

Transform172 = Transform()
Transform172.DEF = "AmraamHolderTransformLeft"
Transform172.translation = [-12,-.176,10.7]

Inline173 = Inline()
Inline173.DEF = "AmraamHolder"
Inline173.url = ["AmraamHolder.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/AmraamHolder.x3d","AmraamHolder.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/AmraamHolder.wrl"]
Transform172.addChildren([Inline173])
Scene17.addChildren([Transform172])

Transform174 = Transform()
Transform174.DEF = "AmraamHolderTransformRight"
Transform174.translation = [12,-.176,10.7]

Inline175 = Inline()
Inline175.USE = "AmraamHolder"
Transform174.addChildren([Inline175])
Scene17.addChildren([Transform174])

Transform176 = Transform()
Transform176.DEF = "AmraamInnerTransformRight"
Transform176.rotation = [-1,0,0,1.57]
Transform176.scale = [1.4,1.4,1.4]
Transform176.translation = [12,-1.6,4.5]

Inline177 = Inline()
Inline177.USE = "Amraam"
Transform176.addChildren([Inline177])
Scene17.addChildren([Transform176])

Transform178 = Transform()
Transform178.DEF = "AmraamInnerTransformLeft"
Transform178.rotation = [-1,0,0,1.57]
Transform178.scale = [1.4,1.4,1.4]
Transform178.translation = [-12,-1.6,4.5]

Inline179 = Inline()
Inline179.USE = "Amraam"
Transform178.addChildren([Inline179])
Scene17.addChildren([Transform178])

Transform180 = Transform()
Transform180.DEF = "SidewinderTransformLeft"
Transform180.rotation = [-1,0,0,1.57]
Transform180.scale = [1.6,1.6,1.6]
Transform180.translation = [-8.7,-2,3.5]

Inline181 = Inline()
Inline181.DEF = "Sidewinder"
Inline181.url = ["../../Weapons/Missiles/Sidewinder.x3d","https://savage.nps.edu/Savage/Weapons/Missiles/Sidewinder.x3d","../../Weapons/Missiles/Sidewinder.wrl","https://savage.nps.edu/Savage/Weapons/Missiles/Sidewinder.wrl"]
Transform180.addChildren([Inline181])
Scene17.addChildren([Transform180])

Transform182 = Transform()
Transform182.DEF = "SidewinderTransformRight"
Transform182.rotation = [-1,0,0,1.57]
Transform182.scale = [1.6,1.6,1.6]
Transform182.translation = [8.7,-2,3.5]

Inline183 = Inline()
Inline183.USE = "Sidewinder"
Transform182.addChildren([Inline183])
Scene17.addChildren([Transform182])

Transform184 = Transform()
Transform184.DEF = "FuelTankHolderTransformLeft"
Transform184.rotation = [0,1,0,1.57]
Transform184.scale = [1.5,1.5,1.5]
Transform184.translation = [-4.8,-1.125,6]

Inline185 = Inline()
Inline185.DEF = "FuelTankHolder"
Inline185.url = ["FuelTankHolder.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTankHolder.x3d","FuelTankHolder.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTankHolder.wrl"]
Transform184.addChildren([Inline185])
Scene17.addChildren([Transform184])

Transform186 = Transform()
Transform186.DEF = "FuelTankHolderTransformRight"
Transform186.rotation = [0,1,0,1.57]
Transform186.scale = [1.5,1.5,1.5]
Transform186.translation = [5.3,-1.125,6]

Inline187 = Inline()
Inline187.USE = "FuelTankHolder"
Transform186.addChildren([Inline187])
Scene17.addChildren([Transform186])

Transform188 = Transform()
Transform188.DEF = "FuelTankTransformRight"
Transform188.rotation = [-1,0,0,1.57]
Transform188.scale = [1.5,1.5,1.5]
Transform188.translation = [5,-2.85,5.5]

Inline189 = Inline()
Inline189.DEF = "FuelTank"
Inline189.url = ["FuelTank.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTank.x3d","FuelTank.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTank.wrl"]
Transform188.addChildren([Inline189])
Scene17.addChildren([Transform188])

Transform190 = Transform()
Transform190.DEF = "FuelTankTransformLeft"
Transform190.rotation = [-1,0,0,1.57]
Transform190.scale = [1.5,1.5,1.5]
Transform190.translation = [-5,-2.85,5.5]

Inline191 = Inline()
Inline191.USE = "FuelTank"
Transform190.addChildren([Inline191])
Scene17.addChildren([Transform190])

Transform192 = Transform()
Transform192.DEF = "InlineCoverOfPlaneTansform"

Shape193 = Shape()

Box194 = Box(size = [4.15,.1,20])
Shape193.geometry = Box194

Appearance195 = Appearance()

Material196 = Material()
Material196.diffuseColor = [.25,.25,.25]
Appearance195.material = Material196
Shape193.appearance = Appearance195
Transform192.addChildren([Shape193])
Scene17.addChildren([Transform192])

Transform197 = Transform()
Transform197.DEF = "TargetHelicopterTransform"
Transform197.translation = [16,-50,-500]

Inline198 = Inline()
Inline198.url = ["Target.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Target.x3d","Target.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Target.wrl"]
Transform197.addChildren([Inline198])
Scene17.addChildren([Transform197])

TimeSensor199 = TimeSensor()
TimeSensor199.DEF = "FireClock"
TimeSensor199.cycleInterval = 8
Scene17.addChildren([TimeSensor199])

PositionInterpolator200 = PositionInterpolator()
PositionInterpolator200.DEF = "MissilePath"
PositionInterpolator200.key = [0.0,.1,1.0]
PositionInterpolator200.keyValue = [-15.65,0,4.5,-15.65,-2,4.5,16,-50,-500]
Scene17.addChildren([PositionInterpolator200])

ROUTE201 = ROUTE()
ROUTE201.fromField = "touchTime"
ROUTE201.fromNode = "FireSensor"
ROUTE201.toField = "set_startTime"
ROUTE201.toNode = "FireClock"
Scene17.addChildren([ROUTE201])

ROUTE202 = ROUTE()
ROUTE202.fromField = "fraction_changed"
ROUTE202.fromNode = "FireClock"
ROUTE202.toField = "set_fraction"
ROUTE202.toNode = "MissilePath"
Scene17.addChildren([ROUTE202])

ROUTE203 = ROUTE()
ROUTE203.fromField = "value_changed"
ROUTE203.fromNode = "MissilePath"
ROUTE203.toField = "set_translation"
ROUTE203.toNode = "LeftmostAmraamTransform"
Scene17.addChildren([ROUTE203])

Viewpoint204 = Viewpoint()
Viewpoint204.DEF = "MissileLaunchView"
Viewpoint204.description = "Missile Fire View"
Viewpoint204.orientation = [0.094,-0.994,0.057,1.1716]
Viewpoint204.position = [-344.3,-142.8,-27.7]
Scene17.addChildren([Viewpoint204])

ROUTE205 = ROUTE()
ROUTE205.fromField = "isActive"
ROUTE205.fromNode = "FireSensor"
ROUTE205.toField = "set_bind"
ROUTE205.toNode = "MissileLaunchView"
Scene17.addChildren([ROUTE205])
# TODO fix type, add filter 
X3D0.scene = Scene17
