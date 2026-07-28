def maximumToys(prices, k):
    prices.sort()
    count = 0
    total = 0
    for price in prices:
        if total + price <= k:
            total = total + price
            count = count + 1
        else:
            break
    return count
n = int(input("Enter number of toys: "))
k = int(input("Enter budget: "))
prices = list(map(int, input("Enter toy prices: ").split()))
print("Maximum toys:", maximumToys(prices, k))