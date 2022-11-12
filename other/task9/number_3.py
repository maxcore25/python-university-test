class Meally:
    state = 'A'

    def join(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'D'
            return 3
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'F'
            return 7
        raise KeyError

    def paste(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'F'
            return 5
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'E':
            self.state = 'F'
            return 8


def main():
    o = Meally()
    return o


o = main()
print(o.join())
print(o.paste())
print(o.join())
print(o.paste())
print(o.paste())
