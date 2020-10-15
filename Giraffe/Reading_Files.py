# Reading Files

# Files can be opened in a few modes: r = read / w = write / a = append / r+ = read and write

# Open file, and store in variable
employee_file = open("employees.txt", "r")

# Test if the file is readable
# print(employee_file.readable())

# Print all information in the file
#print(employee_file.read())

# Read first line in the file
#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.readline())

# Read all lines in the file
#print(employee_file.readlines())

# Read specific lines in the index of the file
#print(employee_file.readlines()[1])

#Create loop to display all lines in the file
for employee in employee_file.readlines():
    print(employee)

# Make sure to close files!!
employee_file.close()