def towerBreakers(n, m):
    if m == 1:
        return 2
    if n % 2 == 0:
        return 2
    return 1
n = int(input("Enter number of towers: "))
m = int(input("Enter height of each tower: "))
answer = towerBreakers(n, m)
print("Winner:", answer)