import numpy
from typing import Any

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
