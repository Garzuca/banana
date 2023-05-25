# validar numero positivo
def validar_num_posi(num):
    while num <= 0:
        num = int(input("por favor vuelve a ingresar el numero"))
    return num


# funcion para validar digitos
def contar_digitos(numero):
    return len(str(numero))


# contar n digitos
def validar_digitos(numero):
    while numero <= 0 and numero >= 999:
        numero = int(input("ingrese un numero de 3 digitos: "))
    contador = 0
    while numero != 0:
        n = numero // 10
        dig = numero % 10
        contador += 1
    return contador


# definir rango
def validar_rango(num, minimo, maximo):
    if num >= minimo and num <= maximo:
        return True
    else:
        return False


# definir si un numero es primo
def validar_num_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero / 2) + 1):
        if numero % i == 0:
            return False
    return True


# cuadrado perfecto
def validar_num_cuadrado(numero):
    raiz = int(numero**0.5)
    if raiz * raiz == numero:
        return True
    else:
        return False


# divisible entre otro
def validar_num_divisible(numero, divisor):
    try:
        numero = int(numero)
        if numero % divisor == 0:
            return True
        else:
            return False
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return False


# programa principal
