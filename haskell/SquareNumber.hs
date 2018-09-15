module Codewars.Kata.Square where
{-module SquareNumber where-}

isSquare :: Integral n => n -> Bool
isSquare x = (==) x $ (^2) $ round $ sqrt $ fromIntegral x 
