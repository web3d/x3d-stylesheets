from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="creator", content="John W Carlson"), 
    meta3 = meta(name="created", content="December 13 2015"), 
    meta4 = meta(name="title", content="force.x3d"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/force.x3d"), 
    meta6 = meta(name="description", content="beginnings of a force directed graph in 3D"), 
    meta7 = meta(name="generator", content="Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit")), 
   Scene8 = Scene(    Group9 = Group(     Shape10 = Shape(      Extrusion11 = Extrusion(DEF="extrusion", spine=[-50,-50,0,50,50,0], creaseAngle=0.785, crossSection=[1.00,0.00,0.92,-0.38,0.71,-0.71,0.38,-0.92,0.00,-1.00,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1.00,-0.00,-0.92,0.38,-0.71,0.71,-0.38,0.92,0.00,1.00,0.38,0.92,0.71,0.71,0.92,0.38,1.00,0.00]), 
      Appearance12 = Appearance(       Material13 = Material(diffuseColor=[0,1,0]))), 
     TimeSensor14 = TimeSensor(DEF="TourTime", loop=True), 
     Script15 = Script(DEF="MoveCylinder",       field16 = field(name="set_cycle", accessType="inputOnly", type="SFTime"), 
      field17 = field(name="spine", accessType="inputOutput", type="MFVec3f", value="-50 -50 0 50 50 0"),       sourceCode = '''\n"+
"ecmascript:\n"+
"\n"+
"                function set_cycle(value) {\n"+
"                        Browser.print(value);\n"+
"                        var endA = new SFVec3f(spine[0].x*Math.random()*2, spine[0].y*Math.random()*2, spine[0].z*Math.random()*2);\n"+
"                        var endB = new SFVec3f(spine[1].x*Math.random()*2, spine[1].y*Math.random()*2, spine[1].z*Math.random()*2);\n"+
"		        spine = new MFVec3f([endA, endB]);\n"+
"                }\n"+
"''', ), 
     ROUTE18 = ROUTE(fromNode="TourTime", fromField="cycleTime", toNode="MoveCylinder", toField="set_cycle"), 
     ROUTE19 = ROUTE(fromNode="MoveCylinder", fromField="spine_changed", toNode="extrusion", toField="spine"))))
