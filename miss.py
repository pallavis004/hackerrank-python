def misereNim(s):
    answer = 0
    for stones in s:
        answer = answer ^ stones
    one = True
    for stones in s:
        if stones > 1:
            one = False
            break
    if one:
        if len(s) % 2 == 0:
            return "First"
        else:
            return "Second"
    else:
        if answer == 0:
            return "Second"
        else:
            return "First"
n = int(input("Enter number of piles: "))
print("Enter stones in each pile:")
s = list(map(int, input().split()))
print("Winner:", misereNim(s))