module A9n where

import Data.List.Split (splitOn)
import Data.List (intercalate)

import Text.Regex.TDFA
import Text.Regex.TDFA.Text ()


abbreviate :: String -> String
abbreviate "" = ""
abbreviate (x:xs)
    | length (x : xs) < 4 = x : xs
    | not (null unwantedChar) = head [ intercalate z (map abbreviate $ splitOn z (x:xs))  |z <- unwantedChar]
    | otherwise = x : (show . length . init) xs ++ [Prelude.last xs]
    where unwantedChar = getAllTextMatches ((x:xs) =~ "[^a-zA-Z]+|\\\n") :: [String]
