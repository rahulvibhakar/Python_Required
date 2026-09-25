#Second Largest number from the array with Time complexity o(n) where we find 2nd largest number from the array.
nums=[10,2,3,40,90]
largest=second=float('-inf')
for num in nums:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        second=num
print(second)