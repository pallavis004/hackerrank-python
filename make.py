def makingAnagrams(s1, s2):
    deletions = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        count1 = s1.count(letter)
        count2 = s2.count(letter)
        deletions += abs(count1 - count2)
    return deletions
if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)
    print(result)
