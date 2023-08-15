maior = -1
posicao = -1
contador = 1

while contador < 100:
    numero = int(input())
    if numero >= maior:
        maior = numero
        posicao = contador
    contador += 1

print(maior)
print(posicao)
