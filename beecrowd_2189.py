n = int(input())
contador = 0

while n != 0:
    contador += 1
    ingressos = map(int, input().split())

    sorteado = -1
    for i, j in enumerate(ingressos):
        if i + 1 == j:
            sorteado = j
            break
    print(f"Teste {contador}")
    print(sorteado)
    print()
    n = int(input())
