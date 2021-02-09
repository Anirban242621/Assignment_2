#WAP to input a number and check whether the number is divisible by 5 and 3 or not.
num = int(input(" Enter the number : "))

if((num % 5 == 0) and (num % 3 == 0)):
    print("Given Number is Divisible by 5 and 3",num)
else:
    print("Given Number is Not Divisible by 5 and 3",num)