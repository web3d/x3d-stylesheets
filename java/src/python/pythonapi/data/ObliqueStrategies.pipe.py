import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setContent("ObliqueStrategies.x3d").setName("title"))
        .addMeta(X3Dpackage.meta().setContent("Text scripting and animation example using Oblique Strategies card set by Brian Eno.").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("Don Brutzman, John Kelly, Ben Cheng").setName("creator"))
        .addMeta(X3Dpackage.meta().setContent("3 November 2013").setName("created"))
        .addMeta(X3Dpackage.meta().setContent("18 October 2015").setName("modified"))
        .addMeta(X3Dpackage.meta().setContent("oblique.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("ObliqueStrategies.txt").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("ObliqueStrategiesScript.js").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://music.hyperreal.org/artists/brian_eno/oblique/oblique.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://www.eno-web.co.uk/obliques.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://gothpunk.com/haiku-intro.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://www.rtqe.net/ObliqueStrategies/OSintro.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("https://en.wikipedia.org/wiki/Oblique_Strategies").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("Brian Eno, Oblique Strategies").setName("subject"))
        .addMeta(X3Dpackage.meta().setContent("images/ObliqueStrategiesEntryScreen.png").setName("Image"))
        .addMeta(X3Dpackage.meta().setContent("http://translate.google.com/translate_tts?tl=en&q=hello%20X3D").setName("audio"))
        .addMeta(X3Dpackage.meta().setContent("translate_tts_HelloX3D.mp3").setName("audio"))
        .addMeta(X3Dpackage.meta().setContent("translate_tts_HelloX3D.wav").setName("audio"))
        .addMeta(X3Dpackage.meta().setContent("multiliingual translation parameter").setName("TODO"))
        .addMeta(X3Dpackage.meta().setContent("http://stackoverflow.com/questions/9163988/download-mp3-from-google-translate-text-to-speech").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://www.greenbot.com/article/2105862/how-to-get-started-with-google-text-to-speech.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("under development, scene Sound/AudioClip triggering (or retrieved file format) not working").setName("warning"))
        .addMeta(X3Dpackage.meta().setContent("BSContact error: Script node TextScript: parse error: line 15 \" var strategy = [];").setName("warning"))
        .addMeta(X3Dpackage.meta().setContent("http://X3dGraphics.com/examples/X3dForAdvancedModeling/Inspiration/ObliqueStrategies.x3d").setName("identifier"))
        .addMeta(X3Dpackage.meta().setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("../license.html").setName("license")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.NavigationInfo().setType(["EXAMINE","ANY"]))
        .addChildren(X3Dpackage.Background().setSkyColor([0.419608,0.427451,1]))
        .addChildren(X3Dpackage.Transform().setScale([0.4,0.4,0.4]).setTranslation([0,1,0])
          .addChildren(X3Dpackage.TouchSensor().setDEF("RandomTextClickedSensor").setDescription("Select to see a new strategy"))
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Text().setString(["Oblique Strategies","","(Over One Hundred Worthwhile Dilemmas)","","by Brian Eno and Peter Schmidt"])
              .setFontStyle(X3Dpackage.FontStyle(setFamily = ["SANS"], setJustify = ["MIDDLE","MIDDLE"], setStyle = "BOLD").setDEF("MessageFont")))
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([1,1,1]))))
          .addChildren(X3Dpackage.Transform().setScale([10,3,1])
            .addChildren(X3Dpackage.Shape().setDEF("HeadlineClickSurface")
              .setGeometry(X3Dpackage.IndexedFaceSet(setCoordIndex = [0,1,2,3,-1], setSolid = False)
                .setCoord(X3Dpackage.Coordinate().setPoint([1,1,0,1,-1,0,-1,-1,0,-1,1,0])))
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setAmbientIntensity(0.245763).setDiffuseColor([0.34773,0.090909,0.005289]).setShininess(0.07).setSpecularColor([0.336735,0.051091,0.051091]).setTransparency(0.8))))))
        .addChildren(X3Dpackage.Script().setDEF("TextScript").setUrl(["./ObliqueStrategiesScript.js"])
          # initialize() method includes unit test to printAllStrategies() to console 

          # TODO insert field definitions here (index string_changed previous next random) and then animate! 

          .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("index for active strategy card, -1 means no selection").setName("index").setType("SFInt32").setValue("0"))
          .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("latest strategy card value").setName("string_changed").setType("MFString"))
          .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("url to invoke Google Translate").setName("textToSpeechUrl").setType("MFString"))
          .addField(X3Dpackage.field().setAccessType("outputOnly").setAppinfo("activate Sound node").setName("newCardTime").setType("SFTime"))
          .addField(X3Dpackage.field().setAccessType("inputOnly").setName("selectPreviousCard").setType("SFBool"))
          .addField(X3Dpackage.field().setAccessType("inputOnly").setName("selectNextCard").setType("SFBool"))
          .addField(X3Dpackage.field().setAccessType("inputOnly").setName("selectRandomCard").setType("SFBool"))
          .addField(X3Dpackage.field().setAccessType("initializeOnly").setAppinfo("controls console tracing").setName("traceEnabled").setType("SFBool").setValue("true")))
        .addChildren(X3Dpackage.Transform().setDEF("CardTransform").setScale([0.4,0.4,0.4]).setTranslation([0,-1.5,0])
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Text().setDEF("CardText")
              .setFontStyle(X3Dpackage.FontStyle(setFamily = ["SANS"], setJustify = ["MIDDLE","MIDDLE"], setStyle = "BOLD")))
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setDiffuseColor([1,1,1]))))
          .addChildren(X3Dpackage.ROUTE().setFromField("string_changed").setFromNode("TextScript").setToField("string").setToNode("CardText"))
          .addChildren(X3Dpackage.Sound().setDEF("CardSoundSpatialization").setMaxBack(100).setMaxFront(100).setMinBack(20).setMinFront(20)
            # Make sure the sound source AudioClip is audible at the user location 

            # Not all X3D players seem to use the .mp3 

            # &#38; is ampersand character, avoids escaping problems and inconsistencies in browsers and X3D players 

            # %20 is space character used in uri/url encoding 

            .setSource(X3Dpackage.AudioClip().setDEF("TextToSpeechAudioClip").setDescription("sends strategy text google translate").setUrl(["http://translate.google.com/translate_tts?tl=en&q=Feed%20the%20recording%20back%20out%20of%20the%20medium","translate_tts_mp3FileFormatNotSupported.wav"])))
          .addChildren(X3Dpackage.ROUTE().setFromField("textToSpeechUrl").setFromNode("TextScript").setToField("url").setToNode("TextToSpeechAudioClip"))
          .addChildren(X3Dpackage.ROUTE().setFromField("newCardTime").setFromNode("TextScript").setToField("startTime").setToNode("TextToSpeechAudioClip")))
        .addChildren(X3Dpackage.Transform().setScale([0.4,0.4,0.4]).setTranslation([-3.2,2.5,0])
          .addChildren(X3Dpackage.TouchSensor().setDEF("PreviousTextClickedSensor").setDescription("Select to see previous strategy"))
          .addChildren(X3Dpackage.ROUTE().setFromField("isActive").setFromNode("PreviousTextClickedSensor").setToField("selectPreviousCard").setToNode("TextScript"))
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Text().setString(["previous"])
              .setFontStyle(X3Dpackage.FontStyle().setUSE("MessageFont")))
            .setAppearance(X3Dpackage.Appearance().setDEF("InterfaceAppearance")
              .setMaterial(X3Dpackage.Material().setDiffuseColor([1,0,0.6]))))
          .addChildren(X3Dpackage.Transform().setScale([2,0.6,1])
            .addChildren(X3Dpackage.Shape().setDEF("TransparentClickSurface")
              # support Selectable Text with a scalable IFS 

              .setGeometry(X3Dpackage.IndexedFaceSet(setCoordIndex = [0,1,2,3,-1], setSolid = False)
                .setCoord(X3Dpackage.Coordinate().setPoint([1,1,0,1,-1,0,-1,-1,0,-1,1,0])))
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setTransparency(1))))))
        .addChildren(X3Dpackage.Transform().setScale([0.4,0.4,0.4]).setTranslation([3.5,2.5,0])
          .addChildren(X3Dpackage.TouchSensor().setDEF("NextTextClickedSensor").setDescription("Select to see next strategy"))
          .addChildren(X3Dpackage.ROUTE().setFromField("isActive").setFromNode("NextTextClickedSensor").setToField("selectNextCard").setToNode("TextScript"))
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Text().setString(["next"])
              .setFontStyle(X3Dpackage.FontStyle().setUSE("MessageFont")))
            .setAppearance(X3Dpackage.Appearance().setUSE("InterfaceAppearance")))
          .addChildren(X3Dpackage.Transform().setScale([1.2,0.6,1])
            .addChildren(X3Dpackage.Shape().setUSE("TransparentClickSurface"))))
        .addChildren(X3Dpackage.Transform().setScale([0.4,0.4,0.4]).setTranslation([-3.3,-0.5,0])
          .addChildren(X3Dpackage.TouchSensor().setUSE("RandomTextClickedSensor"))
          .addChildren(X3Dpackage.ROUTE().setFromField("isActive").setFromNode("RandomTextClickedSensor").setToField("selectRandomCard").setToNode("TextScript"))
          .addChildren(X3Dpackage.Shape()
            .setGeometry(X3Dpackage.Text().setString(["random"])
              .setFontStyle(X3Dpackage.FontStyle().setUSE("MessageFont")))
            .setAppearance(X3Dpackage.Appearance().setUSE("InterfaceAppearance")))
          .addChildren(X3Dpackage.Transform().setScale([1.8,0.6,1])
            .addChildren(X3Dpackage.Shape().setUSE("TransparentClickSurface"))))
        .addChildren(X3Dpackage.Transform().setScale([0.4,0.4,0.4]).setTranslation([3.3,-0.5,0])
          .addChildren(X3Dpackage.Anchor().setDEF("TextToSpeechAnchor").setDescription("text to speech in browser").setParameter(["target=_blank"]).setUrl(["http://translate.google.com/translate_tts?tl=en&q=Overtly%20resist%20change"])
            .addChildren(X3Dpackage.ROUTE().setFromField("textToSpeechUrl").setFromNode("TextScript").setToField("url").setToNode("TextToSpeechAnchor"))
            .addChildren(X3Dpackage.Shape()
              .setGeometry(X3Dpackage.Text().setString(["speech"])
                .setFontStyle(X3Dpackage.FontStyle().setUSE("MessageFont")))
              .setAppearance(X3Dpackage.Appearance().setUSE("InterfaceAppearance")))
            .addChildren(X3Dpackage.Transform().setScale([1.8,0.6,1])
              .addChildren(X3Dpackage.Shape().setUSE("TransparentClickSurface")))))))

