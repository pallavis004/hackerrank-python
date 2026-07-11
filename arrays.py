from collections import Counter
def equalizeArray(arr):
    return len(arr) - max(Counter(arr).values())
if __name__ == '__main__':
    n = int(input())          
    arr = list(map(int, input().split()))  
    result = equalizeArray(arr)
    print(result)