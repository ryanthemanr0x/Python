# If Statements

is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

is_male1 = True
is_tall1 = True

if is_male1 and is_tall1:
    print("You are a tall male")
else:
    print("You are either not male or tall or both")

is_male2 = True
is_tall2 = False

if is_male2 and is_tall2:
        print("You are a tall male")
elif is_male2 and not(is_tall2):
        print("You are a short male")
elif not(is_male2) and is_tall2:
        print("You are not a male and are tall")
else:
        print("You are either not male or tall or both")