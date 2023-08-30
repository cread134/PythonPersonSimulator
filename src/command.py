class Command:
    def __init__(self, name, function):
        self.name = name
        self.function = function
    def cmd(self):
        return self.function()