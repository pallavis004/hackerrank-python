def gamingArray(arr):
    moves = 0
    current_max = 0
    for x in arr:
        if x > current_max:
            current_max = x
            moves += 1
    return "BOB" if moves % 2 == 1 else "ANDY"
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        print(gamingArray(arr))