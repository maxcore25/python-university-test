class Mealy:
    def __init__(self):
        self.state = 'A'

    def coast(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'E':
            self.state = 'F'
            return 7
        if self.state == 'G':
            self.state = 'H'
            return 9
        if self.state == 'H':
            self.state = 'A'
            return 10
        else:
            raise KeyError

    def rig(self):
        if self.state == 'B':
            self.state = 'D'
            return 3
        if self.state == 'C':
            self.state = 'D'
            return 5
        if self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise KeyError

    def tail(self):
        if self.state == 'A':
            self.state = 'E'
            return 1
        if self.state == 'B':
            self.state = 'G'
            return 4
        if self.state == 'H':
            self.state = 'C'
            return 11
        if self.state == 'D':
            self.state = 'E'
            return 6
        else:
            raise KeyError


def main():
    return Mealy()


o = main()
print(o.coast())  # 0
print(o.rig())  # 3
print(o.tail())  # 6
print(o.coast())  # 7
print(o.rig())  # 8
print(o.coast())  # 9
print(o.coast())  # 10
print(o.tail())  # 1
print(o.coast())  # 7
print(o.rig())  # 8
print(o.coast())  # 9
print(o.rig())  # KeyError
print(o.tail())  # 11
print(o.tail())  # KeyError
print(o.rig())  # 5
print(o.tail())  # 6
