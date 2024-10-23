import os

file_path = __file__

folder_path = os.path.dirname(file_path)

folder_name = os.path.basename(folder_path)

def Rename(old_name,new_name):
    try:
        os.rename(old_name, new_name)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

old_name = "start.txt"
new_name = "fin.txt"

# Output
print(f"\nFile path: {folder_path}")
print(f"Folder name: {folder_name}")
if Rename(old_name,new_name):
    print(f"File '{old_name}' was renamed to '{new_name}'")