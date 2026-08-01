def nimbleGame(s):
    answer = 0
    for i in range(len(s)):
        if s[i] % 2 == 1:
            answer = answer ^ i
    if answer == 0:
        return "Second"
    else:
        return "First"
s = list(map(int, input("Enter the coins: ").split()))
answer = nimbleGame(s)
print("Winner:", answer)