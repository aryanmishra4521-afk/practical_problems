def change_string(s):
    s = "X" + s[1:]
    print("Inside Function:", s)
text = input("Enter a string:")
print("Before Function Call:", text)
change_string(text)
print("After Function Call:", text)