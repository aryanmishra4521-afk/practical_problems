def maximum(a, b):
    if a > b:
        return a
    else:
        return b
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
print("The maximum number is:", maximum(number1, number2))