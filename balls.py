def organizingContainers(container):
    return "Possible" if sorted(map(sum, container)) == sorted(map(sum, zip(*container))) else "Impossible"
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        container = [list(map(int, input().rstrip().split())) for _ in range(n)]
        print(organizingContainers(container))