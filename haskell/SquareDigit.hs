module SquareDigit where
import Data.Char

squareDigit :: Int -> Int
squareDigit x 
    |   x < 0 = (val (x * (-1)) * (-1))
    |   otherwise = val x
    where val = read . concatMap show . map (\a -> a^2) . map digitToInt . show
