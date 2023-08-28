
doble x = x + x
triple x = x*3

f:: Int -> Int
f n
    | n== 1 = 8
    | n== 4 = 131
    | n== 16 = 16  

g :: Int -> Int
g n
    | n== 8 = 16
    | n== 131 = 1
    | n== 16 = 4

h x =f(g x)

k y = (f y)

máximo3:: Int -> Int -> Int -> Int
máximo3 x y z
    |x >= y && x >=z =x
    |y >= z && y >=x =y
    |otherwise = z

--"comentario": acá puedo escribir cualquier cosa y el IDE no marca error
{-acá también-}

sumaDistintos:: Int -> Int -> Int -> Int
sumaDistintos x y z
    | x==y && x==z = 0
    | x==y = z
    | x==z = y
    | y==z = x
    | otherwise = x + y + z

digitoUnidades:: Int -> Int
digitoUnidades n 
    |n>=0 = mod n 10
    |otherwise = mod (-n) 10

{-
digitoDecenas:: Int -> Int
digitoDecenas n
    |
-}

