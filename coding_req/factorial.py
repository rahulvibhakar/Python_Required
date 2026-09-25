#Factorial time complexity is o(n) and is used to get a number and multiply from 1 till that number and print the result.
n=int(input("Enter a number: "))
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
print("Factorial is: ",factorial(n))