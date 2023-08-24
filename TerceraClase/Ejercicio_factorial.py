def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
numero = factorial(4)
print("El resultado del factorial es: ",numero)