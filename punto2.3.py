# El código es del RETO 6, PUNTO 6
#Mensaje contextualizador de lo que hace el programa
print("Ingrese el número de contagiados actuales de Covid-19 en NuncaLandia y un número de días para calcular cuantos habrá en un futuro dependiendo de los contagiados actuales")
#Hacemos la función para hacer el cálculo
#Ponemos el caso para las funciones no definidas
def calcularAproximacionContagiadosNuncalandia(*args) -> int:
    aproximacionContagiadosNuncalandia = c*(2**d)
    return aproximacionContagiadosNuncalandia
#Ahora declaramos y inicializamos a las variables
if __name__ == "__main__":
    c:int=int(input("Ingrese el número de actuales contagiados en Nuncalandia: "))
    d:int=int(input("Ingrese el número de días apartir de hoy que se va a analizar: "))
    print("El número de contagiados en Nuncalandia será de", str(calcularAproximacionContagiadosNuncalandia(c,d)), "teniendo en cuenta los días a partir de hoy.")