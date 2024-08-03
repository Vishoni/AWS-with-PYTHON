# 1) String operations
name = "some name"

# Convert to upper, lower, and capitalize
name_upper = name.upper()
name_lower = name.lower()
name_capitalized = name.capitalize()

# Replace 'e' with 'E'
name_replaced = name.replace('e', 'E')

print("Original Name:", name)
print("Uppercase:", name_upper)
print("Lowercase:", name_lower)
print("Capitalized:", name_capitalized)
print("Replaced 'e' with 'E':", name_replaced)

# 2) List operations
L = [1, 2, 3]

# Extend the list with [5, 6, 7]
L.extend([5, 6, 7])

# Remove the 5th value (index 4, since indexing starts at 0)
L.pop(4)

print("Updated List:", L)

# 3) Dictionary operations
d = {'mango': 10, 'banana': 0, 'apple': 15, 'orange': 0, 'pineapple': 20}

# Remove out-of-stock fruits
d = {key: value for key, value in d.items() if value > 0}

# Update mango quantity to 15
d['mango'] = 15

# Decrease pineapple quantity by 5
d['pineapple'] -= 5

print("Updated Dictionary:", d)
