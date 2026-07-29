def gameOfStones(n):
    if n % 7 == 0 or n % 7 == 1:
        return "Second"
    else:
        return "First"
t = int(input("Enter number of test cases: "))
for i in range(t):
    n = int(input("Enter number of stones: "))
    print(gameOfStones(n))