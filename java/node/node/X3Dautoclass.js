var java = require('java');
java.options.push("-Djava.awt.headless=true");
java.options.push("-Xmx1000m");
//java.options.push("-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=5005");
java.classpath.push("C:/Users/coderextreme/X3DJSONLD/pythonSAI/X3DJSAIL.4.0.full.jar");
java.classpath.push("X3DJSAIL.4.0.full.jar");
java.classpath.push("pythonSAI/X3DJSAIL.4.0.full.jar");
java.classpath.push("../pythonSAI/X3DJSAIL.4.0.full.jar");
java.classpath.push("../../pythonSAI/X3DJSAIL.4.0.full.jar");
java.classpath.push("../../../pythonSAI/X3DJSAIL.4.0.full.jar");
java.classpath.push("../../../../pythonSAI/X3DJSAIL.4.0.full.jar");
java.classpath.push("../../../../../pythonSAI/X3DJSAIL.4.0.full.jar");
java.classpath.push("../../../../../../pythonSAI/X3DJSAIL.4.0.full.jar");
java.classpath.push("../../../../../../../pythonSAI/X3DJSAIL.4.0.full.jar");
java.classpath.push("../classes");
java.classpath.push("../../classes");
java.classpath.push("jars/X3DJSAIL.4.0.full.jar");
java.classpath.push("../jars/X3DJSAIL.4.0.full.jar");
java.classpath.push("../../jars/X3DJSAIL.4.0.full.jar");
module.exports = {
Anchor : java.import('org.web3d.x3d.jsail.Networking.Anchor'),
Appearance : java.import('org.web3d.x3d.jsail.Shape.Appearance'),
Arc2D : java.import('org.web3d.x3d.jsail.Geometry2D.Arc2D'),
ArcClose2D : java.import('org.web3d.x3d.jsail.Geometry2D.ArcClose2D'),
AudioClip : java.import('org.web3d.x3d.jsail.Sound.AudioClip'),
Background : java.import('org.web3d.x3d.jsail.EnvironmentalEffects.Background'),
BallJoint : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.BallJoint'),
Billboard : java.import('org.web3d.x3d.jsail.Navigation.Billboard'),
BlendedVolumeStyle : java.import('org.web3d.x3d.jsail.VolumeRendering.BlendedVolumeStyle'),
BooleanFilter : java.import('org.web3d.x3d.jsail.EventUtilities.BooleanFilter'),
BooleanSequencer : java.import('org.web3d.x3d.jsail.EventUtilities.BooleanSequencer'),
BooleanToggle : java.import('org.web3d.x3d.jsail.EventUtilities.BooleanToggle'),
BooleanTrigger : java.import('org.web3d.x3d.jsail.EventUtilities.BooleanTrigger'),
BoundaryEnhancementVolumeStyle : java.import('org.web3d.x3d.jsail.VolumeRendering.BoundaryEnhancementVolumeStyle'),
BoundedPhysicsModel : java.import('org.web3d.x3d.jsail.ParticleSystems.BoundedPhysicsModel'),
Box : java.import('org.web3d.x3d.jsail.Geometry3D.Box'),
CADAssembly : java.import('org.web3d.x3d.jsail.CADGeometry.CADAssembly'),
CADFace : java.import('org.web3d.x3d.jsail.CADGeometry.CADFace'),
CADLayer : java.import('org.web3d.x3d.jsail.CADGeometry.CADLayer'),
CADPart : java.import('org.web3d.x3d.jsail.CADGeometry.CADPart'),
CartoonVolumeStyle : java.import('org.web3d.x3d.jsail.VolumeRendering.CartoonVolumeStyle'),
Circle2D : java.import('org.web3d.x3d.jsail.Geometry2D.Circle2D'),
ClipPlane : java.import('org.web3d.x3d.jsail.Rendering.ClipPlane'),
CollidableOffset : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.CollidableOffset'),
CollidableShape : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.CollidableShape'),
Collision : java.import('org.web3d.x3d.jsail.Navigation.Collision'),
CollisionCollection : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.CollisionCollection'),
CollisionSensor : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.CollisionSensor'),
CollisionSpace : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.CollisionSpace'),
Color : java.import('org.web3d.x3d.jsail.Rendering.Color'),
ColorChaser : java.import('org.web3d.x3d.jsail.Followers.ColorChaser'),
ColorDamper : java.import('org.web3d.x3d.jsail.Followers.ColorDamper'),
ColorInterpolator : java.import('org.web3d.x3d.jsail.Interpolation.ColorInterpolator'),
ColorRGBA : java.import('org.web3d.x3d.jsail.Rendering.ColorRGBA'),
ComposedCubeMapTexture : java.import('org.web3d.x3d.jsail.CubeMapTexturing.ComposedCubeMapTexture'),
ComposedShader : java.import('org.web3d.x3d.jsail.Shaders.ComposedShader'),
ComposedTexture3D : java.import('org.web3d.x3d.jsail.Texturing3D.ComposedTexture3D'),
ComposedVolumeStyle : java.import('org.web3d.x3d.jsail.VolumeRendering.ComposedVolumeStyle'),
Cone : java.import('org.web3d.x3d.jsail.Geometry3D.Cone'),
ConeEmitter : java.import('org.web3d.x3d.jsail.ParticleSystems.ConeEmitter'),
Contact : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.Contact'),
Contour2D : java.import('org.web3d.x3d.jsail.NURBS.Contour2D'),
ContourPolyline2D : java.import('org.web3d.x3d.jsail.NURBS.ContourPolyline2D'),
Coordinate : java.import('org.web3d.x3d.jsail.Rendering.Coordinate'),
CoordinateChaser : java.import('org.web3d.x3d.jsail.Followers.CoordinateChaser'),
CoordinateDamper : java.import('org.web3d.x3d.jsail.Followers.CoordinateDamper'),
CoordinateDouble : java.import('org.web3d.x3d.jsail.NURBS.CoordinateDouble'),
CoordinateInterpolator : java.import('org.web3d.x3d.jsail.Interpolation.CoordinateInterpolator'),
CoordinateInterpolator2D : java.import('org.web3d.x3d.jsail.Interpolation.CoordinateInterpolator2D'),
Cylinder : java.import('org.web3d.x3d.jsail.Geometry3D.Cylinder'),
CylinderSensor : java.import('org.web3d.x3d.jsail.PointingDeviceSensor.CylinderSensor'),
DirectionalLight : java.import('org.web3d.x3d.jsail.Lighting.DirectionalLight'),
DISEntityManager : java.import('org.web3d.x3d.jsail.DIS.DISEntityManager'),
DISEntityTypeMapping : java.import('org.web3d.x3d.jsail.DIS.DISEntityTypeMapping'),
Disk2D : java.import('org.web3d.x3d.jsail.Geometry2D.Disk2D'),
DoubleAxisHingeJoint : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.DoubleAxisHingeJoint'),
EaseInEaseOut : java.import('org.web3d.x3d.jsail.Interpolation.EaseInEaseOut'),
EdgeEnhancementVolumeStyle : java.import('org.web3d.x3d.jsail.VolumeRendering.EdgeEnhancementVolumeStyle'),
ElevationGrid : java.import('org.web3d.x3d.jsail.Geometry3D.ElevationGrid'),
EspduTransform : java.import('org.web3d.x3d.jsail.DIS.EspduTransform'),
ExplosionEmitter : java.import('org.web3d.x3d.jsail.ParticleSystems.ExplosionEmitter'),
Extrusion : java.import('org.web3d.x3d.jsail.Geometry3D.Extrusion'),
FillProperties : java.import('org.web3d.x3d.jsail.Shape.FillProperties'),
FloatVertexAttribute : java.import('org.web3d.x3d.jsail.Shaders.FloatVertexAttribute'),
Fog : java.import('org.web3d.x3d.jsail.EnvironmentalEffects.Fog'),
FogCoordinate : java.import('org.web3d.x3d.jsail.EnvironmentalEffects.FogCoordinate'),
FontStyle : java.import('org.web3d.x3d.jsail.Text.FontStyle'),
ForcePhysicsModel : java.import('org.web3d.x3d.jsail.ParticleSystems.ForcePhysicsModel'),
GeneratedCubeMapTexture : java.import('org.web3d.x3d.jsail.CubeMapTexturing.GeneratedCubeMapTexture'),
GeoCoordinate : java.import('org.web3d.x3d.jsail.Geospatial.GeoCoordinate'),
GeoElevationGrid : java.import('org.web3d.x3d.jsail.Geospatial.GeoElevationGrid'),
GeoLocation : java.import('org.web3d.x3d.jsail.Geospatial.GeoLocation'),
GeoLOD : java.import('org.web3d.x3d.jsail.Geospatial.GeoLOD'),
GeoMetadata : java.import('org.web3d.x3d.jsail.Geospatial.GeoMetadata'),
GeoOrigin : java.import('org.web3d.x3d.jsail.Geospatial.GeoOrigin'),
GeoPositionInterpolator : java.import('org.web3d.x3d.jsail.Geospatial.GeoPositionInterpolator'),
GeoProximitySensor : java.import('org.web3d.x3d.jsail.Geospatial.GeoProximitySensor'),
GeoTouchSensor : java.import('org.web3d.x3d.jsail.Geospatial.GeoTouchSensor'),
GeoTransform : java.import('org.web3d.x3d.jsail.Geospatial.GeoTransform'),
GeoViewpoint : java.import('org.web3d.x3d.jsail.Geospatial.GeoViewpoint'),
Group : java.import('org.web3d.x3d.jsail.Grouping.Group'),
HAnimDisplacer : java.import('org.web3d.x3d.jsail.HAnim.HAnimDisplacer'),
HAnimHumanoid : java.import('org.web3d.x3d.jsail.HAnim.HAnimHumanoid'),
HAnimJoint : java.import('org.web3d.x3d.jsail.HAnim.HAnimJoint'),
HAnimMotion : java.import('org.web3d.x3d.jsail.HAnim.HAnimMotion'),
HAnimSegment : java.import('org.web3d.x3d.jsail.HAnim.HAnimSegment'),
HAnimSite : java.import('org.web3d.x3d.jsail.HAnim.HAnimSite'),
ImageCubeMapTexture : java.import('org.web3d.x3d.jsail.CubeMapTexturing.ImageCubeMapTexture'),
ImageTexture : java.import('org.web3d.x3d.jsail.Texturing.ImageTexture'),
ImageTexture3D : java.import('org.web3d.x3d.jsail.Texturing3D.ImageTexture3D'),
IndexedFaceSet : java.import('org.web3d.x3d.jsail.Geometry3D.IndexedFaceSet'),
IndexedLineSet : java.import('org.web3d.x3d.jsail.Rendering.IndexedLineSet'),
IndexedQuadSet : java.import('org.web3d.x3d.jsail.CADGeometry.IndexedQuadSet'),
IndexedTriangleFanSet : java.import('org.web3d.x3d.jsail.Rendering.IndexedTriangleFanSet'),
IndexedTriangleSet : java.import('org.web3d.x3d.jsail.Rendering.IndexedTriangleSet'),
IndexedTriangleStripSet : java.import('org.web3d.x3d.jsail.Rendering.IndexedTriangleStripSet'),
Inline : java.import('org.web3d.x3d.jsail.Networking.Inline'),
IntegerSequencer : java.import('org.web3d.x3d.jsail.EventUtilities.IntegerSequencer'),
IntegerTrigger : java.import('org.web3d.x3d.jsail.EventUtilities.IntegerTrigger'),
IsoSurfaceVolumeData : java.import('org.web3d.x3d.jsail.VolumeRendering.IsoSurfaceVolumeData'),
KeySensor : java.import('org.web3d.x3d.jsail.KeyDeviceSensor.KeySensor'),
Layer : java.import('org.web3d.x3d.jsail.Layering.Layer'),
LayerSet : java.import('org.web3d.x3d.jsail.Layering.LayerSet'),
Layout : java.import('org.web3d.x3d.jsail.Layout.Layout'),
LayoutGroup : java.import('org.web3d.x3d.jsail.Layout.LayoutGroup'),
LayoutLayer : java.import('org.web3d.x3d.jsail.Layout.LayoutLayer'),
LinePickSensor : java.import('org.web3d.x3d.jsail.Picking.LinePickSensor'),
LineProperties : java.import('org.web3d.x3d.jsail.Shape.LineProperties'),
LineSet : java.import('org.web3d.x3d.jsail.Rendering.LineSet'),
LoadSensor : java.import('org.web3d.x3d.jsail.Networking.LoadSensor'),
LocalFog : java.import('org.web3d.x3d.jsail.EnvironmentalEffects.LocalFog'),
LOD : java.import('org.web3d.x3d.jsail.Navigation.LOD'),
Material : java.import('org.web3d.x3d.jsail.Shape.Material'),
Matrix3VertexAttribute : java.import('org.web3d.x3d.jsail.Shaders.Matrix3VertexAttribute'),
Matrix4VertexAttribute : java.import('org.web3d.x3d.jsail.Shaders.Matrix4VertexAttribute'),
MetadataBoolean : java.import('org.web3d.x3d.jsail.Core.MetadataBoolean'),
MetadataDouble : java.import('org.web3d.x3d.jsail.Core.MetadataDouble'),
MetadataFloat : java.import('org.web3d.x3d.jsail.Core.MetadataFloat'),
MetadataInteger : java.import('org.web3d.x3d.jsail.Core.MetadataInteger'),
MetadataSet : java.import('org.web3d.x3d.jsail.Core.MetadataSet'),
MetadataString : java.import('org.web3d.x3d.jsail.Core.MetadataString'),
MotorJoint : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.MotorJoint'),
MovieTexture : java.import('org.web3d.x3d.jsail.Texturing.MovieTexture'),
MultiTexture : java.import('org.web3d.x3d.jsail.Texturing.MultiTexture'),
MultiTextureCoordinate : java.import('org.web3d.x3d.jsail.Texturing.MultiTextureCoordinate'),
MultiTextureTransform : java.import('org.web3d.x3d.jsail.Texturing.MultiTextureTransform'),
NavigationInfo : java.import('org.web3d.x3d.jsail.Navigation.NavigationInfo'),
Normal : java.import('org.web3d.x3d.jsail.Rendering.Normal'),
NormalInterpolator : java.import('org.web3d.x3d.jsail.Interpolation.NormalInterpolator'),
NurbsCurve : java.import('org.web3d.x3d.jsail.NURBS.NurbsCurve'),
NurbsCurve2D : java.import('org.web3d.x3d.jsail.NURBS.NurbsCurve2D'),
NurbsOrientationInterpolator : java.import('org.web3d.x3d.jsail.NURBS.NurbsOrientationInterpolator'),
NurbsPatchSurface : java.import('org.web3d.x3d.jsail.NURBS.NurbsPatchSurface'),
NurbsPositionInterpolator : java.import('org.web3d.x3d.jsail.NURBS.NurbsPositionInterpolator'),
NurbsSet : java.import('org.web3d.x3d.jsail.NURBS.NurbsSet'),
NurbsSurfaceInterpolator : java.import('org.web3d.x3d.jsail.NURBS.NurbsSurfaceInterpolator'),
NurbsSweptSurface : java.import('org.web3d.x3d.jsail.NURBS.NurbsSweptSurface'),
NurbsSwungSurface : java.import('org.web3d.x3d.jsail.NURBS.NurbsSwungSurface'),
NurbsTextureCoordinate : java.import('org.web3d.x3d.jsail.NURBS.NurbsTextureCoordinate'),
NurbsTrimmedSurface : java.import('org.web3d.x3d.jsail.NURBS.NurbsTrimmedSurface'),
OpacityMapVolumeStyle : java.import('org.web3d.x3d.jsail.VolumeRendering.OpacityMapVolumeStyle'),
OrientationChaser : java.import('org.web3d.x3d.jsail.Followers.OrientationChaser'),
OrientationDamper : java.import('org.web3d.x3d.jsail.Followers.OrientationDamper'),
OrientationInterpolator : java.import('org.web3d.x3d.jsail.Interpolation.OrientationInterpolator'),
OrthoViewpoint : java.import('org.web3d.x3d.jsail.Navigation.OrthoViewpoint'),
PackagedShader : java.import('org.web3d.x3d.jsail.Shaders.PackagedShader'),
ParticleSystem : java.import('org.web3d.x3d.jsail.ParticleSystems.ParticleSystem'),
PickableGroup : java.import('org.web3d.x3d.jsail.Picking.PickableGroup'),
PixelTexture : java.import('org.web3d.x3d.jsail.Texturing.PixelTexture'),
PixelTexture3D : java.import('org.web3d.x3d.jsail.Texturing3D.PixelTexture3D'),
PlaneSensor : java.import('org.web3d.x3d.jsail.PointingDeviceSensor.PlaneSensor'),
PointEmitter : java.import('org.web3d.x3d.jsail.ParticleSystems.PointEmitter'),
PointLight : java.import('org.web3d.x3d.jsail.Lighting.PointLight'),
PointPickSensor : java.import('org.web3d.x3d.jsail.Picking.PointPickSensor'),
PointProperties : java.import('org.web3d.x3d.jsail.Shape.PointProperties'),
PointSet : java.import('org.web3d.x3d.jsail.Rendering.PointSet'),
Polyline2D : java.import('org.web3d.x3d.jsail.Geometry2D.Polyline2D'),
PolylineEmitter : java.import('org.web3d.x3d.jsail.ParticleSystems.PolylineEmitter'),
Polypoint2D : java.import('org.web3d.x3d.jsail.Geometry2D.Polypoint2D'),
PositionChaser : java.import('org.web3d.x3d.jsail.Followers.PositionChaser'),
PositionChaser2D : java.import('org.web3d.x3d.jsail.Followers.PositionChaser2D'),
PositionDamper : java.import('org.web3d.x3d.jsail.Followers.PositionDamper'),
PositionDamper2D : java.import('org.web3d.x3d.jsail.Followers.PositionDamper2D'),
PositionInterpolator : java.import('org.web3d.x3d.jsail.Interpolation.PositionInterpolator'),
PositionInterpolator2D : java.import('org.web3d.x3d.jsail.Interpolation.PositionInterpolator2D'),
PrimitivePickSensor : java.import('org.web3d.x3d.jsail.Picking.PrimitivePickSensor'),
ProgramShader : java.import('org.web3d.x3d.jsail.Shaders.ProgramShader'),
ProjectionVolumeStyle : java.import('org.web3d.x3d.jsail.VolumeRendering.ProjectionVolumeStyle'),
ProtoInstance : java.import('org.web3d.x3d.jsail.Core.ProtoInstance'),
ProximitySensor : java.import('org.web3d.x3d.jsail.EnvironmentalSensor.ProximitySensor'),
QuadSet : java.import('org.web3d.x3d.jsail.CADGeometry.QuadSet'),
ReceiverPdu : java.import('org.web3d.x3d.jsail.DIS.ReceiverPdu'),
Rectangle2D : java.import('org.web3d.x3d.jsail.Geometry2D.Rectangle2D'),
RigidBody : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.RigidBody'),
RigidBodyCollection : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.RigidBodyCollection'),
ScalarChaser : java.import('org.web3d.x3d.jsail.Followers.ScalarChaser'),
ScalarDamper : java.import('org.web3d.x3d.jsail.Followers.ScalarDamper'),
ScalarInterpolator : java.import('org.web3d.x3d.jsail.Interpolation.ScalarInterpolator'),
ScreenFontStyle : java.import('org.web3d.x3d.jsail.Layout.ScreenFontStyle'),
ScreenGroup : java.import('org.web3d.x3d.jsail.Layout.ScreenGroup'),
Script : java.import('org.web3d.x3d.jsail.Scripting.Script'),
SegmentedVolumeData : java.import('org.web3d.x3d.jsail.VolumeRendering.SegmentedVolumeData'),
ShadedVolumeStyle : java.import('org.web3d.x3d.jsail.VolumeRendering.ShadedVolumeStyle'),
ShaderPart : java.import('org.web3d.x3d.jsail.Shaders.ShaderPart'),
ShaderProgram : java.import('org.web3d.x3d.jsail.Shaders.ShaderProgram'),
Shape : java.import('org.web3d.x3d.jsail.Shape.Shape'),
SignalPdu : java.import('org.web3d.x3d.jsail.DIS.SignalPdu'),
SilhouetteEnhancementVolumeStyle : java.import('org.web3d.x3d.jsail.VolumeRendering.SilhouetteEnhancementVolumeStyle'),
SingleAxisHingeJoint : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.SingleAxisHingeJoint'),
SliderJoint : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.SliderJoint'),
Sound : java.import('org.web3d.x3d.jsail.Sound.Sound'),
Sphere : java.import('org.web3d.x3d.jsail.Geometry3D.Sphere'),
SphereSensor : java.import('org.web3d.x3d.jsail.PointingDeviceSensor.SphereSensor'),
SplinePositionInterpolator : java.import('org.web3d.x3d.jsail.Interpolation.SplinePositionInterpolator'),
SplinePositionInterpolator2D : java.import('org.web3d.x3d.jsail.Interpolation.SplinePositionInterpolator2D'),
SplineScalarInterpolator : java.import('org.web3d.x3d.jsail.Interpolation.SplineScalarInterpolator'),
SpotLight : java.import('org.web3d.x3d.jsail.Lighting.SpotLight'),
SquadOrientationInterpolator : java.import('org.web3d.x3d.jsail.Interpolation.SquadOrientationInterpolator'),
StaticGroup : java.import('org.web3d.x3d.jsail.Grouping.StaticGroup'),
StringSensor : java.import('org.web3d.x3d.jsail.KeyDeviceSensor.StringSensor'),
SurfaceEmitter : java.import('org.web3d.x3d.jsail.ParticleSystems.SurfaceEmitter'),
Switch : java.import('org.web3d.x3d.jsail.Grouping.Switch'),
TexCoordChaser2D : java.import('org.web3d.x3d.jsail.Followers.TexCoordChaser2D'),
TexCoordDamper2D : java.import('org.web3d.x3d.jsail.Followers.TexCoordDamper2D'),
Text : java.import('org.web3d.x3d.jsail.Text.Text'),
TextureBackground : java.import('org.web3d.x3d.jsail.EnvironmentalEffects.TextureBackground'),
TextureCoordinate : java.import('org.web3d.x3d.jsail.Texturing.TextureCoordinate'),
TextureCoordinate3D : java.import('org.web3d.x3d.jsail.Texturing3D.TextureCoordinate3D'),
TextureCoordinate4D : java.import('org.web3d.x3d.jsail.Texturing3D.TextureCoordinate4D'),
TextureCoordinateGenerator : java.import('org.web3d.x3d.jsail.Texturing.TextureCoordinateGenerator'),
TextureProperties : java.import('org.web3d.x3d.jsail.Texturing.TextureProperties'),
TextureTransform : java.import('org.web3d.x3d.jsail.Texturing.TextureTransform'),
TextureTransform3D : java.import('org.web3d.x3d.jsail.Texturing3D.TextureTransform3D'),
TextureTransformMatrix3D : java.import('org.web3d.x3d.jsail.Texturing3D.TextureTransformMatrix3D'),
TimeSensor : java.import('org.web3d.x3d.jsail.Time.TimeSensor'),
TimeTrigger : java.import('org.web3d.x3d.jsail.EventUtilities.TimeTrigger'),
ToneMappedVolumeStyle : java.import('org.web3d.x3d.jsail.VolumeRendering.ToneMappedVolumeStyle'),
TouchSensor : java.import('org.web3d.x3d.jsail.PointingDeviceSensor.TouchSensor'),
Transform : java.import('org.web3d.x3d.jsail.Grouping.Transform'),
TransformSensor : java.import('org.web3d.x3d.jsail.EnvironmentalSensor.TransformSensor'),
TransmitterPdu : java.import('org.web3d.x3d.jsail.DIS.TransmitterPdu'),
TriangleFanSet : java.import('org.web3d.x3d.jsail.Rendering.TriangleFanSet'),
TriangleSet : java.import('org.web3d.x3d.jsail.Rendering.TriangleSet'),
TriangleSet2D : java.import('org.web3d.x3d.jsail.Geometry2D.TriangleSet2D'),
TriangleStripSet : java.import('org.web3d.x3d.jsail.Rendering.TriangleStripSet'),
TwoSidedMaterial : java.import('org.web3d.x3d.jsail.Shape.TwoSidedMaterial'),
UniversalJoint : java.import('org.web3d.x3d.jsail.RigidBodyPhysics.UniversalJoint'),
Viewpoint : java.import('org.web3d.x3d.jsail.Navigation.Viewpoint'),
ViewpointGroup : java.import('org.web3d.x3d.jsail.Navigation.ViewpointGroup'),
Viewport : java.import('org.web3d.x3d.jsail.Layering.Viewport'),
VisibilitySensor : java.import('org.web3d.x3d.jsail.EnvironmentalSensor.VisibilitySensor'),
VolumeData : java.import('org.web3d.x3d.jsail.VolumeRendering.VolumeData'),
VolumeEmitter : java.import('org.web3d.x3d.jsail.ParticleSystems.VolumeEmitter'),
VolumePickSensor : java.import('org.web3d.x3d.jsail.Picking.VolumePickSensor'),
WindPhysicsModel : java.import('org.web3d.x3d.jsail.ParticleSystems.WindPhysicsModel'),
WorldInfo : java.import('org.web3d.x3d.jsail.Core.WorldInfo'),
component : java.import('org.web3d.x3d.jsail.Core.component'),
connect : java.import('org.web3d.x3d.jsail.Core.connect'),
EXPORT : java.import('org.web3d.x3d.jsail.Networking.EXPORT'),
ExternProtoDeclare : java.import('org.web3d.x3d.jsail.Core.ExternProtoDeclare'),
field : java.import('org.web3d.x3d.jsail.Core.field'),
fieldValue : java.import('org.web3d.x3d.jsail.Core.fieldValue'),
head : java.import('org.web3d.x3d.jsail.Core.head'),
IMPORT : java.import('org.web3d.x3d.jsail.Networking.IMPORT'),
IS : java.import('org.web3d.x3d.jsail.Core.IS'),
meta : java.import('org.web3d.x3d.jsail.Core.meta'),
ProtoBody : java.import('org.web3d.x3d.jsail.Core.ProtoBody'),
ProtoDeclare : java.import('org.web3d.x3d.jsail.Core.ProtoDeclare'),
ProtoInterface : java.import('org.web3d.x3d.jsail.Core.ProtoInterface'),
ROUTE : java.import('org.web3d.x3d.jsail.Core.ROUTE'),
Scene : java.import('org.web3d.x3d.jsail.Core.Scene'),
unit : java.import('org.web3d.x3d.jsail.Core.unit'),
X3D : java.import('org.web3d.x3d.jsail.Core.X3D'),
SFBool : java.import('org.web3d.x3d.jsail.fields.SFBool'),
MFBool : java.import('org.web3d.x3d.jsail.fields.MFBool'),
SFColor : java.import('org.web3d.x3d.jsail.fields.SFColor'),
MFColor : java.import('org.web3d.x3d.jsail.fields.MFColor'),
SFColorRGBA : java.import('org.web3d.x3d.jsail.fields.SFColorRGBA'),
MFColorRGBA : java.import('org.web3d.x3d.jsail.fields.MFColorRGBA'),
SFDouble : java.import('org.web3d.x3d.jsail.fields.SFDouble'),
MFDouble : java.import('org.web3d.x3d.jsail.fields.MFDouble'),
SFFloat : java.import('org.web3d.x3d.jsail.fields.SFFloat'),
MFFloat : java.import('org.web3d.x3d.jsail.fields.MFFloat'),
SFImage : java.import('org.web3d.x3d.jsail.fields.SFImage'),
MFImage : java.import('org.web3d.x3d.jsail.fields.MFImage'),
SFInt32 : java.import('org.web3d.x3d.jsail.fields.SFInt32'),
MFInt32 : java.import('org.web3d.x3d.jsail.fields.MFInt32'),
SFMatrix3d : java.import('org.web3d.x3d.jsail.fields.SFMatrix3d'),
MFMatrix3d : java.import('org.web3d.x3d.jsail.fields.MFMatrix3d'),
SFMatrix3f : java.import('org.web3d.x3d.jsail.fields.SFMatrix3f'),
MFMatrix3f : java.import('org.web3d.x3d.jsail.fields.MFMatrix3f'),
SFMatrix4d : java.import('org.web3d.x3d.jsail.fields.SFMatrix4d'),
MFMatrix4d : java.import('org.web3d.x3d.jsail.fields.MFMatrix4d'),
SFMatrix4f : java.import('org.web3d.x3d.jsail.fields.SFMatrix4f'),
MFMatrix4f : java.import('org.web3d.x3d.jsail.fields.MFMatrix4f'),
SFString : java.import('org.web3d.x3d.jsail.fields.SFString'),
SFNode : java.import('org.web3d.x3d.jsail.fields.SFNode'),
MFNode : java.import('org.web3d.x3d.jsail.fields.MFNode'),
SFRotation : java.import('org.web3d.x3d.jsail.fields.SFRotation'),
MFRotation : java.import('org.web3d.x3d.jsail.fields.MFRotation'),
MFString : java.import('org.web3d.x3d.jsail.fields.MFString'),
SFTime : java.import('org.web3d.x3d.jsail.fields.SFTime'),
MFTime : java.import('org.web3d.x3d.jsail.fields.MFTime'),
SFVec2d : java.import('org.web3d.x3d.jsail.fields.SFVec2d'),
MFVec2d : java.import('org.web3d.x3d.jsail.fields.MFVec2d'),
SFVec2f : java.import('org.web3d.x3d.jsail.fields.SFVec2f'),
MFVec2f : java.import('org.web3d.x3d.jsail.fields.MFVec2f'),
SFVec3d : java.import('org.web3d.x3d.jsail.fields.SFVec3d'),
MFVec3d : java.import('org.web3d.x3d.jsail.fields.MFVec3d'),
SFVec3f : java.import('org.web3d.x3d.jsail.fields.SFVec3f'),
MFVec3f : java.import('org.web3d.x3d.jsail.fields.MFVec3f'),
SFVec4d : java.import('org.web3d.x3d.jsail.fields.SFVec4d'),
MFVec4d : java.import('org.web3d.x3d.jsail.fields.MFVec4d'),
SFVec4f : java.import('org.web3d.x3d.jsail.fields.SFVec4f'),
MFVec4f : java.import('org.web3d.x3d.jsail.fields.MFVec4f'),
ConfigurationProperties : java.import("org.web3d.x3d.jsail.ConfigurationProperties"),
CommentsBlock : java.import("org.web3d.x3d.jsail.Core.CommentsBlock")
}