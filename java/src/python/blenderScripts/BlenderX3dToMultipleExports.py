# X3DJSAIL directory src/python/blenderScripts

scriptName  = "BlenderX3dToMultipleExports.py"

description = scriptName + " is a Blender Python script to load model.x3d and export multiple output files"

# meta reference: BlenderX3dToMultipleExports.py by Mike Bailey NPS, adapted from original NIH 3D Print Exchange scripts

import os, sys, getopt

def usage():
    print ("")
    print (description)
    print ("""Usage:   blender --background --factory-startup --python""", scriptName, """-- <model>.x3d [<outputpath>]""")
    print ("""Output:   [<outputpath>]<model>.png etc.""")
    print ("""Manual:  https://docs.blender.org/manual/en/latest/render/workflows/command_line.html""")
    print ("""         https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html#python-options""")
    print ("""Warning: cygwin unix on windows fails command-line invocation, use native operating system shell instead""")
    print ("")

# Example: blender --background --factory-startup --python BlenderX3dToMultipleExports.py -- LPD17.meshlab.x3d

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
if len(args) == 1:
    sourceFile = args[0]
    outputPath = os.getcwd() # current directory
elif len(args) == 2:
    sourceFile = args[0]
    outputPath = args[1]
else:
    print("\nError: You must specify a single .x3d input file with an optional output path") #  (with trailing slash)
    print(str(len(args)), " arguments provided " + str(args));
    usage()
    sys.exit(2)

input_name, ext  = os.path.splitext(sourceFile)
PLY_file   = os.path.join(outputPath, input_name + ".blender.ply")
STL_file   = os.path.join(outputPath, input_name + ".blender.stl")
PNG_file   = os.path.join(outputPath, input_name + ".blender.png")
X3D_file   = os.path.join(outputPath, input_name + ".blender.x3d")
BLEND_file = os.path.join(outputPath, input_name + ".blend")

PNG_file_mono   = os.path.join(outputPath, input_name + ".blender_mono.png")
X3D_file_mono   = os.path.join(outputPath, input_name + ".blender_mono.x3d")
BLEND_file_mono = os.path.join(outputPath, input_name + "_mono.blend")

print("outputPath=", outputPath) # debug

os.chdir(".")
 
# CLEAN UP INITIAL VIEW
bpy.ops.object.select_by_type(extend=False, type='MESH')
bpy.ops.object.delete(use_global=False)
bpy.ops.object.select_by_type(extend=False, type='LAMP')
bpy.ops.object.delete(use_global=False)

# IMPORT THE MESH
print("Importing", sourceFile, "...")
bpy.ops.import_scene.x3d(filepath = sourceFile)

# DELETE THE OTHER IMPORTED OBJECTS
print("Deleting imported lamps, curves, cameras...")
bpy.ops.object.select_by_type(extend=False, type='LAMP')
bpy.ops.object.delete(use_global=False)
bpy.ops.object.select_by_type(extend=False, type='CURVE')
bpy.ops.object.delete(use_global=False)
bpy.ops.object.select_by_type(extend=False, type='CAMERA')
bpy.ops.object.delete(use_global=False)

# Check to see if each mesh has "Col" vertex group;
# if so, then turn on vertex color
print("Determining if per-vertex coloring is needed...")
bpy.ops.object.select_by_type(extend=False, type='MESH')
for mesh_object in bpy.context.selected_objects:
    bpy.context.scene.objects.active = mesh_object
    if len(mesh_object.data.vertex_colors.values()) > 0:
        print(str(mesh_object) + " has vertex colors")
        if len(mesh_object.data.materials.values()) == 0:
            print(str(mesh_object) + " has no material; adding material and turning on vertex coloring")
            mesh_object.data.materials.append(bpy.data.materials.new(mesh_object.name))
            bpy.data.materials[mesh_object.name].use_vertex_color_paint = True
#        else:
#            print(str(mesh_object) + " has material(s); turning off vertex coloring")
#            for mesh_object_material in mesh_object.data.materials.values():
#                bpy.data.materials[mesh_object_material.name].use_vertex_color_paint = False
#                print(str(mesh_object) + " has material " + str(mesh_object_material) + " ; turning off vertex coloring")
    else:
        for mesh_object_material in mesh_object.data.materials.values():
            bpy.data.materials[mesh_object_material.name].use_vertex_color_paint = False
#            print(str(mesh_object) + " has material " + str(mesh_object_material) + " ; turning off vertex coloring")

# CAMERA
print("Setting camera...")
cam = bpy.data.cameras.new("TheCamera")
cam.clip_end = 1000000
bpycam = bpy.data.objects.new("TheCamera", cam)
bpy.context.scene.camera = bpycam 
bpy.ops.object.select_by_type(extend=False, type='MESH')
bpy.ops.view3d.camera_to_view_selected()
  
# SET SCENE
print("Setting background color...")
bpy.data.worlds['World'].horizon_color[0]=1
bpy.data.worlds['World'].horizon_color[1]=1
bpy.data.worlds['World'].horizon_color[2]=1
bpy.data.worlds['World'].light_settings.use_ambient_occlusion = True
bpy.data.worlds['World'].light_settings.gather_method = 'APPROXIMATE'

# SAVE PNG
print("Rendering image... " + PNG_file)
bpy.data.scenes['Scene'].render.resolution_x = 500
bpy.data.scenes['Scene'].render.resolution_y = 500
bpy.data.scenes['Scene'].render.resolution_percentage = 100
bpy.data.scenes['Scene'].render.filepath = PNG_file
bpy.ops.render.render(write_still=True)

# EXPORT X3D
print("Exporting " + X3D_file +"\n")
bpy.ops.export_scene.x3d(filepath = X3D_file)

# SAVE .BLEND
print("Saving .blend file", BLEND_file, "...")
bpy.ops.wm.save_as_mainfile(filepath = BLEND_file, check_existing = False)

# ------------------------------------
# NOW WE NEED TO MAKE AN STL OUT OF IT
# ------------------------------------

# RECOLOR TO NIH BLUE
mat = bpy.data.materials.new("NIH_blue")
mat.diffuse_color = (0.20,0.38,0.60)
mat.diffuse_shader = 'LAMBERT' 
mat.diffuse_intensity = 1.0 
mat.specular_color = (1,1,1)
mat.specular_shader = 'COOKTORR'
mat.specular_intensity = 0.5
mat.alpha = 1
mat.ambient = 1
for o in bpy.context.scene.objects:
    if o.type == 'MESH':
        o.data.materials.clear()
        o.data.materials.append(mat)
        
# EXPORT STL
print("Export STL", STL_file, "...")
bpy.ops.export_mesh.stl(filepath = STL_file)

# SAVE MONOCHROME PNG
print("Rendering monochrome", PNG_file_mono, "...")
bpy.data.scenes['Scene'].render.filepath = PNG_file_mono
bpy.ops.render.render(write_still=True)

# SAVE OUT X3D
print("Exporting cleaned monochrome", X3D_file_mono, "...")
bpy.ops.export_scene.x3d(filepath = X3D_file_mono)

# SAVE .BLEND
print("Saving monochrome .blend file", BLEND_file_mono, "...")
bpy.ops.wm.save_as_mainfile(filepath = BLEND_file_mono, check_existing = False)

# QUIT
# print("Quitting Blender") # debug
bpy.ops.wm.quit_blender()
sys.exit(0)
