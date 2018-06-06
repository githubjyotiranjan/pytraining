class Person:
    perinfo="person has 2 hands and 2 legs"
    print("person")
per1 = Person()
per1.name = "Ravi"

per2 = Person()
per2.name = "Kumar"

per3 = Person()
per3.name = "BS"

print (per3.name)
print (per1.name)
print (per2.name)

print(per3.perinfo)
print(per2.perinfo)
Person.perinfo = "testing"
print(Person.perinfo)