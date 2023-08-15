for i in range(11):
    number_I = round(0.2 * i, 1)
    if i % 5 == 0:
        number_I = int(number_I)
    for j in range(3):
        number_J = j + number_I + 1
        print(f"I={number_I} J={number_J}")
