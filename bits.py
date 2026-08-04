def flippingBits(n):
    max_value = 4294967295
    result = max_value - n
    return result
n = int(input("Enter a number: "))
result = flippingBits(n)
print(result)