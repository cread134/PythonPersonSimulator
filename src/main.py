import fileHandler

import commandManager


def get_input():

    result = input("Enter name: ")
    return result


def input_loop():
    while True:
        inputResult = get_input()
        command = commandManager.run_cmd(inputResult);
        if command == False:
            break
        if isinstance(command, str):
            print (command)
            if command[0:4] == "msg:":
                print(command)

if __name__ == "__main__":
    input_loop()