import numpy
import random
from typing import Any
from queue import LifoQueue as Pila #Last In, First Out
from queue import Queue as Cola #"Fifo": First In, First Out


#ejemplos y ejercicio 1

def prueba():
    print ("funciona")

def imprimir_hola():
    print ("Hola Manu")

imprimir_hola()

def es_multiplo_de(n:int,m:int) -> bool:
    res:bool = (n%m)==0 # mod n m ==0 en haskell
    return res

def es_nombre_largo (nombre: str) -> bool:
    res:bool = 3<=len(nombre) and len(nombre)<=8 # &&=and
    return res

def devolver_el_doble_si_es_par(n:int) -> int:
    if es_multiplo_de(n,2):
        res:int = 2*n
    else:
        res:int = n
    return res

def imprimir_pares():
    i:int = 10
    while i<=10 :
        if es_multiplo_de(i,2):
            print(i)
        i=i+1

def imprimir_pares_for():
    for i in range(10,41,1):
        if es_multiplo_de(i,2):
            print(i)
        i=i+1

# ejercicio 2

def raizDe2():
    res:float = round(numpy.sqrt(2), 4)
    return res

def factorial_de(n:int) -> int:
    res:int = 1
    for i in range(1,n+1):
        res = res*i
        print(res)               
    return res

def factorial_w(n:int) -> int:
    res:int = n
    i:int = n-1
    while i>0:
        print(res)
        res=res*i
        i=i-1
    return res

def imprimir_saludo(string):
    print("hola",string)

def fahrenheit_a_celsius(t:float) -> float:
    res:float = ((t-32)*5)/9
    return res

def cantidad_de_pizzas(c:int, min_p:int) -> int:
    if (c*min_p%8) == 0:
        res:int = int((c*min_p)/8)
    else:
        res:int = int((c*min_p + 8 - (c*min_p%8))/8)
    return res

# ejercicio 3

def es_bisiesto(año:int) -> bool:
    if (año%400)==0:
        res:bool = True
    else:
        res:bool = (año%4)==0 and (año%100)!=0
    return res

# ejercicio 4

def peso_pino(m:float) -> float:
    if 3>=m:
        res:float = m*100*3
    else:
        res:float = 3*3*100 + 2*(m-3)*100
    return res

def es_peso_util(kg:float) -> bool:
    res:bool = kg<=1000 and kg>=400

def sirve_pino(m:float) -> bool:
    res:bool= es_peso_util(peso_pino(m))

# ejercicio 5

def trabajo_o_vacaciones(masculino:bool,edad:int): #el sexo es el que figura en el dni, no contempla personas no binarias
    if edad<=18 or edad>=65:
        res= print("Andá de vacaciones")
    else:
        if masculino==False and edad>=60:
            res= print("Andá de vacaciones")
        else: res = print("Te toca trabajar")
    return res

def sumaTotal(s:[int]) -> int:
    total: int=0
    longitud: int=len(s)
    indice_actual: int=0
    while indice_actual < longitud:
        total+= s[indice_actual] # += equivale a "total= total + s[indice_actual]" 
        indice_actual += 1
    return total 

def pertenece(s:[], e: Any) -> bool:
    res:bool=False
    for i in range (0, len(s)):    
        if e==s[i]:
            res = True          
    return res

def es_numero(c: str) -> bool:
    res: bool=False
    if (c<="9") and (c>="0"):
        res=True
    return res

def es_mayus(c: str) -> bool:
    res: bool=False
    if (c<="Z") and (c>="A"):
        res=True
    return res

def es_minus(c: str) -> bool:
    res: bool=False
    if (c<="z") and (c>="a"):
        res=True
    return res

def fortaleza_contraseña(contra:str):
    longitud: int=len(contra)
    
    longitud_mayor_8: bool =False
    if longitud >= 8:
        longitud_mayor_8= True
    
    longitud_menor_5: bool =False
    if longitud < 5:
        longitud_menor_5= True

    tiene_mayus: bool=False
    indice_actual: int=0
    while indice_actual < longitud:
        if es_mayus(contra[indice_actual]):
            tiene_mayus= True
        indice_actual += 1

    tiene_minus: bool=False
    indice_actual: int=0
    while indice_actual < longitud:
        if es_minus(contra[indice_actual]):
            tiene_minus= True
        indice_actual += 1
        
    tiene_numero: bool=False
    indice_actual: int=0
    while indice_actual < longitud:
        if es_numero(contra[indice_actual]):
            tiene_numero= True
        indice_actual += 1

    if longitud_mayor_8 and tiene_mayus and tiene_minus and tiene_numero:
        return "VERDE"
    elif longitud_menor_5: #else if
        return "ROJA"
    else:
        return "AMARILLA"
    
#Pilas, Colas, Archivos

#Pilas, importado de Queue
p = Pila()
p.put(1) #apilar
p.put(2) #apilar
p.put(3) #apilar
print(list(p.queue))
elemento = p.get()
print(elemento) #desapilar
print(p.empty()) #vacia ?
print(list(p.queue))

#Colas, importado de Queue
c= Cola()
c.put(1) #Encolar
c.put(2) #Encolar
c.put(3) #Encolar
print(list(c.queue))
elemento = c.get()
print(elemento) #desEncolar
print(c.empty()) #vacia ?
print(list(c.queue))

#diccionarios, nativos de python
d = dict() #d es diccionario
d[2] = "Argentina" #asigno al valor 2 la clave "Argentina"
                   #si no había nada lo agrega, si lo había lo pisa
2 in d #si el valor 2 está libre

def clonarSinComentarios(nombre_archivo: str):

    arch_Comentado = open(nombre_archivo,"r")
    arch_Sin_Comentario = open("clonadoSinComentarios.py", "w")
    lineas = arch_Comentado.readLines()

    for linea in lineas:
        if not linea.strip()[0] == "#":
            arch_Sin_Comentario.write(linea)

    arch_Comentado.close()
    arch_Sin_Comentario.close()

    return 

def buscarElMaximo(p:Pila) -> int:
    max: int = p.get()
    paux: Pila = Pila()

    while (not p.empty()):
        elem = p.get()
        paux.put(elem)
        if elem > max :
            max = elem

    while not paux.empty():
        elem = paux.get()
        p.put(elem)
            
    return max

def contarElementosPila(p: Pila) -> int:
    res: int = 0
    paux: Pila = Pila()

    while (not p.empty()):
        elem = p.get()
        paux.put(elem)
        res = res + 1

    while not paux.empty():
        elem = paux.get()
        p.put(elem)

    return res

def contarElementosCola(c: Cola) -> int:
    res: int = 0
    caux: Cola = Cola()

    while (not c.empty()):
        elem = c.get()
        caux.put(elem)
        res = res + 1

    while not caux.empty():
        elem = caux.get()
        c.put(elem)

    return res

def armarSecuenciaDeBingo() -> Cola:
    bolillero:Cola = Cola()
    listaOrd:list = list(range(0,99))
    lista:list = random.shuffle(listaOrd)

    while len(lista) > 0:
        bolillero.put(lista.pop())
    
    return bolillero

def jugarCartonDeBingo(carton: [int], bolillero: Cola) -> int:
    intentos: int = 0
    aciertos: int = 0

    while aciertos < 12:
        for i in range (0, 99):
            if carton[i] == bolillero.pop():
                aciertos = aciertos + 1
                intentos = intentos + 1
            else: intentos = intentos + 1
        
    return intentos

def agruparPorLongitud(nombre_archivo: str) -> dict:
    archivo = open(nombre_archivo, "r")
    d = dict()
    lineas = archivo.readLines()

    for linea in lineas:
        palabras = linea.split()
        for palabra in palabras:
            longitud = len(palabra)
            if (longitud in d):
                d[longitud] += 1 #le sumo 1
            else:
                d[longitud] = 1 #al asignarle un valor, creo la clave (antes no existia)
    
    archivo.close()
    return d

def palabraMasFrecuente(nombre_archivo: str) -> str:
    archivo = open(nombre_archivo, "r")
    d = dict()

    lineas = archivo.readLines()
    for linea in lineas:
        palabras = linea.split()
        for palabra in palabras:
            if (palabra in d):
                d[palabra] += 1
            else:
                d[palabra] = 1
        
        max: int = 0
        claveMax: str
        for palabra,frecuencia in d.items():
            if frecuencia > max:
                max = frecuencia
                claveMax = palabra

    archivo.close()
    return claveMax

def reverso(nombre_archivo: str):
    archivo = open(nombre_archivo, "r")
    arch_reverso = open("reverso.txt", "w")

    lineas = archivo.readlines()
    for i in range(len(lineas)-1, -1, -1):
        arch_reverso.write(lineas[i])

    archivo.close()
    arch_reverso.close()

print("voy a testear")
reverso("hola.py")
print("testie")

def agregarFrase(archivo: str, palabra:str):
    archivo = open (archivo, "a") #append escribe al final sin reescribir el archivo, write escribe al inicio pisando lo anterior
    archivo.write(palabra)
    archivo.close()
    
    return