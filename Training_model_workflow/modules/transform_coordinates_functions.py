def from_relative_coordonates_to_absolute(x_center, y_center, width, height, img_width, img_height):
    """
    The function will be used in the 'yolo_to_csv' function to transform the relative coordinates of the 
    YOLO bounding box detection into absolute coordinates.
    The absolute coordinates will be used to create the URL of the bounding boxes of the detected objects.
    
    The 'x_center' parameter is the relative x coordinate of the center of the bounding box.
    The 'y_center' parameter is the relative y coordinate of the center of the bounding box.
    The 'width' parameter is the relative width of the bounding box.
    The 'height' parameter is the relative height of the bounding box.
    The 'img_width' parameter is the width of the downloaded image.
    The'img_height' parameter is the height of the downloaded image.
    
    All the parameters will be automatically filled in 'yolo_to_csv function' by the results data from the YOLO .txt files.
    """
    
    abs_x_center = x_center * img_width
    abs_y_center = y_center * img_height
    abs_width = width * img_width
    abs_height = height * img_height

    upper_left_x = abs_x_center - (abs_width / 2)
    upper_left_y = abs_y_center - (abs_height / 2)

    absolute_coordinates = int(upper_left_x), int(upper_left_y), int(abs_width), int(abs_height)
    
    return absolute_coordinates


def from_ls_to_yolo(x, y, width, height):
    
    """
    This function converts annotation coordinates from Label Studio format to YOLO format (relative coordinates).
    
    Parameters: 
    
    The 'x_center' parameter is the  Label Studio format 'x' coordinate of the center of the bounding box.
    The 'y_center' parameter is the Label Studio format 'y' coordinate of the center of the bounding box.
    The 'width' parameter is the Label Studio format 'width' of the bounding box.
    The 'height' parameter is the Label Studio format 'height' of the bounding box.
    """
    yolo_width = width / 100
    yolo_height =  height / 100
    yolo_x = (x + width / 2) / 100
    yolo_y = (y + height / 2) / 100
    
    return str(yolo_x), str(yolo_y), str(yolo_width), str(yolo_height)