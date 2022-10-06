/* Copyright (c) 1995-2021 held by the author(s).  All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer
      in the documentation and/or other materials provided with the
      distribution.
    * Neither the name of the Web3D Consortium (http://www.web3D.org)
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

package org.web3d.x3d.util.exi;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import org.openexi.schema.EXISchema;
import org.openexi.scomp.EXISchemaFactory;
import org.openexi.scomp.EXISchemaFactoryException;
import org.openexi.scomp.EXISchemaWriter;

import org.xml.sax.InputSource;

/** EXISchemaFactory from OpenEXI is used to compile an EXI schema. */
public class SerializeEXISchema {

    /** constructor */
    public SerializeEXISchema() {
        super();
    }

    /**
     * Utility class. The only arguments required are the source and target file names
     * @param xsdFileName XML schema file name
     * @param fis file input stream
     * @param exigFileName name of file to hold output
     * @throws IOException improper file operation
     * @throws EXISchemaFactoryException unexpected error
     */
    public void serializeEXISchema(
            String xsdFileName,
            InputStream fis,
            String exigFileName
        ) throws IOException, EXISchemaFactoryException
    {
        EXISchemaFactory factory = new EXISchemaFactory();
        EXISchema newSchema;
        InputSource is;
        OutputStream fos = null;
        try
        {
            // Convert the input file to an input source.
            is = new InputSource(fis);
            is.setSystemId(new File(xsdFileName).toString());

            // Compile a new schema.
            newSchema = factory.compile(is);

            // Write the results to a file.
            fos = new FileOutputStream(exigFileName);
            new EXISchemaWriter().serialize(newSchema, fos);
            fos.flush();
        }
        finally
        {
            if (fos != null)
            {
                fos.close();
            }
        }
    }
}
