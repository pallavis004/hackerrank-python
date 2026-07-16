def alternate(s):
    chars = set(s)
    return max(
        (len(f) for a in chars for b in chars if a < b
         for f in [[c for c in s if c in (a, b)]]
         if all(f[i] != f[i+1] for i in range(len(f)-1))),
        default=0
    ) 
if __name__ == '__main__':
    l = int(input().strip())
    s = input()
    print(alternate(s))