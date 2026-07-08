def designerPdfViewer(h, word):
    max_height = 0
    for letter in word:
        index = ord(letter) - ord('a')
        if h[index] > max_height:
            max_height = h[index]
    return max_height * len(word)


if __name__ == "__main__":
    h = list(map(int, input().rstrip().split()))
    word = input().rstrip()

    result = designerPdfViewer(h, word)
    print(result)
