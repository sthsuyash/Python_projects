import os
import shutil

# gets current directory full path
current_dir = os.getcwd()

# gets all the files in current directory as list
files = os.listdir(current_dir)

# iterate through all the files to display
print(f"\n\nThe files in {current_dir} are:")
i = 0
for file in files:
    i += 1
    print(f"{i}) {file}")


def main():
    print(
        """
***** Press to delete: *****
1) file by extension.
2) file by name.
3) folder.
    """)
    delete_type = int(input(f"Enter your choice: "))
    remove = False

    match delete_type:
        case 1:
            file_extension = input("Enter the file extension to remove: ")

            # iterate through all files
            for file in files:
                # if the file extension is as required, delete the file
                if file.endswith("."+file_extension):
                    os.remove(os.path.join(current_dir, file))
                    remove = True

            if remove == True:
                print(f"'.{file_extension}' files removed.\n")
            else:
                print(
                    f"No files with '.{file_extension}' extension found in current directory.\n")
        case 2:
            file_name = input("Enter name of file to remove: ")

            # iterate through all files
            for file in files:
                # if the file name is as required, delete the file
                if file == file_name:
                    os.remove(os.path.join(current_dir, file))
                    remove = True

            if remove == True:
                print(f"'.{file_name}' file removed.\n")
            else:
                print(
                    f"No files with '{file_name}' name found in current directory.\n")

        case 3:
            folder_name = input(f"Enter name of folder to remove: ")

            # iterate through all files
            for file in files:
                # if the file name is as required, delete the file
                if file == folder_name:
                    shutil.rmtree(folder_name)
                    remove = True

            if remove == True:
                print(f"'.{folder_name}' folder removed.\n")
            else:
                print(
                    f"No folder with '{folder_name}' name found in current directory.\n")

        case default:
            print("Please enter the valid type!!")
            main()


main()
os.system("pause")
