def catAndMouse(x, y, z):
    a = abs(x - z)
    b = abs(y - z)
    if a < b:
        return "Cat A"
    elif b < a:
        return "Cat B"
    else:
        return "Mouse C"
if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        x, y, z = map(int, input().split())
        print(catAndMouse(x, y, z))
