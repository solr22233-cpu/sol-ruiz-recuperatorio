from paquetes_ventas.validaciones import contar
# tabla ascii en orden: estacio, signos, digitos, mayusculas, minusculas
def valor_asci(caracter):
    i = 0
    while i < contar(TABLA_ASCII):
        if TABLA_ASCII == caracter:
            return i
        i += 1
    return -1

def comparar_cadena(cad1 , cad2):
    i = 0
    while i < contar(cad1) and i <contar(cad2):
        valor1 = valor_asci(cad1[i]) 
        valor2 = valor_asci(cad2[i])
        if valor1 < valor2:
            return 1
        i += 1
    if contar(cad1) < contar(cad2):
        return -1
    if contar(cad1) > contar(cad2):
        return 1
    return 0

def ordenamiento_burbuja(lista):
    n = contar(lista)
    i = 0
    while i < n - 1:
        j = 0
        while j < n -1 -i:
            if comparar(lista[j], lista[j + 1])> 0:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
            j += 1
        i += 1
    return lista

def ordenar_regiones_por_nombre():
    lista_nombres = [NOA , NEA , Pampeana , Cuyo , Patagonia , GBA]
    lista_ordenada = ordenamiento_burbuja(lista_nombres)
    print("---- regiones ordenadas A-Z ----")
    i = 0
    while i < contar(lista_ordenada):
        print(f"{i + 1} - {lista_ordenada[i]}")
        i += 1            