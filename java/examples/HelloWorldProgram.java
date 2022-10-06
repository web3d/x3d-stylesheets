/**
 * HelloWorldProgram.java
 *
 * Filename:     HelloWorldProgram.java
 * Description:  Example "smoke test" program to create an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL).
 * Identifier:   https://www.web3d.org/specifications/java/examples/HelloWorldProgram.java
 * Reference:    https://en.wikipedia.org/wiki/Smoke_testing_(software)
 * @author       Don Brutzman
 * Created:      6 September 2016
 * Revised:      see version control
 * Compile, run: ../build.xml
 * Reference:    https://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Scripts
 * Reference:    https://www.web3d.org/documents/specifications/19775-1/V3.3/Part01/components/scripting.html
 * Reference:    https://www.web3d.org/x3d/specifications/ISO-IEC-19777-2-X3DLanguageBindings-Java/Part2/X3D_Java.html
 * License:      ../license.html
 */

import java.io.File;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Date;
import org.w3c.dom.DOMImplementation;
import org.w3c.dom.Document;
import org.web3d.x3d.jsail.*;
import org.web3d.x3d.jsail.CADGeometry.*;
import org.web3d.x3d.jsail.Core.*;
import org.web3d.x3d.jsail.CubeMapTexturing.*;
import org.web3d.x3d.jsail.EnvironmentalEffects.*;
import org.web3d.x3d.jsail.fields.*;
import org.web3d.x3d.jsail.DIS.*;
import org.web3d.x3d.jsail.Geometry3D.*;
import org.web3d.x3d.jsail.Geospatial.*;
import org.web3d.x3d.jsail.Grouping.*;
import org.web3d.x3d.jsail.HAnim.*;
import org.web3d.x3d.jsail.Interpolation.*;
import org.web3d.x3d.jsail.Layering.*;
import org.web3d.x3d.jsail.Layout.*;
import org.web3d.x3d.jsail.Navigation.*;
import org.web3d.x3d.jsail.Networking.*;
import org.web3d.x3d.jsail.PointingDeviceSensor.*;
import org.web3d.x3d.jsail.Rendering.*;
import org.web3d.x3d.jsail.Scripting.*;
import org.web3d.x3d.jsail.Shaders.ComposedShader; // TODO whazzup?
import org.web3d.x3d.jsail.Shaders.PackagedShader;
import org.web3d.x3d.jsail.Shaders.ProgramShader;
import org.web3d.x3d.jsail.Shaders.ShaderPart;
import org.web3d.x3d.jsail.Shaders.ShaderProgram;
import org.web3d.x3d.jsail.Shape.*;
import org.web3d.x3d.jsail.Sound.*;
import org.web3d.x3d.jsail.Text.*;
import org.web3d.x3d.jsail.Texturing.*;
import org.web3d.x3d.jsail.Texturing3D.*;
import org.web3d.x3d.jsail.Time.*;
import org.web3d.x3d.jsail.X3DConcreteElement;
import org.web3d.x3d.jsail.X3DLoaderDOM;
// import org.web3d.x3d.util.x3duom.X3DUnifiedObjectModel40; TODO test

public class HelloWorldProgram
{
	/** Top-most object containing both head and Scene (and thus everything else) */
	static X3D x3dModel = new X3D();
	
	String thisClassName   = this.getClass().getName(); // use method from java.lang.Object
	String thisProgramFile = thisClassName + ".java";   // use method from java.lang.Object
	String thisSceneName   = thisClassName + "Output";  // must append filename extension
	
	// global scope
	private final head          head;
	private final Scene         scene;
	private final String   nameArtDeco01Material = "ArtDeco01Material";
	private final String        subdirectoryPath = "examples/";
	private       File          sourceFile;
	private final DecimalFormat formatPrecision2 = new DecimalFormat ("#0.00");
	private       String        compressionRatio;

	/** Constructor */
	HelloWorldProgram()
	{
            x3duomInspectionsTest();
        
            System.out.println ("===========================================");
            System.out.println ("X3DJSAIL version date: " + ConfigurationProperties.VERSION_DATE);
            System.out.println ("===========================================");

            // head and scene are globally visible, best practice is to instantiate/initialize them within constructor
            head  = new head();
            scene = new Scene();
            /* Scene can contain multiple top-level metadata nodes, so no setMetadata() method is provided */
            scene.addMetadata(new MetadataSet().setName("topLevelSceneMetadata")); // TODO consider utility methods addChild etc.

            System.out.println ("HelloWorldProgram() Constructor");
            System.out.println ("===========================================");
            System.out.println ("buildModelSceneGraph(); // construct this model, testing many variations");
                                 buildModelSceneGraph(); // construct this model, testing many variations
            System.out.println ("===========================================");
            System.out.println ("showSceneResults();     // test all serializer outputs");
                                 showSceneResults();     // test all serializer outputs
            System.out.println ("===========================================");
            System.out.println ("testBlenderLauncher();  // check Blender capabilities");
                                 testBlenderLauncher();  // check Blender capabilities
            System.out.println ("===========================================");
            System.out.println ("testMeshLabLauncher();  // check MeshLab capabilities");
                                 testMeshLabLauncher();  // check MeshLab capabilities
            System.out.println ("===========================================");
        }
	
	// reference: https://docs.oracle.com/javase/tutorial/getStarted/application/
	public static void main(String[] args)
	{
        System.out.println("===========================================");
        SpecialTestSection();

        System.out.println("===========================================");
        final String systemClassPath = ConfigurationProperties.getClassPath();
        System.out.println( "ConfigurationProperties.getClassPath()=" + systemClassPath);

        System.out.println("===========================================");
		HelloWorldProgram thisProgram = new HelloWorldProgram ();
        
        String result = thisProgram.validate(); // trace invocation
        System.out.println( "HelloWorldProgram self validation: " + result);
        
        System.out.println("===========================================");
        System.out.println("Quick test of CommandLine capability:");
		// facilitates debugging, allows simple testing
        org.web3d.x3d.jsail.CommandLine.run("-help");
        System.out.println("===========================================");
	}
        
	private String validate()
	{
            if (x3dModel == null)
                buildModelSceneGraph();
            return x3dModel.validationReport();
	}
	/**
     * Testing and debugging
     */
	private static void SpecialTestSection()
	{
        System.out.println("SpecialTest section:");
        
        // thanks to Laurent Renard <laurent.renard@geotoolkit.net> for exposing this bug and sleuthing the correct fix in FontStyle initialize() method
        FontStyle fontStyle1 = new FontStyle();
        FontStyle fontStyle2 = new FontStyle();
        
         // smoke tests for overloaded 'style' field
        ScreenFontStyle screenFontStyle3 = new ScreenFontStyle();
              fontStyle1.setStyle(FontStyle.STYLE_BOLD).setCssStyle("CSS Style;");
        screenFontStyle3.setStyle(FontStyle.STYLE_BOLD).setCssStyle("CSS Style;");
        System.out.println("      fontStyle1 getStyle()=" +       fontStyle1.getStyle() + " getCssStyle()=" +       fontStyle1.getCssStyle());
        System.out.println("screenFontStyle3 getStyle()=" + screenFontStyle3.getStyle() + " getCssStyle()=" + screenFontStyle3.getCssStyle());
        
        fontStyle1.setJustify(FontStyle.JUSTIFY_BEGIN_MIDDLE);
        fontStyle2.setJustify(FontStyle.JUSTIFY_END_MIDDLE);
        System.out.println("fontStyle1 justify=" + (new MFString(fontStyle1.getJustify())).toString()); // Arrays.toString(fontStyle1.getJustify()));
        System.out.println("fontStyle2 justify=" + (new MFString(fontStyle2.getJustify())).toString()); // Arrays.toString(fontStyle2.getJustify()));
        // now test to ensure no mutual interference, expected result true:
        System.out.println("justify field independence test #1 pass = " +
            Boolean.toString((new MFString(fontStyle1.getJustify())).toString().equals(FontStyle.JUSTIFY_BEGIN_MIDDLE) &&
                             (new MFString(fontStyle2.getJustify())).toString().equals(FontStyle.JUSTIFY_END_MIDDLE  )));
        // provided multiple convenience method needed for MF array values, e.g. getJustify(); getJustifyArray(); getJustifyList();
        System.out.println("justify field independence test #2 pass = " + 
            (fontStyle1.getJustifyString().equals(FontStyle.JUSTIFY_BEGIN_MIDDLE) &&
             fontStyle2.getJustifyString().equals(FontStyle.JUSTIFY_END_MIDDLE  )));
        
        PixelTexture pixelTexture = new PixelTexture();
        pixelTexture.setImage(SFImage.DEFAULT_VALUE);
        System.out.println("pixelTexture.getImage=" + pixelTexture.getImageList() + ", getWidth=" + pixelTexture.getWidth() +
                           ", getHeight=" + pixelTexture.getHeight() +   ", getNumberComponents=" + pixelTexture.getNumberComponents() +
                           ", getPixelsString()=" + pixelTexture.getPixelsString()); // empty by default
        int[] values = {1, 3, 4, 0xFF000088, 0x00FF0088, 0x0000FF88 }; // RGBA
        pixelTexture.setImage(values);
        pixelTexture.setImage(new SFImage(values));
        System.out.println("pixelTexture.getImage="    + pixelTexture.getImageList() + 
                           ", getWidth="               + pixelTexture.getWidth() +
                           ", getHeight="              + pixelTexture.getHeight() +   
                           ", getNumberComponents="    + pixelTexture.getNumberComponents() +
                           ", getPixelsString()="      + pixelTexture.getPixelsString() +
                           ", isValid()="              + pixelTexture.isValid() +
                           ", validate() diagnostic='" + pixelTexture.validate() + "'");
    }
	
	private void showSceneResults()
	{
		ConfigurationProperties.setPropertiesFileName(ConfigurationProperties.PROPERTIES_FILENAME_DEFAULT);
		System.out.println ("ConfigurationProperties.getPropertiesFileName()=" + ConfigurationProperties.getPropertiesFileName());
		ConfigurationProperties.loadProperties();
		ConfigurationProperties.setStripDefaultAttributes(true); // TODO test thoroughly
		ConfigurationProperties.setIndentCharacter(ConfigurationProperties.indentCharacter_DEFAULT);
		ConfigurationProperties.setIndentIncrement(ConfigurationProperties.indentIncrement_DEFAULT);
		// Restore default settings for spacing, increments and showing default attribute=value pairs
		ConfigurationProperties.setX3dCanonicalForm();
		ConfigurationProperties.initialize(); // restore all defaults

		System.out.println ();
		System.out.println (thisSceneName + ".java console output");
		System.out.println ("===========================================");
		String validationResults;
		System.out.println ("HelloWorldProgram validation results for resulting scene graph: ");
		try
		{
			// set true if needed to debug output files, otherwise false (strict)
			ConfigurationProperties.setValidationExceptionAllowed(false);
			validationResults = x3dModel.validate();
			if (validationResults.isEmpty())
				 System.out.println ("no errors detected.");
			else System.out.println (validationResults);
		}
		catch (Exception e)
		{
			System.out.flush(); // await completion of any pending output
//			System.out.println (e);
			e.printStackTrace(System.out);
			if (!ConfigurationProperties.isValidationExceptionAllowed())
				System.exit(1);
		}
		System.out.println ("===========================================");
		System.out.println ("x3dModel.toStringX3D()\n");
		System.out.println ( x3dModel.toStringX3D());
		System.out.println ("===========================================");
		System.out.println ("x3dModel.toStringXML()\n");//utility constructor
		System.out.println ( x3dModel.toStringXML());
		System.out.println ("===========================================");
		System.out.println ("x3dModel.toStringClassicVRML()\n");
		System.out.println ( x3dModel.toStringClassicVRML());
		System.out.println ("===========================================");
		System.out.println ("x3dModel.toStringVRML97()\n");
		System.out.println ( x3dModel.toStringVRML97());
		System.out.println ("===========================================");
		
		System.out.println ("Create .x3d (X3D XML Encoding) version of model");
		String savedFileName    = thisSceneName + X3D.FILE_EXTENSION_X3D;
		File   savedFile        = x3dModel.toFileX3D(savedFileName);
		boolean savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileX3D(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
			System.out.println (savedFile.getAbsolutePath());
		System.out.println ("===========================================");

		System.out.println ("Create .xml (X3D XML Encoding) version of model");
		savedFileName    = thisSceneName + X3D.FILE_EXTENSION_XML;
		savedFile        = x3dModel.toFileXML(savedFileName);
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileXML(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
			System.out.println (savedFile.getAbsolutePath());
		System.out.println ("===========================================");

		System.out.println ("Create pretty-print .html documentation of model");
		savedFileName    = thisSceneName + X3D.FILE_EXTENSION_HTML;
		savedFile        = x3dModel.toFileHtmlDocumentation(savedFileName);
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileHtmlDocumentation(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
			System.out.println (savedFile.getAbsolutePath());
		System.out.println ("===========================================");

		System.out.println ("Create .x3d (X3D XML Encoding) cleaned-up version of model using X3D Tidy");
		savedFileName    = thisSceneName + "Tidy" + X3D.FILE_EXTENSION_X3D;
		savedFile        = x3dModel.toFileX3dTidy(savedFileName);
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileX3dTidy(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
			System.out.println (savedFile.getAbsolutePath());
		System.out.println ("===========================================");

		System.out.println ("Create .md (Markdown) file for model meta information using X3dModelMetaToMarkdown.xslt");
		savedFileName    = thisSceneName + X3D.FILE_EXTENSION_MARKDOWN;
		savedFile        = x3dModel.toFileModelMetaMarkdown(savedFileName);
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileModelMetaMarkdown(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
			System.out.println (savedFile.getAbsolutePath());
		System.out.println ("===========================================");
		
		System.out.println ("Create X3D ClassicVRML Encoding of model");
		savedFileName   = thisSceneName + X3D.FILE_EXTENSION_CLASSICVRML;
		savedFile       = x3dModel.toFileClassicVRML(savedFileName);
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileClassicVRML(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
			System.out.println (savedFile.getAbsolutePath());
		System.out.println ("===========================================");
		
		System.out.println ("Create VRML97 Encoding of model");
		savedFileName   = thisSceneName + X3D.FILE_EXTENSION_VRML97;
		savedFile       = x3dModel.toFileVRML97(savedFileName);
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileVRML97(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
			System.out.println (savedFile.getAbsolutePath());
		System.out.println ("===========================================");
		
		ConfigurationProperties.setDebugModeActive(false);
		ConfigurationProperties.setXsltEngine(ConfigurationProperties.XSLT_ENGINE_SAXON);      // default
//		ConfigurationProperties.setXsltEngine(ConfigurationProperties.XSLT_ENGINE_NATIVE_JAVA); // built-in version
		System.out.println ("Create pretty-print HTML documentation of model using ConfigurationProperties.getXsltEngine()=" + ConfigurationProperties.getXsltEngine()
			+ " and stylesheet " + ConfigurationProperties.STYLESHEET_HTML_DOCUMENTATION);
		ConfigurationProperties.setDeleteIntermediateFiles(true);
		savedFileName   = thisSceneName + X3D.FILE_EXTENSION_HTML;
		savedFile       = x3dModel.toFileHtmlDocumentation(savedFileName);
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileHtmlDocumentation(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
			System.out.println (savedFile.getAbsolutePath());
		ConfigurationProperties.setDebugModeActive(false);
		System.out.println ("===========================================");
		
		ConfigurationProperties.setXsltEngine(ConfigurationProperties.XSLT_ENGINE_NATIVE_JAVA); // built-in version avoids unwanted line breaks
//		TODO fix line breaking
//      ConfigurationProperties.setXsltEngine(ConfigurationProperties.XSLT_ENGINE_SAXON);       // SAXON handles latest stylesheet
		System.out.println ("Create concise Java source of model using stylesheet " + ConfigurationProperties.STYLESHEET_JAVA);
		savedFileName   = thisSceneName + X3D.FILE_EXTENSION_JAVA;
		savedFile       = x3dModel.toFileJava(savedFileName, true); // include license
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileJava(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
		{
			System.out.println (savedFile.getAbsolutePath());
			System.out.println ("Test toStringJava()");
			System.out.println ();
			System.out.println (x3dModel.toStringJava());
		}
		System.out.println ("===========================================");
		
		ConfigurationProperties.setXsltEngine(ConfigurationProperties.XSLT_ENGINE_NATIVE_JAVA); // built-in version avoids unwanted line breaks
		System.out.println ("Create JSON Encoding of model using stylesheet " + ConfigurationProperties.STYLESHEET_JSON);
		savedFileName   = thisSceneName + X3D.FILE_EXTENSION_JSON;
		savedFile       = x3dModel.toFileJSON(savedFileName);
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileJSON(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
		{
			System.out.println (savedFile.getAbsolutePath());
			System.out.println ("Test toStringJSON()");
			System.out.println ();
			System.out.println (x3dModel.toStringJSON());
		}
		System.out.println ("===========================================");
//		System.out.println ("Test toStringJavaScript()");
//		System.out.println (x3dModel.toStringJavaScript()); // TODO
//		System.out.println ("===========================================");
		
		ConfigurationProperties.setXsltEngine(ConfigurationProperties.XSLT_ENGINE_SAXON);	   // default
		System.out.println ("Create Python source of model using stylesheet " + ConfigurationProperties.STYLESHEET_PYTHON);
		savedFileName   = thisSceneName + X3D.FILE_EXTENSION_PYTHON;
		savedFile       = x3dModel.toFilePython(savedFileName);
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFilePython(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
		{
			System.out.println (savedFile.getAbsolutePath());
			System.out.println ("Test toStringPython()");
			System.out.println ();
			System.out.println (x3dModel.toStringPython());
		}
		System.out.println ("===========================================");
		
		ConfigurationProperties.setXsltEngine(ConfigurationProperties.XSLT_ENGINE_SAXON);	   // default
		System.out.println ("Create displayable scene page rendered with X3DOM using stylesheet " + ConfigurationProperties.STYLESHEET_X3DOM);
		savedFileName   = thisSceneName + "X3dom" + X3D.FILE_EXTENSION_XHTML;
		savedFile       = x3dModel.toFileX3DOM(savedFileName);
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileX3DOM(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
			System.out.println (savedFile.getAbsolutePath());
		System.out.println ("===========================================");
		
		System.out.println ("Create displayable scene page rendered with X_ITE (formerly Cobweb) using stylesheet " + ConfigurationProperties.STYLESHEET_X3DOM);
		savedFileName   = thisSceneName + "X_ITE" + X3D.FILE_EXTENSION_HTML;
		savedFile       = x3dModel.toFileX_ITE(thisSceneName + X3D.FILE_EXTENSION_X3D, savedFileName);
		savedFileExists = !(savedFile == null);
		System.out.println ("helloWorld.toFileX3DOM(\"" + savedFileName + "\") success: " + savedFileExists);
		if (!(savedFile == null))
			System.out.println (savedFile.getAbsolutePath());
		System.out.println ("===========================================");
		
		System.out.println ("Reload and provide text output using Java DOM, which includes default attribute values");
		testX3DLoaderDOM();
		System.out.println ("===========================================");
		System.out.println ("Test loadModelFromFileX3D(String) and loadModelFromFileX3D(File)");
		X3D newX3DModel = new X3D();
		System.out.println ("checking .x3d encoding " +        thisSceneName + X3D.FILE_EXTENSION_X3D);
		boolean loadSuccess = newX3DModel.loadModelFromFileX3D(thisSceneName + X3D.FILE_EXTENSION_X3D); // also invokes loadModelFromFileX3D(File)
		String validationResult = newX3DModel.validate();
		if (validationResult.isEmpty())
			validationResult = "success";
		System.out.println ("newX3DModel " + thisSceneName + X3D.FILE_EXTENSION_X3D + " loadSuccess=" + loadSuccess + ", isEmpty()=" + newX3DModel.isEmpty() + ", validate()=" + validationResult);

		System.out.println ("checking .xml encoding " + thisSceneName + X3D.FILE_EXTENSION_XML);
		loadSuccess = newX3DModel.loadModelFromFileX3D( thisSceneName + X3D.FILE_EXTENSION_XML); // also invokes loadModelFromFileX3D(File)
		validationResult = newX3DModel.validate();
		if (validationResult.isEmpty())
			validationResult = "success";
		System.out.println ("newX3DModel " + thisSceneName + X3D.FILE_EXTENSION_XML + " loadSuccess=" + loadSuccess + ", isEmpty()=" + newX3DModel.isEmpty() + ", validate()=" + validationResult);

        System.out.println ("===========================================");
		System.out.println ("===========================================");
		System.out.println ("Check file sizes for various forms of compression");
		System.out.println ("Source file " + sourceFile.getName() + " " + sourceFile.length() + " bytes");
		// TODO Decimal Format
		System.out.println ("===========================================");
		System.out.println ("Test toFileEXI() with EXIficient");
		savedFileName   = thisSceneName + "_EXIFICIENT" + X3D.FILE_EXTENSION_EXI;
		File exiFile   = x3dModel.toFileEXI(savedFileName);
		compressionRatio = formatPrecision2.format(exiFile.length()/(double)sourceFile.length() * 100.0);
		System.out.println (exiFile.getName() + "  filesize " + exiFile.length() + " bytes, compression " + compressionRatio + "% of original");
		System.out.println ("===========================================");
		System.out.println ("Test fromFileEXI() with EXIficient");
		// savedFileName from before
		X3D exiModel = new X3D();
        // TODO are results canonical EXI?
		boolean fromFileEXIsuccess = exiModel.fromFileEXI(savedFileName);
		System.out.println ("  fromFileEXIsuccess=" + fromFileEXIsuccess + " for " + savedFileName);
		if (fromFileEXIsuccess)
		{
			String exiModelValidation = exiModel.validate();
			if    (exiModelValidation.isEmpty())
			{
				exiModelValidation += " success";
				System.out.println ("exiModel.validate() results: " + exiModelValidation);
			}
			else
			{
				System.out.println ("exiModel.validate() results:");
				System.out.println (exiModelValidation);
			}
		}
		System.out.println ("===========================================");
		System.out.println ("Test toFileEXI() with OpenEXI: testing in progress");
		// TODO set configuration parameter
		savedFileName   = thisSceneName + "OPENEXI" + X3D.FILE_EXTENSION_EXI;
		exiFile   = x3dModel.toFileEXI(savedFileName);
		compressionRatio = formatPrecision2.format(exiFile.length()/(double)sourceFile.length() * 100.0);
		System.out.println (exiFile.getName() + "  filesize " + exiFile.length() + " bytes, compression " + compressionRatio + "% of original");
		System.out.println ("===========================================");
		System.out.println ("Test fromFileEXI() with OpenEXI: TODO testing in progress, not fully implemented yet");
        // TODO are results canonical EXI?
        // TODO are results the same as EXIFICIENT outputs?
        // TODO once checked sat, add links and results to X3D Examples Archives outputs
		System.out.println ("===========================================");
		System.out.println ("Test toFileGZIP()");
		savedFileName   = thisSceneName + X3D.FILE_EXTENSION_GZIP;
		File gzipFile   = x3dModel.toFileGZIP(savedFileName);
		compressionRatio = formatPrecision2.format(gzipFile.length()/(double)sourceFile.length() * 100.0);
		System.out.println (gzipFile.getName() + "  filesize " + gzipFile.length() + " bytes, compression " + compressionRatio + "% of original");
		System.out.println ("===========================================");
		System.out.println ("Test toFileZip()");
		String savedZipName = thisSceneName + X3D.FILE_EXTENSION_ZIP;
		savedFileName   = thisSceneName + X3D.FILE_EXTENSION_X3D;
		File zipFile    = x3dModel.toFileZIP(savedZipName, savedFileName);
		compressionRatio = formatPrecision2.format(zipFile.length()/(double)sourceFile.length() * 100.0);
		System.out.println (zipFile.getName() + " filesize " + zipFile.length() + " bytes, compression " + compressionRatio + "% of original");
		
		System.out.println ("===========================================");
		System.out.println ("===========================================");
		System.out.println ("Test CommandLine invocations");
		String[] args = {"-help" };
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput.x3d", "-canonicalize", "-toFile", "HelloWorldProgramOutputCanonical.xml" };
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("now check result...");
		args = new String[] {"HelloWorldProgramOutputCanonical.xml", "-validate" };
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput.x3d", "-toX3D", "-toFile", "HelloWorldProgramOutput_CommandLine.x3d" };
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput.x3d", "-toVRML97", "-toFile", "HelloWorldProgramOutput_CommandLine.wrl" };
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput.x3d", "-toX3DV", "-toFile", "HelloWorldProgramOutput_CommandLine.x3dv" };
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput.x3d", "-toMarkdown",        "-toFile", "HelloWorldProgramOutputCatalog.md"};
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput.x3d", "-toMarkdown", "-toFile", "HelloWorldProgramOutput.md"};
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput.x3d",                        "-EXIFICIENT",   "-toEXI", "-toFile", "HelloWorldProgramOutput_CommandLine_EXIFICIENT.exi"};
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput_CommandLine_EXIFICIENT.exi", "-EXIFICIENT", "-fromEXI", "-toFile", "HelloWorldProgramOutput_CommandLine_EXIFICIENT.RoundTrip.x3d"};
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput.x3d",                        "-OpenEXI",      "-toEXI", "-toFile", "HelloWorldProgramOutput_CommandLine.OPENEXI.exi"};
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput_CommandLine.OPENEXI.exi",    "-OpenEXI",    "-fromEXI", "-toFile", "HelloWorldProgramOutput_CommandLine.OPENEXI.RoundTrip.x3d"};
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput.x3d", "-toGZIP", "-toFile", "HelloWorldProgramOutput_CommandLine.x3d.gz"};
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput_CommandLine.x3d.gz", "-fromGZIP"};
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput.x3d", "-toZIP", "-toFile", "HelloWorldProgramOutput_CommandLine.x3d.zip"};
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		args = new String[] {"HelloWorldProgramOutput_CommandLine.x3d.zip", "-fromZIP", "-toFile", "HelloWorldProgramOutput_CommandLineUnzipped.x3d"};
		System.out.println ("CommandLine " + Arrays.toString(args));
		CommandLine.run (args); // run these commands
		System.out.println ("===========================================");
		System.out.println ("ConfigurationProperties.setDebugModeActive(true);");
		ConfigurationProperties.setDebugModeActive(true);
        String results = x3dModel.validate(); // trace invocation
		if  (results.isEmpty())
			 results += "success";
		else results = "\n" + results;
		System.out.println ("x3dModel.validate() results with ConfigurationProperties.setDebugModeActive(true): " + results);
		System.out.println ("===========================================");
		System.out.println ("HelloWorldProgram complete.");
	}
	
	@SuppressWarnings({"UnusedAssignment", "static-access"}) // option to hide warnings when checking for allowable constructs during development
	private void buildModelSceneGraph()
	{
		// independent objects must be instantiated separately - verbose but necessary
	    component component1 = new component();
		unit   unitAngle = new unit();
		unit  unitLength = new unit();
		meta       meta0 = new meta(); // wild-card meta for current status
		meta       meta1 = new meta();
		meta       meta2 = new meta();
		meta       meta3 = new meta();
		meta       meta4 = new meta();
		meta       meta5 = new meta();
		meta       meta6 = new meta();
		meta       meta7 = new meta();
		meta       meta8 = new meta();
		meta       meta9 = new meta();
		meta       meta10 = new meta();
		meta       meta11 = new meta();
		meta       meta12 = new meta();
		meta       meta13 = new meta();
		meta       meta14 = new meta();
		meta       meta15 = new meta();
		meta       meta16 = new meta();
		meta       meta17 = new meta();
		meta       meta18 = new meta();
		meta       meta19 = new meta();
		
		x3dModel.setVersion (X3D.VERSION_4_0); // X3D.VERSION_3_3
		x3dModel.setProfile (X3D.PROFILE_FULL);
        x3dModel.setHtmlID  ("x3dModel.id");
        x3dModel.setCssClass("x3dModel.class");
        x3dModel.setCssStyle("x3dModel.style");
        boolean x3dVersionComparisonTest = x3dModel.supportsX3dVersion(X3D.VERSION_3_0);
        x3dModel.addComments("x3dVersionComparisonTest for this model: supportsX3dVersion(X3D.VERSION_3_0)=" + x3dVersionComparisonTest);
				
		x3dModel.setHead(head);
		// https://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#metaTags
		
		component1 = new component(component.NAME_NAVIGATION,3); // utility constructor
		component1.setName(component.NAME_NAVIGATION).setLevel(3);     // alternate form
		head.addComponent(component1);
		head.addComponent(new component().setName(component.NAME_SHADERS).setLevel(1));
        // utility constructors
        head.addComponent(component.NAME_CADGEOMETRY, 2);
        head.addComponent(component.NAME_DIS,         2);
        head.addComponent(component.NAME_H_ANIM,      1);
        // compare typical set and utility method in head
		head.addComponent(new component().setName("Grouping").setLevel(1));
		head.addComponent("Layering",1);

		unitAngle .setName("AngleRadiansFromDegrees").setCategory(unit.CATEGORY_ANGLE ).setConversionFactor(unit.CONVERSIONFACTOR_ANGLES_toRadiansFromDegrees);
		unitAngle .setName("AngleUnitConversion"    ).setCategory(unit.CATEGORY_ANGLE ).setConversionFactor(unit.CONVERSIONFACTOR_DEFAULT_VALUE);
		unitLength.setName("LengthMetersFromYards"  ).setCategory(unit.CATEGORY_LENGTH).setConversionFactor(unit.CONVERSIONFACTOR_LENGTH_toMetersFromYards);
		unitLength.setName("LengthUnitConversion"   ).setCategory(unit.CATEGORY_LENGTH).setConversionFactor(unit.CONVERSIONFACTOR_DEFAULT_VALUE);
		head.addUnit(unitAngle);
		head.addUnit(unitLength);
        // utility constructor
        head.addUnit("ForceFromPoundsToNewtons",unit.CATEGORY_FORCE,unit.CONVERSIONFACTOR_FORCE_toNewtonsFromPoundsForce);
        
        // utility constructor
		meta0.setName(meta.NAME_TITLE);
		meta0.setContent(thisSceneName + ".x3d");
		head.addMeta(meta0);
		head.clearMeta();
        head.addMeta(meta.NAME_TITLE, thisSceneName + ".x3d"); // replace meta0 with same single value
		
		meta1.setName(meta.NAME_INFO);
		meta1.setContent("continued development and testing in progress");
		meta1 = new meta(meta.NAME_INFO, "continued development and testing in progress"); // utility constructor
		head.addMeta(meta1);
		
		// demonstrate method pipelining for X3D statements when adding multiple meta statements
		head.addMeta(meta2 ).addMeta(meta3 ).addMeta(meta4 ).addMeta(meta5 ).addMeta(meta6 ).addMeta(meta7 )
		    .addMeta(meta8 ).addMeta(meta9 ).addMeta(meta10).addMeta(meta11).addMeta(meta12).addMeta(meta13)
			.addMeta(meta14).addMeta(meta15).addMeta(meta16).addMeta(meta17).addMeta(meta18).addMeta(meta19);
        
		// name="special test" with embedded space character throws exception as expected:
//		meta       meta20 = new meta();
//		meta20.setName("Special NMTOKEN space character test").setContent("test: name value cannot contain embedded space character");
//		head.addMeta(meta20); // adding a meta tag with space characters in name will throw a validation exception

		head.getMetaList();
		
		meta2.setName(meta.NAME_DESCRIPTION);
		meta2.setContent("Example " + this.getClass().getName() + " creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)");
		// demonstrate method pipelining for set accessors of simple-type attributes
		String urlLocation = "https://www.web3d.org/specifications/java/";
		meta3.setName(meta.NAME_REFERENCE).setContent(urlLocation + "X3DJSAIL.html");
		meta4.setName(meta.NAME_GENERATOR).setContent(thisSceneName + ".java");
		
		Date dateTimeValue = new Date(System.currentTimeMillis());
		SimpleDateFormat dateFormat = new SimpleDateFormat("d MMMM yyyy");
		meta6.setName(meta.NAME_MODIFIED).setContent(dateFormat.format(dateTimeValue));
		meta5.setName(meta.NAME_CREATED).setContent("6 September 2016");
		
		meta7.setName(meta.NAME_GENERATOR).setContent("X3D Java Scene Access Interface Library (X3DJSAIL)");
		meta8.setName(meta.NAME_GENERATOR).setContent(urlLocation + subdirectoryPath + thisProgramFile);
		meta9.setName(meta.NAME_GENERATOR).setContent("Netbeans https://www.netbeans.org");
		meta10.setName(meta.NAME_CREATOR).setContent("Don Brutzman");
		meta11.setName(meta.NAME_REFERENCE).setContent("https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/" 
						+ thisSceneName + ".x3d");
		meta12.setName(meta.NAME_REFERENCE).setContent("Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:");
		meta13.setName(meta.NAME_REFERENCE).setContent(thisSceneName + ".txt");
		meta14.setName(meta.NAME_REFERENCE).setContent(thisSceneName + ".x3dv");
		meta15.setName(meta.NAME_REFERENCE).setContent(thisSceneName + ".wrl");
		meta16.setName(meta.NAME_REFERENCE).setContent(thisSceneName + ".html");
		meta17.setName(meta.NAME_REFERENCE).setContent("https://savage.nps.edu/X3dValidator?url=" + 
															  urlLocation + subdirectoryPath + thisSceneName + ".x3d");
		meta18.setName(meta.NAME_IDENTIFIER).setContent(urlLocation + subdirectoryPath + thisSceneName + ".x3d");
		meta19.setName(meta.NAME_LICENSE).setContent("../license.html");
		
		// test utility method
		if (head.findMetaByName(meta.NAME_TITLE) == null) // tested satisfactorily
			System.out.println ("*** head.findMetaByName() method failed to find meta element...");
		
		x3dModel.setScene(scene);
		
		// ========== More object declarations, some with DEF values ==========
		
		String       defaultViewpointDEF = "DefaultView";
		String       topDownViewpointDEF = "TopDownView";
		ViewpointGroup  viewpointGroup = new ViewpointGroup(); //  requires <component name='Navigation' level='3'/>
		Viewpoint defaultViewpoint = new Viewpoint(defaultViewpointDEF);
		Viewpoint topDownViewpoint = new Viewpoint(topDownViewpointDEF);
		String          worldInfoDEFname = "WorldInfoDEF";
		WorldInfo   worldInfoNode  = new WorldInfo(worldInfoDEFname);
        worldInfoNode.setHtmlID  ("worldInfoNode.id");
        worldInfoNode.setCssClass("worldInfoNode.class");
        worldInfoNode.setCssStyle("worldInfoNode.style");
		WorldInfo   worldInfoCopy1 = new WorldInfo();
		WorldInfo   worldInfoCopy2 = new WorldInfo();
		String  logoGeometryTransformDEF = "LogoGeometryTransform";
                Transform    logoTransform = new Transform(logoGeometryTransformDEF);
		Anchor          siteAnchor = new Anchor("siteAnchor");
		Shape             boxShape = new Shape();
		Box                    box = new Box();
		String        lineShapeDEF = "LineShape";
		Shape         lineShape    = new Shape(lineShapeDEF);
	 IndexedLineSet indexedLineSet = new IndexedLineSet();
		Appearance   ilsAppearance = new Appearance();
		Material     ilsMaterial   = new Material();
		Appearance   boxAppearance = new Appearance();
		Material       boxMaterial = new Material();
		ImageTexture  x3dJsaiImage = new ImageTexture();
		String               boxPathAnimatorDEF = "BoxPathAnimator";
		PositionInterpolator boxPathAnimator    = new PositionInterpolator(boxPathAnimatorDEF);
		String      inlineSceneDEF = "inlineScene";
		Inline      inlineScene    = new Inline(inlineSceneDEF);
		IMPORT     importStatement = new IMPORT();
		EXPORT     exportStatement = new EXPORT();
		Collision  collision = new Collision();
		
		// ========== Construct scene graph parent-children relationships ==========
		
		defaultViewpoint.setDescription("Hello X3DJSAIL");
		float[] topDownPosition    = {0.0f, 100, 0};
		float[] topDownOrientation = {1, 0, 0, -1.570796f};
		topDownViewpoint.setDEF("TopDownView").setDescription("top-down view from above").setPosition(topDownPosition).setOrientation(topDownOrientation);
		viewpointGroup.setDescription("Available viewpoints").addChild(defaultViewpoint).addChild(topDownViewpoint);
//		viewpointGroup.addChild(siteAnchor); // test: confirmed node typing checks throw exception as expected
		scene.addChild(viewpointGroup); // utility method to set single X3DNode
		
        // test MFString setters
        scene.addChild(new NavigationInfo().setType(new MFString("\"EXAMINE\" \"FLY\" \"ANY\"")));
        // embedded-whitespace enumeration test: .setType(new MFString("\"EXAMINE     FLY\" \"ANY\"")));
        
		// test utility methods
		if (defaultViewpoint.findNodeByDEF(defaultViewpointDEF) == null) // tested satisfactorily
			System.out.println ("*** unit test: defaultViewpoint.findNodeByDEF() method failed...");
		if (scene.findNodeByDEF(defaultViewpointDEF) == null) // tested satisfactorily
			System.out.println ("*** unit test: scene.findNodeByDEF() method failed...");
		if (defaultViewpoint.findAncestorScene()== null) // tested satisfactorily
			System.out.println ("*** unit test: defaultViewpoint.findAncestorScene() method failed...");
		if (defaultViewpoint.findAncestorX3D()== null) // tested satisfactorily
			System.out.println ("*** unit test: defaultViewpoint.findAncestorX3D() method failed...");
		
		worldInfoNode.setTitle ("HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)");
		worldInfoCopy1.setUSE(worldInfoDEFname); // setUSE via string
		worldInfoCopy2.setUSE(worldInfoNode);    // setUSE via node
//		worldInfoCopy2.addComments("test exception at runtime"); // test sat: cannot add content to USE node
		scene.addChild(worldInfoNode).addChild(worldInfoCopy1).addChild(worldInfoCopy2);
        // utility methods for Scene
		scene.addMetadata  (new MetadataString("scene.addChildMetadata").setName("test").setValue("Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"));
		scene.addLayerSet  (new       LayerSet("scene.addChildLayerSetTest"));
		
		scene.addChild(logoTransform);
		float[] rootTranslationOffset = {0.0f, 1.5f, 0.0f};
			 logoTransform.setTranslation(rootTranslationOffset);
		SFVec3f translationSFVec3f = new SFVec3f(rootTranslationOffset); // alternate approach
		     logoTransform.setTranslation(translationSFVec3f.toFloatArray());        // alternate approach
		     logoTransform.setChildren(siteAnchor);
		        siteAnchor.addChild   (boxShape);
		
		String[] siteAddresses = {"../X3DJSAIL.html", urlLocation + "X3DJSAIL.html"};
		siteAnchor.setUrl(siteAddresses).setDescription("select for X3D Java SAI Library (X3DJSAIL) description");
		  boxShape.setAppearance(boxAppearance);
		String greenMaterialDEF = "GreenMaterial";
		boxAppearance.setMaterial(boxMaterial);
		  boxMaterial.setDEF(greenMaterialDEF);
		String[] imageUrl = {              "images/X3dJavaSceneAccessInterfaceSaiLibrary.png",
							 urlLocation + "examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"};
		x3dJsaiImage.setUrl(imageUrl);
		boxAppearance.setTexture(x3dJsaiImage);
		  boxMaterial.setDiffuseColor(Material.DIFFUSECOLOR_DEFAULT_VALUE);    // reset
		  boxMaterial.setDiffuseColor(SFColor.CYAN);                           // equivalent
		  boxMaterial.setDiffuseColor(new float[] {0, 1, 1});                        // equivalent
		  boxMaterial.setDiffuseColor((new SFColor(0x00FFFF)).toFloatArray()); // equivalent
		  boxMaterial.setDiffuseColor( new SFColor(0.0f, 1.0f, 1.0f));         // equivalent
		  boxMaterial.setEmissiveColor(new SFColor(SFColor.CYAN).complementRGB().scaleRGB(0.8f).normalizeClip());
		  
		  boxMaterial.setTransparency(0.1f);                                 // equivalent
		  boxMaterial.setTransparency((new SFFloat(0.1f)).getValue()); // equivalent
		  boxMaterial.setTransparency((new SFFloat(0.1 )).getValue()); // equivalent utility method also allowing double-precision downcasting
		
		float[] boxSize = {2.0f, 2.0f, 2.0f};
		box.setSize(boxSize).setCssClass("untextured").setDEF("test-NMTOKEN_regex.0123456789");
		boxShape.setDEF("BoxShape").setGeometry(box);
        boxShape.setHtmlID("BoxShapeID");
		
		scene.addChild(lineShape);
		lineShape.setAppearance(ilsAppearance);
		ilsAppearance.setMaterial(ilsMaterial);
		ilsMaterial.setEmissiveColor(SFColor.DARKORCHID);
		lineShape.setGeometry(indexedLineSet);
		 
		// note last coordinate only used by interpolator
		float[] boxPathPointArray = new float[] {0f, 1.5f, 0f,	2, 1.5f, 0,	2, 1.5f, -2,	-2, 1.5f, -2,	-2, 1.5f, 0,	0, 1.5f, 0};
		  int[] boxPathIndexArray = new   int[] {0, 1, 2, 3, 4, 0};
		float[] boxPathKeyArray   = new float[] {0, 0.125f, 0.375f, 0.625f, 0.875f, 1};
		MFVec3f     boxPath = new MFVec3f();
		 boxPath.setValue(boxPathPointArray);
		indexedLineSet.setCoordIndex(boxPathIndexArray);
		Coordinate boxCoordinateNode = new Coordinate();
		boxCoordinateNode.setPoint(boxPathPointArray);
		indexedLineSet.setCoord(boxCoordinateNode);
		indexedLineSet.addComments("Coordinate 3-tuple point count: " + indexedLineSet.getCoordCount());
		
		// test alternate type forms
		boxCoordinateNode.setPoint(new MFVec3f(new float[] {-8f,-9f,4f,-7f,-7f,5f,-3f,0f,5f}));				//  floats to  float array to MFVec3f
		boxCoordinateNode.setPoint(new MFVec3f(new double[] {-8f,-9f,4f,-7f,-7f,5f,-3f,0f,5f}));				//  floats to double array to MFVec3f
		boxCoordinateNode.setPoint(new MFVec3f(new double[] {-8,-9,4,-7,-7,5,-3,0,5}));						//    ints to double array to MFVec3f
		boxCoordinateNode.setPoint(new MFVec3f(new double[] {-8.0,-9.0,4.0,-7.0,-7.0,5.0,-3.0,0.0,5.0}));		// doubles to double array to MFVec3f
//		original SAI interface returns void, cannot be pipelined, candidate specification change
//		boxCoordinateNode.setPoint(new MFVec3f().setValue(new float[] {-8f,-9f,4f,-7f,-7f,5f,-3f,0f,5f}));	//  floats to float array to MFVec3f
		boxCoordinateNode.setPoint(new MFVec3f().setValue(new double[] {-8f,-9f,4f,-7f,-7f,5f,-3f,0f,5f}));	//  floats to double array to MFVec3f
		boxCoordinateNode.setPoint(new MFVec3f().setValue(new double[] {-8,-9,4,-7,-7,5,-3,0,5}));			// doubles to double array to MFVec3f
		boxCoordinateNode.setPoint(new MFVec3f().setValue(new double[] {-8.0,-9.0,4.0,-7.0,-7.0,5.0,-3.0,0.0,5.0}));// doubles to double array to MFVec3f
		boxCoordinateNode.setPoint(boxPathPointArray); // restore
				
		boxPathAnimator.setKey (boxPathKeyArray);
//		boxPathAnimator.setKey (boxPathIndexArray); // TODO alternate method allowing ints?
		boxPathAnimator.setKeyValue(boxPath);
		// Feature: node object constructor with string parameter sets DEF name
		String orbitClockDEF = "OrbitClock";
		TimeSensor orbitClock = new TimeSensor(orbitClockDEF);
		orbitClock.setCycleInterval(8).setEnabled(true).setLoop(true);
		ROUTE orbitClockROUTE = new ROUTE();
		orbitClockROUTE.setFromNode(orbitClockDEF)   .setFromField(TimeSensor.fromField_FRACTION_CHANGED)
					   .setToNode(boxPathAnimatorDEF).setToField  (CoordinateInterpolator.toField_SET_FRACTION);
		ROUTE orbitPositionROUTE = new ROUTE();
		orbitPositionROUTE.setFromNode(boxPathAnimatorDEF)    .setFromField(CoordinateInterpolator.fromField_VALUE_CHANGED)
					      .setToNode(logoGeometryTransformDEF).setToField  ("set_" + Transform.toField_TRANSLATION);	// test set_
		// TODO test addition of f suffix on a field name that doesn't include it already
		scene.addChild(boxPathAnimator).addChild(orbitClock).addChild(orbitClockROUTE).addChild(orbitPositionROUTE);
		
		// ========== Text ==========
		
		String         textTransformDEF = "TextTransform";
		Transform   textTransform = new Transform(textTransformDEF);
		Shape           textShape = new Shape();
		Appearance textAppearance = new Appearance();
		Material     textMaterial = new Material();
		Text          messageText = new Text();
		FontStyle     myFontStyle = new FontStyle();
		
		float[] textOffset = new float[] {0f, -1.5f, 0f};
		 textTransform.setTranslation(textOffset);
		     textShape.setAppearance(textAppearance);
		textAppearance.setMaterial(textMaterial); // demonstrate reuse of object
	 	  textMaterial.setUSE(greenMaterialDEF);  // demonstrate reuse of object
		if (!textMaterial.getUSE().equals(greenMaterialDEF)) // tested satisfactorily
			System.out.println ("*** setUSE()/getUSE() method failed...");
		
		   textShape.setGeometry(messageText);
		   String[]          textStringArray = new String[] {"X3D Java", "SAI Library", "X3DJSAIL"};
		   ArrayList<String> textStringArrayList = new ArrayList<>();
		   Collections.addAll(textStringArrayList, textStringArray);
		   messageText.setString(textStringArray);                         // test alternate method
		   messageText.setString(textStringArrayList);                     // test alternate method
		   messageText.setString(new MFString(textStringArray));     // test alternate method
		   messageText.setString("Hello single line of text");             // test alternate method
		   messageText.setString(new SFString("Hello single line")); // test alternate method
		   messageText.setString(new MFString(textStringArray));     // test alternate method
		   
		   messageText.setFontStyle(myFontStyle);
		   myFontStyle.setFamily (FontStyle.FAMILY_SERIF)
		              .setJustify(new String[] {"MIDDLE","MIDDLE"}) // alternate form, but no error checking until run time
		              .setJustify(FontStyle.JUSTIFY_MIDDLE_MIDDLE)  // preferred form, error checking at compile time
		              .setTopToBottom(FontStyle.TOPTOBOTTOM_DEFAULT_VALUE);
		   // backslash is Java String escape character, &quot; is equivalent XML character entity for " quotation mark
		   // Within a Java String, literal \" is read as " when parsed
		   messageText.addComments("Comment example A, plain quotation marks:  He said, \"Immel did it!\"");  
		   messageText.addComments("Comment example B, XML character entities: He said, &quot;Immel did it!&quot;");
		   MetadataSet metadataStringsSet = new MetadataSet().setName("EscapedQuotationMarksMetadataSet");
		   metadataStringsSet.addValue(new MetadataString("quotesTestC", // note use of utility constructor
								   "MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""));
//		   no need to use &quot; inside a Java String
//		   metadataStringsSet.addValue(new MetadataString().setName("quotesTestD").setValue(
//								   "MFString example D, XML character entities:   He said, \\&quot;Immel did it!\\&quot;"));
		   metadataStringsSet.addValue(new MetadataString("extraChildTest","checks MetadataSet addValue() method"));
		   messageText.setMetadata(metadataStringsSet);
			 
		scene.addChild(textTransform);
//		scene.addChild(new MFNode(shape1, textTransform)); // TODO alternate invocation syntax
		textTransform.addChild(textShape);
		collision.addComments("test containerField='proxy'")
			.setProxy(new Shape("ProxyShape")
			// test MFString alternatives, last one wins: MFString single-string XML syntax, MFString String[] array, String[] array
			.setGeometry(new Text().setString(new MFString(             "\"One, Two, Text\" \"\" \"He said, \"Immel did it!\"\" \"\"")))
			.setGeometry(new Text().setString(new MFString(new String [] {"One, Two, Text", "", "He said, \"Immel did it!\" \"\""}))) /* , "\\s", "\\\\" */
			.setGeometry(new Text().setString(new String [] {"One, Two, Text", "", "He said, \"Immel did it!\" \"\""})) /* , "\\s", "\\\\" */
				.addComments(" alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' ")
				.addComments(" alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' ")
				.addComments(" alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"})")
				.addComments(" reference: https://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html "));
		
		textTransform.addChild(collision);
		
		CommentsBlock commentsBlockDevo = new CommentsBlock();
		commentsBlockDevo.addComments("It's a beautiful world").addComments("... for you!")
				         .addComments("https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song)");
		         textTransform.addChild(commentsBlockDevo);
		
		// check that addComments support for X3D statements is working properly
		String[] commentArray12 = {"comment #1", "comment #2"};
		String[] commentArray34 = {"comment #3", "comment #4"};
		CommentsBlock anotherCommentsBlock = new CommentsBlock(commentArray12);
		anotherCommentsBlock.addComments(commentArray34);
		// now reset and perform an equivalent repeat for testing
		anotherCommentsBlock.clear().addComments(commentArray12).addComments(commentArray34); 
		head.addComments(anotherCommentsBlock); // test

		// show intermediate test results
//		System.out.println ("===========================================");
//		System.out.println ("textMaterial:");
//		System.out.println (    textMaterial.toStringX3D());
//		System.out.println ("===========================================");
//		System.out.println ("shape1:");
//		System.out.println (    boxShape.toStringX3D());
		
		float[]   rotationTupleArray1 = new float[]{0.0f, 1.0f, 0.0f, 0.0f};		// preferred default value
		@SuppressWarnings("MismatchedReadAndWriteOfArray")
		float[]   rotationTupleError1 = new float[]{0.0f};							// illegal value used for testing
		@SuppressWarnings("MismatchedReadAndWriteOfArray")
		float[]   rotationTupleError2 = new float[]{0.0f, 1.0f, 0.0f, 0.0f, 0.0f};	// illegal value used for testing
		@SuppressWarnings("MismatchedReadAndWriteOfArray")
		float[] rotationBadAxisError3 = new float[]{0.0f, 0.0f, 0.0f, 0.0f};		// illegal value used for testing
		SFRotation rotation1;
		rotation1 = new SFRotation();						// equivalent
		rotation1 = new SFRotation(SFRotation.DEFAULT_VALUE);		// equivalent
		rotation1 = new SFRotation(0, 1, 0, 0);			// equivalent constructor, integer axis
		rotation1 = new SFRotation(0.0, 1.0, 0.0, 0.0);		// equivalent constructor, doubles (cast to floats)
		rotation1 = new SFRotation(0.0f, 1.0f, 0.0f, 0.0f);	// equivalent constructor, floats  (matching base precision)
		rotation1 = new SFRotation(rotationTupleArray1);			// equivalent constructor, float array
//		rotation1 = new SFRotation(0, 0, 0, 0);				// illegal value, throws exception as expected
//		rotation1 = new SFRotation(rotation1Tuple);			// throws exception as expected
//		rotation1 = new SFRotation(rotationBadAxis);			// throws exception as expected
//		rotation1 = new SFRotation(rotation5Tuple);			// throws exception as expected

		rotation1.setValue(rotationTupleArray1);
//		rotation1.setValue(rotation1Tuple);	// throws exception as expected
//		rotation1.setValue(rotation5Tuple); // throws exception as expected
//		rotation1.setValue(rotationBadAxis);// throws exception as expected
		
		float[] rotation3Tuple = new float[]{0.0f, 1.0f, 0.0f, SFRotation.degreesToRadians(270.0f),	// float
											  0.0f, 1.0f, 0.0f, SFRotation.degreesToRadians(  0),		// integer
											  0.0f, 1.0f, 0.0f, SFRotation.degreesToRadians( 90.0) };	// double
		MFRotation rotation;
		
		rotation = new MFRotation();								// set empty, creates default (empty array)
//		rotation = new MFRotation(null);							// will not compile, which is good		
		rotation = new MFRotation(new float[]{});					// set empty float array, matches default
//		rotation = new MFRotation(new float[]{0.0f});				// test illegal array, throws exception as expected
//		rotation = new MFRotation(new float[]{0.0f, 1.0f, 0.0f, 0.0f,
//														 0.0f});				// test illegal array, throws exception as expected
		rotation = new MFRotation(rotationTupleArray1);				//  4 floats, single rotation
		rotation = new MFRotation(rotation3Tuple);					// 12 floats,  three rotations
		rotation = new MFRotation(SFRotation.DEFAULT_VALUE);	//  4 floats, single rotation
		
//		rotation = new MFRotation(SFRotation.DEFAULT_VALUE,			// TODO series of float arrays
//											  SFRotation.PREFERRED_DEFAULT_VALUE);// equivalent, one SFRotation

		String orientationInterpolatorDEF = "SpinInterpolator";
		OrientationInterpolator orientationInterpolator = new OrientationInterpolator(orientationInterpolatorDEF);
		orientationInterpolator.setKeyValue (rotation); // test utility method to allow object type
		orientationInterpolator.setKeyValue (rotation3Tuple); // set desired value for this scene
		
		float[] keyTime3Tuple  = new float[]{0f, 0.5f, 1f};		// preferred default value
		ArrayList<Float> keyTime3TupleList;
		keyTime3TupleList = new ArrayList<>();
		// TODO show copyArray to initialize list
//		keyTime3TupleList.addAll(Arrays.asList(keyTime3Tuple));
		keyTime3TupleList.clear();
		keyTime3TupleList.add(0.0f);
		keyTime3TupleList.add(0.5f);
		keyTime3TupleList.add(1f);	// 3 time-fraction floats correspond to 12 rotation floats
		
		orientationInterpolator.setKey(keyTime3Tuple);	// equivalent
		orientationInterpolator.setKey(keyTime3TupleList);// equivalent
		// TODO check tuple size that adding key, or adding keyValue, matches?
		// TODO what about during construction? perhaps add validate() methods instead
		
		// Feature: node object constructor with string parameter sets DEF name
		String spinClockDEF = "SpinClock";
		TimeSensor spinClock = new TimeSensor(spinClockDEF);
		spinClock.setCycleInterval(5).setEnabled(true).setLoop(true);
		
		ROUTE clockROUTE = new ROUTE();
		clockROUTE.setFromNode(orientationInterpolatorDEF).setFromField("value_changed")// equivalent, typos possible
				  .setToNode(textTransformDEF).setToField("rotation");
		clockROUTE.setFromNode(orientationInterpolatorDEF)
				  .setFromField(OrientationInterpolator.fromField_VALUE_CHANGED)	// equivalent, correctly named
				  .setToNode(textTransformDEF)
				  .setToField(Transform.toField_ROTATION);
		
		ROUTE  spinROUTE = new ROUTE();
		spinROUTE.setFromNode(spinClockDEF).setFromField("fraction_changed")
				 .setToNode(orientationInterpolatorDEF).setToField("set_fraction");	// equivalent, typos possible
		spinROUTE.setFromNode(spinClockDEF)
				 .setFromField(TimeSensor.fromField_FRACTION_CHANGED)
				 .setToNode(orientationInterpolatorDEF)
				 .setToField(OrientationInterpolator.toField_SET_FRACTION);	// equivalent, correctly named
		
		CommentsBlock spinnerComment = new CommentsBlock("repeatedly spin 180 degrees as a readable special effect");
		scene.addChild(spinnerComment).addChild(orientationInterpolator);
		scene.addChild(spinClock).addChild(spinROUTE); // ROUTE implements X3DChildNodeInterface
		scene.addChild(clockROUTE);
		
		String colorTypeConversionScriptDEF = "colorTypeConversionScript";
		Script colorTypeConversionScript = new Script(colorTypeConversionScriptDEF);
		String inputColorFieldName   = "colorInput";
		String outputColorsFieldName = "colorsOutput";
		field inputColorField  = new field(inputColorFieldName, field.TYPE_SFCOLOR, field.ACCESSTYPE_INPUTONLY); // equivalent
		inputColorField.setName(inputColorFieldName).setType(field.TYPE_SFCOLOR).setAccessType(field.ACCESSTYPE_INPUTONLY);  // can be reset once created
//		inputColorField.setName			("bad NMTOKEN value");		// fails validity test as expected
//		inputColorField.setType			("bad type value");			// fails validity test as expected
//		inputColorField.setAccessType	("bad accessType value");	// fails validity test as expected

		// must set all field parameters at instantiation so that it is valid
		field outputColorsField = new field(outputColorsFieldName, field.TYPE_MFCOLOR, field.ACCESSTYPE_OUTPUTONLY); 
		colorTypeConversionScript.addField(inputColorField);
		colorTypeConversionScript.addField(outputColorsField);
		colorTypeConversionScript.setSourceCode   ("ecmascript: // test 1 \n");
		colorTypeConversionScript.appendSourceCode("{\n	// test 2\n}\n");
		colorTypeConversionScript.clearSourceCode();
		colorTypeConversionScript.setSourceCode("ecmascript:" + "\n"
				+ "\n"
				+ "function " + inputColorFieldName + " (eventValue)" + " // Example source code" + "\n"
				+ "{" + "\n" 
				+ "   " + outputColorsFieldName + " = new MFColor(eventValue); // assigning value sends output event" + "\n" 
				+ "// Browser.print('" + inputColorFieldName + "=' + eventValue + ', " + outputColorsFieldName + "=' + " + outputColorsFieldName + " + '\\n');\n" 
				+ "}");
		// test utility method
		if (colorTypeConversionScript.findFieldByName(inputColorFieldName) == null) // tested satisfactorily
			System.out.println ("*** Script.findFieldByName() method failed...");
  
		String    backgroundDEF = "GradualBackground";
		String colorAnimatorDEF = "ColorAnimator";
		String    colorClockDEF = "ColorClock";
		Group backgroundGroup = new Group("BackgroundGroup");
		Background           background = new Background(backgroundDEF);
		MFColor         backgroundColor = new MFColor(); // TODO apply
        backgroundColor.setValue(SFColor.AQUA);
		ColorInterpolator colorAnimator = new ColorInterpolator(colorAnimatorDEF);
		TimeSensor           colorClock = new TimeSensor(colorClockDEF);
		colorClock.setCycleInterval(60).setLoop(true);
		colorAnimator.setKey     (keyTime3Tuple);     // equivalent
		colorAnimator.setKey     (keyTime3TupleList); // equivalent
		float[] colorArray = new float[9];
		System.arraycopy (SFColor.AZURE,  0, colorArray, 0, 3);
		System.arraycopy (SFColor.INDIGO, 0, colorArray, 3, 3);
		System.arraycopy (SFColor.AZURE,  0, colorArray, 6, 3);
		colorAnimator.setKeyValue(colorArray).addComments("AZURE to INDIGO and back again");
		
		ROUTE clockToColorAnimatorROUTE = new ROUTE();
		clockToColorAnimatorROUTE.setFromNode(colorClockDEF).setFromField(TimeSensor.fromField_FRACTION_CHANGED)
				                 .setToNode(colorAnimatorDEF).setToField(ColorInterpolator.toField_SET_FRACTION);
		ROUTE colorAnimatorToColorScriptROUTE = new ROUTE();
		colorAnimatorToColorScriptROUTE.setFromNode(colorAnimatorDEF).setFromField(ColorInterpolator.fromField_VALUE_CHANGED)
				                      .setToNode(colorTypeConversionScriptDEF).setToField(inputColorFieldName);
		ROUTE colorScriptToBackgroundROUTE = new ROUTE();
		colorScriptToBackgroundROUTE.setFromNode(colorTypeConversionScriptDEF).setFromField(outputColorsFieldName)
				                      .setToNode(backgroundDEF).setToField(Background.toField_SKYCOLOR);
		scene.addChild(backgroundGroup);
		backgroundGroup.addChild(background);
		backgroundGroup.addChild(colorTypeConversionScript).addChild(colorAnimator);
		backgroundGroup.addChild(colorClock);
		backgroundGroup.addChild(colorScriptToBackgroundROUTE);
		backgroundGroup.addChild(colorAnimatorToColorScriptROUTE);
		backgroundGroup.addChild(clockToColorAnimatorROUTE);
		
		      ProtoDeclare       artDeco01ProtoDeclare = new       ProtoDeclare  ();
		ExternProtoDeclare artDeco02ExternProtoDeclare = new ExternProtoDeclare  ();
		    ProtoInterface              protoInterface = new       ProtoInterface();
		         ProtoBody              protoBody      = new       ProtoBody     ();
			 // ProtoInstance has two constructors, either no value, or else both DEFname and prototypeName
		     ProtoInstance      artDeco01ProtoInstance = new       ProtoInstance ().setName("ArtDeco01Material");
//								                                                               .setContainerField ("material"); // not required, handled automatically by X3DJSAIL setMaterial method
		     ProtoInstance      artDeco02ProtoInstance = new       ProtoInstance ().setName("ArtDeco02Material")
								                                                               .setDEF ("ArtDeco02MaterialDEF");
//								                                                               .setContainerField ("material"); // not required, handled automatically by X3DJSAIL setMaterial method
			      Material           artDeco01Material = new       Material      ();
				  MFString      artDeco01_url_MFString = new       MFString      ();
				        String[]   artDeco01_url_StringArray = new       String[] { "initial value" };
				     field          description01Field = new       field         ();
				fieldValue     description01FieldValue = new       fieldValue    ();
				     field          description02Field = new       field         ();
				fieldValue     description02FieldValue = new       fieldValue    ();
			   TouchSensor		   internalTouchSensor = new	   TouchSensor   ();
						IS		  	        internalIS = new		IS			 ();
				   connect		  	   internalConnect = new		 connect		 ();

			  description01Field.setName("description")
							  .setAccessType(field.ACCESSTYPE_INPUTOUTPUT)
							  .setType(field.TYPE_SFSTRING)
							  .setValue("ArtDeco01Material prototype is a Material node")
							  .setAppinfo("tooltip for descriptionField");
			  description01FieldValue.setName(description01Field.getName())
//							  .setAppinfo("tooltip for description01Field") // TODO
							  .setValue("ArtDeco01Material can substitute for a Material node"); // overrides initial description01Field value
			  description02Field.setName("description")
							  .setAccessType(field.ACCESSTYPE_INPUTOUTPUT)
							  .setType(field.TYPE_SFSTRING)
							  .setValue("ArtDeco02Material is another Material node") // not legal for ExternProtoDeclare field, see test below
							  .setAppinfo("tooltip for descriptionField");
			  description02FieldValue.setName(description02Field.getName())
							  .setValue("ArtDeco02Material can substitute for another Material node"); // overrides initial description02Field value
			  artDeco01ProtoDeclare.setName(nameArtDeco01Material)
								   .setAppinfo("tooltip: ArtDeco01Material prototype is a Material node")
								   .setProtoInterface(protoInterface)
								   .setProtoBody(protoBody);
					 protoInterface.setField(null); // test setting null - operation succeessfully ignored as expected, no exception thrown
					 protoInterface.setField(description01Field);
					 // unit test: addField check for duplicate names of fields
//					 protoInterface.addField(description01Field); // successful test, throws exception as expected
					 protoInterface.addField(new field("enabled", field.TYPE_SFBOOL, field.ACCESSTYPE_INPUTOUTPUT,new SFBool(true).toString()));
					 protoBody.addChild(new CommentsBlock("Initial node of ProtoBody determines prototype node type")); // TODO vararg multiple strings
					 protoBody.addChild(artDeco01Material); // first node (other than comment) defines type, this case tests SFNode different than X3DChildNode

					 // the following diagnostic must follow addition of artDeco01Material as first node in protoBody
					 protoBody.addChild (new CommentsBlock("[HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"" + artDeco01ProtoDeclare.getNodeType() + "\""));
					 protoBody.addChild (new CommentsBlock(" presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types"))
					          .addChild(internalTouchSensor); // successful test of follow-on node
					 internalTouchSensor.setDescription("within ProtoBody").setIS(internalIS);
					 internalIS.addConnect(internalConnect); // careful if you use setConnect since that method wipes out other connections
					 internalConnect.setNodeField("description").setProtoField("description");
					 internalIS.addConnect(new connect().setProtoField("enabled").setNodeField(TimeSensor.toField_ENABLED));
					 
		scene.addChild(artDeco01ProtoDeclare);
		
		// Test WARNING_PROTOINSTANCE_NOT_FOUND works satisfactorily
//		ProtoDeclare artDeco03ProtoDeclare = new ProtoDeclare().setName("artDeco03");
//		scene.addChild (artDeco03ProtoDeclare);

		float[] diffuseColor    = {0.282435f, 0.085159f, 0.134462f};
		artDeco01Material.setAmbientIntensity(0.25f).setShininess(0.127273f)
				         .setDiffuseColor(diffuseColor)
				         .setSpecularColor(new SFColor(0.276305f, 0.11431f, 0.139857f));

		artDeco01_url_MFString.append("https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material");
		// MFString SAI interface returns void, so method pipelining not possible.  Repeat as necessary.
		artDeco01_url_MFString.append("https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material");

		// initial array size 1
		artDeco01_url_StringArray[0] = "https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material";
		// syntax to reinitialize size https://stackoverflow.com/questions/2564298/java-how-to-initialize-string
		artDeco01_url_StringArray = new String[] 
			{ "https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material",
			  "https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"
			};

		artDeco02ExternProtoDeclare.setName("ArtDeco02Material")
								   .setUrl(artDeco01_url_StringArray)    // variable-length String array
//								   .setUrl(artDeco01_url_StringArray[0]) // TODO test singleton String
//								   .setUrl(ArtDeco01_url_MFString)       // TODO test MFString
								   .setAppinfo("this is a different Material node");
		scene.addChild(artDeco02ExternProtoDeclare);
		// getNodeType() prerequisite: must first be added to Scene graph
		artDeco02ExternProtoDeclare.addComments(new CommentsBlock("[HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"" + 
				artDeco02ExternProtoDeclare.getNodeType() + "\"")); // returns "UNKNOWN_EXTERNALPROTOTYPE_SUPPORT_NOT_IMPLEMENTED" as expected
				// TODO X3DJSAIL needs to load/inspect ProtoDeclare corresponding to ExternProtoDeclare url
		
		// ExternProtoDeclare field definitions cannot include value, they are defined within original ProtoDeclare
//		artDeco02ExternProtoDeclare.setField(description02Field); // throws exception as expected
		description02Field.clearValues(); // clear prior value
		artDeco02ExternProtoDeclare.setField(description02Field);
		// Note that getting a fieldList lets programmer reach into contained elements
//		artDeco02ExternProtoDeclare.getFieldList().get(0).setValue("test exception, this should fail validation"); // proceeds unchecked
		artDeco02ExternProtoDeclare.validate(); // test satisfactory: validation catches preceding error

		artDeco01ProtoInstance.setFieldValue(description01FieldValue);
		// test addFieldValue validate() check for duplicate names of fields
//		ArtDeco01ProtoInstance.addFieldValue(description01FieldValue); // test sat, throws exception as expected
		
		artDeco02ProtoInstance.setFieldValue(description02FieldValue);
		// getNodeType prerequisite: ProtoInstance must first be connected to scene graph
		// TODO need to distinguish between ProtoInstance and ProtoDeclare/ExternProtoDeclare and field/fieldValue; also avoid duplicate naming
				 
		scene.addChild(new CommentsBlock("Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place")); 
		// TODO test for improper node type when ProtoInstance is added in wrong place
//		scene.addChild(ArtDeco01ProtoInstance); 
//		scene.addChild(ArtDeco02ProtoInstance); 

		Shape testShape1 = new Shape("TestShape1"); // constructor also initializes DEF
		Shape testShape2 = new Shape("TestShape2");
		Shape testShape3 = new Shape("TestShape3");
		Appearance testAppearance1 = (new Appearance("TestAppearance1")).setMaterial(new Material("TestToBeOverridden1"));
		Appearance testAppearance2 = (new Appearance("TestAppearance2")).setMaterial(new Material("TestToBeOverridden2"));
		Appearance testAppearance3 = (new Appearance("TestAppearance3")).setMaterial(new Material("TestToBeOverridden3"));
		testAppearance1.addComments("ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java").setMaterial(artDeco01ProtoInstance); // successful use of overloaded, specially typed method
		testAppearance2.addComments("ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java").setMaterial(artDeco02ProtoInstance); // successful use of overloaded, specially typed method
		// test ProtoInstance USE
		testAppearance3.addComments("ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. ");
		testAppearance3.setMaterial(new ProtoInstance().setUSE(artDeco02ProtoInstance.getDEF())); // do not apply prototypeName on USE node
//								                             .setContainerField ("material")); // not required, handled automatically by X3DJSAIL setMaterial method
		testShape1.setAppearance(testAppearance1);
		testShape2.setAppearance(testAppearance2);
		testShape3.setAppearance(testAppearance3);
		testShape1.setGeometry(new Sphere().setRadius(0.001f)); // provide initial children to silence superflous Schematron warnings
		testShape2.setGeometry(new Cone().setHeight(0.001f).setBottomRadius(0.001f));
		testShape3.setGeometry(new Cylinder().setHeight(0.001f).setRadius(0.001f));
		scene.addChild(testShape1).addChild(testShape2).addChild(testShape3);

		// prerequisite met: must first be fully connected to scene graph for function getNodeType() to find predecessor declaration
		artDeco01ProtoInstance.addComments(new CommentsBlock("[HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"" + artDeco01ProtoInstance.getNodeType() + "\""));
		artDeco02ProtoInstance.addComments(new CommentsBlock("[HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"" + artDeco02ProtoInstance.getNodeType() + "\""));
	 	
		// Inline/IMPORT/EXPORT validation testing (cannot be self-referential or may cause recursion error)
		inlineScene.setUrl("someOtherScene.x3d").addUrl(urlLocation + subdirectoryPath + "someOtherScene.x3d");
//		           .addUrl(urlLocation + "/java/" + "someOtherScene.x3d"); // TODO 
		importStatement.setInlineDEF(inlineSceneDEF).setImportedDEF(worldInfoDEFname).setAS(worldInfoDEFname + "2"); // overloaded DEF test sat
		exportStatement.setLocalDEF(worldInfoDEFname).setAS(worldInfoDEFname + "3");
		scene.addChild(inlineScene).addChild(importStatement).addChild(exportStatement);
		
		/** Test declarative style, prototype fields IS/connect and scripting */
		ProtoDeclare materialModulatorPrototype = new ProtoDeclare ("MaterialModulator");
		materialModulatorPrototype
			.setAppinfo("mimic a Material node and modulate fields as an animation effect")
			.setDocumentation("https://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html")
			.setProtoInterface(
				new ProtoInterface()
					.addField(new field()
						.setName("enabled")
						.setType(field.TYPE_SFBOOL)
						.setAccessType( field.ACCESSTYPE_INPUTOUTPUT)
						.setValue(true)					  // equivalent, strongly typed
						.setValue(new MFBool(true)) // equivalent
						.setValue(SFBool.TRUE))     // equivalent
					.addField(new field()
						.setName("diffuseColor")
						.setType(field.TYPE_SFCOLOR)
						.setAccessType( field.ACCESSTYPE_INPUTOUTPUT)
						.setValue(new SFColor().setValueByString("0.8 0.8 0.8"))	  // equivalent, strongly typed
						.setValue((SFColor.toString(SFColor.DEFAULT_VALUE)))) // equivalent
					.addField(new field (
						"emissiveColor",field.TYPE_SFCOLOR,field.ACCESSTYPE_INPUTOUTPUT, 
//							new SFColor().setValue(0x00007F).toString())) // hex value for half blue
//							new SFColor(0x00007F).toString())) // equivalent (TODO recheck math)
							(new SFColor(0.05f, 0.05f, 0.5f)).toString())) // equivalent
					.addField(new field (
						"specularColor",field.TYPE_SFCOLOR,field.ACCESSTYPE_INPUTOUTPUT, 
							(SFColor.toString(SFColor.BLACK))))
					.addField(new field (
						"transparency", field.TYPE_SFFLOAT,field.ACCESSTYPE_INPUTOUTPUT, 
							"0.0"))
					.addField(new field (
						"shininess",    field.TYPE_SFFLOAT,field.ACCESSTYPE_INPUTOUTPUT, 
							Float.toString(0.0f)))
					.addField(new field (
						"ambientIntensity",field.TYPE_SFFLOAT,field.ACCESSTYPE_INPUTOUTPUT, 
							SFFloat.toString(0.0f)))
//						.setChildren((Material newMaterial = new Material ("MaterialNode"))))
						// TODO fix syntax or add utility methods
			);
		ProtoBody materialModulatorProtoBody = new ProtoBody();
		materialModulatorPrototype.setProtoBody(materialModulatorProtoBody);
		materialModulatorProtoBody.addChild(
			new Material("MaterialNode")
				.setIS(new IS()
					.addConnect(new connect().setNodeField("diffuseColor"    ).setProtoField("diffuseColor"))
					.addConnect(new connect().setNodeField("emissiveColor"   ).setProtoField("emissiveColor"))
					.addConnect(new connect().setNodeField("specularColor"   ).setProtoField("specularColor"))
					.addConnect(new connect().setNodeField("transparency"    ).setProtoField("transparency"))
					.addConnect(new connect().setNodeField("shininess"       ).setProtoField("shininess"))
					.addConnect(new connect().setNodeField("ambientIntensity").setProtoField("ambientIntensity"))
			));
		materialModulatorProtoBody.addChild(
			new CommentsBlock ("Only first node (the node type) is renderable, others are along for the ride"))
		                          .addChild(
			new Script ("MaterialModulatorScript")
				.addField(new field().setName("enabled").setType(field.TYPE_SFBOOL)
					.setAccessType(field.ACCESSTYPE_INPUTOUTPUT))
				.addField(new field().setName("diffuseColor").setType(field.TYPE_SFCOLOR)
					.setAccessType(field.ACCESSTYPE_INPUTOUTPUT))
				.addField(new field().setName("newColor").setType(field.TYPE_SFCOLOR)
					.setAccessType(field.ACCESSTYPE_OUTPUTONLY))
				.addField(new field().setName("clockTrigger").setType(field.TYPE_SFTIME)
					.setAccessType(field.ACCESSTYPE_INPUTONLY))
				.setIS(new IS()
					.addConnect(new connect().setNodeField("enabled"     ).setProtoField("enabled"))
					.addConnect(new connect().setNodeField("diffuseColor").setProtoField("diffuseColor")))
				.setSourceCode(new StringBuilder("ecmascript:\n").append(
"function initialize ()\n").append(
"{\n").append(
"    newColor = diffuseColor; // start with correct color\n").append(
"}\n").append(
"function set_enabled (newValue)\n").append(
"{\n").append(
"	enabled = newValue;\n").append(
"}\n").append(
"function clockTrigger (timeValue)\n").append(
"{\n").append(
"    if (!enabled) return;\n").append(
"    red   = newColor.r;\n").append(
"    green = newColor.g;\n").append(
"    blue  = newColor.b;\n").append(
"    \n").append(
"    // note different modulation rates for each color component, % is modulus operator\n").append(
"    newColor = new SFColor ((red + 0.02) % 1, (green + 0.03) % 1, (blue + 0.04) % 1);\n").append(
"	if (enabled)\n").append(
"	{\n").append(
"		Browser.print ('diffuseColor=(' + red + ',' + green + ',' + blue + ') newColor=' + newColor.toString() + '\\n');\n").append(
"	}\n").append(
"}"))
			);
		scene.addChild(materialModulatorPrototype);
//		scene.getElementByName("ProtoDeclare", "MaterialModulator"); // test sat

		createDeclarativeShapeTests();
		
		String   soundExampleUrl = "https://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d";
		String[]    soundFileUrl = { "chimes.wav", "https://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav" };
		scene.addChild(new Sound()
				.setLocation(0, 1.6f, 0).addComments("set sound-ellipsoid location height at 1.6m to match typical avatar height")
				.setSource(new AudioClip()
						.setUrl(soundFileUrl).setDescription("chimes")
						.addComments("Scene example fragment from " + soundExampleUrl)));
		
		String   movieExampleUrl = "https://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d";
		String[]    movieFileUrl = { "mpgsys.mpg", "https://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg" };
		scene.addChild(new Sound()
				.setLocation(0, 1.6f, 0).addComments("set sound-ellipsoid location height at 1.6m to match typical avatar height")
				.setSource(new MovieTexture()
					.setDescription("mpgsys.mpg from ConformanceNist suite")
					.setUrl(movieFileUrl)
					.addComments("Scene example fragment from " + movieExampleUrl)
					.addComments("Expected containerField='source', allowed containerField values=" + 
							new MFString(new MovieTexture().getContainerFieldAlternateValues()).toStringX3D())));
                CommentsBlock testComments = new CommentsBlock ();
                String result;
                result = ((Anchor.isNode() == true) && (siteAnchor.isNode() == true)) ? "success" : "failure";
                testComments.addComments("Test " + result + ":  Anchor.isNode()="      +  Anchor.isNode()      + ",              siteAnchor.isNode()=" + siteAnchor.isNode());
                
                result = ((Anchor.isStatement() == false) && (siteAnchor.isStatement() == false)) ? "success" : "failure";
                testComments.addComments("Test " + result + ":  Anchor.isStatement()=" +  Anchor.isStatement() + ",        siteAnchor.isStatement()="  + siteAnchor.isStatement());
		
                result = ((ROUTE.isNode() == false) && (orbitPositionROUTE.isNode() == false)) ? "success" : "failure";
                testComments.addComments("Test " + result + ":   ROUTE.isNode()="      +   ROUTE.isNode()      + ",     orbitPositionROUTE.isNode()="  + orbitPositionROUTE.isNode());
		
                result = ((ROUTE.isStatement() == true) && (orbitPositionROUTE.isStatement() == true)) ? "success" : "failure";
                testComments.addComments("Test " + result + ":   ROUTE.isStatement()=" +   ROUTE.isStatement() + ", orbitPositionROUTE.isStatement()=" + orbitPositionROUTE.isStatement());
                
                result = ((CommentsBlock.isNode() == false) && (CommentsBlock.isNode() == false)) ? "success" : "failure";
                testComments.addComments("Test " + result + ": CommentsBlock.isNode()="      + CommentsBlock.isNode()      + ",           testComments.isNode()="  + testComments.isNode());
		
                result = ((CommentsBlock.isStatement() == false) && (testComments.isStatement() == false)) ? "success" : "failure";
                testComments.addComments("Test " + result + ": CommentsBlock.isStatement()=" + CommentsBlock.isStatement() + ",      testComments.isStatement()="  + testComments.isStatement());
                scene.addComments (testComments);
                
                Extrusion exampleExtrusion = new Extrusion("ExampleExtrusion");
//              exampleExtrusion.setSpine(new MFVec3f() // test closed spine
//                  .append(new SFVec3f(0,0,0)).append(new SFVec3f(0,1,0)).append(new SFVec3f(0,0,0)));
                scene.addChild(new Shape("ExtrusionShape")
                        .setGeometry(exampleExtrusion)
                        .addComments(new CommentsBlock(exampleExtrusion.getDEF() +
                            " isCrossSectionClosed()=" + exampleExtrusion.isCrossSectionClosed() +
                            ", crossSection='" + Arrays.toString(exampleExtrusion.getCrossSection()) + "'"))
                        .addComments(new CommentsBlock(exampleExtrusion.getDEF() +
                            " isSpineClosed()=" + exampleExtrusion.isSpineClosed() +
                            ", spine='" + Arrays.toString(exampleExtrusion.getSpine()) + "'"))
                        .setAppearance(new Appearance("TransparentAppearance").setMaterial(new Material().setTransparency(1))));
                
                Group protoNodeListChildrenTest1 = new Group()
                    .addComments("Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes")
                    .addChild(new ProtoDeclare("NewWorldInfo")
                        .setProtoInterface(new ProtoInterface()
                            .addField(new field("description",field.TYPE_SFSTRING, field.ACCESSTYPE_INITIALIZEONLY)))
                        .setProtoBody(new ProtoBody()
                            .addChild(new WorldInfo())))
                    .addChild(new ProtoInstance("NewWorldInfo", "Proto1")  // prototypeName is always first, DEFlabel is second
                        .addFieldValue(new fieldValue("description","testing 1 2 3"))
                    )
                    .addChild(new Group("Node2").addComments("intentionally empty"))
                    // ProtoInstanc constructor: prototypeName is always first, DEFlabel is second
                    .addChild(new ProtoInstance("NewWorldInfo", "Proto3").setContainerField(WorldInfo.containerField_DEFAULT_VALUE))
                    .addChild(new Transform("Node4").addComments("intentionally empty"))
                    .addComments("Test satisfactorily creates MFNode children array as an ordered list with mixed content");
                scene.addChild(protoNodeListChildrenTest1);
                
                scene.addChild(new ProtoDeclare("ShaderProto")
                            .setProtoBody(new ProtoBody()
                                .addChild(new ProgramShader())));
                Shape protoNodeListChildrenTest2 = new Shape()
                    .setAppearance(new Appearance()
                        .addComments("Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes")
                        .addShaders(new ProgramShader("TestShader1")
                            .addPrograms(new ShaderProgram("TestShader2"))) // gosh are these names confusing or what
                        .addShaders(new ProtoInstance("ShaderProto","TestShader3").setContainerField(ProgramShader.containerField_DEFAULT_VALUE))
                        .addShaders(new ComposedShader("TestShader4")
                            .addParts(new ShaderPart("TestShader5")))
                        .addComments("Test satisfactorily creates MFNode shaders array as an ordered list with mixed content"));
                scene.addChild(protoNodeListChildrenTest2);
                
                Transform specialtyNodes = new Transform("SpecialtyNodes");
                scene.addChild(specialtyNodes);
                
                CADLayer cadLayer = new CADLayer();
                CADAssembly cadAssembly = new CADAssembly();
                CADPart cadPart = new CADPart();
                CADFace cadFace = new CADFace();
//              scene         .addChild(cadLayer);        // test method
                specialtyNodes.addChild(cadLayer);
                cadLayer      .addChild(cadAssembly);
                cadAssembly   .addChild(cadPart);
                cadPart       .addChild(cadFace);

                EspduTransform espduTransform = new EspduTransform();
                espduTransform.addChild(new WorldInfo());
                DISEntityManager disEntityManager = new DISEntityManager();
                disEntityManager.addChild(new DISEntityTypeMapping()); // formerly DISEntityManager addMapping in X3D3
                scene         .addChild(espduTransform);        // test methods
                scene         .addChild(new ReceiverPdu());
                scene         .addChild(new SignalPdu());
                scene         .addChild(new TransmitterPdu());
                scene         .addChild(disEntityManager);
                specialtyNodes.addChild(new EspduTransform());
                specialtyNodes.addChild(new ReceiverPdu());
                specialtyNodes.addChild(new SignalPdu());
                specialtyNodes.addChild(new TransmitterPdu());
                specialtyNodes.addChild(disEntityManager);
                
                // test X3DUrlObject nodes
                LoadSensor loadSensor = new LoadSensor();
                loadSensor.addComments("Contained nodes typically must be USE references for nodes previously DEFined in the scene");
                loadSensor.addComments("The following nodes are test cases for all X3DUrlObject nodes");
                loadSensor.addChild(new Anchor().setUSE("siteAnchor"));
                loadSensor.addChild(new Inline().setUSE(inlineScene.getDEF()));
                loadSensor.addChild(new DISEntityTypeMapping());
                loadSensor.addChild(new GeoMetadata());
                loadSensor.addChild(new AudioClip())     .addChild(new ImageCubeMapTexture()).addChild(new ImageTexture3D())
                          .addChild(new ImageTexture())  .addChild(new MovieTexture())       .addChild(new Script())
                          .addChild(new PackagedShader()).addChild(new ShaderPart())         .addChild(new ShaderProgram());
                scene.addChild(loadSensor);
                // TODO X3Dv4 issue: use correct containerField on output if generating X3D3 content
        
                HAnimHumanoid humanoid = new HAnimHumanoid("TestHumanoidDEF", "TestHumanoid");

                // TODO X3Dv4 issue: do not let HAnimHumanoid provide output fields not supported by current X3D version
//              scene         .addChild(humanoid);  // test method
//              specialtyNodes.addChild(humanoid);

                HAnimJoint     hanimJoint     = new HAnimJoint    ("hanimJointDEF",     HAnimJoint.NAME_HUMANOID_ROOT);
                HAnimSegment   hanimSegment   = new HAnimSegment  ("hanimSegmentDEF",   HAnimSegment.NAME_SACRUM);
                HAnimSite      hanimSite      = new HAnimSite     ("hanimSiteDEF",      HAnimSite.NAME_CERVICALE);
                HAnimDisplacer hanimDisplacer = new HAnimDisplacer("hanimDisplacerDEF", HAnimDisplacer.NAME_CERVICALE);
//                humanoid    .addJoints(hanimJoint);         // TODO fix parent exception
//                hanimJoint  .addChild(hanimSegment);        // TODO fix parent exception
//                hanimSegment.setDisplacers(hanimDisplacer); // test alternate method
//                hanimSegment.addChild(hanimSite);           // TODO fix name exception
//                hanimSegment.addDisplacers(hanimDisplacer); // TODO fix parent exception
//                hanimSegment.setDisplacers(hanimDisplacer); // test alternate method
                
                // all finished, go see if the paint is dry
	}
	
	/** Test declarative programming style using Java 8
	 */
	private void createDeclarativeShapeTests()
	{
		String innerAppearanceNodeDEF  = "DeclarativeAppearanceExample";
		String innerMaterialNodeDEF    = "DeclarativeMaterialExample";
		String innerMetadataStringName = "findThisNameValue";

		Group declarativeGroup = new Group("DeclarativeGroupExample")
			// addChild is singleton pipeline method, avoiding return-void restrictions of SAI addChildren interface
			.addChild(new Shape()
				.setAppearance(new Appearance(innerAppearanceNodeDEF)
					.setMaterial(new Material(innerMaterialNodeDEF)
						.setDiffuseColor(SFColor.LIGHTSEAGREEN))
					.addComments(innerMaterialNodeDEF + " gets overridden by subsequently added MaterialModulator ProtoInstance")
					.setMaterial(new ProtoInstance("MaterialModulator", "MyMaterialModulator") // prototypeName is always first, DEFlabel is second
//                      .setContainerField("material") not required, handled automatically by X3DJSAIL setMaterial method
					))
				.setGeometry(new Cone()
					.setHeight(0.1f).setBottomRadius(0.05f).setBottom(false))
				.setMetadata(new MetadataString("FindableMetadataStringTest") // sets DEF
					.setName(innerMetadataStringName).setValue("test case")))
					// TODO show another metadata/value example using MetadataSet
			.addComments("Test success: declarativeGroup.addChild() singleton pipeline method");

		scene.addComments("Test success: declarative statement createDeclarativeShapeTests()")
			 .addChild   (declarativeGroup) // addChild is pipeline method
			 .addComments(new CommentsBlock("Test success: declarative statement addChild()"));

		// Now check and report result: can we find inner node?
		CommentsBlock createDeclarativeShapeTestResults = new CommentsBlock();
		X3DConcreteElement nodeFoundByDEF = x3dModel.findNodeByDEF(innerAppearanceNodeDEF);
		if  (nodeFoundByDEF != null)
			 createDeclarativeShapeTestResults.addComments("Test success: x3dModel.findNodeByDEF(" + innerAppearanceNodeDEF + ") = " +
				"<"  + nodeFoundByDEF.getElementName() + " DEF='" + ((X3DConcreteNode) nodeFoundByDEF).getDEF() + "'/> i.e." +
				"\n" + nodeFoundByDEF.toStringX3D().trim()); // test CommentsBlock.cleanXmlCommentDelimiters() method
		else createDeclarativeShapeTestResults.addComments("Test failure: x3dModel.findNodeByDEF(" + innerAppearanceNodeDEF + ") = null");

		X3DConcreteElement nodeFoundByName = x3dModel.findElementByNameValue(innerMetadataStringName);
		if  (nodeFoundByName != null)
			 createDeclarativeShapeTestResults.addComments("Test success: x3dModel.findElementByNameValue(" + innerMetadataStringName + ") = " +
				nodeFoundByName.toStringX3D().trim());
		else createDeclarativeShapeTestResults.addComments("Test failure: x3dModel.findElementByNameValue(" + innerMetadataStringName + ") = null");

		nodeFoundByName = x3dModel.findElementByNameValue(nameArtDeco01Material, ProtoDeclare.NAME);
		if  (nodeFoundByName != null)
			 createDeclarativeShapeTestResults.addComments("Test success: x3dModel.findElementByNameValue(\"" + nameArtDeco01Material + "\", \"" + ProtoDeclare.NAME + "\") found"); // obfuscate contained comments since nesting is illegal XML
		else createDeclarativeShapeTestResults.addComments("Test failure: x3dModel.findElementByNameValue(\"" + nameArtDeco01Material + "\", \"" + ProtoDeclare.NAME + "\") = null");

		nodeFoundByName = x3dModel.findElementByNameValue("MaterialModulator", ProtoDeclare.NAME);
		if  (nodeFoundByName != null)
			 createDeclarativeShapeTestResults.addComments("Test success: x3dModel.findElementByNameValue(\"" + "MaterialModulator" + "\", \"" + ProtoDeclare.NAME + "\")  found"); // obfuscate contained comments since nesting is illegal XML
		else createDeclarativeShapeTestResults.addComments("Test failure: x3dModel.findElementByNameValue(\"" + "MaterialModulator" + "\", \"" + ProtoDeclare.NAME + "\")  = null");

		nodeFoundByName = x3dModel.findElementByNameValue("MaterialModulator", ProtoInstance.NAME);
		if  (nodeFoundByName != null)
			 createDeclarativeShapeTestResults.addComments("Test success: x3dModel.findElementByNameValue(\"" + "MaterialModulator" + "\", \"" + ProtoInstance.NAME + "\") found"); // obfuscate contained comments since nesting is illegal XML
		else createDeclarativeShapeTestResults.addComments("Test failure: x3dModel.findElementByNameValue(\"" + "MaterialModulator" + "\", \"" + ProtoInstance.NAME + "\") = null");

		scene.addChild(createDeclarativeShapeTestResults); // addChildren also works but is not pipelined
		
		testFieldObjects();
	}
	
	/** Set of unit tests on field objects.
	 * TODO add assertions.
	 * @see org.web3d.x3d.jsail.fields
	 */
	@SuppressWarnings("UnusedAssignment")
	private void testFieldObjects()
	{
		Group testFieldObjectsGroup = new Group("TestFieldObjectsGroup");
		scene.addChild(testFieldObjectsGroup);
		testFieldObjectsGroup.addComments("testFieldObjects() results");
		StringBuilder results = new StringBuilder();
		
		SFBool valueSFBool = new SFBool();
		results.append("SFBool default=").append(valueSFBool.getValue());
		valueSFBool.setValue(true); // not pipelined
		results.append(", true=").append(valueSFBool.getValue());
		valueSFBool.setValue(false);
		results.append(", false=").append(valueSFBool.getValue());
		results.append(", negate()=").append(valueSFBool.negate().getValue()); // pipelined
		testFieldObjectsGroup.addComments(results.toString());
		results = new StringBuilder(); // reset
		
		MFBool valueMFBool = new MFBool();
//		valueMFBool.setValueByString("0"); // test illegal value. exception message is satisfactory
		results.append("MFBool default=").append(valueMFBool.toString());
		boolean[] defaultBooleans = {true, false, true};
		valueMFBool = new MFBool(defaultBooleans);
		results.append(", initial=").append(valueMFBool.toString());
		results.append(", negate()=").append(valueMFBool.negate().toString());
		testFieldObjectsGroup.addComments(results.toString());
		results = new StringBuilder(); // reset
		
		SFFloat valueSFFloat = new SFFloat();
		results.append("SFFloat default=").append(valueSFFloat.getValue());
		valueSFFloat = new SFFloat(1f);
		results.append(", initial=").append(valueSFFloat); // output uses .toString() by default
		results.append(", setValue(2)=").append(valueSFFloat.setValue(2));
		valueSFFloat.setValue(3.0f);  // not pipelined for floats
		results.append(", setValue(3.0f)=").append(valueSFFloat);
		results.append(", setValue(4.0)=").append(valueSFFloat.setValue(4.0));
		testFieldObjectsGroup.addComments(results.toString());
		results = new StringBuilder(); // reset
		
		MFFloat valueMFFloat = new MFFloat();
		results.append("MFFloat default=").append(valueMFFloat);
		// Java requires coercing double to float, ensuring no unintentional loss of precision
		float[] defaultFloats = {1.0f, 2, (float)3.0};
		valueMFFloat = new MFFloat(defaultFloats);
		results.append(", initial=").append(valueMFFloat);
		valueMFFloat.append(5f); // not pipelined
		results.append(", append(5)=").append(valueMFFloat);
		valueMFFloat.insertValue(3, 4f); // not pipelined
		valueMFFloat.insertValue(0, 0f);
		results.append(", inserts(3,4)(0,0)=").append(valueMFFloat);
		valueMFFloat.append(6); // not pipelined
		results.append(", append(6)=").append(valueMFFloat);
		results.append(", size()=").append(valueMFFloat.size());
		testFieldObjectsGroup.addComments(results.toString());
		results = new StringBuilder(); // reset, line break
		results.append("... get1Value[3]=").append(valueMFFloat.get1Value(3));
		valueMFFloat.remove(1); // not pipelined
		results.append(", remove[1]=").append(valueMFFloat);
		valueMFFloat.set1Value(0,10); // not pipelined
		results.append(", set1Value(0,10)=").append(valueMFFloat);
		valueMFFloat.multiply(2);
		results.append(", multiply(2)=").append(valueMFFloat);
		valueMFFloat.clear(); // not pipelined
		results.append(", clear=").append(valueMFFloat);
		testFieldObjectsGroup.addComments(results.toString());
		results = new StringBuilder(); // reset, line break
		
		SFVec3f valueSFVec3f = new SFVec3f();
		results.append("SFVec3f default=").append(valueSFVec3f); // output uses .toString() by default
		valueSFVec3f = new SFVec3f(1f, 2, (float)3.0);
		results.append(", initial=").append(valueSFVec3f);
		// Java requires coercing double to float, ensuring no unintentional loss of precision
		valueSFVec3f.setValue(4f, 5, (float)6.0);
		results.append(", setValue=").append(valueSFVec3f);
		results.append(", multiply(2)=").append(valueSFVec3f.multiply(2));
		results.append(", normalize()=").append(valueSFVec3f.normalize());
		results.append(", regex matches()=").append(valueSFVec3f.matches());
		testFieldObjectsGroup.addComments(results.toString());
		results = new StringBuilder(); // reset, line break
		results.append("regex test SFVec3f().matches(\"1 2 3\")=").append(SFVec3f.matches("1 2 3")).append(", ");
		results.append("regex test SFVec3f().matches(\"1 2 3 4\")=").append(SFVec3f.matches("1 2 3 4")).append(", ");
		results.append("regex test (SFRotation.matches(\"0 0 0 0\")=").append(SFRotation.matches("0 0 0 0"));
		if (SFRotation.matches("0 0 0 0")) // this should not match
		     results.append(", failure detecting illegal (zero axis) rotation value"); //  true = match
		else results.append(", success detecting illegal (zero axis) rotation value"); // false = no match
		testFieldObjectsGroup.addComments(results.toString());
		results = new StringBuilder(); // reset
        
        // typecast tests
        Material myMaterial = new Material();
        myMaterial.setAmbientIntensity((float) 0.123456789d);
        myMaterial.setAmbientIntensity(new SFFloat(0.123456789d));
        myMaterial.setAmbientIntensity((float) new SFDouble(0.123456789d).getValue());
        // consider adding downcast methods such as SFDouble.toFloat() .toInt() etc.
        // consider adding typecast methods for use of boolean values with numeric types
        
//      X3D failureTestX3D = new X3D().setProfile("wrong").setVersion("2.0");
	}
	
	Document           domDocument;
	DOMImplementation  domImplementation;
	String             domDocumentToStringX3D;
	X3D                reloadedX3dObjectTree;
	File               reloadedFile;
	/**
	 * Load the produced HelloWorldProgramOutput.x3d scene using X3DLoaderDOM, then write resulting DOM back out to a file.
	 */
	private void testX3DLoaderDOM()
	{
		X3DLoaderDOM x3dLoaderDOM = new X3DLoaderDOM();
		x3dLoaderDOM.loadModelFromFileX3D(thisSceneName + ".x3d");
		sourceFile = new File (thisSceneName + ".x3d");
//		boolean successfulLoad = x3dLoader.loadX3DfromFile(new File(thisSceneName + ".x3d")); // alternate form, tested OK
		if (x3dLoaderDOM.isLoadSuccessful())
		{
			if (x3dLoaderDOM.getX3dObjectTree() instanceof X3D)
			{
				System.out.println ("===========================================");
				System.out.println("Test success: x3dLoader.loadX3DfromXML(" + thisSceneName + ".x3d), " + 
												 "x3dLoader.getX3dObjectTree()");
				System.out.println ("===========================================");
			}
			else System.out.println("Test failure: x3dLoader.loadX3DfromXML(" + thisSceneName + ".x3d), " + 
                                                  "x3dLoader.getX3dObjectTree()");
            // alternative approach to loading:
			domDocument       = x3dLoaderDOM.getDomDocument();
			domImplementation = domDocument.getImplementation(); // debug use only
			domDocumentToStringX3D = x3dLoaderDOM.toStringX3D(domDocument);
			System.out.println (domDocumentToStringX3D.trim()); // may include partial results if settings permit
			System.out.println ("===========================================");
			System.out.println("Test success: x3dLoader.getDomDocument() and x3dLoader.toStringX3D(domDocument)");
			System.out.println ("Now test x3dLoader.toX3dModelInstance(domDocument)");
			x3dLoaderDOM.toX3dModelInstance(domDocument); 
			reloadedX3dObjectTree = (X3D) x3dLoaderDOM.getX3dObjectTree();
			x3dLoaderDOM.getValidationResult();  // debug inspection
			String reloadedFileName = thisSceneName + "_ReloadedDOM" + X3D.FILE_EXTENSION_X3D;
			if (reloadedX3dObjectTree != null)
			{
				reloadedX3dObjectTree.validate(); // debug inspection
				reloadedFile = reloadedX3dObjectTree.toFileX3D(reloadedFileName);
				// X3D scene has already been produced at this point, no point in adding further comments
				System.out.println("Test success: x3dLoader.toX3dModelInstance(domDocument), save " + reloadedFileName);
			}
			else System.out.println("Test failure: x3dLoader.toX3dModelInstance(domDocument), save " + reloadedFileName);
		}
		else System.out.println("Test failure: x3dLoader.loadX3DfromXML(" + thisSceneName + ".x3d)");
		System.out.print("x3dLoader validation result: ");
		if  (x3dLoaderDOM.getValidationResult().trim().isEmpty())
			 System.out.println("no issues reported.");
		else System.out.println("\n" + x3dLoaderDOM.getValidationResult());
	}
    
    /** 
     * Test BlenderLauncher utility class, note use of static methods.
     * @see <a href="https://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html">Java Tutorials: Understanding (Static) Class Members</a>
     */
    private void testBlenderLauncher()
    {
        // ordinarily path shenanigans are not needed if latest Blender is installed, but this is included as test code
        System.out.print("Blender default path=" + BlenderLauncher.getBlenderPath());
        if (BlenderLauncher.getBlenderPath().isEmpty())
        {
            System.out.print("[Blender path not set]");
        }
        System.out.println();
        BlenderLauncher.checkBlenderPath(); // check local path and reset to OS-specific default if needed
        System.out.println("Blender.checkBlenderPath() updated path=" + BlenderLauncher.getBlenderPath());
        System.out.println("=================================");
        System.out.println("BlenderLauncher.hasBlender()=" + BlenderLauncher.hasBlender());
        System.out.println("=================================");
        System.out.println("Blender version=" + BlenderLauncher.getBlenderVersion());
        System.out.println("===========================================");
        System.out.println("BlenderLauncher.run(\"-help\")");
        org.web3d.x3d.jsail.BlenderLauncher.run("-help");
        System.out.println("===========================================");
//      System.out.println("BlenderLauncher.launchBlenderWebPage()");
//      org.web3d.x3d.jsail.BlenderLauncher.launchBlenderWebPage();
//      System.out.println("=================================");

        if (BlenderLauncher.hasBlender())
        {
            // split path as separate string, otherwise this often won't work under Windows OS due to embedded space characters in path
            System.out.println("BlenderLauncher.run(\"-BLENDER_PATH\", \"" + BlenderLauncher.getBlenderPath() + "\")");
            org.web3d.x3d.jsail.BlenderLauncher.run(new String[] {"-BLENDER_PATH", BlenderLauncher.getBlenderPath() } );
            System.out.println ("===========================================");
        }
        System.out.println("BlenderLauncher.run(\"-properties X3DJSAIL.properties\")");
        org.web3d.x3d.jsail.BlenderLauncher.run ("-properties X3DJSAIL.properties");
        System.out.println ("===========================================");
//        if (x3dModel == null) // possible during program refactoring
//            x3dModel = new X3D();
//        File tempFile = x3dModel.getTempFileFromX3dJsailJar("python/", "BlenderX3dToPng.py");

        System.out.println("BlenderLauncher.run(\"CleatClamp.x3d -toImage\")");
        org.web3d.x3d.jsail.BlenderLauncher.run ("CleatClamp.x3d -toImage");
        System.out.println("CommandLine.run(\"CleatClamp.x3d -toImage\") tests pass through");
        org.web3d.x3d.jsail.CommandLine.run ("CleatClamp.x3d -toImage");
        // TODO too big
        System.out.println("CommandLine.run(\"CleatClamp.x3d -toJava   -toFile CleatClamp.java\") tests pass through");
        org.web3d.x3d.jsail.CommandLine.run ("CleatClamp.x3d -toJava   -toFile CleatClamp.java");
        System.out.println("CommandLine.run(\"CleatClamp.x3d -toJSON   -toFile CleatClamp.json\") tests pass through");
        org.web3d.x3d.jsail.CommandLine.run ("CleatClamp.x3d -toJSON   -toFile CleatClamp.json");
        System.out.println("CommandLine.run(\"CleatClamp.x3d -toPython -toFile CleatClamp.py\")   tests pass through");
        org.web3d.x3d.jsail.CommandLine.run ("CleatClamp.x3d -toPython -toFile CleatClamp.py");
    }

    /** 
     * Test MeshLabLauncher utility class, note use of static methods.
     * @see <a href="https://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html">Java Tutorials: Understanding (Static) Class Members</a>
     */
    private void testMeshLabLauncher()
    {
        System.out.println(".run(\"-version\"");
        org.web3d.x3d.jsail.MeshLabLauncher.run( "-version");
        System.out.println("===========================================");
        System.out.println("MeshLabLauncher.run(\"-help\"");
        org.web3d.x3d.jsail.MeshLabLauncher.run( "-help");
        System.out.println("===========================================");
        // ordinarily path shenanigans are not needed, but this is included as test code
        System.out.print("MeshLab default path=" + MeshLabLauncher.getMeshLabPath());
        if (MeshLabLauncher.getMeshLabPath().isEmpty())
        {
            System.out.print("[not set]");
        }
        System.out.println();
        MeshLabLauncher.checkMeshLabPath();
        System.out.println("MeshLab.checkMeshLabPath() updated path=" + MeshLabLauncher.getMeshLabPath());
        System.out.println("=================================");
        System.out.println("MeshLabLauncher.hasMeshLab()=" + MeshLabLauncher.hasMeshLab());
        System.out.println("=================================");
        System.out.println("MeshLabLauncher.getMeshLabVersion()=" + MeshLabLauncher.getMeshLabVersion());
        System.out.println("=================================");
//      System.out.println("MeshLabLauncher.launchMeshLabWebPage()");
//      org.web3d.x3d.jsail.MeshLabLauncher.launchMeshLabWebPage();
//      System.out.println("=================================");

        if (MeshLabLauncher.hasMeshLab())
        {
            // split path as separate string, otherwise this often won't work under Windows OS due to embedded space characters in path
            System.out.println("MeshLabLauncher.run(\"-MESHLAB_PATH\", \"" + MeshLabLauncher.getMeshLabPath() + "\")");
            org.web3d.x3d.jsail.MeshLabLauncher.run(new String[] {"-MESHLAB_PATH", MeshLabLauncher.getMeshLabPath() } );
            System.out.println ("===========================================");
        }
        System.out.println("MeshLabLauncher.run(\"-properties X3DJSAIL.properties\")");
        org.web3d.x3d.jsail.MeshLabLauncher.run ("-properties X3DJSAIL.properties");
        System.out.println ("===========================================");
        
        System.out.println("MeshLabLauncher.convertModel(\".\", " +
            "\"CleatClamp.stl\", \"CleatClamp_RoundTrip.stl\");");
        boolean conversionResult = MeshLabLauncher.convertModel(".", // current directory
            "CleatClamp.stl", "CleatClamp_RoundTrip.stl"); // converts ascii to binary, TODO adjust settings
        System.out.println("MeshLabLauncher.wasPriorCommandSuccessful()=" + MeshLabLauncher.wasPriorCommandSuccessful() +
            " conversionResult=" + conversionResult);
        // TODO diff
        
        System.out.println(    "meshLabLauncher.importModel(\".\", \"CleatClamp.stl\"); produces CleatClamp.MeshLab.x3d and CleatClamp.MeshLab.log.txt");
        X3D importedX3D = MeshLabLauncher.importModel (".",   "CleatClamp.stl");
        System.out.println("meshLabLauncher.getPriorMeshLabTraceLogFileName()=" + MeshLabLauncher.getPriorMeshLabTraceLogFilePath());
        System.out.print  ("meshLabLauncher.getPriorMeshLabTraceLogContents()=");
        if  (MeshLabLauncher.getPriorMeshLabTraceLogContents().isEmpty())
             System.out.println("[empty file]");
        else 
        {
            System.out.println();
            System.out.println(MeshLabLauncher.getPriorMeshLabTraceLogContents());
        }
        importedX3D.toFileX3D ("HelloWorldProgramOutput_MeshLabImport.x3d");
        importedX3D.toFileJava("HelloWorldProgramOutput_MeshLabImport.java");
        importedX3D.toFileJSON("HelloWorldProgramOutput_MeshLabImport.json");
        System.out.println ("===========================================");
    }
    
    private static void x3duomInspectionsTest()
	{
        System.out.println("X3DUnifiedObjectModelJaxbTests.x3duomInspectionsTest() start...");
        
        // now tests for ...
//        X3DUnifiedObjectModel40 x3duomInstance = new X3DUnifiedObjectModel40();
//        
//        String x3duomInstanceXml = x3duomInstance.marshalToXml();
//        
//        System.out.println("x3duomInstanceXml.length()=" + x3duomInstanceXml.length());
        
        System.out.println("X3DUnifiedObjectModelJaxbTests.x3duomInspectionsTest() complete");
    }
}
