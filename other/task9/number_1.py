class Meally:
    state = 'A'

    def view(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'E'
            return 6
        if self.state == 'E':
            self.state = 'F'
            return 8
        raise KeyError

    def edit(self):
        if self.state == 'A':
            self.state = 'D'
            return 2
        if self.state == 'B':
            self.state = 'C'
            return 3
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 7

    def bend(self):
        if self.state == 'C':
            self.state = 'A'
            return 5
        if self.state == 'A':
            self.state = 'E'
            return 1


def main():
    o = Meally()
    return o


o = main()
print(o.view()) # 0
print(o.edit()) # 3
print(o.bend()) # 5
print(o.edit()) # 0
print(o.view()) # KeyError
print(o.edit()) # 7
print(o.view()) # 8
