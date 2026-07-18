from itertools import combinationspython
def acmTeam(topic):
    counts = [bin(int(a, 2) | int(b, 2)).count('1') for a, b in combinations(topic, 2)]
    m = max(counts)
    return [m, counts.count(m)]
if __name__ == '__main__':
    n, m = map(int, input().split())  # n = number of people, m = number of topics
    topic = []
    for _ in range(n):
        topic.append(input().strip())
    result = acmTeam(topic)
    print(result[0])
    print(result[1])