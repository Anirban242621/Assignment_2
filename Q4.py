#Write a program to accept a character from the user and display whether it is a vowel or consonant.

ch = input("Enter a character: ")
if any(s.isdigit() for s in ch):
    raise ValueError("Input should be in Charector")
if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")





