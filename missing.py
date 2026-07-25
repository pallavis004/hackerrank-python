def missingNumbers(arr, brr):
    count_arr = {}
    count_brr = {}
    for num in arr:
        count_arr[num] = count_arr.get(num, 0) + 1
    for num in brr:
        count_brr[num] = count_brr.get(num, 0) + 1
    answer = []
    for num in sorted(count_brr):
        if count_arr.get(num, 0) != count_brr[num]:
            answer.append(num)
    return answer
arr = [7, 2, 5, 3, 5, 3]
brr = [7, 2, 5, 4, 6, 3, 5, 3]
print(missingNumbers(arr, brr))