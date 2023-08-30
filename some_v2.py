import string
from functools import reduce

# some os números
# some os quadrados dos números
entrada = "A T 5 T a 3 10 O P P 0 5 2 1"

resultado = reduce(
    lambda x, y: x + y,
    map(
        int,
        filter(
            lambda item: item not in string.ascii_letters,
            entrada.split()
        )
    ),
    0
)

print(resultado)
