#WAP to input 3 numbers and find the second smallest.
print("Enter 3 numbers")
x, y, z = int(input()), int(input()), int(input())
if x<y<z or z<y<x:
   print(y,"is the second smallest number")
elif y<z<x or x<z<y:
    print(z,"is the second smallest number")
else:
    print(x,"is the second smallest number")