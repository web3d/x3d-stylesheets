/* Copyright (c) 1995-2022 held by the author(s).  All rights reserved.

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
package org.web3d.x3d.tests;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.web3d.x3d.util.x3duom.*;

/**
 * X3DUnifiedObjectModelLaxbTests.java
 *
 * Filename:     X3DUnifiedObjectModelLaxbTests.java
 * Identifier:   
 * @author       Don Brutzman
 * Created:      1 June 2019
 * Revised:      see version control
 * Compile, run: ../build.xml
 */

/**
 * Initial test harness using junit5 for the JAXB bindings of the X3D Unified Object Model.
 * @see <a href="https://www.web3d.org/specifications/java/X3DJSAIL.html">X3DJSAIL</a>
 * @see <a href="https://junit.org/junit5/docs/current/user-guide/#running-tests-build-ant">JUnit5 running tests with Ant</a>
 * @see <a href="https://ant.apache.org/manual/Tasks/junitlauncher.html">Ant task junitlauncher</a>
 * @see <a href="https://www.petrikainulainen.net/programming/testing/junit-5-tutorial-writing-assertions-with-junit-5-api">Tutorial: writing assertions with JUnit5</a>
 * @see <a href="../license.html">License</a>   
 */
class X3DUnifiedObjectModelJaxbTests
{
    @Test
    @DisplayName("Test initialization of X3DUOM JAXB objects")
    void x3duomInspectionsTest()
	{
        System.out.println("X3DUnifiedObjectModelJaxbTests.x3duomInspectionsTest() start...");

        // assert statements
        System.out.println ("Preliminary tests...");
        assertTrue (true,  "this test should explicitly pass");
        assertFalse(false, "this test should explicitly fail");
        
        // now tests for ...
        X3DUnifiedObjectModel40 x3duomInstance = new X3DUnifiedObjectModel40();
        
        String x3duomInstanceXml = x3duomInstance.marshalToXml();
        
        System.out.println ("X3DUOM:"); // + x3duomInstance.
        System.out.println("x3duomInstanceXml.length()=" + x3duomInstanceXml.length());
        
        System.out.println("X3DUnifiedObjectModelJaxbTests.x3duomInspectionsTest() complete");
    }
    
    /** Default main() method provided for test purposes.
     * @param args the command line arguments
     * @see #x3duomInspectionsTest()
     */
    public static void main(String[] args)
    {
        System.out.println("X3DUnifiedObjectModelJaxbTests start...");
        X3DUnifiedObjectModelJaxbTests thisObject = new X3DUnifiedObjectModelJaxbTests();
        thisObject.x3duomInspectionsTest();
        System.out.println("X3DUnifiedObjectModelJaxbTests complete");
    }
}