from functools import reduce

lista = [1,2,3,4,5,6,7]

print(reduce(lambda x,y: x+1, lista, 0))