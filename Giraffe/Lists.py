# Working with lists

# Lists can include integers and boolean
# friends = ["Kevin", 2, False]

friends = ["Kevin", "Karen", "Jim"]
print(friends)

# Using index
friends = ["Kevin", "Karen", "Jim"]
#              0        1/-2      2/-1
print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[-2])
print(friends[1:])

friends1 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#              0        1      2        3        4
# Will grab all the elements upto, but not including last element
print(friends1[1:4])

friends[1] = "Mike"
print(friends[1])