s = input("Enter a string: ")

result = s[0].upper() + s[1:-1] + s[-1].upper()

print("Result:", result)