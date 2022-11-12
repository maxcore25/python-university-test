class Meeley:
    state = 'A'

    def skip(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'D'
            return 2
        if self.state == 'E':
            self.state = 'B'
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 9
        if self.state == 'G':
            self.state = 'H'
            return 11
        raise KeyError

    def crash(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'A'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 6

    def chat(self):
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == 'E':
            self.state = 'H'
            return 8
        if self.state == 'F':
            self.state = 'A'
            return 10
        raise KeyError


def main(o):
    o = Meeley()
    return o

