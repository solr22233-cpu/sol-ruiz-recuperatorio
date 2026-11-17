from paquetes_ventas.validaciones import contar

def sumar_vector(vector):
    total = 0
    i = 0
    while i < contar(vector):
        total = total + vector [i]
        i += 1
        return total

def calcular_promedio(vector):
    if contar(vector) == 0:
        return 0
    return sumar_vector / contar(vector)

def calcular_porsentaje(parte, total):
    if  total == 0:
        return 0
    return parte * 100/total

def buscar_mayor(vector):
    mayor = vector[0]
    i = 1
    while i < contar(vector):
        if vector[i] > mayor :
            mayor = vector [i]
        i += 1
    return mayor
            