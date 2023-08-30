maior = -1
posicao = -1
contador = 1

while True:
    try:
        numero = int(input())
        if numero >= maior:
            maior = numero
            posicao = contador
        contador += 1
    except EOFError:
        break

print(maior)
print(posicao)
