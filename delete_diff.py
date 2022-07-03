import os
import hashlib

def get_file_hash(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

# delete all files in path_b that are identical to files in path_a
def delete_diff(path_a, path_b):
    file_count = 0
    for file_a in os.listdir(path_a):
        file_b = os.path.join(path_b, file_a)
        if os.path.isfile(file_b):
            # Hash the files
            hash_a = get_file_hash(os.path.join(path_a, file_a))
            hash_b = get_file_hash(file_b)
            if hash_a == hash_b:
                os.remove(file_b)
            else:
                file_count += 1
                print("File {} is different".format(file_b))
        else:
            try:
                delete_diff(os.path.join(path_a, file_a), file_b)
            except:
                pass
    
    if file_count == 0:
        try:
            os.rmdir(path_b)
        except:
            pass

delete_diff("E:\\User\\Downloads\\New folder (2)\\Ace Asin - Bloodborne SDK3A (Private 2.21.0)\\Assets\\VRCSDK", "E:\\User\\Downloads\\New folder (2)\\Ace Asin - Bloodborne SDK3W (Private 2.21.0)\\Assets\\VRCSDK")