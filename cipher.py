def caesarCipher(s, k):
    def shift(c):
        if c.isalpha():
            base = 65 if c.isupper() else 97
            return chr((ord(c) - base + k) % 26 + base)
        return c
    return ''.join(shift(c) for c in s) 
if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    print(caesarCipher(s, k))