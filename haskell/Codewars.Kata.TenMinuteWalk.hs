module Codewars.Kata.TenMinuteWalk where

walksInDirection :: Char -> [Char] -> Int 
walksInDirection dir walk = length $ filter (== dir) walk

isValidWalk :: [Char] -> Bool
isValidWalk w
    | length (take 11 w) /= 10 = False
    | walksInDirection 'n' w == walksInDirection 's' w
    && walksInDirection 'e' w == walksInDirection 'w' w = True
    | otherwise = False