def remove_last (lst):
 lst.pop()
 return lst
numbers = []
n = int(input("Enter the number of elements you want to add to the list: "))
for i in range(n):
 value = int(input("Enter a number: "))
 numbers.append(value)
print("Before Function Call:", numbers)
remove_last(numbers)
print("After Function Call:", numbers)