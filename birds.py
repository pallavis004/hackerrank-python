def migratoryBirds(arr):
    counts = {}
    for bird in arr:
        counts[bird] = counts.get(bird, 0) + 1
    max_count = max(counts.values())
    candidates = [bird for bird, c in counts.items() if c == max_count]
    return min(candidates)
if __name__ == "__main__":
    print(migratoryBirds([1, 4, 4, 4, 5, 3]))  