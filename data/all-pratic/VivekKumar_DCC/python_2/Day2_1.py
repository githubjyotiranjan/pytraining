randomList=int(input('enter the count='))
vals=1;
while(vals<= randomList):
    try:
       if(randomList%2!= 0):
        print("The odd= ", vals)
        vals=vals+1
    except:
        print("The Even= ", vals)
