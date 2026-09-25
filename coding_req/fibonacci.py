#Fibonacci with Time complexity o(n) where we give input and first and second number is added to get 3 rd number and is done until user input is completed.
n=int(input("Enter a number: "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b