module Codewars.Kata.YourOrderPlease where

import Data.List.Split (wordsBy)
import Data.Char ( isLetter, isDigit )
import Debug.Trace ()
import Data.List (sort)
import Distribution.Simple.Utils (comparing)


takeNumber :: String -> Integer
takeNumber s = read (filter isDigit s) :: Integer

getNumberFromOrder :: String -> [Integer]
getNumberFromOrder = map takeNumber . words

-- yourOrderPlease :: String -> String

getTuple :: String -> [(String, Integer)]
getTuple order = zip (words order) (getNumberFromOrder order)

yourOrderPlease :: String -> String
yourOrderPlease order = unwords . map snd . sort . map (\x -> (lookup x (getTuple order), x)) $ words order
