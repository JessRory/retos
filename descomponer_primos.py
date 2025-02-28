"""append() agrega un elemento tal cual a la lista (lo que crea listas anidadas si el elemento es otra lista).
+= extiende la lista actual con los elementos de otra lista (lo que queremos en este caso)."""

def des_num_prim(numero):
    
    lista_primos = []

    if numero == 1:
        
        lista_primos.append(numero)

    elif numero % 2 == 0:
        
        # Usamos // para obtener un número entero:
        valor = numero // 2  
        
        lista_primos.append(2)
        
         # Concatenamos el resultado de la recursión:
        lista_primos += des_num_prim(valor)  # Concatenamos el resultado de la recursión
        
    elif numero % 3 == 0:
        
        valor = numero // 3
        
        lista_primos.append(3)
        
        lista_primos += des_num_prim(valor)
        
    elif numero % 5 == 0:
        
        valor = numero // 5
        
        lista_primos.append(5)
        
        lista_primos += des_num_prim(valor)
        
    else:
        
        print('Comando inválido')

    return lista_primos

# Prueba
numeros_primos = des_num_prim(70)
print(numeros_primos)  # Salida esperada: [2, 2, 2]


