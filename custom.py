def customerOrder(orders):
    result = []
    for i in range(len(orders)):
        total = orders[i][0] + orders[i][1]
        result.append([total, i + 1])
    result.sort()
    answer = []
    for item in result:
        answer.append(item[1])
    return answer
n = int(input())
orders = []
for i in range(n):
    order = int(input())
    prep = int(input())
    orders.append([order, prep])
print(*customerOrder(orders))