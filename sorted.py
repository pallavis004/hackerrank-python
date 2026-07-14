def almostSorted(arr):
    s = sorted(arr)
    if arr == s:
        print("yes")
        return
    diff = [i for i in range(len(arr)) if arr[i] != s[i]]
    if len(diff) == 2:
        print("yes")
        print("swap", diff[0] + 1, diff[1] + 1)
        return
    l, r = diff[0], diff[-1]
    if arr[:l] + arr[l:r+1][::-1] + arr[r+1:] == s:
        print("yes")
        print("reverse", l + 1, r + 1)
    else:
        print("no")
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    almostSorted(arr)