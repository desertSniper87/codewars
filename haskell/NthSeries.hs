{-module NthSeries where-}
module Codewars.Kata.NthSeries where
    
import Numeric

seriesSum :: Integer -> String
seriesSum x
    |   x == 1 || x == 0 = showFFloat (Just 2) (fromIntegral x) ""
    |   otherwise = showFFloat (Just 2) ( sum [ (/) 1 $ fromIntegral y + (fromIntegral y - 1) * 2 | y <- [1..x] ] ) ""
