import bpy

# Clear existing mesh objects
bpy.ops.object.select_all(action="DESELECT")
bpy.ops.object.select_by_type(type="MESH")
bpy.ops.object.delete()

# Create a new cube mesh
bpy.ops.mesh.primitive_cube_add(
    size=1, enter_editmode=False, align="WORLD", location=(0, 0, 0)
)
cube = bpy.context.object

# Create an armature (skeleton)
bpy.ops.object.armature_add(enter_editmode=False, align="WORLD", location=(0, 0, 0))
armature = bpy.context.object

# Switch to pose mode for the armature
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode="POSE")
bone = armature.pose.bones[0]  # Access the first bone

# Parent the cube to the armature with automatic weights
bpy.context.view_layer.objects.active = cube
bpy.ops.object.mode_set(mode="OBJECT")
bpy.ops.object.select_all(action="DESELECT")
cube.select_set(True)
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode="POSE")
bpy.ops.pose.armature_apply()
bpy.ops.object.mode_set(mode="OBJECT")

# Link the cube to the bone
modifiers = cube.modifiers
if not bone.name in modifiers:
    mod = modifiers.new(name=bone.name, type="ARMATURE")
    mod.use_bone_envelopes = False
    mod.use_vertex_groups = True
    mod.object = armature

# Set up vertex groups
vertex_group = cube.vertex_groups.new(name=bone.name)
vertex_group.add([i for i in range(8)], 1.0, "ADD")

# Assign the vertices to the bone
bpy.context.view_layer.objects.active = cube
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.object.vertex_group_assign()

# Switch back to object mode
bpy.ops.object.mode_set(mode="OBJECT")
