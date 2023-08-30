from functools import reduce

n = int(input())

Q = map(int, input().split())
N = map(int, input().split())

sQ = sorted(Q)
sN = sorted(N)

ganha = 0


def ganhaN(i):
    global ganha
    if sQ[ganha] < sN[i]:
        ganha += 1
        return True
    return False


print(reduce(lambda x, y: x + 1, filter(ganhaN, range(0, n)), 0))
