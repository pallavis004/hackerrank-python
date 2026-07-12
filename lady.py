from collections import Counter
def happyLadybugs(b):
    counts = Counter(b)

    for ch, c in counts.items():
        if ch != '_' and c == 1:
            return "NO"

    if '_' in b:
        return "YES"

    for i in range(len(b)):
        left = b[i - 1] if i > 0 else None
        right = b[i + 1] if i < len(b) - 1 else None

        if b[i] != left and b[i] != right:
            return "NO"
    return "YES"
if __name__ == "__main__":
    g = int(input())

    for _ in range(g):
        n = int(input()) 
        b = input().strip()
        print(happyLadybugs(b)) 
