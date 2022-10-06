scriptName  = "BlenderStlToX3d.py"

description = scriptName + " is a Blender Python script to load model.stl and export model.x3d"

# meta reference: Blender_STL_to_X3D.py by Mike Bailey NPS, adapted from original NIH 3D Print Exchange scripts

import os, sys, getopt

def usage():
    print ("")
    print (description)
    print ("""Usage:   blender --background --factory-startup --python""", scriptName, """-- <model>.x3d [<outputpath>]""")
    print ("""Output:  <outputpath>/<model>.stl products/<filename>.ply""")
    print ("""Manual:  https://docs.blender.org/manual/en/latest/render/workflows/command_line.html""")
    print ("""         https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html#python-options""")
    print ("""Warning: cygwin unix on windows fails command-line invocation, use native operating system shell instead""")
    print ("")

# Example: blender --background --factory-startup --python BlenderStlToX3d.py -- LPD17.stl 

# default: --enable-autoexec

# Parse the command line arguments
print("Command line:", len(sys.argv), "args", sys.argv ) # debug

try:
    import bpy
except ImportError:
    print ("problem with import bpy for blender python")
    sys.exit(2)

try:
    opts, args = getopt.getopt(sys.argv[6:], "h", [ "help" ] )
except getopt.GetoptError as err:
    print (str(err))
    usage()
    sys.exit(2)

''' # multiline comment block
for o, a in opts:
    if o in ("-h", "--help"):
        usage()
        sys.exit()
    else:
        assert False, "unhandled options"
'''

# open the file
if len(args) == 0:
    usage()
    sys.exit()
elif len(args) == 1:
    sourceFile = args[0]
    outputPath = os.getcwd() # current directory
elif len(args) == 2:
    sourceFile = args[0]
    outputPath = args[1]
else:
    print("\nError: You must specify a single .x3d input file with an optional output path") #  (with trailing slash)
    usage()
    sys.exit(2)

input_name, ext  = os.path.splitext(sourceFile)
PLY_file   = os.path.join(outputPath, input_name + ".blender.ply")
PNG_file   = os.path.join(outputPath, input_name + ".blender.png")
STL_file   = os.path.join(outputPath, input_name + ".blender.stl")
X3D_file   = os.path.join(outputPath, input_name + ".blender.x3d")
BLEND_file = os.path.join(outputPath, input_name + ".blend")

print("outputPath=", outputPath) # debug

os.chdir(".")

def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT' 
    mat.diffuse_intensity = 1.0 
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha = alpha
    mat.ambient = 1
    return mat
 
def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)
 
cyan = makeMaterial('Cyan', (0,1,1), (1,1,1), 1)
NIH_blue1 = makeMaterial('NIH_blue1', (0.125,0.333,0.541), (1,1,1), 1)
NIH_blue2 = makeMaterial('NIH_blue2', (0.20,0.38,0.60), (1,1,1), 1)
Erin_blue = makeMaterial('Erin_blue', (0.42,0.64,0.72), (1,1,1), 1)
 
# CLEAN UP INITIAL VIEW
bpy.ops.object.select_by_type(extend=False, type='MESH')
bpy.ops.object.delete(use_global=False)
bpy.ops.object.select_by_type(extend=False, type='LAMP')
bpy.ops.object.delete(use_global=False)

# IMPORT THE MESH
print("Importing", sourceFile, "...")
bpy.ops.import_mesh.stl(filepath = sourceFile)

# REMOVE DOUBLED VERTICES AND ADJUST NORMALS
print("Deleting doubled vertices, adjust normals...")
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.remove_doubles()
#bpy.ops.mesh.normals_make_consistent()
bpy.ops.object.mode_set(mode='OBJECT')

# CENTER AND COLOR
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
bpy.ops.object.location_clear()
bpy.ops.object.visual_transform_apply()
setMaterial(bpy.context.object, NIH_blue2)
bpy.data.worlds['World'].horizon_color[0]=1
bpy.data.worlds['World'].horizon_color[1]=1
bpy.data.worlds['World'].horizon_color[2]=1
bpy.ops.view3d.camera_to_view_selected()
bpy.data.cameras['Camera'].clip_end = 1000000
bpy.data.worlds['World'].light_settings.use_ambient_occlusion = True
bpy.data.worlds['World'].light_settings.gather_method = 'APPROXIMATE'
bpy.data.scenes['Scene'].render.resolution_x = 500
bpy.data.scenes['Scene'].render.resolution_y = 500
bpy.data.scenes['Scene'].render.resolution_percentage = 100
bpy.data.scenes['Scene'].render.filepath = PNG_file
#bpy.ops.render.render(write_still=True)

# EXPORT DIFFERENT FORMATS
print("Export X3D...")
bpy.ops.export_scene.x3d(filepath = X3D_file)
print("Export PLY...")
bpy.ops.export_mesh.ply( filepath = PLY_file)

# SAVE .BLEND
# print("Saving .blend file")
# bpy.ops.wm.save_as_mainfile(filepath = input_name + ".blend", check_existing = False)

# QUIT
# print("Quitting Blender") # debug
bpy.ops.wm.quit_blender()
sys.exit(0)
