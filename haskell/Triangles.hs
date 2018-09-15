module Codewars.Triangles where
{-module Triangles where-}

import Data.List (sort)
import Text.Printf (printf)

isTriangle :: Int -> Int -> Int -> Bool
isTriangle a b c 
  |  a + b <= c = False
  |  b + c <= a = False
  |  c + a <= b = False
  |  otherwise = True
