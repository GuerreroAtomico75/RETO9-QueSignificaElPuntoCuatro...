#El primer punto al cual lo vamos a desarrollar en lambda es el que se desarrolló en el RETO 6, PUNTO 3
#Mensaje contextulizador sobre el programa
print("Dinos el número de gallinas, gallos y/o pollitos que tienes y te diremos cuanta carne te llevaras de cada uno")
#Crearemos lambda en la función main. En total se crearán tres lambdas. El valor del peso no lo cambiamos por ende si sigue en el ejercicio como una variable. 
if __name__ == "__main__":
    N:int=int(input("Ingrese el numero de gallinas que tiene: "))
    M:int=int(input("Ingrese el numero de gallos que tiene: "))
    K:int=int(input("Ingrese el numero de pollitos que tiene: "))
    pG:float=6
    pGallo:float=7
    pP:float=1
# Creamos onas variables que se identificarán con las variables de los valores ingresados. Estas variables son x, y, z.
    carneGallina = (lambda x : x*pG)(N)
    carneGallo = (lambda y :y*pGallo)(M)
    carnePollito = (lambda z: z*pP)(K)
    #Al imprimir nos da los resultados deseados
    print("La cantidad de carne de gallina en función del número de gallinas que tenía es de", str(carneGallina),"Kg")
    print("La cantidad de carne de gallo en función del número de gallos que usted tenía es de", str(carneGallo),"Kg")
    print("La cantidad de carne de pollo en función del número de pollitos que usted tenía es de", str(carnePollito),"Kg")