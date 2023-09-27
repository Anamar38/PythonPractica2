altura = int(input('Ingresa la aultura de los triangulos: '))
# Parte superior del patrón 
for i in range(1, altura + 1):
    for j in range(i):
        print("*", end=" ")
    print()
# Parte inferior del patrón
for i in range(altura - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()