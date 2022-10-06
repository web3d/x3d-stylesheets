package net.coderextreme;

import net.coderextreme.X3DJSONLD;
import org.w3c.dom.*;
import org.w3c.dom.ls.*;
import javax.json.*;
import java.util.*;
import java.io.*;
import javax.xml.transform.stream.*;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.parsers.*;
import org.web3d.x3d.jsail.X3DLoaderDOM;
import org.web3d.x3d.jsail.Core.X3D;


public class JsonConversion {
	public static void main(String args[]) throws Exception {
		X3DJSONLD loader = new X3DJSONLD();

		JsonObject jsobj = loader.readJsonFile(new File("../examples/HelloWorldProgramOutput.json"));
		Document document = loader.loadJsonIntoDocument(jsobj);
        System.out.print(loader.serializeDOM(loader.getX3DVersion(jsobj), document));
		X3DLoaderDOM  xmlLoader = new X3DLoaderDOM();
		X3D X3D0 = (X3D)xmlLoader.toX3dModelInstance(document);
		X3D0.toFileX3D("./examples/Json.x3d");
		X3D0.toFileJSON("./examples/Json.json");
	}
}
