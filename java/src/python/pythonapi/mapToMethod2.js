var mapToMethod2 = {
	"Shape" : {
		"ProtoInstance" : "setGeometry"
	},
	"HAnimJoint" : {
		"Transform" : "addChildren"
	},
	"Appearance" : {
		"ProtoInstance" : "setMaterial"
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
		"IS" : "addSkin",
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
		"ProgramShader" : "addShaders"
	},
	"Collision" : {
		"Transform" : "addChildren",
		"Group" : "addChildren"
	},
	"PrimitivePickSensor" : {
		"IS" : "addPickedGeometry"
	},
	"GeoLOD" : {
		"GeoOrigin" : "setGeoOrigin"
	},
	"LinePickSensor" : {
		"IS" : "addPickedGeometry"
	},
	"GeoMetadata" : {
		"IS" : "addData"
	},
	"Scene" : {
		"LayerSet" : "addLayerSet",
		"MetadataString" : "addChildren"
	}
};

module.exports = mapToMethod2;
