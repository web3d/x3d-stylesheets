/*
Copyright (c) 1995-2020 held by the author(s).  All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer
      in the documentation and/or other materials provided with the
      distribution.
    * Neither the name of the Web3D Consortium (https://www.web3D.org)
      nor the names of its contributors may be used to endorse or
      promote products derived from this software without specific
      prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
*/

package org.web3d.x3d.util.x3duom;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;
import javax.xml.bind.Unmarshaller;
                
import org.web3d.x3d.jsail.Core.X3D;

/**
 * Utility class to expose X3D Unified Object Model (X3DUOM).
 * 
 * <br><br>

 * @author Don Brutzman and Roy Walmsley
 * @see <a href="https://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html" target="_blank">X3D Scene Authoring Hints</a>
 */
public final class X3DUnifiedObjectModel40
{
    private X3DUnifiedObjectModel x3duomInstance;
                
    private final String X3dUnifiedObjectModel40_XML_FILE = "X3dUnifiedObjectModel-4.0.xml";
                
    private JAXBContext jaxbContext;
    
    /** Constructor performs initialization */
    public X3DUnifiedObjectModel40()
    {
        initialize();
    }

    /** Load and initialize X3DUOM JAXB object
     */
    public void initialize() 
    {
        try
        {
            X3D x3dObject = new X3D(); // necessary for static object?  TODO visibility problems

            File x3duomXmlFile = x3dObject.getTempFileFromX3dJsailJar("/specifications", X3dUnifiedObjectModel40_XML_FILE);
                
            if (!x3duomXmlFile.exists())
            {
				String errorNotice = "*** Error: X3DUnifiedObjectModel40." +
								     "X3dUnifiedObjectModel40_XML_FILE=\"" + X3dUnifiedObjectModel40_XML_FILE + "\" not found";
				System.out.println(errorNotice);
                return;
            }
            jaxbContext = JAXBContext.newInstance(X3DUnifiedObjectModel.class);

            Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();

            x3duomInstance = (X3DUnifiedObjectModel) unmarshaller.unmarshal(x3duomXmlFile);
        }
        catch (JAXBException e)
        {
            System.out.println("X3DUnifiedObjectModel initialize() failure:");
            System.out.println(e);
        }
    }
    /** Marshall X3DUOM JAXB object as XML String to file 
     *@param outputFilePath path and filename for result
     */
    public void marshallToXmlFile(String outputFilePath)
    {
        try
        {
            Marshaller marshaller = jaxbContext.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
//          marshaller.marshal(x3duomInstance, System.out); // debug
            marshaller.marshal(x3duomInstance, new File(outputFilePath));
        }
        catch (JAXBException e)
        {
            System.out.println("X3DUnifiedObjectModel40 marshalToXML() marshaller.setProperty failure:");
            System.out.println(e);
        }
    }
    /** Provide XML String of X3DUOM from JAXB object 
     *@return XML string
     */
    public String marshalToXml()
    {
        File tempFile;
        byte[] encodedByteArray = null;
        try
        {
            Marshaller marshaller = jaxbContext.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
//          marshaller.marshal(x3duomInstance, System.out); // debug
            tempFile = File.createTempFile("x3duomJaxb","temp.xml");
            marshaller.marshal(x3duomInstance, tempFile);
            
            // https://stackoverflow.com/questions/326390/how-do-i-create-a-java-string-from-the-contents-of-a-file
            encodedByteArray = Files.readAllBytes(Paths.get(tempFile.getPath()));
        }
        catch (IOException | JAXBException e)
        {
            System.out.println("X3DUnifiedObjectModel40 marshalToXML() failure:");
            System.out.println(e);
        }
        return new String(encodedByteArray);
    }
}
