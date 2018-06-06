class Dog:
    def __init__(self,name,age,teeth):
        self.name=name
        self.age=age
        self.teeth=teeth
    def __init__(self,nm,colour):
        self.nm=nm
        self.colour=colour

dog1 = Dog("alsation",12,"white")
print(dog1.name, dog1.age, dog1.teeth)
dog2 = Dog("xxx",10,"Black")
print(dog2.name, dog2.age, dog2.teeth)
dog3 = Dog("yyy","Brown")
print(dog3.nm, dog3.colour)
