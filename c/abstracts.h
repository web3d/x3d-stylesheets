/** X3DAppearanceChildNode defines an abstract node structure that extends structure X3DNode.
  * Nodes of this type can be used as child nodes for Appearance. */

struct X3DAppearanceChildNode
{
  struct X3DNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DAppearanceNode defines an abstract node structure that extends structure X3DNode.
  * Base type for all Appearance nodes. */

struct X3DAppearanceNode
{
  struct X3DNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DBackgroundNode defines an abstract node structure that extends structures X3DBindableNode, X3DChildNode, and X3DNode.
  * Abstract type from which all backgrounds inherit, also defining a background binding stack. */

struct X3DBackgroundNode
{
  struct X3DBindableNode*  extNode;

  /** Provide float* value in radians (-∞,∞) from inputOutput MFFloat field named "groundAngle". */
  float* (*getGroundAngle) (void* this);

  /** Provide number of primitive values in "groundAngle" array */
  int (*getNumGroundAngle) (void* this);

  /** Assign float* value in radians (-∞,∞) to inputOutput MFFloat field named "groundAngle". */
  void (*setGroundAngle) (void* this, float* angles);

  /** Assign single float* value in radians (-∞,∞) as the MFFloat array for inputOutput field named "groundAngle" */
  void (*setGroundAngle2) (void* this, float* angle);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput MFColor field named "groundColor". */
  void (*getGroundColor) (void* this, float* result);

  /** Provide number of 3-tuple primitive values in "groundColor" array */
  int (*getNumGroundColor) (void* this);

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput MFColor field named "groundColor". */
  void (*setGroundColor) (void* this, float* colors)

  /** Provide float* value in radians (-∞,∞) from inputOutput MFFloat field named "skyAngle". */
  float* (*getSkyAngle) (void* this);

  /** Provide number of primitive values in "skyAngle" array */
  int (*getNumSkyAngle) (void* this);

  /** Assign float* value in radians (-∞,∞) to inputOutput MFFloat field named "skyAngle". */
  void (*setSkyAngle) (void* this, float* angles);

  /** Assign single float* value in radians (-∞,∞) as the MFFloat array for inputOutput field named "skyAngle" */
  void (*setSkyAngle2) (void* this, float* angle);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput MFColor field named "skyColor". */
  void (*getSkyColor) (void* this, float* result);

  /** Provide number of 3-tuple primitive values in "skyColor" array */
  int (*getNumSkyColor) (void* this);

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput MFColor field named "skyColor". */
  void (*setSkyColor) (void* this, float* colors)

  /** Provide float value from inputOutput SFFloat field named "transparency". */
  float (*getTransparency) (void* this);

  /** Assign float value to inputOutput SFFloat field named "transparency". */
  void (*setTransparency) (void* this, float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Assign SFBool value to inputOnly SFBool field named "set_bind". */
  void (*setBind) (void* this, SFBool value);

  /** Provide double value in seconds from outputOnly SFTime field named "bindTime". */
  double (*getBindTime) (void* this);

  /** Provide SFBool value from outputOnly SFBool field named "isBound". */
  SFBool (*getIsBound) (void* this);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DBindableNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Bindable nodes implement the binding stack, so that only one of each node type is active at a given time. */

struct X3DBindableNode
{
  struct X3DChildNode*  extNode;

  /** Assign SFBool value to inputOnly SFBool field named "set_bind". */
  void (*setBind) (void* this, SFBool value);

  /** Provide double value in seconds from outputOnly SFTime field named "bindTime". */
  double (*getBindTime) (void* this);

  /** Provide SFBool value from outputOnly SFBool field named "isBound". */
  SFBool (*getIsBound) (void* this);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DChaserNode defines an abstract node structure that extends structures X3DFollowerNode, X3DChildNode, and X3DNode.
  * The X3DChaserNode abstract node type calculates the output on value_changed as a finite impulse response (FIR) based on the events received on set_destination field. */

struct X3DChaserNode
{
  struct X3DFollowerNode*  extNode;

  /** Provide double value in seconds [0,∞) from initializeOnly SFTime field named "duration". */
  double (*getDuration) (void* this);

  /** Assign double value in seconds [0,∞) to initializeOnly SFTime field named "duration". */
  void (*setDuration) (void* this, double timestamp)

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DChildNode defines an abstract node structure that extends structure X3DNode.
  * A node that implements X3DChildNode is one of the legal children for a X3DGroupingNode parent. */

struct X3DChildNode
{
  struct X3DNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DColorNode defines an abstract node structure that extends structures X3DGeometricPropertyNode and X3DNode.
  * Base type for color specifications in X3D. */

struct X3DColorNode
{
  struct X3DGeometricPropertyNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DComposableVolumeRenderStyleNode defines an abstract node structure that extends structures X3DVolumeRenderStyleNode and X3DNode.
  * The X3DComposableVolumeRenderStyleNode abstract node type is the base type for all node types that allow rendering styles to be sequentially composed together to form a single renderable output. */

struct X3DComposableVolumeRenderStyleNode
{
  struct X3DVolumeRenderStyleNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DComposedGeometryNode defines an abstract node structure that extends structures X3DGeometryNode and X3DNode.
  * Composed geometry nodes produce renderable geometry, can contain Color Coordinate Normal TextureCoordinate, and are contained by a Shape node. */

struct X3DComposedGeometryNode
{
  struct X3DGeometryNode*  extNode;

  /** Provide SFBool value from initializeOnly SFBool field named "ccw". */
  SFBool (*getCcw) (void* this);

  /** Assign SFBool value to initializeOnly SFBool field named "ccw". */
  void (*setCcw) (void* this, SFBool value);

  /** Provide SFBool value from initializeOnly SFBool field named "colorPerVertex". */
  SFBool (*getColorPerVertex) (void* this);

  /** Assign SFBool value to initializeOnly SFBool field named "colorPerVertex". */
  void (*setColorPerVertex) (void* this, SFBool color);

  /** Provide SFBool value from initializeOnly SFBool field named "normalPerVertex". */
  SFBool (*getNormalPerVertex) (void* this);

  /** Assign SFBool value to initializeOnly SFBool field named "normalPerVertex". */
  void (*setNormalPerVertex) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "solid". */
  SFBool (*getSolid) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "solid". */
  void (*setSolid) (void* this, SFBool value);

  /** Provide X3DVertexAttributeNode* value (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DVertexAttributeNode type field named "attrib". */
  void (*getAttrib) (void* this, struct X3DNode* result);

  /** Provide number of nodes in "attrib" array */
  int (*getNumAttrib) (void* this);

  /** Assign X3DVertexAttributeNode* value (using a properly typed node array) to inputOutput X3DVertexAttributeNode type field named "attrib". */
  void (*setAttrib) (void* this, X3DVertexAttributeNode* nodes);

  /** Assign single X3DVertexAttributeNode* value (using a properly typed node) as the MFNode array for inputOutput field named "attrib" */
  void (*setAttrib2) (void* this, X3DVertexAttributeNode* node);

  /** Assign X3DVertexAttributeNode* value (using a properly typed protoInstance array) to inputOutput X3DVertexAttributeNode type field named "attrib". */
  void (*setAttrib3) (void* this, struct X3DPrototypeInstance node);

  /** Assign X3DVertexAttributeNode* value (using a properly typed node array) to inputOutput X3DVertexAttributeNode type field named "attrib". */
  void (*setAttrib4) (void* this, struct X3DNode* nodes);

  /** Provide X3DColorNode value (using a properly typed node or X3DPrototypeInstance) using RGB values [0..1] from inputOutput X3DColorNode type field named "color". */
  void (*getColor) (void* this, struct X3DNode result);

  /** Assign X3DColorNode value (using a properly typed node) using RGB values [0..1] to inputOutput X3DColorNode type field named "color". */
  void (*setColor) (void* this, X3DColorNode color)

  /** Assign X3DColorNode value (using a properly typed protoInstance) */
  void (*setColor2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DCoordinateNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DCoordinateNode type field named "coord". */
  void (*getCoord) (void* this, struct X3DNode result);

  /** Assign X3DCoordinateNode value (using a properly typed node) to inputOutput X3DCoordinateNode type field named "coord". */
  void (*setCoord) (void* this, X3DCoordinateNode node);

  /** Assign X3DCoordinateNode value (using a properly typed protoInstance) */
  void (*setCoord2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide FogCoordinate value (using a properly typed node or X3DPrototypeInstance) from inputOutput FogCoordinate type field named "fogCoord". */
  void (*getFogCoord) (void* this, struct X3DNode result);

  /** Assign FogCoordinate value (using a properly typed node) to inputOutput FogCoordinate type field named "fogCoord". */
  void (*setFogCoord) (void* this, FogCoordinate node);

  /** Assign FogCoordinate value (using a properly typed protoInstance) */
  void (*setFogCoord2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DNormalNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DNormalNode type field named "normal". */
  void (*getNormal) (void* this, struct X3DNode result);

  /** Assign X3DNormalNode value (using a properly typed node) to inputOutput X3DNormalNode type field named "normal". */
  void (*setNormal) (void* this, X3DNormalNode node);

  /** Assign X3DNormalNode value (using a properly typed protoInstance) */
  void (*setNormal2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DSingleTextureCoordinateNode|MultiTextureCoordinate value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DSingleTextureCoordinateNode|MultiTextureCoordinate type field named "texCoord". */
  void (*getTexCoord) (void* this, struct X3DNode result);

  /** Assign X3DSingleTextureCoordinateNode|MultiTextureCoordinate value (using a properly typed node) to inputOutput X3DSingleTextureCoordinateNode|MultiTextureCoordinate type field named "texCoord". */
  void (*setTexCoord) (void* this, struct X3DNode node);

  /** Assign X3DSingleTextureCoordinateNode|MultiTextureCoordinate value (using a properly typed protoInstance) */
  void (*setTexCoord2) (void* this, struct X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DCoordinateNode defines an abstract node structure that extends structures X3DGeometricPropertyNode and X3DNode.
  * Base type for all coordinate node types in X3D. */

struct X3DCoordinateNode
{
  struct X3DGeometricPropertyNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DDamperNode defines an abstract node structure that extends structures X3DFollowerNode, X3DChildNode, and X3DNode.
  * The X3DDamperNode abstract node type creates an IIR response that approaches the destination value according to the shape of the e-function only asymptotically but very quickly. */

struct X3DDamperNode
{
  struct X3DFollowerNode*  extNode;

  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "tau". */
  double (*getTau) (void* this);

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "tau". */
  void (*setTau) (void* this, double timestamp)

  /** Provide float value from inputOutput SFFloat field named "tolerance". */
  float (*getTolerance) (void* this);

  /** Assign float value to inputOutput SFFloat field named "tolerance". */
  void (*setTolerance) (void* this, float value);

  /** Provide int value [0,5) from initializeOnly SFInt32 field named "order". */
  int (*getOrder) (void* this);

  /** Assign int value [0,5) to initializeOnly SFInt32 field named "order". */
  void (*setOrder) (void* this, int value)

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DDragSensorNode defines an abstract node structure that extends structures X3DPointingDeviceSensorNode, X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all drag-style pointing device sensors. */

struct X3DDragSensorNode
{
  struct X3DPointingDeviceSensorNode*  extNode;

  /** Provide 3-tuple float* value from outputOnly SFVec3f field named "trackPoint_changed". */
  void (*getTrackPoint) (void* this, float* result);

  /** Provide SFBool value from inputOutput SFBool field named "autoOffset". */
  SFBool (*getAutoOffset) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "autoOffset". */
  void (*setAutoOffset) (void* this, SFBool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide SFBool value from outputOnly SFBool field named "isOver". */
  SFBool (*getIsOver) (void* this);

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DEnvironmentalSensorNode defines an abstract node structure that extends structures X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for the environmental sensor nodes ProximitySensor, TransformSensor and VisibilitySensor. */

struct X3DEnvironmentalSensorNode
{
  struct X3DSensorNode*  extNode;

  /** Provide 3-tuple float* value (-∞,∞) from initializeOnly SFVec3f field named "size". */
  void (*getSize) (void* this, float* result);

  /** Assign 3-tuple float* value (-∞,∞) to initializeOnly SFVec3f field named "size". */
  void (*setSize) (void* this, float* value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DEnvironmentTextureNode defines an abstract node structure that extends structures X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all nodes that specify cubic environment map sources for texture images. */

struct X3DEnvironmentTextureNode
{
  struct X3DTextureNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DFollowerNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * X3DFollowerNode is the abstract base class for all nodes in the Followers component. */

struct X3DFollowerNode
{
  struct X3DChildNode*  extNode;

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DFontStyleNode defines an abstract node structure.
  * Base type for all font style nodes. */

struct X3DFontStyleNode
{
  /** Provide xs:NMTOKENS value from inputOutput xs:NMTOKENS type field named "class". */
  xs:NMTOKENS (*getClass) (void* this);

  /** Assign xs:NMTOKENS value to inputOutput xs:NMTOKENS type field named "class". */
  void (*setClass) (void* this, xs:NMTOKENS value);

  /** Provide string value from inputOutput SFString field named "id". */
  string (*getId) (void* this);

  /** Assign string value to inputOutput SFString field named "id". */
  void (*setId) (void* this, string value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DGeometricPropertyNode defines an abstract node structure that extends structure X3DNode.
  * Base type for all geometric property node types. */

struct X3DGeometricPropertyNode
{
  struct X3DNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DGeometryNode defines an abstract node structure that extends structure X3DNode.
  * Geometry nodes produce renderable geometry and are contained by a Shape node. */

struct X3DGeometryNode
{
  struct X3DNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DGroupingNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Grouping nodes can contain other nodes as children, thus making up the backbone of a scene graph. */

struct X3DGroupingNode
{
  struct X3DChildNode*  extNode;
  struct X3DBoundedObject*  extNode1;

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  void (*getBboxCenter) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void (*setBboxCenter) (void* this, float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  void (*getBboxSize) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void (*setBboxSize) (void* this, float* value);

  /** Provide SFBool value from inputOutput SFBool field named "bboxDisplay". */
  SFBool (*getBboxDisplay) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "bboxDisplay". */
  void (*setBboxDisplay) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "visible". */
  SFBool (*getVisible) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "visible". */
  void (*setVisible) (void* this, SFBool value);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren (void* this, X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node) as the MFNode array for inputOnly field named "addChildren" */
  void addChildren2 (void* this, X3DChildNode* node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren3 (void* this, struct X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren4 (void* this, struct X3DNode* nodes);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren (void* this, X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node) as the MFNode array for inputOnly field named "removeChildren" */
  void removeChildren2 (void* this, X3DChildNode* node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren3 (void* this, struct X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren4 (void* this, struct X3DNode* nodes);

  /** Provide X3DChildNode* value (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DChildNode type field named "children". */
  void (*getChildren) (void* this, struct X3DNode* result);

  /** Provide number of nodes in "children" array */
  int (*getNumChildren) (void* this);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  void (*setChildren) (void* this, X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node) as the MFNode array for inputOutput field named "children" */
  void (*setChildren2) (void* this, X3DChildNode* node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOutput X3DChildNode type field named "children". */
  void (*setChildren3) (void* this, struct X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  void (*setChildren4) (void* this, struct X3DNode* nodes);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DInfoNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Base type for all nodes that contain only information without visual semantics. */

struct X3DInfoNode
{
  struct X3DChildNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DInterpolatorNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Interpolator nodes are designed for linear keyframed animation. Interpolators are driven by an input key ranging [0..1] and produce corresponding piecewise-linear output functions. */

struct X3DInterpolatorNode
{
  struct X3DChildNode*  extNode;

  /** Assign float value to inputOnly SFFloat field named "set_fraction". */
  void (*setFraction) (void* this, float value);

  /** Provide float* value from inputOutput MFFloat field named "key". */
  float* (*getKey) (void* this);

  /** Provide number of primitive values in "key" array */
  int (*getNumKey) (void* this);

  /** Assign float* value to inputOutput MFFloat field named "key". */
  void (*setKey) (void* this, float* values);

  /** Assign single float* value as the MFFloat array for inputOutput field named "key" */
  void (*setKey2) (void* this, float* value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DKeyDeviceSensorNode defines an abstract node structure that extends structures X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all sensor node types that operate using key devices. */

struct X3DKeyDeviceSensorNode
{
  struct X3DSensorNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DLayerNode defines an abstract node structure that extends structure X3DNode.
  * The X3DLayerNode abstract node type is the base node type for layer nodes. */

struct X3DLayerNode
{
  struct X3DNode*  extNode;
  struct X3DPickableObject*  extNode1;

  /** Provide string* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  string* (*getObjectType) (void* this);

  /** Provide number of primitive values in "objectType" array */
  int (*getNumObjectType) (void* this);

  /** Assign string* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void (*setObjectType) (void* this, string* values)

  /** Provide string* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  string* (*getObjectType) (void* this);

  /** Provide number of primitive values in "objectType" array */
  int (*getNumObjectType) (void* this);

  /** Assign string* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void (*setObjectType) (void* this, string* values);

  /** Assign single string* value ["ALL","NONE","TERRAIN",...] as the MFString array for inputOutput field named "objectType" */
  void (*setObjectType2) (void* this, string* value);

  /** Provide SFBool value from inputOutput SFBool field named "pickable". */
  SFBool (*getPickable) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "pickable". */
  void (*setPickable) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "visible". */
  SFBool (*getVisible) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "visible". */
  void (*setVisible) (void* this, SFBool value);

  /** Provide X3DViewportNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DViewportNode type field named "viewport". */
  void (*getViewport) (void* this, struct X3DNode result);

  /** Assign X3DViewportNode value (using a properly typed node) to inputOutput X3DViewportNode type field named "viewport". */
  void (*setViewport) (void* this, X3DViewportNode node);

  /** Assign X3DViewportNode value (using a properly typed protoInstance) */
  void (*setViewport2) (void* this, struct X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DLayoutNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * X3DLayoutNode is the base node type for layout nodes. */

struct X3DLayoutNode
{
  struct X3DChildNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DLightNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Light nodes provide illumination for rendering geometry in the scene. Implementing nodes must include a global field with type SFBool and accessType inputOutput. */

struct X3DLightNode
{
  struct X3DChildNode*  extNode;

  /** Provide float value from inputOutput SFFloat field named "ambientIntensity". */
  float (*getAmbientIntensity) (void* this);

  /** Assign float value to inputOutput SFFloat field named "ambientIntensity". */
  void (*setAmbientIntensity) (void* this, float value);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "color". */
  void (*getColor) (void* this, float* result);

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "color". */
  void (*setColor) (void* this, float* color)

  /** Provide float value [0,∞) from inputOutput SFFloat field named "intensity". */
  float (*getIntensity) (void* this);

  /** Assign float value [0,∞) to inputOutput SFFloat field named "intensity". */
  void (*setIntensity) (void* this, float value)

  /** Provide SFBool value from inputOutput SFBool field named "on". */
  SFBool (*getOn) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "on". */
  void (*setOn) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "shadows". */
  SFBool (*getShadows) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "shadows". */
  void (*setShadows) (void* this, SFBool value);

  /** Provide float value from inputOutput SFFloat field named "shadowIntensity". */
  float (*getShadowIntensity) (void* this);

  /** Assign float value to inputOutput SFFloat field named "shadowIntensity". */
  void (*setShadowIntensity) (void* this, float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DMaterialNode defines an abstract node structure that extends structures X3DAppearanceChildNode and X3DNode.
  * Base type for all Material nodes. */

struct X3DMaterialNode
{
  struct X3DAppearanceChildNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DNBodyCollidableNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * The X3DNBodyCollidableNode abstract node type represents objects that act as the interface between the rigid body physics, collision geometry proxy, and renderable objects in the scene graph hierarchy. */

struct X3DNBodyCollidableNode
{
  struct X3DChildNode*  extNode;
  struct X3DBoundedObject*  extNode1;

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  void (*getBboxCenter) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void (*setBboxCenter) (void* this, float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  void (*getBboxSize) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void (*setBboxSize) (void* this, float* value);

  /** Provide SFBool value from inputOutput SFBool field named "bboxDisplay". */
  SFBool (*getBboxDisplay) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "bboxDisplay". */
  void (*setBboxDisplay) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "visible". */
  SFBool (*getVisible) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "visible". */
  void (*setVisible) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide 4-tuple float* value in radians from inputOutput SFRotation field named "rotation". */
  float* (*getRotation) (void* this);

  /** Assign 4-tuple float* value in radians to inputOutput SFRotation field named "rotation". */
  void (*setRotation) (void* this, float* value);

  /** Provide 3-tuple float* value from inputOutput SFVec3f field named "translation". */
  void (*getTranslation) (void* this, float* result);

  /** Assign 3-tuple float* value to inputOutput SFVec3f field named "translation". */
  void (*setTranslation) (void* this, float* value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DNBodyCollisionSpaceNode defines an abstract node structure that extends structure X3DNode.
  * The X3DNBodyCollisionSpaceNode abstract node type represents objects that act as a self-contained spatial collection of objects that can interact through collision detection routines. */

struct X3DNBodyCollisionSpaceNode
{
  struct X3DNode*  extNode;
  struct X3DBoundedObject*  extNode1;

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  void (*getBboxCenter) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void (*setBboxCenter) (void* this, float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  void (*getBboxSize) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void (*setBboxSize) (void* this, float* value);

  /** Provide SFBool value from inputOutput SFBool field named "bboxDisplay". */
  SFBool (*getBboxDisplay) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "bboxDisplay". */
  void (*setBboxDisplay) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "visible". */
  SFBool (*getVisible) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "visible". */
  void (*setVisible) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DNetworkSensorNode defines an abstract node structure that extends structures X3DSensorNode, X3DChildNode, and X3DNode.
  * Base typefor all sensors that generate events based on network activity. */

struct X3DNetworkSensorNode
{
  struct X3DSensorNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DNode defines an abstract node structure.
  * All instantiable nodes implement X3DNode, which corresponds to SFNode type in the X3D specification. */

struct X3DNode
{
  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Dispose of this node's resources. */
  void (*dispose) (void* this);

  /** Get a field for this node by name. */
  struct X3DField (*getField) (void* this, string name);

  /** Get list of available fields in this node. */
  struct X3DFieldDefinition* (*getFieldDefinitions) (void* this);

  /** Get the name of this node. */
  string (*getNodeName) (void* this);

  /** Determine if node setup is completed. */
  SFBool (*isRealized) (void* this);

  /** Notify node that setup stage is complete. */
  void (*realize) (void* this);
}
;/** X3DNormalNode defines an abstract node structure that extends structures X3DGeometricPropertyNode and X3DNode.
  * Base type for all normal node types in X3D. */

struct X3DNormalNode
{
  struct X3DGeometricPropertyNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DNurbsControlCurveNode defines an abstract node structure that extends structure X3DNode.
  * Base type for all nodes that provide control curve information in 2D space. */

struct X3DNurbsControlCurveNode
{
  struct X3DNode*  extNode;

  /** Provide 2-tuple double* value from inputOutput MFVec2d field named "controlPoint". */
  void (*getControlPoint) (void* this, double* result);

  /** Provide number of 2-tuple primitive values in "controlPoint" array */
  int (*getNumControlPoint) (void* this);

  /** Assign 2-tuple double* value to inputOutput MFVec2d field named "controlPoint". */
  void (*setControlPoint) (void* this, double* values);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DNurbsSurfaceGeometryNode defines an abstract node structure that extends structures X3DParametricGeometryNode, X3DGeometryNode, and X3DNode.
  * Abstract geometry type for all types of NURBS surfaces. */

struct X3DNurbsSurfaceGeometryNode
{
  struct X3DParametricGeometryNode*  extNode;

  /** Provide SFBool value from initializeOnly SFBool field named "uClosed". */
  SFBool (*getUClosed) (void* this);

  /** Assign SFBool value to initializeOnly SFBool field named "uClosed". */
  void (*setUClosed) (void* this, SFBool value);

  /** Provide SFBool value from initializeOnly SFBool field named "vClosed". */
  SFBool (*getVClosed) (void* this);

  /** Assign SFBool value to initializeOnly SFBool field named "vClosed". */
  void (*setVClosed) (void* this, SFBool value);

  /** Provide int value [0,∞) from initializeOnly SFInt32 field named "uDimension". */
  int (*getUDimension) (void* this);

  /** Assign int value [0,∞) to initializeOnly SFInt32 field named "uDimension". */
  void (*setUDimension) (void* this, int value)

  /** Provide int value [0,∞) from initializeOnly SFInt32 field named "vDimension". */
  int (*getVDimension) (void* this);

  /** Assign int value [0,∞) to initializeOnly SFInt32 field named "vDimension". */
  void (*setVDimension) (void* this, int value)

  /** Provide double* value from initializeOnly MFDouble field named "uKnot". */
  double* (*getUKnot) (void* this);

  /** Provide number of primitive values in "uKnot" array */
  int (*getNumUKnot) (void* this);

  /** Assign double* value to initializeOnly MFDouble field named "uKnot". */
  void (*setUKnot) (void* this, double* values);

  /** Assign single double* value as the MFDouble array for initializeOnly field named "uKnot" */
  void (*setUKnot2) (void* this, double* value);

  /** Provide double* value from initializeOnly MFDouble field named "vKnot". */
  double* (*getVKnot) (void* this);

  /** Provide number of primitive values in "vKnot" array */
  int (*getNumVKnot) (void* this);

  /** Assign double* value to initializeOnly MFDouble field named "vKnot". */
  void (*setVKnot) (void* this, double* values);

  /** Assign single double* value as the MFDouble array for initializeOnly field named "vKnot" */
  void (*setVKnot2) (void* this, double* value);

  /** Provide int value [2,∞) from initializeOnly SFInt32 field named "uOrder". */
  int (*getUOrder) (void* this);

  /** Assign int value [2,∞) to initializeOnly SFInt32 field named "uOrder". */
  void (*setUOrder) (void* this, int value)

  /** Provide int value [2,∞) from initializeOnly SFInt32 field named "vOrder". */
  int (*getVOrder) (void* this);

  /** Assign int value [2,∞) to initializeOnly SFInt32 field named "vOrder". */
  void (*setVOrder) (void* this, int value)

  /** Provide int value from inputOutput SFInt32 field named "uTessellation". */
  int (*getUTessellation) (void* this);

  /** Assign int value to inputOutput SFInt32 field named "uTessellation". */
  void (*setUTessellation) (void* this, int value);

  /** Provide int value from inputOutput SFInt32 field named "vTessellation". */
  int (*getVTessellation) (void* this);

  /** Assign int value to inputOutput SFInt32 field named "vTessellation". */
  void (*setVTessellation) (void* this, int value);

  /** Provide double* value (-∞,∞) from inputOutput MFDouble field named "weight". */
  double* (*getWeight) (void* this);

  /** Provide number of primitive values in "weight" array */
  int (*getNumWeight) (void* this);

  /** Assign double* value (-∞,∞) to inputOutput MFDouble field named "weight". */
  void (*setWeight) (void* this, double* values);

  /** Assign single double* value (-∞,∞) as the MFDouble array for inputOutput field named "weight" */
  void (*setWeight2) (void* this, double* value);

  /** Provide SFBool value from inputOutput SFBool field named "solid". */
  SFBool (*getSolid) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "solid". */
  void (*setSolid) (void* this, SFBool value);

  /** Provide X3DCoordinateNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DCoordinateNode type field named "controlPoint". */
  void (*getControlPoint) (void* this, struct X3DNode result);

  /** Assign X3DCoordinateNode value (using a properly typed node) to inputOutput X3DCoordinateNode type field named "controlPoint". */
  void (*setControlPoint) (void* this, X3DCoordinateNode node);

  /** Assign X3DCoordinateNode value (using a properly typed protoInstance) */
  void (*setControlPoint2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DSingleTextureCoordinateNode|NurbsTextureCoordinate value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DSingleTextureCoordinateNode|NurbsTextureCoordinate type field named "texCoord". */
  void (*getTexCoord) (void* this, struct X3DNode result);

  /** Assign X3DSingleTextureCoordinateNode|NurbsTextureCoordinate value (using a properly typed node) to inputOutput X3DSingleTextureCoordinateNode|NurbsTextureCoordinate type field named "texCoord". */
  void (*setTexCoord) (void* this, struct X3DNode node);

  /** Assign X3DSingleTextureCoordinateNode|NurbsTextureCoordinate value (using a properly typed protoInstance) */
  void (*setTexCoord2) (void* this, struct X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DOneSidedMaterialNode defines an abstract node structure that extends structures X3DMaterialNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for material nodes that describe how the shape looks like from one side. A different number of contanied texture nodes are allowed by each of the implementing nodes. */

struct X3DOneSidedMaterialNode
{
  struct X3DMaterialNode*  extNode;

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "emissiveColor". */
  void (*getEmissiveColor) (void* this, float* result);

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "emissiveColor". */
  void (*setEmissiveColor) (void* this, float* color)

  /** Provide string value from inputOutput SFString field named "emissiveTextureMapping". */
  string (*getEmissiveTextureMapping) (void* this);

  /** Assign string value to inputOutput SFString field named "emissiveTextureMapping". */
  void (*setEmissiveTextureMapping) (void* this, string value);

  /** Provide float value [0,∞) from inputOutput SFFloat field named "normalScale". */
  float (*getNormalScale) (void* this);

  /** Assign float value [0,∞) to inputOutput SFFloat field named "normalScale". */
  void (*setNormalScale) (void* this, float value)

  /** Provide string value from inputOutput SFString field named "normalTextureMapping". */
  string (*getNormalTextureMapping) (void* this);

  /** Assign string value to inputOutput SFString field named "normalTextureMapping". */
  void (*setNormalTextureMapping) (void* this, string value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DParametricGeometryNode defines an abstract node structure that extends structures X3DGeometryNode and X3DNode.
  * Base type for all geometry node types that are created parametrically and use control points to describe the final shape of the surface. */

struct X3DParametricGeometryNode
{
  struct X3DGeometryNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DParticleEmitterNode defines an abstract node structure that extends structure X3DNode.
  * The X3DParticleEmitterNode abstract type represents any node that is an emitter of particles. */

struct X3DParticleEmitterNode
{
  struct X3DNode*  extNode;

  /** Provide SFBool value from inputOutput SFBool field named "on". */
  SFBool (*getOn) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "on". */
  void (*setOn) (void* this, SFBool value);

  /** Provide float value [0,∞) from inputOutput SFFloat field named "speed". */
  float (*getSpeed) (void* this);

  /** Assign float value [0,∞) to inputOutput SFFloat field named "speed". */
  void (*setSpeed) (void* this, float value)

  /** Provide float value [0,∞) from inputOutput SFFloat field named "variation". */
  float (*getVariation) (void* this);

  /** Assign float value [0,∞) to inputOutput SFFloat field named "variation". */
  void (*setVariation) (void* this, float value)

  /** Provide float value [0,∞) from inputOutput SFFloat field named "mass". */
  float (*getMass) (void* this);

  /** Assign float value [0,∞) to inputOutput SFFloat field named "mass". */
  void (*setMass) (void* this, float value)

  /** Provide float value [0,∞) from inputOutput SFFloat field named "surfaceArea". */
  float (*getSurfaceArea) (void* this);

  /** Assign float value [0,∞) to inputOutput SFFloat field named "surfaceArea". */
  void (*setSurfaceArea) (void* this, float value)

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DParticlePhysicsModelNode defines an abstract node structure that extends structure X3DNode.
  * The X3DParticlePhysicsModelNode abstract type represents any node that applies a form of constraints on the particles after they have been generated. */

struct X3DParticlePhysicsModelNode
{
  struct X3DNode*  extNode;

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DPickSensorNode defines an abstract node structure that extends structures X3DSensorNode, X3DChildNode, and X3DNode.
  * The X3DPickSensorNode abstract node type is the base node type that represents the lowest common denominator of picking capabilities. */

struct X3DPickSensorNode
{
  struct X3DSensorNode*  extNode;

  /** Provide string value from inputOutput SFString field named "matchCriterion". */
  string (*getMatchCriterion) (void* this);

  /** Assign string value to inputOutput SFString field named "matchCriterion". */
  void (*setMatchCriterion) (void* this, string value);

  /** Provide string* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  string* (*getObjectType) (void* this);

  /** Provide number of primitive values in "objectType" array */
  int (*getNumObjectType) (void* this);

  /** Assign string* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void (*setObjectType) (void* this, string* values)

  /** Provide string value from initializeOnly SFString field named "intersectionType". */
  string (*getIntersectionType) (void* this);

  /** Assign string value to initializeOnly SFString field named "intersectionType". */
  void (*setIntersectionType) (void* this, string value);

  /** Provide string value from initializeOnly SFString field named "sortOrder". */
  string (*getSortOrder) (void* this);

  /** Assign string value to initializeOnly SFString field named "sortOrder". */
  void (*setSortOrder) (void* this, string value);

  /** Provide string value from initializeOnly SFString field named "intersectionType". */
  string (*getIntersectionType) (void* this);

  /** Assign string value to initializeOnly SFString field named "intersectionType". */
  void (*setIntersectionType) (void* this, string value);

  /** Provide string value from inputOutput SFString field named "matchCriterion". */
  string (*getMatchCriterion) (void* this);

  /** Assign string value to inputOutput SFString field named "matchCriterion". */
  void (*setMatchCriterion) (void* this, string value);

  /** Provide string* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  string* (*getObjectType) (void* this);

  /** Provide number of primitive values in "objectType" array */
  int (*getNumObjectType) (void* this);

  /** Assign string* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void (*setObjectType) (void* this, string* values);

  /** Assign single string* value ["ALL","NONE","TERRAIN",...] as the MFString array for inputOutput field named "objectType" */
  void (*setObjectType2) (void* this, string* value);

  /** Provide string value from initializeOnly SFString field named "sortOrder". */
  string (*getSortOrder) (void* this);

  /** Assign string value to initializeOnly SFString field named "sortOrder". */
  void (*setSortOrder) (void* this, string value);

  /** Provide X3DGroupingNode|X3DShapeNode|Inline* value (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DGroupingNode|X3DShapeNode|Inline type field named "pickTarget". */
  void (*getPickTarget) (void* this, struct X3DNode* result);

  /** Provide number of nodes in "pickTarget" array */
  int (*getNumPickTarget) (void* this);

  /** Assign X3DGroupingNode|X3DShapeNode|Inline* value (using a properly typed node array) to inputOutput X3DGroupingNode|X3DShapeNode|Inline type field named "pickTarget". */
  void (*setPickTarget) (void* this, struct X3DNode* nodes);

  /** Assign single struct X3DNode* value (using a properly typed node) as the MFNode array for inputOutput field named "pickTarget" */
  void (*setPickTarget2) (void* this, struct X3DNode node);

  /** Assign X3DGroupingNode|X3DShapeNode|Inline* value (using a properly typed protoInstance array) to inputOutput X3DGroupingNode|X3DShapeNode|Inline type field named "pickTarget". */
  void (*setPickTarget3) (void* this, struct X3DPrototypeInstance node);

  /** Provide X3DChildNode* value (using a properly typed node array or X3DPrototypeInstance array) from outputOnly X3DChildNode type field named "pickedGeometry". */
  void (*getPickedGeometry) (void* this, struct X3DNode* result);

  /** Provide number of nodes in "pickedGeometry" array */
  int (*getNumPickedGeometry) (void* this);

  /** Provide X3DGeometryNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DGeometryNode type field named "pickingGeometry". */
  void (*getPickingGeometry) (void* this, struct X3DNode result);

  /** Assign X3DGeometryNode value (using a properly typed node) to inputOutput X3DGeometryNode type field named "pickingGeometry". */
  void (*setPickingGeometry) (void* this, X3DGeometryNode node);

  /** Assign X3DGeometryNode value (using a properly typed protoInstance) */
  void (*setPickingGeometry2) (void* this, struct X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DPointingDeviceSensorNode defines an abstract node structure that extends structures X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all pointing device sensors. */

struct X3DPointingDeviceSensorNode
{
  struct X3DSensorNode*  extNode;

  /** Provide SFBool value from outputOnly SFBool field named "isOver". */
  SFBool (*getIsOver) (void* this);

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DProductStructureChildNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Base type marking nodes that are valid product structure children for the CADGeometry component. */

struct X3DProductStructureChildNode
{
  struct X3DChildNode*  extNode;

  /** Provide string value from inputOutput SFString field named "name". */
  string (*getName) (void* this);

  /** Assign string value to inputOutput SFString field named "name". */
  void (*setName) (void* this, string value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DPrototypeInstance defines an abstract structure.
  * Base type for all prototype instances. Note that direct children nodes are disallowed, instead let fieldValue with type SFNode/MFNode contain them. Current practice is that, if desired, prototype authors must explicitly add the metadata SFNode field in the ProtoInterface. */

struct X3DPrototypeInstance
{
  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DRigidJointNode defines an abstract node structure that extends structure X3DNode.
  * The X3DRigidJointNode abstract node type is the base type for all joint types. */

struct X3DRigidJointNode
{
  struct X3DNode*  extNode;

  /** Provide string* value from inputOutput MFString field named "forceOutput". */
  string* (*getForceOutput) (void* this);

  /** Provide number of primitive values in "forceOutput" array */
  int (*getNumForceOutput) (void* this);

  /** Assign string* value to inputOutput MFString field named "forceOutput". */
  void (*setForceOutput) (void* this, string* values);

  /** Provide string* value from inputOutput MFString field named "forceOutput". */
  string* (*getForceOutput) (void* this);

  /** Provide number of primitive values in "forceOutput" array */
  int (*getNumForceOutput) (void* this);

  /** Assign string* value to inputOutput MFString field named "forceOutput". */
  void (*setForceOutput) (void* this, string* values);

  /** Assign single string* value as the MFString array for inputOutput field named "forceOutput" */
  void (*setForceOutput2) (void* this, string* value);

  /** Provide RigidBody value (using a properly typed node or X3DPrototypeInstance) from inputOutput RigidBody type field named "body1". */
  void (*getBody1) (void* this, struct X3DNode result);

  /** Assign RigidBody value (using a properly typed node) to inputOutput RigidBody type field named "body1". */
  void (*setBody1) (void* this, RigidBody node);

  /** Assign RigidBody value (using a properly typed protoInstance) */
  void (*setBody12) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide RigidBody value (using a properly typed node or X3DPrototypeInstance) from inputOutput RigidBody type field named "body2". */
  void (*getBody2) (void* this, struct X3DNode result);

  /** Assign RigidBody value (using a properly typed node) to inputOutput RigidBody type field named "body2". */
  void (*setBody2) (void* this, RigidBody node);

  /** Assign RigidBody value (using a properly typed protoInstance) */
  void (*setBody22) (void* this, struct X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DScriptNode defines an abstract node structure.
  * Base type for scripting nodes (but not shader nodes). */

struct X3DScriptNode
{
  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide SFBool value from inputOutput SFBool field named "load". */
  SFBool (*getLoad) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "load". */
  void (*setLoad) (void* this, SFBool value);

  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "autoRefresh". */
  double (*getAutoRefresh) (void* this);

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "autoRefresh". */
  void (*setAutoRefresh) (void* this, double timestamp)

  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "autoRefreshTimeLimit". */
  double (*getAutoRefreshTimeLimit) (void* this);

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "autoRefreshTimeLimit". */
  void (*setAutoRefreshTimeLimit) (void* this, double timestamp)

  /** Provide string* value from inputOutput MFString field named "url". */
  string* (*getUrl) (void* this);

  /** Provide number of primitive values in "url" array */
  int (*getNumUrl) (void* this);

  /** Assign string* value to inputOutput MFString field named "url". */
  void (*setUrl) (void* this, string* values);

  /** Assign single string* value as the MFString array for inputOutput field named "url" */
  void (*setUrl2) (void* this, string* value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DSensorNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Base type for all sensors. */

struct X3DSensorNode
{
  struct X3DChildNode*  extNode;

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DSequencerNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Base type from which all Sequencers are derived. */

struct X3DSequencerNode
{
  struct X3DChildNode*  extNode;

  /** Assign SFBool value to inputOnly SFBool field named "next". */
  void (*setNext) (void* this, SFBool value);

  /** Assign SFBool value to inputOnly SFBool field named "previous". */
  void (*setPrevious) (void* this, SFBool value);

  /** Assign float value to inputOnly SFFloat field named "set_fraction". */
  void (*setFraction) (void* this, float value);

  /** Provide float* value from inputOutput MFFloat field named "key". */
  float* (*getKey) (void* this);

  /** Provide number of primitive values in "key" array */
  int (*getNumKey) (void* this);

  /** Assign float* value to inputOutput MFFloat field named "key". */
  void (*setKey) (void* this, float* values);

  /** Assign single float* value as the MFFloat array for inputOutput field named "key" */
  void (*setKey2) (void* this, float* value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DShaderNode defines an abstract node structure that extends structures X3DAppearanceChildNode and X3DNode.
  * Base type for all nodes that specify a programmable shader. */

struct X3DShaderNode
{
  struct X3DAppearanceChildNode*  extNode;

  /** Provide string value from initializeOnly SFString field named "language". */
  string (*getLanguage) (void* this);

  /** Assign string value to initializeOnly SFString field named "language". */
  void (*setLanguage) (void* this, string value);

  /** Assign SFBool value to inputOnly SFBool field named "activate". */
  void (*setActivate) (void* this, SFBool value);

  /** Provide SFBool value from outputOnly SFBool field named "isSelected". */
  SFBool (*getIsSelected) (void* this);

  /** Provide SFBool value from outputOnly SFBool field named "isValid". */
  SFBool (*getIsValid) (void* this);

  /** Provide string value from initializeOnly SFString field named "language". */
  string (*getLanguage) (void* this);

  /** Assign string value to initializeOnly SFString field named "language". */
  void (*setLanguage) (void* this, string value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DShapeNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Base type for all Shape nodes. */

struct X3DShapeNode
{
  struct X3DChildNode*  extNode;
  struct X3DBoundedObject*  extNode1;

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  void (*getBboxCenter) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void (*setBboxCenter) (void* this, float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  void (*getBboxSize) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void (*setBboxSize) (void* this, float* value);

  /** Provide SFBool value from inputOutput SFBool field named "bboxDisplay". */
  SFBool (*getBboxDisplay) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "bboxDisplay". */
  void (*setBboxDisplay) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "castShadow". */
  SFBool (*getCastShadow) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "castShadow". */
  void (*setCastShadow) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "visible". */
  SFBool (*getVisible) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "visible". */
  void (*setVisible) (void* this, SFBool value);

  /** Provide X3DAppearanceNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DAppearanceNode type field named "appearance". */
  void (*getAppearance) (void* this, struct X3DNode result);

  /** Assign X3DAppearanceNode value (using a properly typed node) to inputOutput X3DAppearanceNode type field named "appearance". */
  void (*setAppearance) (void* this, X3DAppearanceNode node);

  /** Assign X3DAppearanceNode value (using a properly typed protoInstance) */
  void (*setAppearance2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DGeometryNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DGeometryNode type field named "geometry". */
  void (*getGeometry) (void* this, struct X3DNode result);

  /** Assign X3DGeometryNode value (using a properly typed node) to inputOutput X3DGeometryNode type field named "geometry". */
  void (*setGeometry) (void* this, X3DGeometryNode node);

  /** Assign X3DGeometryNode value (using a properly typed protoInstance) */
  void (*setGeometry2) (void* this, struct X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DSingleTextureCoordinateNode defines an abstract node structure that extends structures X3DTextureCoordinateNode, X3DGeometricPropertyNode, and X3DNode.
  * Base type for all texture coordinate nodes which specify texture coordinates for a single texture. */

struct X3DSingleTextureCoordinateNode
{
  struct X3DTextureCoordinateNode*  extNode;

  /** Provide string value from inputOutput SFString field named "mapping". */
  string (*getMapping) (void* this);

  /** Assign string value to inputOutput SFString field named "mapping". */
  void (*setMapping) (void* this, string value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DSingleTextureNode defines an abstract node structure that extends structures X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all texture node types that define a single texture. A single texture can be used to influence a parameter of various material nodes in the Shape component, and it can be a child of MultiTexture. */

struct X3DSingleTextureNode
{
  struct X3DTextureNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DSingleTextureTransformNode defines an abstract node structure that extends structures X3DTextureTransformNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all texture transform nodes which specify texture coordinate transformation for a single texture. */

struct X3DSingleTextureTransformNode
{
  struct X3DTextureTransformNode*  extNode;

  /** Provide string value from inputOutput SFString field named "mapping". */
  string (*getMapping) (void* this);

  /** Assign string value to inputOutput SFString field named "mapping". */
  void (*setMapping) (void* this, string value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DSoundChannelNode defines an abstract node structure that extends structures X3DSoundNode, X3DChildNode, and X3DNode.
  * Base type for all sound destination nodes, which represent the final destination of an audio signal and are what the user can ultimately hear. */

struct X3DSoundChannelNode
{
  struct X3DSoundNode*  extNode;

  /** Provide int value from outputOnly SFInt32 field named "channelCount". */
  int (*getChannelCount) (void* this);

  /** Provide string value from inputOutput SFString field named "channelCountMode". */
  string (*getChannelCountMode) (void* this);

  /** Assign string value to inputOutput SFString field named "channelCountMode". */
  void (*setChannelCountMode) (void* this, string value);

  /** Provide string value from inputOutput SFString field named "channelInterpretation". */
  string (*getChannelInterpretation) (void* this);

  /** Assign string value to inputOutput SFString field named "channelInterpretation". */
  void (*setChannelInterpretation) (void* this, string value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  float (*getGain) (void* this);

  /** Assign float value to inputOutput SFFloat field named "gain". */
  void (*setGain) (void* this, float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DSoundDestinationNode defines an abstract node structure that extends structures X3DSoundNode, X3DChildNode, and X3DNode.
  * Base type for all sound destination nodes, which represent the final destination of an audio signal and are what the user can ultimately hear. */

struct X3DSoundDestinationNode
{
  struct X3DSoundNode*  extNode;

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide int value from outputOnly SFInt32 field named "channelCount". */
  int (*getChannelCount) (void* this);

  /** Provide string value from inputOutput SFString field named "channelCountMode". */
  string (*getChannelCountMode) (void* this);

  /** Assign string value to inputOutput SFString field named "channelCountMode". */
  void (*setChannelCountMode) (void* this, string value);

  /** Provide string value from inputOutput SFString field named "channelInterpretation". */
  string (*getChannelInterpretation) (void* this);

  /** Assign string value to inputOutput SFString field named "channelInterpretation". */
  void (*setChannelInterpretation) (void* this, string value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  float (*getGain) (void* this);

  /** Assign float value to inputOutput SFFloat field named "gain". */
  void (*setGain) (void* this, float value);

  /** Provide string value from inputOutput SFString field named "mediaDeviceID". */
  string (*getMediaDeviceID) (void* this);

  /** Assign string value to inputOutput SFString field named "mediaDeviceID". */
  void (*setMediaDeviceID) (void* this, string value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DSoundNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Base type for all sound nodes. */

struct X3DSoundNode
{
  struct X3DChildNode*  extNode;

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DSoundProcessingNode defines an abstract node structure that extends structures X3DTimeDependentNode, X3DChildNode, and X3DNode.
  * Base type for all sound processing nodes, which are used to enhance audio with filtering, delaying, changing gain, etc. */

struct X3DSoundProcessingNode
{
  struct X3DTimeDependentNode*  extNode;
  struct X3DSoundNode*  extNode1;

  /** Provide int value from outputOnly SFInt32 field named "channelCount". */
  int (*getChannelCount) (void* this);

  /** Provide string value from inputOutput SFString field named "channelCountMode". */
  string (*getChannelCountMode) (void* this);

  /** Assign string value to inputOutput SFString field named "channelCountMode". */
  void (*setChannelCountMode) (void* this, string value);

  /** Provide string value from inputOutput SFString field named "channelInterpretation". */
  string (*getChannelInterpretation) (void* this);

  /** Assign string value to inputOutput SFString field named "channelInterpretation". */
  void (*setChannelInterpretation) (void* this, string value);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  float (*getGain) (void* this);

  /** Assign float value to inputOutput SFFloat field named "gain". */
  void (*setGain) (void* this, float value);

  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "tailTime". */
  double (*getTailTime) (void* this);

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "tailTime". */
  void (*setTailTime) (void* this, double timestamp)

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide double value in seconds [0,∞) from outputOnly SFTime field named "elapsedTime". */
  double (*getElapsedTime) (void* this);

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide SFBool value from outputOnly SFBool field named "isPaused". */
  SFBool (*getIsPaused) (void* this);

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide double value in seconds from inputOutput SFTime field named "pauseTime". */
  double (*getPauseTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "pauseTime". */
  void (*setPauseTime) (void* this, double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "resumeTime". */
  double (*getResumeTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "resumeTime". */
  void (*setResumeTime) (void* this, double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "startTime". */
  double (*getStartTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "startTime". */
  void (*setStartTime) (void* this, double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "stopTime". */
  double (*getStopTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "stopTime". */
  void (*setStopTime) (void* this, double timestamp);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DSoundSourceNode defines an abstract node structure that extends structures X3DTimeDependentNode, X3DChildNode, and X3DNode.
  * Nodes implementing X3DSoundSourceNode provide signal inputs to the audio graph. */

struct X3DSoundSourceNode
{
  struct X3DTimeDependentNode*  extNode;
  struct X3DSoundNode*  extNode1;

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide float value from inputOutput SFFloat field named "gain". */
  float (*getGain) (void* this);

  /** Assign float value to inputOutput SFFloat field named "gain". */
  void (*setGain) (void* this, float value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide double value in seconds [0,∞) from outputOnly SFTime field named "elapsedTime". */
  double (*getElapsedTime) (void* this);

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide SFBool value from outputOnly SFBool field named "isPaused". */
  SFBool (*getIsPaused) (void* this);

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide double value in seconds from inputOutput SFTime field named "pauseTime". */
  double (*getPauseTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "pauseTime". */
  void (*setPauseTime) (void* this, double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "resumeTime". */
  double (*getResumeTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "resumeTime". */
  void (*setResumeTime) (void* this, double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "startTime". */
  double (*getStartTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "startTime". */
  void (*setStartTime) (void* this, double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "stopTime". */
  double (*getStopTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "stopTime". */
  void (*setStopTime) (void* this, double timestamp);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DTexture2DNode defines an abstract node structure that extends structures X3DSingleTextureNode, X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all nodes which specify 2D sources for texture images. */

struct X3DTexture2DNode
{
  struct X3DSingleTextureNode*  extNode;

  /** Provide SFBool value from initializeOnly SFBool field named "repeatS". */
  SFBool (*getRepeatS) (void* this);

  /** Assign SFBool value to initializeOnly SFBool field named "repeatS". */
  void (*setRepeatS) (void* this, SFBool value);

  /** Provide SFBool value from initializeOnly SFBool field named "repeatT". */
  SFBool (*getRepeatT) (void* this);

  /** Assign SFBool value to initializeOnly SFBool field named "repeatT". */
  void (*setRepeatT) (void* this, SFBool value);

  /** Provide TextureProperties value (using a properly typed node or X3DPrototypeInstance) from initializeOnly TextureProperties type field named "textureProperties". */
  void (*getTextureProperties) (void* this, struct X3DNode result);

  /** Assign TextureProperties value (using a properly typed node) to initializeOnly TextureProperties type field named "textureProperties". */
  void (*setTextureProperties) (void* this, TextureProperties node);

  /** Assign TextureProperties value (using a properly typed protoInstance) */
  void (*setTextureProperties2) (void* this, struct X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DTexture3DNode defines an abstract node structure that extends structures X3DTextureNode, X3DAppearanceChildNode, and X3DNode.
  * Base type for all nodes that specify 3D sources for texture images. */

struct X3DTexture3DNode
{
  struct X3DTextureNode*  extNode;

  /** Provide SFBool value from initializeOnly SFBool field named "repeatS". */
  SFBool (*getRepeatS) (void* this);

  /** Assign SFBool value to initializeOnly SFBool field named "repeatS". */
  void (*setRepeatS) (void* this, SFBool value);

  /** Provide SFBool value from initializeOnly SFBool field named "repeatT". */
  SFBool (*getRepeatT) (void* this);

  /** Assign SFBool value to initializeOnly SFBool field named "repeatT". */
  void (*setRepeatT) (void* this, SFBool value);

  /** Provide SFBool value from initializeOnly SFBool field named "repeatR". */
  SFBool (*getRepeatR) (void* this);

  /** Assign SFBool value to initializeOnly SFBool field named "repeatR". */
  void (*setRepeatR) (void* this, SFBool value);

  /** Provide TextureProperties value (using a properly typed node or X3DPrototypeInstance) from initializeOnly TextureProperties type field named "textureProperties". */
  void (*getTextureProperties) (void* this, struct X3DNode result);

  /** Assign TextureProperties value (using a properly typed node) to initializeOnly TextureProperties type field named "textureProperties". */
  void (*setTextureProperties) (void* this, TextureProperties node);

  /** Assign TextureProperties value (using a properly typed protoInstance) */
  void (*setTextureProperties2) (void* this, struct X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DTextureCoordinateNode defines an abstract node structure that extends structures X3DGeometricPropertyNode and X3DNode.
  * Base type for all nodes which specify texture coordinates. */

struct X3DTextureCoordinateNode
{
  struct X3DGeometricPropertyNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DTextureNode defines an abstract node structure that extends structures X3DAppearanceChildNode and X3DNode.
  * Base type for all nodes which specify sources for texture images. */

struct X3DTextureNode
{
  struct X3DAppearanceChildNode*  extNode;

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DTextureProjectorNode defines an abstract node structure that extends structures X3DLightNode, X3DChildNode, and X3DNode.
  * Base type for all node types that specify texture projector nodes, which provide a form of lighting. */

struct X3DTextureProjectorNode
{
  struct X3DLightNode*  extNode;

  /** Provide float value (0,∞) from outputOnly SFFloat field named "aspectRatio". */
  float (*getAspectRatio) (void* this);

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide 3-tuple float* value from inputOutput SFVec3f field named "direction". */
  void (*getDirection) (void* this, float* result);

  /** Assign 3-tuple float* value to inputOutput SFVec3f field named "direction". */
  void (*setDirection) (void* this, float* value);

  /** Provide float value [-1,∞) from inputOutput SFFloat field named "farDistance". */
  float (*getFarDistance) (void* this);

  /** Assign float value [-1,∞) to inputOutput SFFloat field named "farDistance". */
  void (*setFarDistance) (void* this, float value)

  /** Provide SFBool value from inputOutput SFBool field named "global". */
  SFBool (*getGlobal) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "global". */
  void (*setGlobal) (void* this, SFBool value);

  /** Provide 3-tuple float* value from inputOutput SFVec3f field named "location". */
  void (*getLocation) (void* this, float* result);

  /** Assign 3-tuple float* value to inputOutput SFVec3f field named "location". */
  void (*setLocation) (void* this, float* value);

  /** Provide float value [-1,∞) from inputOutput SFFloat field named "nearDistance". */
  float (*getNearDistance) (void* this);

  /** Assign float value [-1,∞) to inputOutput SFFloat field named "nearDistance". */
  void (*setNearDistance) (void* this, float value)

  /** Provide X3DTexture2DNode value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DTexture2DNode type field named "texture". */
  void (*getTexture) (void* this, struct X3DNode result);

  /** Assign X3DTexture2DNode value (using a properly typed node) to inputOutput X3DTexture2DNode type field named "texture". */
  void (*setTexture) (void* this, X3DTexture2DNode node);

  /** Assign X3DTexture2DNode value (using a properly typed protoInstance) */
  void (*setTexture2) (void* this, struct X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide float value from inputOutput SFFloat field named "ambientIntensity". */
  float (*getAmbientIntensity) (void* this);

  /** Assign float value to inputOutput SFFloat field named "ambientIntensity". */
  void (*setAmbientIntensity) (void* this, float value);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "color". */
  void (*getColor) (void* this, float* result);

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "color". */
  void (*setColor) (void* this, float* color)

  /** Provide float value [0,∞) from inputOutput SFFloat field named "intensity". */
  float (*getIntensity) (void* this);

  /** Assign float value [0,∞) to inputOutput SFFloat field named "intensity". */
  void (*setIntensity) (void* this, float value)

  /** Provide SFBool value from inputOutput SFBool field named "on". */
  SFBool (*getOn) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "on". */
  void (*setOn) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "shadows". */
  SFBool (*getShadows) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "shadows". */
  void (*setShadows) (void* this, SFBool value);

  /** Provide float value from inputOutput SFFloat field named "shadowIntensity". */
  float (*getShadowIntensity) (void* this);

  /** Assign float value to inputOutput SFFloat field named "shadowIntensity". */
  void (*setShadowIntensity) (void* this, float value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DTextureTransformNode defines an abstract node structure that extends structures X3DAppearanceChildNode and X3DNode.
  * Base type for all nodes which specify a transformation of texture coordinates. */

struct X3DTextureTransformNode
{
  struct X3DAppearanceChildNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DTimeDependentNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Base type from which all time-dependent nodes are derived. */

struct X3DTimeDependentNode
{
  struct X3DChildNode*  extNode;

  /** Provide double value in seconds [0,∞) from outputOnly SFTime field named "elapsedTime". */
  double (*getElapsedTime) (void* this);

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide SFBool value from outputOnly SFBool field named "isPaused". */
  SFBool (*getIsPaused) (void* this);

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide double value in seconds from inputOutput SFTime field named "pauseTime". */
  double (*getPauseTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "pauseTime". */
  void (*setPauseTime) (void* this, double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "resumeTime". */
  double (*getResumeTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "resumeTime". */
  void (*setResumeTime) (void* this, double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "startTime". */
  double (*getStartTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "startTime". */
  void (*setStartTime) (void* this, double timestamp);

  /** Provide double value in seconds from inputOutput SFTime field named "stopTime". */
  double (*getStopTime) (void* this);

  /** Assign double value in seconds to inputOutput SFTime field named "stopTime". */
  void (*setStopTime) (void* this, double timestamp);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DTouchSensorNode defines an abstract node structure that extends structures X3DPointingDeviceSensorNode, X3DSensorNode, X3DChildNode, and X3DNode.
  * Base type for all touch-style pointing device sensors. */

struct X3DTouchSensorNode
{
  struct X3DPointingDeviceSensorNode*  extNode;

  /** Provide double value in seconds from outputOnly SFTime field named "touchTime". */
  double (*getTouchTime) (void* this);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide SFBool value from outputOnly SFBool field named "isOver". */
  SFBool (*getIsOver) (void* this);

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide SFBool value from outputOnly SFBool field named "isActive". */
  SFBool (*getIsActive) (void* this);

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DTriggerNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * Base type from which all trigger nodes are derived. */

struct X3DTriggerNode
{
  struct X3DChildNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DVertexAttributeNode defines an abstract node structure that extends structures X3DGeometricPropertyNode and X3DNode.
  * Base type for all nodes that specify per-vertex attribute information to the shader. */

struct X3DVertexAttributeNode
{
  struct X3DGeometricPropertyNode*  extNode;

  /** Provide string value from inputOutput SFString field named "name". */
  string (*getName) (void* this);

  /** Assign string value to inputOutput SFString field named "name". */
  void (*setName) (void* this, string value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DViewpointNode defines an abstract node structure that extends structures X3DBindableNode, X3DChildNode, and X3DNode.
  * Node type X3DViewpointNode defines a specific location in the local coordinate system from which the user may view the scene, and also defines a viewpoint binding stack. */

struct X3DViewpointNode
{
  struct X3DBindableNode*  extNode;

  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide SFBool value from inputOutput SFBool field named "jump". */
  SFBool (*getJump) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "jump". */
  void (*setJump) (void* this, SFBool value);

  /** Provide 4-tuple float* value in radians from inputOutput SFRotation field named "orientation". */
  float* (*getOrientation) (void* this);

  /** Assign 4-tuple float* value in radians to inputOutput SFRotation field named "orientation". */
  void (*setOrientation) (void* this, float* value);

  /** Provide SFBool value from inputOutput SFBool field named "retainUserOffsets". */
  SFBool (*getRetainUserOffsets) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "retainUserOffsets". */
  void (*setRetainUserOffsets) (void* this, SFBool value);

  /** Provide float value from inputOutput SFFloat field named "farDistance". */
  float (*getFarDistance) (void* this);

  /** Assign float value to inputOutput SFFloat field named "farDistance". */
  void (*setFarDistance) (void* this, float value);

  /** Provide float value from inputOutput SFFloat field named "nearDistance". */
  float (*getNearDistance) (void* this);

  /** Assign float value to inputOutput SFFloat field named "nearDistance". */
  void (*setNearDistance) (void* this, float value);

  /** Provide SFBool value from inputOutput SFBool field named "viewAll". */
  SFBool (*getViewAll) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "viewAll". */
  void (*setViewAll) (void* this, SFBool value);

  /** Provide NavigationInfo value (using a properly typed node or X3DPrototypeInstance) from inputOutput NavigationInfo type field named "navigationInfo". */
  void (*getNavigationInfo) (void* this, struct X3DNode result);

  /** Assign NavigationInfo value (using a properly typed node) to inputOutput NavigationInfo type field named "navigationInfo". */
  void (*setNavigationInfo) (void* this, NavigationInfo node);

  /** Assign NavigationInfo value (using a properly typed protoInstance) */
  void (*setNavigationInfo2) (void* this, struct X3DPrototypeInstance protoInstance);

  // ===== methods for fields inherited from parent interfaces =====

  /** Assign SFBool value to inputOnly SFBool field named "set_bind". */
  void (*setBind) (void* this, SFBool value);

  /** Provide double value in seconds from outputOnly SFTime field named "bindTime". */
  double (*getBindTime) (void* this);

  /** Provide SFBool value from outputOnly SFBool field named "isBound". */
  SFBool (*getIsBound) (void* this);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DViewportNode defines an abstract node structure that extends structures X3DGroupingNode, X3DChildNode, and X3DNode.
  * The X3DViewportNode abstract node type is the base node type for viewport nodes. */

struct X3DViewportNode
{
  struct X3DGroupingNode*  extNode;

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  void (*getBboxCenter) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void (*setBboxCenter) (void* this, float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  void (*getBboxSize) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void (*setBboxSize) (void* this, float* value);

  /** Provide SFBool value from inputOutput SFBool field named "bboxDisplay". */
  SFBool (*getBboxDisplay) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "bboxDisplay". */
  void (*setBboxDisplay) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "visible". */
  SFBool (*getVisible) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "visible". */
  void (*setVisible) (void* this, SFBool value);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren (void* this, X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node) as the MFNode array for inputOnly field named "addChildren" */
  void addChildren2 (void* this, X3DChildNode* node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren3 (void* this, struct X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "addChildren". */
  void addChildren4 (void* this, struct X3DNode* nodes);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren (void* this, X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node) as the MFNode array for inputOnly field named "removeChildren" */
  void removeChildren2 (void* this, X3DChildNode* node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren3 (void* this, struct X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOnly X3DChildNode type field named "removeChildren". */
  void removeChildren4 (void* this, struct X3DNode* nodes);

  /** Provide X3DChildNode* value (using a properly typed node array or X3DPrototypeInstance array) from inputOutput X3DChildNode type field named "children". */
  void (*getChildren) (void* this, struct X3DNode* result);

  /** Provide number of nodes in "children" array */
  int (*getNumChildren) (void* this);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  void (*setChildren) (void* this, X3DChildNode* nodes);

  /** Assign single X3DChildNode* value (using a properly typed node) as the MFNode array for inputOutput field named "children" */
  void (*setChildren2) (void* this, X3DChildNode* node);

  /** Assign X3DChildNode* value (using a properly typed protoInstance array) to inputOutput X3DChildNode type field named "children". */
  void (*setChildren3) (void* this, struct X3DPrototypeInstance node);

  /** Assign X3DChildNode* value (using a properly typed node array) to inputOutput X3DChildNode type field named "children". */
  void (*setChildren4) (void* this, struct X3DNode* nodes);

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DVolumeDataNode defines an abstract node structure that extends structures X3DChildNode and X3DNode.
  * The X3DVolumeDataNode abstract node type is the base type for all node types that describe volumetric data to be rendered. */

struct X3DVolumeDataNode
{
  struct X3DChildNode*  extNode;
  struct X3DBoundedObject*  extNode1;

  /** Provide 3-tuple float* value (-∞,∞) from inputOutput SFVec3f field named "dimensions". */
  void (*getDimensions) (void* this, float* result);

  /** Assign 3-tuple float* value (-∞,∞) to inputOutput SFVec3f field named "dimensions". */
  void (*setDimensions) (void* this, float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  void (*getBboxCenter) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void (*setBboxCenter) (void* this, float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  void (*getBboxSize) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void (*setBboxSize) (void* this, float* value);

  /** Provide SFBool value from inputOutput SFBool field named "bboxDisplay". */
  SFBool (*getBboxDisplay) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "bboxDisplay". */
  void (*setBboxDisplay) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "visible". */
  SFBool (*getVisible) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "visible". */
  void (*setVisible) (void* this, SFBool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DVolumeRenderStyleNode defines an abstract node structure that extends structure X3DNode.
  * The X3DVolumeRenderStyleNode abstract node type is the base type for all node types that specify a specific visual rendering style to be used when rendering volume data. */

struct X3DVolumeRenderStyleNode
{
  struct X3DNode*  extNode;

  /** Provide SFBool value from inputOutput SFBool field named "enabled". */
  SFBool (*getEnabled) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "enabled". */
  void (*setEnabled) (void* this, SFBool value);

  // ===== methods for fields inherited from parent interfaces =====

  /** Provide IS value (using a properly typed node or X3DPrototypeInstance) from inputOutput IS type field named "IS". */
  void (*getIS) (void* this, struct X3DNode result);

  /** Assign IS value (using a properly typed node) to inputOutput IS type field named "IS". */
  void (*setIS) (void* this, IS node);

  /** Assign IS value (using a properly typed protoInstance) */
  void (*setIS2) (void* this, struct X3DPrototypeInstance protoInstance);

  /** Provide X3DMetadataObject value (using a properly typed node or X3DPrototypeInstance) from inputOutput X3DMetadataObject type field named "metadata". */
  void (*getMetadata) (void* this, struct X3DNode result);

  /** Assign X3DMetadataObject value (using a properly typed node) to inputOutput X3DMetadataObject type field named "metadata". */
  void (*setMetadata) (void* this, X3DMetadataObject node);

  /** Assign X3DMetadataObject value (using a properly typed protoInstance) */
  void (*setMetadata2) (void* this, struct X3DPrototypeInstance protoInstance);
}
;/** X3DBoundedObject defines an abstract structure.
  * X3DBoundedObject indicates that bounding box values can be provided (or computed) to encompass this node and any children. */

struct X3DBoundedObject
{
  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxCenter". */
  void (*getBboxCenter) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxCenter". */
  void (*setBboxCenter) (void* this, float* value);

  /** Provide 3-tuple float* value from initializeOnly SFVec3f field named "bboxSize". */
  void (*getBboxSize) (void* this, float* result);

  /** Assign 3-tuple float* value to initializeOnly SFVec3f field named "bboxSize". */
  void (*setBboxSize) (void* this, float* value);

  /** Provide SFBool value from inputOutput SFBool field named "bboxDisplay". */
  SFBool (*getBboxDisplay) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "bboxDisplay". */
  void (*setBboxDisplay) (void* this, SFBool value);

  /** Provide SFBool value from inputOutput SFBool field named "visible". */
  SFBool (*getVisible) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "visible". */
  void (*setVisible) (void* this, SFBool value);
}
;/** X3DFogObject defines an abstract structure.
  * Abstract type describing a node that influences the lighting equation through the use of fog semantics. */

struct X3DFogObject
{
  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from inputOutput SFColor field named "color". */
  void (*getColor) (void* this, float* result);

  /** Assign 3-tuple float* value using RGB values [0..1] using RGB values [0..1] to inputOutput SFColor field named "color". */
  void (*setColor) (void* this, float* color)

  /** Provide string value from inputOutput SFString field named "fogType". */
  string (*getFogType) (void* this);

  /** Assign string value to inputOutput SFString field named "fogType". */
  void (*setFogType) (void* this, string value);

  /** Provide float value [0,∞) from inputOutput SFFloat field named "visibilityRange". */
  float (*getVisibilityRange) (void* this);

  /** Assign float value [0,∞) to inputOutput SFFloat field named "visibilityRange". */
  void (*setVisibilityRange) (void* this, float value)
}
;/** X3DMetadataObject defines an abstract structure.
  * Each node inheriting the X3DMetadataObject interface contains a single array of strictly typed values: MFBool, MFInt32, MFFloat, MFDouble, MFString, or MFNode, the latter having children that are all Metadata nodes. */

struct X3DMetadataObject
{
  /** Provide string value from inputOutput SFString field named "name". */
  string (*getName) (void* this);

  /** Assign string value to inputOutput SFString field named "name". */
  void (*setName) (void* this, string value);

  /** Provide string value from inputOutput SFString field named "reference". */
  string (*getReference) (void* this);

  /** Assign string value to inputOutput SFString field named "reference". */
  void (*setReference) (void* this, string value);
}
;/** X3DPickableObject defines an abstract structure.
  * The X3DPickableObject abstract interface marks a node as being capable of having customized picking performed on its contents or children. */

struct X3DPickableObject
{
  /** Provide string* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  string* (*getObjectType) (void* this);

  /** Provide number of primitive values in "objectType" array */
  int (*getNumObjectType) (void* this);

  /** Assign string* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void (*setObjectType) (void* this, string* values)

  /** Provide string* value ["ALL","NONE","TERRAIN",...] from inputOutput MFString field named "objectType". */
  string* (*getObjectType) (void* this);

  /** Provide number of primitive values in "objectType" array */
  int (*getNumObjectType) (void* this);

  /** Assign string* value ["ALL","NONE","TERRAIN",...] to inputOutput MFString field named "objectType". */
  void (*setObjectType) (void* this, string* values);

  /** Assign single string* value ["ALL","NONE","TERRAIN",...] as the MFString array for inputOutput field named "objectType" */
  void (*setObjectType2) (void* this, string* value);

  /** Provide SFBool value from inputOutput SFBool field named "pickable". */
  SFBool (*getPickable) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "pickable". */
  void (*setPickable) (void* this, SFBool value);
}
;/** X3DProgrammableShaderObject defines an abstract structure.
  * Base type for all nodes that specify arbitrary fields for interfacing with per-object attribute values. */

struct X3DProgrammableShaderObject
{}
;/** X3DUrlObject defines an abstract structure.
  * X3DUrlObject indicates that a node has content loaded from a Uniform Resource Locator (URL) and can be tracked via a LoadSensor. Such child nodes have containerField='children' to indicate their relationship to the parent LoadSensor node. */

struct X3DUrlObject
{
  /** Provide string value from inputOutput SFString field named "description". */
  string (*getDescription) (void* this);

  /** Assign string value to inputOutput SFString field named "description". */
  void (*setDescription) (void* this, string value);

  /** Provide SFBool value from inputOutput SFBool field named "load". */
  SFBool (*getLoad) (void* this);

  /** Assign SFBool value to inputOutput SFBool field named "load". */
  void (*setLoad) (void* this, SFBool value);

  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "autoRefresh". */
  double (*getAutoRefresh) (void* this);

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "autoRefresh". */
  void (*setAutoRefresh) (void* this, double timestamp)

  /** Provide double value in seconds [0,∞) from inputOutput SFTime field named "autoRefreshTimeLimit". */
  double (*getAutoRefreshTimeLimit) (void* this);

  /** Assign double value in seconds [0,∞) to inputOutput SFTime field named "autoRefreshTimeLimit". */
  void (*setAutoRefreshTimeLimit) (void* this, double timestamp)

  /** Provide string* value from inputOutput MFString field named "url". */
  string* (*getUrl) (void* this);

  /** Provide number of primitive values in "url" array */
  int (*getNumUrl) (void* this);

  /** Assign string* value to inputOutput MFString field named "url". */
  void (*setUrl) (void* this, string* values);

  /** Assign single string* value as the MFString array for inputOutput field named "url" */
  void (*setUrl2) (void* this, string* value);
}
;enum X3DFieldTypes {

    int INPUT_ONLY = 1,
    int INITIALIZE_ONLY = 2,
    int INPUT_OUTPUT = 3,
    int OUTPUT_ONLY = 4,

    int SFBOOL = 1,
    int MFBOOL = 2,
    int SFCOLOR = 21,
    int MFCOLOR = 22,
    int SFCOLORRGBA = 23,
    int MFCOLORRGBA = 24,
    int SFDOUBLE = 7,
    int MFDOUBLE = 8,
    int SFFLOAT = 5,
    int MFFLOAT = 6,
    int SFIMAGE = 25,
    int MFIMAGE = 26,
    int SFINT32 = 3,
    int MFINT32 = 4,
    int SFNODE = 11,
    int MFNODE = 12,
    int SFROTATION = 19,
    int MFROTATION = 20,
    int SFSTRING = 27,
    int MFSTRING = 28,
    int SFTIME = 9,
    int MFTIME = 10,
    int SFVEC2F = 13,
    int MFVEC2F = 14,
    int SFVEC3F = 15,
    int MFVEC3F = 16,
    int SFVEC3D = 17,
    int MFVEC3D = 18
}
;struct X3DFieldEvent {

	void (*X3DFieldEvent) (void* this , struct Object src, double ts, struct Object data);

	double (*getTime) (void* this);

	struct Object (*getData) (void* this);
}
;struct X3DFieldEventListener {

	void (*readableFieldChanged) (void* this, struct X3DFieldEvent evt);
}
;struct X3DFieldDefinition {

    char* (*getName) (void* this);
 
    int (*getAccessType) (void* this);
 
    int (*getFieldType) (void* this);
 
    char* (*getFieldTypeString) (void* this);
}
;struct X3DField {
 
    struct X3DFieldDefinition (*getDefinition) (void* this);
 
    SFBool (*isReadable) (void* this);
 
    SFBool (*isWritable) (void* this);
 
    void (*addX3DeventListener) (void* this, struct X3DFieldEventListener l);
 
    void (*removeX3DeventListener) (void* this, struct X3DFieldEventListener l);
 
    void (*setUserData) (void* this, Object data);
 
    Object (*getUserData) (void* this);
}

;struct MField {
 
    struct X3DField* x3dField;

    int (*size) (void* this);
 
    void (*clear) (void* this);
 
    void (*remove) (void* this, int index);

}
;/** SFBool defines a node type interface.
  * SFBool is a logical type with possible values (true|false) to match the XML boolean type. Hint: XML boolean values are lower case (true|false) in order to maintain compatibility with HTML and other XML documents. */

struct SFBool
{
   struct X3DField* field
  /** Provide SFBool value from type SFBool */
  SFBool (*getValue) (void* this);

  /** Provide SFBool value from type SFBool */
  void (*setValue) (void* this, SFBool value);
}
;/** MFBool defines a node type interface.
  * MFBool is an array of boolean values. Type MFBool was previously undefined in the VRML97 Specification, but nevertheless needed for event utilities and scripting. Example use: MFBool is useful for defining a series of behavior states using a BooleanSequencer prototype. Hint: XML boolean values are lower case (true|false) in order to maintain compatibility with HTML and other XML documents. */

struct MFBool
{
   struct MField* field
  /** Provide SFBool* value from type MFBool */
  SFBool* (*getValue) (void* this);

  /** Utility method to provide single value from MFBool array */
  SFBool (*get1Value) (void* this, int index);

  /** Provide SFBool* value from type MFBool */
  void (*setValue) (void* this, int size, SFBool* values);

  /** Utility method to set a single value in MFBool array */
  void (*set1Value) (void* this, int index, SFBool value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single value to MFBool array */
  void (*append) (void this, SFBool value);

  /** Utility method to insert a single value in MFBool array */
  void (*insertValue) (void* this, int index, SFBool value)
}
;/** SFColor defines a node type interface.
  * SFColor specifies one RGB (red-green-blue) color triple, where each color value is an RGB triple of floating point numbers in range [0,1]. The default value of an uninitialized SFColor field is (0 0 0). Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFColor
{
   struct X3DField* field
  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type SFColor */
  void (*getValue) (void* this, float* result);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type SFColor */
  void (*setValue) (void* this, float* color)
}
;/** MFColor defines a node type interface.
  * MFColor specifies zero or more SFColor RGB triples, where each color value is an RGB triple of floating point numbers in range [0,1]. The default value of an uninitialized MFColor field is the empty list. Individual SFColor array values are optionally separated by commas in XML syntax. */

struct MFColor
{
   struct MField* field
  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type MFColor */
  void (*getValue) (void* this, float* result);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type MFColor */
  void (*getValue) (void* this, float** result); // overloaded method for convenience

  /** Utility method to provide single 3-tuple value from MFColor array */
  void (*get1Value) (void* this, int index, float* result);

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type MFColor */
  void (*setValue) (void* this, int size, float* colors)

  /** Provide 3-tuple float* value using RGB values [0..1] using RGB values [0..1] from type MFColor */
  void (*setValue) (void* this, float** colors) // overloaded method for convenience

  /** Utility method to set a single 3-tuple value in MFColor array */
  void (*set1Value) (void* this, int index, float* color) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single 3-tuple value to MFColor array */
  void (*append) (void this, float* color);

  /** Utility method to insert a single 3-tuple value in MFColor array */
  void (*insertValue) (void* this, int index, float* color)
}
;/** SFColorRGBA defines a node type interface.
  * SFColorRGBA specifies one RGBA (red-green-blue-alpha) color 4-tuple, where each color value is an RGBA 4-tuple of floating point numbers in range [0,1]. Alpha (opacity) values = (1 - transparency). The default value of an uninitialized SFColorRGBA field is (0 0 0 0). Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFColorRGBA
{
   struct X3DField* field
  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type SFColorRGBA */
  void (*getValue) (void* this, float* result);

  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type SFColorRGBA */
  void (*setValue) (void* this, float* color)
}
;/** MFColorRGBA defines a node type interface.
  * MFColorRGBA specifies zero or more SFColorRGBA 4-tuples, where each color value is an RGBA 4-tuple of floating point numbers in range [0,1]. Alpha (opacity) values = (1 - transparency). The default value of an uninitialized MFColor field is the empty list. Individual SFColorRGBA array values are optionally separated by commas in XML syntax. */

struct MFColorRGBA
{
   struct MField* field
  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  void (*getValue) (void* this, float* result);

  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  void (*getValue) (void* this, float** result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFColorRGBA array */
  void (*get1Value) (void* this, int index, float* result);

  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  void (*setValue) (void* this, int size, float* colors)

  /** Provide 4-tuple float* value using RGBA values [0..1] using RGB values [0..1] from type MFColorRGBA */
  void (*setValue) (void* this, float** colors) // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFColorRGBA array */
  void (*set1Value) (void* this, int index, float* color) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single 4-tuple value to MFColorRGBA array */
  void (*append) (void this, float* color);

  /** Utility method to insert a single 4-tuple value in MFColorRGBA array */
  void (*insertValue) (void* this, int index, float* color)
}
;/** SFDouble defines a node type interface.
  * SFDouble is a double-precision floating-point type. Array values are optionally separated by commas in XML syntax. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision for rationale. */

struct SFDouble
{
   struct X3DField* field
  /** Provide double value from type SFDouble */
  double (*getValue) (void* this);

  /** Provide double value from type SFDouble */
  void (*setValue) (void* this, double value);
}
;/** MFDouble defines a node type interface.
  * MFDouble is an array of Double values, meaning a double-precision floating-point array type. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision for rationale. Array values are optionally separated by commas in XML syntax. */

struct MFDouble
{
   struct MField* field
  /** Provide double* value from type MFDouble */
  double* (*getValue) (void* this);

  /** Utility method to provide single value from MFDouble array */
  double (*get1Value) (void* this, int index);

  /** Provide double* value from type MFDouble */
  void (*setValue) (void* this, int size, double* values);

  /** Utility method to set a single value in MFDouble array */
  void (*set1Value) (void* this, int index, double value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single value to MFDouble array */
  void (*append) (void this, double value);

  /** Utility method to insert a single value in MFDouble array */
  void (*insertValue) (void* this, int index, double value)
}
;/** SFFloat defines a node type interface.
  * SFFloat is a single-precision floating-point type. */

struct SFFloat
{
   struct X3DField* field
  /** Provide float value from type SFFloat */
  float (*getValue) (void* this);

  /** Provide float value from type SFFloat */
  void (*setValue) (void* this, float value);
}
;/** MFFloat defines a node type interface.
  * MFFloat is an array of SFFloat values, meaning a single-precision floating-point array type. Array values are optionally separated by commas in XML syntax. */

struct MFFloat
{
   struct MField* field
  /** Provide float* value from type MFFloat */
  float* (*getValue) (void* this);

  /** Utility method to provide single value from MFFloat array */
  float (*get1Value) (void* this, int index);

  /** Provide float* value from type MFFloat */
  void (*setValue) (void* this, int size, float* values);

  /** Utility method to set a single value in MFFloat array */
  void (*set1Value) (void* this, int index, float value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single value to MFFloat array */
  void (*append) (void this, float value);

  /** Utility method to insert a single value in MFFloat array */
  void (*insertValue) (void* this, int index, float value)
}
;/** SFImage defines a node type interface.
  * SFImage specifies a single uncompressed 2-dimensional pixel image. SFImage fields contain three integers representing the width, height and number of components in the image, followed by (width x height) hexadecimal or integer values representing the pixels in the image. */

struct SFImage
{
   struct X3DField* field
    /** Get image width in pixels */
    int (*getWidth) (void* this);

    /** Get image height in pixels */
    int (*getHeight) (void* this);

    /** Get number of components in an image:
      * 1 (intensity), 2 (intensity alpha), 3 (red green blue), 4 (red green blue alpha-opacity).*/
    int (*getComponents) (void* this);

    /** Get array of pixel values [0-255] */
    void (*getPixels) (void* this, int* pixels);

    struct WritableRenderedImage (*getImage) (void* this);

    /** Initialize image */
    void (*setValue) (void* this, int width,
                          int height,
                          int components,
                          int[] pixels);

    /** Assign a new image as current image */
    void (*setImage) (void* this, struct RenderedImage image);

    /** Assign a portion of a new image as part of current image */
    void (*setSubImage*) (void* this, struct RenderedImage image,
                             int srcWidth,
                             int srcHeight,
                             int srcXOffset,
                             int srcYOffset,
                             int destXOffset,
                             int destYOffset);
}
;/** MFImage defines a node type interface.
  * MFImage is an array of SFImage values. */

struct MFImage
{
   struct MField* field
    /** Get selected image width in pixels */
    int (*getWidth) (void* this, int imageIndex) throws ArrayIndexOutOfBoundsException;

    /** Get selected image height in pixels */
    int (*getHeight) (void* this, int imageIndex) throws ArrayIndexOutOfBoundsException;

    /** Get number of components in selected image:
      * 1 (intensity), 2 (intensity alpha), 3 (red green blue), 4 (red green blue alpha-opacity).*/
    int (*getComponents) (void* this, int imageIndex) throws ArrayIndexOutOfBoundsException;

    /** Get array of pixel values [0-255] in selected image */
    void (*getPixels) (void* this, int imageIndex, int* pixels) throws ArrayIndexOutOfBoundsException;

    struct WritableRenderedImage* (*getImage)(void* this, int imageIndex) throws ArrayIndexOutOfBoundsException;

    /** Assign a new image as a replacement image within the current image array */
    void (*setImage) (void* this, int imageIndex, RenderedImage img) throws ArrayIndexOutOfBoundsException;

    /** Assign a portion of a new image as part of current selected image in array */
    void (*setSubImage) (void* this, int imageIndex,
                             RenderedImage img,
                             int srcWidth,
                             int srcHeight,
                             int srcXOffset,
                             int srcYOffset,
                             int destXOffset,
                             int destYOffset) throws ArrayIndexOutOfBoundsException;

    /** Utility method to set all values for selected image in array */
    void (*set1Value) (void* this, int imageIndex, int value) throws ArrayIndexOutOfBoundsException;

    /** Initialize selected image */
    void (*set1Value1) (void* this, int imageIndex,
                           int width,
                           int height,
                           int components,
                           int[] pixels) throws ArrayIndexOutOfBoundsException;

    /** Utility method to set all values for all images in array */
    void (*setValue) (void* this, int* value);

    /** Assign a new image array as current image array */
    void (*setImage) (void* this, struct RenderedImage* img);

    /** Append a new image to current image array */
    void (*append) (void* this, struct RenderedImage value);

    /** Insert a new image in the current image array */
    void (*insertValue) (void* this, int imageIndex, struct RenderedImage value) throws ArrayIndexOutOfBoundsException;
}
;/** SFInt32 defines a node type interface.
  * SFInt32 specifies one 32-bit signed integer. */

struct SFInt32
{
   struct X3DField* field
  /** Provide int value from type SFInt32 */
  int (*getValue) (void* this);

  /** Provide int value from type SFInt32 */
  void (*setValue) (void* this, int value);
}
;/** MFInt32 defines a node type interface.
  * MFInt32 defines an array of 32-bit signed integers. Array values are optionally separated by commas in XML syntax. */

struct MFInt32
{
   struct MField* field
  /** Provide MFInt32 value from type MFInt32 */
  MFInt32 (*getValue) (void* this);

  /** Utility method to provide single value from MFInt32 array */
  int (*get1Value) (void* this, int index);

  /** Provide MFInt32 value from type MFInt32 */
  void (*setValue) (void* this, int size, MFInt32 values);

  /** Utility method to set a single value in MFInt32 array */
  void (*set1Value) (void* this, int index, int value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single value to MFInt32 array */
  void (*append) (void this, int value);

  /** Utility method to insert a single value in MFInt32 array */
  void (*insertValue) (void* this, int index, int value)
}
;/** SFRotation defines a node type interface.
  * SFRotation is an axis-angle 4-tuple, indicating X-Y-Z direction axis plus angle orientation about that axis. The first three values specify a normalized axis vector about which the rotation takes place, so the first three values shall be within the range [-1..+1] in order to represent a normalized unit vector. The fourth value specifies the amount of right-handed rotation about that axis in radians. Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFRotation
{
   struct X3DField* field
  /** Provide 4-tuple float* value in radians from type SFRotation */
  float* (*getValue) (void* this);

  /** Provide 4-tuple float* value in radians from type SFRotation */
  void (*setValue) (void* this, float* angle);
}
;/** MFRotation defines a node type interface.
  * MFRotation is an array of SFRotation values. Individual singleton SFRotation array values are optionally separated by commas in XML syntax. */

struct MFRotation
{
   struct MField* field
  /** Provide 4-tuple float* value in radians from type MFRotation */
  float* (*getValue) (void* this);

  /** Provide 4-tuple float* value in radians from type MFRotation */
  void (*getValue) (void* this, float** result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFRotation array */
  float* (*get1Value) (void* this, int index);

  /** Provide 4-tuple float* value in radians from type MFRotation */
  void (*setValue) (void* this, int size, float* angles);

  /** Provide 4-tuple float* value in radians from type MFRotation */
  void (*setValue) (void* this, float** angles); // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFRotation array */
  void (*set1Value) (void* this, int index, float* angle) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single 4-tuple value to MFRotation array */
  void (*append) (void this, float* angle);

  /** Utility method to insert a single 4-tuple value in MFRotation array */
  void (*insertValue) (void* this, int index, float* angle)
}
;/** SFString defines a node type interface.
  * SFString defines a single string encoded with the UTF-8 universal character set. */

struct SFString
{
   struct X3DField* field
  /** Provide string value from type SFString */
  string (*getValue) (void* this);

  /** Provide string value from type SFString */
  void (*setValue) (void* this, string value);
}
;/** MFString defines a node type interface.
  * MFString is an array of SFString values, each "quoted" and separated by whitespace. Individual SFString array values are optionally separated by commas in XML syntax. */

struct MFString
{
   struct MField* field
  /** Provide string* value from type MFString */
  string* (*getValue) (void* this);

  /** Utility method to provide single value from MFString array */
  string (*get1Value) (void* this, int index);

  /** Provide string* value from type MFString */
  void (*setValue) (void* this, int size, string* values);

  /** Utility method to set a single value in MFString array */
  void (*set1Value) (void* this, int index, string value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single value to MFString array */
  void (*append) (void this, string value);

  /** Utility method to insert a single value in MFString array */
  void (*insertValue) (void* this, int index, string value)
}
;/** SFTime defines a node type interface.
  * SFTime specifies a single time value, expressed as a double-precision floating point number. Typically, SFTime fields represent the number of seconds since Jan 1, 1970, 00:00:00 GMT. */

struct SFTime
{
   struct X3DField* field
  /** Provide double value in seconds from type SFTime */
  double (*getValue) (void* this);

  /** Provide long value in nanoseconds from type SFTime */
  long (*getCValue) (void* this);

  /** Provide double value in seconds from type SFTime */
  void (*setValue) (void* this, double timestamp);

  /** Assign long value in nanoseconds using System.nanoTime() to type SFTime */
  void (*setValue) (void* this, long value);
}
;/** MFTime defines a node type interface.
  * MFTime is an array of SFTime values. Array values are optionally separated by commas in XML syntax. */

struct MFTime
{
   struct MField* field
  /** Provide double* value in seconds from type MFTime */
  double* (*getValue) (void* this);

  /** Utility method to provide single value from MFTime array */
  double (*get1Value) (void* this, int index);

  /** Utility method to provide single long value in nanoseconds from MFTime array */
  long (*get1CValue) (void* this, int index);

  /** Provide double* value in seconds from type MFTime */
  void (*setValue) (void* this, int size, double* timestamps);

  /** Assign long array in nanoseconds to type MFTime */
  void (*setValue) (void* this, int size, long* values);

  /** Utility method to set a single value in MFTime array */
  void (*set1Value) (void* this, int index, double timestamp) throws ArrayIndexOutOfBoundsException;

  /** Utility method to set a single long value in nanoseconds using System.nanoTime() in MFTime array */
  void (*set1Value) (void* this, int index, long value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single value to MFTime array */
  void (*append) (void this, double timestamp);

  /** Utility method to insert a single value in MFTime array */
  void (*insertValue) (void* this, int index, double timestamp)
}
;/** SFVec2f defines a node type interface.
  * SFVec2f is a 2-tuple pair of SFFloat values. Hint: SFVec2f can be used to specify a 2D single-precision coordinate. Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFVec2f
{
   struct X3DField* field
  /** Provide 2-tuple float* value from type SFVec2f */
  void (*getValue) (void* this, float* result);

  /** Provide 2-tuple float* value from type SFVec2f */
  void (*setValue) (void* this, float* value);
}
;/** MFVec2f defines a node type interface.
  * MFVec2f is an array of SFVec2f values. Individual singleton SFVec2f array values are optionally separated by commas in XML syntax. */

struct MFVec2f
{
   struct MField* field
  /** Provide 2-tuple float* value from type MFVec2f */
  void (*getValue) (void* this, float* result);

  /** Provide 2-tuple float* value from type MFVec2f */
  void (*getValue) (void* this, float** result); // overloaded method for convenience

  /** Utility method to provide single 2-tuple value from MFVec2f array */
  void (*get1Value) (void* this, int index, float* result);

  /** Provide 2-tuple float* value from type MFVec2f */
  void (*setValue) (void* this, int size, float* values);

  /** Provide 2-tuple float* value from type MFVec2f */
  void (*setValue) (void* this, float** values); // overloaded method for convenience

  /** Utility method to set a single 2-tuple value in MFVec2f array */
  void (*set1Value) (void* this, int index, float* value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single 2-tuple value to MFVec2f array */
  void (*append) (void this, float* value);

  /** Utility method to insert a single 2-tuple value in MFVec2f array */
  void (*insertValue) (void* this, int index, float* value)
}
;/** SFVec2d defines a node type interface.
  * SFVec2d is a 2-tuple pair of SFDouble values. Hint: SFVec2d can be used to specify a 2D double-precision coordinate. Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFVec2d
{
   struct X3DField* field
  /** Provide 2-tuple double* value from type SFVec2d */
  void (*getValue) (void* this, double* result);

  /** Provide 2-tuple double* value from type SFVec2d */
  void (*setValue) (void* this, double* value);
}
;/** MFVec2d defines a node type interface.
  * MFVec2d is an array of SFVec2d values. Individual singleton SFVec2d array values are optionally separated by commas in XML syntax. */

struct MFVec2d
{
   struct MField* field
  /** Provide 2-tuple double* value from type MFVec2d */
  void (*getValue) (void* this, double* result);

  /** Provide 2-tuple double* value from type MFVec2d */
  void (*getValue) (void* this, double** result); // overloaded method for convenience

  /** Utility method to provide single 2-tuple value from MFVec2d array */
  void (*get1Value) (void* this, int index, double* result);

  /** Provide 2-tuple double* value from type MFVec2d */
  void (*setValue) (void* this, int size, double* values);

  /** Provide 2-tuple double* value from type MFVec2d */
  void (*setValue) (void* this, double** values); // overloaded method for convenience

  /** Utility method to set a single 2-tuple value in MFVec2d array */
  void (*set1Value) (void* this, int index, double* value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single 2-tuple value to MFVec2d array */
  void (*append) (void this, double* value);

  /** Utility method to insert a single 2-tuple value in MFVec2d array */
  void (*insertValue) (void* this, int index, double* value)
}
;/** SFVec3f defines a node type interface.
  * SFVec3f is a 3-tuple triplet of SFFloat values. Hint: SFVec3f can be used to specify a 3D coordinate or a 3D scale value. Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFVec3f
{
   struct X3DField* field
  /** Provide 3-tuple float* value from type SFVec3f */
  void (*getValue) (void* this, float* result);

  /** Provide 3-tuple float* value from type SFVec3f */
  void (*setValue) (void* this, float* value);
}
;/** MFVec3f defines a node type interface.
  * MFVec3f is an array of SFVec3f values. Individual singleton SFVec3f array values are optionally separated by commas in XML syntax. */

struct MFVec3f
{
   struct MField* field
  /** Provide 3-tuple float* value from type MFVec3f */
  void (*getValue) (void* this, float* result);

  /** Provide 3-tuple float* value from type MFVec3f */
  void (*getValue) (void* this, float** result); // overloaded method for convenience

  /** Utility method to provide single 3-tuple value from MFVec3f array */
  void (*get1Value) (void* this, int index, float* result);

  /** Provide 3-tuple float* value from type MFVec3f */
  void (*setValue) (void* this, int size, float* values);

  /** Provide 3-tuple float* value from type MFVec3f */
  void (*setValue) (void* this, float** values); // overloaded method for convenience

  /** Utility method to set a single 3-tuple value in MFVec3f array */
  void (*set1Value) (void* this, int index, float* value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single 3-tuple value to MFVec3f array */
  void (*append) (void this, float* value);

  /** Utility method to insert a single 3-tuple value in MFVec3f array */
  void (*insertValue) (void* this, int index, float* value)
}
;/** SFVec3d defines a node type interface.
  * SFVec3d is a 3-tuple triplet of SFDouble values. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision. Hint: SFVec3d can be used to specify a georeferenced 3D coordinate. Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFVec3d
{
   struct X3DField* field
  /** Provide 3-tuple double* value from type SFVec3d */
  void (*getValue) (void* this, double* result);

  /** Provide 3-tuple double* value from type SFVec3d */
  void (*setValue) (void* this, double* value);
}
;/** MFVec3d defines a node type interface.
  * MFVec3d is an array of SFVec3d values. Individual singleton SFVec3d array values are optionally separated by commas in XML syntax. Original rationale for inclusion: GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision. Hint: MFVec3d can be used to specify a list of georeferenced 3D coordinates. */

struct MFVec3d
{
   struct MField* field
  /** Provide 3-tuple double* value from type MFVec3d */
  void (*getValue) (void* this, double* result);

  /** Provide 3-tuple double* value from type MFVec3d */
  void (*getValue) (void* this, double** result); // overloaded method for convenience

  /** Utility method to provide single 3-tuple value from MFVec3d array */
  void (*get1Value) (void* this, int index, double* result);

  /** Provide 3-tuple double* value from type MFVec3d */
  void (*setValue) (void* this, int size, double* values);

  /** Provide 3-tuple double* value from type MFVec3d */
  void (*setValue) (void* this, double** values); // overloaded method for convenience

  /** Utility method to set a single 3-tuple value in MFVec3d array */
  void (*set1Value) (void* this, int index, double* value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single 3-tuple value to MFVec3d array */
  void (*append) (void this, double* value);

  /** Utility method to insert a single 3-tuple value in MFVec3d array */
  void (*insertValue) (void* this, int index, double* value)
}
;/** SFVec4f defines a node type interface.
  * SFVec4f is a 4-tuple set of single-precision floating-point values, specifying a 3D homogeneous vector. Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFVec4f
{
   struct X3DField* field
  /** Provide 4-tuple float* value from type SFVec4f */
  void (*getValue) (void* this, float* result);

  /** Provide 4-tuple float* value from type SFVec4f */
  void (*setValue) (void* this, float* value);
}
;/** MFVec4f defines a node type interface.
  * MFVec4f is zero or more SFVec4f values. Individual singleton SFVec4f array values are optionally separated by commas in XML syntax. */

struct MFVec4f
{
   struct MField* field
  /** Provide 4-tuple float* value from type MFVec4f */
  void (*getValue) (void* this, float* result);

  /** Provide 4-tuple float* value from type MFVec4f */
  void (*getValue) (void* this, float** result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFVec4f array */
  void (*get1Value) (void* this, int index, float* result);

  /** Provide 4-tuple float* value from type MFVec4f */
  void (*setValue) (void* this, int size, float* values);

  /** Provide 4-tuple float* value from type MFVec4f */
  void (*setValue) (void* this, float** values); // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFVec4f array */
  void (*set1Value) (void* this, int index, float* value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single 4-tuple value to MFVec4f array */
  void (*append) (void this, float* value);

  /** Utility method to insert a single 4-tuple value in MFVec4f array */
  void (*insertValue) (void* this, int index, float* value)
}
;/** SFVec4d defines a node type interface.
  * SFVec4d is a 4-tuple set of double-precision floating-point values, specifying a 3D homogeneous vector. Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFVec4d
{
   struct X3DField* field
  /** Provide 4-tuple double* value from type SFVec4d */
  void (*getValue) (void* this, double* result);

  /** Provide 4-tuple double* value from type SFVec4d */
  void (*setValue) (void* this, double* value);
}
;/** MFVec4d defines a node type interface.
  * MFVec4d is zero or more SFVec4d values. Individual singleton SFVec4d array values are optionally separated by commas in XML syntax. */

struct MFVec4d
{
   struct MField* field
  /** Provide 4-tuple double* value from type MFVec4d */
  void (*getValue) (void* this, double* result);

  /** Provide 4-tuple double* value from type MFVec4d */
  void (*getValue) (void* this, double** result); // overloaded method for convenience

  /** Utility method to provide single 4-tuple value from MFVec4d array */
  void (*get1Value) (void* this, int index, double* result);

  /** Provide 4-tuple double* value from type MFVec4d */
  void (*setValue) (void* this, int size, double* values);

  /** Provide 4-tuple double* value from type MFVec4d */
  void (*setValue) (void* this, double** values); // overloaded method for convenience

  /** Utility method to set a single 4-tuple value in MFVec4d array */
  void (*set1Value) (void* this, int index, double* value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single 4-tuple value to MFVec4d array */
  void (*append) (void this, double* value);

  /** Utility method to insert a single 4-tuple value in MFVec4d array */
  void (*insertValue) (void* this, int index, double* value)
}
;/** SFMatrix3f defines a node type interface.
  * SFMatrix3f specifies a 3x3 matrix of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFMatrix3f
{
   struct X3DField* field
  /** Provide float* value from type SFMatrix3f */
  float* (*getValue) (void* this);

  /** Provide float* value from type SFMatrix3f */
  void (*setValue) (void* this, float* value);
}
;/** MFMatrix3f defines a node type interface.
  * MFMatrix3f specifies zero or more 3x3 matrices of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 9-tuple values. */

struct MFMatrix3f
{
   struct MField* field
  /** Provide float* value from type MFMatrix3f */
  float* (*getValue) (void* this);

  /** Provide float* value from type MFMatrix3f */
  void (*getValue) (void* this, float** result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix3f array */
  float* (*get1Value) (void* this, int index);

  /** Provide float* value from type MFMatrix3f */
  void (*setValue) (void* this, int size, float* values);

  /** Provide float* value from type MFMatrix3f */
  void (*setValue) (void* this, float** values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix3f array */
  void (*set1Value) (void* this, int index, float* value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single value to MFMatrix3f array */
  void (*append) (void this, float* value);

  /** Utility method to insert a single value in MFMatrix3f array */
  void (*insertValue) (void* this, int index, float* value)
}
;/** SFMatrix3d defines a node type interface.
  * SFMatrix3d specifies a 3x3 matrix of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFMatrix3d
{
   struct X3DField* field
  /** Provide double* value from type SFMatrix3d */
  double* (*getValue) (void* this);

  /** Provide double* value from type SFMatrix3d */
  void (*setValue) (void* this, double* value);
}
;/** MFMatrix3d defines a node type interface.
  * MFMatrix3d specifies zero or more 3x3 matrices of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 9-tuple values. */

struct MFMatrix3d
{
   struct MField* field
  /** Provide double* value from type MFMatrix3d */
  double* (*getValue) (void* this);

  /** Provide double* value from type MFMatrix3d */
  void (*getValue) (void* this, double** result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix3d array */
  double* (*get1Value) (void* this, int index);

  /** Provide double* value from type MFMatrix3d */
  void (*setValue) (void* this, int size, double* values);

  /** Provide double* value from type MFMatrix3d */
  void (*setValue) (void* this, double** values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix3d array */
  void (*set1Value) (void* this, int index, double* value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single value to MFMatrix3d array */
  void (*append) (void this, double* value);

  /** Utility method to insert a single value in MFMatrix3d array */
  void (*insertValue) (void* this, int index, double* value)
}
;/** SFMatrix4f defines a node type interface.
  * SFMatrix4f specifies a 4x4 matrix of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFMatrix4f
{
   struct X3DField* field
  /** Provide float* value from type SFMatrix4f */
  float* (*getValue) (void* this);

  /** Provide float* value from type SFMatrix4f */
  void (*setValue) (void* this, float* value);
}
;/** MFMatrix4f defines a node type interface.
  * MFMatrix4f specifies zero or more 4x4 matrices of single-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 16-tuple values. */

struct MFMatrix4f
{
   struct MField* field
  /** Provide float* value from type MFMatrix4f */
  float* (*getValue) (void* this);

  /** Provide float* value from type MFMatrix4f */
  void (*getValue) (void* this, float** result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix4f array */
  float* (*get1Value) (void* this, int index);

  /** Provide float* value from type MFMatrix4f */
  void (*setValue) (void* this, int size, float* values);

  /** Provide float* value from type MFMatrix4f */
  void (*setValue) (void* this, float** values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix4f array */
  void (*set1Value) (void* this, int index, float* value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single value to MFMatrix4f array */
  void (*append) (void this, float* value);

  /** Utility method to insert a single value in MFMatrix4f array */
  void (*insertValue) (void* this, int index, float* value)
}
;/** SFMatrix4d defines a node type interface.
  * SFMatrix4d specifies a 4x4 matrix of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters within singleton values do not pass strict XML validation. */

struct SFMatrix4d
{
   struct X3DField* field
  /** Provide double* value from type SFMatrix4d */
  double* (*getValue) (void* this);

  /** Provide double* value from type SFMatrix4d */
  void (*setValue) (void* this, double* value);
}
;/** MFMatrix4d defines a node type interface.
  * MFMatrix4d specifies zero or more 4x4 matrices of double-precision floating point numbers, organized in row-major fashion. Warning: comma characters can only appear between singleton 16-tuple values. */

struct MFMatrix4d
{
   struct MField* field
  /** Provide double* value from type MFMatrix4d */
  double* (*getValue) (void* this);

  /** Provide double* value from type MFMatrix4d */
  void (*getValue) (void* this, double** result); // overloaded method for convenience

  /** Utility method to provide single value from MFMatrix4d array */
  double* (*get1Value) (void* this, int index);

  /** Provide double* value from type MFMatrix4d */
  void (*setValue) (void* this, int size, double* values);

  /** Provide double* value from type MFMatrix4d */
  void (*setValue) (void* this, double** values); // overloaded method for convenience

  /** Utility method to set a single value in MFMatrix4d array */
  void (*set1Value) (void* this, int index, double* value) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single value to MFMatrix4d array */
  void (*append) (void this, double* value);

  /** Utility method to insert a single value in MFMatrix4d array */
  void (*insertValue) (void* this, int index, double* value)
}
;/** SFNode defines a node type interface.
  * SFNode specifies an X3D node; the default empty value of an uninitialized SFNode field is sometimes described as NULL. */

struct SFNode
{
   struct X3DField* field
  /** Provide struct X3DNode value (using a properly typed node or X3DPrototypeInstance) from type SFNode */
  void (*getValue) (void* this, struct X3DNode& result);

  /** Provide struct X3DNode value (using a properly typed node or X3DPrototypeInstance) from type SFNode */
  void (*setValue) (void* this, struct X3DNode node);
}
;/** MFNode defines a node type interface.
  * MFNode specifies zero or more nodes; the default value of an MFNode field is the empty list. */

struct MFNode
{
   struct MField* field
  /** Provide struct X3DNode* value (using a properly typed node array or X3DPrototypeInstance array) from type MFNode */
  void (*getValue) (void* this, struct X3DNode* result);

  /** Utility method to provide single value from MFNode array */
  void (*get1Value) (void* this, int index, struct X3DNode result);

  /** Provide struct X3DNode* value (using a properly typed node array or X3DPrototypeInstance array) from type MFNode */
  void (*setValue) (void* this, int size, struct X3DNode* nodes);

  /** Utility method to set a single value in MFNode array */
  void (*set1Value) (void* this, int index, struct X3DNode node) throws ArrayIndexOutOfBoundsException;

  /** Utility method to append a single value to MFNode array */
  void (*append) (void this, struct X3DNode node);

  /** Utility method to insert a single value in MFNode array */
  void (*insertValue) (void* this, int index, struct X3DNode* node)
}
;struct BrowserEvent 
{
    struct EventObject* eventObject;
    enum BrowserEventType {
    INITIALIZED = 0,
    SHUTDOWN = 1,
    URL_ERROR = 2,
    CONNECTION_ERROR = 10,
    LAST_IDENTIFIER = 100,
    }
 
    void struct BrowserEvent(void* this, struct Object browser, int action);
    int (*getID) (void* this);
}
;struct BrowserFactory
{
    void (*BrowserFactory(void* this);
 
    void (*setBrowserFactoryImpl) (void* this, struct BrowserFactoryImpl fac);
 
    static struct X3DComponent (*createX3DComponent) (void* this, Map params);
 
    static struct ExternalBrowser (*getBrowser) (void* this);
 
    static struct ExternalBrowser (*getBrowser) (void* this, string frameName,
                                             int index);
 
    static struct ExternalBrowser (*getBrowser) (void* this, InetAddress address, int port);
}
;struct X3DFieldEvent 
{
    struct EventObject* eventObject;
	
    void (*X3DFieldEvent)(void* this , struct Object src, double ts, struct Object data);
	
    double (*getTime) (void* this);
	
    struct Object (*getData) (void* this);
}
;struct Matrix3
{
   void Matrix3(void* this);
   void (*setIdentity) (void* this);
   void (*set) (void* this, int row, int column)
   float (*get) (void* this, int row, int column)
   void (*setTransform)(void* this, SFVec2f translation,
                             SFVec3f rotation,
                             SFVec2f scale,
                             SFVec3f scaleOrientation,
                             SFVec2f center)
   void (*getTransform)(void* this, SFVec2f& translation,
                             SFVec3f& rotation,
                             SFVec2f& scale)
   struct Matrix3 (*inverse)(void* this)
   struct Matrix3 (*transpose)(void* this)
   struct Matrix3 (*multiplyLeft)(void* this, Matrix3 mat)
   struct Matrix3 (*multiplyRight)(void* this, Matrix3 mat)
   struct Matrix3 (*multiplyRowVector)(void* this, SFVec3f vec)
   struct Matrix3 (*multiplyColVector)(void* this, SFVec3f vec)
}
;struct Matrix4
{
   void Matrix4(void* this);
   void (*setIdentity)(void* this);
   void (*set)(void* this, int row, int column)
   float (*get)(void* this, int row, int column)
   void (*setTransform)(void* this, SFVec3f translation,
                         SFRotation rotation,
                         SFVec3f scale,
                         SFRotation scaleOrientation,
                         SFVec3f center)
   void (*getTransform)(void* this, SFVec3f& translation,
                         SFRotation& rotation,
                         SFVec3f& scale)
   Matrix3 (*inverse)(void* this)
   Matrix3 (*transpose)(void* this)
   Matrix3 (*multiplyLeft)(void* this, Matrix4 mat)
   Matrix3 (*multiplyRight)(void* this, Matrix4 mat)
   Matrix3 (*multiplyRowVector)(void* this, SFVec3f vec)
   Matrix3 (*multiplyColVector)(void* this, SFVec3f vec)
}
;struct ComponentInfo
{
    char* (*getName)(void* this);
    int (*getLevel)(void* this);
    char* (*getTitle)(void* this);
    char* (*getProviderURL)(void* this);
    char* (*toX3Dstring)(void* this);
}
;struct ProfileInfo
{
    char* (*getName)(void* this);
    char* (*getTitle)(void* this);
    struct ComponentInfo* (*getComponents)(void* this);
    char* (*toX3Dstring)(void* this);
}
;struct X3DException 
{
    struct RuntimeException* RuntimeException;
    void (*X3DException1) (void* this);
    void (*X3DException2) (void* this, char*);
}
;struct BrowserNotSharedException 
{
    struct X3DException* x3dException;
    void (*BrowserNotSharedException1) (void* this);
    void (*BrowserNotSharedException2) (void* this, char*);
}
;struct ConnectionException
{
    struct X3DException* x3dException;
    void (*ConnectionException1) (void* this);
    void (*ConnectionException2) (void* this, char*);
}
;struct ImportedNodeException 
{
    struct X3DException* x3dException;
    void (*ImportedNodeException1) (void* this);
    void (*ImportedNodeException2) (void* this, char*);
}
;struct InsufficientCapabilitiesException 
{
    struct X3DException* x3dException;
    void (*InsufficientCapabilitiesException1) (void* this);
    void (*InsufficientCapabilitiesException2) (void* this, char*);
}
;struct InvalidBrowserException 
{
    struct X3DException* x3dException;
    void (*InvalidBrowserException1) (void* this);
    void (*InvalidBrowserException2) (void* this, char*);
}
;struct InvalidDocumentException 
{
    struct X3DException* x3dException;
    void (*InvalidDocumentException1) (void* this);
    void (*InvalidDocumentException2) (void* this, char*);
}
;struct InvalidExecutionContextException 
{
    struct X3DException* x3dException;
    void (*InvalidExecutionContextException1) (void* this);
    void (*InvalidExecutionContextException2) (void* this, char*);
}
;struct InvalidFieldException 
{
    struct X3DException* x3dException;
    void (*InvalidFieldException1) (void* this);
    void (*InvalidFieldException2) (void* this, char*);
}
;struct InvalidFieldValueException 
{
    struct X3DException* x3dException;
    void (*InvalidFieldValueException1) (void* this);
    void (*InvalidFieldValueException2) (void* this, char*);
}
;struct InvalidNodeException 
{
    struct X3DException* x3dException;
    void (*InvalidNodeException1) (void* this);
    void (*InvalidNodeException2) (void* this, char*);
}
;struct InvalidOperationTimingException 
{
    struct X3DException* x3dException;
    void (*InvalidOperationTimingException1) (void* this);
    void (*InvalidOperationTimingException2) (void* this, char*);
}
;struct InvalidProtoException 
{
    struct X3DException* x3dException;
    void (*InvalidProtoException1) (void* this);
    void (*InvalidProtoException2) (void* this, char*);
}
;struct InvalidRouteException 
{
    struct X3DException* x3dException;
    void (*InvalidRouteException1) (void* this);
    void (*InvalidRouteException2) (void* this, char*);
}
;struct InvalidURLException 
{
    struct X3DException* x3dException;
    void (*InvalidURLException1) (void* this);
    void (*InvalidURLException2) (void* this, char*);
}
;struct InvalidX3DException 
{
    struct X3DException* x3dException;
    void (*InvalidX3DException1) (void* this);
    void (*InvalidX3DException2) (void* this, char*);
}
;struct NodeInUseException 
{
    struct X3DException* x3dException;
    void (*NodeInUseException1) (void* this);
    void (*NodeInUseException2) (void* this, char*);
}
;struct NodeUnavailableException 
{
    struct X3DException* x3dException;
    void (*NodeUnavailableException1) (void* this);
    void (*NodeUnavailableException2) (void* this, char*);
}
;struct NoSuchBrowserException 
{
    struct X3DException* x3dException;
    void (*NoSuchBrowserException1) (void* this);
    void (*NoSuchBrowserException2) (void* this, char*);
}
;struct NotSupportedException 
{
    struct X3DException* X3DException;
    void (*NotSupportedException1) (void* this);
    void (*NotSupportedException2) (void* this, char*);
}
;struct URLUnavailableException 
{
    struct X3DException* X3DException;
    void (*URLUnavailableException1) (void* this);
    void (*URLUnavailableException2) (void* this, char*);
}
;