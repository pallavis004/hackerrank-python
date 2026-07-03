def getTotalX(a, b):
    count = 0
    for x in range(max(a), min(b) + 1):
        if all(x % i == 0 for i in a) and all(j % x == 0 for j in b):
            count += 1
    return count


if __name__ == '__main__':
    a = [2, 4]
    b = [16, 32, 96]
    print(getTotalX(a, b))