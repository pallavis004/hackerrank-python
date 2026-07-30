def lonelyinteger(a):
    for number in a:
        count = 0
        for value in a:
            if number == value:
                count = count + 1
        if count == 1:
            return number
input()
a = list(map(int, input().split()))
print(lonelyinteger(a))