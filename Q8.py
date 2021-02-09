#WAP to input marks of 5 subject and find average and assign grade
sub1=int(input("Enter marks of the First subject: "))
sub2=int(input("Enter marks of the Second subject: "))
sub3=int(input("Enter marks of the Third subject: "))
sub4=int(input("Enter marks of the Fourth subject: "))
sub5=int(input("Enter marks of the Fifth subject: "))
total=(sub1+sub2+sub3+sub4+sub4)
avg=total/5
if(avg>=90):
    print("Grade: O")
elif(avg>=80 and avg<=89):
    print("Grade: E")
elif(avg>=70 and avg<=79):
    print("Grade: A")
elif(avg<70):
    print("Grade: B")