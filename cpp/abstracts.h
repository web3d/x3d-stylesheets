using namespace std;
/** X3DAppearanceChildNode defines an abstract node class that extends class X3DNode.
  * Nodes of this type can be used as child nodes for Appearance. */

class X3DAppearanceChildNode : public X3DNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DAppearanceNode defines an abstract node class that extends class X3DNode.
  * Base type for all Appearance nodes. */

class X3DAppearanceNode : public X3DNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DBackgroundNode defines an abstract node class that extends classs X3DBindableNode, X3DChildNode, and X3DNode.
  * Abstract type from which all backgrounds inherit, also defining a background binding stack. */

class X3DBackgroundNode : public X3DBindableNode
{
  /** Provide float* value in radians (-inf,inf) from inputOutput MFFloat field named "groundAngle". */
  float* getGroundAngle ();

  /** Provide number of primitive values in "groundAngle" array */
  int getNumGroundAngle ();

  /** Assign float* value in radians (-inf,inf) to inputOutput MFFloat field named "groundAngle". */
  void setGroundAngle (float* angles);

  /** Assign single float* value in radians (-inf,inf) as the MFFloat array for inputOutput field named "groundAngle" */
  void setGroundAngle (float angle);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput MFColor field named "groundColor". */
  float* getGroundColor ();

  /** Provide number of 3-tuple primitive values in "groundColor" array */
  int getNumGroundColor ();

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput MFColor field named "groundColor". */
  void setGroundColor (float* colors) throw (InvalidFieldValueException);

  /** Provide float* value in radians (-inf,inf) from inputOutput MFFloat field named "skyAngle". */
  float* getSkyAngle ();

  /** Provide number of primitive values in "skyAngle" array */
  int getNumSkyAngle ();

  /** Assign float* value in radians (-inf,inf) to inputOutput MFFloat field named "skyAngle". */
  void setSkyAngle (float* angles);

  /** Assign single float* value in radians (-inf,inf) as the MFFloat array for inputOutput field named "skyAngle" */
  void setSkyAngle (float angle);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput MFColor field named "skyColor". */
  float* getSkyColor ();

  /** Provide number of 3-tuple primitive values in "skyColor" array */
  int getNumSkyColor ();

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput MFColor field named "skyColor". */
  void setSkyColor (float* colors) throw (InvalidFieldValueException);

  /** Provide float value from inputOutput SFFloat field named "transparency". */
  float getTransparency ();

  /** Assign float value to inputOutput SFFloat field named "transparency". */
  void setTransparency (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Assign bool value to inputOnly SFBool field named "set_bind". */
  void setBind (bool value);

  /** Provide double value in seconds from outputOnly SFTime field named "bindTime". */
  double getBindTime ();

  /** Provide bool value from outputOnly SFBool field named "isBound". */
  bool getIsBound ();

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DBindableNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Bindable nodes implement the binding stack, so that only one of each node type is active at a given time. */

class X3DBindableNode : public X3DChildNode
{
  /** Assign bool value to inputOnly SFBool field named "set_bind". */
  void setBind (bool value);

  /** Provide double value in seconds from outputOnly SFTime field named "bindTime". */
  double getBindTime ();

  /** Provide bool value from outputOnly SFBool field named "isBound". */
  bool getIsBound ();

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DChaserNode defines an abstract node class that extends classs X3DFollowerNode, X3DChildNode, and X3DNode.
  * The X3DChaserNode abstract node type calculates the output on value_changed as a finite impulse response (FIR) based on the events received on set_destination field. */

class X3DChaserNode : public X3DFollowerNode
{
  /** Provide double value in seconds [0,inf) from initializeOnly SFTime field named "duration". */
  double getDuration ();

  /** Assign double value in seconds [0,inf) to initializeOnly SFTime field named "duration". */
  void setDuration (double timestamp) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DChildNode defines an abstract node class that extends class X3DNode.
  * A node that implements X3DChildNode is one of the legal children for a X3DGroupingNode parent. */

class X3DChildNode : public X3DNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DColorNode defines an abstract node class that extends classs X3DGeometricPropertyNode and X3DNode.
  * Base type for color specifications in X3D. */

class X3DColorNode : public X3DGeometricPropertyNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DComposableVolumeRenderStyleNode defines an abstract node class that extends classs X3DVolumeRenderStyleNode and X3DNode.
  * The X3DComposableVolumeRenderStyleNode abstract node type is the base type for all node types that allow rendering styles to be sequentially composed together to form a single renderable output. */

class X3DComposableVolumeRenderStyleNode : public X3DVolumeRenderStyleNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DComposedGeometryNode defines an abstract node class that extends classs X3DGeometryNode and X3DNode.
  * Composed geometry nodes produce renderable geometry, can contain Color Coordinate Normal TextureCoordinate, and are contained by a Shape node. */

class X3DComposedGeometryNode : public X3DGeometryNode
{
  /** Provide bool value from initializeOnly SFBool field named "ccw". */
  bool getCcw ();

  /** Assign bool value to initializeOnly SFBool field named "ccw". */
  void setCcw (bool value);

  /** Provide bool value from initializeOnly SFBool field named "colorPerVertex". */
  bool getColorPerVertex ();

  /** Assign bool value to initializeOnly SFBool field named "colorPerVertex". */
  void setColorPerVertex (bool color);

  /** Provide bool value from initializeOnly SFBool field named "normalPerVertex". */
  bool getNormalPerVertex ();

  /** Assign bool value to initializeOnly SFBool field named "normalPerVertex". */
  void setNormalPerVertex (bool value);

  /** Provide bool value from inputOutput SFBool field named "solid". */
  bool getSolid ();

  /** Assign bool value to inputOutput SFBool field named "solid". */
  void setSolid (bool value);

  /** Provide X3DVertexAttributeNode* value (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DVertexAttributeNode type field named "attrib". */
  X3DNode* getAttrib ();

  /** Provide number of nodes in "attrib" array */
  int getNumAttrib ();

  /** Assign X3DVertexAttributeNode* value (using a properly typed node array) to inputOutput X3DVertexAttributeNode type field named "attrib". */
  void setAttrib (X3DVertexAttributeNode* nodes);

  /** Assign single X3DVertexAttributeNode* value (using a properly typed node MFNode) as the MFNode array for inputOutput field named "attrib" */
  void setAttrib (X3DVertexAttributeNode node);

  /** Assign X3DVertexAttributeNode* value (using a properly typed protoInstance array) to inputOutput X3DVertexAttributeNode type field named "attrib". */
  void setAttrib (X3DPrototypeInstance node);

  /** Assign X3DVertexAttributeNode* value (using a properly typed node array) to inputOutput X3DVertexAttributeNode type field named "attrib". */
  void setAttrib (X3DNode nodes);

  /** Provide X3DColorNode value (using a properly typed node or X3DPrototypeInstance) using RGB values [0..1] from inputOutput X3DColorNode type field named "color". */
  X3DNode* getColor ();

  /** Assign X3DColorNode value (using a properly typed node) using RGB values [0..1] to inputOutput X3DColorNode type field named "color". */
  void setColor (X3DColorNode color) throw (InvalidFieldValueException);

  /** Assign X3DColorNode value (using a properly typed protoInstance) */
  void setColor (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DCoordinateNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DCoordinateNode type field named "coord". */
  X3DNode* getCoord ();

  /** Assign X3DCoordinateNode value (using a properly typed node) to inputOutput X3DCoordinateNode type field named "coord". */
  void setCoord (X3DCoordinateNode node);

  /** Assign X3DCoordinateNode value (using a properly typed protoInstance) */
  void setCoord (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide FogCoordinate value (using a properly typed node or X3DPrototypeInstance) from inputOutput FogCoordinate type field named "fogCoord". */
  X3DNode* getFogCoord ();

  /** Assign FogCoordinate value (using a properly typed node) to inputOutput FogCoordinate type field named "fogCoord". */
  void setFogCoord (FogCoordinate node);

  /** Assign FogCoordinate value (using a properly typed protoInstance) */
  void setFogCoord (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DNormalNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DNormalNode type field named "normal". */
  X3DNode* getNormal ();

  /** Assign X3DNormalNode value (using a properly typed node) to inputOutput X3DNormalNode type field named "normal". */
  void setNormal (X3DNormalNode node);

  /** Assign X3DNormalNode value (using a properly typed protoInstance) */
  void setNormal (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DSingleTextureCoordinateNode|MultiTextureCoordinate value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DSingleTextureCoordinateNode|MultiTextureCoordinate type field named "texCoord". */
  X3DNode* getTexCoord ();

  /** Assign X3DSingleTextureCoordinateNode|MultiTextureCoordinate value (using a properly typed node) to inputOutput X3DSingleTextureCoordinateNode|MultiTextureCoordinate type field named "texCoord". */
  void setTexCoord (X3DNode node);

  /** Assign X3DSingleTextureCoordinateNode|MultiTextureCoordinate value (using a properly typed protoInstance) */
  void setTexCoord (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DCoordinateNode defines an abstract node class that extends classs X3DGeometricPropertyNode and X3DNode.
  * Base type for all coordinate node types in X3D. */

class X3DCoordinateNode : public X3DGeometricPropertyNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DDamperNode defines an abstract node class that extends classs X3DFollowerNode, X3DChildNode, and X3DNode.
  * The X3DDamperNode abstract node type creates an IIR response that approaches the destination value according to the shape of the e-function only asymptotically but very quickly. */

class X3DDamperNode : public X3DFollowerNode
{
  /** Provide double value in seconds [0,inf) from inputOutput SFTime field named "tau". */
  double getTau ();

  /** Assign double value in seconds [0,inf) to inputOutput SFTime field named "tau". */
  void setTau (double timestamp) throw (InvalidFieldValueException);

  /** Provide float value from inputOutput SFFloat field named "tolerance". */
  float getTolerance ();

  /** Assign float value to inputOutput SFFloat field named "tolerance". */
  void setTolerance (float value);

  /** Provide int value [0,5) from initializeOnly SFInt32 field named "order". */
  int getOrder ();

  /** Assign int value [0,5) to initializeOnly SFInt32 field named "order". */
  void setOrder (int value) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DDragSensorNode defines an abstract node class that extends classs X3DPointingDeviceSensorNode, X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all drag-style pointing device sensors. */

class X3DDragSensorNode : public X3DPointingDeviceSensorNode
{
  /** Provide 3-tuple float* value from outputOnly SFVec3f field named "trackPoint_changed". */
  float* getTrackPoint ();

  /** Provide bool value from inputOutput SFBool field named "autoOffset". */
  bool getAutoOffset ();

  /** Assign bool value to inputOutput SFBool field named "autoOffset". */
  void setAutoOffset (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isOver". */
  bool getIsOver ();

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DEnvironmentalSensorNode defines an abstract node class that extends classs X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for the environmental sensor nodes ProximitySensor, TransformSensor and VisibilitySensor. */

class X3DEnvironmentalSensorNode : public X3DSensorNode
{
  /** Provide 3-tuple float* value (-inf,inf) from initializeOnly SFVec3f field named "size". */
  float* getSize ();

  /** Assign 3-tuple float* value (-inf,inf) to initializeOnly SFVec3f field named "size". */
  void setSize (float* value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DEnvironmentTextureNode defines an abstract node class that extends classs X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all nodes that specify cubic environment map sources for texture images. */

class X3DEnvironmentTextureNode : public X3DTextureNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DFollowerNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * X3DFollowerNode is the abstract base class for all nodes in the Followers component. */

class X3DFollowerNode : public X3DChildNode
{
  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DFontStyleNode defines an abstract node class.
  * Base type for all font style nodes. */

class X3DFontStyleNode : public X3DNode
{
  /** Provide xs:NMTOKENS value from inputOutput xs:NMTOKENS type field named "class". */
  xs:NMTOKENS getClass ();

  /** Assign xs:NMTOKENS value to inputOutput xs:NMTOKENS type field named "class". */
  void setClass (xs:NMTOKENS value);

  /** Provide MFString value from inputOutput SFString field named "id". */
  MFString getId ();

  /** Assign MFString value to inputOutput SFString field named "id". */
  void setId (MFString value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DGeometricPropertyNode defines an abstract node class that extends class X3DNode.
  * Base type for all geometric property node types. */

class X3DGeometricPropertyNode : public X3DNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DGeometryNode defines an abstract node class that extends class X3DNode.
  * Geometry nodes produce renderable geometry and are contained by a Shape node. */

class X3DGeometryNode : public X3DNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DGroupingNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Grouping nodes can contain other nodes as children, thus making up the backbone of a scene graph. */

class X3DGroupingNode : public X3DChildNode, X3DBoundedObject
{
  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  float* getBboxCenter ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void setBboxCenter (float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  float* getBboxSize ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void setBboxSize (float* value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  void setVisible (bool value);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren (X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node MFNode) as the MFNode array for inputOnly field named "addChildren" */
  void addChildren (X3DChildNode node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren (X3DNode nodes);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren (X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node MFNode) as the MFNode array for inputOnly field named "removeChildren" */
  void removeChildren (X3DChildNode node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren (X3DNode nodes);

  /** Provide X3DChildNode* value (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DChildNode type field named "children". */
  X3DNode* getChildren ();

  /** Provide number of nodes in "children" array */
  int getNumChildren ();

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  void setChildren (X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node MFNode) as the MFNode array for inputOutput field named "children" */
  void setChildren (X3DChildNode node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOutput X3DChildNode type field named "children". */
  void setChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  void setChildren (X3DNode nodes);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DInfoNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Base type for all nodes that contain only information without visual semantics. */

class X3DInfoNode : public X3DChildNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DInterpolatorNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Interpolator nodes are designed for linear keyframed animation. Interpolators are driven by an input key ranging [0..1] and produce corresponding piecewise-linear output functions. */

class X3DInterpolatorNode : public X3DChildNode
{
  /** Assign float value to inputOnly SFFloat field named "set_fraction". */
  void setFraction (float value);

  /** Provide float* value from inputOutput MFFloat field named "key". */
  float* getKey ();

  /** Provide number of primitive values in "key" array */
  int getNumKey ();

  /** Assign float* value to inputOutput MFFloat field named "key". */
  void setKey (float* values);

  /** Assign single float* value as the MFFloat array for inputOutput field named "key" */
  void setKey (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DKeyDeviceSensorNode defines an abstract node class that extends classs X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all sensor node types that operate using key devices. */

class X3DKeyDeviceSensorNode : public X3DSensorNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DLayerNode defines an abstract node class that extends class X3DNode.
  * The X3DLayerNode abstract node type is the base node type for layer nodes. */

class X3DLayerNode : public X3DNode, X3DPickableObject
{
  /** Provide MFString* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  MFString* getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  int getNumObjectType ();

  /** Assign MFString* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void setObjectType (MFString* values) throw (InvalidFieldValueException);

  /** Provide MFString* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  MFString* getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  int getNumObjectType ();

  /** Assign MFString* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void setObjectType (MFString* values);

  /** Assign single MFString* value ["ALL","NONE","TERRAIN",...] as the MFString array for inputOutput field named "objectType" */
  void setObjectType (MFString value);

  /** Provide bool value from inputOutput SFBool field named "pickable". */
  bool getPickable ();

  /** Assign bool value to inputOutput SFBool field named "pickable". */
  void setPickable (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  void setVisible (bool value);

  /** Provide X3DViewportNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DViewportNode type field named "viewport". */
  X3DNode* getViewport ();

  /** Assign X3DViewportNode value (using a properly typed node) to inputOutput X3DViewportNode type field named "viewport". */
  void setViewport (X3DViewportNode node);

  /** Assign X3DViewportNode value (using a properly typed protoInstance) */
  void setViewport (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DLayoutNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * X3DLayoutNode is the base node type for layout nodes. */

class X3DLayoutNode : public X3DChildNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DLightNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Light nodes provide illumination for rendering geometry in the scene. Implementing nodes must include a global field with type SFBool and accessType inputOutput. */

class X3DLightNode : public X3DChildNode
{
  /** Provide float value from inputOutput SFFloat field named "ambientIntensity". */
  float getAmbientIntensity ();

  /** Assign float value to inputOutput SFFloat field named "ambientIntensity". */
  void setAmbientIntensity (float value);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "color". */
  float* getColor ();

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "color". */
  void setColor (float* color) throw (InvalidFieldValueException);

  /** Provide float value [0,inf) from inputOutput SFFloat field named "intensity". */
  float getIntensity ();

  /** Assign float value [0,inf) to inputOutput SFFloat field named "intensity". */
  void setIntensity (float value) throw (InvalidFieldValueException);

  /** Provide bool value from inputOutput SFBool field named "on". */
  bool getOn ();

  /** Assign bool value to inputOutput SFBool field named "on". */
  void setOn (bool value);

  /** Provide bool value from inputOutput SFBool field named "shadows". */
  bool getShadows ();

  /** Assign bool value to inputOutput SFBool field named "shadows". */
  void setShadows (bool value);

  /** Provide float value from inputOutput SFFloat field named "shadowIntensity". */
  float getShadowIntensity ();

  /** Assign float value to inputOutput SFFloat field named "shadowIntensity". */
  void setShadowIntensity (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DMaterialNode defines an abstract node class that extends classs X3DAppearanceChildNode and X3DNode.
  * Base type for all Material nodes. */

class X3DMaterialNode : public X3DAppearanceChildNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DNBodyCollidableNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * The X3DNBodyCollidableNode abstract node type represents objects that act as the interface between the rigid body physics, collision geometry proxy, and renderable objects in the scene graph hierarchy. */

class X3DNBodyCollidableNode : public X3DChildNode, X3DBoundedObject
{
  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  float* getBboxCenter ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void setBboxCenter (float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  float* getBboxSize ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void setBboxSize (float* value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  void setVisible (bool value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide 4-tuple float* value in radians from inputOutput SFRotation field named "rotation". */
  float* getRotation ();

  /** Assign 4-tuple float* value in radians to inputOutput SFRotation field named "rotation". */
  void setRotation (float* value);

  /** Provide 3-tuple float* value from inputOutput SFVec3f field named "translation". */
  float* getTranslation ();

  /** Assign 3-tuple float* value to inputOutput SFVec3f field named "translation". */
  void setTranslation (float* value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DNBodyCollisionSpaceNode defines an abstract node class that extends class X3DNode.
  * The X3DNBodyCollisionSpaceNode abstract node type represents objects that act as a self-contained spatial collection of objects that can interact through collision detection routines. */

class X3DNBodyCollisionSpaceNode : public X3DNode, X3DBoundedObject
{
  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  float* getBboxCenter ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void setBboxCenter (float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  float* getBboxSize ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void setBboxSize (float* value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  void setVisible (bool value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DNetworkSensorNode defines an abstract node class that extends classs X3DSensorNode, X3DChildNode, and X3DNode.
  * Base typefor all sensors that generate events based on network activity. */

class X3DNetworkSensorNode : public X3DSensorNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DNode defines an abstract node class.
  * All instantiable nodes implement X3DNode, which corresponds to SFNode type in the X3D specification. */

class X3DNode
{
  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Dispose of this node's resources. */
  void dispose();

  /** Get a field for this node by name. */
  X3DField* getField (MFString name);

  /** Get list of available fields in this node. */
  X3DFieldDefinition* getFieldDefinitions();

  /** Get the name of this node. */
  MFString getNodeName();

  /** Determine if node setup is completed. */
  bool isRealized ();

  /** Notify node that setup stage is complete. */
  void realize ();
}
;/** X3DNormalNode defines an abstract node class that extends classs X3DGeometricPropertyNode and X3DNode.
  * Base type for all normal node types in X3D. */

class X3DNormalNode : public X3DGeometricPropertyNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DNurbsControlCurveNode defines an abstract node class that extends class X3DNode.
  * Base type for all nodes that provide control curve information in 2D space. */

class X3DNurbsControlCurveNode : public X3DNode
{
  /** Provide 2-tuple double* value from inputOutput MFVec2d field named "controlPoint". */
  double* getControlPoint ();

  /** Provide number of 2-tuple primitive values in "controlPoint" array */
  int getNumControlPoint ();

  /** Assign 2-tuple double* value to inputOutput MFVec2d field named "controlPoint". */
  void setControlPoint (double* values);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DNurbsSurfaceGeometryNode defines an abstract node class that extends classs X3DParametricGeometryNode, X3DGeometryNode, and X3DNode.
  * Abstract geometry type for all types of NURBS surfaces. */

class X3DNurbsSurfaceGeometryNode : public X3DParametricGeometryNode
{
  /** Provide bool value from initializeOnly SFBool field named "uClosed". */
  bool getUClosed ();

  /** Assign bool value to initializeOnly SFBool field named "uClosed". */
  void setUClosed (bool value);

  /** Provide bool value from initializeOnly SFBool field named "vClosed". */
  bool getVClosed ();

  /** Assign bool value to initializeOnly SFBool field named "vClosed". */
  void setVClosed (bool value);

  /** Provide int value [0,inf) from initializeOnly SFInt32 field named "uDimension". */
  int getUDimension ();

  /** Assign int value [0,inf) to initializeOnly SFInt32 field named "uDimension". */
  void setUDimension (int value) throw (InvalidFieldValueException);

  /** Provide int value [0,inf) from initializeOnly SFInt32 field named "vDimension". */
  int getVDimension ();

  /** Assign int value [0,inf) to initializeOnly SFInt32 field named "vDimension". */
  void setVDimension (int value) throw (InvalidFieldValueException);

  /** Provide double* value from initializeOnly MFDouble field named "uKnot". */
  double* getUKnot ();

  /** Provide number of primitive values in "uKnot" array */
  int getNumUKnot ();

  /** Assign double* value to initializeOnly MFDouble field named "uKnot". */
  void setUKnot (double* values);

  /** Assign single double* value as the MFDouble array for initializeOnly field named "uKnot" */
  void setUKnot (double value);

  /** Provide double* value from initializeOnly MFDouble field named "vKnot". */
  double* getVKnot ();

  /** Provide number of primitive values in "vKnot" array */
  int getNumVKnot ();

  /** Assign double* value to initializeOnly MFDouble field named "vKnot". */
  void setVKnot (double* values);

  /** Assign single double* value as the MFDouble array for initializeOnly field named "vKnot" */
  void setVKnot (double value);

  /** Provide int value [2,inf) from initializeOnly SFInt32 field named "uOrder". */
  int getUOrder ();

  /** Assign int value [2,inf) to initializeOnly SFInt32 field named "uOrder". */
  void setUOrder (int value) throw (InvalidFieldValueException);

  /** Provide int value [2,inf) from initializeOnly SFInt32 field named "vOrder". */
  int getVOrder ();

  /** Assign int value [2,inf) to initializeOnly SFInt32 field named "vOrder". */
  void setVOrder (int value) throw (InvalidFieldValueException);

  /** Provide int value from inputOutput SFInt32 field named "uTessellation". */
  int getUTessellation ();

  /** Assign int value to inputOutput SFInt32 field named "uTessellation". */
  void setUTessellation (int value);

  /** Provide int value from inputOutput SFInt32 field named "vTessellation". */
  int getVTessellation ();

  /** Assign int value to inputOutput SFInt32 field named "vTessellation". */
  void setVTessellation (int value);

  /** Provide double* value (-inf,inf) from inputOutput MFDouble field named "weight". */
  double* getWeight ();

  /** Provide number of primitive values in "weight" array */
  int getNumWeight ();

  /** Assign double* value (-inf,inf) to inputOutput MFDouble field named "weight". */
  void setWeight (double* values);

  /** Assign single double* value (-inf,inf) as the MFDouble array for inputOutput field named "weight" */
  void setWeight (double value);

  /** Provide bool value from inputOutput SFBool field named "solid". */
  bool getSolid ();

  /** Assign bool value to inputOutput SFBool field named "solid". */
  void setSolid (bool value);

  /** Provide X3DCoordinateNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DCoordinateNode type field named "controlPoint". */
  X3DNode* getControlPoint ();

  /** Assign X3DCoordinateNode value (using a properly typed node) to inputOutput X3DCoordinateNode type field named "controlPoint". */
  void setControlPoint (X3DCoordinateNode node);

  /** Assign X3DCoordinateNode value (using a properly typed protoInstance) */
  void setControlPoint (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DSingleTextureCoordinateNode|NurbsTextureCoordinate value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DSingleTextureCoordinateNode|NurbsTextureCoordinate type field named "texCoord". */
  X3DNode* getTexCoord ();

  /** Assign X3DSingleTextureCoordinateNode|NurbsTextureCoordinate value (using a properly typed node) to inputOutput X3DSingleTextureCoordinateNode|NurbsTextureCoordinate type field named "texCoord". */
  void setTexCoord (X3DNode node);

  /** Assign X3DSingleTextureCoordinateNode|NurbsTextureCoordinate value (using a properly typed protoInstance) */
  void setTexCoord (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DOneSidedMaterialNode defines an abstract node class that extends classs X3DMaterialNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for material nodes that describe how the shape looks like from one side. A different number of contanied texture nodes are allowed by each of the implementing nodes. */

class X3DOneSidedMaterialNode : public X3DMaterialNode
{
  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "emissiveColor". */
  float* getEmissiveColor ();

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "emissiveColor". */
  void setEmissiveColor (float* color) throw (InvalidFieldValueException);

  /** Provide MFString value from inputOutput SFString field named "emissiveTextureMapping". */
  MFString getEmissiveTextureMapping ();

  /** Assign MFString value to inputOutput SFString field named "emissiveTextureMapping". */
  void setEmissiveTextureMapping (MFString value);

  /** Provide float value [0,inf) from inputOutput SFFloat field named "normalScale". */
  float getNormalScale ();

  /** Assign float value [0,inf) to inputOutput SFFloat field named "normalScale". */
  void setNormalScale (float value) throw (InvalidFieldValueException);

  /** Provide MFString value from inputOutput SFString field named "normalTextureMapping". */
  MFString getNormalTextureMapping ();

  /** Assign MFString value to inputOutput SFString field named "normalTextureMapping". */
  void setNormalTextureMapping (MFString value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DParametricGeometryNode defines an abstract node class that extends classs X3DGeometryNode and X3DNode.
  * Base type for all geometry node types that are created parametrically and use control points to describe the final shape of the surface. */

class X3DParametricGeometryNode : public X3DGeometryNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DParticleEmitterNode defines an abstract node class that extends class X3DNode.
  * The X3DParticleEmitterNode abstract type represents any node that is an emitter of particles. */

class X3DParticleEmitterNode : public X3DNode
{
  /** Provide bool value from inputOutput SFBool field named "on". */
  bool getOn ();

  /** Assign bool value to inputOutput SFBool field named "on". */
  void setOn (bool value);

  /** Provide float value [0,inf) from inputOutput SFFloat field named "speed". */
  float getSpeed ();

  /** Assign float value [0,inf) to inputOutput SFFloat field named "speed". */
  void setSpeed (float value) throw (InvalidFieldValueException);

  /** Provide float value [0,inf) from inputOutput SFFloat field named "variation". */
  float getVariation ();

  /** Assign float value [0,inf) to inputOutput SFFloat field named "variation". */
  void setVariation (float value) throw (InvalidFieldValueException);

  /** Provide float value [0,inf) from inputOutput SFFloat field named "mass". */
  float getMass ();

  /** Assign float value [0,inf) to inputOutput SFFloat field named "mass". */
  void setMass (float value) throw (InvalidFieldValueException);

  /** Provide float value [0,inf) from inputOutput SFFloat field named "surfaceArea". */
  float getSurfaceArea ();

  /** Assign float value [0,inf) to inputOutput SFFloat field named "surfaceArea". */
  void setSurfaceArea (float value) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DParticlePhysicsModelNode defines an abstract node class that extends class X3DNode.
  * The X3DParticlePhysicsModelNode abstract type represents any node that applies a form of constraints on the particles after they have been generated. */

class X3DParticlePhysicsModelNode : public X3DNode
{
  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DPickSensorNode defines an abstract node class that extends classs X3DSensorNode, X3DChildNode, and X3DNode.
  * The X3DPickSensorNode abstract node type is the base node type that represents the lowest common denominator of picking capabilities. */

class X3DPickSensorNode : public X3DSensorNode
{
  /** Provide MFString value from inputOutput SFString field named "matchCriterion". */
  MFString getMatchCriterion ();

  /** Assign MFString value to inputOutput SFString field named "matchCriterion". */
  void setMatchCriterion (MFString value);

  /** Provide MFString* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  MFString* getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  int getNumObjectType ();

  /** Assign MFString* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void setObjectType (MFString* values) throw (InvalidFieldValueException);

  /** Provide MFString value from initializeOnly SFString field named "intersectionType". */
  MFString getIntersectionType ();

  /** Assign MFString value to initializeOnly SFString field named "intersectionType". */
  void setIntersectionType (MFString value);

  /** Provide MFString value from initializeOnly SFString field named "sortOrder". */
  MFString getSortOrder ();

  /** Assign MFString value to initializeOnly SFString field named "sortOrder". */
  void setSortOrder (MFString value);

  /** Provide MFString value from initializeOnly SFString field named "intersectionType". */
  MFString getIntersectionType ();

  /** Assign MFString value to initializeOnly SFString field named "intersectionType". */
  void setIntersectionType (MFString value);

  /** Provide MFString value from inputOutput SFString field named "matchCriterion". */
  MFString getMatchCriterion ();

  /** Assign MFString value to inputOutput SFString field named "matchCriterion". */
  void setMatchCriterion (MFString value);

  /** Provide MFString* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  MFString* getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  int getNumObjectType ();

  /** Assign MFString* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void setObjectType (MFString* values);

  /** Assign single MFString* value ["ALL","NONE","TERRAIN",...] as the MFString array for inputOutput field named "objectType" */
  void setObjectType (MFString value);

  /** Provide MFString value from initializeOnly SFString field named "sortOrder". */
  MFString getSortOrder ();

  /** Assign MFString value to initializeOnly SFString field named "sortOrder". */
  void setSortOrder (MFString value);

  /** Provide X3DGroupingNode|X3DShapeNode|Inline* value (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DGroupingNode|X3DShapeNode|Inline type field named "pickTarget". */
  X3DNode* getPickTarget ();

  /** Provide number of nodes in "pickTarget" array */
  int getNumPickTarget ();

  /** Assign X3DGroupingNode|X3DShapeNode|Inline* value (using a properly typed node array) to inputOutput X3DGroupingNode|X3DShapeNode|Inline type field named "pickTarget". */
  void setPickTarget (X3DNode nodes);

  /** Assign single X3DNode value (using a properly typed node MFNode) as the MFNode array for inputOutput field named "pickTarget" */
  void setPickTarget (X3DNode node);

  /** Assign X3DGroupingNode|X3DShapeNode|Inline* value (using a properly typed protoInstance array) to inputOutput X3DGroupingNode|X3DShapeNode|Inline type field named "pickTarget". */
  void setPickTarget (X3DPrototypeInstance node);

  /** Provide X3DChildNode* value (using a properly typed node array or X3DPrototypeInstance array) from outputOnly X3DChildNode type field named "pickedGeometry". */
  X3DNode* getPickedGeometry ();

  /** Provide number of nodes in "pickedGeometry" array */
  int getNumPickedGeometry ();

  /** Provide X3DGeometryNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DGeometryNode type field named "pickingGeometry". */
  X3DNode* getPickingGeometry ();

  /** Assign X3DGeometryNode value (using a properly typed node) to inputOutput X3DGeometryNode type field named "pickingGeometry". */
  void setPickingGeometry (X3DGeometryNode node);

  /** Assign X3DGeometryNode value (using a properly typed protoInstance) */
  void setPickingGeometry (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DPointingDeviceSensorNode defines an abstract node class that extends classs X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all pointing device sensors. */

class X3DPointingDeviceSensorNode : public X3DSensorNode
{
  /** Provide bool value from outputOnly SFBool field named "isOver". */
  bool getIsOver ();

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DProductStructureChildNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Base type marking nodes that are valid product structure children for the CADGeometry component. */

class X3DProductStructureChildNode : public X3DChildNode
{
  /** Provide MFString value from inputOutput SFString field named "name". */
  MFString getName ();

  /** Assign MFString value to inputOutput SFString field named "name". */
  void setName (MFString value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DPrototypeInstance defines an abstract class.
  * Base type for all prototype instances. Note that direct children nodes are disallowed, instead let fieldValue with type SFNode/MFNode contain them. Current practice is that, if desired, prototype authors must explicitly add the metadata SFNode field in the ProtoInterface. */

class X3DPrototypeInstance : public X3DNode
{
  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DRigidJointNode defines an abstract node class that extends class X3DNode.
  * The X3DRigidJointNode abstract node type is the base type for all joint types. */

class X3DRigidJointNode : public X3DNode
{
  /** Provide MFString* value from inputOutput MFString field named "forceOutput". */
  MFString* getForceOutput ();

  /** Provide number of primitive values in "forceOutput" array */
  int getNumForceOutput ();

  /** Assign MFString* value to inputOutput MFString field named "forceOutput". */
  void setForceOutput (MFString* values);

  /** Provide MFString* value from inputOutput MFString field named "forceOutput". */
  MFString* getForceOutput ();

  /** Provide number of primitive values in "forceOutput" array */
  int getNumForceOutput ();

  /** Assign MFString* value to inputOutput MFString field named "forceOutput". */
  void setForceOutput (MFString* values);

  /** Assign single MFString* value as the MFString array for inputOutput field named "forceOutput" */
  void setForceOutput (MFString value);

  /** Provide RigidBody value (using a properly typed node or X3DPrototypeInstance) from inputOutput RigidBody type field named "body1". */
  X3DNode* getBody1 ();

  /** Assign RigidBody value (using a properly typed node) to inputOutput RigidBody type field named "body1". */
  void setBody1 (RigidBody node);

  /** Assign RigidBody value (using a properly typed protoInstance) */
  void setBody1 (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide RigidBody value (using a properly typed node or X3DPrototypeInstance) from inputOutput RigidBody type field named "body2". */
  X3DNode* getBody2 ();

  /** Assign RigidBody value (using a properly typed node) to inputOutput RigidBody type field named "body2". */
  void setBody2 (RigidBody node);

  /** Assign RigidBody value (using a properly typed protoInstance) */
  void setBody2 (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DScriptNode defines an abstract node class.
  * Base type for scripting nodes (but not shader nodes). */

class X3DScriptNode : public X3DChildNode, X3DUrlObject
{
  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide bool value from inputOutput SFBool field named "load". */
  bool getLoad ();

  /** Assign bool value to inputOutput SFBool field named "load". */
  void setLoad (bool value);

  /** Provide double value in seconds [0,inf) from inputOutput SFTime field named "autoRefresh". */
  double getAutoRefresh ();

  /** Assign double value in seconds [0,inf) to inputOutput SFTime field named "autoRefresh". */
  void setAutoRefresh (double timestamp) throw (InvalidFieldValueException);

  /** Provide double value in seconds [0,inf) from inputOutput SFTime field named "autoRefreshTimeLimit". */
  double getAutoRefreshTimeLimit ();

  /** Assign double value in seconds [0,inf) to inputOutput SFTime field named "autoRefreshTimeLimit". */
  void setAutoRefreshTimeLimit (double timestamp) throw (InvalidFieldValueException);

  /** Provide MFString* value from inputOutput MFString field named "url". */
  MFString* getUrl ();

  /** Provide number of primitive values in "url" array */
  int getNumUrl ();

  /** Assign MFString* value to inputOutput MFString field named "url". */
  void setUrl (MFString* values);

  /** Assign single MFString* value as the MFString array for inputOutput field named "url" */
  void setUrl (MFString value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DSensorNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Base type for all sensors. */

class X3DSensorNode : public X3DChildNode
{
  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DSequencerNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Base type from which all Sequencers are derived. */

class X3DSequencerNode : public X3DChildNode
{
  /** Assign bool value to inputOnly SFBool field named "next". */
  void setNext (bool value);

  /** Assign bool value to inputOnly SFBool field named "previous". */
  void setPrevious (bool value);

  /** Assign float value to inputOnly SFFloat field named "set_fraction". */
  void setFraction (float value);

  /** Provide float* value from inputOutput MFFloat field named "key". */
  float* getKey ();

  /** Provide number of primitive values in "key" array */
  int getNumKey ();

  /** Assign float* value to inputOutput MFFloat field named "key". */
  void setKey (float* values);

  /** Assign single float* value as the MFFloat array for inputOutput field named "key" */
  void setKey (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DShaderNode defines an abstract node class that extends classs X3DAppearanceChildNode and X3DNode.
  * Base type for all nodes that specify a programmable shader. */

class X3DShaderNode : public X3DAppearanceChildNode
{
  /** Provide MFString value from initializeOnly SFString field named "language". */
  MFString getLanguage ();

  /** Assign MFString value to initializeOnly SFString field named "language". */
  void setLanguage (MFString value);

  /** Assign bool value to inputOnly SFBool field named "activate". */
  void setActivate (bool value);

  /** Provide bool value from outputOnly SFBool field named "isSelected". */
  bool getIsSelected ();

  /** Provide bool value from outputOnly SFBool field named "isValid". */
  bool getIsValid ();

  /** Provide MFString value from initializeOnly SFString field named "language". */
  MFString getLanguage ();

  /** Assign MFString value to initializeOnly SFString field named "language". */
  void setLanguage (MFString value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DShapeNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Base type for all Shape nodes. */

class X3DShapeNode : public X3DChildNode, X3DBoundedObject
{
  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  float* getBboxCenter ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void setBboxCenter (float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  float* getBboxSize ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void setBboxSize (float* value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "castShadow". */
  bool getCastShadow ();

  /** Assign bool value to inputOutput SFBool field named "castShadow". */
  void setCastShadow (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  void setVisible (bool value);

  /** Provide X3DAppearanceNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DAppearanceNode type field named "appearance". */
  X3DNode* getAppearance ();

  /** Assign X3DAppearanceNode value (using a properly typed node) to inputOutput X3DAppearanceNode type field named "appearance". */
  void setAppearance (X3DAppearanceNode node);

  /** Assign X3DAppearanceNode value (using a properly typed protoInstance) */
  void setAppearance (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DGeometryNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DGeometryNode type field named "geometry". */
  X3DNode* getGeometry ();

  /** Assign X3DGeometryNode value (using a properly typed node) to inputOutput X3DGeometryNode type field named "geometry". */
  void setGeometry (X3DGeometryNode node);

  /** Assign X3DGeometryNode value (using a properly typed protoInstance) */
  void setGeometry (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DSingleTextureCoordinateNode defines an abstract node class that extends classs X3DTextureCoordinateNode, X3DGeometricPropertyNode, and X3DNode.
  * Base type for all texture coordinate nodes which specify texture coordinates for a single texture. */

class X3DSingleTextureCoordinateNode : public X3DTextureCoordinateNode
{
  /** Provide MFString value from inputOutput SFString field named "mapping". */
  MFString getMapping ();

  /** Assign MFString value to inputOutput SFString field named "mapping". */
  void setMapping (MFString value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DSingleTextureNode defines an abstract node class that extends classs X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all texture node types that define a single texture. A single texture can be used to influence a parameter of various material nodes in the Shape component, and it can be a child of MultiTexture. */

class X3DSingleTextureNode : public X3DTextureNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DSingleTextureTransformNode defines an abstract node class that extends classs X3DTextureTransformNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all texture transform nodes which specify texture coordinate transformation for a single texture. */

class X3DSingleTextureTransformNode : public X3DTextureTransformNode
{
  /** Provide MFString value from inputOutput SFString field named "mapping". */
  MFString getMapping ();

  /** Assign MFString value to inputOutput SFString field named "mapping". */
  void setMapping (MFString value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DSoundChannelNode defines an abstract node class that extends classs X3DSoundNode, X3DChildNode, and X3DNode.
  * Base type for all sound destination nodes, which represent the final destination of an audio signal and are what the user can ultimately hear. */

class X3DSoundChannelNode : public X3DSoundNode
{
  /** Provide int value from outputOnly SFInt32 field named "channelCount". */
  int getChannelCount ();

  /** Provide MFString value from inputOutput SFString field named "channelCountMode". */
  MFString getChannelCountMode ();

  /** Assign MFString value to inputOutput SFString field named "channelCountMode". */
  void setChannelCountMode (MFString value);

  /** Provide MFString value from inputOutput SFString field named "channelInterpretation". */
  MFString getChannelInterpretation ();

  /** Assign MFString value to inputOutput SFString field named "channelInterpretation". */
  void setChannelInterpretation (MFString value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  float getGain ();

  /** Assign float value to inputOutput SFFloat field named "gain". */
  void setGain (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DSoundDestinationNode defines an abstract node class that extends classs X3DSoundNode, X3DChildNode, and X3DNode.
  * Base type for all sound destination nodes, which represent the final destination of an audio signal and are what the user can ultimately hear. */

class X3DSoundDestinationNode : public X3DSoundNode
{
  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide int value from outputOnly SFInt32 field named "channelCount". */
  int getChannelCount ();

  /** Provide MFString value from inputOutput SFString field named "channelCountMode". */
  MFString getChannelCountMode ();

  /** Assign MFString value to inputOutput SFString field named "channelCountMode". */
  void setChannelCountMode (MFString value);

  /** Provide MFString value from inputOutput SFString field named "channelInterpretation". */
  MFString getChannelInterpretation ();

  /** Assign MFString value to inputOutput SFString field named "channelInterpretation". */
  void setChannelInterpretation (MFString value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  float getGain ();

  /** Assign float value to inputOutput SFFloat field named "gain". */
  void setGain (float value);

  /** Provide MFString value from inputOutput SFString field named "mediaDeviceID". */
  MFString getMediaDeviceID ();

  /** Assign MFString value to inputOutput SFString field named "mediaDeviceID". */
  void setMediaDeviceID (MFString value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DSoundNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Base type for all sound nodes. */

class X3DSoundNode : public X3DChildNode
{
  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DSoundProcessingNode defines an abstract node class that extends classs X3DTimeDependentNode, X3DChildNode, and X3DNode.
  * Base type for all sound processing nodes, which are used to enhance audio with filtering, delaying, changing gain, etc. */

class X3DSoundProcessingNode : public X3DTimeDependentNode, X3DSoundNode
{
  /** Provide int value from outputOnly SFInt32 field named "channelCount". */
  int getChannelCount ();

  /** Provide MFString value from inputOutput SFString field named "channelCountMode". */
  MFString getChannelCountMode ();

  /** Assign MFString value to inputOutput SFString field named "channelCountMode". */
  void setChannelCountMode (MFString value);

  /** Provide MFString value from inputOutput SFString field named "channelInterpretation". */
  MFString getChannelInterpretation ();

  /** Assign MFString value to inputOutput SFString field named "channelInterpretation". */
  void setChannelInterpretation (MFString value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  float getGain ();

  /** Assign float value to inputOutput SFFloat field named "gain". */
  void setGain (float value);

  /** Provide double value in seconds [0,inf) from inputOutput SFTime field named "tailTime". */
  double getTailTime ();

  /** Assign double value in seconds [0,inf) to inputOutput SFTime field named "tailTime". */
  void setTailTime (double timestamp) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide double value in seconds [0,inf) from outputOnly SFTime field named "elapsedTime". */
  double getElapsedTime ();

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide bool value from outputOnly SFBool field named "isPaused". */
  bool getIsPaused ();

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide double value in seconds from inputOutput SFTime field named "pauseTime". */
  double getPauseTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "pauseTime". */
  void setPauseTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "resumeTime". */
  double getResumeTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "resumeTime". */
  void setResumeTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "startTime". */
  double getStartTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "startTime". */
  void setStartTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "stopTime". */
  double getStopTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "stopTime". */
  void setStopTime (double timestamp);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DSoundSourceNode defines an abstract node class that extends classs X3DTimeDependentNode, X3DChildNode, and X3DNode.
  * Nodes implementing X3DSoundSourceNode provide signal inputs to the audio graph. */

class X3DSoundSourceNode : public X3DTimeDependentNode, X3DSoundNode
{
  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  float getGain ();

  /** Assign float value to inputOutput SFFloat field named "gain". */
  void setGain (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide double value in seconds [0,inf) from outputOnly SFTime field named "elapsedTime". */
  double getElapsedTime ();

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide bool value from outputOnly SFBool field named "isPaused". */
  bool getIsPaused ();

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide double value in seconds from inputOutput SFTime field named "pauseTime". */
  double getPauseTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "pauseTime". */
  void setPauseTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "resumeTime". */
  double getResumeTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "resumeTime". */
  void setResumeTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "startTime". */
  double getStartTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "startTime". */
  void setStartTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "stopTime". */
  double getStopTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "stopTime". */
  void setStopTime (double timestamp);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DTexture2DNode defines an abstract node class that extends classs X3DSingleTextureNode, X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all nodes which specify 2D sources for texture images. */

class X3DTexture2DNode : public X3DSingleTextureNode
{
  /** Provide bool value from initializeOnly SFBool field named "repeatS". */
  bool getRepeatS ();

  /** Assign bool value to initializeOnly SFBool field named "repeatS". */
  void setRepeatS (bool value);

  /** Provide bool value from initializeOnly SFBool field named "repeatT". */
  bool getRepeatT ();

  /** Assign bool value to initializeOnly SFBool field named "repeatT". */
  void setRepeatT (bool value);

  /** Provide TextureProperties value (using a properly typed node or X3DPrototypeInstance) from initializeOnly TextureProperties type field named "textureProperties". */
  X3DNode* getTextureProperties ();

  /** Assign TextureProperties value (using a properly typed node) to initializeOnly TextureProperties type field named "textureProperties". */
  void setTextureProperties (TextureProperties node);

  /** Assign TextureProperties value (using a properly typed protoInstance) */
  void setTextureProperties (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DTexture3DNode defines an abstract node class that extends classs X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all nodes that specify 3D sources for texture images. */

class X3DTexture3DNode : public X3DTextureNode
{
  /** Provide bool value from initializeOnly SFBool field named "repeatS". */
  bool getRepeatS ();

  /** Assign bool value to initializeOnly SFBool field named "repeatS". */
  void setRepeatS (bool value);

  /** Provide bool value from initializeOnly SFBool field named "repeatT". */
  bool getRepeatT ();

  /** Assign bool value to initializeOnly SFBool field named "repeatT". */
  void setRepeatT (bool value);

  /** Provide bool value from initializeOnly SFBool field named "repeatR". */
  bool getRepeatR ();

  /** Assign bool value to initializeOnly SFBool field named "repeatR". */
  void setRepeatR (bool value);

  /** Provide TextureProperties value (using a properly typed node or X3DPrototypeInstance) from initializeOnly TextureProperties type field named "textureProperties". */
  X3DNode* getTextureProperties ();

  /** Assign TextureProperties value (using a properly typed node) to initializeOnly TextureProperties type field named "textureProperties". */
  void setTextureProperties (TextureProperties node);

  /** Assign TextureProperties value (using a properly typed protoInstance) */
  void setTextureProperties (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DTextureCoordinateNode defines an abstract node class that extends classs X3DGeometricPropertyNode and X3DNode.
  * Base type for all nodes which specify texture coordinates. */

class X3DTextureCoordinateNode : public X3DGeometricPropertyNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DTextureNode defines an abstract node class that extends classs X3DAppearanceChildNode and X3DNode.
  * Base type for all nodes which specify sources for texture images. */

class X3DTextureNode : public X3DAppearanceChildNode
{
  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DTextureProjectorNode defines an abstract node class that extends classs X3DLightNode, X3DChildNode, and X3DNode.
  * Base type for all node types that specify texture projector nodes, which provide a form of lighting. */

class X3DTextureProjectorNode : public X3DLightNode
{
  /** Provide float value (0,inf) from outputOnly SFFloat field named "aspectRatio". */
  float getAspectRatio ();

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide 3-tuple float* value from inputOutput SFVec3f field named "direction". */
  float* getDirection ();

  /** Assign 3-tuple float* value to inputOutput SFVec3f field named "direction". */
  void setDirection (float* value);

  /** Provide float value [-1,inf) from inputOutput SFFloat field named "farDistance". */
  float getFarDistance ();

  /** Assign float value [-1,inf) to inputOutput SFFloat field named "farDistance". */
  void setFarDistance (float value) throw (InvalidFieldValueException);

  /** Provide bool value from inputOutput SFBool field named "global". */
  bool getGlobal ();

  /** Assign bool value to inputOutput SFBool field named "global". */
  void setGlobal (bool value);

  /** Provide 3-tuple float* value from inputOutput SFVec3f field named "location". */
  float* getLocation ();

  /** Assign 3-tuple float* value to inputOutput SFVec3f field named "location". */
  void setLocation (float* value);

  /** Provide float value [-1,inf) from inputOutput SFFloat field named "nearDistance". */
  float getNearDistance ();

  /** Assign float value [-1,inf) to inputOutput SFFloat field named "nearDistance". */
  void setNearDistance (float value) throw (InvalidFieldValueException);

  /** Provide X3DTexture2DNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DTexture2DNode type field named "texture". */
  X3DNode* getTexture ();

  /** Assign X3DTexture2DNode value (using a properly typed node) to inputOutput X3DTexture2DNode type field named "texture". */
  void setTexture (X3DTexture2DNode node);

  /** Assign X3DTexture2DNode value (using a properly typed protoInstance) */
  void setTexture (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide float value from inputOutput SFFloat field named "ambientIntensity". */
  float getAmbientIntensity ();

  /** Assign float value to inputOutput SFFloat field named "ambientIntensity". */
  void setAmbientIntensity (float value);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "color". */
  float* getColor ();

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "color". */
  void setColor (float* color) throw (InvalidFieldValueException);

  /** Provide float value [0,inf) from inputOutput SFFloat field named "intensity". */
  float getIntensity ();

  /** Assign float value [0,inf) to inputOutput SFFloat field named "intensity". */
  void setIntensity (float value) throw (InvalidFieldValueException);

  /** Provide bool value from inputOutput SFBool field named "on". */
  bool getOn ();

  /** Assign bool value to inputOutput SFBool field named "on". */
  void setOn (bool value);

  /** Provide bool value from inputOutput SFBool field named "shadows". */
  bool getShadows ();

  /** Assign bool value to inputOutput SFBool field named "shadows". */
  void setShadows (bool value);

  /** Provide float value from inputOutput SFFloat field named "shadowIntensity". */
  float getShadowIntensity ();

  /** Assign float value to inputOutput SFFloat field named "shadowIntensity". */
  void setShadowIntensity (float value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DTextureTransformNode defines an abstract node class that extends classs X3DAppearanceChildNode and X3DNode.
  * Base type for all nodes which specify a transformation of texture coordinates. */

class X3DTextureTransformNode : public X3DAppearanceChildNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DTimeDependentNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Base type from which all time-dependent nodes are derived. */

class X3DTimeDependentNode : public X3DChildNode
{
  /** Provide double value in seconds [0,inf) from outputOnly SFTime field named "elapsedTime". */
  double getElapsedTime ();

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide bool value from outputOnly SFBool field named "isPaused". */
  bool getIsPaused ();

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide double value in seconds from inputOutput SFTime field named "pauseTime". */
  double getPauseTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "pauseTime". */
  void setPauseTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "resumeTime". */
  double getResumeTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "resumeTime". */
  void setResumeTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "startTime". */
  double getStartTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "startTime". */
  void setStartTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "stopTime". */
  double getStopTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "stopTime". */
  void setStopTime (double timestamp);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DTouchSensorNode defines an abstract node class that extends classs X3DPointingDeviceSensorNode, X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all touch-style pointing device sensors. */

class X3DTouchSensorNode : public X3DPointingDeviceSensorNode
{
  /** Provide double value in seconds from outputOnly SFTime field named "touchTime". */
  double getTouchTime ();

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isOver". */
  bool getIsOver ();

  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DTriggerNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * Base type from which all trigger nodes are derived. */

class X3DTriggerNode : public X3DChildNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DVertexAttributeNode defines an abstract node class that extends classs X3DGeometricPropertyNode and X3DNode.
  * Base type for all nodes that specify per-vertex attribute information to the shader. */

class X3DVertexAttributeNode : public X3DGeometricPropertyNode
{
  /** Provide MFString value from inputOutput SFString field named "name". */
  MFString getName ();

  /** Assign MFString value to inputOutput SFString field named "name". */
  void setName (MFString value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DViewpointNode defines an abstract node class that extends classs X3DBindableNode, X3DChildNode, and X3DNode.
  * Node type X3DViewpointNode defines a specific location in the local coordinate system from which the user may view the scene, and also defines a viewpoint binding stack. */

class X3DViewpointNode : public X3DBindableNode
{
  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide bool value from inputOutput SFBool field named "jump". */
  bool getJump ();

  /** Assign bool value to inputOutput SFBool field named "jump". */
  void setJump (bool value);

  /** Provide 4-tuple float* value in radians from inputOutput SFRotation field named "orientation". */
  float* getOrientation ();

  /** Assign 4-tuple float* value in radians to inputOutput SFRotation field named "orientation". */
  void setOrientation (float* value);

  /** Provide bool value from inputOutput SFBool field named "retainUserOffsets". */
  bool getRetainUserOffsets ();

  /** Assign bool value to inputOutput SFBool field named "retainUserOffsets". */
  void setRetainUserOffsets (bool value);

  /** Provide float value from inputOutput SFFloat field named "farDistance". */
  float getFarDistance ();

  /** Assign float value to inputOutput SFFloat field named "farDistance". */
  void setFarDistance (float value);

  /** Provide float value from inputOutput SFFloat field named "nearDistance". */
  float getNearDistance ();

  /** Assign float value to inputOutput SFFloat field named "nearDistance". */
  void setNearDistance (float value);

  /** Provide bool value from inputOutput SFBool field named "viewAll". */
  bool getViewAll ();

  /** Assign bool value to inputOutput SFBool field named "viewAll". */
  void setViewAll (bool value);

  /** Provide NavigationInfo value (using a properly typed node or X3DPrototypeInstance) from inputOutput NavigationInfo type field named "navigationInfo". */
  X3DNode* getNavigationInfo ();

  /** Assign NavigationInfo value (using a properly typed node) to inputOutput NavigationInfo type field named "navigationInfo". */
  void setNavigationInfo (NavigationInfo node);

  /** Assign NavigationInfo value (using a properly typed protoInstance) */
  void setNavigationInfo (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  // ===== methods for fields inherited from parent interfaces =====

  /** Assign bool value to inputOnly SFBool field named "set_bind". */
  void setBind (bool value);

  /** Provide double value in seconds from outputOnly SFTime field named "bindTime". */
  double getBindTime ();

  /** Provide bool value from outputOnly SFBool field named "isBound". */
  bool getIsBound ();

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DViewportNode defines an abstract node class that extends classs X3DGroupingNode, X3DChildNode, and X3DNode.
  * The X3DViewportNode abstract node type is the base node type for viewport nodes. */

class X3DViewportNode : public X3DGroupingNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  float* getBboxCenter ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void setBboxCenter (float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  float* getBboxSize ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void setBboxSize (float* value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  void setVisible (bool value);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren (X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node MFNode) as the MFNode array for inputOnly field named "addChildren" */
  void addChildren (X3DChildNode node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren (X3DNode nodes);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren (X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node MFNode) as the MFNode array for inputOnly field named "removeChildren" */
  void removeChildren (X3DChildNode node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren (X3DNode nodes);

  /** Provide X3DChildNode* value (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DChildNode type field named "children". */
  X3DNode* getChildren ();

  /** Provide number of nodes in "children" array */
  int getNumChildren ();

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  void setChildren (X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node MFNode) as the MFNode array for inputOutput field named "children" */
  void setChildren (X3DChildNode node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOutput X3DChildNode type field named "children". */
  void setChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  void setChildren (X3DNode nodes);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DVolumeDataNode defines an abstract node class that extends classs X3DChildNode and X3DNode.
  * The X3DVolumeDataNode abstract node type is the base type for all node types that describe volumetric data to be rendered. */

class X3DVolumeDataNode : public X3DChildNode, X3DBoundedObject
{
  /** Provide 3-tuple float* value (-inf,inf) from inputOutput SFVec3f field named "dimensions". */
  float* getDimensions ();

  /** Assign 3-tuple float* value (-inf,inf) to inputOutput SFVec3f field named "dimensions". */
  void setDimensions (float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  float* getBboxCenter ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void setBboxCenter (float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  float* getBboxSize ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void setBboxSize (float* value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  void setVisible (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DVolumeRenderStyleNode defines an abstract node class that extends class X3DNode.
  * The X3DVolumeRenderStyleNode abstract node type is the base type for all node types that specify a specific visual rendering style to be used when rendering volume data. */

class X3DVolumeRenderStyleNode : public X3DNode
{
  /** Provide bool value from inputOutput SFBool field named "enabled". */
  bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  void setEnabled (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  X3DNode* getIS ();

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void setIS (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  X3DNode* getMetadata ();

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void setMetadata (X3DPrototypeInstance protoInstance) throw (InvalidFieldValueException);
}
;/** X3DBoundedObject defines an abstract class.
  * X3DBoundedObject indicates that bounding box values can be provided (or computed) to encompass this node and any children. */

class X3DBoundedObject
{
  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  float* getBboxCenter ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void setBboxCenter (float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  float* getBboxSize ();

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void setBboxSize (float* value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  void setVisible (bool value);
}
;/** X3DFogObject defines an abstract class.
  * Abstract type describing a node that influences the lighting equation through the use of fog semantics. */

class X3DFogObject
{
  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "color". */
  float* getColor ();

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "color". */
  void setColor (float* color) throw (InvalidFieldValueException);

  /** Provide MFString value from inputOutput SFString field named "fogType". */
  MFString getFogType ();

  /** Assign MFString value to inputOutput SFString field named "fogType". */
  void setFogType (MFString value);

  /** Provide float value [0,inf) from inputOutput SFFloat field named "visibilityRange". */
  float getVisibilityRange ();

  /** Assign float value [0,inf) to inputOutput SFFloat field named "visibilityRange". */
  void setVisibilityRange (float value) throw (InvalidFieldValueException);
}
;/** X3DMetadataObject defines an abstract class.
  * Each node inheriting the X3DMetadataObject interface contains a single array of strictly typed values: MFBool, MFInt32, MFFloat, MFDouble, MFString, or MFNode, the latter having children that are all Metadata nodes. */

class X3DMetadataObject
{
  /** Provide MFString value from inputOutput SFString field named "name". */
  MFString getName ();

  /** Assign MFString value to inputOutput SFString field named "name". */
  void setName (MFString value);

  /** Provide MFString value from inputOutput SFString field named "reference". */
  MFString getReference ();

  /** Assign MFString value to inputOutput SFString field named "reference". */
  void setReference (MFString value);
}
;/** X3DPickableObject defines an abstract class.
  * The X3DPickableObject abstract interface marks a node as being capable of having customized picking performed on its contents or children. */

class X3DPickableObject
{
  /** Provide MFString* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  MFString* getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  int getNumObjectType ();

  /** Assign MFString* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void setObjectType (MFString* values) throw (InvalidFieldValueException);

  /** Provide MFString* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  MFString* getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  int getNumObjectType ();

  /** Assign MFString* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void setObjectType (MFString* values);

  /** Assign single MFString* value ["ALL","NONE","TERRAIN",...] as the MFString array for inputOutput field named "objectType" */
  void setObjectType (MFString value);

  /** Provide bool value from inputOutput SFBool field named "pickable". */
  bool getPickable ();

  /** Assign bool value to inputOutput SFBool field named "pickable". */
  void setPickable (bool value);
}
;/** X3DProgrammableShaderObject defines an abstract class.
  * Base type for all nodes that specify arbitrary fields for interfacing with per-object attribute values. */

class X3DProgrammableShaderObject
{}
;/** X3DUrlObject defines an abstract class.
  * X3DUrlObject indicates that a node has content loaded from a Uniform Resource Locator (URL) and can be tracked via a LoadSensor. Such child nodes have containerField='children' to indicate their relationship to the parent LoadSensor node. */

class X3DUrlObject
{
  /** Provide MFString value from inputOutput SFString field named "description". */
  MFString getDescription ();

  /** Assign MFString value to inputOutput SFString field named "description". */
  void setDescription (MFString value);

  /** Provide bool value from inputOutput SFBool field named "load". */
  bool getLoad ();

  /** Assign bool value to inputOutput SFBool field named "load". */
  void setLoad (bool value);

  /** Provide double value in seconds [0,inf) from inputOutput SFTime field named "autoRefresh". */
  double getAutoRefresh ();

  /** Assign double value in seconds [0,inf) to inputOutput SFTime field named "autoRefresh". */
  void setAutoRefresh (double timestamp) throw (InvalidFieldValueException);

  /** Provide double value in seconds [0,inf) from inputOutput SFTime field named "autoRefreshTimeLimit". */
  double getAutoRefreshTimeLimit ();

  /** Assign double value in seconds [0,inf) to inputOutput SFTime field named "autoRefreshTimeLimit". */
  void setAutoRefreshTimeLimit (double timestamp) throw (InvalidFieldValueException);

  /** Provide MFString* value from inputOutput MFString field named "url". */
  MFString* getUrl ();

  /** Provide number of primitive values in "url" array */
  int getNumUrl ();

  /** Assign MFString* value to inputOutput MFString field named "url". */
  void setUrl (MFString* values);

  /** Assign single MFString* value as the MFString array for inputOutput field named "url" */
  void setUrl (MFString value);
}
;
enum X3DFieldTypes {
	int INPUT_ONLY = 1;
	int INITIALIZE_ONLY = 2;
	int INPUT_OUTPUT = 3;
	int OUTPUT_ONLY = 4;

	int SFBOOL = 1;
	int MFBOOL = 2;
	int SFCOLOR = 21;
	int MFCOLOR = 22;
	int SFCOLORRGBA = 23;
	int MFCOLORRGBA = 24;
	int SFDOUBLE = 7;
	int MFDOUBLE = 8;
	int SFFLOAT = 5;
	int MFFLOAT = 6;
	int SFIMAGE = 25;
	int MFIMAGE = 26;
	int SFINT32 = 3;
	int MFINT32 = 4;
	int SFNODE = 11;
	int MFNODE = 12;
	int SFROTATION = 19;
	int MFROTATION = 20;
	int SFSTRING = 27;
	int MFSTRING = 28;
	int SFTIME = 9;
	int MFTIME = 10;
	int SFVEC2F = 13;
	int MFVEC2F = 14;
	int SFVEC3F = 15;
	int MFVEC3F = 16;
	int SFVEC3D = 17;
	int MFVEC3D = 18;
}
					;
class X3DFieldEvent : public EventObject {

public:
	X3DFieldEvent(CObject src, double ts, CObject data);

	double getTime();

	CObject getData();
}
					;
class X3DFieldEventListener : public EventListener {
	void readableFieldChanged(X3DFieldEvent evt);
}
					;
class X3DFieldDefinition {
public:
	MFString getName();

	int getAccessType();

	int getFieldType();

	MFString getFieldTypeString();
}
					;
class X3DField {

public:
	X3DFieldDefinition getDefinition();

	bool isReadable();

	bool isWritable();

	void addX3DEventListener(X3DFieldEventListener l);

	void removeX3DEventListener(X3DFieldEventListener l);

	void setUserData(CObject data);

	CObject getUserData();
}
					;
class MField : public X3DField {

public:
	int size();

	void clear();

	void remove(int index);
}
					;/** SFBool defines a node type interface.
  * SFBool is a logical type with possible values (true|false) to match the XML boolean type. Hint: XML boolean values are lower case (true|false) in order to maintain compatibility with HTML and other XML documents. */

class SFBool : public X3DField
{
  /** Provide bool value from type SFBool */
  bool getValue ();

  /** Provide bool value from type SFBool */
  void setValue (bool value);
}
;/** MFBool defines a node type interface.
  * MFBool is an array of boolean values. Type MFBool was previously undefined in the VRML97 Specification, but nevertheless needed for event utilities and scripting. Example use: MFBool is useful for defining a series of behavior states using a BooleanSequencer prototype. Hint: XML boolean values are lower case (true|false) in order to maintain compatibility with HTML and other XML documents. */

class MFBool : public MField
{
  /** Provide bool* value from type MFBool */
  bool* getValue ();

  /** Utility method to provide single value from MFBool array */
  bool get1Value (int index);

  /** Provide bool* value from type MFBool */
  void setValue (int size, bool* values);

  /** Utility method to set a single value in MFBool array */
  void set1Value (int index, bool value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single value to MFBool array */
  void append (bool value);

  /** Utility method to insert a single value in MFBool array */
  void insertValue (int index, bool value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFColor defines a node type interface.
  * SFColor specifies one RGB (red-green-blue) color triple, where each color value is an RGB triple of floating point numbers in range [0,1]. The default value of an uninitialized SFColor field is (0 0 0). Warning: comma characters within singleton values do not pass strict XML validation. */

class SFColor : public X3DField
{
  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type SFColor */
  void getValue (float* result);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type SFColor */
  void setValue (float* color) throw (InvalidFieldValueException);
}
;/** MFColor defines a node type interface.
  * MFColor specifies zero or more SFColor RGB triples, where each color value is an RGB triple of floating point numbers in range [0,1]. The default value of an uninitialized MFColor field is the empty list. Individual SFColor array values are optionally separated by commas in XML syntax. */

class MFColor : public MField
{
  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type MFColor */
  void getValue (float* result);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type MFColor */
  void getValue (float** result); // overloaded method for convenience

  /** Utility method to provide single 3-tuple value from MFColor array */
  void get1Value (int index, float* result);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type MFColor */
  void setValue (int size, float* colors) throw (InvalidFieldValueException);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type MFColor */
  void setValue (float** colors) throw (InvalidFieldValueException); // overloaded method for convenience

  /** Utility method to set a single 3-tuple value in MFColor array */
  void set1Value (int index, float* color) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single 3-tuple value to MFColor array */
  void append (float* color);

  /** Utility method to insert a single 3-tuple value in MFColor array */
  void insertValue (int index, float* color) throw (ArrayIndexOutOfBoundsException);
}
;/** SFColorRGBA defines a node type interface.
  * SFColorRGBA specifies one RGBA (red-green-blue-alpha) color 4-tuple, where each color value is an RGBA 4-tuple of floating point numbers in range [0,1]. Alpha (opacity) values = (1 - transparency). The default value of an uninitialized SFColorRGBA field is (0 0 0 0). Warning: comma characters within singleton values do not pass strict XML validation. */

class SFColorRGBA : public X3DField
{
  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type SFColorRGBA */
  void getValue (float* result);

  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type SFColorRGBA */
  void setValue (float* color) throw (InvalidFieldValueException);
}
;/** MFColorRGBA defines a node type interface.
  * MFColorRGBA specifies zero or more SFColorRGBA 4-tuples, where each color value is an RGBA 4-tuple of floating point numbers in range [0,1]. Alpha (opacity) values = (1 - transparency). The default value of an uninitialized MFColor field is the empty list. Individual SFColorRGBA array values are optionally separated by commas in XML syntax. */

class MFColorRGBA : public MField
{
  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  void getValue (float* result);

  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  void getValue (float** result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFColorRGBA array */
  void get1Value (int index, float* result);

  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  void setValue (int size, float* colors) throw (InvalidFieldValueException);

  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  void setValue (float** colors) throw (InvalidFieldValueException); // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFColorRGBA array */
  void set1Value (int index, float* color) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single 4-tuple value to MFColorRGBA array */
  void append (float* color);

  /** Utility method to insert a single 4-tuple value in MFColorRGBA array */
  void insertValue (int index, float* color) throw (ArrayIndexOutOfBoundsException);
}
;/** SFDouble defines a node type interface.
  * SFDouble is a double-precision floating-point type. Array values are optionally separated by commas in XML syntax. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision for rationale. */

class SFDouble : public X3DField
{
  /** Provide double value from type SFDouble */
  double getValue ();

  /** Provide double value from type SFDouble */
  void setValue (double value);
}
;/** MFDouble defines a node type interface.
  * MFDouble is an array of Double values, meaning a double-precision floating-point array type. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision for rationale. Array values are optionally separated by commas in XML syntax. */

class MFDouble : public MField
{
  /** Provide double* value from type MFDouble */
  double* getValue ();

  /** Utility method to provide single value from MFDouble array */
  double get1Value (int index);

  /** Provide double* value from type MFDouble */
  void setValue (int size, double* values);

  /** Utility method to set a single value in MFDouble array */
  void set1Value (int index, double value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single value to MFDouble array */
  void append (double value);

  /** Utility method to insert a single value in MFDouble array */
  void insertValue (int index, double value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFFloat defines a node type interface.
  * SFFloat is a single-precision floating-point type. */

class SFFloat : public X3DField
{
  /** Provide float value from type SFFloat */
  float getValue ();

  /** Provide float value from type SFFloat */
  void setValue (float value);
}
;/** MFFloat defines a node type interface.
  * MFFloat is an array of SFFloat values, meaning a single-precision floating-point array type. Array values are optionally separated by commas in XML syntax. */

class MFFloat : public MField
{
  /** Provide float* value from type MFFloat */
  float* getValue ();

  /** Utility method to provide single value from MFFloat array */
  float get1Value (int index);

  /** Provide float* value from type MFFloat */
  void setValue (int size, float* values);

  /** Utility method to set a single value in MFFloat array */
  void set1Value (int index, float value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single value to MFFloat array */
  void append (float value);

  /** Utility method to insert a single value in MFFloat array */
  void insertValue (int index, float value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFImage defines a node type interface.
  * SFImage specifies a single uncompressed 2-dimensional pixel image. SFImage fields contain three integers representing the width, height and number of components in the image, followed by (width x height) hexadecimal or integer values representing the pixels in the image. */

class SFImage : public X3DField
{
    /** Get image width in pixels */
    int getWidth ();

    /** Get image height in pixels */
    int getHeight ();

    /** Get number of components in an image:
      * 1 (intensity), 2 (intensity alpha), 3 (red green blue), 4 (red green blue alpha-opacity).*/
    int getComponents();

    /** Get array of pixel values [0-255] */
    void getPixels (int* pixels);

    /** GDI++ Image **/
    Image getImage();

    /** Initialize image */
    void setValue (int width,
                          int height,
                          int components,
                          int* pixels);

    /** Assign a new image as current image */
    void setImage (Image image);

    /** Assign a portion of a new image as part of current image */
    void setSubImage (CImage image,
                             int srcWidth,
                             int srcHeight,
                             int srcXOffset,
                             int srcYOffset,
                             int destXOffset,
                             int destYOffset);
}
;/** MFImage defines a node type interface.
  * MFImage is an array of SFImage values. */

class MFImage : public MField
{
    /** Get selected image width in pixels */
    int getWidth (int imageIndex) throw (ArrayIndexOutOfBoundsException);

    /** Get selected image height in pixels */
    int getHeight (int imageIndex) throw (ArrayIndexOutOfBoundsException);

    /** Get number of components in selected image:
      * 1 (intensity), 2 (intensity alpha), 3 (red green blue), 4 (red green blue alpha-opacity).*/
    int getComponents (int imageIndex) throw (ArrayIndexOutOfBoundsException);

    /** Get array of pixel values [0-255] in selected image */
    void getPixels (int imageIndex, int* pixels) throw (ArrayIndexOutOfBoundsException);

    /** Get <a href="http://docs.oracle.com/javase/8/docs/api/java/awt/image/WritableRenderedImage.html">java.awt.image.WritableRenderedImage</a> version of selected image */
    WritableRenderedImage getImage(int imageIndex) throw (ArrayIndexOutOfBoundsException);

    /** Assign a new image as a replacement image within the current image array */
    void setImage (int imageIndex, RenderedImage img) throw (ArrayIndexOutOfBoundsException);

    /** Assign a portion of a new image as part of current selected image in array */
    void setSubImage (int imageIndex,
                             RenderedImage img,
                             int srcWidth,
                             int srcHeight,
                             int srcXOffset,
                             int srcYOffset,
                             int destXOffset,
                             int destYOffset) throw (ArrayIndexOutOfBoundsException);

    /** Utility method to set all values for selected image in array */
    void set1Value (int imageIndex, int value) throw (ArrayIndexOutOfBoundsException);

    /** Initialize selected image */
    void set1Value (int imageIndex,
                           int width,
                           int height,
                           int components,
                           int* pixels) throw (ArrayIndexOutOfBoundsException);

    /** Utility method to set all values for all images in array */
    void setValue (int* value);

    /** Assign a new image array as current image array */
    void setImage (RenderedImage* img);

    /** Append a new image to current image array */
    void append (RenderedImage value);

    /** Insert a new image in the current image array */
    void insertValue (int imageIndex, RenderedImage value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFInt32 defines a node type interface.
  * SFInt32 specifies one 32-bit signed integer. */

class SFInt32 : public X3DField
{
  /** Provide int value from type SFInt32 */
  int getValue ();

  /** Provide int value from type SFInt32 */
  void setValue (int value);
}
;/** MFInt32 defines a node type interface.
  * MFInt32 defines an array of 32-bit signed integers. Array values are optionally separated by commas in XML syntax. */

class MFInt32 : public MField
{
  /** Provide MFInt32 value from type MFInt32 */
  MFInt32 getValue ();

  /** Utility method to provide single value from MFInt32 array */
  int get1Value (int index);

  /** Provide MFInt32 value from type MFInt32 */
  void setValue (int size, MFInt32 values);

  /** Utility method to set a single value in MFInt32 array */
  void set1Value (int index, int value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single value to MFInt32 array */
  void append (int value);

  /** Utility method to insert a single value in MFInt32 array */
  void insertValue (int index, int value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFRotation defines a node type interface.
  * SFRotation is an axis-angle 4-tuple, indicating X-Y-Z direction axis plus angle orientation about that axis. The first three values specify a normalized axis vector about which the rotation takes place, so the first three values shall be within the range [-1..+1] in order to represent a normalized unit vector. The fourth value specifies the amount of right-handed rotation about that axis in radians. Warning: comma characters within singleton values do not pass strict XML validation. */

class SFRotation : public X3DField
{
  /** Provide 4-tuple float* value in radians from type SFRotation */
  float* getValue ();

  /** Provide 4-tuple float* value in radians from type SFRotation */
  void setValue (float* angle);
}
;/** MFRotation defines a node type interface.
  * MFRotation is an array of SFRotation values. Individual singleton SFRotation array values are optionally separated by commas in XML syntax. */

class MFRotation : public MField
{
  /** Provide 4-tuple float* value in radians from type MFRotation */
  float* getValue ();

  /** Provide 4-tuple float* value in radians from type MFRotation */
  void getValue (float** result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFRotation array */
  float* get1Value (int index);

  /** Provide 4-tuple float* value in radians from type MFRotation */
  void setValue (int size, float* angles);

  /** Provide 4-tuple float* value in radians from type MFRotation */
  void setValue (float** angles); // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFRotation array */
  void set1Value (int index, float* angle) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single 4-tuple value to MFRotation array */
  void append (float* angle);

  /** Utility method to insert a single 4-tuple value in MFRotation array */
  void insertValue (int index, float* angle) throw (ArrayIndexOutOfBoundsException);
}
;/** SFString defines a node type interface.
  * SFString defines a single MFString encoded with the UTF-8 universal character set. */

class SFString : public X3DField
{
  /** Provide MFString value from type SFString */
  MFString getValue ();

  /** Provide MFString value from type SFString */
  void setValue (MFString value);
}
;/** MFString defines a node type interface.
  * MFString is an array of SFString values, each "quoted" and separated by whitespace. Individual SFString array values are optionally separated by commas in XML syntax. */

class MFString : public MField
{
  /** Provide MFString* value from type MFString */
  MFString* getValue ();

  /** Utility method to provide single value from MFString array */
  MFString get1Value (int index);

  /** Provide MFString* value from type MFString */
  void setValue (int size, MFString* values);

  /** Utility method to set a single value in MFString array */
  void set1Value (int index, MFString value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single value to MFString array */
  void append (MFString value);

  /** Utility method to insert a single value in MFString array */
  void insertValue (int index, MFString value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFTime defines a node type interface.
  * SFTime specifies a single time value, expressed as a double-precision floating point number. Typically, SFTime fields represent the number of seconds since Jan 1, 1970, 00:00:00 GMT. */

class SFTime : public X3DField
{
  /** Provide double value in seconds from type SFTime */
  double getValue ();

  /** Provide long value in nanoseconds from type SFTime */
  long getCppValue ();

  /** Provide double value in seconds from type SFTime */
  void setValue (double timestamp);

  /** Assign long value in nanoseconds using System.nanoTime() to type SFTime */
  void setValue (long value);
}
;/** MFTime defines a node type interface.
  * MFTime is an array of SFTime values. Array values are optionally separated by commas in XML syntax. */

class MFTime : public MField
{
  /** Provide double* value in seconds from type MFTime */
  double* getValue ();

  /** Utility method to provide single value from MFTime array */
  double get1Value (int index);

  /** Utility method to provide single long value in nanoseconds from MFTime array */
  long get1CPPValue (int index);

  /** Provide double* value in seconds from type MFTime */
  void setValue (int size, double* timestamps);

  /** Assign long array in nanoseconds to type MFTime */
  void setValue (int size, long* values);

  /** Utility method to set a single value in MFTime array */
  void set1Value (int index, double timestamp) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to set a single long value in nanoseconds using System.nanoTime() in MFTime array */
  void set1Value (int index, long value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single value to MFTime array */
  void append (double timestamp);

  /** Utility method to insert a single value in MFTime array */
  void insertValue (int index, double timestamp) throw (ArrayIndexOutOfBoundsException);
}
;/** SFVec2f defines a node type interface.
  * SFVec2f is a 2-tuple pair of SFFloat values. Hint: SFVec2f can be used to specify a 2D single-precision coordinate. Warning: comma characters within singleton values do not pass strict XML validation. */

class SFVec2f : public X3DField
{
  /** Provide 2-tuple float* value from type SFVec2f */
  void getValue (float* result);

  /** Provide 2-tuple float* value from type SFVec2f */
  void setValue (float* value);
}
;/** MFVec2f defines a node type interface.
  * MFVec2f is an array of SFVec2f values. Individual singleton SFVec2f array values are optionally separated by commas in XML syntax. */

class MFVec2f : public MField
{
  /** Provide 2-tuple float* value from type MFVec2f */
  void getValue (float* result);

  /** Provide 2-tuple float* value from type MFVec2f */
  void getValue (float** result); // overloaded method for convenience

  /** Utility method to provide single 2-tuple value from MFVec2f array */
  void get1Value (int index, float* result);

  /** Provide 2-tuple float* value from type MFVec2f */
  void setValue (int size, float* values);

  /** Provide 2-tuple float* value from type MFVec2f */
  void setValue (float** values); // overloaded method for convenience

  /** Utility method to set a single 2-tuple value in MFVec2f array */
  void set1Value (int index, float* value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single 2-tuple value to MFVec2f array */
  void append (float* value);

  /** Utility method to insert a single 2-tuple value in MFVec2f array */
  void insertValue (int index, float* value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFVec2d defines a node type interface.
  * SFVec2d is a 2-tuple pair of SFDouble values. Hint: SFVec2d can be used to specify a 2D double-precision coordinate. Warning: comma characters within singleton values do not pass strict XML validation. */

class SFVec2d : public X3DField
{
  /** Provide 2-tuple double* value from type SFVec2d */
  void getValue (double* result);

  /** Provide 2-tuple double* value from type SFVec2d */
  void setValue (double* value);
}
;/** MFVec2d defines a node type interface.
  * MFVec2d is an array of SFVec2d values. Individual singleton SFVec2d array values are optionally separated by commas in XML syntax. */

class MFVec2d : public MField
{
  /** Provide 2-tuple double* value from type MFVec2d */
  void getValue (double* result);

  /** Provide 2-tuple double* value from type MFVec2d */
  void getValue (double** result); // overloaded method for convenience

  /** Utility method to provide single 2-tuple value from MFVec2d array */
  void get1Value (int index, double* result);

  /** Provide 2-tuple double* value from type MFVec2d */
  void setValue (int size, double* values);

  /** Provide 2-tuple double* value from type MFVec2d */
  void setValue (double** values); // overloaded method for convenience

  /** Utility method to set a single 2-tuple value in MFVec2d array */
  void set1Value (int index, double* value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single 2-tuple value to MFVec2d array */
  void append (double* value);

  /** Utility method to insert a single 2-tuple value in MFVec2d array */
  void insertValue (int index, double* value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFVec3f defines a node type interface.
  * SFVec3f is a 3-tuple triplet of SFFloat values. Hint: SFVec3f can be used to specify a 3D coordinate or a 3D scale value. Warning: comma characters within singleton values do not pass strict XML validation. */

class SFVec3f : public X3DField
{
  /** Provide 3-tuple float* value from type SFVec3f */
  void getValue (float* result);

  /** Provide 3-tuple float* value from type SFVec3f */
  void setValue (float* value);
}
;/** MFVec3f defines a node type interface.
  * MFVec3f is an array of SFVec3f values. Individual singleton SFVec3f array values are optionally separated by commas in XML syntax. */

class MFVec3f : public MField
{
  /** Provide 3-tuple float* value from type MFVec3f */
  void getValue (float* result);

  /** Provide 3-tuple float* value from type MFVec3f */
  void getValue (float** result); // overloaded method for convenience

  /** Utility method to provide single 3-tuple value from MFVec3f array */
  void get1Value (int index, float* result);

  /** Provide 3-tuple float* value from type MFVec3f */
  void setValue (int size, float* values);

  /** Provide 3-tuple float* value from type MFVec3f */
  void setValue (float** values); // overloaded method for convenience

  /** Utility method to set a single 3-tuple value in MFVec3f array */
  void set1Value (int index, float* value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single 3-tuple value to MFVec3f array */
  void append (float* value);

  /** Utility method to insert a single 3-tuple value in MFVec3f array */
  void insertValue (int index, float* value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFVec3d defines a node type interface.
  * SFVec3d is a 3-tuple triplet of SFDouble values. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision. Hint: SFVec3d can be used to specify a georeferenced 3D coordinate. Warning: comma characters within singleton values do not pass strict XML validation. */

class SFVec3d : public X3DField
{
  /** Provide 3-tuple double* value from type SFVec3d */
  void getValue (double* result);

  /** Provide 3-tuple double* value from type SFVec3d */
  void setValue (double* value);
}
;/** MFVec3d defines a node type interface.
  * MFVec3d is an array of SFVec3d values. Individual singleton SFVec3d array values are optionally separated by commas in XML syntax. Original rationale for inclusion: GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision. Hint: MFVec3d can be used to specify a list of georeferenced 3D coordinates. */

class MFVec3d : public MField
{
  /** Provide 3-tuple double* value from type MFVec3d */
  void getValue (double* result);

  /** Provide 3-tuple double* value from type MFVec3d */
  void getValue (double** result); // overloaded method for convenience

  /** Utility method to provide single 3-tuple value from MFVec3d array */
  void get1Value (int index, double* result);

  /** Provide 3-tuple double* value from type MFVec3d */
  void setValue (int size, double* values);

  /** Provide 3-tuple double* value from type MFVec3d */
  void setValue (double** values); // overloaded method for convenience

  /** Utility method to set a single 3-tuple value in MFVec3d array */
  void set1Value (int index, double* value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single 3-tuple value to MFVec3d array */
  void append (double* value);

  /** Utility method to insert a single 3-tuple value in MFVec3d array */
  void insertValue (int index, double* value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFVec4f defines a node type interface.
  * SFVec4f is a 4-tuple set of single-precision floating-point values, specifying a 3D homogeneous vector. Warning: comma characters within singleton values do not pass strict XML validation. */

class SFVec4f : public X3DField
{
  /** Provide 4-tuple float* value from type SFVec4f */
  void getValue (float* result);

  /** Provide 4-tuple float* value from type SFVec4f */
  void setValue (float* value);
}
;/** MFVec4f defines a node type interface.
  * MFVec4f is zero or more SFVec4f values. Individual singleton SFVec4f array values are optionally separated by commas in XML syntax. */

class MFVec4f : public MField
{
  /** Provide 4-tuple float* value from type MFVec4f */
  void getValue (float* result);

  /** Provide 4-tuple float* value from type MFVec4f */
  void getValue (float** result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFVec4f array */
  void get1Value (int index, float* result);

  /** Provide 4-tuple float* value from type MFVec4f */
  void setValue (int size, float* values);

  /** Provide 4-tuple float* value from type MFVec4f */
  void setValue (float** values); // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFVec4f array */
  void set1Value (int index, float* value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single 4-tuple value to MFVec4f array */
  void append (float* value);

  /** Utility method to insert a single 4-tuple value in MFVec4f array */
  void insertValue (int index, float* value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFVec4d defines a node type interface.
  * SFVec4d is a 4-tuple set of double-precision floating-point values, specifying a 3D homogeneous vector. Warning: comma characters within singleton values do not pass strict XML validation. */

class SFVec4d : public X3DField
{
  /** Provide 4-tuple double* value from type SFVec4d */
  void getValue (double* result);

  /** Provide 4-tuple double* value from type SFVec4d */
  void setValue (double* value);
}
;/** MFVec4d defines a node type interface.
  * MFVec4d is zero or more SFVec4d values. Individual singleton SFVec4d array values are optionally separated by commas in XML syntax. */

class MFVec4d : public MField
{
  /** Provide 4-tuple double* value from type MFVec4d */
  void getValue (double* result);

  /** Provide 4-tuple double* value from type MFVec4d */
  void getValue (double** result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFVec4d array */
  void get1Value (int index, double* result);

  /** Provide 4-tuple double* value from type MFVec4d */
  void setValue (int size, double* values);

  /** Provide 4-tuple double* value from type MFVec4d */
  void setValue (double** values); // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFVec4d array */
  void set1Value (int index, double* value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single 4-tuple value to MFVec4d array */
  void append (double* value);

  /** Utility method to insert a single 4-tuple value in MFVec4d array */
  void insertValue (int index, double* value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFMatrix3f defines a node type interface.
  * SFMatrix3f specifies a 3x3 matrix of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

class SFMatrix3f : public X3DField
{
  /** Provide float* value from type SFMatrix3f */
  float* getValue ();

  /** Provide float* value from type SFMatrix3f */
  void setValue (float* value);
}
;/** MFMatrix3f defines a node type interface.
  * MFMatrix3f specifies zero or more 3x3 matrices of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 9-tuple values. */

class MFMatrix3f : public MField
{
  /** Provide float* value from type MFMatrix3f */
  float* getValue ();

  /** Provide float* value from type MFMatrix3f */
  void getValue (float** result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix3f array */
  float* get1Value (int index);

  /** Provide float* value from type MFMatrix3f */
  void setValue (int size, float* values);

  /** Provide float* value from type MFMatrix3f */
  void setValue (float** values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix3f array */
  void set1Value (int index, float* value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single value to MFMatrix3f array */
  void append (float* value);

  /** Utility method to insert a single value in MFMatrix3f array */
  void insertValue (int index, float* value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFMatrix3d defines a node type interface.
  * SFMatrix3d specifies a 3x3 matrix of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

class SFMatrix3d : public X3DField
{
  /** Provide double* value from type SFMatrix3d */
  double* getValue ();

  /** Provide double* value from type SFMatrix3d */
  void setValue (double* value);
}
;/** MFMatrix3d defines a node type interface.
  * MFMatrix3d specifies zero or more 3x3 matrices of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 9-tuple values. */

class MFMatrix3d : public MField
{
  /** Provide double* value from type MFMatrix3d */
  double* getValue ();

  /** Provide double* value from type MFMatrix3d */
  void getValue (double** result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix3d array */
  double* get1Value (int index);

  /** Provide double* value from type MFMatrix3d */
  void setValue (int size, double* values);

  /** Provide double* value from type MFMatrix3d */
  void setValue (double** values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix3d array */
  void set1Value (int index, double* value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single value to MFMatrix3d array */
  void append (double* value);

  /** Utility method to insert a single value in MFMatrix3d array */
  void insertValue (int index, double* value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFMatrix4f defines a node type interface.
  * SFMatrix4f specifies a 4x4 matrix of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

class SFMatrix4f : public X3DField
{
  /** Provide float* value from type SFMatrix4f */
  float* getValue ();

  /** Provide float* value from type SFMatrix4f */
  void setValue (float* value);
}
;/** MFMatrix4f defines a node type interface.
  * MFMatrix4f specifies zero or more 4x4 matrices of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 16-tuple values. */

class MFMatrix4f : public MField
{
  /** Provide float* value from type MFMatrix4f */
  float* getValue ();

  /** Provide float* value from type MFMatrix4f */
  void getValue (float** result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix4f array */
  float* get1Value (int index);

  /** Provide float* value from type MFMatrix4f */
  void setValue (int size, float* values);

  /** Provide float* value from type MFMatrix4f */
  void setValue (float** values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix4f array */
  void set1Value (int index, float* value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single value to MFMatrix4f array */
  void append (float* value);

  /** Utility method to insert a single value in MFMatrix4f array */
  void insertValue (int index, float* value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFMatrix4d defines a node type interface.
  * SFMatrix4d specifies a 4x4 matrix of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

class SFMatrix4d : public X3DField
{
  /** Provide double* value from type SFMatrix4d */
  double* getValue ();

  /** Provide double* value from type SFMatrix4d */
  void setValue (double* value);
}
;/** MFMatrix4d defines a node type interface.
  * MFMatrix4d specifies zero or more 4x4 matrices of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 16-tuple values. */

class MFMatrix4d : public MField
{
  /** Provide double* value from type MFMatrix4d */
  double* getValue ();

  /** Provide double* value from type MFMatrix4d */
  void getValue (double** result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix4d array */
  double* get1Value (int index);

  /** Provide double* value from type MFMatrix4d */
  void setValue (int size, double* values);

  /** Provide double* value from type MFMatrix4d */
  void setValue (double** values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix4d array */
  void set1Value (int index, double* value) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single value to MFMatrix4d array */
  void append (double* value);

  /** Utility method to insert a single value in MFMatrix4d array */
  void insertValue (int index, double* value) throw (ArrayIndexOutOfBoundsException);
}
;/** SFNode defines a node type interface.
  * SFNode specifies an X3D node; the default empty value of an uninitialized SFNode field is sometimes described as NULL. */

class SFNode : public X3DField
{
  /** Provide X3DNode value (using a properly typed node or X3DPrototypeInstance) from type SFNode */
  void getValue (X3DNode& result);

  /** Provide X3DNode value (using a properly typed node or X3DPrototypeInstance) from type SFNode */
  void setValue (X3DNode node);
}
;/** MFNode defines a node type interface.
  * MFNode specifies zero or more nodes; the default value of an MFNode field is the empty list. */

class MFNode : public MField
{
  /** Provide X3DNode value (using a properly typed node array or X3DPrototypeInstance array) from type MFNode */
  void getValue (X3DNode& result);

  /** Utility method to provide single value from MFNode array */
  void get1Value (int index, X3DNode result);

  /** Provide X3DNode value (using a properly typed node array or X3DPrototypeInstance array) from type MFNode */
  void setValue (int size, X3DNode nodes);

  /** Utility method to set a single value in MFNode array */
  void set1Value (int index, X3DNode node) throw (ArrayIndexOutOfBoundsException);

  /** Utility method to append a single value to MFNode array */
  void append (X3DNode node);

  /** Utility method to insert a single value in MFNode array */
  void insertValue (int index, X3DNode node) throw (ArrayIndexOutOfBoundsException);
}
;
class BrowserEvent : public EventObject
{
public:
	static int INITIALIZED = 0;
	static int SHUTDOWN = 1;
	static int URL_ERROR = 2;
	static int CONNECTION_ERROR = 10;
	static int LAST_IDENTIFIER = 100;

	BrowserEvent(Object browser, int action);
	int getID();
}
					;
class BrowserFactory
{
public:
	BrowserFactory();

	static void setBrowserFactoryImpl(
						BrowserFactoryImpl fac)
						throw Exception(IllegalArgumentException,
						X3DException,
						SecurityException);

	static X3DComponent createX3DComponent(Map params)
						throw Exception(NotSupportedException);

	static ExternalBrowser getBrowser()
						throw Exception(NotSupportedException,
						NoSuchBrowserException,
						ConnectionException);

	static ExternalBrowser getBrowser(MFString frameName,
						int index)
						throw Exception(NotSupportedException,
						NoSuchBrowserException,
						ConnectionException);

	static ExternalBrowser getBrowser(InetAddress address, int port)
						throw Exception(NotSupportedException,
						NoSuchBrowserException,
						UnknownHostException,
						ConnectionException);
}
					;
class X3DFieldEvent : public EventObject
{
public:
	X3DFieldEvent(Object src, double ts, Object data);
	double getTime();
	CObject getData();
}
					;
class Matrix3
{
public:
	Matrix3();
	void setIdentity();
	void set(int row, int column);
	float get(int row, int column);
	void setTransform(SFVec2f translation,
					SFVec3f rotation,
					SFVec2f scale,
					SFVec3f scaleOrientation,
					SFVec2f center);
	void getTransform(SFVec2f& translation,
					SFVec3f& rotation,
					SFVec2f& scale);
	Matrix3 inverse();
	Matrix3 transpose();
	Matrix3 multiplyLeft(Matrix3 mat);
	Matrix3 multiplyRight(Matrix3 mat);
	Matrix3 multiplyRowVector(SFVec3f vec);
	Matrix3 multiplyColVector(SFVec3f vec);
}
					;
class Matrix4
{
public:
	Matrix4();
	void setIdentity();
	void set(int row, int column);
	float get(int row, int column);
	void setTransform(SFVec3f translation,
						SFRotation rotation,
						SFVec3f scale,
						SFRotation scaleOrientation,
						SFVec3f center);
	void getTransform(SFVec3f& translation,
						SFRotation& rotation,
						SFVec3f& scale);
	Matrix3 inverse();
	Matrix3 transpose();
	Matrix3 multiplyLeft(Matrix4 mat);
	Matrix3 multiplyRight(Matrix4 mat);
	Matrix3 multiplyRowVector(SFVec3f vec);
	Matrix3 multiplyColVector(SFVec3f vec);
}
					;
class ComponentInfo
{
public:
	MFString getName();
	int getLevel();
	MFString getTitle();
	MFString getProviderURL();
	MFString toX3DString();
}
					;
class ProfileInfo
{
public:
	MFString getName();
	MFString getTitle();
	ComponentInfo* getComponents();
	MFString toX3DString();
}
					;
class X3DException : public RuntimeException
{
public:
	X3DException();
	X3DException(MFString);
}
					;
class BrowserNotSharedException : public X3DException
{
public:
	BrowserNotSharedException();
	BrowserNotSharedException(MFString);
}
					;
class ConnectionException : public X3DException
{
public:
	ConnectionException();
	ConnectionException(MFString);
}
					;
class ImportedNodeException : public X3DException
{
public:
	ImportedNodeException();
	ImportedNodeException(MFString);
}
					;
class InsufficientCapabilitiesException : public X3DException
{
public:
	InsufficientCapabilitiesException();
	InsufficientCapabilitiesException(MFString);
}
					;
class InvalidBrowserException : public X3DException
{
public:
	InvalidBrowserException();
	InvalidBrowserException(MFString);
}
					;
class InvalidDocumentException : public X3DException
{
public:
	InvalidDocumentException();
	InvalidDocumentException(MFString);
}
					;
class InvalidExecutionContextException : public X3DException
{
public:
	InvalidExecutionContextException();
	InvalidExecutionContextException(MFString);
}
					;
class InvalidFieldException : public X3DException
{
public:
	InvalidFieldException();
	InvalidFieldException(MFString);
}
					;
class InvalidFieldValueException : public X3DException
{
public:
	InvalidFieldValueException();
	InvalidFieldValueException(MFString);
}
					;
class InvalidNodeException : public X3DException
{
public:
	InvalidNodeException();
	InvalidNodeException(MFString);
}
					;
class InvalidOperationTimingException : public X3DException
{
public:
	InvalidOperationTimingException();
	InvalidOperationTimingException(MFString);
}
					;
class InvalidProtoException : public X3DException
{
public:
	InvalidProtoException();
	InvalidProtoException(MFString);
}
					;
class InvalidRouteException : public X3DException
{
public:
	InvalidRouteException();
	InvalidRouteException(MFString);
}
					;
class InvalidURLException : public X3DException
{
public:
	InvalidURLException();
	InvalidURLException(MFString);
}
					;
class InvalidX3DException : public X3DException
{
public:
	InvalidX3DException();
	InvalidX3DException(MFString);
}
					;
class NodeInUseException : public X3DException
{
public:
	NodeInUseException();
	NodeInUseException(MFString);
}
					;
class NodeUnavailableException : public X3DException
{
public:
	NodeUnavailableException();
	NodeUnavailableException(MFString);
}
					;
class NoSuchBrowserException : public X3DException
{
public:
	NoSuchBrowserException();
	NoSuchBrowserException(MFString);
}
					;
class NotSupportedException : public X3DException
{
public:
	NotSupportedException();
	NotSupportedException(MFString);
}
					;
class URLUnavailableException : public X3DException
{
public:
	URLUnavailableException();
	URLUnavailableException(MFString);
}
					;