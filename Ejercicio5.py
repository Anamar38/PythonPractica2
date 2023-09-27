def contar_digitos(numero, digito):
    numero_str = str(numero)
    cantidad_de_veces = numero_str.count(str(digito))
    
    return cantidad_de_veces

# Solicitamos el número y el dígito
numero = int(input("Ingrese un número: "))
digito = int(input("Dígito a contar: "))

cantidad_de_veces = contar_digitos(numero, digito)
print(f"Cantidad de veces {digito} en el número: {cantidad_de_veces}")
