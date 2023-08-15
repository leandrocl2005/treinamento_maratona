numero = int(input())
alcool = 0
gasolina = 0
diesel = 0

while numero != 4:
    if numero == 1:
        alcool += 1
    elif numero == 2:
        gasolina += 1
    elif numero == 3:
        diesel += 1
    numero = int(input())

print(f"MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
