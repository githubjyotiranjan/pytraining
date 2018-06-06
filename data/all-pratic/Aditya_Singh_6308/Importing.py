class Test:

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __set__(self, instance, value):
        print("Setter")
        self.a = value

    def add(self):
        return self.b + self.a + self.c
