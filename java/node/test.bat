set PATH=%PATH%;%HOMEDRIVE%%HOMEPATH%\apache-ant-1.10.4\bin
cd .. && ant test.node && node node/examples/Node.js > node/examples/Node0.x3d
