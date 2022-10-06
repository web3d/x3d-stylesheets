/** X3DAppearanceChildNode defines an abstract node interface that extends interface X3DNode.
  * Nodes of this type can be used as child nodes for Appearance. */

public interface X3DAppearanceChildNode : X3DNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DAppearanceNode defines an abstract node interface that extends interface X3DNode.
  * Base type for all Appearance nodes. */

public interface X3DAppearanceNode : X3DNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DBackgroundNode defines an abstract node interface that extends interfaces X3DBindableNode, X3DChildNode, and X3DNode.
  * Abstract type from which all backgrounds inherit, also defining a background binding stack. */

public interface X3DBackgroundNode : X3DBindableNode
{
  /** Provide array of float results array in radians (-∞,∞) from inputOutput MFFloat field named "groundAngle". */
  public float[] getGroundAngle ();

  /** Provide number of primitive values in "groundAngle" array */
  public int getNumGroundAngle ();

  /** Assign float array in radians (-∞,∞) to inputOutput MFFloat field named "groundAngle". */
  public void setGroundAngle (float[] angles);

  /** Assign single float value in radians (-∞,∞) as the MFFloat array for inputOutput field named "groundAngle" */
  public void setGroundAngle (float angle);

  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from inputOutput MFColor field named "groundColor". */
  public void getGroundColor (float[] result);

  /** Provide number of 3-tuple primitive values in "groundColor" array */
  public int getNumGroundColor ();

  /** Assign 3-tuple float array using RGB values [0..1] using RGB values [0..1] to inputOutput MFColor field named "groundColor". */
  public void setGroundColor (float[] colors);

  /** Provide array of float results array in radians (-∞,∞) from inputOutput MFFloat field named "skyAngle". */
  public float[] getSkyAngle ();

  /** Provide number of primitive values in "skyAngle" array */
  public int getNumSkyAngle ();

  /** Assign float array in radians (-∞,∞) to inputOutput MFFloat field named "skyAngle". */
  public void setSkyAngle (float[] angles);

  /** Assign single float value in radians (-∞,∞) as the MFFloat array for inputOutput field named "skyAngle" */
  public void setSkyAngle (float angle);

  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from inputOutput MFColor field named "skyColor". */
  public void getSkyColor (float[] result);

  /** Provide number of 3-tuple primitive values in "skyColor" array */
  public int getNumSkyColor ();

  /** Assign 3-tuple float array using RGB values [0..1] using RGB values [0..1] to inputOutput MFColor field named "skyColor". */
  public void setSkyColor (float[] colors);

  /** Provide float value from inputOutput SFFloat field named "transparency". */
  public float getTransparency ();

  /** Assign float value to inputOutput SFFloat field named "transparency". */
  public void setTransparency (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Assign bool value to inputOnly SFBool field named "set_bind". */
  public void setBind (bool value);

  /** Provide double value in seconds from outputOnly SFTime field named "bindTime". */
  public double getBindTime ();

  /** Provide bool value from outputOnly SFBool field named "isBound". */
  public bool getIsBound ();

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DBindableNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Bindable nodes implement the binding stack, so that only one of each node type is active at a given time. */

public interface X3DBindableNode : X3DChildNode
{
  /** Assign bool value to inputOnly SFBool field named "set_bind". */
  public void setBind (bool value);

  /** Provide double value in seconds from outputOnly SFTime field named "bindTime". */
  public double getBindTime ();

  /** Provide bool value from outputOnly SFBool field named "isBound". */
  public bool getIsBound ();

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DChaserNode defines an abstract node interface that extends interfaces X3DFollowerNode, X3DChildNode, and X3DNode.
  * The X3DChaserNode abstract node type calculates the output on value_changed as a finite impulse response (FIR) based on the events received on set_destination field. */

public interface X3DChaserNode : X3DFollowerNode
{
  /** Provide double value in seconds [0,∞) from initializeOnly SFTime field named "duration". */
  public double getDuration ();

  /** Assign double value in seconds [0,∞) to initializeOnly SFTime field named "duration". */
  public void setDuration (double timestamp);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DChildNode defines an abstract node interface that extends interface X3DNode.
  * A node that implements X3DChildNode is one of the legal children for a X3DGroupingNode parent. */

public interface X3DChildNode : X3DNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DColorNode defines an abstract node interface that extends interfaces X3DGeometricPropertyNode and X3DNode.
  * Base type for color specifications in X3D. */

public interface X3DColorNode : X3DGeometricPropertyNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DComposableVolumeRenderStyleNode defines an abstract node interface that extends interfaces X3DVolumeRenderStyleNode and X3DNode.
  * The X3DComposableVolumeRenderStyleNode abstract node type is the base type for all node types that allow rendering styles to be sequentially composed together to form a single renderable output. */

public interface X3DComposableVolumeRenderStyleNode : X3DVolumeRenderStyleNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DComposedGeometryNode defines an abstract node interface that extends interfaces X3DGeometryNode and X3DNode.
  * Composed geometry nodes produce renderable geometry, can contain Color Coordinate Normal TextureCoordinate, and are contained by a Shape node. */

public interface X3DComposedGeometryNode : X3DGeometryNode
{
  /** Provide bool value from initializeOnly SFBool field named "ccw". */
  public bool getCcw ();

  /** Assign bool value to initializeOnly SFBool field named "ccw". */
  public void setCcw (bool value);

  /** Provide bool value from initializeOnly SFBool field named "colorPerVertex". */
  public bool getColorPerVertex ();

  /** Assign bool value to initializeOnly SFBool field named "colorPerVertex". */
  public void setColorPerVertex (bool color);

  /** Provide bool value from initializeOnly SFBool field named "normalPerVertex". */
  public bool getNormalPerVertex ();

  /** Assign bool value to initializeOnly SFBool field named "normalPerVertex". */
  public void setNormalPerVertex (bool value);

  /** Provide bool value from inputOutput SFBool field named "solid". */
  public bool getSolid ();

  /** Assign bool value to inputOutput SFBool field named "solid". */
  public void setSolid (bool value);

  /** Provide array of X3DVertexAttributeNode results array (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DVertexAttributeNode type field named "attrib". */
  public void getAttrib (X3DNode[] result);

  /** Provide number of nodes in "attrib" array */
  public int getNumAttrib ();

  /** Assign X3DVertexAttributeNode array (using a properly typed node array) to inputOutput X3DVertexAttributeNode type field named "attrib". */
  public void setAttrib (X3DVertexAttributeNode[] nodes);

  /** Assign single X3DVertexAttributeNode value (using a properly typed node) as the MFNode array for inputOutput field named "attrib" */
  public void setAttrib (X3DVertexAttributeNode node);

  /** Assign X3DVertexAttributeNode array (using a properly typed protoInstance array) to inputOutput X3DVertexAttributeNode type field named "attrib". */
  public void setAttrib (X3DPrototypeInstance node);

  /** Assign X3DVertexAttributeNode array (using a properly typed node array) to inputOutput X3DVertexAttributeNode type field named "attrib". */
  public void setAttrib (X3DNode[] nodes);

  /** Provide X3DColorNode value (using a properly typed node or X3DPrototypeInstance) using RGB values [0..1] from inputOutput X3DColorNode type field named "color". */
  public void getColor (X3DNode result);

  /** Assign X3DColorNode value (using a properly typed node) using RGB values [0..1] to inputOutput X3DColorNode type field named "color". */
  public void setColor (X3DColorNode color);

  /** Assign X3DColorNode value (using a properly typed protoInstance) */
  public void setColor (X3DPrototypeInstance protoInstance);

  /** Provide X3DCoordinateNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DCoordinateNode type field named "coord". */
  public void getCoord (X3DNode result);

  /** Assign X3DCoordinateNode value (using a properly typed node) to inputOutput X3DCoordinateNode type field named "coord". */
  public void setCoord (X3DCoordinateNode node);

  /** Assign X3DCoordinateNode value (using a properly typed protoInstance) */
  public void setCoord (X3DPrototypeInstance protoInstance);

  /** Provide FogCoordinate value (using a properly typed node or X3DPrototypeInstance) from inputOutput FogCoordinate type field named "fogCoord". */
  public void getFogCoord (X3DNode result);

  /** Assign FogCoordinate value (using a properly typed node) to inputOutput FogCoordinate type field named "fogCoord". */
  public void setFogCoord (FogCoordinate node);

  /** Assign FogCoordinate value (using a properly typed protoInstance) */
  public void setFogCoord (X3DPrototypeInstance protoInstance);

  /** Provide X3DNormalNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DNormalNode type field named "normal". */
  public void getNormal (X3DNode result);

  /** Assign X3DNormalNode value (using a properly typed node) to inputOutput X3DNormalNode type field named "normal". */
  public void setNormal (X3DNormalNode node);

  /** Assign X3DNormalNode value (using a properly typed protoInstance) */
  public void setNormal (X3DPrototypeInstance protoInstance);

  /** Provide X3DSingleTextureCoordinateNode|MultiTextureCoordinate value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DSingleTextureCoordinateNode|MultiTextureCoordinate type field named "texCoord". */
  public void getTexCoord (X3DNode result);

  /** Assign X3DSingleTextureCoordinateNode|MultiTextureCoordinate value (using a properly typed node) to inputOutput X3DSingleTextureCoordinateNode|MultiTextureCoordinate type field named "texCoord". */
  public void setTexCoord (X3DNode node);

  /** Assign X3DSingleTextureCoordinateNode|MultiTextureCoordinate value (using a properly typed protoInstance) */
  public void setTexCoord (X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DCoordinateNode defines an abstract node interface that extends interfaces X3DGeometricPropertyNode and X3DNode.
  * Base type for all coordinate node types in X3D. */

public interface X3DCoordinateNode : X3DGeometricPropertyNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DDamperNode defines an abstract node interface that extends interfaces X3DFollowerNode, X3DChildNode, and X3DNode.
  * The X3DDamperNode abstract node type creates an IIR response that approaches the destination value according to the shape of the e-function only asymptotically but very quickly. */

public interface X3DDamperNode : X3DFollowerNode
{
  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "tau". */
  public double getTau ();

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "tau". */
  public void setTau (double timestamp);

  /** Provide float value from inputOutput SFFloat field named "tolerance". */
  public float getTolerance ();

  /** Assign float value to inputOutput SFFloat field named "tolerance". */
  public void setTolerance (float value);

  /** Provide int value [0,5) from initializeOnly SFInt32 field named "order". */
  public int getOrder ();

  /** Assign int value [0,5) to initializeOnly SFInt32 field named "order". */
  public void setOrder (int value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DDragSensorNode defines an abstract node interface that extends interfaces X3DPointingDeviceSensorNode, X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all drag-style pointing device sensors. */

public interface X3DDragSensorNode : X3DPointingDeviceSensorNode
{
  /** Provide array of 3-tuple float results array from outputOnly SFVec3f field named "trackPoint_changed". */
  public void getTrackPoint (float[] result);

  /** Provide bool value from inputOutput SFBool field named "autoOffset". */
  public bool getAutoOffset ();

  /** Assign bool value to inputOutput SFBool field named "autoOffset". */
  public void setAutoOffset (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isOver". */
  public bool getIsOver ();

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DEnvironmentalSensorNode defines an abstract node interface that extends interfaces X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for the environmental sensor nodes ProximitySensor, TransformSensor and VisibilitySensor. */

public interface X3DEnvironmentalSensorNode : X3DSensorNode
{
  /** Provide array of 3-tuple float results array (-∞,∞) from initializeOnly SFVec3f field named "size". */
  public void getSize (float[] result);

  /** Assign 3-tuple float array (-∞,∞) to initializeOnly SFVec3f field named "size". */
  public void setSize (float[] value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DEnvironmentTextureNode defines an abstract node interface that extends interfaces X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all nodes that specify cubic environment map sources for texture images. */

public interface X3DEnvironmentTextureNode : X3DTextureNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DFollowerNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * X3DFollowerNode is the abstract base class for all nodes in the Followers component. */

public interface X3DFollowerNode : X3DChildNode
{
  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DFontStyleNode defines an abstract node interface.
  * Base type for all font style nodes. */

public interface X3DFontStyleNode : X3DNode
{
  /** Provide xs:NMTOKENS value from inputOutput xs:NMTOKENS type field named "class". */
  public xs:NMTOKENS getClass ();

  /** Assign xs:NMTOKENS value to inputOutput xs:NMTOKENS type field named "class". */
  public void setClass (xs:NMTOKENS value);

  /** Provide String value from inputOutput SFString field named "id". */
  public String getId ();

  /** Assign String value to inputOutput SFString field named "id". */
  public void setId (String value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DGeometricPropertyNode defines an abstract node interface that extends interface X3DNode.
  * Base type for all geometric property node types. */

public interface X3DGeometricPropertyNode : X3DNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DGeometryNode defines an abstract node interface that extends interface X3DNode.
  * Geometry nodes produce renderable geometry and are contained by a Shape node. */

public interface X3DGeometryNode : X3DNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DGroupingNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Grouping nodes can contain other nodes as children, thus making up the backbone of a scene graph. */

public interface X3DGroupingNode : X3DChildNode, X3DBoundedObject
{
  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxCenter". */
  public void getBboxCenter (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxCenter". */
  public void setBboxCenter (float[] value);

  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxSize". */
  public void getBboxSize (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxSize". */
  public void setBboxSize (float[] value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  public bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  public void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  public bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  public void setVisible (bool value);

  /** Assign X3DChildNode array (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  public void addChildren (X3DChildNode[] nodes);

  /** Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOnly field named "addChildren" */
  public void addChildren (X3DChildNode node);

  /** Assign X3DChildNode array (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "addChildren". */
  public void addChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode array (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  public void addChildren (X3DNode[] nodes);

  /** Assign X3DChildNode array (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  public void removeChildren (X3DChildNode[] nodes);

  /** Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOnly field named "removeChildren" */
  public void removeChildren (X3DChildNode node);

  /** Assign X3DChildNode array (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "removeChildren". */
  public void removeChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode array (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  public void removeChildren (X3DNode[] nodes);

  /** Provide array of X3DChildNode results array (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DChildNode type field named "children". */
  public void getChildren (X3DNode[] result);

  /** Provide number of nodes in "children" array */
  public int getNumChildren ();

  /** Assign X3DChildNode array (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  public void setChildren (X3DChildNode[] nodes);

  /** Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOutput field named "children" */
  public void setChildren (X3DChildNode node);

  /** Assign X3DChildNode array (using a properly typed protoInstance array) to inputOutput X3DChildNode type field named "children". */
  public void setChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode array (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  public void setChildren (X3DNode[] nodes);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DInfoNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Base type for all nodes that contain only information without visual semantics. */

public interface X3DInfoNode : X3DChildNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DInterpolatorNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Interpolator nodes are designed for linear keyframed animation. Interpolators are driven by an input key ranging [0..1] and produce corresponding piecewise-linear output functions. */

public interface X3DInterpolatorNode : X3DChildNode
{
  /** Assign float value to inputOnly SFFloat field named "set_fraction". */
  public void setFraction (float value);

  /** Provide array of float results array from inputOutput MFFloat field named "key". */
  public float[] getKey ();

  /** Provide number of primitive values in "key" array */
  public int getNumKey ();

  /** Assign float array to inputOutput MFFloat field named "key". */
  public void setKey (float[] values);

  /** Assign single float value as the MFFloat array for inputOutput field named "key" */
  public void setKey (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DKeyDeviceSensorNode defines an abstract node interface that extends interfaces X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all sensor node types that operate using key devices. */

public interface X3DKeyDeviceSensorNode : X3DSensorNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DLayerNode defines an abstract node interface that extends interface X3DNode.
  * The X3DLayerNode abstract node type is the base node type for layer nodes. */

public interface X3DLayerNode : X3DNode, X3DPickableObject
{
  /** Provide array of String results array ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  public String[] getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  public int getNumObjectType ();

  /** Assign String array ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  public void setObjectType (String[] values);

  /** Provide array of String results array ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  public String[] getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  public int getNumObjectType ();

  /** Assign String array ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  public void setObjectType (String[] values);

  /** Assign single String value ["ALL","NONE","TERRAIN",...] as the MFString array for inputOutput field named "objectType" */
  public void setObjectType (String value);

  /** Provide bool value from inputOutput SFBool field named "pickable". */
  public bool getPickable ();

  /** Assign bool value to inputOutput SFBool field named "pickable". */
  public void setPickable (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  public bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  public void setVisible (bool value);

  /** Provide X3DViewportNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DViewportNode type field named "viewport". */
  public void getViewport (X3DNode result);

  /** Assign X3DViewportNode value (using a properly typed node) to inputOutput X3DViewportNode type field named "viewport". */
  public void setViewport (X3DViewportNode node);

  /** Assign X3DViewportNode value (using a properly typed protoInstance) */
  public void setViewport (X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DLayoutNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * X3DLayoutNode is the base node type for layout nodes. */

public interface X3DLayoutNode : X3DChildNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DLightNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Light nodes provide illumination for rendering geometry in the scene. Implementing nodes must include a global field with type SFBool and accessType inputOutput. */

public interface X3DLightNode : X3DChildNode
{
  /** Provide float value from inputOutput SFFloat field named "ambientIntensity". */
  public float getAmbientIntensity ();

  /** Assign float value to inputOutput SFFloat field named "ambientIntensity". */
  public void setAmbientIntensity (float value);

  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "color". */
  public void getColor (float[] result);

  /** Assign 3-tuple float array using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "color". */
  public void setColor (float[] color);

  /** Provide float value [0,∞) from inputOutput SFFloat field named "intensity". */
  public float getIntensity ();

  /** Assign float value [0,∞) to inputOutput SFFloat field named "intensity". */
  public void setIntensity (float value);

  /** Provide bool value from inputOutput SFBool field named "on". */
  public bool getOn ();

  /** Assign bool value to inputOutput SFBool field named "on". */
  public void setOn (bool value);

  /** Provide bool value from inputOutput SFBool field named "shadows". */
  public bool getShadows ();

  /** Assign bool value to inputOutput SFBool field named "shadows". */
  public void setShadows (bool value);

  /** Provide float value from inputOutput SFFloat field named "shadowIntensity". */
  public float getShadowIntensity ();

  /** Assign float value to inputOutput SFFloat field named "shadowIntensity". */
  public void setShadowIntensity (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DMaterialNode defines an abstract node interface that extends interfaces X3DAppearanceChildNode and X3DNode.
  * Base type for all Material nodes. */

public interface X3DMaterialNode : X3DAppearanceChildNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DNBodyCollidableNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * The X3DNBodyCollidableNode abstract node type represents objects that act as the interface between the rigid body physics, collision geometry proxy, and renderable objects in the scene graph hierarchy. */

public interface X3DNBodyCollidableNode : X3DChildNode, X3DBoundedObject
{
  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxCenter". */
  public void getBboxCenter (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxCenter". */
  public void setBboxCenter (float[] value);

  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxSize". */
  public void getBboxSize (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxSize". */
  public void setBboxSize (float[] value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  public bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  public void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  public bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  public void setVisible (bool value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide array of 4-tuple float results array in radians from inputOutput SFRotation field named "rotation". */
  public float[] getRotation ();

  /** Assign 4-tuple float array in radians to inputOutput SFRotation field named "rotation". */
  public void setRotation (float[] value);

  /** Provide array of 3-tuple float results array from inputOutput SFVec3f field named "translation". */
  public void getTranslation (float[] result);

  /** Assign 3-tuple float array to inputOutput SFVec3f field named "translation". */
  public void setTranslation (float[] value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DNBodyCollisionSpaceNode defines an abstract node interface that extends interface X3DNode.
  * The X3DNBodyCollisionSpaceNode abstract node type represents objects that act as a self-contained spatial collection of objects that can interact through collision detection routines. */

public interface X3DNBodyCollisionSpaceNode : X3DNode, X3DBoundedObject
{
  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxCenter". */
  public void getBboxCenter (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxCenter". */
  public void setBboxCenter (float[] value);

  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxSize". */
  public void getBboxSize (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxSize". */
  public void setBboxSize (float[] value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  public bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  public void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  public bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  public void setVisible (bool value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DNetworkSensorNode defines an abstract node interface that extends interfaces X3DSensorNode, X3DChildNode, and X3DNode.
  * Base typefor all sensors that generate events based on network activity. */

public interface X3DNetworkSensorNode : X3DSensorNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DNode defines an abstract node interface.
  * All instantiable nodes implement X3DNode, which corresponds to SFNode type in the X3D specification. */

public interface X3DNode
{
  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);

  /** Dispose of this node's resources. */
  void dispose();

  /** Get a field for this node by name. */
  X3DField getField (String name);

  /** Get list of available fields in this node. */
  X3DFieldDefinition[] getFieldDefinitions();

  /** Get the name of this node. */
  String getNodeName();

  /** Determine if node setup is completed. */
  boolean isRealized ();

  /** Notify node that setup stage is complete. */
  void realize ();
}
/** X3DNormalNode defines an abstract node interface that extends interfaces X3DGeometricPropertyNode and X3DNode.
  * Base type for all normal node types in X3D. */

public interface X3DNormalNode : X3DGeometricPropertyNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DNurbsControlCurveNode defines an abstract node interface that extends interface X3DNode.
  * Base type for all nodes that provide control curve information in 2D space. */

public interface X3DNurbsControlCurveNode : X3DNode
{
  /** Provide array of 2-tuple double results array from inputOutput MFVec2d field named "controlPoint". */
  public void getControlPoint (double[] result);

  /** Provide number of 2-tuple primitive values in "controlPoint" array */
  public int getNumControlPoint ();

  /** Assign 2-tuple double array to inputOutput MFVec2d field named "controlPoint". */
  public void setControlPoint (double[] values);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DNurbsSurfaceGeometryNode defines an abstract node interface that extends interfaces X3DParametricGeometryNode, X3DGeometryNode, and X3DNode.
  * Abstract geometry type for all types of NURBS surfaces. */

public interface X3DNurbsSurfaceGeometryNode : X3DParametricGeometryNode
{
  /** Provide bool value from initializeOnly SFBool field named "uClosed". */
  public bool getUClosed ();

  /** Assign bool value to initializeOnly SFBool field named "uClosed". */
  public void setUClosed (bool value);

  /** Provide bool value from initializeOnly SFBool field named "vClosed". */
  public bool getVClosed ();

  /** Assign bool value to initializeOnly SFBool field named "vClosed". */
  public void setVClosed (bool value);

  /** Provide int value [0,∞) from initializeOnly SFInt32 field named "uDimension". */
  public int getUDimension ();

  /** Assign int value [0,∞) to initializeOnly SFInt32 field named "uDimension". */
  public void setUDimension (int value);

  /** Provide int value [0,∞) from initializeOnly SFInt32 field named "vDimension". */
  public int getVDimension ();

  /** Assign int value [0,∞) to initializeOnly SFInt32 field named "vDimension". */
  public void setVDimension (int value);

  /** Provide array of double results array from initializeOnly MFDouble field named "uKnot". */
  public double[] getUKnot ();

  /** Provide number of primitive values in "uKnot" array */
  public int getNumUKnot ();

  /** Assign double array to initializeOnly MFDouble field named "uKnot". */
  public void setUKnot (double[] values);

  /** Assign single double value as the MFDouble array for initializeOnly field named "uKnot" */
  public void setUKnot (double value);

  /** Provide array of double results array from initializeOnly MFDouble field named "vKnot". */
  public double[] getVKnot ();

  /** Provide number of primitive values in "vKnot" array */
  public int getNumVKnot ();

  /** Assign double array to initializeOnly MFDouble field named "vKnot". */
  public void setVKnot (double[] values);

  /** Assign single double value as the MFDouble array for initializeOnly field named "vKnot" */
  public void setVKnot (double value);

  /** Provide int value [2,∞) from initializeOnly SFInt32 field named "uOrder". */
  public int getUOrder ();

  /** Assign int value [2,∞) to initializeOnly SFInt32 field named "uOrder". */
  public void setUOrder (int value);

  /** Provide int value [2,∞) from initializeOnly SFInt32 field named "vOrder". */
  public int getVOrder ();

  /** Assign int value [2,∞) to initializeOnly SFInt32 field named "vOrder". */
  public void setVOrder (int value);

  /** Provide int value from inputOutput SFInt32 field named "uTessellation". */
  public int getUTessellation ();

  /** Assign int value to inputOutput SFInt32 field named "uTessellation". */
  public void setUTessellation (int value);

  /** Provide int value from inputOutput SFInt32 field named "vTessellation". */
  public int getVTessellation ();

  /** Assign int value to inputOutput SFInt32 field named "vTessellation". */
  public void setVTessellation (int value);

  /** Provide array of double results array (-∞,∞) from inputOutput MFDouble field named "weight". */
  public double[] getWeight ();

  /** Provide number of primitive values in "weight" array */
  public int getNumWeight ();

  /** Assign double array (-∞,∞) to inputOutput MFDouble field named "weight". */
  public void setWeight (double[] values);

  /** Assign single double value (-∞,∞) as the MFDouble array for inputOutput field named "weight" */
  public void setWeight (double value);

  /** Provide bool value from inputOutput SFBool field named "solid". */
  public bool getSolid ();

  /** Assign bool value to inputOutput SFBool field named "solid". */
  public void setSolid (bool value);

  /** Provide X3DCoordinateNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DCoordinateNode type field named "controlPoint". */
  public void getControlPoint (X3DNode result);

  /** Assign X3DCoordinateNode value (using a properly typed node) to inputOutput X3DCoordinateNode type field named "controlPoint". */
  public void setControlPoint (X3DCoordinateNode node);

  /** Assign X3DCoordinateNode value (using a properly typed protoInstance) */
  public void setControlPoint (X3DPrototypeInstance protoInstance);

  /** Provide X3DSingleTextureCoordinateNode|NurbsTextureCoordinate value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DSingleTextureCoordinateNode|NurbsTextureCoordinate type field named "texCoord". */
  public void getTexCoord (X3DNode result);

  /** Assign X3DSingleTextureCoordinateNode|NurbsTextureCoordinate value (using a properly typed node) to inputOutput X3DSingleTextureCoordinateNode|NurbsTextureCoordinate type field named "texCoord". */
  public void setTexCoord (X3DNode node);

  /** Assign X3DSingleTextureCoordinateNode|NurbsTextureCoordinate value (using a properly typed protoInstance) */
  public void setTexCoord (X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DOneSidedMaterialNode defines an abstract node interface that extends interfaces X3DMaterialNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for material nodes that describe how the shape looks like from one side. A different number of contanied texture nodes are allowed by each of the implementing nodes. */

public interface X3DOneSidedMaterialNode : X3DMaterialNode
{
  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "emissiveColor". */
  public void getEmissiveColor (float[] result);

  /** Assign 3-tuple float array using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "emissiveColor". */
  public void setEmissiveColor (float[] color);

  /** Provide String value from inputOutput SFString field named "emissiveTextureMapping". */
  public String getEmissiveTextureMapping ();

  /** Assign String value to inputOutput SFString field named "emissiveTextureMapping". */
  public void setEmissiveTextureMapping (String value);

  /** Provide float value [0,∞) from inputOutput SFFloat field named "normalScale". */
  public float getNormalScale ();

  /** Assign float value [0,∞) to inputOutput SFFloat field named "normalScale". */
  public void setNormalScale (float value);

  /** Provide String value from inputOutput SFString field named "normalTextureMapping". */
  public String getNormalTextureMapping ();

  /** Assign String value to inputOutput SFString field named "normalTextureMapping". */
  public void setNormalTextureMapping (String value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DParametricGeometryNode defines an abstract node interface that extends interfaces X3DGeometryNode and X3DNode.
  * Base type for all geometry node types that are created parametrically and use control points to describe the final shape of the surface. */

public interface X3DParametricGeometryNode : X3DGeometryNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DParticleEmitterNode defines an abstract node interface that extends interface X3DNode.
  * The X3DParticleEmitterNode abstract type represents any node that is an emitter of particles. */

public interface X3DParticleEmitterNode : X3DNode
{
  /** Provide bool value from inputOutput SFBool field named "on". */
  public bool getOn ();

  /** Assign bool value to inputOutput SFBool field named "on". */
  public void setOn (bool value);

  /** Provide float value [0,∞) from inputOutput SFFloat field named "speed". */
  public float getSpeed ();

  /** Assign float value [0,∞) to inputOutput SFFloat field named "speed". */
  public void setSpeed (float value);

  /** Provide float value [0,∞) from inputOutput SFFloat field named "variation". */
  public float getVariation ();

  /** Assign float value [0,∞) to inputOutput SFFloat field named "variation". */
  public void setVariation (float value);

  /** Provide float value [0,∞) from inputOutput SFFloat field named "mass". */
  public float getMass ();

  /** Assign float value [0,∞) to inputOutput SFFloat field named "mass". */
  public void setMass (float value);

  /** Provide float value [0,∞) from inputOutput SFFloat field named "surfaceArea". */
  public float getSurfaceArea ();

  /** Assign float value [0,∞) to inputOutput SFFloat field named "surfaceArea". */
  public void setSurfaceArea (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DParticlePhysicsModelNode defines an abstract node interface that extends interface X3DNode.
  * The X3DParticlePhysicsModelNode abstract type represents any node that applies a form of constraints on the particles after they have been generated. */

public interface X3DParticlePhysicsModelNode : X3DNode
{
  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DPickSensorNode defines an abstract node interface that extends interfaces X3DSensorNode, X3DChildNode, and X3DNode.
  * The X3DPickSensorNode abstract node type is the base node type that represents the lowest common denominator of picking capabilities. */

public interface X3DPickSensorNode : X3DSensorNode
{
  /** Provide String value from inputOutput SFString field named "matchCriterion". */
  public String getMatchCriterion ();

  /** Assign String value to inputOutput SFString field named "matchCriterion". */
  public void setMatchCriterion (String value);

  /** Provide array of String results array ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  public String[] getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  public int getNumObjectType ();

  /** Assign String array ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  public void setObjectType (String[] values);

  /** Provide String value from initializeOnly SFString field named "intersectionType". */
  public String getIntersectionType ();

  /** Assign String value to initializeOnly SFString field named "intersectionType". */
  public void setIntersectionType (String value);

  /** Provide String value from initializeOnly SFString field named "sortOrder". */
  public String getSortOrder ();

  /** Assign String value to initializeOnly SFString field named "sortOrder". */
  public void setSortOrder (String value);

  /** Provide String value from initializeOnly SFString field named "intersectionType". */
  public String getIntersectionType ();

  /** Assign String value to initializeOnly SFString field named "intersectionType". */
  public void setIntersectionType (String value);

  /** Provide String value from inputOutput SFString field named "matchCriterion". */
  public String getMatchCriterion ();

  /** Assign String value to inputOutput SFString field named "matchCriterion". */
  public void setMatchCriterion (String value);

  /** Provide array of String results array ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  public String[] getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  public int getNumObjectType ();

  /** Assign String array ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  public void setObjectType (String[] values);

  /** Assign single String value ["ALL","NONE","TERRAIN",...] as the MFString array for inputOutput field named "objectType" */
  public void setObjectType (String value);

  /** Provide String value from initializeOnly SFString field named "sortOrder". */
  public String getSortOrder ();

  /** Assign String value to initializeOnly SFString field named "sortOrder". */
  public void setSortOrder (String value);

  /** Provide array of X3DGroupingNode|X3DShapeNode|Inline results array (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DGroupingNode|X3DShapeNode|Inline type field named "pickTarget". */
  public void getPickTarget (X3DNode[] result);

  /** Provide number of nodes in "pickTarget" array */
  public int getNumPickTarget ();

  /** Assign X3DGroupingNode|X3DShapeNode|Inline array (using a properly typed node array) to inputOutput X3DGroupingNode|X3DShapeNode|Inline type field named "pickTarget". */
  public void setPickTarget (X3DNode[] nodes);

  /** Assign single X3DNode[] value (using a properly typed node) as the MFNode array for inputOutput field named "pickTarget" */
  public void setPickTarget (X3DNode node);

  /** Assign X3DGroupingNode|X3DShapeNode|Inline array (using a properly typed protoInstance array) to inputOutput X3DGroupingNode|X3DShapeNode|Inline type field named "pickTarget". */
  public void setPickTarget (X3DPrototypeInstance node);

  /** Provide array of X3DChildNode results array (using a properly typed node array or X3DPrototypeInstance array) from outputOnly X3DChildNode type field named "pickedGeometry". */
  public void getPickedGeometry (X3DNode[] result);

  /** Provide number of nodes in "pickedGeometry" array */
  public int getNumPickedGeometry ();

  /** Provide X3DGeometryNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DGeometryNode type field named "pickingGeometry". */
  public void getPickingGeometry (X3DNode result);

  /** Assign X3DGeometryNode value (using a properly typed node) to inputOutput X3DGeometryNode type field named "pickingGeometry". */
  public void setPickingGeometry (X3DGeometryNode node);

  /** Assign X3DGeometryNode value (using a properly typed protoInstance) */
  public void setPickingGeometry (X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DPointingDeviceSensorNode defines an abstract node interface that extends interfaces X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all pointing device sensors. */

public interface X3DPointingDeviceSensorNode : X3DSensorNode
{
  /** Provide bool value from outputOnly SFBool field named "isOver". */
  public bool getIsOver ();

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DProductStructureChildNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Base type marking nodes that are valid product structure children for the CADGeometry component. */

public interface X3DProductStructureChildNode : X3DChildNode
{
  /** Provide String value from inputOutput SFString field named "name". */
  public String getName ();

  /** Assign String value to inputOutput SFString field named "name". */
  public void setName (String value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DPrototypeInstance defines an abstract interface.
  * Base type for all prototype instances. Note that direct children nodes are disallowed, instead let fieldValue with type SFNode/MFNode contain them. Current practice is that, if desired, prototype authors must explicitly add the metadata SFNode field in the ProtoInterface. */

public interface X3DPrototypeInstance : X3DNode
{
  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DRigidJointNode defines an abstract node interface that extends interface X3DNode.
  * The X3DRigidJointNode abstract node type is the base type for all joint types. */

public interface X3DRigidJointNode : X3DNode
{
  /** Provide array of String results array from inputOutput MFString field named "forceOutput". */
  public String[] getForceOutput ();

  /** Provide number of primitive values in "forceOutput" array */
  public int getNumForceOutput ();

  /** Assign String array to inputOutput MFString field named "forceOutput". */
  public void setForceOutput (String[] values);

  /** Provide array of String results array from inputOutput MFString field named "forceOutput". */
  public String[] getForceOutput ();

  /** Provide number of primitive values in "forceOutput" array */
  public int getNumForceOutput ();

  /** Assign String array to inputOutput MFString field named "forceOutput". */
  public void setForceOutput (String[] values);

  /** Assign single String value as the MFString array for inputOutput field named "forceOutput" */
  public void setForceOutput (String value);

  /** Provide RigidBody value (using a properly typed node or X3DPrototypeInstance) from inputOutput RigidBody type field named "body1". */
  public void getBody1 (X3DNode result);

  /** Assign RigidBody value (using a properly typed node) to inputOutput RigidBody type field named "body1". */
  public void setBody1 (RigidBody node);

  /** Assign RigidBody value (using a properly typed protoInstance) */
  public void setBody1 (X3DPrototypeInstance protoInstance);

  /** Provide RigidBody value (using a properly typed node or X3DPrototypeInstance) from inputOutput RigidBody type field named "body2". */
  public void getBody2 (X3DNode result);

  /** Assign RigidBody value (using a properly typed node) to inputOutput RigidBody type field named "body2". */
  public void setBody2 (RigidBody node);

  /** Assign RigidBody value (using a properly typed protoInstance) */
  public void setBody2 (X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DScriptNode defines an abstract node interface.
  * Base type for scripting nodes (but not shader nodes). */

public interface X3DScriptNode : X3DChildNode, X3DUrlObject
{
  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide bool value from inputOutput SFBool field named "load". */
  public bool getLoad ();

  /** Assign bool value to inputOutput SFBool field named "load". */
  public void setLoad (bool value);

  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "autoRefresh". */
  public double getAutoRefresh ();

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "autoRefresh". */
  public void setAutoRefresh (double timestamp);

  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "autoRefreshTimeLimit". */
  public double getAutoRefreshTimeLimit ();

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "autoRefreshTimeLimit". */
  public void setAutoRefreshTimeLimit (double timestamp);

  /** Provide array of String results array from inputOutput MFString field named "url". */
  public String[] getUrl ();

  /** Provide number of primitive values in "url" array */
  public int getNumUrl ();

  /** Assign String array to inputOutput MFString field named "url". */
  public void setUrl (String[] values);

  /** Assign single String value as the MFString array for inputOutput field named "url" */
  public void setUrl (String value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DSensorNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Base type for all sensors. */

public interface X3DSensorNode : X3DChildNode
{
  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DSequencerNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Base type from which all Sequencers are derived. */

public interface X3DSequencerNode : X3DChildNode
{
  /** Assign bool value to inputOnly SFBool field named "next". */
  public void setNext (bool value);

  /** Assign bool value to inputOnly SFBool field named "previous". */
  public void setPrevious (bool value);

  /** Assign float value to inputOnly SFFloat field named "set_fraction". */
  public void setFraction (float value);

  /** Provide array of float results array from inputOutput MFFloat field named "key". */
  public float[] getKey ();

  /** Provide number of primitive values in "key" array */
  public int getNumKey ();

  /** Assign float array to inputOutput MFFloat field named "key". */
  public void setKey (float[] values);

  /** Assign single float value as the MFFloat array for inputOutput field named "key" */
  public void setKey (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DShaderNode defines an abstract node interface that extends interfaces X3DAppearanceChildNode and X3DNode.
  * Base type for all nodes that specify a programmable shader. */

public interface X3DShaderNode : X3DAppearanceChildNode
{
  /** Provide String value from initializeOnly SFString field named "language". */
  public String getLanguage ();

  /** Assign String value to initializeOnly SFString field named "language". */
  public void setLanguage (String value);

  /** Assign bool value to inputOnly SFBool field named "activate". */
  public void setActivate (bool value);

  /** Provide bool value from outputOnly SFBool field named "isSelected". */
  public bool getIsSelected ();

  /** Provide bool value from outputOnly SFBool field named "isValid". */
  public bool getIsValid ();

  /** Provide String value from initializeOnly SFString field named "language". */
  public String getLanguage ();

  /** Assign String value to initializeOnly SFString field named "language". */
  public void setLanguage (String value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DShapeNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Base type for all Shape nodes. */

public interface X3DShapeNode : X3DChildNode, X3DBoundedObject
{
  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxCenter". */
  public void getBboxCenter (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxCenter". */
  public void setBboxCenter (float[] value);

  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxSize". */
  public void getBboxSize (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxSize". */
  public void setBboxSize (float[] value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  public bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  public void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "castShadow". */
  public bool getCastShadow ();

  /** Assign bool value to inputOutput SFBool field named "castShadow". */
  public void setCastShadow (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  public bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  public void setVisible (bool value);

  /** Provide X3DAppearanceNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DAppearanceNode type field named "appearance". */
  public void getAppearance (X3DNode result);

  /** Assign X3DAppearanceNode value (using a properly typed node) to inputOutput X3DAppearanceNode type field named "appearance". */
  public void setAppearance (X3DAppearanceNode node);

  /** Assign X3DAppearanceNode value (using a properly typed protoInstance) */
  public void setAppearance (X3DPrototypeInstance protoInstance);

  /** Provide X3DGeometryNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DGeometryNode type field named "geometry". */
  public void getGeometry (X3DNode result);

  /** Assign X3DGeometryNode value (using a properly typed node) to inputOutput X3DGeometryNode type field named "geometry". */
  public void setGeometry (X3DGeometryNode node);

  /** Assign X3DGeometryNode value (using a properly typed protoInstance) */
  public void setGeometry (X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DSingleTextureCoordinateNode defines an abstract node interface that extends interfaces X3DTextureCoordinateNode, X3DGeometricPropertyNode, and X3DNode.
  * Base type for all texture coordinate nodes which specify texture coordinates for a single texture. */

public interface X3DSingleTextureCoordinateNode : X3DTextureCoordinateNode
{
  /** Provide String value from inputOutput SFString field named "mapping". */
  public String getMapping ();

  /** Assign String value to inputOutput SFString field named "mapping". */
  public void setMapping (String value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DSingleTextureNode defines an abstract node interface that extends interfaces X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all texture node types that define a single texture. A single texture can be used to influence a parameter of various material nodes in the Shape component, and it can be a child of MultiTexture. */

public interface X3DSingleTextureNode : X3DTextureNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DSingleTextureTransformNode defines an abstract node interface that extends interfaces X3DTextureTransformNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all texture transform nodes which specify texture coordinate transformation for a single texture. */

public interface X3DSingleTextureTransformNode : X3DTextureTransformNode
{
  /** Provide String value from inputOutput SFString field named "mapping". */
  public String getMapping ();

  /** Assign String value to inputOutput SFString field named "mapping". */
  public void setMapping (String value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DSoundChannelNode defines an abstract node interface that extends interfaces X3DSoundNode, X3DChildNode, and X3DNode.
  * Base type for all sound destination nodes, which represent the final destination of an audio signal and are what the user can ultimately hear. */

public interface X3DSoundChannelNode : X3DSoundNode
{
  /** Provide int value from outputOnly SFInt32 field named "channelCount". */
  public int getChannelCount ();

  /** Provide String value from inputOutput SFString field named "channelCountMode". */
  public String getChannelCountMode ();

  /** Assign String value to inputOutput SFString field named "channelCountMode". */
  public void setChannelCountMode (String value);

  /** Provide String value from inputOutput SFString field named "channelInterpretation". */
  public String getChannelInterpretation ();

  /** Assign String value to inputOutput SFString field named "channelInterpretation". */
  public void setChannelInterpretation (String value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  public float getGain ();

  /** Assign float value to inputOutput SFFloat field named "gain". */
  public void setGain (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DSoundDestinationNode defines an abstract node interface that extends interfaces X3DSoundNode, X3DChildNode, and X3DNode.
  * Base type for all sound destination nodes, which represent the final destination of an audio signal and are what the user can ultimately hear. */

public interface X3DSoundDestinationNode : X3DSoundNode
{
  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide int value from outputOnly SFInt32 field named "channelCount". */
  public int getChannelCount ();

  /** Provide String value from inputOutput SFString field named "channelCountMode". */
  public String getChannelCountMode ();

  /** Assign String value to inputOutput SFString field named "channelCountMode". */
  public void setChannelCountMode (String value);

  /** Provide String value from inputOutput SFString field named "channelInterpretation". */
  public String getChannelInterpretation ();

  /** Assign String value to inputOutput SFString field named "channelInterpretation". */
  public void setChannelInterpretation (String value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  public float getGain ();

  /** Assign float value to inputOutput SFFloat field named "gain". */
  public void setGain (float value);

  /** Provide String value from inputOutput SFString field named "mediaDeviceID". */
  public String getMediaDeviceID ();

  /** Assign String value to inputOutput SFString field named "mediaDeviceID". */
  public void setMediaDeviceID (String value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DSoundNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Base type for all sound nodes. */

public interface X3DSoundNode : X3DChildNode
{
  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DSoundProcessingNode defines an abstract node interface that extends interfaces X3DTimeDependentNode, X3DChildNode, and X3DNode.
  * Base type for all sound processing nodes, which are used to enhance audio with filtering, delaying, changing gain, etc. */

public interface X3DSoundProcessingNode : X3DTimeDependentNode, X3DSoundNode
{
  /** Provide int value from outputOnly SFInt32 field named "channelCount". */
  public int getChannelCount ();

  /** Provide String value from inputOutput SFString field named "channelCountMode". */
  public String getChannelCountMode ();

  /** Assign String value to inputOutput SFString field named "channelCountMode". */
  public void setChannelCountMode (String value);

  /** Provide String value from inputOutput SFString field named "channelInterpretation". */
  public String getChannelInterpretation ();

  /** Assign String value to inputOutput SFString field named "channelInterpretation". */
  public void setChannelInterpretation (String value);

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  public float getGain ();

  /** Assign float value to inputOutput SFFloat field named "gain". */
  public void setGain (float value);

  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "tailTime". */
  public double getTailTime ();

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "tailTime". */
  public void setTailTime (double timestamp);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide double value in seconds [0,∞) from outputOnly SFTime field named "elapsedTime". */
  public double getElapsedTime ();

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide bool value from outputOnly SFBool field named "isPaused". */
  public bool getIsPaused ();

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide double value in seconds from inputOutput SFTime field named "pauseTime". */
  public double getPauseTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "pauseTime". */
  public void setPauseTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "resumeTime". */
  public double getResumeTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "resumeTime". */
  public void setResumeTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "startTime". */
  public double getStartTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "startTime". */
  public void setStartTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "stopTime". */
  public double getStopTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "stopTime". */
  public void setStopTime (double timestamp);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DSoundSourceNode defines an abstract node interface that extends interfaces X3DTimeDependentNode, X3DChildNode, and X3DNode.
  * Nodes implementing X3DSoundSourceNode provide signal inputs to the audio graph. */

public interface X3DSoundSourceNode : X3DTimeDependentNode, X3DSoundNode
{
  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  public float getGain ();

  /** Assign float value to inputOutput SFFloat field named "gain". */
  public void setGain (float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide double value in seconds [0,∞) from outputOnly SFTime field named "elapsedTime". */
  public double getElapsedTime ();

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide bool value from outputOnly SFBool field named "isPaused". */
  public bool getIsPaused ();

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide double value in seconds from inputOutput SFTime field named "pauseTime". */
  public double getPauseTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "pauseTime". */
  public void setPauseTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "resumeTime". */
  public double getResumeTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "resumeTime". */
  public void setResumeTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "startTime". */
  public double getStartTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "startTime". */
  public void setStartTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "stopTime". */
  public double getStopTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "stopTime". */
  public void setStopTime (double timestamp);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DTexture2DNode defines an abstract node interface that extends interfaces X3DSingleTextureNode, X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all nodes which specify 2D sources for texture images. */

public interface X3DTexture2DNode : X3DSingleTextureNode
{
  /** Provide bool value from initializeOnly SFBool field named "repeatS". */
  public bool getRepeatS ();

  /** Assign bool value to initializeOnly SFBool field named "repeatS". */
  public void setRepeatS (bool value);

  /** Provide bool value from initializeOnly SFBool field named "repeatT". */
  public bool getRepeatT ();

  /** Assign bool value to initializeOnly SFBool field named "repeatT". */
  public void setRepeatT (bool value);

  /** Provide TextureProperties value (using a properly typed node or X3DPrototypeInstance) from initializeOnly TextureProperties type field named "textureProperties". */
  public void getTextureProperties (X3DNode result);

  /** Assign TextureProperties value (using a properly typed node) to initializeOnly TextureProperties type field named "textureProperties". */
  public void setTextureProperties (TextureProperties node);

  /** Assign TextureProperties value (using a properly typed protoInstance) */
  public void setTextureProperties (X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DTexture3DNode defines an abstract node interface that extends interfaces X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all nodes that specify 3D sources for texture images. */

public interface X3DTexture3DNode : X3DTextureNode
{
  /** Provide bool value from initializeOnly SFBool field named "repeatS". */
  public bool getRepeatS ();

  /** Assign bool value to initializeOnly SFBool field named "repeatS". */
  public void setRepeatS (bool value);

  /** Provide bool value from initializeOnly SFBool field named "repeatT". */
  public bool getRepeatT ();

  /** Assign bool value to initializeOnly SFBool field named "repeatT". */
  public void setRepeatT (bool value);

  /** Provide bool value from initializeOnly SFBool field named "repeatR". */
  public bool getRepeatR ();

  /** Assign bool value to initializeOnly SFBool field named "repeatR". */
  public void setRepeatR (bool value);

  /** Provide TextureProperties value (using a properly typed node or X3DPrototypeInstance) from initializeOnly TextureProperties type field named "textureProperties". */
  public void getTextureProperties (X3DNode result);

  /** Assign TextureProperties value (using a properly typed node) to initializeOnly TextureProperties type field named "textureProperties". */
  public void setTextureProperties (TextureProperties node);

  /** Assign TextureProperties value (using a properly typed protoInstance) */
  public void setTextureProperties (X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DTextureCoordinateNode defines an abstract node interface that extends interfaces X3DGeometricPropertyNode and X3DNode.
  * Base type for all nodes which specify texture coordinates. */

public interface X3DTextureCoordinateNode : X3DGeometricPropertyNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DTextureNode defines an abstract node interface that extends interfaces X3DAppearanceChildNode and X3DNode.
  * Base type for all nodes which specify sources for texture images. */

public interface X3DTextureNode : X3DAppearanceChildNode
{
  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DTextureProjectorNode defines an abstract node interface that extends interfaces X3DLightNode, X3DChildNode, and X3DNode.
  * Base type for all node types that specify texture projector nodes, which provide a form of lighting. */

public interface X3DTextureProjectorNode : X3DLightNode
{
  /** Provide float value (0,∞) from outputOnly SFFloat field named "aspectRatio". */
  public float getAspectRatio ();

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide array of 3-tuple float results array from inputOutput SFVec3f field named "direction". */
  public void getDirection (float[] result);

  /** Assign 3-tuple float array to inputOutput SFVec3f field named "direction". */
  public void setDirection (float[] value);

  /** Provide float value [-1,∞) from inputOutput SFFloat field named "farDistance". */
  public float getFarDistance ();

  /** Assign float value [-1,∞) to inputOutput SFFloat field named "farDistance". */
  public void setFarDistance (float value);

  /** Provide bool value from inputOutput SFBool field named "global". */
  public bool getGlobal ();

  /** Assign bool value to inputOutput SFBool field named "global". */
  public void setGlobal (bool value);

  /** Provide array of 3-tuple float results array from inputOutput SFVec3f field named "location". */
  public void getLocation (float[] result);

  /** Assign 3-tuple float array to inputOutput SFVec3f field named "location". */
  public void setLocation (float[] value);

  /** Provide float value [-1,∞) from inputOutput SFFloat field named "nearDistance". */
  public float getNearDistance ();

  /** Assign float value [-1,∞) to inputOutput SFFloat field named "nearDistance". */
  public void setNearDistance (float value);

  /** Provide X3DTexture2DNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DTexture2DNode type field named "texture". */
  public void getTexture (X3DNode result);

  /** Assign X3DTexture2DNode value (using a properly typed node) to inputOutput X3DTexture2DNode type field named "texture". */
  public void setTexture (X3DTexture2DNode node);

  /** Assign X3DTexture2DNode value (using a properly typed protoInstance) */
  public void setTexture (X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide float value from inputOutput SFFloat field named "ambientIntensity". */
  public float getAmbientIntensity ();

  /** Assign float value to inputOutput SFFloat field named "ambientIntensity". */
  public void setAmbientIntensity (float value);

  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "color". */
  public void getColor (float[] result);

  /** Assign 3-tuple float array using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "color". */
  public void setColor (float[] color);

  /** Provide float value [0,∞) from inputOutput SFFloat field named "intensity". */
  public float getIntensity ();

  /** Assign float value [0,∞) to inputOutput SFFloat field named "intensity". */
  public void setIntensity (float value);

  /** Provide bool value from inputOutput SFBool field named "on". */
  public bool getOn ();

  /** Assign bool value to inputOutput SFBool field named "on". */
  public void setOn (bool value);

  /** Provide bool value from inputOutput SFBool field named "shadows". */
  public bool getShadows ();

  /** Assign bool value to inputOutput SFBool field named "shadows". */
  public void setShadows (bool value);

  /** Provide float value from inputOutput SFFloat field named "shadowIntensity". */
  public float getShadowIntensity ();

  /** Assign float value to inputOutput SFFloat field named "shadowIntensity". */
  public void setShadowIntensity (float value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DTextureTransformNode defines an abstract node interface that extends interfaces X3DAppearanceChildNode and X3DNode.
  * Base type for all nodes which specify a transformation of texture coordinates. */

public interface X3DTextureTransformNode : X3DAppearanceChildNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DTimeDependentNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Base type from which all time-dependent nodes are derived. */

public interface X3DTimeDependentNode : X3DChildNode
{
  /** Provide double value in seconds [0,∞) from outputOnly SFTime field named "elapsedTime". */
  public double getElapsedTime ();

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide bool value from outputOnly SFBool field named "isPaused". */
  public bool getIsPaused ();

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide double value in seconds from inputOutput SFTime field named "pauseTime". */
  public double getPauseTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "pauseTime". */
  public void setPauseTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "resumeTime". */
  public double getResumeTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "resumeTime". */
  public void setResumeTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "startTime". */
  public double getStartTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "startTime". */
  public void setStartTime (double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "stopTime". */
  public double getStopTime ();

  /** Assign double value in seconds to inputOutput SFTime field named "stopTime". */
  public void setStopTime (double timestamp);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DTouchSensorNode defines an abstract node interface that extends interfaces X3DPointingDeviceSensorNode, X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all touch-style pointing device sensors. */

public interface X3DTouchSensorNode : X3DPointingDeviceSensorNode
{
  /** Provide double value in seconds from outputOnly SFTime field named "touchTime". */
  public double getTouchTime ();

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide bool value from outputOnly SFBool field named "isOver". */
  public bool getIsOver ();

  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide bool value from outputOnly SFBool field named "isActive". */
  public bool getIsActive ();

  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DTriggerNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * Base type from which all trigger nodes are derived. */

public interface X3DTriggerNode : X3DChildNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DVertexAttributeNode defines an abstract node interface that extends interfaces X3DGeometricPropertyNode and X3DNode.
  * Base type for all nodes that specify per-vertex attribute information to the shader. */

public interface X3DVertexAttributeNode : X3DGeometricPropertyNode
{
  /** Provide String value from inputOutput SFString field named "name". */
  public String getName ();

  /** Assign String value to inputOutput SFString field named "name". */
  public void setName (String value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DViewpointNode defines an abstract node interface that extends interfaces X3DBindableNode, X3DChildNode, and X3DNode.
  * Node type X3DViewpointNode defines a specific location in the local coordinate system from which the user may view the scene, and also defines a viewpoint binding stack. */

public interface X3DViewpointNode : X3DBindableNode
{
  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide bool value from inputOutput SFBool field named "jump". */
  public bool getJump ();

  /** Assign bool value to inputOutput SFBool field named "jump". */
  public void setJump (bool value);

  /** Provide array of 4-tuple float results array in radians from inputOutput SFRotation field named "orientation". */
  public float[] getOrientation ();

  /** Assign 4-tuple float array in radians to inputOutput SFRotation field named "orientation". */
  public void setOrientation (float[] value);

  /** Provide bool value from inputOutput SFBool field named "retainUserOffsets". */
  public bool getRetainUserOffsets ();

  /** Assign bool value to inputOutput SFBool field named "retainUserOffsets". */
  public void setRetainUserOffsets (bool value);

  /** Provide float value from inputOutput SFFloat field named "farDistance". */
  public float getFarDistance ();

  /** Assign float value to inputOutput SFFloat field named "farDistance". */
  public void setFarDistance (float value);

  /** Provide float value from inputOutput SFFloat field named "nearDistance". */
  public float getNearDistance ();

  /** Assign float value to inputOutput SFFloat field named "nearDistance". */
  public void setNearDistance (float value);

  /** Provide bool value from inputOutput SFBool field named "viewAll". */
  public bool getViewAll ();

  /** Assign bool value to inputOutput SFBool field named "viewAll". */
  public void setViewAll (bool value);

  /** Provide NavigationInfo value (using a properly typed node or X3DPrototypeInstance) from inputOutput NavigationInfo type field named "navigationInfo". */
  public void getNavigationInfo (X3DNode result);

  /** Assign NavigationInfo value (using a properly typed node) to inputOutput NavigationInfo type field named "navigationInfo". */
  public void setNavigationInfo (NavigationInfo node);

  /** Assign NavigationInfo value (using a properly typed protoInstance) */
  public void setNavigationInfo (X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Assign bool value to inputOnly SFBool field named "set_bind". */
  public void setBind (bool value);

  /** Provide double value in seconds from outputOnly SFTime field named "bindTime". */
  public double getBindTime ();

  /** Provide bool value from outputOnly SFBool field named "isBound". */
  public bool getIsBound ();

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DViewportNode defines an abstract node interface that extends interfaces X3DGroupingNode, X3DChildNode, and X3DNode.
  * The X3DViewportNode abstract node type is the base node type for viewport nodes. */

public interface X3DViewportNode : X3DGroupingNode
{
  // ===== methods for fields inherited from parent interfaces =====

  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxCenter". */
  public void getBboxCenter (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxCenter". */
  public void setBboxCenter (float[] value);

  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxSize". */
  public void getBboxSize (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxSize". */
  public void setBboxSize (float[] value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  public bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  public void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  public bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  public void setVisible (bool value);

  /** Assign X3DChildNode array (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  public void addChildren (X3DChildNode[] nodes);

  /** Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOnly field named "addChildren" */
  public void addChildren (X3DChildNode node);

  /** Assign X3DChildNode array (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "addChildren". */
  public void addChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode array (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  public void addChildren (X3DNode[] nodes);

  /** Assign X3DChildNode array (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  public void removeChildren (X3DChildNode[] nodes);

  /** Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOnly field named "removeChildren" */
  public void removeChildren (X3DChildNode node);

  /** Assign X3DChildNode array (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "removeChildren". */
  public void removeChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode array (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  public void removeChildren (X3DNode[] nodes);

  /** Provide array of X3DChildNode results array (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DChildNode type field named "children". */
  public void getChildren (X3DNode[] result);

  /** Provide number of nodes in "children" array */
  public int getNumChildren ();

  /** Assign X3DChildNode array (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  public void setChildren (X3DChildNode[] nodes);

  /** Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOutput field named "children" */
  public void setChildren (X3DChildNode node);

  /** Assign X3DChildNode array (using a properly typed protoInstance array) to inputOutput X3DChildNode type field named "children". */
  public void setChildren (X3DPrototypeInstance node);

  /** Assign X3DChildNode array (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  public void setChildren (X3DNode[] nodes);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DVolumeDataNode defines an abstract node interface that extends interfaces X3DChildNode and X3DNode.
  * The X3DVolumeDataNode abstract node type is the base type for all node types that describe volumetric data to be rendered. */

public interface X3DVolumeDataNode : X3DChildNode, X3DBoundedObject
{
  /** Provide array of 3-tuple float results array (-∞,∞) from inputOutput SFVec3f field named "dimensions". */
  public void getDimensions (float[] result);

  /** Assign 3-tuple float array (-∞,∞) to inputOutput SFVec3f field named "dimensions". */
  public void setDimensions (float[] value);

  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxCenter". */
  public void getBboxCenter (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxCenter". */
  public void setBboxCenter (float[] value);

  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxSize". */
  public void getBboxSize (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxSize". */
  public void setBboxSize (float[] value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  public bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  public void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  public bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  public void setVisible (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DVolumeRenderStyleNode defines an abstract node interface that extends interface X3DNode.
  * The X3DVolumeRenderStyleNode abstract node type is the base type for all node types that specify a specific visual rendering style to be used when rendering volume data. */

public interface X3DVolumeRenderStyleNode : X3DNode
{
  /** Provide bool value from inputOutput SFBool field named "enabled". */
  public bool getEnabled ();

  /** Assign bool value to inputOutput SFBool field named "enabled". */
  public void setEnabled (bool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  public void getIS (X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  public void setIS (IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  public void setIS (X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  public void getMetadata (X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  public void setMetadata (X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  public void setMetadata (X3DPrototypeInstance protoInstance);
}
/** X3DBoundedObject defines an abstract interface.
  * X3DBoundedObject indicates that bounding box values can be provided (or computed) to encompass this node and any children. */

public interface X3DBoundedObject
{
  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxCenter". */
  public void getBboxCenter (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxCenter". */
  public void setBboxCenter (float[] value);

  /** Provide array of 3-tuple float results array from initializeOnly SFVec3f field named "bboxSize". */
  public void getBboxSize (float[] result);

  /** Assign 3-tuple float array to initializeOnly SFVec3f field named "bboxSize". */
  public void setBboxSize (float[] value);

  /** Provide bool value from inputOutput SFBool field named "bboxDisplay". */
  public bool getBboxDisplay ();

  /** Assign bool value to inputOutput SFBool field named "bboxDisplay". */
  public void setBboxDisplay (bool value);

  /** Provide bool value from inputOutput SFBool field named "visible". */
  public bool getVisible ();

  /** Assign bool value to inputOutput SFBool field named "visible". */
  public void setVisible (bool value);
}
/** X3DFogObject defines an abstract interface.
  * Abstract type describing a node that influences the lighting equation through the use of fog semantics. */

public interface X3DFogObject
{
  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "color". */
  public void getColor (float[] result);

  /** Assign 3-tuple float array using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "color". */
  public void setColor (float[] color);

  /** Provide String value from inputOutput SFString field named "fogType". */
  public String getFogType ();

  /** Assign String value to inputOutput SFString field named "fogType". */
  public void setFogType (String value);

  /** Provide float value [0,∞) from inputOutput SFFloat field named "visibilityRange". */
  public float getVisibilityRange ();

  /** Assign float value [0,∞) to inputOutput SFFloat field named "visibilityRange". */
  public void setVisibilityRange (float value);
}
/** X3DMetadataObject defines an abstract interface.
  * Each node inheriting the X3DMetadataObject interface contains a single array of strictly typed values: MFBool, MFInt32, MFFloat, MFDouble, MFString, or MFNode, the latter having children that are all Metadata nodes. */

public interface X3DMetadataObject
{
  /** Provide String value from inputOutput SFString field named "name". */
  public String getName ();

  /** Assign String value to inputOutput SFString field named "name". */
  public void setName (String value);

  /** Provide String value from inputOutput SFString field named "reference". */
  public String getReference ();

  /** Assign String value to inputOutput SFString field named "reference". */
  public void setReference (String value);
}
/** X3DPickableObject defines an abstract interface.
  * The X3DPickableObject abstract interface marks a node as being capable of having customized picking performed on its contents or children. */

public interface X3DPickableObject
{
  /** Provide array of String results array ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  public String[] getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  public int getNumObjectType ();

  /** Assign String array ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  public void setObjectType (String[] values);

  /** Provide array of String results array ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  public String[] getObjectType ();

  /** Provide number of primitive values in "objectType" array */
  public int getNumObjectType ();

  /** Assign String array ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  public void setObjectType (String[] values);

  /** Assign single String value ["ALL","NONE","TERRAIN",...] as the MFString array for inputOutput field named "objectType" */
  public void setObjectType (String value);

  /** Provide bool value from inputOutput SFBool field named "pickable". */
  public bool getPickable ();

  /** Assign bool value to inputOutput SFBool field named "pickable". */
  public void setPickable (bool value);
}
/** X3DProgrammableShaderObject defines an abstract interface.
  * Base type for all nodes that specify arbitrary fields for interfacing with per-object attribute values. */

public interface X3DProgrammableShaderObject
{}
/** X3DUrlObject defines an abstract interface.
  * X3DUrlObject indicates that a node has content loaded from a Uniform Resource Locator (URL) and can be tracked via a LoadSensor. Such child nodes have containerField='children' to indicate their relationship to the parent LoadSensor node. */

public interface X3DUrlObject
{
  /** Provide String value from inputOutput SFString field named "description". */
  public String getDescription ();

  /** Assign String value to inputOutput SFString field named "description". */
  public void setDescription (String value);

  /** Provide bool value from inputOutput SFBool field named "load". */
  public bool getLoad ();

  /** Assign bool value to inputOutput SFBool field named "load". */
  public void setLoad (bool value);

  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "autoRefresh". */
  public double getAutoRefresh ();

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "autoRefresh". */
  public void setAutoRefresh (double timestamp);

  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "autoRefreshTimeLimit". */
  public double getAutoRefreshTimeLimit ();

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "autoRefreshTimeLimit". */
  public void setAutoRefreshTimeLimit (double timestamp);

  /** Provide array of String results array from inputOutput MFString field named "url". */
  public String[] getUrl ();

  /** Provide number of primitive values in "url" array */
  public int getNumUrl ();

  /** Assign String array to inputOutput MFString field named "url". */
  public void setUrl (String[] values);

  /** Assign single String value as the MFString array for inputOutput field named "url" */
  public void setUrl (String value);
}
public interface X3DFieldTypes {

    public int INPUT_ONLY = 1;
    public int INITIALIZE_ONLY = 2;
    public int INPUT_OUTPUT = 3;
    public int OUTPUT_ONLY = 4;

    public int SFBOOL = 1;
    public int MFBOOL = 2;
    public int SFCOLOR = 21;
    public int MFCOLOR = 22;
    public int SFCOLORRGBA = 23;
    public int MFCOLORRGBA = 24;
    public int SFDOUBLE = 7;
    public int MFDOUBLE = 8;
    public int SFFLOAT = 5;
    public int MFFLOAT = 6;
    public int SFIMAGE = 25;
    public int MFIMAGE = 26;
    public int SFINT32 = 3;
    public int MFINT32 = 4;
    public int SFNODE = 11;
    public int MFNODE = 12;
    public int SFROTATION = 19;
    public int MFROTATION = 20;
    public int SFSTRING = 27;
    public int MFSTRING = 28;
    public int SFTIME = 9;
    public int MFTIME = 10;
    public int SFVEC2F = 13;
    public int MFVEC2F = 14;
    public int SFVEC3F = 15;
    public int MFVEC3F = 16;
    public int SFVEC3D = 17;
    public int MFVEC3D = 18;
}
public class X3DFieldEvent {

    public X3DFieldEvent(Object src, double ts, Object data);

    public double getTime();

    public Object getData();
}
public class X3DFieldEventListener {
    public void readableFieldChanged(X3DFieldEvent evt);
}
public interface X3DFieldDefinition {

    public String getName();

    public int getAccessType();

    public int getFieldType();

    public String getFieldTypeString();
}
public interface X3DField {

    public X3DFieldDefinition getDefinition();

    public bool isReadable();

    public bool isWritable();

    public void addX3DEventListener(X3DFieldEventListener l);

    public void removeX3DEventListener(X3DFieldEventListener l);

    public void setUserData(Object data);

    public Object getUserData();
}
public interface MField : X3DField {

    public int size();

    public void clear();

    public void remove(int index);
}
/** SFBool defines a node type interface.
  * SFBool is a logical type with possible values (true|false) to match the XML boolean type. Hint: XML boolean values are lower case (true|false) in order to maintain compatibility with HTML and other XML documents. */

public interface SFBool : X3DField
{
  /** Provide bool value from type SFBool */
  public bool getValue ();

  /** Provide bool value from type SFBool */
  public void setValue (bool value);
}
/** MFBool defines a node type interface.
  * MFBool is an array of boolean values. Type MFBool was previously undefined in the VRML97 Specification, but nevertheless needed for event utilities and scripting. Example use: MFBool is useful for defining a series of behavior states using a BooleanSequencer prototype. Hint: XML boolean values are lower case (true|false) in order to maintain compatibility with HTML and other XML documents. */

public interface MFBool : MField
{
  /** Provide array of bool results array from type MFBool */
  public bool[] getValue ();

  /** Utility method to provide single value from MFBool array */
  public bool get1Value (int index);

  /** Provide array of bool results array from type MFBool */
  public void setValue (int size, bool[] values);

  /** Utility method to set a single value in MFBool array */
  public void set1Value (int index, bool value);

  /** Utility method to append a single value to MFBool array */
  public void append (bool value);

  /** Utility method to insert a single value in MFBool array */
  public void insertValue (int index, bool value) ;
}
/** SFColor defines a node type interface.
  * SFColor specifies one RGB (red-green-blue) color triple, where each color value is an RGB triple of floating point numbers in range [0,1]. The default value of an uninitialized SFColor field is (0 0 0). Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFColor : X3DField
{
  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from type SFColor */
  public void getValue (float[] result);

  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from type SFColor */
  public void setValue (float[] color);
}
/** MFColor defines a node type interface.
  * MFColor specifies zero or more SFColor RGB triples, where each color value is an RGB triple of floating point numbers in range [0,1]. The default value of an uninitialized MFColor field is the empty list. Individual SFColor array values are optionally separated by commas in XML syntax. */

public interface MFColor : MField
{
  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from type MFColor */
  public void getValue (float[] result);

  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from type MFColor */
  public void getValue (float[][] result); // overloaded method for convenience

  /** Utility method to provide single 3-tuple value from MFColor array */
  public void get1Value (int index, float[] result);

  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from type MFColor */
  public void setValue (int size, float[] colors);

  /** Provide array of 3-tuple float results array using RGB values [0..1] using RGB values [0..1] from type MFColor */
  public void setValue (float[][] colors); // overloaded method for convenience

  /** Utility method to set a single 3-tuple value in MFColor array */
  public void set1Value (int index, float[] color);

  /** Utility method to append a single 3-tuple value to MFColor array */
  public void append (float[] color);

  /** Utility method to insert a single 3-tuple value in MFColor array */
  public void insertValue (int index, float[] color) ;
}
/** SFColorRGBA defines a node type interface.
  * SFColorRGBA specifies one RGBA (red-green-blue-alpha) color 4-tuple, where each color value is an RGBA 4-tuple of floating point numbers in range [0,1]. Alpha (opacity) values = (1 - transparency). The default value of an uninitialized SFColorRGBA field is (0 0 0 0). Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFColorRGBA : X3DField
{
  /** Provide array of 4-tuple float results array using RGBA values [0..1] using RGB values [0..1] from type SFColorRGBA */
  public void getValue (float[] result);

  /** Provide array of 4-tuple float results array using RGBA values [0..1] using RGB values [0..1] from type SFColorRGBA */
  public void setValue (float[] color);
}
/** MFColorRGBA defines a node type interface.
  * MFColorRGBA specifies zero or more SFColorRGBA 4-tuples, where each color value is an RGBA 4-tuple of floating point numbers in range [0,1]. Alpha (opacity) values = (1 - transparency). The default value of an uninitialized MFColor field is the empty list. Individual SFColorRGBA array values are optionally separated by commas in XML syntax. */

public interface MFColorRGBA : MField
{
  /** Provide array of 4-tuple float results array using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  public void getValue (float[] result);

  /** Provide array of 4-tuple float results array using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  public void getValue (float[][] result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFColorRGBA array */
  public void get1Value (int index, float[] result);

  /** Provide array of 4-tuple float results array using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  public void setValue (int size, float[] colors);

  /** Provide array of 4-tuple float results array using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  public void setValue (float[][] colors); // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFColorRGBA array */
  public void set1Value (int index, float[] color);

  /** Utility method to append a single 4-tuple value to MFColorRGBA array */
  public void append (float[] color);

  /** Utility method to insert a single 4-tuple value in MFColorRGBA array */
  public void insertValue (int index, float[] color) ;
}
/** SFDouble defines a node type interface.
  * SFDouble is a double-precision floating-point type. Array values are optionally separated by commas in XML syntax. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision for rationale. */

public interface SFDouble : X3DField
{
  /** Provide double value from type SFDouble */
  public double getValue ();

  /** Provide double value from type SFDouble */
  public void setValue (double value);
}
/** MFDouble defines a node type interface.
  * MFDouble is an array of Double values, meaning a double-precision floating-point array type. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision for rationale. Array values are optionally separated by commas in XML syntax. */

public interface MFDouble : MField
{
  /** Provide array of double results array from type MFDouble */
  public double[] getValue ();

  /** Utility method to provide single value from MFDouble array */
  public double get1Value (int index);

  /** Provide array of double results array from type MFDouble */
  public void setValue (int size, double[] values);

  /** Utility method to set a single value in MFDouble array */
  public void set1Value (int index, double value);

  /** Utility method to append a single value to MFDouble array */
  public void append (double value);

  /** Utility method to insert a single value in MFDouble array */
  public void insertValue (int index, double value) ;
}
/** SFFloat defines a node type interface.
  * SFFloat is a single-precision floating-point type. */

public interface SFFloat : X3DField
{
  /** Provide float value from type SFFloat */
  public float getValue ();

  /** Provide float value from type SFFloat */
  public void setValue (float value);
}
/** MFFloat defines a node type interface.
  * MFFloat is an array of SFFloat values, meaning a single-precision floating-point array type. Array values are optionally separated by commas in XML syntax. */

public interface MFFloat : MField
{
  /** Provide array of float results array from type MFFloat */
  public float[] getValue ();

  /** Utility method to provide single value from MFFloat array */
  public float get1Value (int index);

  /** Provide array of float results array from type MFFloat */
  public void setValue (int size, float[] values);

  /** Utility method to set a single value in MFFloat array */
  public void set1Value (int index, float value);

  /** Utility method to append a single value to MFFloat array */
  public void append (float value);

  /** Utility method to insert a single value in MFFloat array */
  public void insertValue (int index, float value) ;
}
/** SFImage defines a node type interface.
  * SFImage specifies a single uncompressed 2-dimensional pixel image. SFImage fields contain three integers representing the width, height and number of components in the image, followed by (width x height) hexadecimal or integer values representing the pixels in the image. */

public interface SFImage : X3DField
{
    /** Get image width in pixels */
    public int getWidth ();

    /** Get image height in pixels */
    public int getHeight ();

    /** Get number of components in an image:
      * 1 (intensity), 2 (intensity alpha), 3 (red green blue), 4 (red green blue alpha-opacity).*/
    public int getComponents();

    /** Get array of pixel values [0-255] */
    public void getPixels (int[] pixels);

    /** Get java.awt.image.WritableRenderedImage version of image */
    public  java.awt.image.WritableRenderedImage getImage();

    /** Initialize image */
    public void setValue (int width,
                          int height,
                          int components,
                          int[] pixels);

    /** Assign a new image as current image */
    public void setImage (RenderedImage image);

    /** Assign a portion of a new image as part of current image */
    public void setSubImage (RenderedImage image,
                             int srcWidth,
                             int srcHeight,
                             int srcXOffset,
                             int srcYOffset,
                             int destXOffset,
                             int destYOffset);
}
/** MFImage defines a node type interface.
  * MFImage is an array of SFImage values. */

public interface MFImage : MField
{
    /** Get selected image width in pixels */
    public int getWidth (int imageIndex) throws ArrayIndexOutOfBoundsException;

    /** Get selected image height in pixels */
    public int getHeight (int imageIndex) throws ArrayIndexOutOfBoundsException;

    /** Get number of components in selected image:
      * 1 (intensity), 2 (intensity alpha), 3 (red green blue), 4 (red green blue alpha-opacity).*/
    public int getComponents (int imageIndex) throws ArrayIndexOutOfBoundsException;

    /** Get array of pixel values [0-255] in selected image */
    public void getPixels (int imageIndex, int[] pixels) throws ArrayIndexOutOfBoundsException;

    /** Get <a href="http://docs.oracle.com/javase/8/docs/api/java/awt/image/WritableRenderedImage.html">java.awt.image.WritableRenderedImage</a> version of selected image */
    public WritableRenderedImage getImage(int imageIndex) throws ArrayIndexOutOfBoundsException;

    /** Assign a new image as a replacement image within the current image array */
    public void setImage (int imageIndex, RenderedImage img) throws ArrayIndexOutOfBoundsException;

    /** Assign a portion of a new image as part of current selected image in array */
    public void setSubImage (int imageIndex,
                             RenderedImage img,
                             int srcWidth,
                             int srcHeight,
                             int srcXOffset,
                             int srcYOffset,
                             int destXOffset,
                             int destYOffset) throws ArrayIndexOutOfBoundsException;

    /** Utility method to set all values for selected image in array */
    public void set1Value (int imageIndex, int value) throws ArrayIndexOutOfBoundsException;

    /** Initialize selected image */
    public void set1Value (int imageIndex,
                           int width,
                           int height,
                           int components,
                           int[] pixels) throws ArrayIndexOutOfBoundsException;

    /** Utility method to set all values for all images in array */
    public void setValue (int[] value);

    /** Assign a new image array as current image array */
    public void setImage (RenderedImage[] img);

    /** Append a new image to current image array */
    public void append (RenderedImage value);

    /** Insert a new image in the current image array */
    public void insertValue (int imageIndex, RenderedImage value) throws ArrayIndexOutOfBoundsException;
}
/** SFInt32 defines a node type interface.
  * SFInt32 specifies one 32-bit signed integer. */

public interface SFInt32 : X3DField
{
  /** Provide int value from type SFInt32 */
  public int getValue ();

  /** Provide int value from type SFInt32 */
  public void setValue (int value);
}
/** MFInt32 defines a node type interface.
  * MFInt32 defines an array of 32-bit signed integers. Array values are optionally separated by commas in XML syntax. */

public interface MFInt32 : MField
{
  /** Provide MFInt32 value from type MFInt32 */
  public MFInt32 getValue ();

  /** Utility method to provide single value from MFInt32 array */
  public int get1Value (int index);

  /** Provide MFInt32 value from type MFInt32 */
  public void setValue (int size, MFInt32 values);

  /** Utility method to set a single value in MFInt32 array */
  public void set1Value (int index, int value);

  /** Utility method to append a single value to MFInt32 array */
  public void append (int value);

  /** Utility method to insert a single value in MFInt32 array */
  public void insertValue (int index, int value) ;
}
/** SFRotation defines a node type interface.
  * SFRotation is an axis-angle 4-tuple, indicating X-Y-Z direction axis plus angle orientation about that axis. The first three values specify a normalized axis vector about which the rotation takes place, so the first three values shall be within the range [-1..+1] in order to represent a normalized unit vector. The fourth value specifies the amount of right-handed rotation about that axis in radians. Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFRotation : X3DField
{
  /** Provide array of 4-tuple float results array in radians from type SFRotation */
  public float[] getValue ();

  /** Provide array of 4-tuple float results array in radians from type SFRotation */
  public void setValue (float[] angle);
}
/** MFRotation defines a node type interface.
  * MFRotation is an array of SFRotation values. Individual singleton SFRotation array values are optionally separated by commas in XML syntax. */

public interface MFRotation : MField
{
  /** Provide array of 4-tuple float results array in radians from type MFRotation */
  public float[] getValue ();

  /** Provide array of 4-tuple float results array in radians from type MFRotation */
  public void getValue (float[][] result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFRotation array */
  public float[] get1Value (int index);

  /** Provide array of 4-tuple float results array in radians from type MFRotation */
  public void setValue (int size, float[] angles);

  /** Provide array of 4-tuple float results array in radians from type MFRotation */
  public void setValue (float[][] angles); // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFRotation array */
  public void set1Value (int index, float[] angle);

  /** Utility method to append a single 4-tuple value to MFRotation array */
  public void append (float[] angle);

  /** Utility method to insert a single 4-tuple value in MFRotation array */
  public void insertValue (int index, float[] angle) ;
}
/** SFString defines a node type interface.
  * SFString defines a single string encoded with the UTF-8 universal character set. */

public interface SFString : X3DField
{
  /** Provide String value from type SFString */
  public String getValue ();

  /** Provide String value from type SFString */
  public void setValue (String value);
}
/** MFString defines a node type interface.
  * MFString is an array of SFString values, each "quoted" and separated by whitespace. Individual SFString array values are optionally separated by commas in XML syntax. */

public interface MFString : MField
{
  /** Provide array of String results array from type MFString */
  public String[] getValue ();

  /** Utility method to provide single value from MFString array */
  public String get1Value (int index);

  /** Provide array of String results array from type MFString */
  public void setValue (int size, String[] values);

  /** Utility method to set a single value in MFString array */
  public void set1Value (int index, String value);

  /** Utility method to append a single value to MFString array */
  public void append (String value);

  /** Utility method to insert a single value in MFString array */
  public void insertValue (int index, String value) ;
}
/** SFTime defines a node type interface.
  * SFTime specifies a single time value, expressed as a double-precision floating point number. Typically, SFTime fields represent the number of seconds since Jan 1, 1970, 00:00:00 GMT. */

public interface SFTime : X3DField
{
  /** Provide double value in seconds from type SFTime */
  public double getValue ();

  /** Provide long value in nanoseconds from type SFTime */
  public long getJavaValue ();

  /** Provide double value in seconds from type SFTime */
  public void setValue (double timestamp);

  /** Assign long value in nanoseconds using System.nanoTime() to type SFTime */
  public void setValue (long value);
}
/** MFTime defines a node type interface.
  * MFTime is an array of SFTime values. Array values are optionally separated by commas in XML syntax. */

public interface MFTime : MField
{
  /** Provide array of double results array in seconds from type MFTime */
  public double[] getValue ();

  /** Utility method to provide single value from MFTime array */
  public double get1Value (int index);

  /** Utility method to provide single long value in nanoseconds from MFTime array */
  public long get1JavaValue (int index);

  /** Provide array of double results array in seconds from type MFTime */
  public void setValue (int size, double[] timestamps);

  /** Assign long array in nanoseconds to type MFTime */
  public void setValue (int size, long[] values);

  /** Utility method to set a single value in MFTime array */
  public void set1Value (int index, double timestamp);

  /** Utility method to set a single long value in nanoseconds using System.nanoTime() in MFTime array */
  public void set1Value (int index, long value);

  /** Utility method to append a single value to MFTime array */
  public void append (double timestamp);

  /** Utility method to insert a single value in MFTime array */
  public void insertValue (int index, double timestamp) ;
}
/** SFVec2f defines a node type interface.
  * SFVec2f is a 2-tuple pair of SFFloat values. Hint: SFVec2f can be used to specify a 2D single-precision coordinate. Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFVec2f : X3DField
{
  /** Provide array of 2-tuple float results array from type SFVec2f */
  public void getValue (float[] result);

  /** Provide array of 2-tuple float results array from type SFVec2f */
  public void setValue (float[] value);
}
/** MFVec2f defines a node type interface.
  * MFVec2f is an array of SFVec2f values. Individual singleton SFVec2f array values are optionally separated by commas in XML syntax. */

public interface MFVec2f : MField
{
  /** Provide array of 2-tuple float results array from type MFVec2f */
  public void getValue (float[] result);

  /** Provide array of 2-tuple float results array from type MFVec2f */
  public void getValue (float[][] result); // overloaded method for convenience

  /** Utility method to provide single 2-tuple value from MFVec2f array */
  public void get1Value (int index, float[] result);

  /** Provide array of 2-tuple float results array from type MFVec2f */
  public void setValue (int size, float[] values);

  /** Provide array of 2-tuple float results array from type MFVec2f */
  public void setValue (float[][] values); // overloaded method for convenience

  /** Utility method to set a single 2-tuple value in MFVec2f array */
  public void set1Value (int index, float[] value);

  /** Utility method to append a single 2-tuple value to MFVec2f array */
  public void append (float[] value);

  /** Utility method to insert a single 2-tuple value in MFVec2f array */
  public void insertValue (int index, float[] value) ;
}
/** SFVec2d defines a node type interface.
  * SFVec2d is a 2-tuple pair of SFDouble values. Hint: SFVec2d can be used to specify a 2D double-precision coordinate. Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFVec2d : X3DField
{
  /** Provide array of 2-tuple double results array from type SFVec2d */
  public void getValue (double[] result);

  /** Provide array of 2-tuple double results array from type SFVec2d */
  public void setValue (double[] value);
}
/** MFVec2d defines a node type interface.
  * MFVec2d is an array of SFVec2d values. Individual singleton SFVec2d array values are optionally separated by commas in XML syntax. */

public interface MFVec2d : MField
{
  /** Provide array of 2-tuple double results array from type MFVec2d */
  public void getValue (double[] result);

  /** Provide array of 2-tuple double results array from type MFVec2d */
  public void getValue (double[][] result); // overloaded method for convenience

  /** Utility method to provide single 2-tuple value from MFVec2d array */
  public void get1Value (int index, double[] result);

  /** Provide array of 2-tuple double results array from type MFVec2d */
  public void setValue (int size, double[] values);

  /** Provide array of 2-tuple double results array from type MFVec2d */
  public void setValue (double[][] values); // overloaded method for convenience

  /** Utility method to set a single 2-tuple value in MFVec2d array */
  public void set1Value (int index, double[] value);

  /** Utility method to append a single 2-tuple value to MFVec2d array */
  public void append (double[] value);

  /** Utility method to insert a single 2-tuple value in MFVec2d array */
  public void insertValue (int index, double[] value) ;
}
/** SFVec3f defines a node type interface.
  * SFVec3f is a 3-tuple triplet of SFFloat values. Hint: SFVec3f can be used to specify a 3D coordinate or a 3D scale value. Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFVec3f : X3DField
{
  /** Provide array of 3-tuple float results array from type SFVec3f */
  public void getValue (float[] result);

  /** Provide array of 3-tuple float results array from type SFVec3f */
  public void setValue (float[] value);
}
/** MFVec3f defines a node type interface.
  * MFVec3f is an array of SFVec3f values. Individual singleton SFVec3f array values are optionally separated by commas in XML syntax. */

public interface MFVec3f : MField
{
  /** Provide array of 3-tuple float results array from type MFVec3f */
  public void getValue (float[] result);

  /** Provide array of 3-tuple float results array from type MFVec3f */
  public void getValue (float[][] result); // overloaded method for convenience

  /** Utility method to provide single 3-tuple value from MFVec3f array */
  public void get1Value (int index, float[] result);

  /** Provide array of 3-tuple float results array from type MFVec3f */
  public void setValue (int size, float[] values);

  /** Provide array of 3-tuple float results array from type MFVec3f */
  public void setValue (float[][] values); // overloaded method for convenience

  /** Utility method to set a single 3-tuple value in MFVec3f array */
  public void set1Value (int index, float[] value);

  /** Utility method to append a single 3-tuple value to MFVec3f array */
  public void append (float[] value);

  /** Utility method to insert a single 3-tuple value in MFVec3f array */
  public void insertValue (int index, float[] value) ;
}
/** SFVec3d defines a node type interface.
  * SFVec3d is a 3-tuple triplet of SFDouble values. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision. Hint: SFVec3d can be used to specify a georeferenced 3D coordinate. Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFVec3d : X3DField
{
  /** Provide array of 3-tuple double results array from type SFVec3d */
  public void getValue (double[] result);

  /** Provide array of 3-tuple double results array from type SFVec3d */
  public void setValue (double[] value);
}
/** MFVec3d defines a node type interface.
  * MFVec3d is an array of SFVec3d values. Individual singleton SFVec3d array values are optionally separated by commas in XML syntax. Original rationale for inclusion: GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision. Hint: MFVec3d can be used to specify a list of georeferenced 3D coordinates. */

public interface MFVec3d : MField
{
  /** Provide array of 3-tuple double results array from type MFVec3d */
  public void getValue (double[] result);

  /** Provide array of 3-tuple double results array from type MFVec3d */
  public void getValue (double[][] result); // overloaded method for convenience

  /** Utility method to provide single 3-tuple value from MFVec3d array */
  public void get1Value (int index, double[] result);

  /** Provide array of 3-tuple double results array from type MFVec3d */
  public void setValue (int size, double[] values);

  /** Provide array of 3-tuple double results array from type MFVec3d */
  public void setValue (double[][] values); // overloaded method for convenience

  /** Utility method to set a single 3-tuple value in MFVec3d array */
  public void set1Value (int index, double[] value);

  /** Utility method to append a single 3-tuple value to MFVec3d array */
  public void append (double[] value);

  /** Utility method to insert a single 3-tuple value in MFVec3d array */
  public void insertValue (int index, double[] value) ;
}
/** SFVec4f defines a node type interface.
  * SFVec4f is a 4-tuple set of single-precision floating-point values, specifying a 3D homogeneous vector. Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFVec4f : X3DField
{
  /** Provide array of 4-tuple float results array from type SFVec4f */
  public void getValue (float[] result);

  /** Provide array of 4-tuple float results array from type SFVec4f */
  public void setValue (float[] value);
}
/** MFVec4f defines a node type interface.
  * MFVec4f is zero or more SFVec4f values. Individual singleton SFVec4f array values are optionally separated by commas in XML syntax. */

public interface MFVec4f : MField
{
  /** Provide array of 4-tuple float results array from type MFVec4f */
  public void getValue (float[] result);

  /** Provide array of 4-tuple float results array from type MFVec4f */
  public void getValue (float[][] result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFVec4f array */
  public void get1Value (int index, float[] result);

  /** Provide array of 4-tuple float results array from type MFVec4f */
  public void setValue (int size, float[] values);

  /** Provide array of 4-tuple float results array from type MFVec4f */
  public void setValue (float[][] values); // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFVec4f array */
  public void set1Value (int index, float[] value);

  /** Utility method to append a single 4-tuple value to MFVec4f array */
  public void append (float[] value);

  /** Utility method to insert a single 4-tuple value in MFVec4f array */
  public void insertValue (int index, float[] value) ;
}
/** SFVec4d defines a node type interface.
  * SFVec4d is a 4-tuple set of double-precision floating-point values, specifying a 3D homogeneous vector. Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFVec4d : X3DField
{
  /** Provide array of 4-tuple double results array from type SFVec4d */
  public void getValue (double[] result);

  /** Provide array of 4-tuple double results array from type SFVec4d */
  public void setValue (double[] value);
}
/** MFVec4d defines a node type interface.
  * MFVec4d is zero or more SFVec4d values. Individual singleton SFVec4d array values are optionally separated by commas in XML syntax. */

public interface MFVec4d : MField
{
  /** Provide array of 4-tuple double results array from type MFVec4d */
  public void getValue (double[] result);

  /** Provide array of 4-tuple double results array from type MFVec4d */
  public void getValue (double[][] result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFVec4d array */
  public void get1Value (int index, double[] result);

  /** Provide array of 4-tuple double results array from type MFVec4d */
  public void setValue (int size, double[] values);

  /** Provide array of 4-tuple double results array from type MFVec4d */
  public void setValue (double[][] values); // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFVec4d array */
  public void set1Value (int index, double[] value);

  /** Utility method to append a single 4-tuple value to MFVec4d array */
  public void append (double[] value);

  /** Utility method to insert a single 4-tuple value in MFVec4d array */
  public void insertValue (int index, double[] value) ;
}
/** SFMatrix3f defines a node type interface.
  * SFMatrix3f specifies a 3x3 matrix of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFMatrix3f : X3DField
{
  /** Provide array of float results array from type SFMatrix3f */
  public float[] getValue ();

  /** Provide array of float results array from type SFMatrix3f */
  public void setValue (float[] value);
}
/** MFMatrix3f defines a node type interface.
  * MFMatrix3f specifies zero or more 3x3 matrices of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 9-tuple values. */

public interface MFMatrix3f : MField
{
  /** Provide array of float results array from type MFMatrix3f */
  public float[] getValue ();

  /** Provide array of float results array from type MFMatrix3f */
  public void getValue (float[][] result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix3f array */
  public float[] get1Value (int index);

  /** Provide array of float results array from type MFMatrix3f */
  public void setValue (int size, float[] values);

  /** Provide array of float results array from type MFMatrix3f */
  public void setValue (float[][] values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix3f array */
  public void set1Value (int index, float[] value);

  /** Utility method to append a single value to MFMatrix3f array */
  public void append (float[] value);

  /** Utility method to insert a single value in MFMatrix3f array */
  public void insertValue (int index, float[] value) ;
}
/** SFMatrix3d defines a node type interface.
  * SFMatrix3d specifies a 3x3 matrix of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFMatrix3d : X3DField
{
  /** Provide array of double results array from type SFMatrix3d */
  public double[] getValue ();

  /** Provide array of double results array from type SFMatrix3d */
  public void setValue (double[] value);
}
/** MFMatrix3d defines a node type interface.
  * MFMatrix3d specifies zero or more 3x3 matrices of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 9-tuple values. */

public interface MFMatrix3d : MField
{
  /** Provide array of double results array from type MFMatrix3d */
  public double[] getValue ();

  /** Provide array of double results array from type MFMatrix3d */
  public void getValue (double[][] result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix3d array */
  public double[] get1Value (int index);

  /** Provide array of double results array from type MFMatrix3d */
  public void setValue (int size, double[] values);

  /** Provide array of double results array from type MFMatrix3d */
  public void setValue (double[][] values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix3d array */
  public void set1Value (int index, double[] value);

  /** Utility method to append a single value to MFMatrix3d array */
  public void append (double[] value);

  /** Utility method to insert a single value in MFMatrix3d array */
  public void insertValue (int index, double[] value) ;
}
/** SFMatrix4f defines a node type interface.
  * SFMatrix4f specifies a 4x4 matrix of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFMatrix4f : X3DField
{
  /** Provide array of float results array from type SFMatrix4f */
  public float[] getValue ();

  /** Provide array of float results array from type SFMatrix4f */
  public void setValue (float[] value);
}
/** MFMatrix4f defines a node type interface.
  * MFMatrix4f specifies zero or more 4x4 matrices of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 16-tuple values. */

public interface MFMatrix4f : MField
{
  /** Provide array of float results array from type MFMatrix4f */
  public float[] getValue ();

  /** Provide array of float results array from type MFMatrix4f */
  public void getValue (float[][] result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix4f array */
  public float[] get1Value (int index);

  /** Provide array of float results array from type MFMatrix4f */
  public void setValue (int size, float[] values);

  /** Provide array of float results array from type MFMatrix4f */
  public void setValue (float[][] values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix4f array */
  public void set1Value (int index, float[] value);

  /** Utility method to append a single value to MFMatrix4f array */
  public void append (float[] value);

  /** Utility method to insert a single value in MFMatrix4f array */
  public void insertValue (int index, float[] value) ;
}
/** SFMatrix4d defines a node type interface.
  * SFMatrix4d specifies a 4x4 matrix of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

public interface SFMatrix4d : X3DField
{
  /** Provide array of double results array from type SFMatrix4d */
  public double[] getValue ();

  /** Provide array of double results array from type SFMatrix4d */
  public void setValue (double[] value);
}
/** MFMatrix4d defines a node type interface.
  * MFMatrix4d specifies zero or more 4x4 matrices of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 16-tuple values. */

public interface MFMatrix4d : MField
{
  /** Provide array of double results array from type MFMatrix4d */
  public double[] getValue ();

  /** Provide array of double results array from type MFMatrix4d */
  public void getValue (double[][] result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix4d array */
  public double[] get1Value (int index);

  /** Provide array of double results array from type MFMatrix4d */
  public void setValue (int size, double[] values);

  /** Provide array of double results array from type MFMatrix4d */
  public void setValue (double[][] values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix4d array */
  public void set1Value (int index, double[] value);

  /** Utility method to append a single value to MFMatrix4d array */
  public void append (double[] value);

  /** Utility method to insert a single value in MFMatrix4d array */
  public void insertValue (int index, double[] value) ;
}
/** SFNode defines a node type interface.
  * SFNode specifies an X3D node; the default empty value of an uninitialized SFNode field is sometimes described as NULL. */

public interface SFNode : X3DField
{
  /** Provide X3DNode value (using a properly typed node or X3DPrototypeInstance) from type SFNode */
  public void getValue (X3DNode result);

  /** Provide X3DNode value (using a properly typed node or X3DPrototypeInstance) from type SFNode */
  public void setValue (X3DNode node);
}
/** MFNode defines a node type interface.
  * MFNode specifies zero or more nodes; the default value of an MFNode field is the empty list. */

public interface MFNode : MField
{
  /** Provide array of X3DNode results array (using a properly typed node array or X3DPrototypeInstance array) from type MFNode */
  public void getValue (X3DNode[] result);

  /** Utility method to provide single value from MFNode array */
  public void get1Value (int index, X3DNode result);

  /** Provide array of X3DNode results array (using a properly typed node array or X3DPrototypeInstance array) from type MFNode */
  public void setValue (int size, X3DNode[] nodes);

  /** Utility method to set a single value in MFNode array */
  public void set1Value (int index, X3DNode node);

  /** Utility method to append a single value to MFNode array */
  public void append (X3DNode node);

  /** Utility method to insert a single value in MFNode array */
  public void insertValue (int index, X3DNode node) ;
}
public class BrowserEvent : EventObject
{
    public static int INITIALIZED = 0;
    public static int SHUTDOWN = 1;
    public static int URL_ERROR = 2;
    public static int CONNECTION_ERROR = 10;
    public static int LAST_IDENTIFIER = 100;

    public BrowserEvent(Object browser, int action);
    public int getID();
}
public class BrowserFactory
{
    private BrowserFactory();

    public static void setBrowserFactoryImpl(
        BrowserFactoryImpl fac)
        throws IllegalArgumentException,
               X3DException,
               SecurityException;

    public static X3DComponent createX3DComponent(Map params)
        throws NotSupportedException;

    public static ExternalBrowser getBrowser(Applet applet)
        throws NotSupportedException,
               NoSuchBrowserException,
               ConnectionException;

    public static ExternalBrowser getBrowser(Applet applet,
                                             String frameName,
                                             int index)
        throws NotSupportedException,
               NoSuchBrowserException,
               ConnectionException;

    public static ExternalBrowser getBrowser(InetAddress address, int port)
        throws NotSupportedException,
               NoSuchBrowserException,
               UnknownHostException,
               ConnectionException;
}
public class X3DFieldEvent : EventObject
{
    public X3DFieldEvent(Object src, double ts, Object data);
    public double getTime();
    public Object getData();
}
public class Matrix3
{
	public Matrix3();
	public void setIdentity();
    public void set(int row, int column)
    public float get(int row, int column)
    public void setTransform(SFVec2f translation,
                             SFVec3f rotation,
                             SFVec2f scale,
                             SFVec3f scaleOrientation,
                             SFVec2f center)
    public void getTransform(SFVec2f translation,
                             SFVec3f rotation,
                             SFVec2f scale)
    public Matrix3 inverse()
    public Matrix3 transpose()
    public Matrix3 multiplyLeft(Matrix3 mat)
    public Matrix3 multiplyRight(Matrix3 mat)
    public Matrix3 multiplyRowVector(SFVec3f vec)
    public Matrix3 multiplyColVector(SFVec3f vec)
}
public class Matrix4
{
	public Matrix4();
	public void setIdentity();
    public void set(int row, int column)
    public float get(int row, int column)
    public void setTransform(SFVec3f translation,
                             SFRotation rotation,
                             SFVec3f scale,
                             SFRotation scaleOrientation,
                             SFVec3f center)
    public void getTransform(SFVec3f translation,
                             SFRotation rotation,
                             SFVec3f scale)
    public Matrix3 inverse()
    public Matrix3 transpose()
    public Matrix3 multiplyLeft(Matrix4 mat)
    public Matrix3 multiplyRight(Matrix4 mat)
    public Matrix3 multiplyRowVector(SFVec3f vec)
    public Matrix3 multiplyColVector(SFVec3f vec)
}
public interface ComponentInfo
{
    public String getName();
    public int getLevel();
    public String getTitle();
    public String getProviderURL();
    public String toX3DString();
}public interface ProfileInfo
{
    public String getName();
    public String getTitle();
    public ComponentInfo[] getComponents();
    public String toX3DString();
}public class X3DException : RuntimeException
{
	public X3DException();
	public X3DException(String);
}
public class BrowserNotSharedException : X3DException
{
	public BrowserNotSharedException();
	public BrowserNotSharedException(String);
}
public class ConnectionException : X3DException
{
	public ConnectionException();
	public ConnectionException(String);
}
public class ImportedNodeException : X3DException
{
	public ImportedNodeException();
	public ImportedNodeException(String);
}
public class InsufficientCapabilitiesException : X3DException
{
	public InsufficientCapabilitiesException();
	public InsufficientCapabilitiesException(String);
}
public class InvalidBrowserException : X3DException
{
	public InvalidBrowserException();
	public InvalidBrowserException(String);
}
public class InvalidDocumentException : X3DException
{
	public InvalidDocumentException();
	public InvalidDocumentException(String);
}
public class InvalidExecutionContextException : X3DException
{
	public InvalidExecutionContextException();
	public InvalidExecutionContextException(String);
}
public class InvalidFieldException : X3DException
{
	public InvalidFieldException();
	public InvalidFieldException(String);
}
public class InvalidFieldValueException : X3DException
{
	public InvalidFieldValueException();
	public InvalidFieldValueException(String);
}
public class InvalidNodeException : X3DException
{
	public InvalidNodeException();
	public InvalidNodeException(String);
}
public class InvalidOperationTimingException : X3DException
{
	public InvalidOperationTimingException();
	public InvalidOperationTimingException(String);
}
public class InvalidProtoException : X3DException
{
	public InvalidProtoException();
	public InvalidProtoException(String);
}
public class InvalidRouteException : X3DException
{
	public InvalidRouteException();
	public InvalidRouteException(String);
}
public class InvalidURLException : X3DException
{
	public InvalidURLException();
	public InvalidURLException(String);
}
public class InvalidX3DException : X3DException
{
	public InvalidX3DException();
	public InvalidX3DException(String);
}
public class NodeInUseException : X3DException
{
	public NodeInUseException();
	public NodeInUseException(String);
}
public class NodeUnavailableException : X3DException
{
	public NodeUnavailableException();
	public NodeUnavailableException(String);
}
public class NoSuchBrowserException : X3DException
{
	public NoSuchBrowserException();
	public NoSuchBrowserException(String);
}
public class NotSupportedException : X3DException
{
	public NotSupportedException();
	public NotSupportedException(String);
}
public class URLUnavailableException : X3DException
{
	public URLUnavailableException();
	public URLUnavailableException(String);
}
