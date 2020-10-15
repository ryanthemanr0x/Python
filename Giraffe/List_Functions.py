# List Functions

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# Add lists together
# friends.extend(lucky_numbers)
print(friends)

# Append lists - Add items to the end of the list
friends1 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends1.append("Creed")
print(friends1)

# Insert items into lists
friends2 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2.insert(1, "Kelly")
print(friends2)

# Remove elements from lists
friends3 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends3.remove("Jim")
print(friends3)

# Clear elements from lists
friends4 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends4.clear()
print(friends4)

# pop elements from lists - remove last element from the list
friends5 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends5.pop()
print(friends5)

# find elements in lists - Which index value is the element in
friends6 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends6.index("Kevin") )
print(friends6.index("Jim") )

# count how many times an element appears in a list
friends7 = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends7.count("Jim") )

# sort list in ascending order
friends8 = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends8.sort()
lucky_numbers.sort()
print(friends8)
print(lucky_numbers)

# sort list in decending order
lucky_numbers1 = [4, 8, 15, 16, 23, 42]
lucky_numbers1.reverse()
print(lucky_numbers1)

# copy list
friends9 = friends.copy()
print(friends9)