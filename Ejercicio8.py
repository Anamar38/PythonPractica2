# Función principal 
def factorial_numero(numero):
    # Verificamos si el número es negativo
    if numero < 0:
         return "El factorial no está definido para números negativos"
    factorial = 1
    for i in range(1, numero+1):
         factorial = factorial * i
 
    return factorial

# Solicitamos al usuario un número 
numero = int(input("Ingrese un número: "))

# Llamamos a la función y mostramos el resultado
resultado_factorial = factorial_numero(numero)
print (f"El factorial de {numero} es: {resultado_factorial}")
