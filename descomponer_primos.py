"""append() agrega un elemento tal cual a la lista (lo que crea listas anidadas si el elemento es otra lista).
+= extiende la lista actual con los elementos de otra lista (lo que queremos en este caso)."""


def numero_primo(num):
    
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
    
    elif numero % 2 == 0:
        
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

    #else:
        #print('Comando inválido')

    return lista_primos

# Prueba
numeros_primos = des_num_prim(444)
print(numeros_primos)



