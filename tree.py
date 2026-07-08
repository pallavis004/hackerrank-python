from functools import reduce
def utopianTree(n):
    return reduce(lambda h,i: h*2 if i%2<1 else h+1, range(n), 1)

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(utopianTree(n))