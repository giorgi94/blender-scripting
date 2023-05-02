import bpy

# Create a mesh for the plane
mesh = bpy.data.meshes.new("Plane")

# Define the vertices and faces for a rectangle
vertices = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0)]
faces = [(0, 1, 2, 3)]

# Create the plane object and add it to the scene
plane = bpy.data.objects.new("Plane", mesh)
bpy.context.scene.collection.objects.link(plane)

# Set the mesh data
mesh.from_pydata(vertices, [], faces)
mesh.update()

# Get the first vertex of the plane
vertex = plane.data.vertices[0]

# Create a keyframe animation for the vertex
frame_start = 0
frame_end = 100
frame_interval = (frame_end - frame_start) / 5  # 5 seconds of animation
keyframe_values = [(frame_start, 0), (frame_end, 1)]

# Set up the keyframes for the Y coordinate of the vertex
keyframe_points = [(frame_start, vertex.co.z), (frame_end, vertex.co.z + 1)]
for i, (frame, value) in enumerate(keyframe_values):
    bpy.context.scene.frame_set(frame)
    vertex.co[2] = keyframe_points[i][1]
    vertex.keyframe_insert(data_path="co", index=1)
    vertex.keyframe_insert(data_path="co", index=2)
