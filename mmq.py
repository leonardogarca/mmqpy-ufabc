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

inc2 = 0
for i in range(count):
    inc2 += 1/(yinc[i]**2)

_x = 0
for i in range(count):
    _x += x[i]/(yinc[i]**2)
_x = _x / inc2

_x2 = 0
for i in range(count):
    _x2 += (x[i]**2)/(yinc[i]**2)
_x2 = _x2 / inc2

_y = 0
for i in range(count):
    _y += (y[i])/(yinc[i]**2)
_y = _y / inc2

xy = 0
for i in range(count):
    xy += (x[i]*y[i])/(yinc[i]**2)
xy = xy / inc2

a = ((_x * _y)- xy)/((_x**2)-_x2)
b = _y - (a*_x)

inca = ((1/inc2)/(_x2 - _x**2))**0.5
incb = ((_x2/inc2)/(_x2 - _x**2))**0.5

print("o valor de a é: "+ str(a) + " +- " + str(inca))
print("o valor de b é: " + str(b) + " +- " + str(incb))