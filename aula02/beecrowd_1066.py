pares = 0
impares = 0
positivos = 0
negativos = 0

a = int(input())
if a % 2 == 0:
    pares += 1
else:
    impares += 1
if a > 0:
    positivos += 1
elif a < 0:
    negativos += 1

a = int(input())
if a % 2 == 0:
    pares += 1
else:
    impares += 1
if a > 0:
    positivos += 1
elif a < 0:
    negativos += 1

a = int(input())
if a % 2 == 0:
    pares += 1
else:
    impares += 1
if a > 0:
    positivos += 1
elif a < 0:
    negativos += 1

a = int(input())
if a % 2 == 0:
    pares += 1
else:
    impares += 1
if a > 0:
    positivos += 1
elif a < 0:
    negativos += 1

a = int(input())
if a % 2 == 0:
    pares += 1
else:
    impares += 1
if a > 0:
    positivos += 1
elif a < 0:
    negativos += 1

print("{} valor(es) par(es)".format(pares))
print("{} valor(es) impar(es)".format(impares))
print("{} valor(es) positivo(s)".format(positivos))
print("{} valor(es) negativo(s)".format(negativos))
