marks=int(input("Enter marks: "))
if(marks>=90):
    print("Excellent.")
elif(marks>=70 and marks<=89):
    print("Good")
elif(marks>=60 and marks<=69):
    print("Better")
else:
    print("Needs improvement.")