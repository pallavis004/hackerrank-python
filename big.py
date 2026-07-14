def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))
if __name__ == '__main__':
    unsorted = ['1', '200', '150', '3']
    print(bigSorting(unsorted))