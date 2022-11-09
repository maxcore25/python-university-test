class Mealy:
    def __init__(self):
        self.state = 'A'

    def coat(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'B'
            return 3
        if self.state == 'C':
            self.state = 'C'
            return 5
        if self.state == 'E':
            self.state = 'B'
            return 8
        else:
            raise KeyError

    def scrub(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise KeyError


def main():
    return Mealy()


o = main()
print(o.scrub())  # 1
print(o.scrub())  # 6
print(o.coat())  # 8
print(o.coat())  # 3
print(o.coat())  # 3
print(o.scrub())  # 2
print(o.coat())  # 5
print(o.coat())  # 5
print(o.scrub())  # 4
print(o.scrub())  # 6
print(o.scrub())  # 7
