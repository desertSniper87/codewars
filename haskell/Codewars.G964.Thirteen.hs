module Codewars.G964.Thirteen where

digs :: Integer -> [Integer]
digs 0 = []
digs x = x `mod` 10 : digs (x `div` 10)

modlist ::  Int -> [Integer]
modlist len =  map (\x -> 10^x `mod` 13) [0..len-1]

mulist ::  Integer -> [Integer]
mulist x = zipWith (*) (digs x) (modlist . length . digs $ x)

thirtUtil :: Integer -> Integer
thirtUtil = sum . mulist

thirt :: Integer -> Integer
thirt x
    | x > 100 = (thirt . thirtUtil) x 
    | otherwise = x
