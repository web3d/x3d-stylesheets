#!/bin/bash

# generate a schema from X3DJSAIL

export HOME=c:/Users/coderextreme
export REPOSITORY=${HOME}/.m2/repository
javac -cp "${REPOSITORY}/org/slf4j/slf4j-jdk14/1.7.12/slf4j-jdk14-1.7.12.jar;${REPOSITORY}/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.jar;${REPOSITORY}/com/fasterxml/classmate/1.5.1/classmate-1.5.1.jar;${HOME}/jsonschema-generator/jsonschema-generator/target/jsonschema-generator-4.10.0-SNAPSHOT.jar;../jars/X3DJSAIL.3.3.full.jar;." net/coderextreme/SchemaG.java
npm install -g jsonlint
java -cp "${REPOSITORY}/org/slf4j/slf4j-jdk14/1.7.12/slf4j-jdk14-1.7.12.jar;${REPOSITORY}/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.jar;${REPOSITORY}/com/fasterxml/classmate/1.5.1/classmate-1.5.1.jar;${HOME}/jsonschema-generator/jsonschema-generator/target/jsonschema-generator-4.10.0-SNAPSHOT.jar;../jars/X3DJSAIL.3.3.full.jar;." net.coderextreme.SchemaG | jsonlint
