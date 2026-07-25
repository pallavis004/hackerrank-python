def icecreamParlor(m, arr):
    items = {}
    for i in range(len(arr)):
        need = m - arr[i]
        if need in items:
            print(items[need] + 1, i + 1)
            return
        items[arr[i]] = i
m = 4
arr = [1, 4, 5, 3, 2]
icecreamParlor(m, arr)