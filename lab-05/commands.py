import os 
import shutil

def cd(path: str):
    try:
        os.chdir(path)
    except:
        print("No such dirrectory")

def ls(path: str = None):
    try:
        if path is None or path == "":
            path = pwd()
        lst = os.listdir(path)
        for l in lst:
            print(l)
    except:
        print("Something is wrong")

def pwd()->str:
    current_directory = os.getcwd()
    return current_directory

def touch(path: str):
    try:
        open(path, 'a').close()
    except:
        print(f"Cannot create a file in such a directory {path}")

def rm(path: str):
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        else:
            raise(FileNotFoundError)
    except FileNotFoundError:
        print(f"{path} does not exist.")

def mkdir(path: str):
    try:
        os.makedirs(path, 0o777, False)
    except:
        print(f"Could not create a directory {path}")

def mv(old: str, new: str):
    try:
        os.rename(old, new)
    except:
        print("Something went wrong")

def less(path: str):
    with open(path, "r") as f:
        num_lines = sum(1 for line in f)
        f.seek(0)
        current_line = 0
        lines_to_display = 25
        
        # Print the contents of the file one page at a time
        while current_line < num_lines:
            for i in range(current_line, current_line + lines_to_display):
                line = f.readline()
                if line:
                    print(line, end='')
                else:
                    break
            current_line += lines_to_display
            # Wait for user input before displaying the next page
            inp = input("Press any button to continue or q to exit... ")
            if inp == 'q':
                os.system('clear')
                break
            os.system('clear')

def help():
    print("Use 'cd' cammand to change directory \n"
        "Use 'ls' command to see the content of a directory \n"
        "Use 'mkdir' command to create a directory \n"
        "Use 'touch' command to create a file \n"
        "Use 'mv' command to rename a file or a directory \n"
        "Use 'pwd' command to see the currennt directory \n"
        "Use 'less' command to see the content of a file \n"
        "Use 'exit' command to exit the program ") 