module A9n where

import Data.List.Split (splitOn)
import Data.List (intercalate)

import Text.Regex.TDFA ( (=~), AllTextMatches(getAllTextMatches) )
import Text.Regex.TDFA.Text ()

handleBackSlashNumber:: String -> String
handleBackSlashNumber x =  head z : [Prelude.last z]
    where z= x =~ "\\\\[0-9]+"

abbreviate :: String -> String
abbreviate "" = ""
abbreviate (x:xs)
    | length (x : xs) < 4 = x : xs
    | (x:xs) =~ "\\\\[0-9]+" :: Bool = ""
    | not (null unwantedChar) = head [ intercalate z (map abbreviate $ splitOn z (x:xs))  |z <- unwantedChar]
    | otherwise = x : (show . length . init) xs ++ [Prelude.last xs]
    where unwantedChar = getAllTextMatches ((x:xs) =~ "[^a-zA-Z]+|\\\n") :: [String]
