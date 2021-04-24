module Main where


import Data.Char ( ord, chr, isAscii, isLetter )
import GHC.Unicode (isAlpha)

rot13 :: String -> String
rot13 = map rot13char

rot13char :: Char -> Char
rot13char x
    | not (isAscii x && isLetter x) = x
    | nextAscii - base >= 26 = chr(base -1 + nextAscii `mod` (base + 25))
    | otherwise = chr (ord x + 13)
    where base = if ord x >=  ord 'a' then ord 'a' else ord 'A'
          nextAscii = ord x + 13

main :: IO ()
main = do
     print $ rot13 "\807629;\313452\172417\EOT~HI\228471"
     print $ rot13 "W]\146299:7!"


