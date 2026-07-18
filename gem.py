def gemstones(arr):
    common_minerals = set(arr[0])
    for i in range(1, len(arr)):
        current_rock_minerals = set(arr[i])
        common_minerals = common_minerals & current_rock_minerals
    return len(common_minerals)
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    print(result)