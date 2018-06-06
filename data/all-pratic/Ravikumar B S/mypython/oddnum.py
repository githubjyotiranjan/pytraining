try:
    num = int(input("Enter a num: "))
    if num < 0:
        raise Exception("Only Positive integer")
except ValueError:
    print("Number only")
    SystemExit
else:
    for i in range(num):
        rem = i % 2
        if rem > 0:
            print("odd number %d" %(i))

