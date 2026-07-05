def bonAppetit(bill, k, b):
    total = sum(bill) - bill[k]
    fair_share = total // 2
    if fair_share == b:
        print("Bon Appetit")
    else:
        print(b - fair_share)
if __name__ == "__main__":
    bonAppetit([3, 10, 2, 9], 1, 12)