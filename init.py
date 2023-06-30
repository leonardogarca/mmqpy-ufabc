from mmq import mmqpy

x = []
print("digite os valores de x ou 'Q' quando terminar: ", end = "")
while True:
    inp = input()
    if inp == 'Q':
        break
    else:
        x.append(float(inp))

count = len(x)

y = []
print("digite os valores de y: ", end = "")
for i in range(count):
    inp = input()
    y.append(float(inp))

yinc = []
print("digite a incerteza de cada valor de y: ", end = "")
for i in range(count):
    inp = input()
    yinc.append(float(inp))

resultado = mmqpy(x, y, yinc)

print("o valor de a é: "+ str(resultado[0]) + " +- " + str(sresultado[1]))
print("o valor de b é: " + str(resultado[2]) + " +- " + str(resultado[3]))