#El primer punto al cual lo vamos a desarrollar en lambda es el que se desarrolló en el RETO 6, PUNTO 5
#Mensaje contextualizador de lo que hace el programa
print("Ingrese el capital que se le prestará al cliente, el interés del prestamo  que será MENSUAL y el tiempo en el que se pagará en MESES")
#En la función main crearemos el la función lambda
if __name__ == "__main__":
    c:float=float(input("Ingrese el capital que se le prestará al cliente: "))
    i:float=float(input("Ingrese el interes mensual del prestamo: ")) # Acá cambié el código que hice en el Reto 6, antes sólo se podían poner valores de 0 a 1, ahora cualquier valor. ya que en la ecuación el porcentaje lo saco dividiendo i/100
    n:int=int(input("Ingrese el número de meses del prestamo: "))
    valorPrestamo = (lambda x, y, z : x*((1+(y/100))**z))(c, i, n) #Acá creamos el lambda y hacemos que x = c, y = i, z = n
    print("El valor del prestamo que usted deberá tener pagado al finalizar el prestamos es de", str(valorPrestamo)) # Si imprimimos nos dará el resultado dependiendo de los valores que se ingresaron