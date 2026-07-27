def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    total = 0
    for i in range(len(calorie)):
        total = total + (2 ** i) * calorie[i]
    return total
n = int(input("Enter number of cupcakes: "))
calorie = list(map(int, input("Enter calories: ").split()))
print(marcsCakewalk(calorie))