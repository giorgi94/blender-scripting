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

# Access the vertex you want to animate
vertex_index_to_animate = (
    1  # Change this to the index of the vertex you want to animate
)
vertex = plane.data.vertices[vertex_index_to_animate]


vertex.keyframe_insert(data_path="co", frame=1, index=0)
vertex.keyframe_insert(data_path="co", frame=1, index=1)
vertex.keyframe_insert(data_path="co", frame=1, index=2)

frame_number = 50

# Set the z-coordinate at frame 100 (ending point)
bpy.context.scene.frame_set(frame_number)
vertex.co.z = 1
vertex.keyframe_insert(data_path="co", frame=frame_number, index=2)


frame_number = 100
bpy.context.scene.frame_set(frame_number)
vertex.co.x = 7
vertex.keyframe_insert(data_path="co", frame=frame_number, index=0)
