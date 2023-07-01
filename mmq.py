def mmqpy(x, y, yinc):
    """Calcula a reta de tendencia pelo MMQ
    
    Parametros
    ----------
    x : List
        Lista com os valores do eixo X
    y : List
        Lista com os valores do eixo Y
    yinc : List
        Lista com os valores da incerteza dos pontos no eixo Y
    
    Saída
    -----
    List
        Lista seguindo o formato
        [coeficiente angular,
        incerteza do coeficiente angular,
        coeficiente linear,
        incerteza do coeficiente linear]
    """
    
    count = len(x)
    
    inc2 = 0
    for i in range(count):
        inc2 += divsupersegura(1,(yinc[i]**2))
    
    _x = 0
    for i in range(count):
        _x += divsupersegura(x[i],(yinc[i]**2))
    _x = _x / inc2

    _x2 = 0
    for i in range(count):
        _x2 += divsupersegura((x[i]**2),(yinc[i]**2))
    _x2 = _x2 / inc2

    _y = 0
    for i in range(count):
        _y += divsupersegura((y[i]),(yinc[i]**2))
    _y = _y / inc2

    xy = 0
    for i in range(count):
        xy += divsupersegura((x[i]*y[i]),(yinc[i]**2))
    xy = xy / inc2

    a = divsupersegura(((_x * _y)- xy),((_x**2)-_x2))
    b = _y - (a*_x)

    inca = divsupersegura((1/inc2),(_x2 - _x**2))**0.5
    incb = divsupersegura((_x2/inc2),(_x2 - _x**2))**0.5

    return [a, inca, b, incb]

def divsupersegura(a, b):
    """Divisão que retorna 0 se o denominador for 0"""
    return a/b if b != 0 else 0

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

print("O valor do coeficiente angular (a) é: "+ str(resultado[0]) + " +- " + str(resultado[1]))
print("O valor do coeficiente linear (b) é: " + str(resultado[2]) + " +- " + str(resultado[3]))