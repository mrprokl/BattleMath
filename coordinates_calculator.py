import numpy as np
import cv2

def image_point_to_world_coordinates(image, current_position, image_point=None, camera_matrix=None, depth=1.0):
    """
    Convert a 2D image point to 3D world coordinates.
    
    Parameters:
    - image: Input image processed with cv2
    - current_position: Current camera/robot position [x, y, z]
    - image_point: Optional 2D point on the image. If None, a random point is generated.
    - camera_matrix: Camera intrinsic matrix. If None, a default matrix is used.
    - depth: Assumed depth of the point from the camera (default 1.0 meter)
    
    Returns:
    - world_coordinates: Predicted 3D world coordinates of the point
    """
    # Validate inputs
    if image is None:
        raise ValueError("Input image cannot be None")
    
    # Set default camera matrix if not provided
    if camera_matrix is None:
        camera_matrix = np.array([
            [528.6, 0, 320],    # fx, skew, cx
            [0, 528.6, 240],    # 0, fy, cy
            [0, 0, 1]           # 0, 0, 1
        ])
    
    # Generate random image point if not provided
    if image_point is None:
        height, width = image.shape[:2]
        image_point = np.array([
            np.random.uniform(0, width),
            np.random.uniform(0, height)
        ])
    
    # Ensure image point is a 2D homogeneous coordinate
    image_point_homogeneous = np.array([
        image_point[0],
        image_point[1],
        1
    ])
    
    # Compute inverse of camera matrix
    try:
        camera_matrix_inv = np.linalg.inv(camera_matrix)
    except np.linalg.LinAlgError:
        raise ValueError("Camera matrix is not invertible")
    
    # Convert image point to camera coordinates
    # Assuming a normalized depth of 1.0 meter
    camera_coords = camera_matrix_inv @ image_point_homogeneous * depth
    
    # Add the z-coordinate (depth)
    camera_coords = np.append(camera_coords, depth)
    
    # Transform camera coordinates to world coordinates
    # Assuming the current position represents the camera's position in world coordinates
    world_coordinates = np.array(current_position) + camera_coords[:3]
    
    return world_coordinates


def main():
    image = cv2.imread('THE_IMAGE.jpeg')
    current_position = [0, 0, 0]
    
    # Generate world coordinates for a random image point
    world_point = image_point_to_world_coordinates(image, current_position)
    
    print("Predicted World Coordinates:", world_point)

if __name__ == "__main__":
    main()