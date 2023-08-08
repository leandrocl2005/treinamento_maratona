A, B, C = map(float, input().split())

A, B, C = sorted([A, B, C], reverse=True)

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if (A == B) and (B == C):
        print("TRIANGULO EQUILATERO")
    if (A == B) and (B != C):
        print("TRIANGULO ISOSCELES")
    if (A == C) and (B != C):
        print("TRIANGULO ISOSCELES")
    if (B == C) and (B != A):
        print("TRIANGULO ISOSCELES")