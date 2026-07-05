def pageCount(n, p):
    front = p // 2
    back = n // 2 - p // 2
    return min(front, back)
if __name__ == "__main__":
    print(pageCount(6, 2))