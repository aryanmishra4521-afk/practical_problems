text = input("Enter your text: ")
print("Uppercase ", text.upper())
print("Lowercase ", text.lower())
print("reverse", text[::-1])

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1
        print("Total Number of Vowel found: ", count)
