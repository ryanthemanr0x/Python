# Exponent Function - take a number, and apply it to a certain power

# Example 1
print(2**3)

# Example 2
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))
