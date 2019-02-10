
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["May", "Minnie", "Marshall", "Oscar", "Toby"]
""""         0        1          2         3        4   """
""""        -5       -4         -3        -2        -1    """
# Print out different elements of list
print(friends)
print(friends[1])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

# Modifying an element of list
friends[1] = "Mike"
print(friends[1])

# Inserting an element to particular index in the list
friends.insert(1, "Kelly")
print(friends)

# Extending list
friends.append("Creed")
print(friends)

# Removing element from the list
friends.remove("Toby")
print(friends)

# Popping out last element from the list
friends.pop()
print(friends)

# Making a copy of list
friends_copy = friends.copy()
print(friends_copy)

friends.append("Oscar")

# Soring ASB
friends.sort()
print(friends)

# Reversing order
lucky_numbers.reverse()
print(lucky_numbers)

# Merging lists together
friends.extend(lucky_numbers)
print(friends)

# Printing out Index of first element that match criteria
print(friends.index("Oscar"))

# Counting how elements match the criteria
print(friends.count("Oscar"))

# Deleting everything from the list
friends.clear()
print(friends)

# Tuples
coordinates = (1, 5)
print(coordinates)
# Tuples cannot be modified
# coordinates [0] = 7
