def pokerNim(k, c):
    xor = 0
    for chips in c:
        xor = xor ^ chips
    if xor == 0:
        return "Second"
    else:
        return "First"
k = int(input("Enter k: "))
c = list(map(int, input("Enter chips: ").split()))
answer = pokerNim(k, c)
print("Winner:", answer)