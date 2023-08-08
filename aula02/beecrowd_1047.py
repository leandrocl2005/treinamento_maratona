hi, mi, hf, mf = map(int, input().split())

if (hi == hf) and (mi <= mf):
    horas = 24
    minutos = mf - mi
elif (hi == hf) and (mi > mf):
    horas = 23
    minutos = 60 - (mi - mf)

elif (hi < hf) and (mi <= mf):
    horas = hf - hi
    minutos = mf - mi

elif (hi < hf) and (mi > mf):
    horas = hf - hi - 1
    minutos = 60 - mi + mf

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
