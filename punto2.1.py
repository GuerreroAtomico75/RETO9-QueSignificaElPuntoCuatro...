#A este programa se le añadirán los ARGUMENTOS NO DEFINIDOS, este es del Reto 6, Punto 4
#Mensaje contextualizador sobre el programa
print("Ingrese la cantidad de productos que va a comprar de panes, bolsas de leche y huevos. Te daremos el precio que tiene que pagar, se te informará de las vueltas o lo que quedas debiendo.")
#Crearemos un programa con las siguientes funciones
#Una función que me diga el precio dependiendo de el número de panes que compre
#Ponemos el *args1 en la función
def calcularPrecioPanes(*args1) -> int:
    precioPanes = 0
    for P in args1:
        precioPanes = P*valorPan
    return precioPanes
#Otra función que me diga el precio dependiendo del número de bolsas de leche que compre
#Ponemos el *args2 en la función
def calcularPrecioBolsasDeLeche(*args2) -> int:
    precioBolsasDeLeche = 0
    for M in args2:
        precioBolsasDeLeche= M*valorBolsasDeLeche
    return precioBolsasDeLeche
#Y por último una función que diga el precio dependiendo del número de huevos que compre
#Ponemos el *args3 en la función
def calcularPrecioHuevo(*args3) -> int:
    precioHuevos = 0
    for H in args3:
        precioHuevos = H*valorHuevo
    return precioHuevos
#Ahora declaramos e inicializamos variables, haciendo la suma entre los resultados de las funciones
#las funciones no definidas ya no están en la función main
if __name__ == "__main__":
    P:int=int(input("Ingrese el numero de panes que comprará: "))
    M:int=int(input("Ingrese el numero de bolsas de leche que comprará: "))
    H:int=int(input("Ingrese el numero de huevos que comprará: "))
    valorPan:int=300
    valorBolsasDeLeche:int=3300
    valorHuevo:int=350
    #El ejercicio habla de poner las funciones args, solo se habían creado las funciones para los precios individuales con lo cual cuando hago la suma de todos los precios dan es la unión de los valores de las tuplas.
    valorTotal = str(calcularPrecioPanes(P)) + str(calcularPrecioBolsasDeLeche(M)) + str(calcularPrecioHuevo(H))
    print("El precio de los panes en función del número de panes que comprará es de", str(calcularPrecioPanes(P)),"pesos.")
    print("El precio de las bolsas de leche en función del número de bolsas de leche que comprará es de", str(calcularPrecioBolsasDeLeche(M)),"pesos.")
    print("El precio de los huevos en función del número de huevos que comprará es de", str(calcularPrecioHuevo(H)),"pesos.")
    print("El valor total que debe pagar es de", str(valorTotal),"pesos")
    dineroIngresado:int=int(input("Ingrese dinero con el que pagará: "))
    if dineroIngresado > valorTotal:
        vueltas = dineroIngresado - valorTotal
        print("Las vueltas de su compra son", str(vueltas), "pesos")
    elif dineroIngresado < valorTotal:
        debe = valorTotal - dineroIngresado
        print("No ingresó el dinero total que debía, queda debiendo", str(debe), "pesos")
    else:
        print("¡Gracias por su compra!")