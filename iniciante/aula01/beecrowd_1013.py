A, B, C = list(map(int, input().split()))

maiorAB = (A + B + abs(A - B)) // 2
maiorABC = (maiorAB + C + abs(maiorAB - C)) // 2

print(f"{maiorABC} eh o maior")
