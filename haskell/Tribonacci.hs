module Tribonacci where

tribonacci :: Num a => (a, a, a) -> Int -> [a]
tribonacci (a, b, c) n = map (trib a b c) [0..n-1]

{-trib :: Int -> Int -> Int -> Int -> Int-}
{-trib a b c n -}
        {-|  n == 0 = a-}
        {-|  n == 1 = b-}
        {-|  n == 2 = c-}
        {-|  n == 3 = a + b + c-}
        {-|  otherwise = (trib a b c (n-1)) + (trib a b c (n-2)) + (trib a b c (n-3))-}
  
{-trib :: Int -> Int -> Int -> Int -> Int-}
trib a b c term
    |   term == 0 = a 
    |   term == 1 = b
    |   term == 2 = c
    |   otherwise = (trib a b c (term - 1)) + (trib a b c (term - 2)) + (trib a b c (term - 3))
