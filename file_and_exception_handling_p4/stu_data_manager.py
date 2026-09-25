try:
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    with open("stu.txt","a") as file:
        file.write(f"{name},{age}")
except ValueError:
    print("Wrong value!!")