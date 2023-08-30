n = int(input())

for _ in range(n):
    B, E = map(int, input().split())
    lista = "".join(map(str, range(B, E + 1)))
    print(lista + lista[::-1])
