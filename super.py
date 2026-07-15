def superReducedString(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack) or "Empty String"
if __name__ == '__main__':
    s = input().strip()
    print(superReducedString(s))