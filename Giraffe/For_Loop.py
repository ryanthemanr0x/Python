# For Loop

#Example 1 - Define variable for each iteration of the loop
for letter in "Giraffe Academy":
    print(letter)

#Example 2
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

# Example 3
friends = ["Jim", "Karen", "Kevin"]
for name in friends:
    print(name)

# Example 4
for index in range(10):
    print(index)

# Example 5
for index in range(3, 10):
    print(index)

# Example 6
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index])

# Example 7
for index in range(10):
    if index == 0:
        print("First iteration")
    else:
        print("Not First!")


