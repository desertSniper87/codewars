module Stray (stray) where
import Data.List (nub)

count :: Eq a => a -> [a] -> Int
count x = length . filter (x==)

unique :: [Int] -> Int
unique xs = (head . filter (\x -> count x xs == 1)) xs


stray :: [Int] -> Int
stray (x:xs:rest)
    | x /= xs && rest /= [] && x/= head rest = x
    | length rest == 1 = unique $ [x] ++ [xs] ++ rest
    | otherwise = stray(xs:head rest:tail rest)
