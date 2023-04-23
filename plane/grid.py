import bpy
import bmesh
import math
import mathutils

# Set the size of the grid
n = 10

# Create the mesh data
mesh = bpy.data.meshes.new("Grid")
obj = bpy.data.objects.new("Grid", mesh)
bpy.context.scene.collection.objects.link(obj)

# Create a BMesh object and add a grid
bm = bmesh.new()
for i in range(n):
    for j in range(n):
        x = i - (n - 1) / 2
        y = j - (n - 1) / 2
        bm.verts.new((x, y, 0))

# Add faces to the grid
for i in range(n - 1):
    for j in range(n - 1):
        v1 = bm.verts[i * n + j]
        v2 = bm.verts[i * n + j + 1]
        v3 = bm.verts[(i + 1) * n + j + 1]
        v4 = bm.verts[(i + 1) * n + j]
        bm.faces.new((v1, v2, v3, v4))

# Transform the vertices using f(x,y,z) = (x,y,xy)
for v in bm.verts:
    v.co = mathutils.Vector((v.co[0], v.co[1], v.co[0] * v.co[1]))

# Update the mesh and scene
bm.to_mesh(mesh)
bm.free()
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
bpy.ops.object.editmode_toggle()
bpy.ops.object.editmode_toggle()
