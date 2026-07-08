def simpleArraySum(ar):
    total = 0
    for x in ar:
        total = total + x
    return total


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    print(result)
