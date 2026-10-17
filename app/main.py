import os 
import sys

# Global
VERBOSE = False

def log(*args, **kwargs):
    """Prints messages only if the global VERBOSE flag is True."""
    if VERBOSE:
        print("[VERBOSE]", *args, **kwargs)

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
            command_found = False
            if command[5:] in ["exit", "echo", "type"]:
                print(f"{command[5:]} is a shell builtin")
                command_found = True

            elif len(os.get_exec_path()) > 0:
                log(f"{command[5:]} is not a shell builtin, checking at PATH")
                log(f"-> Count of folder at PATH: {len(os.get_exec_path())}")

                for path in os.get_exec_path():
                    log(f"--> Folder at: {path} exist: {os.path.exists(path)}")

                    if os.path.exists(path):
                        count_of_filesandfolders = len( os.listdir(path) )
                        log(f"---> Count of files and folders: {count_of_filesandfolders}")

                        for item in os.listdir(path):
                            log(f"----> Item: {item}", end = " | ")
                            #breakpoint()
                            if os.path.isfile( os.path.join(path, item ) ):
                                log(f"Type: File", end = " | ")
                                if item == command[5:]:
                                    log(f"Matched: True", end = " | ")
                                    if os.access(os.path.join(path, item ), os.X_OK):
                                        log(f"Executable: True")
                                        print(f"{command[5:]} is {os.path.join(path, item )}")
                                        command_found = True
                                        break
                                else:
                                    log(f"Matched: False", end = " | ")
                            else:
                                log(f"Type: Folder", end = " | ")
                            log()
                        #breakpoint()
                        if command_found:
                            break
                    else:
                        log("Path does not exist. Check next folder.")

            else:
                log(f"PATH is empty")

            if not command_found:
                print(f"{command[5:]}: not found")

        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
