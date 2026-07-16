def pangrams(s):
    return "pangram" if set(s.lower()) >= set("abcdefghijklmnopqrstuvwxyz") else "not pangram"
if __name__ == "__main__":
    s = input().strip()
    print(pangrams(s))