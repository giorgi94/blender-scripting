import bpy

# create a new armature object
armature_obj = bpy.data.objects.new("Armature", bpy.data.armatures.new("Armature"))

# add the armature object to the scene
bpy.context.scene.collection.objects.link(armature_obj)

# select the armature object and enter edit mode
bpy.context.view_layer.objects.active = armature_obj
bpy.ops.object.mode_set(mode='EDIT')

# create a new bone in the armature data block
new_bone = armature_obj.data.edit_bones.new("Bone")

# set the head and tail positions of the new bone
new_bone.head = (0, 0, 0)
new_bone.tail = (0, 1, 0)

# exit edit mode and deselect the armature object
bpy.ops.object.mode_set(mode='OBJECT')
armature_obj.select_set(False)
