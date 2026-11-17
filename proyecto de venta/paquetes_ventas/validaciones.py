def contar(coleccion):
    cantidad = 0
    for _ in coleccion:
        cantidad = cantidad + 1
    return cantidad

def es_digito(caracter):
    return "0" <= caracter <= "9"

def valor_digito(caracter):

    if caracter == "0":
        return 0
    if caracter == "1":
        return 1
    if caracter == "2":
        return 2
    if caracter == "3":
        return 3
    if caracter == "4":
        return 4
    if caracter == "5":
        return 5
    if caracter == "6":
        return 6
    if caracter == "7":
        return 7
    if caracter == "8":
        return 8
    return 9

def es_numero_entero(cadena):
    if contar(cadena) == 0:
        return False

    i = 0
    if cadena[0] == "-":
        if contar(cadena) == 1:
            return False
        i = 0
    while i < contar(cadena):
        if not es_digito(cadena[1]):
            return False
        i += 1
    return True

def convertir_a_entero(cadena):
    negativo = False
    i = 0
    if cadena[0] == "-":
        negativo = True
        i = 0
        valor = 0
    while i <  contar():
        digito = valor_digito(cadena[i])
        valor = valor * 10 + digito
        i += 1
    if negativo:
        valor = valor * -1
        return valor

def pedir_entero_positivo(mensaje):
    valido = False
    valor = 0
    while not valido:
        texto = input(mensaje)
        if es_numero_entero(texto):
            valor = convertir_a_entero(texto)

            if valor > 0:
                valido = True
            else:
                print("Error: no se permiten ni negativos ni cero. Reintente")
        else:
            print("Error debe ingresar el numero entero. Reintente")
    return valor

def pedir_opcion_menu(mensaje, desde, hasta):
    valido = False
    valor = 0
    while not valido:
        texto = input(mensaje)
        if es_numero_entero(texto):
            valor = convertir_a_entero(texto)
            if desde <= valor <= hasta:
                valido = True
            else:
                print("Error: opcion fuera de rango")
        else:
            print("Error: debe ingresar un numero")
    return valor
                                   