module Difference where

difference :: Integral a => [a] -> [a] -> [a]
difference [] y = []
difference (x:xs) y 
  | x `elem` y = difference xs y
  | otherwise = x : difference xs y
  
