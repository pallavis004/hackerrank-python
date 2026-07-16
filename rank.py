def hackerrankInString(s):
    target = "hackerrank"
    it = iter(s)
    return "YES" if all(c in it for c in target) else "NO"
if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        s = input().strip()
        print(hackerrankInString(s))