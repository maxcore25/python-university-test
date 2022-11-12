class Mealy:
    state = 'A'

    def debug(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'D':
            self.state = 'A'
            return 5
        if self.state == 'F':
            self.state = 'A'
            return 8
        raise KeyError

    def load(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == 'E':
            self.state = 'F'
            return 7
        raise KeyError

    def get(self):
        if self.state == 'B':
            self.state = 'D'
            return 2
        if self.state == 'D':
            self.state = 'D'
            return 6
        raise KeyError


def main():
    return Mealy()


o = main()
print(o.debug()) # 0
print(o.get()) # 2
print(o.get()) # 6
print(o.load()) # 4
print(o.load()) # 7
print(o.debug()) # 8
print(o.debug()) # 0
print(o.get()) # 2
print(o.debug()) # 5
print(o.debug()) # 0
print(o.load())
print(o.load())
