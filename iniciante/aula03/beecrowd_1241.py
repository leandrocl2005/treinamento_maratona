n = int(input())

for _ in range(n):
    primeiro, segundo = input().split()
    ind = -len(segundo)
    if primeiro[ind:] == segundo:
        print("encaixa")
    else:
        print("nao encaixa")
