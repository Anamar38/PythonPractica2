def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_serie = [0, 1]
        while len(fibonacci_serie) < n:
            siguiente_numero = fibonacci_serie[-1] + fibonacci_serie[-2]
            if siguiente_numero <= 50:
                fibonacci_serie.append(siguiente_numero)
            else:
                break
        return fibonacci_serie
serie_fibonacci = fibonacci(50)

# Imprimimos la serie de Fibonacci
print("Serie de Fibonacci entre 0 y 50:")
print(serie_fibonacci)
