import math
def is_smart_number(num):
    val = int(math.sqrt(num))
    if val * val == num:
        return True
    return False
t = int(input("Enter number of test cases: "))
for i in range(t):
    num = int(input("Enter a number: "))
    result = is_smart_number(num)
    if result:
        print("YES")
    else:
        print("NO")