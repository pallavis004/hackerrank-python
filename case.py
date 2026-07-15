def camelcase(s):
    return sum(1 for c in s if c.isupper()) + 1
if __name__ == '__main__':
    s = input().strip()
    print(camelcase(s))