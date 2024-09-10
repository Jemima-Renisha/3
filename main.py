class bird:
    def __init__(self):
        print("It is bird class")
    def birdname(self):
        print("Birdname")
    def walk(self):
        print("It can walk")
class penguin(bird):
    def __init__(self):
        super().__init__()
    def birdname(self):
        print("Bird name is penguin")
    def walk(self):
        print("It can walk!!!")

x = penguin()
x.birdname()
x.walk()
