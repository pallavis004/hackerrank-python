import bisect
def climbingLeaderboard(ranked, player):
    uniq = sorted(set(ranked))
    result = []
    for score in player:
        pos = bisect.bisect_right(uniq, score)
        result.append(len(uniq) - pos + 1)
    return result
if __name__ == '__main__':
    n = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    for result in climbingLeaderboard(ranked, player):
        print(result)