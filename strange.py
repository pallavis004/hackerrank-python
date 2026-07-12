def strangeCounter(t):
    start, total = 3, 3
    while t > total:
        start *= 2
        total += start
    return total - t + 1
if __name__ == "__main__":
    t = int(input())
    print(strangeCounter(t))