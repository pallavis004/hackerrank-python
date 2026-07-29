def checkArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"
n = int(input("Enter number of elements: "))
k = int(input("Enter k value: "))
A = list(map(int, input("Enter elements of A: ").split()))
B = list(map(int, input("Enter elements of B: ").split()))
result = checkArrays(k, A, B)
print("Answer:", result)