var mapToMethod2 = {
	"Shape" : {
		"ProtoInstance" : "setGeometry"
	},
	"HAnimJoint" : {
		"Transform" : "addChild"
	},
	"Appearance" : {
		"ProtoInstance" : "setMaterial",
		"ProgramShader" : "addShaders"
	},
	"ComposedShader" : {
		"field" : "addField"
	},
	"Script" : {
		"field" : "addField"
	},
	"MetadataSet" : {
		"ProtoInstance" : "setMetadata"
	},
	"RigidBody" : {
		"CollidableShape" : "addGeometry"
	},
	"HAnimHumanoid" : {
		"HAnimJoint" : "addJoints",
		"HAnimSegment" : "addSegments",
		"HAnimSite" : "addViewpoints",
		"Group" : "addSkeleton"
	},
	"X3DPickSensorNode" : {
		"IS" : "addPickedGeometry"
	},
	"VolumePickSensor" : {
		"IS" : "addPickedGeometry"
	},
	"PointPickSensor" : {
		"IS" : "addPickedGeometry"
	},
	"ProtoBody" : {
		"ProgramShader" : "addChild"
	},
	"Collision" : {
		"Transform" : "addChild",
		"Group" : "addChild"
	},
	"PrimitivePickSensor" : {
		"IS" : "addPickedGeometry"
	},
	"GeoLOD" : {
		"GeoOrigin" : "setGeoOrigin"
	},
	"Scene" : {
		"LayerSet" : "addLayerSet",
		"MetadataString" : "addMetadata"
	}
};

module.exports = mapToMethod2;
