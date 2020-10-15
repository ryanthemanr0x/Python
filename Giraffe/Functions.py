# Functions - Lines of code to accomplish a task
# Code MUST be indented, to be part of the function!
# Named in lower case, 2 or more words = use underscore!

#def = function
def say_hi():
    print("Hello User")


# Execute the function = Calling the function
print("Top")
say_hi()
print("Bottom")

# Parameter = information given to the function

def say_hi1(name):
    print("Hello " + name )


# Execute the function = Calling the function
say_hi1("Ryan")
say_hi1("Steve")
say_hi1("Mike")

def say_hi2(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi2("Ryan", "34")
say_hi2("Steve", "70")
say_hi2("Mike", "60")
