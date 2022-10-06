package examples;

import org.w3c.dom.Document;
import java.io.File;
import org.web3d.x3d.jsail.X3DLoaderDOM;
import org.web3d.x3d.jsail.Core.X3D;

class XML {
	public static void main(String [] args) throws Exception {
		X3DLoaderDOM xmlLoader = new X3DLoaderDOM();
                xmlLoader.loadModelFromFileX3D("./examples/Java.json" + ".x3d");
		Document document       = xmlLoader.getDomDocument();
		X3D X3D0 = (X3D)xmlLoader.toX3dModelInstance(document);
		X3D0.toFileX3D("./examples/XML.x3d");
	}
}
