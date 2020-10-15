# Write to files
'''
# Example 1 - Append to an existing file
employee_file = open("employees.txt", "a")
#print(employee_file.read())

#employee_file.write("Toby - Human Resources")

#Escape Character - New line Character = \n
employee_file.write("\nKelly - Customer Service")

employee_file.close()
'''

'''
# Example #2 - Create and Write to a new file
employee_file = open("employees1.txt", "w")

#Escape Character - New line Character = \n
employee_file.write("\nKelly - Customer Service")

employee_file.close()
'''

# Example #3 - Create and Write to a new HTML file
employee_file = open("index.html", "w")

#Escape Character - New line Character = \n
employee_file.write("<p>This is HTML</p>")

employee_file.close()
