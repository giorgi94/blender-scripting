import bpy
from math import cos, sin, pi

# Create the mesh data
mesh_data = bpy.data.meshes.new("Pyramid")

# Create the vertices and faces for the mesh


def generate_pyramid(n):

    verts = [(0, 0, 2)]
    faces = [tuple(range(1, n + 1))]

    for i in range(1, n + 1):
        verts.append((cos(i * 2 * pi / n), sin(i * 2 * pi / n), 0))

    for i in range(0, n):
        faces.append((0, i, i + 1))

    faces.append((0, n, 1))

    return verts, faces


verts, faces = generate_pyramid(3)


# Set the mesh data
mesh_data.from_pydata(verts, [], faces)

# Create the object and add it to the scene
object_data = bpy.data.objects.new("Plane", mesh_data)
bpy.context.scene.collection.objects.link(object_data)
