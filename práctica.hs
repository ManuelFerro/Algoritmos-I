
doble :: Num a => a -> a
doble x = x + x
triple :: Num a => a -> a
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
estanRelacionados a b |a>=0 && b>=0 && mod a b==0 = True
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

absoluto :: (Num t, Ord t)=> t -> t
absoluto n |n <= 0 = -n
           |otherwise = n

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p1,p2,p3) (q1,q2,q3) = absoluto(p1 - q1) + absoluto(p2 - q2) + absoluto(p3 - q3)

productoPunto :: (Float,Float) -> (Float,Float) -> Float
productoPunto (a,b) (c,d) = a*c + b*d

-- Prac 4

fibbonacci :: Int -> Int
fibbonacci n |n==0 = 0
             |n==1 = 1
             |otherwise = fibbonacci(n-1) + fibbonacci(n-2)

parteEntera :: Float -> Int
parteEntera x | 0 <= x && x < 1 = 0
              | 0 >= x && x > -1 = 0
              | x >= 1 = 1 + parteEntera(x-1)
              |otherwise = parteEntera(x+1) - 1

ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

sacarUltimo :: Int -> Int
sacarUltimo n = div n 10

tDI :: Int -> Bool
tDI n |n < 10 = True
      |otherwise = (ultimoDigito n == ultimoDigito (sacarUltimo n)) && tDI (sacarUltimo n)

cantDigitos :: Int -> Int
cantDigitos n | 0<=n && n<=9 = 1
              | otherwise = 1 + cantDigitos (div n 10) 

iesimoDigito :: Int -> Int -> Int
iesimoDigito n i = mod (div n 10^(cantDigitos(n) -i)) 10

menorDivisor :: Int -> Int
menorDivisor n | n==1 = 1
               |otherwise = menorDivisorDesde n 2

menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde n m | mod n m == 0 = m
                      |otherwise = menorDivisorDesde n (m+1)

esPrimo :: Int -> Bool
esPrimo n | n==1 = False
          |menorDivisor n == n = True
          |otherwise = False

mismoSiguientePrimo :: Int -> Int
mismoSiguientePrimo n | esPrimo n == True = n
                      |otherwise = mismoSiguientePrimo (n+1)

enesimoPrimo :: Int -> Int
enesimoPrimo 1 = 2
enesimoPrimo n = mismoSiguientePrimo (enesimoPrimo (n-1) + 1)

sumaKPrimos :: Int -> Int
sumaKPrimos 1 = enesimoPrimo 1
sumaKPrimos k = enesimoPrimo k + sumaKPrimos (k-1)

esSumaDePrimerosKPrimos :: Int -> Int -> Bool
esSumaDePrimerosKPrimos k n | sumaKPrimos k == n = True
                            | sumaKPrimos k > n =False
                            | otherwise = esSumaDePrimerosKPrimos (k+1) n

esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos n = esSumaDePrimerosKPrimos 1 n

cantidadDivisoresHasta n 1 = 1
cantidadDivisoresHasta n d | mod n d == 0 = 1 + cantidadDivisoresHasta n (d-1)
                           | otherwise = cantidadDivisoresHasta n (d-1)

factorial :: (Num t, Ord t)=> t -> t
factorial 0 = 1
factorial n = n*(factorial (n-1))

numCombinatorio :: Integer -> Integer -> Integer
numCombinatorio n k = (factorial n)/((factorial K)*(factorial (n-k))) 

{-contarPitagoras :: Integer -> Integer -> Integer -> Integer
contarPitagoras m n r | m==0 || n==0 = contarPitagoras0 m n r
                      | m^2 + n^2 <= r^2 = (numCombinatorio m n)
                      |
                      |
                      | otherwise = barrerPitagoras m n r

contarPitagoras0 :: Integer -> Integer -> Integer -> Integer
contarPitagoras0 m n r | m==0 && m==n = 1
                       | m==0 && n^2 >= r^2 = 1
                       | m==0 && n^2 <= r^2 = n + 1

barrerPitagoras :: Integer -> Integer -> Integer -> Integer
barrerPitagoras m n r | m==n && m==0 = 
                      | m==n = contarPitagoras (m-1) (n-1) r
                      | 
                      |-}