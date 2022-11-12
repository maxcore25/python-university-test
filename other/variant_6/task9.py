class Meely:
    state = "A"

    def scale(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "C"
            return 1
        if self.state == "C":
            self.state = "G"
            return 5
        if self.state == "E":
            self.state = "E"
            return 8
        if self.state == "F":
            self.state = "G"
            return 9
        else:
            raise KeyError

    def drag(self):
        if self.state == "B":
            self.state = "E"
            return 2
        if self.state == "C":
            self.state = "D"
            return 3
        if self.state == "D":
            self.state = "E"
            return 6
        else:
            raise KeyError

    def tag(self):
        if self.state == "C":
            self.state = "C"
            return 4
        if self.state == "E":
            self.state = "F"
            return 7
        else:
            raise KeyError


def main():
    return Meely()


o = main()
print(o.scale())
print(o.scale())
print(o.tag())
print(o.tag())
print(o.drag())
print(o.drag())
print(o.scale())
print(o.scale())
print(o.tag())
print(o.scale())
