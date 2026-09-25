#Palindrome with time complexity o(n) checks if string is same when it is checked from last to first.
s=input("Enter a string: ")
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")