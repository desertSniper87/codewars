module Fibonacci(main) where

import Text.Printf

{-fib:: Int -> Int-}
{-fib 0 = 0-}
{-fib 1 = 1-}
{-fib n = fib (n-1) + fib (n-2)-}

fib :: Int -> Int -> Int -> Int
fib term val prev
    |   term == 0 = prev
    |   term == 1 = val
    |   otherwise = fib (term - 1) (val + prev) val


main :: IO ()
main =
    let v = 1
        p = 0 in
        printf "%d" $ fib 6 v p
