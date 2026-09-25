#Exception handling is process of handling runtime errors at time of execution.
try:
    age=int(input())
except ValueError:
    print("Invalid value")
except Exception as e:
    print(e)