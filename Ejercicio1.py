
lista_numeros = []
# Iteramos a través del rango 
for numero in range(1500, 2701):
    # Verificamos si el número es divisible por 7 y múltiplo de 5
    if numero % 7 == 0 and numero % 5 == 0:
        lista_numeros.append(numero)
# Imprimimos la lista de números que cumplen con las condiciones
print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(lista_numeros)
