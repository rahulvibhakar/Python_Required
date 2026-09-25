try:
    num=int(input("Enter a number: "))
    for i in range(1,11):
        print("The table is as follows: ")
        print(f"{num} x {i} = {num*i}")
except ValueError:
    print("Enter valid integer.")
