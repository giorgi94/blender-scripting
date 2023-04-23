import bpy
import math


def f(x, y, z):
    return (x, y, (x**3 + y**2) * math.sin(x * y + y**3 + x**3))


# Number of vertices per row/column
n = 120

# Create the mesh data
mesh_data = bpy.data.meshes.new("Plane")

# Create the vertices and faces for the mesh
verts = []
faces = []

for i in range(n):
    for j in range(n):
        # Calculate the vertex position using the function
        x = (i / (n - 1)) * 2 - 1
        y = (j / (n - 1)) * 2 - 1
        z = f(x, y, 0)[2]

        # Add the vertex to the list
        verts.append((x, y, z))

        # Add the face to the list
        if i < n - 1 and j < n - 1:
            index = i * n + j
            faces.append((index, index + 1, index + n + 1, index + n))

# Set the mesh data
mesh_data.from_pydata(verts, [], faces)

# Create the object and add it to the scene
object_data = bpy.data.objects.new("Plane", mesh_data)
bpy.context.scene.collection.objects.link(object_data)
