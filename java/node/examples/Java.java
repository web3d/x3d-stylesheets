import net.coderextreme.X3DJSONLD;
import org.w3c.dom.Document;
import javax.json.JsonObject;
import java.io.File;
import java.io.FileWriter;
import org.web3d.x3d.jsail.X3DLoaderDOM;
import org.web3d.x3d.jsail.Core.X3D;

class Java {
	public static void main(String [] args) throws Exception {
		X3DJSONLD loader = new X3DJSONLD();
		X3DLoaderDOM xmlLoader = new X3DLoaderDOM();

		JsonObject jsobj = loader.readJsonFile(new File("./examples/HelloWorldProgramOutput.json"));
		Document document = loader.loadJsonIntoDocument(jsobj);

/*
		FileWriter fw = new FileWriter("./examples/Java.json.x3d");
		fw.write(loader.serializeDOM(loader.getX3DVersion(jsobj), document));
		fw.close();

                xmlLoader.loadModelFromFileX3D("./examples/Java.json.x3d");
		document       = xmlLoader.getDomDocument();
*/

		X3D X3D0 = (X3D)xmlLoader.toX3dModelInstance(document);
		X3D0.toFileX3D("./examples/Java.x3d");
		X3D0.toFileJSON("./examples/Java.json");
	}
}
