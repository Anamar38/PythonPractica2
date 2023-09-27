def eliminar_vocales(cadena):
    # Cadena vacía para almacenar el resultado
    resultado = ""
    for caracter in cadena:
        if caracter.lower() not in "aeiou":
            resultado += caracter
    return resultado

# Solicitamos al usuario una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Llamamos a la función y mostramos el resultado
resultado = eliminar_vocales(cadena)
print("El texto sin vocales es: ", resultado)
