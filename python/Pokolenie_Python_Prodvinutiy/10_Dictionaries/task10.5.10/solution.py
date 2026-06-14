def is_subfolder(folder_dict, subfolder, folder):
    if folder not in folder_dict:
        return False
    
    queue = [folder]
    
    while queue:
        current = queue.pop(0)
        
        children = folder_dict.get(current, [])
        
        if subfolder in children:
            return True
        
        queue.extend(children)
    
    return False