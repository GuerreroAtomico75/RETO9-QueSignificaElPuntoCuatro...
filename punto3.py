#Caso de función recursiva de una potencia
def funcionRecursivaPotencia(n : float, e: int) -> float:
    #Estos son los casos base:
    if n == 1 or n == 0:
        return n
    elif e == 0:
        return 1
    #El caso recursivo es el siguiente:
    else:
        pot = n**e
        return pot

# Hacemos función main
if __name__ == "__main__":
    #Pedimos que ingresen datos
    n = float(input("Ingrese la base: "))
    e = int(input("Ingrese un exponente: "))
    potencia = funcionRecursivaPotencia(n, e)
    print("El resultado de", n, "elevado a la", e, "es", str(potencia)) #Imprimimos el resultado