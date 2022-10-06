import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setContent("HeadsUpDisplayExample.x3d").setName("title"))
        .addMeta(X3Dpackage.meta().setContent("Prototype definition that demonstrates use of a simple HeadsUpDisplay (HUD) prototype that maintains a stable position for its children on the screen.").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("Leonard Daly and Don Brutzman").setName("creator"))
        .addMeta(X3Dpackage.meta().setContent("15 July 2006").setName("created"))
        .addMeta(X3Dpackage.meta().setContent("24 October 2016").setName("modified"))
        .addMeta(X3Dpackage.meta().setContent("HeadsUpDisplayPrototype.x3d").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://X3dGraphics.com").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/x3d/content/examples/X3dResources.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("Copyright 2006, Daly Realism and Don Brutzman").setName("rights"))
        .addMeta(X3Dpackage.meta().setContent("X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com").setName("subject"))
        .addMeta(X3Dpackage.meta().setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayExample.x3d").setName("identifier"))
        .addMeta(X3Dpackage.meta().setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("../license.html").setName("license")))
      .setScene(X3Dpackage.Scene()
        # Simple Heads-Up Display (HUD) Prototype\\n \\n Manages the display of a HUD and maintains its position on the screen.\\n Changes to fieldOfView (in Viewpoint node) will change screen position\\n \\n Fields:\\n hudSize Size of HUD (initializeOnly - SFVec3f) default=\"1 1 .01\"\\n hudColor Color of HUD (inputOutput - SFColor) default=\"1 1 1\"\\n screenOffset Offset of HUD. This field positions the HUD on the display screen (inputOutput - SFVec3f) default=\"0 0 0\"\\n hudGeometry Geometry to be placed on the HUD. Origin is center of HUD. (inputOutput - MFNode) default = []\\n position_changed Current viewer location (outputOnly - SFVec3f)\\n orientation_changed Current viewer orientation (outputOnly - SFRotation)\\n \\n \\n 

        .addChildren(X3Dpackage.ExternProtoDeclare().setAppinfo("Heads-up display (HUD) keeps child geometry aligned on screen in a consistent location").setName("HeadsUpDisplay").setUrl(["HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","HeadsUpDisplayPrototype.wrl#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.wrl#HeadsUpDisplay"])
          .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("offset position for HUD relative to current view location, default 0 0 -5").setName("screenOffset").setType("SFVec3f"))
          .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("X3D content positioned at HUD offset").setName("children").setType("MFNode"))
          .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("HUD position update (in world coordinates) relative to original location").setName("position_changed").setType("SFVec3f"))
          .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("HUD orientation update relative to original location").setName("orientation_changed").setType("SFRotation")))
        .addChildren(X3Dpackage.Background().setDEF("SandyShallowBottom").setGroundAngle([0.05,1.52,1.56,1.5707]).setGroundColor([0.2,0.2,0,0.3,0.3,0,0.5,0.5,0.3,0.1,0.3,0.4,0,0.2,0.4]).setSkyAngle([0.04,0.05,0.1,1.309,1.570]).setSkyColor([0.8,0.8,0.2,0.8,0.8,0.2,0.1,0.1,0.6,0.1,0.1,0.6,0.1,0.25,0.8,0.6,0.6,0.9]))
        .addChildren(X3Dpackage.Viewpoint().setDescription("Heads-up display (HUD)"))
        # ProtoDeclare is the \"cookie cutter\" template, ProtoInstance creates an actual occurrence 

        .addChildren(X3Dpackage.ProtoInstance().setDEF("HeadsUpDisplayInstance").setName("HeadsUpDisplay")
          # example: upper left-hand corner of screen (x=-2, y=1) and set back z=-5 from user view 

          .addFieldValue(X3Dpackage.fieldValue().setName("screenOffset").setValue("-0.75 1 -5"))
          .addFieldValue(X3Dpackage.fieldValue().setName("children")
            .addChildren(X3Dpackage.Shape()
              .setGeometry(X3Dpackage.Text().setString(["HUD text stays fixed","while user navigates"])
                .setFontStyle(X3Dpackage.FontStyle(setJustify = ["MIDDLE","MIDDLE"], setSize = 0.3)))
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDiffuseColor([0.894118,0.819608,1]))))))
        .addChildren(X3Dpackage.Inline().setUrl(["../HelloWorld.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.x3d","../HelloWorld.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.wrl"]))))

