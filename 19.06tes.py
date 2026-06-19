a = int(input("Enter a number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >b and a > c:
    print(f"The Largest number is {a}")
elif b > a and b > c:
    print(f"The Largest number is {b}")
else:
    print(f"The Largest number is {c}")
    