def interpret(textfile):
    with open(textfile) as f:
        lines = f.readlines()
        print(lines)


class Levelmaker:
    def __init__(self):
        self.LEVEL = None
