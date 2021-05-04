class Sum():
    def __init__(self, a):
        self.a = a


    def __add__(self, b):
        return self.a + b + 1

s = Sum(9)

print(s+1)