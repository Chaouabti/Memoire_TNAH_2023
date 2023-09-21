def get_labels(labels_file):
    '''
    This functions checks if the file 'labels.txt' exists. 
    If not, it generated a .txt file with the generic names for each existing class "class1" to "classN". 
    The users can then change the names later.
    Beware: if defined classes have not been used in the training dataset, they will not appear in this labels.txt file.
    '''
    labels_dict = {}
    with open(labels_file, 'r') as labels:
        for line in labels:
            key, value = line.strip().split(': ')
            key = key.strip("'")
            value = value.strip("',\n")
            labels_dict[key] = value
    
    return labels_dict


def get_class_name(class_id, labels):
    
    """
    This function returns the class name from the class ID. If the class key is not specified, the function returns "class unknown".
    The function will be used in the 'yolo_to_csv' function.
    
    The 'class_id' parameter is the ID of the class that will return the name of the class. will be automatically filled in 'yolo_to_csv function'.
    """
    labels = labels
    return labels.get(str(class_id), 'unknown-class')

def get_class_code(class_name, labels):
    
    """
    This function returns  the the ID (key number) from the class name. If the ID key is not specified,
    the function returns "class unknown".
    
    The 'class_id' parameter is  of the class name that will return the ID of the class.
    The parameter will be automatically filled in 'generate_corrected_files' with the results 
    data from Label Studio's corrected csv file.
    """

    labels = {str([value]): key for key, value in labels.items()}
    return labels.get(str(class_name), 'unknown-class')
