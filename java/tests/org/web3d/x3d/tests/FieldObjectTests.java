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

import java.util.Arrays;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.web3d.x3d.jsail.fields.*;
import org.web3d.x3d.jsail.ConfigurationProperties;

/**
 * FieldObjectTests.java
 *
 * Filename:     FieldObjectTests.java
 * Identifier:   
 * @author       Don Brutzman
 * Created:      23 June 2018
 * Revised:      see version control
 * Compile, run: ../build.xml
 */

/**
 * Initial test harness using junit5 for the X3D Java Scene Access Interface Library (X3DJSAIL).
 * @see <a href="https://www.web3d.org/specifications/java/X3DJSAIL.html">X3DJSAIL</a>
 * @see <a href="https://junit.org/junit5/docs/current/user-guide/#running-tests-build-ant">JUnit5 running tests with Ant</a>
 * @see <a href="https://ant.apache.org/manual/Tasks/junitlauncher.html">Ant task junitlauncher</a>
 * @see <a href="https://www.petrikainulainen.net/programming/testing/junit-5-tutorial-writing-assertions-with-junit-5-api">Tutorial: writing assertions with JUnit5</a>
 * @see <a href="../license.html">License</a>   
 */
class FieldObjectTests
{
    @Test
    @DisplayName("Test initialization of all X3D SF/MF field objects")
    void fieldObjectInitializationsTest()
	{
        System.out.println("FieldObjectTests.fieldObjectInitializationsTest() start...");

        // assert statements
        System.out.println ("Preliminary tests...");
        assertTrue (true,  "this test should explicitly pass");
        assertFalse(false, "this test should explicitly fail");
        
        // now tests for each field type
        SFBoolTests();
        MFBoolTests();
        
        SFImageTests();
        MFImageTests();
        
        SFInt32Tests();
        MFInt32Tests();
        
        // regex expressions for SFFloat, SFDouble and SFTime are identical but classes are unique, so test each of them!
        SFFloatTests();
        SFDoubleTests();
        SFTimeTests();
        // regex expressions for MFFloat, MFDouble and MFTime are identical but classes are unique, so test each of them!
        MFFloatTests();
        MFDoubleTests();
        MFTimeTests();
        
        SFVec2fTests();
        SFVec2dTests();
        MFVec2fTests();
        MFVec2dTests();
        
        SFVec3fTests();
        SFVec3fBboxSizeTests();
        SFVec3dTests();
        MFVec3fTests();
        MFVec3dTests();
        
        SFVec4fTests();
        SFVec4dTests();
        MFVec4fTests();
        MFVec4dTests();
        
        SFColorTests();
        MFColorTests();
        SFColorRGBATests();
        MFColorRGBATests();
        
        SFRotationTests();
        MFRotationTests();
        
        SFMatrix3fTests();
        SFMatrix3dTests();
        MFMatrix3fTests();
        MFMatrix3dTests();
        
        SFMatrix4fTests();
        SFMatrix4dTests();
        MFMatrix4fTests();
        MFMatrix4dTests();
        
        System.out.println("FieldObjectTests.fieldObjectInitializationsTest() complete");
    }
    
    @Test
    @DisplayName("Test SFBool single-field boolean")
    void SFBoolTests()
	{
        System.out.println ("SFBoolTests...");
        // default value for SFBool is false, not true
        assertTrue  ((SFBool.DEFAULT_VALUE == new SFBool().setValueByString(SFBool.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                       "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFBool testSFBool = new SFBool(); // static initializer is tested, might throw exception
        assertFalse  (SFBool.DEFAULT_VALUE,       "test correct default value for this field object");
        assertTrue  (testSFBool.matches(),       "testSFBool.matches() tests that object initialization correctly matches regex");
        assertTrue  (SFBool.matches(SFBool.DEFAULT_VALUE_STRING),
                                                       "SFBool.matches(SFBool.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFBool.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFBool.REGEX.contains("^") && !SFBool.REGEX.contains("$"), "test SFBool.REGEX does not contain anchor characters ^ or $");

        testSFBool.setValue(true);               // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (testSFBool.getValue(),      "tests setting object value to true results in value of true");
        testSFBool.setValue(false);              // returns void because it matches (overrides) Java SAI specification interface
        assertFalse (testSFBool.getValue(),      "tests setting object value to false results in value of false");
        
        assertTrue  (SFBool.matches("true"),     "SFBool.matches(\"true\")  tests correct string value");
        assertTrue  (SFBool.matches("false"),    "SFBool.matches(\"false\") tests correct string value");
        assertTrue  (SFBool.matches("  true "),  "SFBool.matches(\"  true \") tests correct string value, including external whitespace");
        assertTrue  (SFBool.matches(" false "),  "SFBool.matches(\" false \") tests correct string value, including external whitespace");
        
        assertFalse (SFBool.matches(""),         "SFBool.matches(\"\") tests incorrect empty string value");
        assertFalse (SFBool.matches(","),        "SFBool.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFBool.matches("true,"),    "SFBool.matches(\"true,\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFBool.matches(",false"),   "SFBool.matches(\",false\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFBool.matches("TRUE"),     "SFBool.matches(\"TRUE\")  tests incorrect case of string value");
        assertFalse (SFBool.matches("FALSE"),    "SFBool.matches(\"FALSE\") tests incorrect case of string value");
        assertFalse (SFBool.matches("rtue"),     "SFBool.matches(\"rtue\") tests incorrect ordering of characters in string value");
        assertFalse (SFBool.matches("aflse"),    "SFBool.matches(\"aflse\") tests incorrect ordering of characters in string value");
        assertFalse (SFBool.matches("blah"),     "SFBool.matches(\"blah\")  tests incorrect string value");
        assertFalse (SFBool.matches("NaN"),      "SFBool.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFBool multiple-field boolean")
    void MFBoolTests()
	{
        System.out.println ("MFBoolTests...");
        assertTrue  (Arrays.equals(MFBool.DEFAULT_VALUE, new MFBool().setValueByString(MFBool.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFBool testMFBool = new MFBool(); // static initializer is tested, might throw exception
        boolean[] emptyArray       = {};
        boolean[] singleTrueArray  = { true  };
        boolean[] singleFalseArray = { false };
        boolean[] trueTrueArray    = { true, true  };
        boolean[] trueFalseArray   = { true, false };
        boolean[] falseTrueArray   = { false, true };
        boolean[] falseFalseArray  = { false, false };
        assertTrue  (Arrays.equals(emptyArray, MFBool.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (testMFBool.matches(),       "testMFBool.matches() tests that object initialization correctly matches regex");
        assertTrue  (MFBool.matches(MFBool.DEFAULT_VALUE_STRING),
                                                       "MFBool.matches(MFBool.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFBool.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFBool.REGEX.contains("^") && !MFBool.REGEX.contains("$"), "test MFBool.REGEX does not contain anchor characters ^ or $");

        testMFBool.setValue(true);               // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleTrueArray,  testMFBool.getPrimitiveValue()), "tests setting object value to boolean true results in same value");
        assertTrue  (testMFBool.get1Value(0),   "tests setting object value to true results in get1Value(index 0) of true");
        
        testMFBool.setValue(false);               // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleFalseArray,  testMFBool.getPrimitiveValue()), "tests setting object value to boolean false results in same value");
        assertFalse (testMFBool.get1Value(0),   "tests setting object value to false results in get1Value(index 0) of false");
        
        testMFBool.setValue (singleTrueArray);
        assertTrue  (Arrays.equals(singleTrueArray,  testMFBool.getPrimitiveValue()), "tests setting object value to boolean[] array { true } results in same value");
        testMFBool.setValue(false);              // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleFalseArray, testMFBool.getPrimitiveValue()), "tests setting object value to boolean true results in same value");
        testMFBool.setValue (singleFalseArray);
        assertTrue  (Arrays.equals(singleFalseArray, testMFBool.getPrimitiveValue()), "tests setting object value to boolean[] array { false } results in same value");
        testMFBool.setValue (trueTrueArray);
        assertTrue  (Arrays.equals(trueTrueArray,    testMFBool.getPrimitiveValue()), "tests setting object value to boolean[] array { true, true } results in same value");
        testMFBool.setValue (trueFalseArray);
        assertTrue  (Arrays.equals(trueFalseArray,   testMFBool.getPrimitiveValue()), "tests setting object value to boolean[] array { true, false } results in same value");
        testMFBool.setValue (falseTrueArray);
        assertTrue  (Arrays.equals(falseTrueArray,   testMFBool.getPrimitiveValue()), "tests setting object value to boolean[] array { false, true } results in same value");
        testMFBool.setValue (falseFalseArray);
        assertTrue  (Arrays.equals(falseFalseArray,  testMFBool.getPrimitiveValue()), "tests setting object value to boolean[] array { false, false } results in same value");
        
        assertTrue  (MFBool.matches(""),            "MFBool.matches(\"\") tests correct empty string value");
        assertTrue  (MFBool.matches("true"),        "MFBool.matches(\"true\")  tests correct string value");
        assertTrue  (MFBool.matches("false"),       "MFBool.matches(\"false\") tests correct string value");
        assertTrue  (MFBool.matches("true true"),   "MFBool.matches(\"true true\")   tests correct string value");
        assertTrue  (MFBool.matches("true false"),  "MFBool.matches(\"true false\")  tests correct string value");
        assertTrue  (MFBool.matches("false true"),  "MFBool.matches(\"false true\")  tests correct string value");
        assertTrue  (MFBool.matches("false false"), "MFBool.matches(\"false false\") tests correct string value");
        assertTrue  (MFBool.matches("  true "),  "MFBool.matches(\"  true \") tests correct string value, including external whitespace");
        assertTrue  (MFBool.matches(" false "),  "MFBool.matches(\" false \") tests correct string value, including external whitespace");
        assertTrue  (MFBool.matches("  true  true  "),  "MFBool.matches(\"  true \") tests correct string value, including whitespace");
        assertTrue  (MFBool.matches(" false  false "),  "MFBool.matches(\" false  false \") tests correct string value, including whitespace");
        assertTrue  (MFBool.matches("  false , true  "),"MFBool.matches(\"  false , true \") tests correct string value, including whitespace and commas");
        assertTrue  (MFBool.matches(" true,  false "),  "MFBool.matches(\" true,  false \") tests correct string value, including whitespace and commas");
        assertTrue  (MFBool.matches(" true,  false , "),"MFBool.matches(\" true,  false , \") tests correct string value, including whitespace and commas, with allowed trailing comma");
        
        assertFalse (MFBool.matches(","),           "MFBool.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (MFBool.matches("TRUE"),        "MFBool.matches(\"TRUE\")  tests incorrect case of string value");
        assertFalse (MFBool.matches("FALSE"),       "MFBool.matches(\"FALSE\") tests incorrect case of string value");
        assertFalse (MFBool.matches("rtue"),        "MFBool.matches(\"rtue\") tests incorrect ordering of characters in string value");
        assertFalse (MFBool.matches("aflse"),       "MFBool.matches(\"aflse\") tests incorrect ordering of characters in string value");
        assertFalse (MFBool.matches("blah"),        "MFBool.matches(\"blah\")  tests incorrect string value");
        assertFalse (MFBool.matches("NaN"),         "MFBool.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
        assertFalse (MFBool.matches("true TRUE"),   "MFBool.matches(\"true TRUE\")  tests incorrect case of string value");
        assertFalse (MFBool.matches("false FALSE"), "MFBool.matches(\"false FALSE\") tests incorrect case of string value");
    }
    
    @Test
    @DisplayName("Test SFImage single-field variable-length integer/hexadecimal array")
    void SFImageTests()
	{
        System.out.println ("SFImageTests...");
        assertTrue  (Arrays.equals(SFImage.DEFAULT_VALUE, new SFImage().setValueByString(SFImage.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFImage testSFImage = new SFImage(); // static initializer is tested, might throw exception
        assertTrue  (testSFImage.matches(),       "testSFImage.matches() tests that object initialization correctly matches regex");
        int[]  emptyArray       = {};
        int[]  defaultValueArray= { 0, 0, 0 };
        int[]  singleValueArray = { 1, 1, 1, 0 };
        int[]  doubleValueArray = { 1, 2, 2, 0xFF00,   0xFF00 };
        int[]  tripleValueArray = { 1, 3, 3, 0xFF0000, 0x00FF00, 0x0000FF };
      int[] quadrupleValueArray = { 2, 2, 2, 0xFF00,   0x00FF,   0xF0F0,  0x00FF };
        int[]    rgbaValueArray = { 1, 3, 4, 0xFF000088, 0x00FF0088, 0x0000FF88 }; // RGBA
        
        assertTrue  (Arrays.equals(defaultValueArray, SFImage.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (SFImage.matches(SFImage.DEFAULT_VALUE_STRING),
                                                        "SFImage.matches(SFImage.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFImage.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFImage.REGEX.contains("^") && !SFImage.REGEX.contains("$"), "test SFImage.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertFalse  (SFVec2f.REGEX.equals(SFImage.REGEX), "test SFVec2f.REGEX.equals(SFImage.REGEX) returns false");

        testSFImage.setValue(0, 0, 0, emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(defaultValueArray,  testSFImage.getPrimitiveValue()), "tests setting object value to (0, 0, 0, emptyArray) results in default singleton array with same value");
        testSFImage.setValue(defaultValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(defaultValueArray,  testSFImage.getPrimitiveValue()), "tests setting object value to (defaultValueArray) results in default singleton array with same value");
//      System.out.println("tests defaultValueArray.getPixelsString()=" + testSFImage.getPixelsString());
        assertEquals(testSFImage.getPixelsString(),"", "tests defaultValueArray.getPixelsString()");

        testSFImage.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleValueArray,testSFImage.getPrimitiveValue()),   "tests setting object value to (singleValueArray) results in equivalent getPrimitiveValue()");
//      System.out.println("tests singleValueArray.getPixelsString()=" + testSFImage.getPixelsString());
        assertEquals(testSFImage.getPixelsString(),"0x00", "tests singleValueArray.getPixelsString()");
      
        testSFImage.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(doubleValueArray,testSFImage.getPrimitiveValue()),   "tests setting object value to (doubleValueArray) results in equivalent getPrimitiveValue()");
//      System.out.println("tests doubleValueArray.getPixelsString()=" + testSFImage.getPixelsString());
        assertEquals(testSFImage.getPixelsString(),"0xFF00 0xFF00", "tests doubleValueArray.getPixelsString()");
      
        testSFImage.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(tripleValueArray,testSFImage.getPrimitiveValue()),   "tests setting object value to (tripleValueArray) results in equivalent getPrimitiveValue()");
//      System.out.println("tests tripleValueArray.getPixelsString()=" + testSFImage.getPixelsString());
        assertEquals(testSFImage.getPixelsString(),"0xFF0000 0x00FF00 0x0000FF", "tests tripleValueArray.getPixelsString()");
      
        testSFImage.setValue(quadrupleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(quadrupleValueArray,testSFImage.getPrimitiveValue()),   "tests setting object value to (quadrupleValueArray) results in equivalent getPrimitiveValue()");
//      System.out.println("tests quadrupleValueArray.getPixelsString()=" + testSFImage.getPixelsString());
        assertEquals(testSFImage.getPixelsString(),"0xFF00 0x00FF 0xF0F0 0x00FF", "tests quadrupleValueArray.getPixelsString()");

        testSFImage.setValue(rgbaValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(rgbaValueArray,testSFImage.getPrimitiveValue()),   "tests setting object value to (rgbaValueArray) results in equivalent getPrimitiveValue()");
//      System.out.println("tests rgbaValueArray.getPixelsString()=" + testSFImage.getPixelsString());
        assertEquals(testSFImage.getPixelsString(),"0xFF000088 0x00FF0088 0x0000FF88", "tests rgbaValueArray.getPixelsString()");

        assertTrue  (SFImage.matches("0 0 0"),      "SFImage.matches( \"0 0 0\")   tests correct string value");
        
		String valueHexadecimalInput  = " 1 2 3 0x040404 0x050505 ";
		String valueHexadecimalString =  "1 2 3 0x40404 0x50505";
		String valueDecimalString     =  "1 2 3 263172 328965";
		assertTrue  (SFImage.matches(valueHexadecimalInput),      "SFImage.matches( \"" + valueHexadecimalInput + "\")   tests correct string value");
        assertTrue  (testSFImage.setValueByString(valueHexadecimalInput).matches(), "testSFImage.setValueByString(\" 1 2 3 0x040404 0x050505 \").matches() tests correct string value");
        assertTrue  (testSFImage.toStringHexadecimal().equals(valueHexadecimalString), "testSFImage.toStringHexadecimal() tests correct string output");
        ConfigurationProperties.setSFImagePixelOutputHexadecimal(false);
		assertFalse (ConfigurationProperties.isSFImagePixelOutputHexadecimal(), "test ConfigurationProperties.setSFImagePixelOutputHexadecimal(false)");
        assertTrue  (testSFImage.toStringDecimal().equals(valueDecimalString), "testSFImage.toStringDecimal() tests correct string output");
        assertTrue  (testSFImage.toString().equals(testSFImage.toStringDecimal()), "testSFImage.toString() checks Decimal string output");
        ConfigurationProperties.setSFImagePixelOutputHexadecimal(true);
		assertTrue  (ConfigurationProperties.isSFImagePixelOutputHexadecimal(), "test ConfigurationProperties.setSFImagePixelOutputHexadecimal(true)");
		assertTrue  (testSFImage.toString().equals(testSFImage.toStringHexadecimal()), "testSFImage.toString() checks Hexadecimal string output");
        
		// TODO check other utility methods
        
        assertFalse (SFImage.matches(""),          "SFImage.matches(\"\") tests incorrect empty string value");
        assertFalse (SFImage.matches(","),         "SFImage.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFImage.matches("true false"),"SFImage.matches(\"true false\") tests incorrect boolean string value");
        assertFalse (SFImage.matches("blah"),      "SFImage.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFImage.matches("NaN NaN"),   "SFImage.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFImage multi-field variable-length integer/hexadecimal array")
    void MFImageTests()
	{
        System.out.println ("MFImageTests...");
        assertTrue  (Arrays.equals(MFImage.DEFAULT_VALUE, new MFImage().setValueByString(MFImage.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFImage testMFImage = new MFImage(); // static initializer is tested, might throw exception
        assertTrue  (testMFImage.matches(),       "testMFImage.matches() tests that object initialization correctly matches regex");
        int[]  emptyArray       = {};
        int[]  defaultValueArray= { 0, 0, 0 };
        int[]  singleValueArray = { 1, 1, 1, 0 };
        int[]  doubleValueArray = { 1, 2, 2, 0xFF00,   0xFF00 };
        int[]  tripleValueArray = { 1, 3, 3, 0xFF0000, 0x00FF00, 0x0000FF };
      int[] quadrupleValueArray = { 2, 2, 2, 0xFF00,   0x00FF,   0xF0F0,  0x00FF };

        assertTrue  (Arrays.equals(emptyArray, MFImage.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFImage.matches(MFImage.DEFAULT_VALUE_STRING),
                                                        "MFImage.matches(MFImage.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFImage.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFImage.REGEX.contains("^") && !MFImage.REGEX.contains("$"), "test MFImage.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertFalse  (MFVec2f.REGEX.equals(MFImage.REGEX), "test MFVec2f.REGEX.equals(MFImage.REGEX) returns false");

        // TODO utility method needed to set singleton object using individual values
//        testMFImage.setValue(0.0d, 0.0d); // returns void because it matches (overrides) Java SAI specification interface
//        assertTrue  (Arrays.equals(singleValueArray,  testMFImage.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testMFImage.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(emptyArray,testMFImage.getPrimitiveValue()),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFImage.matches(),       "testMFImage.matches() tests emptyArray initialization correctly matches regex");
        testMFImage.setValue(defaultValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(defaultValueArray,testMFImage.getPrimitiveValue()),   "tests setting object value to defaultValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFImage.matches(),       "testMFImage.matches() tests defaultValueArray correctly matches regex");
        testMFImage.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleValueArray,testMFImage.getPrimitiveValue()),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFImage.matches(),       "testMFImage.matches() tests singleValueArray correctly matches regex");
        testMFImage.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(doubleValueArray,testMFImage.getPrimitiveValue()),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFImage.matches(),       "testMFImage.matches() tests doubleValueArray correctly matches regex");
        testMFImage.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(tripleValueArray,testMFImage.getPrimitiveValue()),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFImage.matches(),       "testMFImage.matches() tests tripleValueArray correctly matches regex");
        testMFImage.setValue(quadrupleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(quadrupleValueArray,testMFImage.getPrimitiveValue()),   "tests setting object value to quadrupleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFImage.matches(),       "testMFImage.matches() tests quadrupleValueArray correctly matches regex");
        
        String valueHexadecimalInput  = " 1 2 3 0x040404 0x050505 ";
		String valueHexadecimalString = "1 2 3 0x40404 0x50505";
		String valueDecimalString     = "1 2 3 263172 328965";
		assertTrue  (SFImage.matches(valueHexadecimalInput),      "SFImage.matches( \"" + valueHexadecimalInput + "\")   tests correct string value");
        assertTrue  (testMFImage.setValueByString(valueHexadecimalInput).matches(), "testMFImage.setValueByString(\" 1 2 3 0x040404 0x050505 \").matches() tests correct string value");
        assertTrue  (testMFImage.toStringHexadecimal().equals(valueHexadecimalString), "testMFImage.toStringHexadecimal() tests correct string output");
        ConfigurationProperties.setSFImagePixelOutputHexadecimal(false);
		assertFalse (ConfigurationProperties.isSFImagePixelOutputHexadecimal(), "test ConfigurationProperties.setSFImagePixelOutputHexadecimal(false)");
        assertTrue  (testMFImage.toStringDecimal().equals(valueDecimalString), "testMFImage.toStringDecimal() tests correct string output");
        assertTrue  (testMFImage.toString().equals(testMFImage.toStringDecimal()), "testMFImage.toString() checks Decimal string output");
        ConfigurationProperties.setSFImagePixelOutputHexadecimal(true);
		assertTrue  (ConfigurationProperties.isSFImagePixelOutputHexadecimal(), "test ConfigurationProperties.setSFImagePixelOutputHexadecimal(true)");
		assertTrue  (testMFImage.toString().equals(testMFImage.toStringHexadecimal()), "testMFImage.toString() checks Hexadecimal string output");
        
		assertTrue  (MFImage.matches(""),            "MFImage.matches(\"\") tests correct empty string value");
        assertFalse (MFImage.matches(","),           "MFImage.matches(\",\") tests incorrect inclusion of comma as whitespace");
        // TODO more tests with multiple images
        
        assertFalse (MFImage.matches("true false"),"MFImage.matches(\"true false\") tests incorrect boolean string value");
        assertFalse (MFImage.matches("blah"),      "MFImage.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFImage.matches("NaN NaN"),   "MFImage.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFInt32 single-field 32-bit integer")
    void SFInt32Tests()
	{
        System.out.println ("SFInt32Tests...");
        assertTrue  ((SFInt32.DEFAULT_VALUE == new SFInt32().setValueByString(SFInt32.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFInt32 testSFInt32 = new SFInt32(); // static initializer is tested, might throw exception
        assertTrue  (testSFInt32.matches(),       "testSFInt32.matches() tests that object initialization correctly matches regex");
        assertEquals(0, SFInt32.DEFAULT_VALUE,    "test correct default value for this field object");
        assertTrue  (SFInt32.matches(SFInt32.DEFAULT_VALUE_STRING),
                                                        "SFInt32.matches(SFInt32.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFInt32.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFInt32.REGEX.contains("^") && !SFInt32.REGEX.contains("$"), "test SFInt32.REGEX does not contain anchor characters ^ or $");

		testSFInt32.setValue(10); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (testSFInt32.toStringHexadecimal().equalsIgnoreCase("0xA"), "test SFInt32.toStringHexadecimal().equalsIgnoreCase(\"A\") tests hexadecimal output");

        testSFInt32.setValue(1); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 1,testSFInt32.getValue(),   "tests setting object value to 1 results in value of 1");
        testSFInt32.setValue(-1); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(-1,testSFInt32.getValue(),   "tests setting object value to -1 results in value of -1");
        
        assertTrue  (SFInt32.matches( "0"),       "SFInt32.matches( \"0\")   tests correct string value");
        assertTrue  (SFInt32.matches( "1"),       "SFInt32.matches( \"1\")   tests correct string value");
        assertTrue  (SFInt32.matches("-1"),       "SFInt32.matches(\"-1\")   tests correct string value");
        assertTrue  (SFInt32.matches("  3 "),     "SFInt32.matches(\"  3 \") tests correct string value, including external whitespace");
        assertTrue  (SFInt32.matches(" -3 "),     "SFInt32.matches(\" -3 \") tests correct string value, including external whitespace");
        assertTrue  (SFInt32.matches("  12E45  "),"SFInt32.matches(\"  12E45  \") tests correct string value, scientific notation");
        assertTrue  (SFInt32.matches(" +12E+45 "),"SFInt32.matches(\" +12E+45 \") tests correct string value, scientific notation");
        assertTrue  (SFInt32.matches(" -12E-45 "),"SFInt32.matches(\" -12E-45 \") tests correct string value, scientific notation");
        
        assertFalse (SFInt32.matches(""),         "SFInt32.matches(\"\") tests incorrect empty string value");
        assertFalse (SFInt32.matches(","),        "SFInt32.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFInt32.matches("true"),     "SFInt32.matches(\"true\") tests incorrect boolean string value");
        assertFalse (SFInt32.matches("blah"),     "SFInt32.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFInt32.matches("0 1"),      "SFInt32.matches(\"0 1\")  tests incorrect array as string value");
        assertFalse (SFInt32.matches("NaN"),      "SFInt32.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFInt32 multi-field 32-bit integer array")
    void MFInt32Tests()
	{
        System.out.println ("MFInt32Tests...");
        assertTrue  (Arrays.equals(MFInt32.DEFAULT_VALUE, new MFInt32().setValueByString(MFInt32.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFInt32 testMFInt32 = new MFInt32(); // static initializer is tested, might throw exception
        assertTrue  (testMFInt32.matches(),       "testMFInt32.matches() tests that object initialization correctly matches regex");
        int[] emptyArray       = {};
        int[] singleValueArray = { 0 };
        int[] doubleValueArray = { -1, -2 };
        int[] tripleValueArray = {  3,  4,  5 };
        assertTrue  (Arrays.equals(emptyArray, MFInt32.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (MFInt32.matches(MFInt32.DEFAULT_VALUE_STRING),
                                                        "MFInt32.matches(MFInt32.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFInt32.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFInt32.REGEX.contains("^") && !MFInt32.REGEX.contains("$"), "test MFInt32.REGEX does not contain anchor characters ^ or $");

        testMFInt32.setValue(0); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 0,testMFInt32.get1Value(0),   "tests setting object value to 0 results in get1Value(index 0) of 0");
        assertTrue  (Arrays.equals(singleValueArray,  testMFInt32.getPrimitiveValue()), "tests setting object value to 0 results in singleton array with same value");
        
        testMFInt32.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFInt32.getPrimitiveValue(),   "tests setting object value to emptyArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFInt32.matches(),       "testMFInt32.matches() tests emptyArray initialization correctly matches regex");
        testMFInt32.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFInt32.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFInt32.matches(),       "testMFInt32.matches() tests singleValueArray initialization correctly matches regex");
        testMFInt32.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFInt32.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFInt32.matches(),       "testMFInt32.matches() tests doubleValueArray initialization correctly matches regex");
        testMFInt32.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFInt32.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFInt32.matches(),       "testMFInt32.matches() tests tripleValueArray initialization correctly matches regex");
        
        assertTrue  (MFInt32.matches(""),           "MFInt32.matches(\"\") tests correct empty string value");
        assertFalse (MFInt32.matches(","),          "MFInt32.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFInt32.matches( "0"),         "MFInt32.matches( \"0\")   tests correct string value");
        assertTrue  (MFInt32.matches( "1"),         "MFInt32.matches( \"1\")   tests correct string value");
        assertTrue  (MFInt32.matches("-1"),         "MFInt32.matches(\"-1\")   tests correct string value");
        assertTrue  (MFInt32.matches("  3 "),       "MFInt32.matches(\"  3 \") tests correct string value, including external whitespace");
        assertTrue  (MFInt32.matches(" -3 "),       "MFInt32.matches(\" -3 \") tests correct string value, including external whitespace");
        assertTrue  (MFInt32.matches(" 0  12E45  "),"MFInt32.matches(\" 0  12E45  \") tests correct string value, scientific notation");
        assertTrue  (MFInt32.matches("+0 +12E+45 "),"MFInt32.matches(\"+0 +12E+45 \") tests correct string value, scientific notation");
        assertTrue  (MFInt32.matches("-0,-12E-45 "),"MFInt32.matches(\"-0,-12E-45 \") tests correct string value, scientific notation");
        assertTrue  (MFInt32.matches("0 1"),        "MFInt32.matches(\"0 1\")  tests correct array as string value");
        assertTrue  (MFInt32.matches("0, 1"),       "MFInt32.matches(\"0, 1\")  tests correct array as string value, including whitespace and comma");
        assertTrue  (MFInt32.matches("0 , 1 , "),   "MFInt32.matches(\"0 , 1 , \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");

        assertFalse (MFInt32.matches("true"),     "MFInt32.matches(\"true\") tests incorrect boolean string value");
        assertFalse (MFInt32.matches("blah"),     "MFInt32.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFInt32.matches("NaN"),      "MFInt32.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFFloat single-field single-precision floating-point number")
    void SFFloatTests()
	{
        System.out.println ("SFFloatTests...");
        assertTrue  ((SFFloat.DEFAULT_VALUE == new SFFloat().setValueByString(SFFloat.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                          "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFFloat testSFFloat = new SFFloat(); // static initializer is tested, might throw exception
        assertTrue  (testSFFloat.matches(),         "testSFFloat.matches() tests that object initialization correctly matches regex");
        assertEquals(0.0f, SFFloat.DEFAULT_VALUE,   "test correct default value for this field object");
        assertTrue  (SFFloat.matches(SFFloat.DEFAULT_VALUE_STRING),
                                                          "SFFloat.matches(SFFloat.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFFloat.isDefaultValue(),  "test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFFloat.REGEX.contains("^") && !SFFloat.REGEX.contains("$"), "test SFFloat.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFFloat.REGEX.equals(SFDouble.REGEX), "test SFFloat.REGEX.equals(SFDouble.REGEX) returns true");
        assertTrue  (SFFloat.REGEX.equals(SFTime.REGEX),   "test SFFloat.REGEX.equals(SFTime.REGEX) returns true");
        
        testSFFloat.setValue(1); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 1.0f,testSFFloat.getValue(),  "tests setting object value to 1 results in value of 1.0f");
        testSFFloat.setValue(1.0f); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 1.0f,testSFFloat.getValue(),  "tests setting object value to 1.0f results in value of 1.0f");
        testSFFloat.setValue(1.0d); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 1.0f,testSFFloat.getValue(),  "tests setting object value to 1.0d results in value of 1.0f");
        testSFFloat.setValue(-1); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(-1.0f,testSFFloat.getValue(),  "tests setting object value to -1 results in value of -1.0f");
        
        assertTrue  (SFFloat.matches( "0"),       "SFFloat.matches( \"0\")   tests correct string value");
        assertTrue  (SFFloat.matches( "1"),       "SFFloat.matches( \"1\")   tests correct string value");
        assertTrue  (SFFloat.matches("-1"),       "SFFloat.matches(\"-1\")   tests correct string value");
        assertTrue  (SFFloat.matches( "0.0"),     "SFFloat.matches( \"0.0\") tests correct string value");
        assertTrue  (SFFloat.matches( "1.0"),     "SFFloat.matches( \"1.0\") tests correct string value");
        assertTrue  (SFFloat.matches("-1.0"),     "SFFloat.matches(\"-1.0\") tests correct string value");
        assertTrue  (SFFloat.matches("  3 "),     "SFFloat.matches(\"  3 \") tests correct string value, including external whitespace");
        assertTrue  (SFFloat.matches(" -3 "),     "SFFloat.matches(\" -3 \") tests correct string value, including external whitespace");
        assertTrue  (SFFloat.matches(" 12.3E45 "),"SFFloat.matches(\" 12.3E45 \") tests correct string value, scientific notation");
        assertTrue  (SFFloat.matches("+12.3E+45"),"SFFloat.matches(\"+12.3E+45\") tests correct string value, scientific notation");
        assertTrue  (SFFloat.matches("-12.3E-45"),"SFFloat.matches(\"-12.3E-45\") tests correct string value, scientific notation");
        assertTrue  (SFFloat.matches( ".6"),      "SFFloat.matches( \".6\") tests correct string value, no leading digit before decimal point");
        assertTrue  (SFFloat.matches("-.6"),      "SFFloat.matches(\"-.6\") tests correct string value, no leading digit before decimal point");
        assertTrue  (SFFloat.matches( ".6e7"),    "SFFloat.matches( \".6e7\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (SFFloat.matches("-.6e-7"),   "SFFloat.matches(\"-.6e-7\") tests correct string value, no leading digit before decimal point, scientific notation");

        assertFalse (SFFloat.matches(""),        "SFFloat.matches(\"\") tests incorrect empty string value");
        assertFalse (SFFloat.matches(","),       "SFFloat.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFFloat.matches("true"),    "SFFloat.matches(\"true\") tests incorrect boolean string value");
        assertFalse (SFFloat.matches("blah"),    "SFFloat.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFFloat.matches("0 1"),     "SFFloat.matches(\"0 1\")  tests incorrect array as string value");
        assertFalse (SFFloat.matches("0.0 1.0"), "SFFloat.matches(\"0.0 1.0\") tests incorrect array as string value");
        assertFalse (SFFloat.matches("NaN"),     "SFFloat.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFFloat multi-field single-precision floating-point array")
    void MFFloatTests()
	{
        System.out.println ("MFFloatTests...");
        assertTrue  (Arrays.equals(MFFloat.DEFAULT_VALUE, new MFFloat().setValueByString(MFFloat.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFFloat testMFFloat = new MFFloat(); // static initializer is tested, might throw exception
        assertTrue  (testMFFloat.matches(),       "testMFFloat.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f };
        float[] doubleValueArray = { -1.0f, -2.0f };
        float[] tripleValueArray = {  3.0f,  4.0f,  5.0f };
        assertTrue  (Arrays.equals(emptyArray, MFFloat.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (MFFloat.matches(MFFloat.DEFAULT_VALUE_STRING),
                                                        "MFFloat.matches(MFFloat.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFFloat.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFFloat.REGEX.contains("^") && !MFFloat.REGEX.contains("$"), "test MFFloat.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFFloat.REGEX.equals(MFDouble.REGEX), "test MFFloat.REGEX.equals(MFDouble.REGEX) returns true");
        assertTrue  (MFFloat.REGEX.equals(MFTime.REGEX),   "test MFFloat.REGEX.equals(MFTime.REGEX) returns true");

        testMFFloat.setValue(0.0f); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 0.0f,testMFFloat.get1Value(0),   "tests setting object value to 0.0f results in get1Value(index 0) of 0");
        assertTrue  (Arrays.equals(singleValueArray,  testMFFloat.getPrimitiveValue()), "tests setting object value to 0.0f results in singleton array with same value");
        
        testMFFloat.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFFloat.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFFloat.matches(),       "testMFFloat.matches() tests emptyArray initialization correctly matches regex");
        testMFFloat.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFFloat.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        testMFFloat.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFFloat.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        testMFFloat.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFFloat.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        
        assertTrue  (MFFloat.matches(""),          "MFFloat.matches(\"\") tests correct empty string value");
        assertFalse (MFFloat.matches(","),         "MFFloat.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFFloat.matches( "0"),        "MFFloat.matches( \"0\")   tests correct string value");
        assertTrue  (MFFloat.matches( "1"),        "MFFloat.matches( \"1\")   tests correct string value");
        assertTrue  (MFFloat.matches("-1"),        "MFFloat.matches(\"-1\")   tests correct string value");
        assertTrue  (MFFloat.matches("  3 "),      "MFFloat.matches(\"  3 \") tests correct string value, including external whitespace");
        assertTrue  (MFFloat.matches(" -3 "),      "MFFloat.matches(\" -3 \") tests correct string value, including external whitespace");
        assertTrue  (MFFloat.matches(" 0  12E45 "),"MFFloat.matches(\"0  12E45 \") tests correct string value, scientific notation");
        assertTrue  (MFFloat.matches("+0,+12E+45"),"MFFloat.matches(\"+0,+12E+45\") tests correct string value, scientific notation");
        assertTrue  (MFFloat.matches("-0,-12E-45"),"MFFloat.matches(\"-0,-12E-45\") tests correct string value, scientific notation");

        assertTrue  (MFFloat.matches( "0.0"),        "MFFloat.matches( \"0.0\")   tests correct string value");
        assertTrue  (MFFloat.matches( "1.0"),        "MFFloat.matches( \"1.0\")   tests correct string value");
        assertTrue  (MFFloat.matches("-1.0"),        "MFFloat.matches(\"-1.0\")   tests correct string value");
        assertTrue  (MFFloat.matches("  3.0 "),      "MFFloat.matches(\"  3.0 \") tests correct string value, including external whitespace");
        assertTrue  (MFFloat.matches(" -3.0 "),      "MFFloat.matches(\" -3.0 \") tests correct string value, including external whitespace");
        assertTrue  (MFFloat.matches("0 1"),         "MFFloat.matches(\"0 1\")  tests correct array as string value");
        assertTrue  (MFFloat.matches("0.0 1.0"),     "MFFloat.matches(\"0.0 1.0\")  tests correct array as string value");
        assertTrue  (MFFloat.matches(" 0.0  12.3E45  "),    "MFFloat.matches(\" 0.0  12.3E45  \") tests correct string value, scientific notation");
        assertTrue  (MFFloat.matches("+0.0 +12.3E+45 "),    "MFFloat.matches(\"+0.0 +12.3E+45 \") tests correct string value, scientific notation");
        assertTrue  (MFFloat.matches("-0.0,-12.3E-45 "),    "MFFloat.matches(\"-0.0,-12.3E-45 \") tests correct string value, scientific notation");
        assertTrue  (MFFloat.matches( ".6 -.6 .6e7 -.6e-7"),"MFFloat.matches(\".6 -.6 .6e7 -.6e-7\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (MFFloat.matches("0 , 1 , "),   "MFFloat.matches(\"0 , 1 , \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");
        
        assertFalse (MFFloat.matches("true"),     "MFFloat.matches(\"true\") tests incorrect boolean string value");
        assertFalse (MFFloat.matches("blah"),     "MFFloat.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFFloat.matches("NaN"),      "MFFloat.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFDouble single-field double-precision floating-point number")
    void SFDoubleTests()
	{
        System.out.println ("SFDoubleTests...");
        assertTrue  ((SFDouble.DEFAULT_VALUE == new SFDouble().setValueByString(SFDouble.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                           "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFDouble testSFDouble = new SFDouble(); // static initializer is tested, might throw exception
        assertTrue  (testSFDouble.matches(),         "testSFDouble.matches() tests that object initialization correctly matches regex");
        assertEquals(0.0d, SFDouble.DEFAULT_VALUE,   "test correct default value for this field object");
        assertTrue  (SFDouble.matches(SFDouble.DEFAULT_VALUE_STRING),
                                                           "SFDouble.matches(SFDouble.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFDouble.isDefaultValue(),  "test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFDouble.REGEX.contains("^") && !SFDouble.REGEX.contains("$"), "test SFDouble.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFFloat.REGEX.equals(SFDouble.REGEX), "test SFFloat.REGEX.equals(SFDouble.REGEX) returns true");
        assertTrue  (SFFloat.REGEX.equals(SFTime.REGEX),   "test SFFloat.REGEX.equals(SFTime.REGEX) returns true");

        testSFDouble.setValue(1); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 1.0d,testSFDouble.getValue(),  "tests setting object value to 1 results in value of 1.0d");
        testSFDouble.setValue(1.0d); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 1.0d,testSFDouble.getValue(),  "tests setting object value to 1.0d results in value of 1.0d");
        testSFDouble.setValue(1.0d); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 1.0d,testSFDouble.getValue(),  "tests setting object value to 1.0d results in value of 1.0d");
        testSFDouble.setValue(-1); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(-1.0d,testSFDouble.getValue(),  "tests setting object value to -1 results in value of -1.0d");
        
        assertTrue  (SFDouble.matches( "0"),      "SFDouble.matches( \"0\")   tests correct string value");
        assertTrue  (SFDouble.matches( "1"),      "SFDouble.matches( \"1\")   tests correct string value");
        assertTrue  (SFDouble.matches("-1"),      "SFDouble.matches(\"-1\")   tests correct string value");
        assertTrue  (SFDouble.matches( "0.0"),    "SFDouble.matches( \"0.0\") tests correct string value");
        assertTrue  (SFDouble.matches( "1.0"),    "SFDouble.matches( \"1.0\") tests correct string value");
        assertTrue  (SFDouble.matches("-1.0"),    "SFDouble.matches(\"-1.0\") tests correct string value");
        assertTrue  (SFDouble.matches("  3 "),    "SFDouble.matches(\"  3 \") tests correct string value, including external whitespace");
        assertTrue  (SFDouble.matches(" -3 "),    "SFDouble.matches(\" -3 \") tests correct string value, including external whitespace");
        assertTrue  (SFDouble.matches( ".6"),     "SFDouble.matches( \".6\") tests correct string value, no leading digit before decimal point");
        assertTrue  (SFDouble.matches("-.6"),     "SFDouble.matches(\"-.6\") tests correct string value, no leading digit before decimal point");
        assertTrue  (SFDouble.matches( ".6e7"),   "SFDouble.matches( \".6e7\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (SFDouble.matches("-.6e-7"),  "SFDouble.matches(\"-.6e-7\") tests correct string value, no leading digit before decimal point, scientific notation");

        assertFalse (SFDouble.matches(" 0.0  12.3E45  "),"SFDouble.matches(\" 0.0  12.3E45  \") tests correct string value, scientific notation");
        assertFalse (SFDouble.matches("+0.0 +12.3E+45 "),"SFDouble.matches(\"+0.0 +12.3E+45 \") tests correct string value, scientific notation");
        assertFalse (SFDouble.matches("-0.0,-12.3E-45 "),"SFDouble.matches(\"-0.0,-12.3E-45 \") tests correct string value, scientific notation");
        
        assertFalse (SFDouble.matches(""),        "SFDouble.matches(\"\") tests incorrect empty string value");
        assertFalse (SFDouble.matches(","),       "SFDouble.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFDouble.matches("true"),    "SFDouble.matches(\"true\") tests incorrect boolean string value");
        assertFalse (SFDouble.matches("blah"),    "SFDouble.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFDouble.matches("0 1"),     "SFDouble.matches(\"0 1\")  tests incorrect array as string value");
        assertFalse (SFDouble.matches("0.0 1.0"), "SFDouble.matches(\"0.0 1.0\") tests incorrect array as string value");
        assertFalse (SFDouble.matches("NaN"),     "SFDouble.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFDouble multi-field double-precision floating-point array")
    void MFDoubleTests()
	{
        System.out.println ("MFDoubleTests...");
        assertTrue  (Arrays.equals(MFDouble.DEFAULT_VALUE, new MFDouble().setValueByString(MFDouble.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFDouble testMFDouble = new MFDouble(); // static initializer is tested, might throw exception
        assertTrue  (testMFDouble.matches(),       "testMFDouble.matches() tests that object initialization correctly matches regex");
        double[] emptyArray       = {};
        double[] singleValueArray = { 0.0 };
        double[] doubleValueArray = { -1.0, -2.0 };
        double[] tripleValueArray = {  3.0,  4.0,  5.0 };
        assertTrue  (Arrays.equals(emptyArray, MFDouble.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (MFDouble.matches(MFDouble.DEFAULT_VALUE_STRING),
                                                        "MFDouble.matches(MFDouble.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFDouble.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFDouble.REGEX.contains("^") && !MFDouble.REGEX.contains("$"), "test MFDouble.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFFloat.REGEX.equals(MFDouble.REGEX), "test MFFloat.REGEX.equals(MFDouble.REGEX) returns true");
        assertTrue  (MFFloat.REGEX.equals(MFTime.REGEX),   "test MFFloat.REGEX.equals(MFTime.REGEX) returns true");

        testMFDouble.setValue(0.0); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 0.0,testMFDouble.get1Value(0),   "tests setting object value to 0.0 results in get1Value(index 0) of 0");
        assertTrue  (Arrays.equals(singleValueArray,  testMFDouble.getPrimitiveValue()), "tests setting object value to 0.0 results in singleton array with same value");
        
        testMFDouble.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFDouble.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFDouble.matches(),       "testMFDouble.matches() tests emptyArray initialization correctly matches regex");
        testMFDouble.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFDouble.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        testMFDouble.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFDouble.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        testMFDouble.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFDouble.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        
        assertTrue  (MFDouble.matches(""),          "MFDouble.matches(\"\") tests correct empty string value");
        assertFalse (MFDouble.matches(","),        "MFDouble.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFDouble.matches( "0"),        "MFDouble.matches( \"0\")   tests correct string value");
        assertTrue  (MFDouble.matches( "1"),        "MFDouble.matches( \"1\")   tests correct string value");
        assertTrue  (MFDouble.matches("-1"),        "MFDouble.matches(\"-1\")   tests correct string value");
        assertTrue  (MFDouble.matches("  3 "),      "MFDouble.matches(\"  3 \") tests correct string value, including external whitespace");
        assertTrue  (MFDouble.matches(" -3 "),      "MFDouble.matches(\" -3 \") tests correct string value, including external whitespace");
        assertTrue  (MFDouble.matches(" 0  12E45 "), "MFDouble.matches(\" 0  12E45  \") tests correct string value, scientific notation");
        assertTrue  (MFDouble.matches("+0 +12E+45 "),"MFDouble.matches(\"+0 +12E+45 \") tests correct string value, scientific notation");
        assertTrue  (MFDouble.matches("-0,-12E-45 "),"MFDouble.matches(\"-0,-12E-45 \") tests correct string value, scientific notation");

        assertTrue  (MFDouble.matches( "0.0"),        "MFDouble.matches( \"0.0\")   tests correct string value");
        assertTrue  (MFDouble.matches( "1.0"),        "MFDouble.matches( \"1.0\")   tests correct string value");
        assertTrue  (MFDouble.matches("-1.0"),        "MFDouble.matches(\"-1.0\")   tests correct string value");
        assertTrue  (MFDouble.matches("  3.0 "),      "MFDouble.matches(\"  3.0 \") tests correct string value, including external whitespace");
        assertTrue  (MFDouble.matches(" -3.0 "),      "MFDouble.matches(\" -3.0 \") tests correct string value, including external whitespace");
        assertTrue  (MFDouble.matches("0 1"),                "MFDouble.matches(\"0 1\")  tests correct array as string value");
        assertTrue  (MFDouble.matches("0.0 1.0"),            "MFDouble.matches(\"0.0 1.0\")  tests correct array as string value");
        assertTrue  (MFDouble.matches(" 0.0  12.3E45  "),    "MFDouble.matches(\" 0.0  12.3E45 \") tests correct string value, scientific notation");
        assertTrue  (MFDouble.matches("+0.0 +12.3E+45 "),    "MFDouble.matches(\"+0.0 +12.3E+45 \") tests correct string value, scientific notation");
        assertTrue  (MFDouble.matches("-0.0,-12.3E-45 "),    "MFDouble.matches(\"-0.0,-12.3E-45 \") tests correct string value, scientific notation");
        assertTrue  (MFDouble.matches( ".6 -.6 .6e7 -.6e-7"),"MFDouble.matches(\".6 -.6 .6e7 -.6e-7\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (MFDouble.matches("0 , 1 , "),           "MFDouble.matches(\"0 , 1 , \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");

        assertFalse (MFDouble.matches("true"),     "MFDouble.matches(\"true\") tests incorrect boolean string value");
        assertFalse (MFDouble.matches("blah"),     "MFDouble.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFDouble.matches("NaN"),      "MFDouble.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFTime single-field double-precision floating-point number")
    void SFTimeTests()
	{
        System.out.println ("SFTimeTests...");
        assertTrue  ((SFTime.DEFAULT_VALUE == new SFTime().setValueByString(SFTime.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                         "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFTime testSFTime = new SFTime(); // static initializer is tested, might throw exception
        assertTrue  (testSFTime.matches(),         "testSFTime.matches() tests that object initialization correctly matches regex");
        assertEquals(-1.0d, SFTime.DEFAULT_VALUE,  "test correct default value for this field object");
        assertTrue  (SFTime.matches(SFTime.DEFAULT_VALUE_STRING),
                                                         "SFTime.matches(SFTime.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFTime.isDefaultValue(),  "test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFTime.REGEX.contains("^") && !SFTime.REGEX.contains("$"), "test SFTime.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFFloat.REGEX.equals(SFDouble.REGEX), "test SFFloat.REGEX.equals(SFDouble.REGEX) returns true");
        assertTrue  (SFFloat.REGEX.equals(SFTime.REGEX),   "test SFFloat.REGEX.equals(SFTime.REGEX) returns true");

        testSFTime.setValue(1); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 1.0d,testSFTime.getValue(),  "tests setting object value to 1 results in value of 1.0d");
        testSFTime.setValue(1.0d); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 1.0d,testSFTime.getValue(),  "tests setting object value to 1.0d results in value of 1.0d");
        testSFTime.setValue(1.0d); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 1.0d,testSFTime.getValue(),  "tests setting object value to 1.0d results in value of 1.0d");
        testSFTime.setValue(-1); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(-1.0d,testSFTime.getValue(),  "tests setting object value to -1 results in value of -1.0d");
        testSFTime.setValue(-2); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(-2.0d,testSFTime.getValue(),  "tests setting object value to -2 results in value of -2.0d, a legal negative time value");
        
        assertFalse (SFTime.matches(""),        "SFTime.matches(\"\") tests incorrect empty string value");
        assertFalse (SFTime.matches(","),       "SFTime.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (SFTime.matches( "0"),      "SFTime.matches( \"0\")   tests correct string value");
        assertTrue  (SFTime.matches( "1"),      "SFTime.matches( \"1\")   tests correct string value");
        assertTrue  (SFTime.matches("-1"),      "SFTime.matches(\"-1\")   tests correct string value");
        assertTrue  (SFTime.matches( "0.0"),    "SFTime.matches( \"0.0\") tests correct string value");
        assertTrue  (SFTime.matches( "1.0"),    "SFTime.matches( \"1.0\") tests correct string value");
        assertTrue  (SFTime.matches("-1.0"),    "SFTime.matches(\"-1.0\") tests correct string value");
        assertTrue  (SFTime.matches("-2.0"),    "SFTime.matches(\"-2.0\") tests correct string value, a legal negative time value");
        assertTrue  (SFTime.matches("  3 "),    "SFTime.matches(\"  3 \") tests correct string value, including external whitespace");
        assertTrue  (SFTime.matches(" -3 "),    "SFTime.matches(\" -3 \") tests correct string value, including external whitespace");
        assertTrue  (SFTime.matches( ".6"),     "SFTime.matches( \".6\") tests correct string value, no leading digit before decimal point");
        assertTrue  (SFTime.matches("-.6"),     "SFTime.matches(\"-.6\") tests correct string value, no leading digit before decimal point");
        assertTrue  (SFTime.matches( ".6e7"),   "SFTime.matches( \".6e7\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (SFTime.matches("-.6e-7"),  "SFTime.matches(\"-.6e-7\") tests correct string value, no leading digit before decimal point, scientific notation");

        assertFalse (SFTime.matches("true"),    "SFTime.matches(\"true\") tests incorrect boolean string value");
        assertFalse (SFTime.matches("blah"),    "SFTime.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFTime.matches("0 1"),     "SFTime.matches(\"0 1\")  tests incorrect array as string value");
        assertFalse (SFTime.matches("0.0 1.0"), "SFTime.matches(\"0.0 1.0\") tests incorrect array as string value");
        assertFalse (SFTime.matches("NaN"),     "SFTime.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFTime multi-field double-precision floating-point array")
    void MFTimeTests()
	{
        System.out.println ("MFTimeTests...");
        assertTrue  (Arrays.equals(MFTime.DEFAULT_VALUE, new MFTime().setValueByString(MFTime.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFTime testMFTime = new MFTime(); // static initializer is tested, might throw exception
        assertTrue  (testMFTime.matches(),       "testMFTime.matches() tests that object initialization correctly matches regex");
        double[] emptyArray       = {};
        double[] singleValueArray = { 0.0 };
        double[] doubleValueArray = { -1.0, -2.0 };
        double[] tripleValueArray = {  3.0,  4.0,  5.0 };
        assertTrue  (Arrays.equals(emptyArray, MFTime.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (MFTime.matches(MFTime.DEFAULT_VALUE_STRING),
                                                        "MFTime.matches(MFTime.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFTime.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFTime.REGEX.contains("^") && !MFTime.REGEX.contains("$"), "test MFTime.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFFloat.REGEX.equals(MFDouble.REGEX), "test MFFloat.REGEX.equals(MFDouble.REGEX) returns true");
        assertTrue  (MFFloat.REGEX.equals(MFTime.REGEX),   "test MFFloat.REGEX.equals(MFTime.REGEX) returns true");

        testMFTime.setValue(0.0); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals( 0.0,testMFTime.get1Value(0),   "tests setting object value to 0.0 results in get1Value(index 0) of 0");
        assertTrue  (Arrays.equals(singleValueArray,  testMFTime.getPrimitiveValue()), "tests setting object value to 0.0 results in singleton array with same value");
        
        testMFTime.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFTime.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFTime.matches(),       "testMFTime.matches() tests emptyArray initialization correctly matches regex");
        testMFTime.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFTime.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        testMFTime.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFTime.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        testMFTime.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFTime.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        
        assertTrue  (MFTime.matches(""),          "MFTime.matches(\"\") tests correct empty string value");
        assertFalse (MFTime.matches(","),         "MFTime.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFTime.matches( "0"),        "MFTime.matches( \"0\")   tests correct string value");
        assertTrue  (MFTime.matches( "1"),        "MFTime.matches( \"1\")   tests correct string value");
        assertTrue  (MFTime.matches("-1"),        "MFTime.matches(\"-1\")   tests correct string value");
        assertTrue  (MFTime.matches("  3 "),      "MFTime.matches(\"  3 \") tests correct string value, including external whitespace");
        assertTrue  (MFTime.matches(" -3 "),      "MFTime.matches(\" -3 \") tests correct string value, including external whitespace");
        assertTrue  (MFTime.matches(" 0 12E45  "),"MFTime.matches(\"0  12E45\") tests correct string value, scientific notation");
        assertTrue  (MFTime.matches("+0,+12E+45"),"MFTime.matches(\"+0,+12E+45\") tests correct string value, scientific notation");
        assertTrue  (MFTime.matches("-0,-12E-45"),"MFTime.matches(\"-0,-12E-45\") tests correct string value, scientific notation");

        assertTrue  (MFTime.matches( "0.0"),        "MFTime.matches( \"0\")   tests correct string value");
        assertTrue  (MFTime.matches( "1.0"),        "MFTime.matches( \"1\")   tests correct string value");
        assertTrue  (MFTime.matches("-1.0"),        "MFTime.matches(\"-1\")   tests correct string value");
        assertTrue  (MFTime.matches("  3.0 "),      "MFTime.matches(\"  3 \") tests correct string value, including external whitespace");
        assertTrue  (MFTime.matches(" -3.0 "),      "MFTime.matches(\" -3 \") tests correct string value, including external whitespace");
        assertTrue  (MFTime.matches("0 1"),                "MFTime.matches(\"0 1\")  tests correct array as string value");
        assertTrue  (MFTime.matches("0.0 1.0"),            "MFTime.matches(\"0.0 1.0\")  tests correct array as string value");
        assertTrue  (MFTime.matches(" 0.0  12.3E45  "),    "MFTime.matches(\" 0.0  12.3E45 \") tests correct string value, scientific notation");
        assertTrue  (MFTime.matches("+0.0,+12.3E+45 "),    "MFTime.matches(\"+0.0,+12.3E+45 \") tests correct string value, scientific notation");
        assertTrue  (MFTime.matches("-0.0,-12.3E-45 "),    "MFTime.matches(\"-0.0,-12.3E-45 \") tests correct string value, scientific notation");
        assertTrue  (MFTime.matches( ".6 -.6 .6e7 -.6e-7"),"MFTime.matches(\".6 -.6 .6e7 -.6e-7\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (MFTime.matches("0 , 1 , "),           "MFTime.matches(\"0 , 1 , \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");
        
        assertFalse (MFTime.matches("true"),     "MFTime.matches(\"true\") tests incorrect boolean string value");
        assertFalse (MFTime.matches("blah"),     "MFTime.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFTime.matches("NaN"),      "MFTime.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFVec2f single-field 2-tuple single-precision floating-point array")
    void SFVec2fTests()
	{
        System.out.println ("SFVec2fTests...");
        assertTrue  (Arrays.equals(SFVec2f.DEFAULT_VALUE, new SFVec2f().setValueByString(SFVec2f.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFVec2f testSFVec2f = new SFVec2f(); // static initializer is tested, might throw exception
        assertTrue  (testSFVec2f.matches(),       "testSFVec2f.matches() tests that object initialization correctly matches regex");
//      float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f, 0.0f };
//      float[] doubleValueArray = { 0.0f, 1.0f, -2.0f, -3.0f };
//      float[] tripleValueArray = { 0.0f, 1.0f, -2.0f, -3.0f,  4.0f,  5.0f };
        assertTrue  (Arrays.equals(singleValueArray, SFVec2f.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (SFVec2f.matches(SFVec2f.DEFAULT_VALUE_STRING),
                                                        "SFVec2f.matches(SFVec2f.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFVec2f.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFVec2f.REGEX.contains("^") && !SFVec2f.REGEX.contains("$"), "test SFVec2f.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFVec2f.REGEX.equals(SFVec2d.REGEX), "test SFVec2f.REGEX.equals(SFVec2d.REGEX) returns true");

        testSFVec2f.setValue(0.0f, 0.0f); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleValueArray,  testSFVec2f.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testSFVec2f.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFVec2f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
      
        assertTrue  (SFVec2f.matches( "0 1"),      "SFVec2f.matches( \"0 1\")   tests correct string value");
        assertTrue  (SFVec2f.matches( "2 3"),      "SFVec2f.matches( \"2 3\")   tests correct string value");
        assertTrue  (SFVec2f.matches("-1 -2"),     "SFVec2f.matches(\"-1 -2\")  tests correct string value");
        assertTrue  (SFVec2f.matches(" 0  12E45 "),"SFVec2f.matches(\"0  12E45 \") tests correct string value, scientific notation");
        assertTrue  (SFVec2f.matches("+0 +12E+45"),"SFVec2f.matches(\"+0,+12E+45\") tests correct string value, scientific notation");
        assertTrue  (SFVec2f.matches("-0 -12E-45"),"SFVec2f.matches(\"-0,-12E-45\") tests correct string value, scientific notation");

        assertTrue  (SFVec2f.matches(" 0.0  1.0 "),  "SFVec2f.matches(\" 0.0  1.0 \") tests correct string value");
        assertTrue  (SFVec2f.matches("-1.0 -3.0"),   "SFVec2f.matches(\"-1.0 -3.0\") tests correct string value, including external whitespace");
        assertTrue  (SFVec2f.matches("0 1"),         "SFVec2f.matches(\"0 1\")  tests correct array as string value");
        assertTrue  (SFVec2f.matches("0.0 1.0"),     "SFVec2f.matches(\"0.0 1.0\")  tests correct array as string value");
        assertTrue  (SFVec2f.matches(" 0.0  12.3E45  "),    "SFVec2f.matches(\" 0.0  12.3E45  \") tests correct string value, scientific notation");
        assertTrue  (SFVec2f.matches("+0.0 +12.3E+45 "),    "SFVec2f.matches(\"+0.0 +12.3E+45 \") tests correct string value, scientific notation");
        assertTrue  (SFVec2f.matches("-0.0 -12.3E-45 "),    "SFVec2f.matches(\"-0.0 -12.3E-45 \") tests correct string value, scientific notation");
        
        assertFalse (SFVec2f.matches(""),          "SFVec2f.matches(\"\") tests incorrect empty string value");
        assertFalse (SFVec2f.matches(","),         "SFVec2f.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFVec2f.matches( ".6 -.6 .6e7 -.6e-7"),"SFVec2f.matches(\".6 -.6 .6e7 -.6e-7\") tests incorrect string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFVec2f.matches("true false"),"SFVec2f.matches(\"true false\") tests incorrect boolean string value");
        assertFalse (SFVec2f.matches("blah"),      "SFVec2f.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFVec2f.matches("NaN NaN"),   "SFVec2f.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFVec2f multi-field 2-tuple single-precision floating-point array")
    void MFVec2fTests()
	{
        System.out.println ("MFVec2fTests...");
        assertTrue  (Arrays.equals(MFVec2f.DEFAULT_VALUE, new MFVec2f().setValueByString(MFVec2f.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFVec2f testMFVec2f = new MFVec2f(); // static initializer is tested, might throw exception
        assertTrue  (testMFVec2f.matches(),       "testMFVec2f.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f, 0.0f };
        float[] doubleValueArray = { 0.0f, 1.0f, -2.0f, -3.0f };
        float[] tripleValueArray = { 0.0f, 1.0f, -2.0f, -3.0f,  4.0f,  5.0f };
        assertTrue  (Arrays.equals(emptyArray, MFVec2f.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFVec2f.matches(MFVec2f.DEFAULT_VALUE_STRING),
                                                        "MFVec2f.matches(MFVec2f.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFVec2f.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFVec2f.REGEX.contains("^") && !MFVec2f.REGEX.contains("$"), "test MFVec2f.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFVec2f.REGEX.equals(MFVec2d.REGEX), "test MFVec2f.REGEX.equals(MFVec2d.REGEX) returns true");

        // TODO utility method needed to set singleton object using individual values
//        testMFVec2f.setValue(0.0f, 0.0f); // returns void because it matches (overrides) Java SAI specification interface
//        assertTrue  (Arrays.equals(singleValueArray,  testMFVec2f.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testMFVec2f.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFVec2f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec2f.matches(),       "testMFVec2f.matches() tests emptyArray initialization correctly matches regex");
        testMFVec2f.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFVec2f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec2f.matches(),       "testMFVec2f.matches() tests singleValueArray correctly matches regex");
        testMFVec2f.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFVec2f.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec2f.matches(),       "testMFVec2f.matches() tests doubleValueArray correctly matches regex");
        testMFVec2f.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFVec2f.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec2f.matches(),       "testMFVec2f.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFVec2f.matches( "0 1  2 3"),      "MFVec2f.matches( \"0 1  2 3\")    tests correct string value");
        assertTrue  (MFVec2f.matches( "0 1, 2 3"),      "MFVec2f.matches( \"0 1, 2 33\")   tests correct string value");
        assertTrue  (MFVec2f.matches("-1 -2, -3 -4"),   "MFVec2f.matches(\"-1 -2, -3 -4\") tests correct string value");
        assertTrue  (MFVec2f.matches(" 0  12E45 "),"MFVec2f.matches(\"0  12E45 \") tests correct string value, scientific notation");
        assertTrue  (MFVec2f.matches("+0 +12E+45"),"MFVec2f.matches(\"+0,+12E+45\") tests correct string value, scientific notation");
        assertTrue  (MFVec2f.matches("-0 -12E-45"),"MFVec2f.matches(\"-0,-12E-45\") tests correct string value, scientific notation");

        assertTrue  (MFVec2f.matches(""),            "MFVec2f.matches(\"\") tests correct empty string value");
        assertFalse (MFVec2f.matches(","),           "MFVec2f.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFVec2f.matches(" 0.0  1.0 "),  "MFVec2f.matches(\" 0.0  1.0 \") tests correct string value");
        assertTrue  (MFVec2f.matches("-1.0 -3.0"),   "MFVec2f.matches(\"-1.0 -3.0\") tests correct string value, including external whitespace");
        assertTrue  (MFVec2f.matches("0 1"),         "MFVec2f.matches(\"0 1\")  tests correct array as string value");
        assertTrue  (MFVec2f.matches("0.0 1.0"),     "MFVec2f.matches(\"0.0 1.0\")  tests correct array as string value");
        assertTrue  (MFVec2f.matches(" 0.0  12.3E45  "),    "MFVec2f.matches(\" 0.0  12.3E45  \") tests correct string value, scientific notation");
        assertTrue  (MFVec2f.matches("+0.0 +12.3E+45 "),    "MFVec2f.matches(\"+0.0 +12.3E+45 \") tests correct string value, scientific notation");
        assertTrue  (MFVec2f.matches("-0.0 -12.3E-45 "),    "MFVec2f.matches(\"-0.0 -12.3E-45 \") tests correct string value, scientific notation");
        assertTrue  (MFVec2f.matches( ".6 -.6 .6e7 -.6e-7"),"MFVec2f.matches(\".6 -.6 .6e7 -.6e-7\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (MFVec2f.matches("0 0, 1 1, "),         "MFVec2f.matches(\"0 0, 1 1, \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");
        
        assertFalse (MFVec2f.matches("true false"),"MFVec2f.matches(\"true false\") tests incorrect boolean string value");
        assertFalse (MFVec2f.matches("blah"),      "MFVec2f.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFVec2f.matches("NaN NaN"),   "MFVec2f.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFVec2d single-field 2-tuple double-precision floating-point array")
    void SFVec2dTests()
	{
        System.out.println ("SFVec2dTests...");
        assertTrue  (Arrays.equals(SFVec2d.DEFAULT_VALUE, new SFVec2d().setValueByString(SFVec2d.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFVec2d testSFVec2d = new SFVec2d(); // static initializer is tested, might throw exception
        assertTrue  (testSFVec2d.matches(),       "testSFVec2d.matches() tests that object initialization correctly matches regex");
//      double[] emptyArray       = {};
        double[] singleValueArray = { 0.0d, 0.0f };
//      double[] doubleValueArray = { 0.0d, 1.0d, -2.0d, -3.0d };
//      double[] tripleValueArray = { 0.0d, 1.0d, -2.0d, -3.0d,  4.0d,  5.0d };
        assertTrue  (Arrays.equals(singleValueArray, SFVec2d.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (SFVec2d.matches(SFVec2d.DEFAULT_VALUE_STRING),
                                                        "SFVec2d.matches(SFVec2d.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFVec2d.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFVec2d.REGEX.contains("^") && !SFVec2d.REGEX.contains("$"), "test SFVec2d.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFVec2f.REGEX.equals(SFVec2d.REGEX), "test SFVec2f.REGEX.equals(SFVec2d.REGEX) returns true");

        testSFVec2d.setValue(0.0f, 0.0f); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleValueArray,  testSFVec2d.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testSFVec2d.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFVec2d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
      
        assertTrue  (SFVec2d.matches( "0 1"),      "SFVec2d.matches( \"0 1\")   tests correct string value");
        assertTrue  (SFVec2d.matches( "2 3"),      "SFVec2d.matches( \"2 3\")   tests correct string value");
        assertTrue  (SFVec2d.matches("-1 -2"),     "SFVec2d.matches(\"-1 -2\")  tests correct string value");
        assertTrue  (SFVec2d.matches(" 0  12E45 "),"SFVec2d.matches(\"0  12E45 \") tests correct string value, scientific notation");
        assertTrue  (SFVec2d.matches("+0 +12E+45"),"SFVec2d.matches(\"+0,+12E+45\") tests correct string value, scientific notation");
        assertTrue  (SFVec2d.matches("-0 -12E-45"),"SFVec2d.matches(\"-0,-12E-45\") tests correct string value, scientific notation");

        assertTrue  (SFVec2d.matches(" 0.0  1.0 "),  "SFVec2d.matches(\" 0.0  1.0 \") tests correct string value");
        assertTrue  (SFVec2d.matches("-1.0 -3.0"),   "SFVec2d.matches(\"-1.0 -3.0\") tests correct string value, including external whitespace");
        assertTrue  (SFVec2d.matches("0 1"),         "SFVec2d.matches(\"0 1\")  tests correct array as string value");
        assertTrue  (SFVec2d.matches("0.0 1.0"),     "SFVec2d.matches(\"0.0 1.0\")  tests correct array as string value");
        assertTrue  (SFVec2d.matches(" 0.0  12.3E45  "),    "SFVec2d.matches(\" 0.0  12.3E45  \") tests correct string value, scientific notation");
        assertTrue  (SFVec2d.matches("+0.0 +12.3E+45 "),    "SFVec2d.matches(\"+0.0 +12.3E+45 \") tests correct string value, scientific notation");
        assertTrue  (SFVec2d.matches("-0.0 -12.3E-45 "),    "SFVec2d.matches(\"-0.0 -12.3E-45 \") tests correct string value, scientific notation");
        
        assertFalse (SFVec2d.matches(""),          "SFVec2d.matches(\"\") tests incorrect empty string value");
        assertFalse (SFVec2d.matches(","),         "SFVec2d.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFVec2d.matches( ".6 -.6 .6e7 -.6e-7"),"SFVec2d.matches(\".6 -.6 .6e7 -.6e-7\") tests incorrect string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFVec2d.matches("true false"),"SFVec2d.matches(\"true false\") tests incorrect boolean string value");
        assertFalse (SFVec2d.matches("blah"),      "SFVec2d.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFVec2d.matches("NaN NaN"),   "SFVec2d.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFVec2d multi-field 2-tuple double-precision floating-point array")
    void MFVec2dTests()
	{
        System.out.println ("MFVec2dTests...");
        assertTrue  (Arrays.equals(MFVec2d.DEFAULT_VALUE, new MFVec2d().setValueByString(MFVec2d.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFVec2d testMFVec2d = new MFVec2d(); // static initializer is tested, might throw exception
        assertTrue  (testMFVec2d.matches(),       "testMFVec2d.matches() tests that object initialization correctly matches regex");
        double[] emptyArray       = {};
        double[] singleValueArray = { 0.0d, 0.0d };
        double[] doubleValueArray = { 0.0d, 1.0d, -2.0d, -3.0d };
        double[] tripleValueArray = { 0.0d, 1.0d, -2.0d, -3.0d,  4.0d,  5.0d };
        assertTrue  (Arrays.equals(emptyArray, MFVec2d.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFVec2d.matches(MFVec2d.DEFAULT_VALUE_STRING),
                                                        "MFVec2d.matches(MFVec2d.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFVec2d.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFVec2d.REGEX.contains("^") && !MFVec2d.REGEX.contains("$"), "test MFVec2d.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFVec2f.REGEX.equals(MFVec2d.REGEX), "test MFVec2f.REGEX.equals(MFVec2d.REGEX) returns true");

        // TODO utility method needed to set singleton object using individual values
//        testMFVec2d.setValue(0.0d, 0.0d); // returns void because it matches (overrides) Java SAI specification interface
//        assertTrue  (Arrays.equals(singleValueArray,  testMFVec2d.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testMFVec2d.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFVec2d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec2d.matches(),       "testMFVec2d.matches() tests emptyArray initialization correctly matches regex");
        testMFVec2d.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFVec2d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec2d.matches(),       "testMFVec2d.matches() tests singleValueArray correctly matches regex");
        testMFVec2d.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFVec2d.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec2d.matches(),       "testMFVec2d.matches() tests doubleValueArray correctly matches regex");
        testMFVec2d.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFVec2d.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec2d.matches(),       "testMFVec2d.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFVec2d.matches( "0 1  2 3"),      "MFVec2d.matches( \"0 1  2 3\")    tests correct string value");
        assertTrue  (MFVec2d.matches( "0 1, 2 3"),      "MFVec2d.matches( \"0 1, 2 33\")   tests correct string value");
        assertTrue  (MFVec2d.matches("-1 -2, -3 -4"),   "MFVec2d.matches(\"-1 -2, -3 -4\") tests correct string value");
        assertTrue  (MFVec2d.matches(" 0  12E45 "),"MFVec2d.matches(\"0  12E45 \") tests correct string value, scientific notation");
        assertTrue  (MFVec2d.matches("+0 +12E+45"),"MFVec2d.matches(\"+0,+12E+45\") tests correct string value, scientific notation");
        assertTrue  (MFVec2d.matches("-0 -12E-45"),"MFVec2d.matches(\"-0,-12E-45\") tests correct string value, scientific notation");

        assertTrue  (MFVec2d.matches(""),            "MFVec2d.matches(\"\") tests correct empty string value");
        assertFalse (MFVec2d.matches(","),           "MFVec2d.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFVec2d.matches(" 0.0  1.0 "),  "MFVec2d.matches(\" 0.0  1.0 \") tests correct string value");
        assertTrue  (MFVec2d.matches("-1.0 -3.0"),   "MFVec2d.matches(\"-1.0 -3.0\") tests correct string value, including external whitespace");
        assertTrue  (MFVec2d.matches("0 1"),         "MFVec2d.matches(\"0 1\")  tests correct array as string value");
        assertTrue  (MFVec2d.matches("0.0 1.0"),     "MFVec2d.matches(\"0.0 1.0\")  tests correct array as string value");
        assertTrue  (MFVec2d.matches(" 0.0  12.3E45  "),    "MFVec2d.matches(\" 0.0  12.3E45  \") tests correct string value, scientific notation");
        assertTrue  (MFVec2d.matches("+0.0 +12.3E+45 "),    "MFVec2d.matches(\"+0.0 +12.3E+45 \") tests correct string value, scientific notation");
        assertTrue  (MFVec2d.matches("-0.0 -12.3E-45 "),    "MFVec2d.matches(\"-0.0 -12.3E-45 \") tests correct string value, scientific notation");
        assertTrue  (MFVec2d.matches( ".6 -.6 .6e7 -.6e-7"),"MFVec2d.matches(\".6 -.6 .6e7 -.6e-7\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (MFVec2d.matches("0 0, 1 1, "),         "MFVec2d.matches(\"0 0, 1 1, \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");
        
        assertFalse (MFVec2d.matches("true false"),"MFVec2d.matches(\"true false\") tests incorrect boolean string value");
        assertFalse (MFVec2d.matches("blah"),      "MFVec2d.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFVec2d.matches("NaN NaN"),   "MFVec2d.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFVec3f single-field 3-tuple single-precision floating-point array")
    void SFVec3fTests()
	{
        System.out.println ("SFVec3fTests...");
        assertTrue  (Arrays.equals(SFVec3f.DEFAULT_VALUE, new SFVec3f().setValueByString(SFVec3f.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFVec3f testSFVec3f = new SFVec3f(); // static initializer is tested, might throw exception
        assertTrue  (testSFVec3f.matches(),       "testSFVec3f.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f, 0.0f, 0.0f };
//      float[] doubleValueArray = { 0.0f, 1.0f, -2.0f, -3.0f, -4.0f, -5.0f };
//      float[] tripleValueArray = { 0.0f, 1.0f, -2.0f, -3.0f,  4.0f,  5.0f, -6.0f,  7.0f,  8.0f };
        assertTrue  (Arrays.equals(singleValueArray, SFVec3f.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (SFVec3f.matches(SFVec3f.DEFAULT_VALUE_STRING),
                                                        "SFVec3f.matches(SFVec3f.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFVec3f.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFVec3f.REGEX.contains("^") && !SFVec3f.REGEX.contains("$"), "test SFVec3f.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFVec3f.REGEX.equals(SFVec3d.REGEX), "test SFVec3f.REGEX.equals(SFVec3d.REGEX) returns true");

        testSFVec3f.setValue(0.0f, 0.0f, 0.0f); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleValueArray,  testSFVec3f.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testSFVec3f.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFVec3f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
      
        assertTrue  (SFVec3f.matches( "0 1 2"),      "SFVec3f.matches( \"0 1 2\")   tests correct string value");
        assertTrue  (SFVec3f.matches( "2 3 4"),      "SFVec3f.matches( \"2 3 4\")   tests correct string value");
        assertTrue  (SFVec3f.matches("-1 -2 -3"),     "SFVec3f.matches(\"-1 -2 -3\")  tests correct string value");
        assertTrue  (SFVec3f.matches(" 0  12E45  0"),"SFVec3f.matches(\" 0  12E45  0\") tests correct string value, scientific notation");
        assertTrue  (SFVec3f.matches("+0 +12E+45 0"),"SFVec3f.matches(\"+0 +12E+45 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec3f.matches("-0 -12E-45 0"),"SFVec3f.matches(\"-0 -12E-45 0\") tests correct string value, scientific notation");

        assertTrue  (SFVec3f.matches(" 0.0  1.0 2.0 "),  "SFVec3f.matches(\" 0.0  1.0 2.0 \") tests correct string value");
        assertTrue  (SFVec3f.matches("-1.0 -2.0 -3.0"),   "SFVec3f.matches(\"-1.0 -2.0 -3.0\") tests correct string value, including external whitespace");
        assertTrue  (SFVec3f.matches("0 1 2"),         "SFVec3f.matches(\"0 1 2\")  tests correct array as string value");
        assertTrue  (SFVec3f.matches("0.0 1.0 2.0"),     "SFVec3f.matches(\"0.0 1.0 2.0\")  tests correct array as string value");
        assertTrue  (SFVec3f.matches(" 0.0  12.3E45  0"),    "SFVec3f.matches(\" 0.0  12.3E45  0\") tests correct string value, scientific notation");
        assertTrue  (SFVec3f.matches("+0.0 +12.3E+45 0"),    "SFVec3f.matches(\"+0.0 +12.3E+45 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec3f.matches("-0.0 -12.3E-45 0"),    "SFVec3f.matches(\"-0.0 -12.3E-45 0\") tests correct string value, scientific notation");
        
        assertFalse (SFVec3f.matches(""),                   "SFVec3f.matches(\"\") tests incorrect empty string value");
        assertFalse (SFVec3f.matches(","),                  "SFVec3f.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFVec3f.matches( ".6 -.6 .6e7 -.6e-7"),"SFVec3f.matches(\".6 -.6 .6e7 -.6e-7\") tests incorrect string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFVec3f.matches("true false false"),   "SFVec3f.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (SFVec3f.matches("blah"),               "SFVec3f.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFVec3f.matches("NaN NaN NaN"),        "SFVec3f.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFVec3f bboxSizeType checks on single-field 3-tuple single-precision floating-point array")
    void SFVec3fBboxSizeTests()
	{
        System.out.println ("SFVec3fBboxSizeTests for bounding box (bbox) constraints...");
        float[] defaultBboxSizeArray = { -1.0f, -1.0f, -1.0f };
        assertTrue  (Arrays.equals(SFVec3f.DEFAULT_VALUE_BBOXSIZETYPE, new SFVec3f().setValueByString(SFVec3f.DEFAULT_VALUE_BBOXSIZETYPE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE_BBOXSIZETYPE matches DEFAULT_VALUE_BBOXSIZETYPE_STRING for this field object");
        SFVec3f testSFVec3fBboxSize = new SFVec3f(SFVec3f.DEFAULT_VALUE_BBOXSIZETYPE); // static initializer is tested, might throw exception
        assertTrue  (testSFVec3fBboxSize.matches(),       "testSFVec3fBboxSize.matches() tests that object initialization correctly matches regex");
        assertTrue  (Arrays.equals(defaultBboxSizeArray, SFVec3f.DEFAULT_VALUE_BBOXSIZETYPE), "test correct default value for this field object");
        assertTrue  (SFVec3f.matches(SFVec3f.DEFAULT_VALUE_BBOXSIZETYPE_STRING),
                                                        "SFVec3f.matches(SFVec3f.DEFAULT_VALUE_BBOXSIZETYPE_STRING) tests object initialization correctly matches regex");
        assertFalse (testSFVec3fBboxSize.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFVec3f.REGEX_BBOXSIZETYPE.contains("^") && !SFVec3f.REGEX_BBOXSIZETYPE.contains("$"), "test SFVec3f.REGEX does not contain anchor characters ^ or $");
        // avoid unexpected equivalent regexes
        assertFalse (SFVec3f.REGEX.equals(SFVec3f.REGEX_BBOXSIZETYPE), "test SFVec3f.REGEX.equals(SFVec3f.REGEX_BBOXSIZETYPE) returns false");

        testSFVec3fBboxSize.setValue(-1.0f, -1.0f, -1.0f);
        assertTrue  (Arrays.equals(defaultBboxSizeArray,  testSFVec3fBboxSize.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f 0.0f results in singleton array with same value");
        
        testSFVec3fBboxSize.setValue(defaultBboxSizeArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(defaultBboxSizeArray,testSFVec3fBboxSize.getPrimitiveValue(),   "tests setting object value to default-value array results in equivalent getPrimitiveValue()");

        assertFalse  (SFVec3f.matches            (""), "tests empty string \"\" fails SFVec3f.matches(value), illegal value");
        assertTrue   (SFVec3f.matchesBboxSizeType(""), "tests empty string \"\" passes SFVec3f.matchesBboxSizeType(value), legal value");
        
        assertFalse  (testSFVec3fBboxSize.setValue        ( -2.0f, -2.0f, -2.0f ).matchesBboxSizeType(), "tests setting object value to -2.0f -2.0f -2.0f fails");
        assertFalse  (testSFVec3fBboxSize.setValueByString("-2.0   -2.0   -2.0" ).matchesBboxSizeType(), "tests setting object value to \"-2.0   -2.0   -2.0\" fails");
        assertFalse  (testSFVec3fBboxSize.setValue        ( -2.0f, -2.0f, -2.0f ).matchesBboxSizeType(), "tests setting object value to -2.0f -2.0f -2.0f fails");
        assertTrue   (SFVec3f.matches            ("-2.0 -2.0 -2.0"), "tests \"-2.0 -2.0 -2.0\" passes SFVec3f.matches(value)");
        assertFalse  (SFVec3f.matchesBboxSizeType("-2.0 -2.0 -2.0"), "tests \"-2.0 -2.0 -2.0\" fails  SFVec3f.matchesBboxSizeType(value)");
        assertTrue   (SFVec3f.matches            (" 2.0  2.0  2.0"), "tests \" 2.0  2.0  2.0\" passes SFVec3f.matches(value)");
        assertTrue   (SFVec3f.matchesBboxSizeType(" 2.0  2.0  2.0"), "tests \" 2.0  2.0  2.0\" passes SFVec3f.matchesBboxSizeType(value)");
        assertTrue   (SFVec3f.matchesBboxSizeType(" -1e+00 -1e00 -1e-00 "), "tests \" -1e+00 -1e00 -1e-00 \" passes SFVec3f.matchesBboxSizeType(value) for sentinel with scientific notation");
        assertTrue   (SFVec3f.matchesBboxSizeType(" 0.0  0.0  0.0"), "tests \" 0.0  0.0  0.0\" passes SFVec3f.matchesBboxSizeType(value)");
        assertFalse  (SFVec3f.matchesBboxSizeType(" 0.0  0.0  0.0  0.0"), "tests \" 0.0  0.0  0.0  0.0\" fails SFVec3f.matchesBboxSizeType(value), too many values");
        assertFalse  (SFVec3f.matchesBboxSizeType(" 0.0  0.0"),           "tests \" 0.0  0.0\" fails SFVec3f.matchesBboxSizeType(value), insufficient values");
    }

    @Test
    @DisplayName("Test MFVec3f multi-field 3-tuple single-precision floating-point array")
    void MFVec3fTests()
	{
        System.out.println ("MFVec3fTests...");
        assertTrue  (Arrays.equals(MFVec3f.DEFAULT_VALUE, new MFVec3f().setValueByString(MFVec3f.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFVec3f testMFVec3f = new MFVec3f(); // static initializer is tested, might throw exception
        assertTrue  (testMFVec3f.matches(),       "testMFVec3f.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f, 0.0f, 0.0f };
        float[] doubleValueArray = { 0.0f, 1.0f, -2.0f, -3.0f, -4.0f, -5.0f };
        float[] tripleValueArray = { 0.0f, 1.0f, -2.0f, -3.0f,  4.0f,  5.0f, 6.0f, 7.0f, 8.0f };
        assertTrue  (Arrays.equals(emptyArray, MFVec3f.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFVec3f.matches(MFVec3f.DEFAULT_VALUE_STRING),
                                                        "MFVec3f.matches(MFVec3f.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFVec3f.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFVec3f.REGEX.contains("^") && !MFVec3f.REGEX.contains("$"), "test MFVec3f.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFVec3f.REGEX.equals(MFVec3d.REGEX), "test MFVec3f.REGEX.equals(MFVec3d.REGEX) returns true");

        // TODO utility method needed to set singleton object using individual values
//        testMFVec3f.setValue(0.0f, 0.0f, 0.0f); // returns void because it matches (overrides) Java SAI specification interface
//        assertTrue  (Arrays.equals(singleValueArray,  testMFVec3f.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testMFVec3f.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFVec3f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec3f.matches(),       "testMFVec3f.matches() tests emptyArray initialization correctly matches regex");
        testMFVec3f.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFVec3f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec3f.matches(),       "testMFVec3f.matches() tests singleValueArray correctly matches regex");
        testMFVec3f.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFVec3f.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec3f.matches(),       "testMFVec3f.matches() tests doubleValueArray correctly matches regex");
        testMFVec3f.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFVec3f.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec3f.matches(),       "testMFVec3f.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFVec3f.matches(" 0  1  2   3  4  5"),   "MFVec3f.matches( \" 0  1  2   3  4  5\")   tests correct string value");
        assertTrue  (MFVec3f.matches(" 0  1  2,  3  4  5"),   "MFVec3f.matches( \" 0  1  2,  3  4  5\")   tests correct string value");
        assertTrue  (MFVec3f.matches("-0 -1 -2, -3 -4 -5"),   "MFVec3f.matches(\"-0 -1 -2, -3 -4 -5\") tests correct string value");
        assertTrue  (MFVec3f.matches(" 0  12E45  0"),"MFVec3f.matches(\"0   12E45  0\") tests correct string value, scientific notation");
        assertTrue  (MFVec3f.matches("+0 +12E+45 0"),"MFVec3f.matches(\"+0 +12E+45 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec3f.matches("-0 -12E-45 0"),"MFVec3f.matches(\"-0 -12E-45 0\") tests correct string value, scientific notation");

        assertTrue  (MFVec3f.matches(""),             "MFVec3f.matches(\"\") tests correct empty string value");
        assertFalse (MFVec3f.matches(","),            "MFVec3f.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFVec3f.matches(" 0.0  1.0 2.0"),"MFVec3f.matches(\" 0.0  1.0 2.0\") tests correct string value");
        assertTrue  (MFVec3f.matches("-1.0 -3.0 2.0"),"MFVec3f.matches(\"-1.0 -3.0 2.0\") tests correct string value, including external whitespace");
        assertTrue  (MFVec3f.matches("0 1 2"),        "MFVec3f.matches(\"0 1 2\")  tests correct array as string value");
        assertTrue  (MFVec3f.matches("0.0 1.0 2.0"),  "MFVec3f.matches(\"0.0 1.0 2.0\")  tests correct array as string value");
        assertTrue  (MFVec3f.matches(" 0.0  12.3E45  0"),       "MFVec3f.matches(\" 0.0  12.3E45  0\") tests correct string value, scientific notation");
        assertTrue  (MFVec3f.matches("+0.0 +12.3E+45 0"),       "MFVec3f.matches(\"+0.0 +12.3E+45 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec3f.matches("-0.0 -12.3E-45 0"),       "MFVec3f.matches(\"-0.0 -12.3E-45 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec3f.matches( ".6 -.6 0 .6e7 -.6e-7 0"),"MFVec3f.matches(\".6 -.6 0 .6e7 -.6e-7 0\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (MFVec3f.matches("0 0 0, 1 1 1, "),         "MFVec3f.matches(\"0 0 0, 1 1 1, \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");

        assertFalse (MFVec3f.matches("true false"),"MFVec3f.matches(\"true false\") tests incorrect boolean string value");
        assertFalse (MFVec3f.matches("blah"),      "MFVec3f.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFVec3f.matches("NaN NaN"),   "MFVec3f.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFColor single-field 3-tuple single-precision floating-point array")
    void SFColorTests()
	{
        System.out.println ("SFColorTests...");
        assertTrue  (Arrays.equals(SFColor.DEFAULT_VALUE, new SFColor().setValueByString(SFColor.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFColor testSFColor = new SFColor(); // static initializer is tested, might throw exception
        assertTrue  (testSFColor.matches(),       "testSFColor.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f, 0.0f, 0.0f };
//      float[] doubleValueArray = { 1.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f  };
//      float[] tripleValueArray = { 1.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 1.0f };
        assertTrue  (Arrays.equals(singleValueArray, SFColor.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (SFColor.matches(SFColor.DEFAULT_VALUE_STRING),
                                                        "SFColor.matches(SFColor.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFColor.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFColor.REGEX.contains("^") && !SFColor.REGEX.contains("$"), "test SFColor.REGEX does not contain anchor characters ^ or $");

        testSFColor.setValue(0.0f, 0.0f, 0.0f); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleValueArray,  testSFColor.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testSFColor.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFColor.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
      
        assertTrue  (SFColor.matches( "1 0 0"),        "SFColor.matches( \"1 0 0\")   tests correct string value");
        assertTrue  (SFColor.matches( "0.2 0.3 0.4"),  "SFColor.matches( \"0.2 0.3 0.4\")   tests correct string value");
        assertTrue  (SFColor.matches("0 0 0"),         "SFColor.matches(\"-0 0 0\")  tests correct string value");
        assertTrue  (SFColor.matches("1 1 1"),         "SFColor.matches(\"1 1 1\")  tests correct string value");
        assertTrue  (SFColor.matches(" 0  0.12E45  0"),"SFColor.matches(\" 0  0.12E45  0\") tests correct string value, scientific notation");
        assertTrue  (SFColor.matches("+0 +0.12E+45 0"),"SFColor.matches(\"+0 +0.12E+45 0\") tests correct string value, scientific notation");
        assertTrue  (SFColor.matches(" 0  0.12E-45 0"),"SFColor.matches(\" 0  0.12E-45 0\") tests correct string value, scientific notation");

        assertTrue  (SFColor.matches(" 0.0  1.0 0.0 "),  "SFColor.matches(\" 0.0  1.0 0.0 \") tests correct string value");
        
        assertFalse (SFColor.matches(""),                   "SFColor.matches(\"\") tests incorrect empty string value");
        assertFalse (SFColor.matches(","),                  "SFColor.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFColor.matches("0 1 2"),              "SFColor.matches(\"0 1 2\")  tests incorrect array as string value");
        assertFalse (SFColor.matches("0.0 1.0 2.0"),        "SFColor.matches(\"0.0 1.0 2.0\")  tests incorrect array as string value");
        assertFalse (SFColor.matches("-1.0 -2.0 -3.0"),     "SFColor.matches(\"-1.0 -2.0 -3.0\") tests incorrect string value, including external whitespace");
        assertFalse (SFColor.matches( ".6 -.6 .6e7 -.6e-7"),"SFColor.matches(\".6 -.6 .6e7 -.6e-7\") tests incorrect string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFColor.matches("true false false"),   "SFColor.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (SFColor.matches("blah"),               "SFColor.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFColor.matches("NaN NaN NaN"),        "SFColor.matches(\"NaN\") tests Not A Number (NaN) which is not an allowed string value");
    
        assertEquals(SFColor.toStringHTML(0.0f, 0.5f, 1.0f),"#007fff",           "SFColor.toStringHTML(0.0f, 0.5f, 1.0f) tests HTML export as \"#007fff\"");
        assertEquals(SFColor.toStringCSS (0.0f, 0.5f, 1.0f),"color:(0,127,255)", "SFColor.toStringCSS (0.0f, 0.5f, 1.0f) tests CSS export as \"color:(0,127,255)\"");
    }
    
    @Test
    @DisplayName("Test MFColor multi-field 3-tuple single-precision floating-point array")
    void MFColorTests()
	{
        System.out.println ("MFColorTests...");
        assertTrue  (Arrays.equals(MFColor.DEFAULT_VALUE, new MFColor().setValueByString(MFColor.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFColor testMFColor = new MFColor(); // static initializer is tested, might throw exception
        assertTrue  (testMFColor.matches(),       "testMFColor.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.8f, 0.8f, 0.8f };
        float[] doubleValueArray = { 1.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f  };
        float[] tripleValueArray = { 1.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 1.0f };
        assertTrue  (Arrays.equals(emptyArray, MFColor.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFColor.matches(MFColor.DEFAULT_VALUE_STRING),
                                                        "MFColor.matches(MFColor.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFColor.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFColor.REGEX.contains("^") && !MFColor.REGEX.contains("$"), "test MFColor.REGEX does not contain anchor characters ^ or $");

        // TODO utility method needed to set singleton object using individual values
//        testMFColor.setValue(0.0f, 0.0f, 0.0f); // returns void because it matches (overrides) Java SAI specification interface
//        assertTrue  (Arrays.equals(singleValueArray,  testMFColor.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testMFColor.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFColor.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFColor.matches(),       "testMFColor.matches() tests emptyArray initialization correctly matches regex");
        testMFColor.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFColor.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFColor.matches(),       "testMFColor.matches() tests singleValueArray correctly matches regex");
        testMFColor.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFColor.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFColor.matches(),       "testMFColor.matches() tests doubleValueArray correctly matches regex");
        testMFColor.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFColor.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFColor.matches(),       "testMFColor.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFColor.matches(" 0  1  .2  .3  .4 .5"),   "MFColor.matches( \" 0  1  .2  .3  .4 .5\")   tests correct string value");
        assertTrue  (MFColor.matches(" 0  1  .2, .3  .4 .5"),   "MFColor.matches( \" 0  1  .2, .3  .4 .5\")   tests correct string value");
        
        // TODO fix gnarly problem in regex, the following value should not match
//        assertFalse (MFColor.matches(" 0  1, .2  .3, .4 .5"),   "MFColor.matches( \" 0  1, .2  .3, .4 .5\")   tests incorrect comma placement in string value");
        
        assertTrue  (MFColor.matches(" 0  0.12E45  0"),"MFColor.matches(\"0   0.12E45  0\") tests correct string value, scientific notation");
        assertTrue  (MFColor.matches("+0 +0.12E+45 0"),"MFColor.matches(\"+0 +0.12E+45 0\") tests correct string value, scientific notation");
        assertTrue  (MFColor.matches(" 0  0.12E-45 0"),"MFColor.matches(\" 0  0.12E-45 0\") tests correct string value, scientific notation");

        assertTrue  (MFColor.matches(""),             "MFColor.matches(\"\") tests correct empty string value");
        assertFalse (MFColor.matches(","),            "MFColor.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (MFColor.matches(" 0.0  1.0 2.0"),"MFColor.matches(\" 0.0  1.0 2.0\") tests incorrect string value");
        assertFalse (MFColor.matches("-1.0 -3.0 2.0"),"MFColor.matches(\"-1.0 -3.0 2.0\") tests incorrect string value, including external whitespace");
        assertFalse (MFColor.matches("0 1 2"),        "MFColor.matches(\"0 1 2\")  tests correct array as string value");
        assertTrue  (MFColor.matches( ".6 -.6 0 .6e7 -.6e-7 0"),"MFColor.matches(\".6 -.6 0 .6e7 -.6e-7 0\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (MFColor.matches("0 0 0, 1 1 1, "),         "MFColor.matches(\"0 0 0, 1 1 1, \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");

        assertFalse (MFColor.matches("true false false"),          "MFColor.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (MFColor.matches("blah"),                      "MFColor.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFColor.matches("NaN NaN NaN NaN NaN NaN"),   "MFColor.matches(\"NaN NaN NaN NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFColorRGBA single-field 4-tuple single-precision floating-point array")
    void SFColorRGBATests()
	{
        System.out.println ("SFColorRGBATests...");
        assertTrue  (Arrays.equals(SFColorRGBA.DEFAULT_VALUE, new SFColorRGBA().setValueByString(SFColorRGBA.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFColorRGBA testSFColorRGBA = new SFColorRGBA(); // static initializer is tested, might throw exception
        assertTrue  (testSFColorRGBA.matches(),   "testSFColorRGBA.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f, 0.0f, 0.0f, 0.0f };
//      float[] doubleValueArray = { 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f  };
//      float[] tripleValueArray = { 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.5f, 0.6f };
        assertTrue  (Arrays.equals(singleValueArray, SFColorRGBA.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (SFColorRGBA.matches(SFColorRGBA.DEFAULT_VALUE_STRING),
                                                        "SFColorRGBA.matches(SFColorRGBA.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFColorRGBA.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFColorRGBA.REGEX.contains("^") && !SFColorRGBA.REGEX.contains("$"), "test SFColorRGBA.REGEX does not contain anchor characters ^ or $");

        testSFColorRGBA.setValue(0.0f, 0.0f, 0.0f, 0.0f); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleValueArray,  testSFColorRGBA.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testSFColorRGBA.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFColorRGBA.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
      
        assertTrue  (SFColorRGBA.matches( "1 0 0 0.5"),          "SFColorRGBA.matches( \"1 0 0 0.5\")   tests correct string value");
        assertTrue  (SFColorRGBA.matches( "0.2 0.3 0.4 0.5"),    "SFColorRGBA.matches( \"0.2 0.3 0.4 0.5\")   tests correct string value");
        assertTrue  (SFColorRGBA.matches("0 0 0 0.5"),           "SFColorRGBA.matches(\"-0 0 0\")  tests correct string value");
        assertTrue  (SFColorRGBA.matches("1 1 1 0.5"),           "SFColorRGBA.matches(\"1 1 1\")  tests correct string value");
        assertTrue  (SFColorRGBA.matches(" 0  0.12E45  0 0.5e0"),"SFColorRGBA.matches(\" 0  0.12E45  0 0.5e0\") tests correct string value, scientific notation");
        assertTrue  (SFColorRGBA.matches("+0 +0.12E+45 0 0.5e0"),"SFColorRGBA.matches(\"+0 +0.12E+45 0\") tests correct string value, scientific notation");
        assertTrue  (SFColorRGBA.matches(" 0  0.12E-45 0 0.5e0"),"SFColorRGBA.matches(\" 0  0.12E-45 0\") tests correct string value, scientific notation");

        assertTrue  (SFColorRGBA.matches(" 0.0  1.0 0.0 0.5"),   "SFColorRGBA.matches(\" 0.0  1.0 0.0 0.5\") tests correct string value");
        assertTrue  (SFColorRGBA.matches( ".6 -.6 .6e7 -.6e-7"), "SFColorRGBA.matches(\".6 -.6 .6e7 -.6e-7\") tests incorrect string value, no leading digit before decimal point, scientific notation");
        
        assertFalse (SFColorRGBA.matches(""),                    "SFColorRGBA.matches(\"\") tests incorrect empty string value");
        assertFalse (SFColorRGBA.matches(","),                   "SFColorRGBA.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFColorRGBA.matches("0 1 2"),               "SFColorRGBA.matches(\"0 1 2\")  tests incorrect array as string value");
        assertFalse (SFColorRGBA.matches("0.0 1.0 2.0 0.5"),     "SFColorRGBA.matches(\"0.0 1.0 2.0 0.5\")  tests incorrect array as string value");
        assertFalse (SFColorRGBA.matches("-1.0 -2.0 -3.0 0.5"),  "SFColorRGBA.matches(\"-1.0 -2.0 -3.0 0.5\") tests incorrect string value, including external whitespace");
        assertFalse (SFColorRGBA.matches("true false false false"),"SFColorRGBA.matches(\"true false false false\") tests incorrect boolean string value");
        assertFalse (SFColorRGBA.matches("blah"),                "SFColorRGBA.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFColorRGBA.matches("NaN NaN NaN NaN"),     "SFColorRGBA.matches(\"NaN NaN NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFColorRGBA multi-field 4-tuple single-precision floating-point array")
    void MFColorRGBATests()
	{
        System.out.println ("MFColorRGBATests...");
        assertTrue  (Arrays.equals(MFColorRGBA.DEFAULT_VALUE, new MFColorRGBA().setValueByString(MFColorRGBA.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFColorRGBA testMFColorRGBA = new MFColorRGBA(); // static initializer is tested, might throw exception
        assertTrue  (testMFColorRGBA.matches(),       "testMFColorRGBA.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f, 0.0f, 0.0f, 0.0f };
        float[] doubleValueArray = { 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f  };
        float[] tripleValueArray = { 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.5f, 0.6f };
        assertTrue  (Arrays.equals(emptyArray, MFColorRGBA.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFColorRGBA.matches(MFColorRGBA.DEFAULT_VALUE_STRING),
                                                        "MFColorRGBA.matches(MFColorRGBA.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFColorRGBA.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFColorRGBA.REGEX.contains("^") && !MFColorRGBA.REGEX.contains("$"), "test MFColorRGBA.REGEX does not contain anchor characters ^ or $");

        // TODO utility method needed to set singleton object using individual values
//        testMFColorRGBA.setValue(0.0f, 0.0f, 0.0f); // returns void because it matches (overrides) Java SAI specification interface
//        assertTrue  (Arrays.equals(singleValueArray,  testMFColorRGBA.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testMFColorRGBA.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFColorRGBA.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFColorRGBA.matches(),       "testMFColorRGBA.matches() tests emptyArray initialization correctly matches regex");
        testMFColorRGBA.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFColorRGBA.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFColorRGBA.matches(),       "testMFColorRGBA.matches() tests singleValueArray correctly matches regex");
        testMFColorRGBA.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFColorRGBA.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFColorRGBA.matches(),       "testMFColorRGBA.matches() tests doubleValueArray correctly matches regex");
        testMFColorRGBA.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFColorRGBA.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFColorRGBA.matches(),       "testMFColorRGBA.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFColorRGBA.matches(" 0  1  .2 0.5  .3  .4 .5 0.5"),   "MFColorRGBA.matches( \" 0  1  .2 0.5  .3  .4 .5 0.5\")   tests correct string value");
        assertTrue  (MFColorRGBA.matches(" 0  1  .2 0.5, .3  .4 .5 0.5"),   "MFColorRGBA.matches( \" 0  1  .2 0.5, .3  .4 .5 0.5\")   tests correct string value");
        
        // TODO fix gnarly problem in regex, the following value should not match
//        assertFalse (MFColorRGBA.matches(" 0  1, .2 0.5  .3, .4 .5 0.5"),   "MFColorRGBA.matches( \" 0  1, .2 0.5  .3, .4 .5 0.5\")   tests incorrect comma placement in string value");
        
        assertTrue  (MFColorRGBA.matches(" 0  0.12E45  0 0.5"),"MFColorRGBA.matches(\"0   0.12E45  0 0.5\") tests correct string value, scientific notation");
        assertTrue  (MFColorRGBA.matches("+0 +0.12E+45 0 0.5"),"MFColorRGBA.matches(\"+0 +0.12E+45 0 0.5\") tests correct string value, scientific notation");
        assertTrue  (MFColorRGBA.matches(" 0  0.12E-45 0 0.5"),"MFColorRGBA.matches(\" 0  0.12E-45 0 0.5\") tests correct string value, scientific notation");

        assertTrue  (MFColorRGBA.matches(""),                  "MFColorRGBA.matches(\"\") tests correct empty string value");
        assertTrue  (MFColorRGBA.matches("0 0 0 0, 1 1 1 1, "),"MFColorRGBA.matches(\"0 0 0 0, 1 1 1 1, \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");

        assertFalse (MFColorRGBA.matches(","),            "MFColorRGBA.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (MFColorRGBA.matches(" 0.0  1.0 2.0 0.5"),"MFColorRGBA.matches(\" 0.0  1.0 2.0 0.5\") tests incorrect string value");
        assertFalse (MFColorRGBA.matches("-1.0 -3.0 2.0 0.5"),"MFColorRGBA.matches(\"-1.0 -3.0 2.0 0.5\") tests incorrect string value, including external whitespace");
        assertFalse (MFColorRGBA.matches("0 1 2 0.5"),        "MFColorRGBA.matches(\"0 1 2 0.5\")  tests incorrect array as string value");
        assertFalse (MFColorRGBA.matches( ".6 -.6 0 .6e7 -.6e-7 0"),"MFColorRGBA.matches(\".6 -.6 0 .6e7 -.6e-7 0\") tests correct string value, no leading digit before decimal point, scientific notation");
        
        assertFalse (MFColorRGBA.matches("true false false false"),            "MFColorRGBA.matches(\"true false false false\") tests incorrect boolean string value");
        assertFalse (MFColorRGBA.matches("blah"),                              "MFColorRGBA.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFColorRGBA.matches("NaN NaN NaN NaN NaN NaN NaN NaN"),   "MFColorRGBA.matches(\"NaN NaN NaN NaN NaN NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFVec3d single-field 3-tuple double-precision floating-point array")
    void SFVec3dTests()
	{
        System.out.println ("SFVec3dTests...");
        assertTrue  (Arrays.equals(SFVec3d.DEFAULT_VALUE, new SFVec3d().setValueByString(SFVec3d.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFVec3d testSFVec3d = new SFVec3d(); // static initializer is tested, might throw exception
        assertTrue  (testSFVec3d.matches(),       "testSFVec3d.matches() tests that object initialization correctly matches regex");
        double[] emptyArray       = {};
        double[] singleValueArray = { 0.0d, 0.0d, 0.0d };
//      double[] doubleValueArray = { 0.0d, 1.0d, -2.0d, -3.0d, -4.0d,  5.0d };
//      double[] tripleValueArray = { 0.0d, 1.0d, -2.0d, -3.0d,  4.0d,  5.0d, -6.0d,  7.0d,  8.0d };
        assertTrue  (Arrays.equals(singleValueArray, SFVec3d.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (SFVec3d.matches(SFVec3d.DEFAULT_VALUE_STRING),
                                                        "SFVec3d.matches(SFVec3d.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFVec3d.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFVec3d.REGEX.contains("^") && !SFVec3d.REGEX.contains("$"), "test SFVec3d.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFVec3f.REGEX.equals(SFVec3d.REGEX), "test SFVec3f.REGEX.equals(SFVec3d.REGEX) returns true");

        testSFVec3d.setValue(0.0d, 0.0d, 0.0d); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleValueArray,  testSFVec3d.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testSFVec3d.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFVec3d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
      
        assertTrue  (SFVec3d.matches( "0 1 2"),      "SFVec3d.matches( \"0 1 2\")   tests correct string value");
        assertTrue  (SFVec3d.matches( "2 3 4"),      "SFVec3d.matches( \"2 3 4\")   tests correct string value");
        assertTrue  (SFVec3d.matches("-1 -2 -3"),    "SFVec3d.matches(\"-1 -2 -3\")  tests correct string value");
        assertTrue  (SFVec3d.matches(" 0  12E45  0"),"SFVec3d.matches(\" 0  12E45  0\") tests correct string value, scientific notation");
        assertTrue  (SFVec3d.matches("+0 +12E+45 0"),"SFVec3d.matches(\"+0 +12E+45 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec3d.matches("-0 -12E-45 0"),"SFVec3d.matches(\"-0 -12E-45 0\") tests correct string value, scientific notation");

        assertTrue  (SFVec3d.matches(" 0.0  1.0 0"), "SFVec3d.matches(\" 0.0  1.0 0\") tests correct string value");
        assertTrue  (SFVec3d.matches("-1.0 -3.0 0"), "SFVec3d.matches(\"-1.0 -3.0 0\") tests correct string value, including external whitespace");
        assertTrue  (SFVec3d.matches("0 1 2"),       "SFVec3d.matches(\"0 1 2\")  tests correct array as string value");
        assertTrue  (SFVec3d.matches("0.0 1.0 0"),   "SFVec3d.matches(\"0.0 1.0 0\")  tests correct array as string value");
        assertTrue  (SFVec3d.matches(" 0.0  12.3E45  0"),    "SFVec3d.matches(\" 0.0  12.3E45  0\") tests correct string value, scientific notation");
        assertTrue  (SFVec3d.matches("+0.0 +12.3E+45 0"),    "SFVec3d.matches(\"+0.0 +12.3E+45 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec3d.matches("-0.0 -12.3E-45 0"),    "SFVec3d.matches(\"-0.0 -12.3E-45 0\") tests correct string value, scientific notation");
        
        assertFalse (SFVec3d.matches(""),                   "SFVec3d.matches(\"\") tests incorrect empty string value");
        assertFalse (SFVec3d.matches(","),                  "SFVec3d.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFVec3d.matches( ".6 -.6 .6e7 -.6e-7"),"SFVec3d.matches(\".6 -.6 .6e7 -.6e-7\") tests incorrect string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFVec3d.matches("true false false"),   "SFVec3d.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (SFVec3d.matches("blah"),               "SFVec3d.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFVec3d.matches("NaN NaN NaN"),        "SFVec3d.matches(\"NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFVec3d multi-field 3-tuple double-precision floating-point array")
    void MFVec3dTests()
	{
        System.out.println ("MFVec3dTests...");
        assertTrue  (Arrays.equals(MFVec3d.DEFAULT_VALUE, new MFVec3d().setValueByString(MFVec3d.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFVec3d testMFVec3d = new MFVec3d(); // static initializer is tested, might throw exception
        assertTrue  (testMFVec3d.matches(),       "testMFVec3d.matches() tests that object initialization correctly matches regex");
        double[] emptyArray       = {};
        double[] singleValueArray = { 0.0d, 0.0d, 0.0d };
        double[] doubleValueArray = { 0.0d, 1.0d, -2.0d, -3.0d, -4.0d,  5.0d };
        double[] tripleValueArray = { 0.0d, 1.0d, -2.0d, -3.0d,  4.0d,  5.0d, -6.0d,  7.0d,  8.0d };
        assertTrue  (Arrays.equals(emptyArray, MFVec3d.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFVec3d.matches(MFVec3d.DEFAULT_VALUE_STRING),
                                                        "MFVec3d.matches(MFVec3d.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFVec3d.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFVec3d.REGEX.contains("^") && !MFVec3d.REGEX.contains("$"), "test MFVec3d.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFVec3f.REGEX.equals(MFVec3d.REGEX), "test MFVec3f.REGEX.equals(MFVec3d.REGEX) returns true");

        // TODO utility method needed to set singleton object using individual values
//        testMFVec3d.setValue(0.0d, 0.0d, 0.0d); // returns void because it matches (overrides) Java SAI specification interface
//        assertTrue  (Arrays.equals(singleValueArray,  testMFVec3d.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testMFVec3d.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFVec3d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec3d.matches(),       "testMFVec3d.matches() tests emptyArray initialization correctly matches regex");
        testMFVec3d.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFVec3d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec3d.matches(),       "testMFVec3d.matches() tests singleValueArray correctly matches regex");
        testMFVec3d.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFVec3d.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec3d.matches(),       "testMFVec3d.matches() tests doubleValueArray correctly matches regex");
        testMFVec3d.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFVec3d.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec3d.matches(),       "testMFVec3d.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFVec3d.matches(" 0  1  2   3  4  5"),      "MFVec3d.matches( \" 0  1  2   3  4  5\")    tests correct string value");
        assertTrue  (MFVec3d.matches(" 0  1  2,  3  4  5"),      "MFVec3d.matches( \" 0  1  2,  3  4  5\")   tests correct string value");
        assertTrue  (MFVec3d.matches("-1 -2 -3, -4 -5 -6"),   "MFVec3d.matches(\"-1 -2, -3 -4\") tests correct string value");
        assertTrue  (MFVec3d.matches(" 0  12E45  0"),"MFVec3d.matches(\" 0  12E45  0\") tests correct string value, scientific notation");
        assertTrue  (MFVec3d.matches("+0 +12E+45 0"),"MFVec3d.matches(\"+0,+12E+45 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec3d.matches("-0 -12E-45 0"),"MFVec3d.matches(\"-0,-12E-45 0\") tests correct string value, scientific notation");

        assertTrue  (MFVec3d.matches(""),             "MFVec3d.matches(\"\") tests correct empty string value");
        assertFalse (MFVec3d.matches(","),            "MFVec3d.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFVec3d.matches(" 0.0  1.0 2.0"),"MFVec3d.matches(\" 0.0  1.0 2.0\") tests correct string value");
        assertTrue  (MFVec3d.matches("-1.0 -3.0 -0"), "MFVec3d.matches(\"-1.0 -3.0 -0\") tests correct string value, including external whitespace");
        assertTrue  (MFVec3d.matches("0 1 0"),         "MFVec3d.matches(\"0 1 0\")  tests correct array as string value");
        assertTrue  (MFVec3d.matches("0.0 1.0 0"),    "MFVec3d.matches(\"0.0 1.0 0\")  tests correct array as string value");
        assertTrue  (MFVec3d.matches(" 0.0  12.3E45  0 "),      "MFVec3d.matches(\" 0.0  12.3E45  0\") tests correct string value, scientific notation");
        assertTrue  (MFVec3d.matches("+0.0 +12.3E+45 0 "),      "MFVec3d.matches(\"+0.0 +12.3E+45 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec3d.matches("-0.0 -12.3E-45 0 "),      "MFVec3d.matches(\"-0.0 -12.3E-45 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec3d.matches( ".6 -.6 0 .6e7 -.6e-7 0"),"MFVec3d.matches(\".6 -.6 0 .6e7 -.6e-7 0\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (MFVec3d.matches("0 0 0, 1 1 1, "),         "MFVec3d.matches(\"0 0 0, 1 1 1, \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");

        assertFalse (MFVec3d.matches("true false false"),"MFVec3d.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (MFVec3d.matches("blah"),            "MFVec3d.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFVec3d.matches("NaN NaN NaN"),     "MFVec3d.matches(\"NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFVec4f single-field 4-tuple single-precision floating-point array")
    void SFVec4fTests()
	{
        System.out.println ("SFVec4fTests...");
        assertTrue  (Arrays.equals(SFVec4f.DEFAULT_VALUE, new SFVec4f().setValueByString(SFVec4f.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFVec4f testSFVec4f = new SFVec4f(); // static initializer is tested, might throw exception
        assertTrue  (testSFVec4f.matches(),       "testSFVec4f.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f, 0.0f, 0.0f, 1.0f };
//      float[] doubleValueArray = { 0.0f, 1.0f, -2.0f,  3.0f, -4.0f, -5.0f, -6.0f, -7.0f };
//      float[] tripleValueArray = { 0.0f, 1.0f, -2.0f,  3.0f, -4.0f, -5.0f, -6.0f, -7.0f, 8.0f, 9.0f, 10.0f, 11.0f };
        assertTrue  (Arrays.equals(singleValueArray, SFVec4f.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (SFVec4f.matches(SFVec4f.DEFAULT_VALUE_STRING),
                                                        "SFVec4f.matches(SFVec4f.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFVec4f.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFVec4f.REGEX.contains("^") && !SFVec4f.REGEX.contains("$"), "test SFVec4f.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFVec4f.REGEX.equals(SFVec4d.REGEX),    "test SFVec4f.REGEX.equals(SFVec4d.REGEX) returns true");
        assertTrue  (SFVec4f.REGEX.equals(SFRotation.REGEX), "test SFVec4f.REGEX.equals(SFRotation.REGEX) returns true");

        testSFVec4f.setValue(0.0f, 0.0f, 0.0f, 1.0f); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleValueArray,  testSFVec4f.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testSFVec4f.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFVec4f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
      
        assertTrue  (SFVec4f.matches( "0 1 2 3"),      "SFVec4f.matches( \"0 1 2 3\")   tests correct string value");
        assertTrue  (SFVec4f.matches( "2 3 4 5"),      "SFVec4f.matches( \"2 3 4 5\")   tests correct string value");
        assertTrue  (SFVec4f.matches("-1 -2 -3 -4"),   "SFVec4f.matches(\"-1 -2 -3 -4\")  tests correct string value");
        assertTrue  (SFVec4f.matches(" 0  12E45  0 0"),"SFVec4f.matches(\" 0  12E45  0 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec4f.matches("+0 +12E+45 0 0"),"SFVec4f.matches(\"+0 +12E+45 0 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec4f.matches("-0 -12E-45 0 0"),"SFVec4f.matches(\"-0 -12E-45 0 0\") tests correct string value, scientific notation");

        assertTrue  (SFVec4f.matches(" 0.0  1.0 2.0 3.0"),   "SFVec4f.matches(\" 0.0  1.0 2.0 3.0\") tests correct string value");
        assertTrue  (SFVec4f.matches("-1.0 -2.0 -3.0 -4.0"), "SFVec4f.matches(\"-1.0 -2.0 -3.0 -4.0\") tests correct string value, including external whitespace");
        assertTrue  (SFVec4f.matches("0 1 2 3"),             "SFVec4f.matches(\"0 1 2 3\")  tests correct array as string value");
        assertTrue  (SFVec4f.matches("0.0 1.0 2.0 3.0"),     "SFVec4f.matches(\"0.0 1.0 2.0 3.0\")  tests correct array as string value");
        assertTrue  (SFVec4f.matches(" 0.0  12.3E45  0 0"),  "SFVec4f.matches(\" 0.0  12.3E45  0 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec4f.matches("+0.0 +12.3E+45 0 0"),  "SFVec4f.matches(\"+0.0 +12.3E+45 0 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec4f.matches("-0.0 -12.3E-45 0 0"),  "SFVec4f.matches(\"-0.0 -12.3E-45 0 0\") tests correct string value, scientific notation");
        
        assertFalse (SFVec4f.matches(""),                     "SFVec4f.matches(\"\") tests incorrect empty string value");
        assertFalse (SFVec4f.matches(","),                    "SFVec4f.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFVec4f.matches( ".6 -.6 .6e7 -.6e-7 0"),"SFVec4f.matches(\".6 -.6 .6e7 -.6e-7 0\") tests incorrect string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFVec4f.matches("true false false true"),"SFVec4f.matches(\"true false false true\") tests incorrect boolean string value");
        assertFalse (SFVec4f.matches("blah"),                 "SFVec4f.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFVec4f.matches("NaN NaN NaN NaN"),      "SFVec4f.matches(\"NaN NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFVec4f multi-field 4-tuple single-precision floating-point array")
    void MFVec4fTests()
	{
        System.out.println ("MFVec4fTests...");
        assertTrue  (Arrays.equals(MFVec4f.DEFAULT_VALUE, new MFVec4f().setValueByString(MFVec4f.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFVec4f testMFVec4f = new MFVec4f(); // static initializer is tested, might throw exception
        assertTrue  (testMFVec4f.matches(),       "testMFVec4f.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f, 0.0f, 0.0f, 1.0f };
        float[] doubleValueArray = { 0.0f, 1.0f, -2.0f,  3.0f, -4.0f, -5.0f, -6.0f, -7.0f };
        float[] tripleValueArray = { 0.0f, 1.0f, -2.0f,  3.0f, -4.0f, -5.0f, -6.0f, -7.0f, 8.0f, 9.0f, 10.0f, 11.0f };
        assertTrue  (Arrays.equals(emptyArray, MFVec4f.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFVec4f.matches(MFVec4f.DEFAULT_VALUE_STRING),
                                                        "MFVec4f.matches(MFVec4f.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFVec4f.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFVec4f.REGEX.contains("^") && !MFVec4f.REGEX.contains("$"), "test MFVec4f.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFVec4f.REGEX.equals(MFVec4d.REGEX),    "test MFVec4f.REGEX.equals(MFVec4d.REGEX) returns true");
        assertTrue  (MFVec4f.REGEX.equals(MFRotation.REGEX), "test MFVec4f.REGEX.equals(MFRotation.REGEX) returns true");

        // TODO utility method needed to set singleton object using individual values
//        testMFVec4f.setValue(0.0f, 0.0f, 0.0f, 1.0f); // returns void because it matches (overrides) Java SAI specification interface
//        assertTrue  (Arrays.equals(singleValueArray,  testMFVec4f.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f 0.0f 0.0f results in singleton array with same value");
        
        testMFVec4f.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFVec4f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec4f.matches(),       "testMFVec4f.matches() tests emptyArray initialization correctly matches regex");
        testMFVec4f.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFVec4f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec4f.matches(),       "testMFVec4f.matches() tests singleValueArray correctly matches regex");
        testMFVec4f.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFVec4f.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec4f.matches(),       "testMFVec4f.matches() tests doubleValueArray correctly matches regex");
        testMFVec4f.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFVec4f.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec4f.matches(),       "testMFVec4f.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFVec4f.matches(" 0  1  2  3   4  5  6  7"),   "MFVec4f.matches(\" 0  1  2  3   4  5  6  7\")   tests correct string value");
        assertTrue  (MFVec4f.matches(" 0  1  2  3,  4  5  6  7"),   "MFVec4f.matches(\" 0  1  2  3,  4  5  6  7\")   tests correct string value");
        assertTrue  (MFVec4f.matches("-0 -1 -2 -3, -4 -5 -6 -7"),   "MFVec4f.matches(\"-0 -1 -2 -3, -4 -5 -6 -7\") tests correct string value");
        assertTrue  (MFVec4f.matches(" 0  12E45  0 0"),"MFVec4f.matches(\"0   12E45  0 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec4f.matches("+0 +12E+45 0 0"),"MFVec4f.matches(\"+0 +12E+45 0 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec4f.matches("-0 -12E-45 0 0"),"MFVec4f.matches(\"-0 -12E-45 0 0\") tests correct string value, scientific notation");

        assertTrue  (MFVec4f.matches(""),               "MFVec4f.matches(\"\") tests correct empty string value");
        assertTrue  (MFVec4f.matches(" 0.0  1.0 2.0 0"),"MFVec4f.matches(\" 0.0  1.0 2.0 0\") tests correct string value");
        assertTrue  (MFVec4f.matches("-1.0 -3.0 2.0 0"),"MFVec4f.matches(\"-1.0 -3.0 2.0 0\") tests correct string value, including external whitespace");
        assertTrue  (MFVec4f.matches("0 1 2 3"),        "MFVec4f.matches(\"0 1 2 3\")  tests correct array as string value");
        assertTrue  (MFVec4f.matches("0.0 1.0 2.0 0"),  "MFVec4f.matches(\"0.0 1.0 2.0 0\")  tests correct array as string value");
        assertTrue  (MFVec4f.matches(" 0.0  12.3E45  0 0"),         "MFVec4f.matches(\" 0.0  12.3E45  0 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec4f.matches("+0.0 +12.3E+45 0 0"),         "MFVec4f.matches(\"+0.0 +12.3E+45 0 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec4f.matches("-0.0 -12.3E-45 0 0"),         "MFVec4f.matches(\"-0.0 -12.3E-45 0 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec4f.matches( ".6 -.6 0 .6e7 -.6e-7 0 0 0"),"MFVec4f.matches(\".6 -.6 0 .6e7 -.6e-7 0 0 0\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (MFVec4f.matches("0 0 0 0, 1 1 1 1, "),         "MFVec4f.matches(\"0 0 0 0, 1 1 1 1, \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");

        assertFalse (MFVec4f.matches(","),              "MFVec4f.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (MFVec4f.matches("true false false true"),"MFVec4f.matches(\"true false false true\") tests incorrect boolean string value");
        assertFalse (MFVec4f.matches("blah"),                 "MFVec4f.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFVec4f.matches("NaN NaN NaN NaN"),      "MFVec4f.matches(\"NaN NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFRotation single-field 4-tuple single-precision floating-point array")
    void SFRotationTests()
	{
        System.out.println ("SFRotationTests...");
        assertTrue  (Arrays.equals(SFRotation.DEFAULT_VALUE, new SFRotation().setValueByString(SFRotation.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFRotation testSFRotation = new SFRotation(); // static initializer is tested, might throw exception
        assertTrue  (testSFRotation.matches(),       "testSFRotation.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f, 0.0f, 1.0f, 0.0f };
//      float[] doubleValueArray = { 0.0f, 1.0f, -2.0f,  3.0f, -4.0f, -5.0f, -6.0f, -7.0f };
//      float[] tripleValueArray = { 0.0f, 1.0f, -2.0f,  3.0f, -4.0f, -5.0f, -6.0f, -7.0f, 8.0f, 9.0f, 10.0f, 11.0f };
        assertTrue  (Arrays.equals(singleValueArray, SFRotation.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (SFRotation.matches(SFRotation.DEFAULT_VALUE_STRING),
                                                        "SFRotation.matches(SFRotation.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFRotation.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFRotation.REGEX.contains("^") && !SFRotation.REGEX.contains("$"), "test SFRotation.REGEX does not contain anchor characters ^ or $");
        testSFRotation.setValue(0.0f, 0.0f, 1.0f, 0.0f); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleValueArray,  testSFRotation.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        // confirm expected equivalent regexes
        assertTrue  (SFVec4f.REGEX.equals(SFVec4d.REGEX),    "test SFVec4f.REGEX.equals(SFVec4d.REGEX) returns true");
        assertTrue  (SFVec4f.REGEX.equals(SFRotation.REGEX), "test SFVec4f.REGEX.equals(SFRotation.REGEX) returns true");
        
        testSFRotation.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFRotation.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
      
        assertTrue  (SFRotation.matches( "0 1 2 3"),      "SFRotation.matches( \"0 1 2 3\")   tests correct string value");
        assertTrue  (SFRotation.matches( "2 3 4 5"),      "SFRotation.matches( \"2 3 4 5\")   tests correct string value");
        assertTrue  (SFRotation.matches("-1 -2 -3 -4"),   "SFRotation.matches(\"-1 -2 -3 -4\")  tests correct string value");
        assertTrue  (SFRotation.matches(" 0  12E45  0 0"),"SFRotation.matches(\" 0  12E45  0 0\") tests correct string value, scientific notation");
        assertTrue  (SFRotation.matches("+0 +12E+45 0 0"),"SFRotation.matches(\"+0 +12E+45 0 0\") tests correct string value, scientific notation");
        assertTrue  (SFRotation.matches("-0 -12E-45 0 0"),"SFRotation.matches(\"-0 -12E-45 0 0\") tests correct string value, scientific notation");

        assertTrue  (SFRotation.matches(" 0.0  1.0 2.0 3.0"),   "SFRotation.matches(\" 0.0  1.0 2.0 3.0\") tests correct string value");
        assertTrue  (SFRotation.matches("-1.0 -2.0 -3.0 -4.0"), "SFRotation.matches(\"-1.0 -2.0 -3.0 -4.0\") tests correct string value, including external whitespace");
        assertTrue  (SFRotation.matches("0 1 2 3"),             "SFRotation.matches(\"0 1 2 3\")  tests correct array as string value");
        assertTrue  (SFRotation.matches("0.0 1.0 2.0 3.0"),     "SFRotation.matches(\"0.0 1.0 2.0 3.0\")  tests correct array as string value");
        assertTrue  (SFRotation.matches(" 0.0  12.3E45  0 0"),  "SFRotation.matches(\" 0.0  12.3E45  0 0\") tests correct string value, scientific notation");
        assertTrue  (SFRotation.matches("+0.0 +12.3E+45 0 0"),  "SFRotation.matches(\"+0.0 +12.3E+45 0 0\") tests correct string value, scientific notation");
        assertTrue  (SFRotation.matches("-0.0 -12.3E-45 0 0"),  "SFRotation.matches(\"-0.0 -12.3E-45 0 0\") tests correct string value, scientific notation");

        assertFalse (SFRotation.matches(""),                     "SFRotation.matches(\"\") tests incorrect empty string value");
        assertFalse (SFRotation.matches(","),                    "SFRotation.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFRotation.matches( ".6 -.6 .6e7 -.6e-7 0"),"SFRotation.matches(\".6 -.6 .6e7 -.6e-7 0\") tests incorrect string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFRotation.matches("true false false true"),"SFRotation.matches(\"true false false true\") tests incorrect boolean string value");
        assertFalse (SFRotation.matches("blah"),                 "SFRotation.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFRotation.matches("NaN NaN NaN NaN"),      "SFRotation.matches(\"NaN NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFRotation multi-field 4-tuple single-precision floating-point array")
    void MFRotationTests()
	{
        System.out.println ("MFRotationTests...");
        assertTrue  (Arrays.equals(MFRotation.DEFAULT_VALUE, new MFRotation().setValueByString(MFRotation.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFRotation testMFRotation = new MFRotation(); // static initializer is tested, might throw exception
        assertTrue  (testMFRotation.matches(),       "testMFRotation.matches() tests that object initialization correctly matches regex");
        float[] emptyArray       = {};
        float[] singleValueArray = { 0.0f, 0.0f, 1.0f, 0.0f };
        float[] doubleValueArray = { 0.0f, 1.0f, -2.0f,  3.0f, -4.0f, -5.0f, -6.0f, -7.0f };
        float[] tripleValueArray = { 0.0f, 1.0f, -2.0f,  3.0f, -4.0f, -5.0f, -6.0f, -7.0f, 8.0f, 9.0f, 10.0f, 11.0f };
        assertTrue  (Arrays.equals(emptyArray, MFRotation.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFRotation.matches(MFRotation.DEFAULT_VALUE_STRING),
                                                        "MFRotation.matches(MFRotation.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFRotation.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFRotation.REGEX.contains("^") && !MFRotation.REGEX.contains("$"), "test MFRotation.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFVec4f.REGEX.equals(MFVec4d.REGEX),    "test MFVec4f.REGEX.equals(MFVec4d.REGEX) returns true");
        assertTrue  (MFVec4f.REGEX.equals(MFRotation.REGEX), "test MFVec4f.REGEX.equals(MFRotation.REGEX) returns true");

        // TODO utility method needed to set singleton object using individual values
//      // setValue(0 0 0 0) throws exception as expected due to zero-length axis
//        testMFRotation.setValue(0.0f, 0.0f, 0.0f, 0.0f); // returns void because it matches (overrides) Java SAI specification interface
//        assertTrue  (Arrays.equals(singleValueArray,  testMFRotation.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f 0.0f 0.0f results in singleton array with same value");
        
        testMFRotation.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFRotation.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFRotation.matches(),       "testMFRotation.matches() tests emptyArray initialization correctly matches regex");
        testMFRotation.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFRotation.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFRotation.matches(),       "testMFRotation.matches() tests singleValueArray correctly matches regex");
        testMFRotation.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFRotation.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFRotation.matches(),       "testMFRotation.matches() tests doubleValueArray correctly matches regex");
        testMFRotation.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFRotation.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFRotation.matches(),       "testMFRotation.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFRotation.matches(" 0  1  2  3   4  5  6  7"),   "MFRotation.matches(\" 0  1  2  3   4  5  6  7\")   tests correct string value");
        assertTrue  (MFRotation.matches(" 0  1  2  3,  4  5  6  7"),   "MFRotation.matches(\" 0  1  2  3,  4  5  6  7\")   tests correct string value");
        assertTrue  (MFRotation.matches("-0 -1 -2 -3, -4 -5 -6 -7"),   "MFRotation.matches(\"-0 -1 -2 -3, -4 -5 -6 -7\") tests correct string value");
        assertTrue  (MFRotation.matches(" 0  12E45  0 0"),"MFRotation.matches(\"0   12E45  0 0\") tests correct string value, scientific notation");
        assertTrue  (MFRotation.matches("+0 +12E+45 0 0"),"MFRotation.matches(\"+0 +12E+45 0 0\") tests correct string value, scientific notation");
        assertTrue  (MFRotation.matches("-0 -12E-45 0 0"),"MFRotation.matches(\"-0 -12E-45 0 0\") tests correct string value, scientific notation");

        assertTrue  (MFRotation.matches(""),               "MFRotation.matches(\"\") tests correct empty string value");
        assertTrue  (MFRotation.matches(" 0.0  1.0 2.0 0"),"MFRotation.matches(\" 0.0  1.0 2.0 0\") tests correct string value");
        assertTrue  (MFRotation.matches("-1.0 -3.0 2.0 0"),"MFRotation.matches(\"-1.0 -3.0 2.0 0\") tests correct string value, including external whitespace");
        assertTrue  (MFRotation.matches("0 1 2 3"),        "MFRotation.matches(\"0 1 2 3\")  tests correct array as string value");
        assertTrue  (MFRotation.matches("0.0 1.0 2.0 0"),  "MFRotation.matches(\"0.0 1.0 2.0 0\")  tests correct array as string value");
        assertTrue  (MFRotation.matches(" 0.0  12.3E45  0 0"),         "MFRotation.matches(\" 0.0  12.3E45  0 0\") tests correct string value, scientific notation");
        assertTrue  (MFRotation.matches("+0.0 +12.3E+45 0 0"),         "MFRotation.matches(\"+0.0 +12.3E+45 0 0\") tests correct string value, scientific notation");
        assertTrue  (MFRotation.matches("-0.0 -12.3E-45 0 0"),         "MFRotation.matches(\"-0.0 -12.3E-45 0 0\") tests correct string value, scientific notation");
        assertTrue  (MFRotation.matches( ".6 -.6 0 .6e7 -.6e-7 0 0 0"),"MFRotation.matches(\".6 -.6 0 .6e7 -.6e-7 0 0 0\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (MFRotation.matches("0 0 0 0, 1 1 1 1, "),         "MFRotation.matches(\"0 0 0 0, 1 1 1 1, \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");

        assertFalse (MFRotation.matches(","),              "MFRotation.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (MFRotation.matches("true false false true"),"MFRotation.matches(\"true false false true\") tests incorrect boolean string value");
        assertFalse (MFRotation.matches("blah"),                 "MFRotation.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFRotation.matches("NaN NaN NaN NaN"),      "MFRotation.matches(\"NaN NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFVec4d single-field 4-tuple double-precision floating-point array")
    void SFVec4dTests()
	{
        System.out.println ("SFVec4dTests...");
        assertTrue  (Arrays.equals(SFVec4d.DEFAULT_VALUE, new SFVec4d().setValueByString(SFVec4d.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFVec4d testSFVec4d = new SFVec4d(); // static initializer is tested, might throw exception
        assertTrue  (testSFVec4d.matches(),       "testSFVec4d.matches() tests that object initialization correctly matches regex");
        double[] emptyArray       = {};
        double[] singleValueArray = { 0.0d, 0.0d, 0.0d, 1.0d };
//      double[] doubleValueArray = { 0.0d, 1.0d, -2.0d,  3.0d, -4.0d, -5.0d, -6.0d, -7.0d };
//      double[] tripleValueArray = { 0.0d, 1.0d, -2.0d,  3.0d, -4.0d, -5.0d, -6.0d, -7.0d, 8.0d, 9.0d, 10.0d, 11.0d };
        assertTrue  (Arrays.equals(singleValueArray, SFVec4d.DEFAULT_VALUE), "test correct default value for this field object");
        assertTrue  (SFVec4d.matches(SFVec4d.DEFAULT_VALUE_STRING),
                                                        "SFVec4d.matches(SFVec4d.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFVec4d.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFVec4d.REGEX.contains("^") && !SFVec4d.REGEX.contains("$"), "test SFVec4d.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFVec4f.REGEX.equals(SFVec4d.REGEX), "test SFVec4f.REGEX.equals(SFVec4d.REGEX) returns true");

        testSFVec4d.setValue(0.0d, 0.0d, 0.0d, 1.0d); // returns void because it matches (overrides) Java SAI specification interface
        assertTrue  (Arrays.equals(singleValueArray,  testSFVec4d.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testSFVec4d.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFVec4d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
      
        assertTrue  (SFVec4d.matches( "0 1 2 3"),      "SFVec4d.matches( \"0 1 2 3\")   tests correct string value");
        assertTrue  (SFVec4d.matches( "2 3 4 5"),      "SFVec4d.matches( \"2 3 4 5\")   tests correct string value");
        assertTrue  (SFVec4d.matches("-1 -2 -3 -4"),    "SFVec4d.matches(\"-1 -2 -3 -4\")  tests correct string value");
        assertTrue  (SFVec4d.matches(" 0  12E45  0 0"),"SFVec4d.matches(\" 0  12E45  0 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec4d.matches("+0 +12E+45 0 0"),"SFVec4d.matches(\"+0 +12E+45 0 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec4d.matches("-0 -12E-45 0 0"),"SFVec4d.matches(\"-0 -12E-45 0 0\") tests correct string value, scientific notation");

        assertTrue  (SFVec4d.matches(" 0.0  1.0 0 0"), "SFVec4d.matches(\" 0.0  1.0 0 0\") tests correct string value");
        assertTrue  (SFVec4d.matches("-1.0 -3.0 0 0"), "SFVec4d.matches(\"-1.0 -3.0 0 0\") tests correct string value, including external whitespace");
        assertTrue  (SFVec4d.matches("0 1 2 3"),       "SFVec4d.matches(\"0 1 2 3\")  tests correct array as string value");
        assertTrue  (SFVec4d.matches("0.0 1.0 0 0"),   "SFVec4d.matches(\"0.0 1.0 0 0\")  tests correct array as string value");
        assertTrue  (SFVec4d.matches(" 0.0  12.3E45  0 0"),    "SFVec4d.matches(\" 0.0  12.3E45  0 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec4d.matches("+0.0 +12.3E+45 0 0"),    "SFVec4d.matches(\"+0.0 +12.3E+45 0 0\") tests correct string value, scientific notation");
        assertTrue  (SFVec4d.matches("-0.0 -12.3E-45 0 0"),    "SFVec4d.matches(\"-0.0 -12.3E-45 0 0\") tests correct string value, scientific notation");
        
        assertFalse (SFVec4d.matches(""),                   "SFVec4d.matches(\"\") tests incorrect empty string value");
        assertFalse (SFVec4d.matches(","),                  "SFVec4d.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertFalse (SFVec4d.matches( ".6 -.6 .6e7 -.6e-7 0"),"SFVec4d.matches(\".6 -.6 .6e7 -.6e-7 0\") tests incorrect string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFVec4d.matches("true false false true"),   "SFVec4d.matches(\"true false false true\") tests incorrect boolean string value");
        assertFalse (SFVec4d.matches("blah"),                    "SFVec4d.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFVec4d.matches("NaN NaN NaN NaN"),         "SFVec4d.matches(\"NaN NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFVec4d multi-field 4-tuple double-precision floating-point array")
    void MFVec4dTests()
	{
        System.out.println ("MFVec4dTests...");
        assertTrue  (Arrays.equals(MFVec4d.DEFAULT_VALUE, new MFVec4d().setValueByString(MFVec4d.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFVec4d testMFVec4d = new MFVec4d(); // static initializer is tested, might throw exception
        assertTrue  (testMFVec4d.matches(),       "testMFVec4d.matches() tests that object initialization correctly matches regex");
        double[] emptyArray       = {};
        double[] singleValueArray = { 0.0d, 0.0d, 0.0d, 1.0d };
        double[] doubleValueArray = { 0.0d, 1.0d, -2.0d,  3.0d, -4.0d, -5.0d, -6.0d, -7.0d };
        double[] tripleValueArray = { 0.0d, 1.0d, -2.0d,  3.0d, -4.0d, -5.0d, -6.0d, -7.0d, 8.0d, 9.0d, 10.0d, 11.0d };
        assertTrue  (Arrays.equals(emptyArray, MFVec4d.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFVec4d.matches(MFVec4d.DEFAULT_VALUE_STRING),
                                                        "MFVec4d.matches(MFVec4d.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFVec4d.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFVec4d.REGEX.contains("^") && !MFVec4d.REGEX.contains("$"), "test MFVec4d.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFVec4f.REGEX.equals(MFVec4d.REGEX), "test MFVec4f.REGEX.equals(MFVec4d.REGEX) returns true");

        // TODO utility method needed to set singleton object using individual values
//        testMFVec4d.setValue(0.0d, 0.0d, 0.0d, 0.0d); // returns void because it matches (overrides) Java SAI specification interface
//        assertTrue  (Arrays.equals(singleValueArray,  testMFVec4d.getPrimitiveValue()), "tests setting object value to 0.0f 0.0f results in singleton array with same value");
        
        testMFVec4d.setValue(emptyArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(emptyArray,testMFVec4d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec4d.matches(),       "testMFVec4d.matches() tests emptyArray initialization correctly matches regex");
        testMFVec4d.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFVec4d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec4d.matches(),       "testMFVec4d.matches() tests singleValueArray correctly matches regex");
        testMFVec4d.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFVec4d.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec4d.matches(),       "testMFVec4d.matches() tests doubleValueArray correctly matches regex");
        testMFVec4d.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFVec4d.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFVec4d.matches(),       "testMFVec4d.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFVec4d.matches(" 0  1  2  3   4  5  7  8"),      "MFVec4d.matches( \" 0  1  2  3   4  5  7  8\")    tests correct string value");
        assertTrue  (MFVec4d.matches(" 0  1  2  3,  4  5  7  8"),      "MFVec4d.matches( \" 0  1  2  3,  4  5  7  8\")   tests correct string value");
        assertTrue  (MFVec4d.matches("-1 -2 -3 -4, -5 -6 -7 -8"),   "MFVec4d.matches(\"-1 -2 -3 -4, -5 -6 -7 -8\") tests correct string value");
        assertTrue  (MFVec4d.matches(" 0  12E45  0 0"),"MFVec4d.matches(\" 0  12E45  0 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec4d.matches("+0 +12E+45 0 0"),"MFVec4d.matches(\"+0,+12E+45 0 0\") tests correct string value, scientific notation");
        assertTrue  (MFVec4d.matches("-0 -12E-45 0 0"),"MFVec4d.matches(\"-0,-12E-45 0 0\") tests correct string value, scientific notation");

        assertTrue  (MFVec4d.matches(""),                "MFVec4d.matches(\"\") tests correct empty string value");
        assertFalse (MFVec4d.matches(","),               "MFVec4d.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFVec4d.matches(" 0.0  1.0 2.0 0"), "MFVec4d.matches(\" 0.0  1.0 2.0 0\") tests correct string value");
        assertTrue  (MFVec4d.matches("-1.0 -3.0 -0  0"), "MFVec4d.matches(\"-1.0 -3.0 -0  0\") tests correct string value, including external whitespace");
        assertTrue  (MFVec4d.matches("0 1 0 0"),         "MFVec4d.matches(\"0 1 0 0\")  tests correct array as string value");
        assertTrue  (MFVec4d.matches("0.0 1.0 0 0"),     "MFVec4d.matches(\"0.0 1.0 0 0\")  tests correct array as string value");
        assertTrue  (MFVec4d.matches(" 0.0  12.3E45  0 0 "),        "MFVec4d.matches(\" 0.0  12.3E45  0 0 \") tests correct string value, scientific notation");
        assertTrue  (MFVec4d.matches("+0.0 +12.3E+45 0 0 "),        "MFVec4d.matches(\"+0.0 +12.3E+45 0 0 \") tests correct string value, scientific notation");
        assertTrue  (MFVec4d.matches("-0.0 -12.3E-45 0 0 "),        "MFVec4d.matches(\"-0.0 -12.3E-45 0 0 \") tests correct string value, scientific notation");
        assertTrue  (MFVec4d.matches( ".6 -.6 0 .6e7 -.6e-7 0 0 0"),"MFVec4d.matches(\".6 -.6 0 .6e7 -.6e-7 0 0 0\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertTrue  (MFVec4d.matches("0 0 0 0, 1 1 1 1, "),         "MFVec4d.matches(\"0 0 0 0, 1 1 1 1, \")  tests correct array as string value, including whitespace and commas, with allowed trailing comma");

        assertFalse (MFVec4d.matches("true false false true"),"MFVec4d.matches(\"true false false true\") tests incorrect boolean string value");
        assertFalse (MFVec4d.matches("blah"),                 "MFVec4d.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFVec4d.matches("NaN NaN NaN"),          "MFVec4d.matches(\"NaN NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFMatrix3f single-field 9-tuple single-precision floating-point array")
    void SFMatrix3fTests()
	{
        System.out.println ("SFMatrix3fTests...");
        assertTrue  (Arrays.equals(SFMatrix3f.DEFAULT_VALUE, new SFMatrix3f().setValueByString(SFMatrix3f.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFMatrix3f testSFMatrix3f = new SFMatrix3f(); // static initializer is tested, might throw exception
        assertTrue  (testSFMatrix3f.matches(),       "testSFMatrix3f.matches() tests that object initialization correctly matches regex");
        float []       emptyArray = {};
        float []    identityArray = { 1.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 1.0f };
        float [] singleValueArray = { 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
//      float[] doubleValueArray = { 1.0f, -2.0f, -3.0f, -4.0f,  5.0f, -6.0f,  7.0f,  8.0f, 9.0f, 11.0f, -12.0f, -13.0f, -14.0f,  15.0f, -16.0f,  17.0f,  18.0f, 19.0f  };
//      float[] tripleValueArray = { 1.0f, -2.0f, -3.0f,  4.0f,  5.0f, -6.0f,  7.0f,  8.0f, 9.0f, 11.0f, -12.0f, -13.0f, -14.0f,  15.0f, -16.0f,  17.0f,  18.0f, 19.0f, 21.0f, -22.0f, -23.0f, -24.0f,  25.0f, -26.0f,  27.0f,  28.0f, 29.0f };
        assertTrue  (Arrays.equals(identityArray, SFMatrix3f.DEFAULT_VALUE), "test correct default value is identity array for this MF field object");
        assertTrue  (SFMatrix3f.matches(SFMatrix3f.DEFAULT_VALUE_STRING),
                                                        "SFMatrix3f.matches(SFMatrix3f.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFMatrix3f.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFMatrix3f.REGEX.contains("^") && !SFMatrix3f.REGEX.contains("$"), "test SFMatrix3f.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFMatrix3f.REGEX.equals(SFMatrix3d.REGEX), "test SFMatrix3f.REGEX.equals(SFMatrix3d.REGEX) returns true");

        testSFMatrix3f = new SFMatrix3f();
        assertTrue  (Arrays.equals(identityArray,testSFMatrix3f.getPrimitiveValue()),   "tests setting object value to emptyArray results in identityArray for equivalent getPrimitiveValue()");
        assertTrue  (testSFMatrix3f.matches(),       "testSFMatrix3f.matches() tests emptyArray initialization correctly matches regex");
        testSFMatrix3f.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFMatrix3f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testSFMatrix3f.matches(),       "testSFMatrix3f.matches() tests singleValueArray correctly matches regex");
//        testSFMatrix3f.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
//        assertEquals(doubleValueArray,testSFMatrix3f.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
//        assertTrue  (testSFMatrix3f.matches(),       "testSFMatrix3f.matches() tests doubleValueArray correctly matches regex");
//        testSFMatrix3f.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
//        assertEquals(tripleValueArray,testSFMatrix3f.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
//        assertTrue  (testSFMatrix3f.matches(),       "testSFMatrix3f.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (SFMatrix3f.matches(" 0  1  2   3  4  5  6 7 8 "),   "SFMatrix3f.matches( \" 0  1  2   3  4  5  6 7 8 \") tests correct string value");
        assertFalse (SFMatrix3f.matches(" 0  1  2,  3  4  5, 6 7 8 "),   "SFMatrix3f.matches( \" 0  1  2,  3  4  5, 6 7 8 \") tests incorrect string value, no commas allowed");
        assertTrue  (SFMatrix3f.matches("-1 -2 -3  -4 -5 -6  7 8 9 "),   "SFMatrix3f.matches( \"-1 -2 -3  -4 -5 -6  7 8 9 \") tests correct string value");
        assertTrue  (SFMatrix3f.matches(" 0  12E45  0 4 5 6 7 8 9 "),"SFMatrix3f.matches(\" 0  12E45  0 4 5 6 7 8 9 \") tests correct string value, scientific notation");
        assertTrue  (SFMatrix3f.matches("+0 +12E+45 0 4 5 6 7 8 9 "),"SFMatrix3f.matches(\"+0,+12E+45 0 4 5 6 7 8 9 \") tests correct string value, scientific notation");
        assertTrue  (SFMatrix3f.matches("-0 -12E-45 0 4 5 6 7 8 9 "),"SFMatrix3f.matches(\"-0,-12E-45 0 4 5 6 7 8 9 \") tests correct string value, scientific notation");

        assertFalse (SFMatrix3f.matches(""),             "SFMatrix3f.matches(\"\") tests incorrect empty string value");
        assertFalse (SFMatrix3f.matches(","),            "SFMatrix3f.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (SFMatrix3f.matches(" 0.0  1.0 2.0 3 4 5 6 7 8"), "SFMatrix3f.matches(\" 0.0  1.0 2.0 3 4 5 6 7 8\") tests correct string value");
        assertTrue  (SFMatrix3f.matches("-1.0 -3.0 -0  3 4 5 6 7 8"), "SFMatrix3f.matches(\"-1.0 -3.0 -0  3 4 5 6 7 8\") tests correct string value, including external whitespace");
        assertTrue  (SFMatrix3f.matches("0 1 0  3 4 5 6 7 8"),        "SFMatrix3f.matches(\"0 1 0  3 4 5 6 7 8\")  tests correct array as string value");
        assertTrue  (SFMatrix3f.matches("0.0 1.0 0  3 4 5 6 7 8"),    "SFMatrix3f.matches(\"0.0 1.0 0  3 4 5 6 7 8\")  tests correct array as string value");
        assertTrue  (SFMatrix3f.matches(" 0.0  12.3E45  0  3 4 5 6 7 8 "),"SFMatrix3f.matches(\" 0.0  12.3E45  0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix3f.matches("+0.0 +12.3E+45 0  3 4 5 6 7 8 "),"SFMatrix3f.matches(\"+0.0 +12.3E+45 0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix3f.matches("-0.0 -12.3E-45 0  3 4 5 6 7 8 "),"SFMatrix3f.matches(\"-0.0 -12.3E-45 0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix3f.matches( ".6 -.6 0 .6e7 -.6e-7 0 6 7 8 "),"SFMatrix3f.matches(\".6 -.6 0 .6e7 -.6e-7 0 6 7 8 \") tests correct string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFMatrix3f.matches("0 0 0, 1 1 1, 2 2 2, "),         "SFMatrix3f.matches(\"0 0 0, 1 1 1, 2 2 2, \")  tests incorrect array as string value, including whitespace and commas, with trailing comma");

        assertFalse (SFMatrix3f.matches("true false false"),"SFMatrix3f.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (SFMatrix3f.matches("blah"),            "SFMatrix3f.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFMatrix3f.matches("NaN NaN NaN"),     "SFMatrix3f.matches(\"NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFMatrix3d single-field 9-tuple double-precision floating-point array")
    void SFMatrix3dTests()
	{
        System.out.println ("SFMatrix3dTests...");
        assertTrue  (Arrays.equals(SFMatrix3d.DEFAULT_VALUE, new SFMatrix3d().setValueByString(SFMatrix3d.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFMatrix3d testSFMatrix3d = new SFMatrix3d(); // static initializer is tested, might throw exception
        assertTrue  (testSFMatrix3d.matches(),       "testSFMatrix3d.matches() tests that object initialization correctly matches regex");
        double []       emptyArray = {};
        double []    identityArray = { 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0 };
        double [] singleValueArray = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
//      double [] doubleValueArray = { 1.0, -2.0, -3.0d, -4.0d,  5.0d, -6.0d,  7.0d,  8.0d, 9.0d, 11.0d, -12.0d, -13.0d, -14.0d,  15.0d, -16.0d,  17.0d,  18.0d, 19.0d  };
//      double [] tripleValueArray = { 1.0, -2.0, -3.0d,  4.0d,  5.0d, -6.0d,  7.0d,  8.0d, 9.0d, 11.0d, -12.0d, -13.0d, -14.0d,  15.0d, -16.0d,  17.0d,  18.0d, 19.0d, 21.0d, -22.0d, -23.0d, -24.0d,  25.0d, -26.0d,  27.0d,  28.0d, 29.0d };
        assertTrue  (Arrays.equals(identityArray, SFMatrix3d.DEFAULT_VALUE), "test correct default value is identity array for this MF field object");
        assertTrue  (SFMatrix3d.matches(SFMatrix3d.DEFAULT_VALUE_STRING),
                                                        "SFMatrix3d.matches(SFMatrix3d.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFMatrix3d.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFMatrix3d.REGEX.contains("^") && !SFMatrix3d.REGEX.contains("$"), "test SFMatrix3d.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFMatrix3f.REGEX.equals(SFMatrix3d.REGEX), "test SFMatrix3f.REGEX.equals(SFMatrix3d.REGEX) returns true");

        testSFMatrix3d = new SFMatrix3d();
        assertTrue  (Arrays.equals(identityArray,testSFMatrix3d.getPrimitiveValue()),   "tests setting object value to emptyArray results in identityArray for equivalent getPrimitiveValue()");
        assertTrue  (testSFMatrix3d.matches(),       "testSFMatrix3d.matches() tests emptyArray initialization correctly matches regex");
        testSFMatrix3d.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFMatrix3d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testSFMatrix3d.matches(),       "testSFMatrix3d.matches() tests singleValueArray correctly matches regex");
//        testSFMatrix3d.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
//        assertEquals(doubleValueArray,testSFMatrix3d.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
//        assertTrue  (testSFMatrix3d.matches(),       "testSFMatrix3d.matches() tests doubleValueArray correctly matches regex");
//        testSFMatrix3d.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
//        assertEquals(tripleValueArray,testSFMatrix3d.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
//        assertTrue  (testSFMatrix3d.matches(),       "testSFMatrix3d.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (SFMatrix3d.matches(" 0  1  2   3  4  5  6 7 8 "),   "SFMatrix3d.matches( \" 0  1  2   3  4  5  6 7 8 \") tests correct string value");
        assertFalse (SFMatrix3d.matches(" 0  1  2,  3  4  5, 6 7 8 "),   "SFMatrix3d.matches( \" 0  1  2,  3  4  5, 6 7 8 \") tests incorrect string value, no commas allowed");
        assertTrue  (SFMatrix3d.matches("-1 -2 -3  -4 -5 -6  7 8 9 "),   "SFMatrix3d.matches( \"-1 -2 -3  -4 -5 -6  7 8 9 \") tests correct string value");
        assertTrue  (SFMatrix3d.matches(" 0  12E45  0 4 5 6 7 8 9 "),"SFMatrix3d.matches(\" 0  12E45  0 4 5 6 7 8 9 \") tests correct string value, scientific notation");
        assertTrue  (SFMatrix3d.matches("+0 +12E+45 0 4 5 6 7 8 9 "),"SFMatrix3d.matches(\"+0,+12E+45 0 4 5 6 7 8 9 \") tests correct string value, scientific notation");
        assertTrue  (SFMatrix3d.matches("-0 -12E-45 0 4 5 6 7 8 9 "),"SFMatrix3d.matches(\"-0,-12E-45 0 4 5 6 7 8 9 \") tests correct string value, scientific notation");

        assertFalse (SFMatrix3d.matches(""),             "SFMatrix3d.matches(\"\") tests incorrect empty string value");
        assertFalse (SFMatrix3d.matches(","),            "SFMatrix3d.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (SFMatrix3d.matches(" 0.0  1.0 2.0 3 4 5 6 7 8"), "SFMatrix3d.matches(\" 0.0  1.0 2.0 3 4 5 6 7 8\") tests correct string value");
        assertTrue  (SFMatrix3d.matches("-1.0 -3.0 -0  3 4 5 6 7 8"), "SFMatrix3d.matches(\"-1.0 -3.0 -0  3 4 5 6 7 8\") tests correct string value, including external whitespace");
        assertTrue  (SFMatrix3d.matches("0 1 0  3 4 5 6 7 8"),        "SFMatrix3d.matches(\"0 1 0  3 4 5 6 7 8\")  tests correct array as string value");
        assertTrue  (SFMatrix3d.matches("0.0 1.0 0  3 4 5 6 7 8"),    "SFMatrix3d.matches(\"0.0 1.0 0  3 4 5 6 7 8\")  tests correct array as string value");
        assertTrue  (SFMatrix3d.matches(" 0.0  12.3E45  0  3 4 5 6 7 8 "),"SFMatrix3d.matches(\" 0.0  12.3E45  0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix3d.matches("+0.0 +12.3E+45 0  3 4 5 6 7 8 "),"SFMatrix3d.matches(\"+0.0 +12.3E+45 0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix3d.matches("-0.0 -12.3E-45 0  3 4 5 6 7 8 "),"SFMatrix3d.matches(\"-0.0 -12.3E-45 0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix3d.matches( ".6 -.6 0 .6e7 -.6e-7 0 6 7 8 "),"SFMatrix3d.matches(\".6 -.6 0 .6e7 -.6e-7 0 6 7 8 \") tests correct string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFMatrix3d.matches("0 0 0, 1 1 1, 2 2 2, "),         "SFMatrix3d.matches(\"0 0 0, 1 1 1, 2 2 2, \")  tests incorrect array as string value, including whitespace and commas, with trailing comma");

        assertFalse (SFMatrix3d.matches("true false false"),"SFMatrix3d.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (SFMatrix3d.matches("blah"),            "SFMatrix3d.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFMatrix3d.matches("NaN NaN NaN"),     "SFMatrix3d.matches(\"NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFMatrix3f multiple-field 9-tuple single-precision floating-point array")
    void MFMatrix3fTests()
	{
        System.out.println ("MFMatrix3fTests...");
        assertTrue  (Arrays.equals(MFMatrix3f.DEFAULT_VALUE, new MFMatrix3f().setValueByString(MFMatrix3f.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFMatrix3f testMFMatrix3f = new MFMatrix3f(); // static initializer is tested, might throw exception
        assertTrue  (testMFMatrix3f.matches(),       "testMFMatrix3f.matches() tests that object initialization correctly matches regex");
        float []       emptyArray = {};
//      float []    identityArray = { 1.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 1.0f };
        float [] singleValueArray = { 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        float [] doubleValueArray = { 1.0f, -2.0f, -3.0f, -4.0f,  5.0f, -6.0f,  7.0f,  8.0f, 9.0f, 11.0f, -12.0f, -13.0f, -14.0f,  15.0f, -16.0f,  17.0f,  18.0f, 19.0f  };
        float [] tripleValueArray = { 1.0f, -2.0f, -3.0f,  4.0f,  5.0f, -6.0f,  7.0f,  8.0f, 9.0f, 11.0f, -12.0f, -13.0f, -14.0f,  15.0f, -16.0f,  17.0f,  18.0f, 19.0f, 21.0f, -22.0f, -23.0f, -24.0f,  25.0f, -26.0f,  27.0f,  28.0f, 29.0f };
        assertTrue  (Arrays.equals(emptyArray, MFMatrix3f.DEFAULT_VALUE), "test correct default value is emptyArray for this MF field object");
        assertTrue  (MFMatrix3f.matches(MFMatrix3f.DEFAULT_VALUE_STRING),
                                                        "MFMatrix3f.matches(MFMatrix3f.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFMatrix3f.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFMatrix3f.REGEX.contains("^") && !MFMatrix3f.REGEX.contains("$"), "test MFMatrix3f.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFMatrix3f.REGEX.equals(MFMatrix3d.REGEX), "test MFMatrix3f.REGEX.equals(MFMatrix3d.REGEX) returns true");

        testMFMatrix3f = new MFMatrix3f();
        assertTrue  (Arrays.equals(emptyArray,testMFMatrix3f.getPrimitiveValue()),   "tests default object value is emptyArray and results in emptyArray for equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix3f.matches(),       "testMFMatrix3f.matches() tests emptyArray initialization correctly matches regex");
        testMFMatrix3f.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFMatrix3f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix3f.matches(),       "testMFMatrix3f.matches() tests singleValueArray correctly matches regex");
        testMFMatrix3f.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFMatrix3f.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix3f.matches(),       "testMFMatrix3f.matches() tests doubleValueArray correctly matches regex");
        testMFMatrix3f.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFMatrix3f.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix3f.matches(),       "testMFMatrix3f.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFMatrix3f.matches(" 0  1  2   3  4  5  6 7 8 "),"MFMatrix3f.matches( \" 0  1  2   3  4  5  6 7 8 \") tests correct string value");
        assertFalse (MFMatrix3f.matches(" 0  1  2,  3  4  5, 6 7 8 "),"MFMatrix3f.matches( \" 0  1  2,  3  4  5, 6 7 8 \") tests incorrect string value, no commas allowed");
        assertTrue  (MFMatrix3f.matches("-1 -2 -3  -4 -5 -6  7 8 9 "),"MFMatrix3f.matches( \"-1 -2 -3  -4 -5 -6  7 8 9 \") tests correct string value");
        assertTrue  (MFMatrix3f.matches(" 0  12E45  0 4 5 6 7 8 9 "), "MFMatrix3f.matches(\" 0  12E45  0 4 5 6 7 8 9 \") tests correct string value, scientific notation");
        assertTrue  (MFMatrix3f.matches("+0 +12E+45 0 4 5 6 7 8 9 "), "MFMatrix3f.matches(\"+0,+12E+45 0 4 5 6 7 8 9 \") tests correct string value, scientific notation");
        assertTrue  (MFMatrix3f.matches("-0 -12E-45 0 4 5 6 7 8 9 ")," MFMatrix3f.matches(\"-0,-12E-45 0 4 5 6 7 8 9 \") tests correct string value, scientific notation");

        assertTrue  (MFMatrix3f.matches(""),             "MFMatrix3f.matches(\"\") tests correct empty string value");
        assertFalse (MFMatrix3f.matches(","),            "MFMatrix3f.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFMatrix3f.matches(" 0.0  1.0 2.0 3 4 5 6 7 8"), "MFMatrix3f.matches(\" 0.0  1.0 2.0 3 4 5 6 7 8\") tests correct string value");
        assertTrue  (MFMatrix3f.matches("-1.0 -3.0 -0  3 4 5 6 7 8"), "MFMatrix3f.matches(\"-1.0 -3.0 -0  3 4 5 6 7 8\") tests correct string value, including external whitespace");
        assertTrue  (MFMatrix3f.matches("0 1 0  3 4 5 6 7 8"),        "MFMatrix3f.matches(\"0 1 0  3 4 5 6 7 8\")  tests correct array as string value");
        assertTrue  (MFMatrix3f.matches("0.0 1.0 0  3 4 5 6 7 8"),    "MFMatrix3f.matches(\"0.0 1.0 0  3 4 5 6 7 8\")  tests correct array as string value");
        assertTrue  (MFMatrix3f.matches(" 0.0  12.3E45  0  3 4 5 6 7 8 "),"MFMatrix3f.matches(\" 0.0  12.3E45  0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix3f.matches("+0.0 +12.3E+45 0  3 4 5 6 7 8 "),"MFMatrix3f.matches(\"+0.0 +12.3E+45 0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix3f.matches("-0.0 -12.3E-45 0  3 4 5 6 7 8 "),"MFMatrix3f.matches(\"-0.0 -12.3E-45 0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix3f.matches( ".6 -.6 0 .6e7 -.6e-7 0 6 7 8 "),"MFMatrix3f.matches(\".6 -.6 0 .6e7 -.6e-7 0 6 7 8 \") tests correct string value, no leading digit before decimal point, scientific notation");
        assertFalse (MFMatrix3f.matches("0 0 0, 1 1 1, 2 2 2, "),         "MFMatrix3f.matches(\"0 0 0, 1 1 1, 2 2 2, \")  tests incorrect array as string value, including whitespace and commas, with trailing comma");

        assertFalse (MFMatrix3f.matches("true false false"),"MFMatrix3f.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (MFMatrix3f.matches("blah"),            "MFMatrix3f.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFMatrix3f.matches("NaN NaN NaN"),     "MFMatrix3f.matches(\"NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFMatrix3d multiple-field 9-tuple double-precision floating-point array")
    void MFMatrix3dTests()
	{
        System.out.println ("MFMatrix3dTests...");
        assertTrue  (Arrays.equals(MFMatrix3d.DEFAULT_VALUE, new MFMatrix3d().setValueByString(MFMatrix3d.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFMatrix3d testMFMatrix3d = new MFMatrix3d(); // static initializer is tested, might throw exception
        assertTrue  (testMFMatrix3d.matches(),       "testMFMatrix3d.matches() tests that object initialization correctly matches regex");
        double []       emptyArray = {};
//      double []    identityArray = { 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0 };
        double [] singleValueArray = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        double [] doubleValueArray = { 1.0, -2.0, -3.0d, -4.0d,  5.0d, -6.0d,  7.0d,  8.0d, 9.0d, 11.0d, -12.0d, -13.0d, -14.0d,  15.0d, -16.0d,  17.0d,  18.0d, 19.0d  };
        double [] tripleValueArray = { 1.0, -2.0, -3.0d,  4.0d,  5.0d, -6.0d,  7.0d,  8.0d, 9.0d, 11.0d, -12.0d, -13.0d, -14.0d,  15.0d, -16.0d,  17.0d,  18.0d, 19.0d, 21.0d, -22.0d, -23.0d, -24.0d,  25.0d, -26.0d,  27.0d,  28.0d, 29.0d };
        assertTrue  (Arrays.equals(emptyArray, MFMatrix3d.DEFAULT_VALUE), "test correct default value is emptyArray for this MF field object");
        assertTrue  (MFMatrix3d.matches(MFMatrix3d.DEFAULT_VALUE_STRING),
                                                        "MFMatrix3d.matches(MFMatrix3d.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFMatrix3d.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFMatrix3d.REGEX.contains("^") && !MFMatrix3d.REGEX.contains("$"), "test MFMatrix3d.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFMatrix3f.REGEX.equals(MFMatrix3d.REGEX), "test MFMatrix3f.REGEX.equals(MFMatrix3d.REGEX) returns true");

        testMFMatrix3d = new MFMatrix3d();
        assertTrue  (Arrays.equals(emptyArray,testMFMatrix3d.getPrimitiveValue()),   "tests setting object value is emptyArray and results in emptyArray for equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix3d.matches(),       "testMFMatrix3d.matches() tests emptyArray initialization correctly matches regex");
        testMFMatrix3d.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFMatrix3d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix3d.matches(),       "testMFMatrix3d.matches() tests singleValueArray correctly matches regex");
        testMFMatrix3d.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFMatrix3d.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix3d.matches(),       "testMFMatrix3d.matches() tests doubleValueArray correctly matches regex");
        testMFMatrix3d.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFMatrix3d.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix3d.matches(),       "testMFMatrix3d.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFMatrix3d.matches(" 0  1  2   3  4  5  6 7 8 "),"MFMatrix3d.matches( \" 0  1  2   3  4  5  6 7 8 \") tests correct string value");
        assertFalse (MFMatrix3d.matches(" 0  1  2,  3  4  5, 6 7 8 "),"MFMatrix3d.matches( \" 0  1  2,  3  4  5, 6 7 8 \") tests incorrect string value, no commas allowed");
        assertTrue  (MFMatrix3d.matches("-1 -2 -3  -4 -5 -6  7 8 9 "),"MFMatrix3d.matches( \"-1 -2 -3  -4 -5 -6  7 8 9 \") tests correct string value");
        assertTrue  (MFMatrix3d.matches(" 0  12E45  0 4 5 6 7 8 9 "), "MFMatrix3d.matches(\" 0  12E45  0 4 5 6 7 8 9 \") tests correct string value, scientific notation");
        assertTrue  (MFMatrix3d.matches("+0 +12E+45 0 4 5 6 7 8 9 "), "MFMatrix3d.matches(\"+0,+12E+45 0 4 5 6 7 8 9 \") tests correct string value, scientific notation");
        assertTrue  (MFMatrix3d.matches("-0 -12E-45 0 4 5 6 7 8 9 "), "MFMatrix3d.matches(\"-0,-12E-45 0 4 5 6 7 8 9 \") tests correct string value, scientific notation");

        assertTrue  (MFMatrix3d.matches(""),             "MFMatrix3d.matches(\"\") tests correct empty string value");
        assertFalse (MFMatrix3d.matches(","),            "MFMatrix3d.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFMatrix3d.matches(" 0.0  1.0 2.0 3 4 5 6 7 8"), "MFMatrix3d.matches(\" 0.0  1.0 2.0 3 4 5 6 7 8\") tests correct string value");
        assertTrue  (MFMatrix3d.matches("-1.0 -3.0 -0  3 4 5 6 7 8"), "MFMatrix3d.matches(\"-1.0 -3.0 -0  3 4 5 6 7 8\") tests correct string value, including external whitespace");
        assertTrue  (MFMatrix3d.matches("0 1 0  3 4 5 6 7 8"),        "MFMatrix3d.matches(\"0 1 0  3 4 5 6 7 8\")  tests correct array as string value");
        assertTrue  (MFMatrix3d.matches("0.0 1.0 0  3 4 5 6 7 8"),    "MFMatrix3d.matches(\"0.0 1.0 0  3 4 5 6 7 8\")  tests correct array as string value");
        assertTrue  (MFMatrix3d.matches(" 0.0  12.3E45  0  3 4 5 6 7 8 "),"MFMatrix3d.matches(\" 0.0  12.3E45  0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix3d.matches("+0.0 +12.3E+45 0  3 4 5 6 7 8 "),"MFMatrix3d.matches(\"+0.0 +12.3E+45 0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix3d.matches("-0.0 -12.3E-45 0  3 4 5 6 7 8 "),"MFMatrix3d.matches(\"-0.0 -12.3E-45 0  3 4 5 6 7 8\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix3d.matches( ".6 -.6 0 .6e7 -.6e-7 0 6 7 8 "),"MFMatrix3d.matches(\".6 -.6 0 .6e7 -.6e-7 0 6 7 8 \") tests correct string value, no leading digit before decimal point, scientific notation");
        assertFalse (MFMatrix3d.matches("0 0 0, 1 1 1, 2 2 2, "),         "MFMatrix3d.matches(\"0 0 0, 1 1 1, 2 2 2, \")  tests incorrect array as string value, including whitespace and commas, with trailing comma");

        assertFalse (MFMatrix3d.matches("true false false"),"MFMatrix3d.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (MFMatrix3d.matches("blah"),            "MFMatrix3d.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFMatrix3d.matches("NaN NaN NaN"),     "MFMatrix3d.matches(\"NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFMatrix4f single-field 16-tuple single-precision floating-point array")
    void SFMatrix4fTests()
	{
        System.out.println ("SFMatrix4fTests...");
        assertTrue  (Arrays.equals(SFMatrix4f.DEFAULT_VALUE, new SFMatrix4f().setValueByString(SFMatrix4f.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFMatrix4f testSFMatrix4f = new SFMatrix4f(); // static initializer is tested, might throw exception
        assertTrue  (testSFMatrix4f.matches(),       "testSFMatrix4f.matches() tests that object initialization correctly matches regex");
        float []       emptyArray = {};
        float []    identityArray = { 1.0f, 0.0f, 0.0f, 0.0f,  0.0f, 1.0f, 0.0f, 0.0f,  0.0f, 0.0f, 1.0f, 0.0f,  0.0f, 0.0f, 0.0f, 1.0f };
        float [] singleValueArray = { 0.0f, 0.0f, 0.0f, 0.0f,  0.0f, 0.0f, 0.0f, 0.0f,  0.0f, 0.0f, 0.0f, 0.0f,  0.0f, 0.0f, 0.0f, 0.0f };
//      float[] doubleValueArray = {  1.0f, -2.0f, -3.0f, -4.0f,  5.0f,  -6.0f,   7.0f,   8.0f,   9.0f,  10.0f, -11.0f, -12.0f, -13.0f, -14.0f, 15.0f, -16.0f, 
//                                    17.0f, 18.0f, 19.0f, 20.0f, 21.0f, -22.0f, -23.0f, -24.0f,  25.0f, -26.0f,  27.0f,  28.0f,  29.0f,  30.0f, 31.0f,  32.0f };
//      float[] tripleValueArray = {  1.0f, -2.0f, -3.0f, -4.0f,  5.0f,  -6.0f,   7.0f,   8.0f,   9.0f,  10.0f, -11.0f, -12.0f, -13.0f, -14.0f, 15.0f, -16.0f, 
//                                    17.0f, 18.0f, 19.0f, 20.0f, 21.0f, -22.0f, -23.0f, -24.0f,  25.0f, -26.0f,  27.0f,  28.0f,  29.0f,  30.0f, 31.0f,  32.0f,
//                                    33.0f, 34.0f, 35.0f, 36.0f, 37.0f, -38.0f, -39.0f, -40.0f,  41.0f, -42.0f,  43.0f,  44.0f,  45.0f,  46.0f, 47.0f,  48.0f};
        assertTrue  (Arrays.equals(identityArray, SFMatrix4f.DEFAULT_VALUE), "test correct default value is identity array for this MF field object");
        assertTrue  (SFMatrix4f.matches(SFMatrix4f.DEFAULT_VALUE_STRING),
                                                        "SFMatrix4f.matches(SFMatrix4f.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFMatrix4f.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFMatrix4f.REGEX.contains("^") && !SFMatrix4f.REGEX.contains("$"), "test SFMatrix4f.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFMatrix4f.REGEX.equals(SFMatrix4d.REGEX), "test SFMatrix4f.REGEX.equals(SFMatrix4d.REGEX) returns true");

        testSFMatrix4f = new SFMatrix4f();
        assertTrue  (Arrays.equals(identityArray,testSFMatrix4f.getPrimitiveValue()),   "tests setting default object value results in identityArray for equivalent getPrimitiveValue()");
        testSFMatrix4f.setIdentity();
        assertTrue  (Arrays.equals(identityArray,testSFMatrix4f.getPrimitiveValue()),   "tests setting object value using setIdentity() results in identityArray for equivalent getPrimitiveValue()");
        // TODO other utility methods when implemented
        assertTrue  (testSFMatrix4f.matches(),       "testSFMatrix4f.matches() tests setIdentity() initialization correctly matches regex");
        testSFMatrix4f.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFMatrix4f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testSFMatrix4f.matches(),       "testSFMatrix4f.matches() tests singleValueArray correctly matches regex");
//        testSFMatrix4f.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
//        assertEquals(doubleValueArray,testSFMatrix4f.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
//        assertTrue  (testSFMatrix4f.matches(),       "testSFMatrix4f.matches() tests doubleValueArray correctly matches regex");
//        testSFMatrix4f.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
//        assertEquals(tripleValueArray,testSFMatrix4f.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
//        assertTrue  (testSFMatrix4f.matches(),       "testSFMatrix4f.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (SFMatrix4f.matches(" 0  1  2   3  4  5  6 7 8  9 10 11 12 13 14 15"),"SFMatrix4f.matches(\" 0  1  2   3  4  5  6 7 8  9 10 11 12 13 14 15\") tests correct string value");
        assertFalse (SFMatrix4f.matches(" 0  1  2,  3  4  5, 6 7 8  9 10 11 12 13 14 15"),"SFMatrix4f.matches(\" 0  1  2,  3  4  5, 6 7 8  9 10 11 12 13 14 15\") tests incorrect string value, no commas allowed");
        assertTrue  (SFMatrix4f.matches("-1 -2 -3  -4 -5 -6  7 8 9 10 11 12 13 14 15 16"),"SFMatrix4f.matches(\"-1 -2 -3  -4 -5 -6  7 8 9 10 11 12 13 14 15 16\") tests correct string value");
        assertTrue  (SFMatrix4f.matches(" 0  12E45  0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"SFMatrix4f.matches(\" 0  12E45  0 4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix4f.matches("+0 +12E+45 0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"SFMatrix4f.matches(\"+0,+12E+45 0 4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix4f.matches("-0 -12E-45 0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"SFMatrix4f.matches(\"-0,-12E-45 0 4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");

        assertFalse (SFMatrix4f.matches(""),             "SFMatrix4f.matches(\"\") tests incorrect empty string value");
        assertFalse (SFMatrix4f.matches(","),            "SFMatrix4f.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (SFMatrix4f.matches(" 0.0  1.0 2.0       4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4f.matches(\" 0.0  1.0 2.0       4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value");
        assertTrue  (SFMatrix4f.matches("-1.0 -3.0 -0        4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4f.matches(\"-1.0 -3.0 -0        4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, including external whitespace");
        assertTrue  (SFMatrix4f.matches("0   1   0           4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4f.matches(\"0   1   0           4 5 6 7 8 9 10 11 12 13 14 15 16\")  tests correct array as string value");
        assertTrue  (SFMatrix4f.matches("0.0 1.0 0           4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4f.matches(\"0.0 1.0 0           4 5 6 7 8 9 10 11 12 13 14 15 16\")  tests correct array as string value");
        assertTrue  (SFMatrix4f.matches(" 0.0  12.3E45  0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4f.matches(\" 0.0  12.3E45  0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix4f.matches("+0.0 +12.3E+45 0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4f.matches(\"+0.0 +12.3E+45 0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix4f.matches("-0.0 -12.3E-45 0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4f.matches(\"-0.0 -12.3E-45 0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix4f.matches(" .6 -.6 .6e7 -.6e-7   5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4f.matches(\" .6 -.6 .6e7 -.6e-7   5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFMatrix4f.matches("0 0 0 0, 1 1 1 1, 2 2 2 2, 3 3 3 3"),                   "SFMatrix4f.matches(\"0 0 0 0, 1 1 1 1, 2 2 2 2, 3 3 3 3\")  tests incorrect array as string value, including whitespace and commas, with trailing comma");

        assertFalse (SFMatrix4f.matches("true false false"),"SFMatrix4f.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (SFMatrix4f.matches("blah"),            "SFMatrix4f.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFMatrix4f.matches("NaN NaN NaN"),     "SFMatrix4f.matches(\"NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test SFMatrix4d single-field 16-tuple double-precision floating-point array")
    void SFMatrix4dTests()
	{
        System.out.println ("SFMatrix4dTests...");
        assertTrue  (Arrays.equals(SFMatrix4d.DEFAULT_VALUE, new SFMatrix4d().setValueByString(SFMatrix4d.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        SFMatrix4d testSFMatrix4d = new SFMatrix4d(); // static initializer is tested, might throw exception
        assertTrue  (testSFMatrix4d.matches(),       "testSFMatrix4d.matches() tests that object initialization correctly matches regex");
        double []       emptyArray = {};
        double []    identityArray = { 1.0d, 0.0d, 0.0d, 0.0d,  0.0d, 1.0d, 0.0d, 0.0d,  0.0d, 0.0d, 1.0d, 0.0d,  0.0d, 0.0d, 0.0d, 1.0d };
        double [] singleValueArray = { 0.0d, 0.0d, 0.0d, 0.0d,  0.0d, 0.0d, 0.0d, 0.0d,  0.0d, 0.0d, 0.0d, 0.0d,  0.0d, 0.0d, 0.0d, 0.0d };
//      double [] doubleValueArray = { 1.0d, -2.0d, -3.0d, -4.0d,  5.0d,  -6.0d,   7.0d,   8.0d,   9.0d,  10.0d, -11.0d, -12.0d, -13.0d, -14.0d, 15.0d, -16.0d, 
//                                    17.0d, 18.0d, 19.0d, 20.0d, 21.0d, -22.0d, -23.0d, -24.0d,  25.0d, -26.0d,  27.0d,  28.0d,  29.0d,  30.0d, 31.0d,  32.0d };
//      double [] tripleValueArray = { 1.0d, -2.0d, -3.0d, -4.0d,  5.0d,  -6.0d,   7.0d,   8.0d,   9.0d,  10.0d, -11.0d, -12.0d, -13.0d, -14.0d, 15.0d, -16.0d, 
//                                    17.0d, 18.0d, 19.0d, 20.0d, 21.0d, -22.0d, -23.0d, -24.0d,  25.0d, -26.0d,  27.0d,  28.0d,  29.0d,  30.0d, 31.0d,  32.0d,
//                                    33.0d, 34.0d, 35.0d, 36.0d, 37.0d, -38.0d, -39.0d, -40.0d,  41.0d, -42.0d,  43.0d,  44.0d,  45.0d,  46.0d, 47.0d,  48.0d};
        assertTrue  (Arrays.equals(identityArray, SFMatrix4d.DEFAULT_VALUE), "test correct default value is identity array for this MF field object");
        assertTrue  (SFMatrix4d.matches(SFMatrix4d.DEFAULT_VALUE_STRING),
                                                        "SFMatrix4d.matches(SFMatrix4d.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testSFMatrix4d.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!SFMatrix4d.REGEX.contains("^") && !SFMatrix4d.REGEX.contains("$"), "test SFMatrix4d.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (SFMatrix4f.REGEX.equals(SFMatrix4d.REGEX), "test SFMatrix4d.REGEX.equals(SFMatrix4d.REGEX) returns true");

        testSFMatrix4d = new SFMatrix4d();
        assertTrue  (Arrays.equals(identityArray,testSFMatrix4d.getPrimitiveValue()),   "tests setting default object value results in identityArray for equivalent getPrimitiveValue()");
        testSFMatrix4d.setIdentity();
        assertTrue  (Arrays.equals(identityArray,testSFMatrix4d.getPrimitiveValue()),   "tests setting object value using setIdentity() results in identityArray for equivalent getPrimitiveValue()");
        assertTrue  (testSFMatrix4d.matches(),       "testSFMatrix4d.matches() tests setIdentity() initialization correctly matches regex");
        testSFMatrix4d.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testSFMatrix4d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testSFMatrix4d.matches(),       "testSFMatrix4d.matches() tests singleValueArray correctly matches regex");
//        testSFMatrix4d.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
//        assertEquals(doubleValueArray,testSFMatrix4d.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
//        assertTrue  (testSFMatrix4d.matches(),       "testSFMatrix4d.matches() tests doubleValueArray correctly matches regex");
//        testSFMatrix4d.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
//        assertEquals(tripleValueArray,testSFMatrix4d.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
//        assertTrue  (testSFMatrix4d.matches(),       "testSFMatrix4d.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (SFMatrix4d.matches(" 0  1  2   3  4  5  6 7 8  9 10 11 12 13 14 15"),"SFMatrix4d.matches( \" 0  1  2   3  4  5  6 7 8  9 10 11 12 13 14 15\") tests correct string value");
        assertFalse (SFMatrix4d.matches(" 0  1  2,  3  4  5, 6 7 8  9 10 11 12 13 14 15"),"SFMatrix4d.matches( \" 0  1  2,  3  4  5, 6 7 8  9 10 11 12 13 14 15\") tests incorrect string value, no commas allowed");
        assertTrue  (SFMatrix4d.matches("-1 -2 -3  -4 -5 -6  7 8 9 10 11 12 13 14 15 16"),"SFMatrix4d.matches( \"-1 -2 -3  -4 -5 -6  7 8 9 10 11 12 13 14 15 16\") tests correct string value");
        assertTrue  (SFMatrix4d.matches(" 0  12E45  0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"SFMatrix4d.matches(\" 0  12E45  0 4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix4d.matches("+0 +12E+45 0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"SFMatrix4d.matches(\"+0,+12E+45 0 4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix4d.matches("-0 -12E-45 0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"SFMatrix4d.matches(\"-0,-12E-45 0 4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");

        assertFalse (SFMatrix4d.matches(""),             "SFMatrix4d.matches(\"\") tests incorrect empty string value");
        assertFalse (SFMatrix4d.matches(","),            "SFMatrix4d.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (SFMatrix4d.matches(" 0.0  1.0 2.0       4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4d.matches(\" 0.0  1.0 2.0       4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value");
        assertTrue  (SFMatrix4d.matches("-1.0 -3.0 -0        4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4d.matches(\"-1.0 -3.0 -0        4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, including external whitespace");
        assertTrue  (SFMatrix4d.matches("0   1   0           4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4d.matches(\"0   1   0           4 5 6 7 8 9 10 11 12 13 14 15 16\")  tests correct array as string value");
        assertTrue  (SFMatrix4d.matches("0.0 1.0 0           4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4d.matches(\"0.0 1.0 0           4 5 6 7 8 9 10 11 12 13 14 15 16\")  tests correct array as string value");
        assertTrue  (SFMatrix4d.matches(" 0.0  12.3E45  0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4d.matches(\" 0.0  12.3E45  0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix4d.matches("+0.0 +12.3E+45 0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4d.matches(\"+0.0 +12.3E+45 0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix4d.matches("-0.0 -12.3E-45 0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4d.matches(\"-0.0 -12.3E-45 0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (SFMatrix4d.matches(" .6 -.6 .6e7 -.6e-7   5 6 7 8 9 10 11 12 13 14 15 16"), "SFMatrix4d.matches(\" .6 -.6 .6e7 -.6e-7   5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertFalse (SFMatrix4d.matches("0 0 0 0, 1 1 1 1, 2 2 2 2, 3 3 3 3"),                   "SFMatrix4d.matches(\"0 0 0 0, 1 1 1 1, 2 2 2 2, 3 3 3 3\")  tests incorrect array as string value, including whitespace and commas, with trailing comma");

        assertFalse (SFMatrix4d.matches("true false false"),"SFMatrix4d.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (SFMatrix4d.matches("blah"),            "SFMatrix4d.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (SFMatrix4d.matches("NaN NaN NaN"),     "SFMatrix4d.matches(\"NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFMatrix4f multiple-field 16-tuple single-precision floating-point array")
    void MFMatrix4fTests()
	{
        System.out.println ("MFMatrix4fTests...");
        assertTrue  (Arrays.equals(MFMatrix4f.DEFAULT_VALUE, new MFMatrix4f().setValueByString(MFMatrix4f.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFMatrix4f testMFMatrix4f = new MFMatrix4f(); // static initializer is tested, might throw exception
        assertTrue  (testMFMatrix4f.matches(),       "testMFMatrix4f.matches() tests that object initialization correctly matches regex");
        float []       emptyArray = {};
//      float []    identityArray = { 1.0f, 0.0f, 0.0f, 0.0f,  0.0f, 1.0f, 0.0f, 0.0f,  0.0f, 0.0f, 1.0f, 0.0f,  0.0f, 0.0f, 0.0f, 1.0f };
        float [] singleValueArray = { 0.0f, 0.0f, 0.0f, 0.0f,  0.0f, 0.0f, 0.0f, 0.0f,  0.0f, 0.0f, 0.0f, 0.0f,  0.0f, 0.0f, 0.0f, 0.0f };
        float [] doubleValueArray = {  1.0f, -2.0f, -3.0f, -4.0f,  5.0f,  -6.0f,   7.0f,   8.0f,   9.0f,  10.0f, -11.0f, -12.0f, -13.0f, -14.0f, 15.0f, -16.0f, 
                                      17.0f, 18.0f, 19.0f, 20.0f, 21.0f, -22.0f, -23.0f, -24.0f,  25.0f, -26.0f,  27.0f,  28.0f,  29.0f,  30.0f, 31.0f,  32.0f };
        float [] tripleValueArray = {  1.0f, -2.0f, -3.0f, -4.0f,  5.0f,  -6.0f,   7.0f,   8.0f,   9.0f,  10.0f, -11.0f, -12.0f, -13.0f, -14.0f, 15.0f, -16.0f, 
                                      17.0f, 18.0f, 19.0f, 20.0f, 21.0f, -22.0f, -23.0f, -24.0f,  25.0f, -26.0f,  27.0f,  28.0f,  29.0f,  30.0f, 31.0f,  32.0f,
                                      33.0f, 34.0f, 35.0f, 36.0f, 37.0f, -38.0f, -39.0f, -40.0f,  41.0f, -42.0f,  43.0f,  44.0f,  45.0f,  46.0f, 47.0f,  48.0f};
        assertTrue  (Arrays.equals(emptyArray, MFMatrix4f.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFMatrix4f.matches(MFMatrix4f.DEFAULT_VALUE_STRING),
                                                        "MFMatrix4f.matches(MFMatrix4f.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFMatrix4f.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFMatrix4f.REGEX.contains("^") && !MFMatrix4f.REGEX.contains("$"), "test MFMatrix4f.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFMatrix4f.REGEX.equals(MFMatrix4d.REGEX), "test MFMatrix4f.REGEX.equals(MFMatrix4d.REGEX) returns true");

        testMFMatrix4f = new MFMatrix4f();
        assertTrue  (Arrays.equals(emptyArray,testMFMatrix4f.getPrimitiveValue()),   "tests setting object value to default object results in emptyArray for equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix4f.matches(),       "testMFMatrix4f.matches() tests emptyArray initialization correctly matches regex");
        testMFMatrix4f.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFMatrix4f.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix4f.matches(),       "testMFMatrix4f.matches() tests singleValueArray correctly matches regex");
        testMFMatrix4f.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFMatrix4f.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix4f.matches(),       "testMFMatrix4f.matches() tests doubleValueArray correctly matches regex");
        testMFMatrix4f.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFMatrix4f.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix4f.matches(),       "testMFMatrix4f.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFMatrix4f.matches(" 0  1  2   3  4  5  6 7 8  9 10 11 12 13 14 15"),"MFMatrix4f.matches( \" 0  1  2   3  4  5  6 7 8  9 10 11 12 13 14 15\") tests correct string value");
        assertFalse (MFMatrix4f.matches(" 0  1  2,  3  4  5, 6 7 8  9 10 11 12 13 14 15"),"MFMatrix4f.matches( \" 0  1  2,  3  4  5, 6 7 8  9 10 11 12 13 14 15\") tests incorrect string value, no commas allowed");
        assertTrue  (MFMatrix4f.matches("-1 -2 -3  -4 -5 -6  7 8 9 10 11 12 13 14 15 16"),"MFMatrix4f.matches( \"-1 -2 -3  -4 -5 -6  7 8 9 10 11 12 13 14 15 16\") tests correct string value");
        assertTrue  (MFMatrix4f.matches(" 0  12E45  0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"MFMatrix4f.matches(\" 0  12E45  0 4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix4f.matches("+0 +12E+45 0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"MFMatrix4f.matches(\"+0,+12E+45 0 4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix4f.matches("-0 -12E-45 0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"MFMatrix4f.matches(\"-0,-12E-45 0 4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");

        assertTrue  (MFMatrix4f.matches(""),             "MFMatrix4f.matches(\"\") tests correct empty string value");
        assertFalse (MFMatrix4f.matches(","),            "MFMatrix4f.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFMatrix4f.matches(" 0.0  1.0 2.0       4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4f.matches(\" 0.0  1.0 2.0       4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value");
        assertTrue  (MFMatrix4f.matches("-1.0 -3.0 -0        4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4f.matches(\"-1.0 -3.0 -0        4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, including external whitespace");
        assertTrue  (MFMatrix4f.matches("0   1   0           4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4f.matches(\"0   1   0           4 5 6 7 8 9 10 11 12 13 14 15 16\")  tests correct array as string value");
        assertTrue  (MFMatrix4f.matches("0.0 1.0 0           4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4f.matches(\"0.0 1.0 0           4 5 6 7 8 9 10 11 12 13 14 15 16\")  tests correct array as string value");
        assertTrue  (MFMatrix4f.matches(" 0.0  12.3E45  0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4f.matches(\" 0.0  12.3E45  0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix4f.matches("+0.0 +12.3E+45 0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4f.matches(\"+0.0 +12.3E+45 0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix4f.matches("-0.0 -12.3E-45 0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4f.matches(\"-0.0 -12.3E-45 0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix4f.matches(" .6 -.6 .6e7 -.6e-7   5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4f.matches(\" .6 -.6 .6e7 -.6e-7   5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertFalse (MFMatrix4f.matches("0 0 0 0, 1 1 1 1, 2 2 2 2, 3 3 3 3"),                   "MFMatrix4f.matches(\"0 0 0 0, 1 1 1 1, 2 2 2 2, 3 3 3 3\")  tests incorrect array as string value, including whitespace and commas, with trailing comma");

        assertFalse (MFMatrix4f.matches("true false false"),"MFMatrix4f.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (MFMatrix4f.matches("blah"),            "MFMatrix4f.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFMatrix4f.matches("NaN NaN NaN"),     "MFMatrix4f.matches(\"NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }
    
    @Test
    @DisplayName("Test MFMatrix4d multiple-field 16-tuple double-precision floating-point array")
    void MFMatrix4dTests()
	{
        System.out.println ("MFMatrix4dTests...");
        assertTrue  (Arrays.equals(MFMatrix4d.DEFAULT_VALUE, new MFMatrix4d().setValueByString(MFMatrix4d.DEFAULT_VALUE_STRING).getPrimitiveValue()), 
                                                        "test DEFAULT_VALUE matches DEFAULT_VALUE_STRING for this field object");
        MFMatrix4d testMFMatrix4d = new MFMatrix4d(); // static initializer is tested, might throw exception
        assertTrue  (testMFMatrix4d.matches(),       "testMFMatrix4d.matches() tests that object initialization correctly matches regex");
        double []       emptyArray = {};
//      double []    identityArray = { 1.0d, 0.0d, 0.0d, 0.0d,  0.0d, 1.0d, 0.0d, 0.0d,  0.0d, 0.0d, 1.0d, 0.0d,  0.0d, 0.0d, 0.0d, 1.0d };
        double [] singleValueArray = { 0.0d, 0.0d, 0.0d, 0.0d,  0.0d, 0.0d, 0.0d, 0.0d,  0.0d, 0.0d, 0.0d, 0.0d,  0.0d, 0.0d, 0.0d, 0.0d };
      double [] doubleValueArray = { 1.0d, -2.0d, -3.0d, -4.0d,  5.0d,  -6.0d,   7.0d,   8.0d,   9.0d,  10.0d, -11.0d, -12.0d, -13.0d, -14.0d, 15.0d, -16.0d, 
                                    17.0d, 18.0d, 19.0d, 20.0d, 21.0d, -22.0d, -23.0d, -24.0d,  25.0d, -26.0d,  27.0d,  28.0d,  29.0d,  30.0d, 31.0d,  32.0d };
      double [] tripleValueArray = { 1.0d, -2.0d, -3.0d, -4.0d,  5.0d,  -6.0d,   7.0d,   8.0d,   9.0d,  10.0d, -11.0d, -12.0d, -13.0d, -14.0d, 15.0d, -16.0d, 
                                    17.0d, 18.0d, 19.0d, 20.0d, 21.0d, -22.0d, -23.0d, -24.0d,  25.0d, -26.0d,  27.0d,  28.0d,  29.0d,  30.0d, 31.0d,  32.0d,
                                    33.0d, 34.0d, 35.0d, 36.0d, 37.0d, -38.0d, -39.0d, -40.0d,  41.0d, -42.0d,  43.0d,  44.0d,  45.0d,  46.0d, 47.0d,  48.0d};
        assertTrue  (Arrays.equals(emptyArray, MFMatrix4d.DEFAULT_VALUE), "test correct default value is empty array for this MF field object");
        assertTrue  (MFMatrix4d.matches(MFMatrix4d.DEFAULT_VALUE_STRING),
                                                        "MFMatrix4d.matches(MFMatrix4d.DEFAULT_VALUE_STRING) tests object initialization correctly matches regex");
        assertTrue  (testMFMatrix4d.isDefaultValue(),"test initialized field object isDefaultValue() returns true");
        assertTrue  (!MFMatrix4d.REGEX.contains("^") && !MFMatrix4d.REGEX.contains("$"), "test MFMatrix4d.REGEX does not contain anchor characters ^ or $");
        // confirm expected equivalent regexes
        assertTrue  (MFMatrix4d.REGEX.equals(MFMatrix4d.REGEX), "test MFMatrix4d.REGEX.equals(MFMatrix4d.REGEX) returns true");

        testMFMatrix4d = new MFMatrix4d();
        assertTrue  (Arrays.equals(emptyArray,testMFMatrix4d.getPrimitiveValue()),   "tests setting object value to default object results in emptyArray for equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix4d.matches(),       "testMFMatrix4d.matches() tests emptyArray initialization correctly matches regex");
        testMFMatrix4d.setValue(singleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(singleValueArray,testMFMatrix4d.getPrimitiveValue(),   "tests setting object value to singleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix4d.matches(),       "testMFMatrix4d.matches() tests singleValueArray correctly matches regex");
        testMFMatrix4d.setValue(doubleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(doubleValueArray,testMFMatrix4d.getPrimitiveValue(),   "tests setting object value to doubleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix4d.matches(),       "testMFMatrix4d.matches() tests doubleValueArray correctly matches regex");
        testMFMatrix4d.setValue(tripleValueArray); // returns void because it matches (overrides) Java SAI specification interface
        assertEquals(tripleValueArray,testMFMatrix4d.getPrimitiveValue(),   "tests setting object value to tripleValueArray results in equivalent getPrimitiveValue()");
        assertTrue  (testMFMatrix4d.matches(),       "testMFMatrix4d.matches() tests tripleValueArray correctly matches regex");
        
        assertTrue  (MFMatrix4d.matches(" 0  1  2   3  4  5  6 7 8  9 10 11 12 13 14 15"),"MFMatrix4d.matches(\" 0  1  2   3  4  5  6 7 8  9 10 11 12 13 14 15\") tests correct string value");
        assertFalse (MFMatrix4d.matches(" 0  1  2,  3  4  5, 6 7 8  9 10 11 12 13 14 15"),"MFMatrix4d.matches(\" 0  1  2,  3  4  5, 6 7 8  9 10 11 12 13 14 15\") tests incorrect string value, no commas allowed");
        assertTrue  (MFMatrix4d.matches("-1 -2 -3  -4 -5 -6  7 8 9 10 11 12 13 14 15 16"),"MFMatrix4d.matches(\"-1 -2 -3  -4 -5 -6  7 8 9 10 11 12 13 14 15 16\") tests correct string value");
        assertTrue  (MFMatrix4d.matches(" 0  12E45  0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"MFMatrix4d.matches(\" 0  12E45  0 4 5 6  7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix4d.matches("+0 +12E+45 0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"MFMatrix4d.matches(\"+0 +12E+45 0 4 5 6  7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix4d.matches("-0 -12E-45 0 4 5 6  7 8 9 10 11 12 13 14 15 16"),"MFMatrix4d.matches(\"-0 -12E-45 0 4 5 6  7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");

        assertTrue  (MFMatrix4d.matches(""),             "MFMatrix4d.matches(\"\") tests correct empty string value");
        assertFalse (MFMatrix4d.matches(","),            "MFMatrix4d.matches(\",\") tests incorrect inclusion of comma as whitespace");
        assertTrue  (MFMatrix4d.matches(" 0.0  1.0 2.0       4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4d.matches(\" 0.0  1.0 2.0       4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value");
        assertTrue  (MFMatrix4d.matches("-1.0 -3.0 -0        4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4d.matches(\"-1.0 -3.0 -0        4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, including external whitespace");
        assertTrue  (MFMatrix4d.matches("0   1   0           4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4d.matches(\"0   1   0           4 5 6 7 8 9 10 11 12 13 14 15 16\")  tests correct array as string value");
        assertTrue  (MFMatrix4d.matches("0.0 1.0 0           4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4d.matches(\"0.0 1.0 0           4 5 6 7 8 9 10 11 12 13 14 15 16\")  tests correct array as string value");
        assertTrue  (MFMatrix4d.matches(" 0.0  12.3E45  0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4d.matches(\" 0.0  12.3E45  0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix4d.matches("+0.0 +12.3E+45 0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4d.matches(\"+0.0 +12.3E+45 0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix4d.matches("-0.0 -12.3E-45 0    4 5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4d.matches(\"-0.0 -12.3E-45 0    4 5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, scientific notation");
        assertTrue  (MFMatrix4d.matches(" .6 -.6 .6e7 -.6e-7   5 6 7 8 9 10 11 12 13 14 15 16"), "MFMatrix4d.matches(\" .6 -.6 .6e7 -.6e-7   5 6 7 8 9 10 11 12 13 14 15 16\") tests correct string value, no leading digit before decimal point, scientific notation");
        assertFalse (MFMatrix4d.matches("0 0 0 0, 1 1 1 1, 2 2 2 2, 3 3 3 3"),                   "MFMatrix4d.matches(\"0 0 0 0, 1 1 1 1, 2 2 2 2, 3 3 3 3\")  tests incorrect array as string value, including whitespace and commas, with trailing comma");

        assertFalse (MFMatrix4d.matches("true false false"),"MFMatrix4d.matches(\"true false false\") tests incorrect boolean string value");
        assertFalse (MFMatrix4d.matches("blah"),            "MFMatrix4d.matches(\"blah\") tests incorrect alphabetic string value");
        assertFalse (MFMatrix4d.matches("NaN NaN NaN"),     "MFMatrix4d.matches(\"NaN NaN NaN\") tests Not A Number (NaN) which is not an allowed string value");
    }

    /** Default main() method provided for test purposes.
     * @param args the command line arguments
     * @see #fieldObjectInitializationsTest()
     */
    public static void main(String[] args)
    {
        System.out.println("FieldObjectTests start...");
        FieldObjectTests thisFieldTestSet = new FieldObjectTests();
        thisFieldTestSet.fieldObjectInitializationsTest();
        System.out.println("FieldObjectTests complete");
    }
}