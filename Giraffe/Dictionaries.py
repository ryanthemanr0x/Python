# Dictionary = Key value pairs

month_Conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(month_Conversions["Nov"])
print(month_Conversions["Mar"])
print(month_Conversions.get("Dec"))
# Test entering in value not in dictionary
print(month_Conversions.get("Luv", "Not a valid key!!!"))

