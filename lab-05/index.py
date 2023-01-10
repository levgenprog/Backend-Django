import commands

def main():
    commands.cd("/home/")
    print("Type --h for help")
    print("Type exit to quit the program")
    while True:
        try:
            command = input(f"{commands.pwd()} >> ")
            command.strip()
            words = command.split()
            if words[0] == "cd":
                commands.cd(get_command(words))
            elif words[0] == "ls":
                commands.ls(get_command(words))
            elif words[0] == "touch":
                commands.touch(get_command(words))
            elif words[0] == "rm":
                commands.rm(get_command(words))
            elif words[0] == "mkdir":
                commands.mkdir(get_command(words))
            elif words[0] == "mv":
                words.pop(0)
                commands.mv(words[0], words[1])
            elif words[0] == "less":
                commands.less(get_command(words))
            elif words[0] == "pwd":
                print(commands.pwd())
            elif words[0] == "--h":
                commands.help()
            elif words[0] == "exit":
                print("See you! ")
                break
        except:
            print(f"Something went wrong {command}")

def get_command(words):
    words.pop(0)
    return(" ".join(words))

if __name__ == '__main__':
    main()
