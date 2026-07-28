def decentNumber(n):
    five_count = n
    while five_count >= 0:
        three_count = n - five_count
        if five_count % 3 == 0 and three_count % 5 == 0:
            print("5" * five_count + "3" * three_count)
            return
        five_count = five_count - 5
    print(-1)
n = int(input("Enter number of digits: "))
decentNumber(n)