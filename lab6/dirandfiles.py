#ex1
import os

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_directories_and_files(path):
    directories = []
    files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            directories.append(item)
        elif os.path.isfile(item_path):
            files.append(item)
    return directories, files

path = "/path/to/your/directory"

print("Directories:")
print(list_directories(path))

print("\nFiles:")
print(list_files(path))

print("\nDirectories and Files:")
directories, files = list_directories_and_files(path)
print("Directories:")
print(directories)
print("Files:")
print(files)

#ex2
import os

def check_access(path):
    access_info = {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }
    return access_info

path = "/path/to/your/directory_or_file"

access_info = check_access(path)

print(f"Path: {path}")
print(f"Exists: {access_info['exists']}")
print(f"Readable: {access_info['readable']}")
print(f"Writable: {access_info['writable']}")
print(f"Executable: {access_info['executable']}")

#ex3
import os

def path_info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return True, filename, directory
    else:
        return False, None, None

path = "/path/to/your/file_or_directory"

exists, filename, directory = path_info(path)

if exists:
    print(f"Path exists")
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
else:
    print(f"Path does not exist")

#ex4
def count(file):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

file = "path/to/your/file.txt"

line_count = count(file)
print(line_count)

#ex5
def write_list_to_file(file, lst):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

file = "path/to/your/file.txt"

lst = [1, 2, 3, 4, 5]

write_list_to_file(file, lst)

print(file)

#ex6
import string

def generate():
    for letter in string.ascii_uppercase:
        file = f"{letter}.txt"
        with open(file, 'w') as file:
            file.write(f"This is file {file}\n")
        print(f"File {file} created.")

generate()

#ex7
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
        for line in source:
            destination.write(line)

source_file = "a.txt"
destination_file = "b.txt"

copy_file(source_file, destination_file)

print(f"Contents of {source_file} copied to {destination_file}")

#ex8
import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File {path} deleted successfully")
        else:
            print(f"Permission denied: {path}")
    else:
        print(f"File not found: {path}")

path = "path/to/your/file.txt"

delete_file(path)
