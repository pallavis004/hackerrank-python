def introTutorial(V, arr):
    return len([x for x in arr if x < V])
if __name__ == '__main__':
    V = 4
    arr = [1, 3 , 5 ,7]
    print(introTutorial(V, arr))