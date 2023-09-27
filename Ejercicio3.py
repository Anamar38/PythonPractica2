numeros_pares = 0
numeros_impares = 0
lista_numeros= []

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ")
    if respuesta.upper() == 'NO':
        break
    elif respuesta.upper() == 'SI':
        try:
            numero = int(input("Ingrese el número: "))
            lista_numeros.append(numero)
            #verificamos la condicion
            if numero % 2 == 0:
                numeros_pares += 1
            else:
                numeros_impares += 1
        except ValueError:
            print("Entrada no válida. Ingrese un número entero válido.")
    else:
        print("Respuesta inválida. Responda 'SI' o 'NO'.")

# Mostramos los números ingresados
print(f"Números ingresados: {lista_numeros}")

# Mostramos el resultado
print(f"Cantidad de números pares: {numeros_pares}")
print(f"Cantidad de números impares: {numeros_impares}")
