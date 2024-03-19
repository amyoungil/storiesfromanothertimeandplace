import bpy
import mathutils

# publish: true

# Set the frame range for the animation
start_frame = 1
end_frame = 50

# Get the point light (destination point) and the cube by name
point_light = bpy.data.objects.get("DestinationPoint")
cube = bpy.data.objects.get("Cube.001")

if point_light and cube:
    # Get the destination as a mathutils.Vector() of the destination's global position
    destination = mathutils.Vector((point_light.location))
    
    # Calculate the vector from the cube's starting position to the destination
    total_distance_vector = destination - cube.location
    
    # Calculate the distance to move each frame
    move_per_frame = total_distance_vector / (end_frame - start_frame)
    
    # Record the cube's original location to use as a base for each frame's movement
    original_location = cube.location.copy()

    for frame in range(start_frame, end_frame + 1):
        bpy.context.scene.frame_set(frame)
        
        # Calculate the new location based on the original location and the movement per frame
        cube.location = original_location + (move_per_frame * (frame - start_frame))
        
        cube.keyframe_insert(data_path="location", index=-1)

    print(f"Animation created for {cube.name} from frame {start_frame} to {end_frame}.")
else:
    print(f"One or more objects not found in the scene.")
