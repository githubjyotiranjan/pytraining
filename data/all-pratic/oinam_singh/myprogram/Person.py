class Person:
    email="oinam@yahoo.co.in"
    print ("Hello class")

    def __init__(self,name,email,age,mobileNo):
        self.name=name
        self.email=email
        self.age=age
        self.__mobileNo=mobileNo
    def show(self):
        print(self.name,self.__mobileNo)
p=Person('oinam','oinam@sldf.com',29,9823432238)
print(p.email)
#p.__mobileNo  # error because of private
p.show();
