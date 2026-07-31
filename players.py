def nimGame(pile):
    answer = 0
    for stones in pile:
        answer = answer ^ stones
    if answer == 0:
        return "Second"
    else:
        return "First"
pile = list(map(int, input("Enter the pile values: ").split()))
result = nimGame(pile)
print("Winner:", result)