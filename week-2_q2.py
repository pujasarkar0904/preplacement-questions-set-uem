arr = [1, 0, 3, 0, 5, 0, 2]

result = []

# Add non-zero elements firsts
for x in arr:
    if x != 0:
        result.append(x)

# Add zeros at the end
for x in arr:
    if x == 0:
        result.append(x)

print("Array after moving zeros:", result)