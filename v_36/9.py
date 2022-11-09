class Mealy:
    def __init__(self):
        self.state = 'A'

    def pan(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'E':
            self.state = 'F'
            return 5
        if self.state == 'F':
            self.state = 'G'
            return 7
        if self.state == 'G':
            self.state = 'C'
            return 9
        else:
            raise KeyError

    def skew(self):
        if self.state == 'A':
            self.state = 'F'
            return 1
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == 'E':
            self.state = 'A'
            return 6
        if self.state == 'F':
            self.state = 'B'
            return 8
        else:
            raise KeyError


def main():
    return Mealy()


o = main()
print(o.pan())  # 0
print(o.pan())  # 2
print(o.skew())  # 3
print(o.skew())  # 4
print(o.skew())  # 6
print(o.skew())  # 1
print(o.pan())  # 7
print(o.pan())  # 9
print(o.skew())  # 3
print(o.skew())  # 4
print(o.pan())  # 5
print(o.skew())  # 8
print(o.pan())  # 2
