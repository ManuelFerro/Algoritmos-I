import Test.HUnit
import Data.String (String)
relacionesValidas:: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas (a0:as) | noTuplasRepetidas (a0:as) == True && noTuplasAmbasIguales (a0:as) == True = True
                          | otherwise = False

noTuplasAmbasIguales:: [(String,String)] -> Bool
noTuplasAmbasIguales [] = True
noTuplasAmbasiguales ((a,b):as) | a==b = False
                                | otherwise = noTuplasAmbasIguales (as)


noTuplasRepetidas:: [(String,String)] -> Bool
noTuplasRepetidas [] = True
noTuplasRepetidas ((a,b):as) | pertenece (a,b) as == True = False
                             | pertenece (b,a) as == True = False
                             | otherwise = noTuplasRepetidas (as)

pertenece:: (Eq c) => c->[c] -> Bool
pertenece c0 [] = False
pertenece c0 (c1:cs) | c0 == head(c1:cs) = True
                     | otherwise = pertenece c0 (cs)

--

personas:: [(String,String)] -> [String]
personas [] = []
personas ((a,b):xs) | pertenece a (personas xs) && pertenece b (personas xs) = personas xs
                    | pertenece a (personas xs) = b:personas xs
                    | pertenece b (personas xs) = a:personas xs
                    | otherwise = a:b:personas xs

--

amigosDe:: String -> [(String,String)] -> [String]
amigosDe [] _ = []
amigosDe p ((a,b):as) | p==a = b:amigosDe p (as)
                      | p==b = a:amigosDe p (as)
                      | otherwise = amigosDe p (as)

--

cardinal:: [t] -> integer
cardinal [] = 0
cardinal (t:ts) = 1 + cardinal (ts) 

cantidadDeAmigos:: String -> [(String,String)] -> Integer
cantidadDeAmigos p rs = cardinal(amigosDe p rs)  

personaConMasAmigos:: [(String,String)] -> String
personaConMasAmigos red = personaonMasAmigosAux (personas red) red 

{-personaConMasAmigosAux:: [String] -> [(String,String)] -> String
personaConMasAmigosAux 

-}