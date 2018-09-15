module Codewars.G964.Arge where
{-module Population where-}

nbYear :: Int -> Double -> Int -> Int -> Int
nbYear p0 percent aug p = popExp 0 p0 percent aug p
popExp :: Int -> Int -> Double -> Int -> Int -> Int
popExp x p0 percent aug p
    |   p0 >= p = x 
    |   otherwise = popExp (x+1) (truncate (fromIntegral p0 + (percent * fromIntegral p0 / 100) + fromIntegral aug)) percent aug p
