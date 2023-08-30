maior = -1
posicao = -1

for i in range(100):  # 0, 1, 2, 3
    numero = int(input())
    if numero >= maior:
        maior = numero
        posicao = i + 1

print(maior)
print(posicao)
