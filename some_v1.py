import string

# some os números
# some os quadrados dos números
entrada = "A T 5 T a 3 10 O P P 0 5 2 1"

lista = entrada.split()

soma = 0
for item in lista:
    if item not in string.ascii_letters:
        item = int(item)
        soma += item

print(soma)
