import os 
import shutil

from_dir = "C:\\Users\\Admin\\Desktop\\Aarush files\\WhiteHatJr\\Visual projects\\Class102"
to_dir = "C:\\Users\\Admin\\Desktop\\Aarush files\\WhiteHatJr\\Visual projects\\Class102\\test"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:

    name, ext = os.path.splitext(file_name)
    print(name)
    print(ext)

    if ext == "":
        continue
    if ext in ['.gif', '.jfif', '.jpg', '.jpeg', '.png']:
        path1 = from_dir + '/' + file_name

        path2 = to_dir + '/' + "Image_files"

        path3 = to_dir + '/' + "Image_files" + '/' + file_name
        print(path1)
        print(path3)

        if os.path.exists(path2):
            print("Moving " + file_name + "..")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving "+ file_name + "..")
            shutil.move(path1, path3)




