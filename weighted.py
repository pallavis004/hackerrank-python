def weightedUniformStrings(s, queries):
    weights = set()
    current_weight = 0
    previous = ""
    for letter in s:
        value = ord(letter) - ord('a') + 1
        if letter == previous:
            current_weight += value
        else:
            current_weight = value
        weights.add(current_weight)
        previous = letter
    answer = []
    for number in queries:
        if number in weights:
            answer.append("Yes")
        else:
            answer.append("No")
    return answer
if __name__ == '__main__':
    s = input()
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = weightedUniformStrings(s, queries)
    print(result)