class Mynum():
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a <= x:
            y = self.a
            self.a += 1
            return y*y
        else:
            raise StopIteration

cl = Mynum()
myiter = iter(cl)

x = int(input())

for y in myiter:
    print(y)
