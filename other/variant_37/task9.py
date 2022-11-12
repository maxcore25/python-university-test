class Mealy:
    state = "A"

    def punch(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "D":
            self.state = "A"
            return 6
        raise KeyError

    def stare(self):
        if self.state == "A":
            self.state = "E"
            return 1
        if self.state == "B":
            self.state = "C"
            return 3
        raise KeyError

    def carve(self):
        if self.state == "A":
            self.state = "C"
            return 2
        if self.state == "C":
            self.state = "D"
            return 4
        if self.state == "D":
            self.state = "E"
            return 5
        if self.state == "E":
            self.state = "F"
            return 7
        if self.state == "F":
            self.state = "G"
            return 8
        if self.state == "G":
            self.state = "D"
            return 9
        raise KeyError


def main():
    return Mealy()

