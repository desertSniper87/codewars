module AlternateSplit.JorgeVS.Kata where

import Control.Monad (forM_)

indices :: (Num a, Enum a) => (a -> Bool) -> [b] -> [b]
indices f  = map snd .filter (f . fst) . zip [0..]

evens :: [b] -> [b]
evens = indices even

odds :: [b] -> [b]
odds = indices odd


encrypt' :: String  -> String
encrypt' x = odds x ++ evens x 

encrypt :: String -> Int -> String
encrypt s n 
    | n < 1 = s
    | otherwise = iterate encrypt' s !! n

decrypt' :: String -> String
decrypt' x = decrypt'' fstHalf sndHalf 
    where fstHalf = take l x 
          sndHalf = drop l x
          l = length x `div` 2

decrypt :: String -> Int -> String
decrypt s n 
    | n < 1 = s
    | otherwise = iterate decrypt' s !! n


decrypt'' :: [a] -> [a] -> [a]
decrypt'' [] x = x
decrypt'' (x:xs) (y:ys) = y : x : decrypt'' xs ys 

