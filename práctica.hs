
doble x = x + x
triple x = x*3

f:: Int -> Int
f n |n==1 = 8
    |n==4 = 131
    |n==16 = 16  

g :: Int -> Int
g n | n== 8 = 16
    | n== 131 = 1
    | n== 16 = 4

h x =f(g x)

k y = (f y)

máximo3:: Int -> Int -> Int -> Int
máximo3 x y z |x >= y && x >=z =x
              |y >= z && y >=x =y
              |otherwise = z

--"comentario": acá puedo escribir cualquier cosa y el IDE no marca error
{-acá también-}

sumaDistintos:: Int -> Int -> Int -> Int
sumaDistintos x y z | x==y && x==z = 0
                    | x==y = z
                    | x==z = y
                    | y==z = x
                    | otherwise = x + y + z

digitoUnidades:: Int -> Int
digitoUnidades n |n>=0 = mod n 10
                 |otherwise = mod (-n) 10

--Prac 3

estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b |a>=0 && b>=0 && mod a b == 0 = True
                      |otherwise = False

posPrimerPar :: (Int,Int, Int) -> Int
posPrimerPar (x,y,z) |mod x 2 == 0 = 1
                     |mod y 2 == 0 = 2
                     |mod z 2 == 0 = 3
                     |otherwise = 4

añoBisiesto :: Int -> Bool
añoBisiesto n |mod n 4 /= 0 = False
              |mod n 100 == 0 && mod n 400 /= 0 = False
              |otherwise = True

absoluto :: (Num t)=> t -> t
absoluto n |n <= 0 = -n
           |otherwise = n

distanciaManhattan :: (Float, Float, Float) ->(Float, Float, Float) ->Float
distanciaManhattan (p1,p2,p3) (q1,q2,q3) = absoluto(p1 - q1) + absoluto(p2 - q2) + absoluto(p3 - q3)

productoPunto :: (Float,Float) -> (Float,Float) -> Float
productoPunto (a,b) (c,d) = a*c + b*d

-- Prac 4

fibbonacci :: Int -> Int
fibbonacci n |n==0 = 0
             |n==1 = 1
             |otherwise = fibbonacci(n-1) + fibbonacci(n-2)

parteEntera :: Float -> Integer
parteEntera x | 0 <= x && x < 1 = 0
              | 0 >= x && x > -1 = 0
              | x >= 1 = 1 + parteEntera(x-1)
              |otherwise = parteEntera(x+1) - 1

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

sacarUltimo :: Integer -> Integer
sacarultimo n = div n 10

tDI :: Int -> Bool
tDI n |n < 10 = True
      |otherwise = (ultimoDigito n == ultimoDigito (sacarUltimo n)) && tDI (sacarUltimo n)

cantDigitos :: Integer -> Integer
cantDigitos n | n==0 = 1
{-              | otherwise =

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n 10^(cantDigitos(n) -i)) 10 -}