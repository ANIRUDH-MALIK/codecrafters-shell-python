import sys


def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:
        sys.stdout.write("$ ")
        command = input()

        if command == "exit":
            # Exit the shell
            break

        if command.startswith("echo "):
            # print with newline at the end
            print(command[5:])
            continue
        
        print(f"{command}: command not found")



if __name__ == "__main__":
    main()
