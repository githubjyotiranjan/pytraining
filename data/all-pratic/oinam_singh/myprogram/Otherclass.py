import PersonNew
#p2=PersonNew("Oinam",'ssdfsd@sldjfl.com',23,972343433)
#PersonNew.s
class Otherclass (PersonNew) :
    otherVar="other var"
    def __init__(self,name,email,age):
        super(Otherclass, self).__init__(name,email,age)
    def show(self):
        self.show()
        #print(self.name, self.email, self.age)
other=Otherclass("Oinam",'ssdfsd@sldjfl.com',23)
other.show()