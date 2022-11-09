class Mealy:
    def __init__(self):
        self.state = 'A'

    def merge(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'D':
            self.state = 'A'
            return 6
        if self.state == 'E':
            self.state = 'F'
            return 8
        else:
            raise KeyError

    def amble(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        if self.state == 'B':
            self.state = 'C'
            return 3
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise KeyError

    def erase(self):
        if self.state == 'D':
            self.state = 'F'
            return 7
        if self.state == 'A':
            self.state = 'F'
            return 2
        else:
            raise KeyError


def main():
    return Mealy()


o = main()
print(o.merge())  # 0
print(o.amble())  # 3
print(o.amble())  # 4
print(o.merge())  # 6
print(o.amble())  # 1
print(o.merge())  # 0
print(o.amble())  # 3
print(o.amble())  # 4
print(o.amble())  # 5
print(o.amble())  # KeyError
print(o.merge())  # 8
