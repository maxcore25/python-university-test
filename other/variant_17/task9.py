class Mealy:
    state = "A"

    def march(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "C"
            return 1
        if self.state == "D":
            self.state = "A"
            return 4
        if self.state == "E":
            self.state = "F"
            return 5
        if self.state == "F":
            self.state = "C"
            return 8
        if self.state == "G":
            self.state = "H"
            return 9
        raise KeyError

    def color(self):
        if self.state == "C":
            self.state = "D"
            return 2
        if self.state == "F":
            self.state = "G"
            return 7
        if self.state == "G":
            self.state = "C"
            return 10
        raise KeyError

    def fill(self):
        if self.state == "D":
            self.state = "E"
            return 3
        if self.state == "E":
            self.state = "C"
            return 6
        if self.state == "G":
            self.state = "A"
            return 7


def main():
    o = Mealy()
    return o


o = main()
print(o.march())
print(o.march())
print(o.color())
print(o.fill())
print(o.fill())
print(o.color())
print(o.fill())
print(o.march())
print(o.color())
print(o.color())
print(o.color())
print(o.color())
print(o.march())
print(o.march())
