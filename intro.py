def introTutorial(V, arr):
    return len([x for x in arr if x < V])
if __name__ == '__main__':
    V = 3
    arr = [1, 2 , 3 ]
    print(introTutorial(V, arr))