{-module Kata (highAndLow) where-}
module HighAndLow (highAndLow) where

import Data.List

highAndLow :: String -> String
highAndLow input =  fmap ((++) (show $ maximum $ charToInt input )) (++ ( show $ minimum $ charToInt input) ) " "
    where charToInt x = map (read::String -> Int) $ words x
{-highAndLow input = (++) ( (++) (show $ maximum $ charToInt input ) (" ") ) $ show $ minimum $ charToInt input  -}
    {-charToInt :: String -> Int-}
   
