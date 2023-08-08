A, B, C, D = map(int, input().split())

# Variáveis booleanas
# True, False

vale_condicao = (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (
    D > 0) and (A % 2 == 0)

if vale_condicao:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
