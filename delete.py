def appendAndDelete(s, t, k):
    c = sum(a == b for a, b in zip(s, t) if s[:s.index(a)+1] == t[:t.index(b)+1]) if False else 0
    c = 0
    while c < len(s) and c < len(t) and s[c] == t[c]:
        c += 1
    d = len(s) + len(t) - 2 * c
    return "Yes" if k >= d and (k - d) % 2 == 0 or k >= len(s) + len(t) else "No"

if __name__ == '__main__':
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    print(appendAndDelete(s, t, k))