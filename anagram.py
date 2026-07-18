def anagram(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    first = s[:mid]
    second = s[mid:]
    c1 = Counter(first)
    c2 = Counter(second)
    changes = 0
    for ch in c1:
        if c1[ch] > c2[ch]:
            changes += c1[ch] - c2[ch]
    return changes
if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        result = anagram(s)
        print(result)