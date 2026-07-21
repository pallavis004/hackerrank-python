def palindromeIndex(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            string_after_removing_left = s[left + 1:right + 1]
            if string_after_removing_left == string_after_removing_left[::-1]:
                return left
            string_after_removing_right = s[left:right]
            if string_after_removing_right == string_after_removing_right[::-1]:
                return right
            return -1
    return -1
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
print(result)