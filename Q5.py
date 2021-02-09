#WAP to input a number and check whether the number is 2 digit number or not.
def specialNumber(n): 
	if (n < 10 or n > 99): 
		print("Invalid Input! The given number is not two digit") 
	else:
		print(n , " is a Two-Digit Number") 		
n = int(input("Enter a number"))
specialNumber(n) 