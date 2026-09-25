#Prime number with Time complexity o(^n) checks whether number is Prime or not(number divisble by 1 and itself is Prime others are not).
prime=int(input("Enter a number: "))
is_prime=True

for i in range(2,int(prime**0.5)+1):
    if prime%i==0:
        is_prime=False
        break

if is_prime and prime>1:
    print(prime," is a Prime number.")
else:
    print(prime," is not Prime number.")