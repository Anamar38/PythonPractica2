# Función principal 
def validar_numero_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True

# Solicitamos al usuario un número 
numero = int(input("Ingrese un número: "))

# Llamamos a la función y mostramos el resultado
if validar_numero_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

