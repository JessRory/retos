"""append() agrega un elemento tal cual a la lista (lo que crea listas anidadas si el elemento es otra lista).
+= extiende la lista actual con los elementos de otra lista (lo que queremos en este caso)."""

def numero_primo(num):
    # Función para verificar si un número es primo
    for n in range(2, num):
        if num % n == 0:
            return False
    print(f'El número {num} es primo')
    return True

def des_num_prim(numero, llamada=True):
    lista_primos = []

    # Solo verificamos si es primo en la primera llamada
    if llamada and numero_primo(numero):
        print('Por lo tanto, sólo es divisible entre uno y sí mismo.')
        return [numero, 1]

    # Factorización en números primos
    if numero == 1:
        return [1]

    # Chequeo de múltiplo de 7 basado en las cifras
    cifras = [int(num) for num in str(numero)]
    if len(cifras) > 1:  # Aseguramos que hay al menos dos cifras para evitar errores
        primer_numero = cifras[0]
        resto_numero = cifras[1]
        if (primer_numero * 2) - resto_numero == 0 or (((primer_numero * 2) - resto_numero) % 7) == 0:
            lista_primos.append(7)
            numero //= 7  # Dividimos el número por 7 si es múltiplo

    # Factorización de 2, 3, 5 y otros números
    if numero % 2 == 0:
        valor = numero // 2
        lista_primos.append(2)
        lista_primos += des_num_prim(valor, False)

    elif numero % 3 == 0:
        valor = numero // 3
        lista_primos.append(3)
        lista_primos += des_num_prim(valor, False)

    elif numero % 5 == 0:
        valor = numero // 5
        lista_primos.append(5)
        lista_primos += des_num_prim(valor, False)

    # Comprobación de otros factores primos mayores
    divisor = 7
    while divisor * divisor <= numero:  # Solo probamos hasta la raíz cuadrada del número
        while numero % divisor == 0:
            lista_primos.append(divisor)
            numero //= divisor
        divisor += 2  # Probamos los números impares (ya hemos probado 2, 3, 5)

    # Si queda un número primo mayor que 1, lo agregamos
    if numero > 1:
        lista_primos.append(numero)

    return lista_primos

# Prueba
numeros_primos = des_num_prim(1974)
numeros_primos.sort(reverse=True)
print(numeros_primos)



