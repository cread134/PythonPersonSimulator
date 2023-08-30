import command
def exitProgram():
    return False


def showCommand():
    for command in availableCommands:
        print(command);
    return True
    
availableCommands = {
    "exit": command.Command("exit", exitProgram),
    "show": command.Command("show", showCommand)
}

def run_cmd(cmd):
    return availableCommands.get(cmd).cmd();

