import fileHandler
import commandManager

def get_input():
    result = input("Enter command: ")
    return result

def input_loop():
    while True:
        inputResult = get_input()
        command = commandManager.run_cmd(inputResult);
        if command == False:
            break
        if isinstance(command, str):
            if command[0:4] == "msg:":
                print(command)