module Codewars.G964.Printer where
{-module PrinterError where-}
import Data.Char

printerError :: [Char] -> [Char]
printerError x = validCodeLength x ++ "/" ++  (show . length) x
    where validCodeLength = show . length . filter (\x -> x>109) . map ord 
    

