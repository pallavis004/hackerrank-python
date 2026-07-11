import math
def encryption(s):
    s = s.replace(" ", "")
    L = len(s)
    c = math.ceil(math.sqrt(L))
    r = math.floor(math.sqrt(L))
    r = c if r * c < L else r
    return " ".join("".join(s[j] for j in range(i, L, c)) for i in range(c))
if __name__ == '__main__':
    s = input().strip()
    print(encryption(s))