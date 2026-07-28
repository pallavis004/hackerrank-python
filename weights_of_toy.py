def toys(w):
    w.sort()
    count = 1
    first_weight = w[0]
    for weight in w:
        if weight > first_weight + 4:
            count = count + 1
            first_weight = weight
    return count
weights = list(map(int, input("Enter toy weights: ").split()))
print(toys(weights))