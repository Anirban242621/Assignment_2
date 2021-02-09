#WAP that reads two numbers and an arithmetic operator and displays the result

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
ch = input("Enter any of these char for specific operation +,-,*,/: ")
result = 0
if (ch == '+'):
    result = num1 + num2
elif (ch == '-'):
    result = num1 - num2
elif (ch == '*'):
    result = num1 * num2
elif(ch == '/'):
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, "=", result)