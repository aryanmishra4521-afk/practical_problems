def countdown(n):
    while n >= 1:
        yield n
        n -= 1


n = int(input("Enter starting number: "))

for number in countdown(n):
    print(number)
    