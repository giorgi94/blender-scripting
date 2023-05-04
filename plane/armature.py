import bpy


def one_bone():

    # create a new armature object
    armature_obj = bpy.data.objects.new("Armature", bpy.data.armatures.new("Armature"))

    # add the armature object to the scene
    bpy.context.scene.collection.objects.link(armature_obj)

    # select the armature object and enter edit mode
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode="EDIT")

    # create a new bone in the armature data block
    new_bone = armature_obj.data.edit_bones.new("Bone")

    # set the head and tail positions of the new bone
    new_bone.head = (0, 0, 0)
    new_bone.tail = (0, 1, 0)

    # exit edit mode and deselect the armature object
    bpy.ops.object.mode_set(mode="OBJECT")
    armature_obj.select_set(False)


def two_bone():
    # create a new armature object
    armature_obj = bpy.data.objects.new("Armature", bpy.data.armatures.new("Armature"))

    # add the armature object to the scene
    bpy.context.scene.collection.objects.link(armature_obj)

    # select the armature object and enter edit mode
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode="EDIT")

    # create the first bone in the armature data block
    bone1 = armature_obj.data.edit_bones.new("Bone1")
    bone1.head = (0, 0, 0)
    bone1.tail = (0, 1, 0)

    # create the second bone in the armature data block
    bone2 = armature_obj.data.edit_bones.new("Bone2")
    bone2.head = (0, 1, 0)
    bone2.tail = (0, 2, 0)

    # connect the second bone to the tail of the first bone
    bone2.parent = bone1

    # exit edit mode and deselect the armature object
    bpy.ops.object.mode_set(mode="OBJECT")
    armature_obj.select_set(False)
