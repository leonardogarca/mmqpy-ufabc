from mmq import mmqpy
from sys import argv

csv = False

try:
    if argv[1].endswith(".csv"):
        csv = argv[1]
except IndexError:
    print("Sem CSV. Vai ter que digitar cada valor um por um")

x = []
y = []
yinc = []

if csv:
    import pandas as pd
    df = pd.read_csv(csv)
    x = df["x"]
    y = df["y"]
    yinc = df["sigmay"]

else:
    print("digite os valores de x ou 'Q' quando terminar: ", end = "")
    while True:
        inp = input()
        if inp == 'Q':
            break
        else:
            x.append(float(inp))

    count = len(x)

    print("digite os valores de y: ", end = "")
    for i in range(count):
        inp = input()
        y.append(float(inp))

    print("digite a incerteza de cada valor de y: ", end = "")
    for i in range(count):
        inp = input()
        yinc.append(float(inp))

resultado = mmqpy(x, y, yinc)

print("o valor do coeficiente angular (a) é: "+ str(resultado[0]) + " +- " + str(resultado[1]))
print("o valor do coeficiente linear (b) é: " + str(resultado[2]) + " +- " + str(resultado[3]))