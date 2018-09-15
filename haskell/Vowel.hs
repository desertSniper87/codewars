module Vowel where
{-module Codewars.Kata.Vowel where-}

getCount :: [Char] -> Int
vowels = "aeiou"
getCount s = length [i | i <- s, i `elem` vowels ]
 
