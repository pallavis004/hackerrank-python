def twoStrings(s1, s2):
    for letter in s1:
        if letter in s2:
            return "YES"
        else:
            continue
    return "NO"
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        print(result)
