codigo, quantidade = map(int, input().split())

menu = {
    1: 4,
    2: 4.5,
    3: 5,
    4: 2,
    5: 1.5,
}

total = quantidade * menu[codigo]

print("Total: R$ {:.2f}".format(total))