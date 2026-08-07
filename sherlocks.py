def isValid(s):
    count = {}
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    frequencies = list(count.values())

    if len(set(frequencies)) == 1:
        return "YES"
    for i in range(len(frequencies)):
        frequencies[i] -= 1

        new_list = []

        for value in frequencies:
            if value > 0:
                new_list.append(value)

        if len(new_list) > 0 and len(set(new_list)) == 1:
            return "YES"
        frequencies[i] += 1
    return "NO"
s = input("Enter the string: ")
print(isValid(s))