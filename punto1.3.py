#A este ejercicio le crearemos los lambdas. Es del RETO 6, PUNTO 1
#Con este código recibiremos el volumen y área superficial de una esfera y de un cono. Los valores de la esfera y el cono los ingresará usted
#importamos el paquete math para poder más adelante añadir el valor de pi a través de math.pi
import math
#Creamos una función main en la cula incluiremos lambda
if __name__ == "__main__":
    r1 : float = float(input("Ingrese el radio de la esfera: "))
    pi : float = math.pi
    r2 : float = float(input("Ingrese el radio del cono: "))
    h : float = float(input("Ingrese la altura del cono: "))
    volumen = (lambda x:(4/3)*(pi)*(x**2))(r1) #Este lambda será para el volumen de la esfera
    area = (lambda x:4*pi*(x**2))(r1) #Este lambda será para el área superficial de la esfera
    volumen1 = (lambda y, z: ((pi)*(y**2)*(z))/3)(r2, h) #Este lambda será para el volumen del cono
    generatriz = (lambda y, z:((z**2)+(y**2))**0.5)(r2, h) #Para el volumen del cono se necesita hallar la generatriz, para ello creamos otro lambda
    area1 = (lambda y:((pi)*(y**2)) + ((pi)*(y)*(generatriz)))(r2) #Este lambda será para el área del cono
    #Si imprimimos nos dará los respectivos resultados
    print("El volumen de la esfera es", str(volumen), "y el área superficial de la esfera es", str(area))
    print("El volumen del cono es", str(volumen1), "y el área superficial del cono es", str(area1))