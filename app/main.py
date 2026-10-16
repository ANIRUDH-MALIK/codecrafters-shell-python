import sys


def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:
        sys.stdout.write("$ ")
        command = input()

        if command == "exit":
            # Exit the shell
            break
        elif command.startswith("echo"):
            # print with newline at the end
            print(command[5:])
        elif command.startswith("type"):
            if command[5:] in ["exit", "echo", "type"]:
                print(f"{command[5:]} is a shell builtin")
            else:
                print(f"{command[5:]}: not found")
        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
