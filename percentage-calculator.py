import numbers

x = int(input("Enter computers patched: "))
y = int(input("Enter total patchable computers: "))
z = 100/(int(x)+int(y))

print("The total number of patched computers is " +str(y*z) + "%")
