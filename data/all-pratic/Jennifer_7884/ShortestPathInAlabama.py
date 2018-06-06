stations = {'Alabaster':[('Birmingham', 24), ('Montgomery', 71)],
'Birmingham':[('Huntsville', 103), ('Tuscaloosa', 59)],
'Demopolis':[('Mobile', 141), ('Montgomery', 101), ('Tuscaloosa', 65)],
'Mobile':[('Montgomery', 169)],
'Montgomery':[('Tuscaloosa', 134)]}

print(stations.values())

def checkValid(station):
    if stations.keys().__contains__(origin.capitalize()) == False:
        values = stations.values()
        found = False
        for i in range(0, values.__len__()):
           if values[i][0] == station:
               found = True
        return found
    else:
        return True


origin = input("Enter your current location: ")
if checkValid(origin):
    print("Invalid origin")
dest = input("Enter your destination: ")
if checkValid(dest):
    print("Invalid destination")
