def add_entry(d):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    d[key] = value
def reassign_dict(d):
    d = {"new" : "dictionary"}
    print("Inside reassgin function :" ,d)
data = {}
n = int(input("Enter the number of entries : "))
for i in range(n):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    data[key] = value
print("Original Dictionary:", data)
add_entry(data)
print("After Function Call:", data)
reassign_dict(data)