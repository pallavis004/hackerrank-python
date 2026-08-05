def sumXor(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        if n % 2 == 0:
            count = count + 1
        n = n // 2
    return 2 ** count
n = int(input("Enter a number: "))
answer = sumXor(n)
print("Answer:", answer)