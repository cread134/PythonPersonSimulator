class Command:
    def __init__(self, name, function, description):
        self.name = name
        self.function = function
        self.description = description
    def cmd(self):
        return self.function()
    def getName(self):
        return self.name
    def getDescription(self):
        return self.description