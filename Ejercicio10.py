# Lista de nombres de meses
meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]

def convertir_fecha(fecha):
    # Dividir la fecha en palabras
    palabras = fecha.split()
    
    # Si la fecha tiene 3 palabras (mes día, año)
    if len(palabras) == 3:
        mes_str, dia, año = palabras
    # Si la fecha tiene 3 elementos separados por "/"
    elif fecha.count("/") == 2:
        mes_str, dia, año = fecha.split("/")
    else:
        return "Formato de fecha no válido"
    
    # Obtener el número de mes a partir del nombre del mes
    if mes_str in meses:
        mes = meses.index(mes_str) + 1
    else:
        return "Nombre de mes no válido"
    
    # Formatear la fecha en AAAA-MM-DD
    fecha_formateada = f"{año}-{mes:02d}-{dia:02d}"
    
    return fecha_formateada

# Solicitar al usuario una fecha
fecha_input = input("Ingrese una fecha en formato mes-día-año o 'mes día, año': ")

# Llamar a la función convertir_fecha y mostrar el resultado
fecha_convertida = convertir_fecha(fecha_input)

if fecha_convertida != "Formato de fecha no válido" and fecha_convertida != "Nombre de mes no válido":
    print("Fecha en formato AAAA-MM-DD:", fecha_convertida)
else:
    print("Formato de fecha no válido o nombre de mes incorrecto.")
