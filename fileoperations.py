import os
new_dir_name = "classwork2"
os.makedirs(new_dir_name, exist_ok=True)
print(f"Directory '{new_dir_name}' created.")
cwd_contents = os.listdir(new_dir_name)
print("Current working directory contents:")
for item in cwd_contents:
    print(item)
file_name = "new.txt"
file_path = os.path.join(new_dir_name, file_name)
with open(file_path, "w") as file:
    file.write("i am doing classwork 2")
print(f"File '{file_name}' created in '{new_dir_name}' and content written.")
with open(file_path, "r") as file:
    content = file.read()
print("Content of the file:")
print(content)
new_file_name = "renamed.txt"
new_file_path = os.path.join(new_dir_name, new_file_name)
os.rename(file_path, new_file_path)
print(f"File renamed to {new_file_name}.")
new_dir_contents = os.listdir(new_dir_name)
print(f"Contents of '{new_dir_name}' after renaming the file:")
for item in new_dir_contents:
    print(item)
os.remove(new_file_path)
os.rmdir(new_dir_name)
print(f"Directory '{new_dir_name}' and its contents deleted.")