lista_numeros = []

for _ in range(100):  # 0, 1, 2, 3
    numero = int(input())
    lista_numeros.append(numero)

maior = max(lista_numeros)
posicao = lista_numeros.index(maior)

print(maior)
print(posicao + 1)
