# RETO9-QueSignificaElPuntoCuatro...
#### Problemas planteados
##### 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
###### Solución
###### * Primera función
La primera función que cambié a lambda fue la de *Reto 6, punto 5*.
  * Antes de aplicar lambda:
    ```
    #Mensaje contextualizador de lo que hace el programa
    print("Ingrese el capital que se le prestará al cliente, el interés del prestamo  que será MENSUAL y el tiempo en el que se pagará en MESES")
    #Hacemos la función para hacer el cálculo
    def calcularValorDelPrestamo(c:float, i:float, n:int) -> float:
        valorDelPrestamo = c*((1+i)**n)
        return valorDelPrestamo
    #Ahora declaramos y inicializamos a las variables
    if __name__ == "__main__":
        c:float=float(input("Ingrese el capital que se le prestará al cliente: "))
        i:float=float(input("Ingrese el interes mensual del prestamo, tenga en cuenta que SOLO podrá ingresar valores  de 0 a 1: "))
        if 0 <= i <=1:
            print("Gracias por darnos el interes con las condiciones establecidas")
        else:
            print("Ingrese un valor para el interés con las condiciones establecidas")
        n:int=int(input("Ingrese el número de meses del prestamo: "))
        valorPrestamo = calcularValorDelPrestamo(c, i, n)
        print("El valor del prestamo que usted deberá tener pagado al finalizar el prestamos es de", str(valorPrestamo))
    ```

  * Después de lambda
    ```
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
    ```
---
###### * Segunda Función
La segunda función que cambié a lambda fue la de *Reto 6, punto 3*.
  * Antes de aplicar lambda
    ```
    #Mensaje contextulizador sobre el programa
    print("Dinos el número de gallinas, gallos y/o pollitos que tienes y te diremos cuanta carne te llevaras de cada uno")
    #Para hacer este ejercicio crearemos tres funciones
    #Primero crearemos la función relacionada con las gallinas
    def calcularCantidadCarneGallina(N:int) -> float:
        cantidadCarneGallina = N*pesoGallina
        return cantidadCarneGallina
    #Después crearemos la función relacionada con los gallos
    def calcularCantidadCarneGallo(M:int) -> float:
        cantidadCarneGallo = M*pesoGallo
        return cantidadCarneGallo
    #Y por último crearemos la función relacionada con los pollitos
    def calcularCantidadCarnePollito(K:int) -> float:
        cantidadCarnePollito = K*pesoPollito
        return cantidadCarnePollito
    #Al tener las funciones procedemos a Declarar e inicializar las variables
    if __name__ == "__main__":
        N:int=int(input("Ingrese el numero de gallinas que tiene: "))
        M:int=int(input("Ingrese el numero de gallos que tiene: "))
        K:int=int(input("Ingrese el numero de pollitos que tiene: "))
        pesoGallina:float=6
        pesoGallo:float=7
        pesoPollito:float=1
        carneGallina = calcularCantidadCarneGallina(N)
        carneGallo = calcularCantidadCarneGallo(M)
        carnePollito = calcularCantidadCarnePollito(K)
        print("La cantidad de carne de gallina en función del número de gallinas que tenía es de", str(carneGallina),"Kg")
        print("La cantidad de carne de gallo en función del número de gallos que usted tenía es de", str(carneGallo),"Kg")
        print("La cantidad de carne de pollo en función del número de pollitos que usted tenía es de", str(carnePollito),"Kg")
    ```
  * Después de aplicar lambda
    ```
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
    ```
---
### Tercera Función
La tercera función que cambié a lambda fue la de *Reto 6, punto 1*.
  * Antes de lambda
    ```
    #importamos el paquete math para poder más adelante añadir el valor de pi a través de math.pi
    import math
    #La primera función que crearemos es la función para hallar el VOLUMEN de la ESFERA
    def calcularVolumenDeLaEsfera(r1:float) -> float:
        volumenDeLaEsfera = (4/3)*(pi)*(r1**2) #Esta es la formula para hallar el volumen de la esfera
        return volumenDeLaEsfera
    #Ahora calcularemos el ÁREA SUPERFICIAL de la ESFERA a tráves de la siguiente función
    def calcularAreaSuperficialDeLaEsfera(r1:float) -> float:
        areaSuperficialDeLaEsfera = 4*pi*(r1**2) #Ecuación de el área superficial
        return areaSuperficialDeLaEsfera
    #Ahora calcularemos el VOLUMEN del CONO a través de la siguiente función
    def calcularVolumenDelCono(r2:float, h:float) -> float:
        volumenDelCono = ((pi)*(r2**2)*(h))/3 #Formula para hallar el volumen del cono
        return volumenDelCono
    #Ahora calcularemos el ÁREA SUPERFICIAL del CONO a tráves de la siguiente función
    def calcularAreaSuperficialDelCono(r2:float, h:float) -> float:
        generatriz = ((h**2)+(r2**2))**0.5
        areaSuperficialDelCono = ((pi)*(r2**2)) + ((pi)*(r2)*(generatriz))
        return areaSuperficialDelCono
    #Ponemos las variables sin olvidarnos del math.pi para tener el valor de pi
    if __name__ == "__main__":
        r1 : float = float(input("Ingrese el radio de la esfera: "))
        pi : float = math.pi
        r2 : float = float(input("Ingrese el radio del cono: "))
        h : float = float(input("Ingrese la altura del cono: "))
        volumen = calcularVolumenDeLaEsfera(r1)
        area = calcularAreaSuperficialDeLaEsfera(r1)
        volumen1 = calcularVolumenDelCono(r2, h)
        area1 = calcularAreaSuperficialDelCono(r2, h)
        print("El volumen de la esfera es", str(volumen), "y el área superficial de la esfera es", str(area))
        print("El volumen del cono es", str(volumen1), "y el área superficial del cono es", str(area1))
    ```
* Después de lambda
  ```
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
  ```
  ---
##### 2.De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
###### Solución
###### Primera Función
La función del *reto 6, punto4*
  * Antes de *args
    ```
    #Mensaje contextualizador sobre el programa
    print("Ingrese la cantidad de productos que va a comprar de panes, bolsas de leche y huevos. Te daremos el precio que tiene que pagar, se te informará de las vueltas o lo que quedas debiendo.")
    #Crearemos un programa con las siguientes funciones
    #Una función que me diga el precio dependiendo de el número de panes que compre
    def calcularPrecioPanes(P:int) -> int:
        precioPanes = P*valorPan
        return precioPanes
    #Otra función que me diga el precio dependiendo del número de bolsas de leche que compre
    def calcularPrecioBolsasDeLeche(M:int) -> int:
        precioBolsasDeLeche = M*valorBolsasDeLeche
        return precioBolsasDeLeche
    #Y por último una función que diga el precio dependiendo del número de huevos que compre
    def calcularPrecioHuevo(H:int) -> int:
        precioHuevos = H*valorHuevo
        return precioHuevos
    #Ahora declaramos e inicializamos variables, haciendo la suma entre los resultados de las funciones
    if __name__ == "__main__":
        P:int=int(input("Ingrese el numero de panes que comprará: "))
        M:int=int(input("Ingrese el numero de bolsas de leche que comprará: "))
        H:int=int(input("Ingrese el numero de huevos que comprará: "))
        valorPan:int=300
        valorBolsasDeLeche:int=3300
        valorHuevo:int=350
        precioDelPan = calcularPrecioPanes(P)
        precioDeLasBolsasDeLeche = calcularPrecioBolsasDeLeche(M)
        precioDeLosHuevos = calcularPrecioHuevo(H)
        valorTotal = precioDelPan + precioDeLasBolsasDeLeche + precioDeLosHuevos
        print("El precio de los panes en función del número de panes que comprará es de", str(precioDelPan),"pesos.")
        print("El precio de las bolsas de leche en función del número de bolsas de leche que comprará es de", str(precioDeLasBolsasDeLeche),"pesos.")
        print("El precio de los huevos en función del número de huevos que comprará es de", str(precioDeLosHuevos),"pesos.")
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
    ```
  * Después de *args
  ```
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
  ```
###### Segunda Función
La función del *reto 6, punto2*
  * Antes de *args
```
#Importamos parquete
import math
pi = math.pi
#Primero haremos las funciones
#Iniciaremos por el PERIMETRO del RECTÁNGULO
def calcularPerimetroDelRectangulo(a:float, b:float) ->float:
    perimetroRectangulo = (a*2) + (b*2) #Esta será fórmula para hallar el perimetro
    return perimetroRectangulo
#Ahora haremos la función para el ÁREA del RECTÁNGULO
def calcularAreaDelRectangulo(a: float, b:float) -> float:
    areaRectangulo = (a*b) #Esta será la fórmula para hallar el área
    return areaRectangulo
#Siguiente será el PERIMETRO de la CIRCUNFERENCIA
def calcularPerimetroDelaCircunferencia (r:float) -> float:
    perimetroCircunferencia = 2*pi*r #Esta es la fórmula para calcular el perimetro del circulo
    return perimetroCircunferencia
#Por último haremos la función para calcular el ÁREA de la CIRCUNFERENCIA
def calcularAreaDelCirculo(r:float) -> float:
    areaDelCirculo = pi*(r**2)
    return areaDelCirculo
#Ingresamos variables
if __name__ == "__main__":
    a:float=float(input("Ingrese un valor para un lado del rectángulo: "))
    b:float=float(input("Ingrese  un valor para la base del rectángulo: "))
    r:float=float(input("Ingrese un valor para el radio del circulo: "))
    perimetroR = calcularPerimetroDelRectangulo(a, b)
    areaR = calcularAreaDelRectangulo(a, b)
    perimetroC = calcularPerimetroDelaCircunferencia(r)
    areaC = calcularAreaDelCirculo(r)
    print("El perimetro y el área del rectangulo son", str(perimetroR), "y", str(areaR), "respectivamente.")
    print("El perimetro y el área del circulo son", str(perimetroC), "y", str(areaC), "respectivamente.")
```
  *Después de *args
```
#Este código es del RETO 6 PUNTO 2
#Importamos parquete
import math
pi = math.pi
#Primero haremos las funciones
#Iniciaremos por el PERIMETRO del RECTÁNGULO
def calcularPerimetroDelRectangulo(*args1) ->float:
    perimetroRectangulo = (a*2) + (b*2) #Esta será fórmula para hallar el perimetro
    return perimetroRectangulo
#Ahora haremos la función para el ÁREA del RECTÁNGULO
def calcularAreaDelRectangulo(*args2) -> float:
    areaRectangulo = (a*b) #Esta será la fórmula para hallar el área
    return areaRectangulo
#Siguiente será el PERIMETRO de la CIRCUNFERENCIA
def calcularPerimetroDelaCircunferencia (*args3) -> float:
    perimetroCircunferencia = 2*pi*r #Esta es la fórmula para calcular el perimetro del circulo
    return perimetroCircunferencia
#Por último haremos la función para calcular el ÁREA de la CIRCUNFERENCIA
def calcularAreaDelCirculo(*args4) -> float:
    areaDelCirculo = pi*(r**2)
    return areaDelCirculo
#Ingresamos variables
if __name__ == "__main__":
    a:float=float(input("Ingrese un valor para un lado del rectángulo: "))
    b:float=float(input("Ingrese  un valor para la base del rectángulo: "))
    r:float=float(input("Ingrese un valor para el radio del circulo: "))
    print("El perimetro y el área del rectangulo son", str(calcularPerimetroDelRectangulo(a, b)), "y", str(calcularAreaDelRectangulo(a, b)), "respectivamente.")
    print("El perimetro y el área del circulo son", str(calcularPerimetroDelaCircunferencia(r)), "y", str(calcularAreaDelCirculo(r)), "respectivamente.")
```
###### Tercera Función
La función del *reto 6, punto6*
  * Antes de *args
```
#Mensaje contextualizador de lo que hace el programa
print("Ingrese el número de contagiados actuales de Covid-19 en NuncaLandia y un número de días para calcular cuantos habrá en un futuro dependiendo de los contagiados actuales")
#Hacemos la función para hacer el cálculo
def calcularAproximacionContagiadosNuncalandia(c:int, d:int) -> int:
    aproximacionContagiadosNuncalandia = c*(2**d)
    return aproximacionContagiadosNuncalandia
#Ahora declaramos y inicializamos a las variables
if __name__ == "__main__":
    c:int=int(input("Ingrese el número de actuales contagiados en Nuncalandia: "))
    d:int=int(input("Ingrese el número de días apartir de hoy que se va a analizar: "))
    proximosContagiadosNuncalandia = calcularAproximacionContagiadosNuncalandia(c, d)
    print("El número de contagiados en Nuncalandia será de", str(proximosContagiadosNuncalandia), "teniendo en cuenta los días a partir de hoy.")
```

  * Después de *args
```
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
```
---

##### 3. Escriba una función recursiva para calcular la operación de la potencia.
La solución del problema es la siguiente:
```
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
```
---
##### 4. Utilice la siguiente plantilla de code para contar el tiempo:
```
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este hilo.
---

##### 5. Crear cuenta en stackoverflow y adjuntar imagen en el repo
La cuenta esá creada
[punto5](https://i.postimg.cc/4dVRW2FC/punto5.jpg)
---
##### 6. Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.
El perfil mío es este
[linkedin](https://www.linkedin.com/feed/?trk=onboarding-landing)

---

### Gracias por mirar este repo.
### Espero haya sido de tu agrado
