def taumBday(b, w, bc, wc, z):
    return b * min(bc, wc + z) + w * min(wc, bc + z)
if __name__ == '__main__':
    t = int(input()) 
    for _ in range(t):
        b, w = map(int, input().split())
        bc, wc, z = map(int, input().split())
        result = taumBday(b, w, bc, wc, z)
        print(result)