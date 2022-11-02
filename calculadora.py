from math import sqrt


def secondDegreeEcuation(a, b, c):
    raiz = b ** 2 - 4 * a * c
    if raiz < 0:
        print("No tiene solución real")
        return None, None
    else:
        x1 = (-b + sqrt(raiz)) / (2 * a)
        x2 = (-b - sqrt(raiz)) / (2 * a)

        return x1, x2


a = int(input("Introduce un valor: "))
b = int(input("Introduce un valor: "))
c = int(input("Introduce un valor: "))

x1, x2 = secondDegreeEcuation(a, b, c)

print(x1, x2)
