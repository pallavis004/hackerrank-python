def marsExploration(s):
    sos = "SOS" * (len(s) // 3)
    return sum(a != b for a, b in zip(s, sos))
if __name__ == "__main__":
    s = input().strip()
    print(marsExploration(s))