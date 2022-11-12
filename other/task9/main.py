class Mealy:
    state = "A"

    def build(self):
        if self.state == "A":
            self.state = "A"
            return 1
        if self.state == "D":
            self.state = "A"
            return 5
        if self.state == "E":
            self.state = "F"
            return 6

    def skew(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "C"
            return 2
        if self.state == "C":
            self.state = "D"
            return 3
        if self.state == "D":
            self.state = "E"
            return 4
        if self.state == "E":
            self.state = "A"
            return 7
        if self.state == "F":
            self.state = "D"
            return 8


def main():
    o = Mealy()
    return o


o = main()
print(o.skew())  # 0
print(o.skew())  # 2
print(o.skew())  # 3
print(o.skew())  # 4
print(o.build())  # 6
print(o.skew())  # 8
print(o.build())  # 5
print(o.skew())  # 0
print(o.skew())  # 2
print(o.skew())  # 3
print(o.skew())  # 4
print(o.skew())  # 7
