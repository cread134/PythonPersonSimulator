import command
import fileHandler
def exitProgram():
    return False

def showCommand():
    print("available commands:")
    for command in availableCommands.values():
        result = "  " + command.getName()
        result += " - " + command.getDescription()
        print(result)
    return True

def getFilesInDirectory():
    files = fileHandler.get_files();
    for file in files:
        print("-> " + file)
    return True;
    
availableCommands = {
    "exit": command.Command("exit", exitProgram, "exit the program"),
    "show": command.Command("show", showCommand, "show available commands"),
    "shwDir": command.Command("shwDir", getFilesInDirectory, "show files in directory")
}

def run_cmd(cmd):
    if cmd not in availableCommands:
        return "msg: => " + cmd + " is not a valid command"
    return availableCommands.get(cmd).cmd();

