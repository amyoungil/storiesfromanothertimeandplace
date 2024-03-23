import bpy
import mathutils

# publish: true
# Assuming the cube and the destination point are objects in your scene
cube_name = "Cube.001"
destination_point_name = "DestinationPoint"

# Get the cube and destination point objects
cube = bpy.data.objects.get(cube_name)
destination_point = bpy.data.objects.get(destination_point_name).location

# Placeholder for the closest vertex information
closest_vertex = None
min_distance = float('inf')  # Initialize with infinity

# Ensure the cube object exists and has mesh data
if cube and cube.type == 'MESH':
    # Convert destination point to the cube's local space
    destination_local = cube.matrix_world.inverted() @ mathutils.Vector(destination_point)
    
    # Iterate through each vertex of the cube
    for vertex in cube.data.vertices:
        # Calculate the distance from the vertex to the destination point
        distance = (vertex.co - destination_local).length
        # Update the closest vertex and minimum distance if necessary
        if distance < min_distance:
            min_distance = distance
            closest_vertex = vertex

# Check if a closest vertex was found
if closest_vertex:
    print(f"Closest vertex index: {closest_vertex.index}, Distance: {min_distance}")
    
else:
    print("No closest vertex found.")
