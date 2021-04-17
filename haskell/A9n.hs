module A9n where

import Data.List.Split (splitOn)
import Data.List (intercalate)

abbreviate :: String -> String
abbreviate "" = ""
abbreviate (x:xs)
    | length (x : xs) < 4 = x : xs
    | '-' `elem` (x:xs) = intercalate "-" (map abbreviate $ splitOn "-" (x:xs))
    | '1' `elem` (x:xs) = intercalate "1" (map abbreviate $ splitOn "1" (x:xs))
    | '2' `elem` (x:xs) = intercalate "2" (map abbreviate $ splitOn "2" (x:xs))
    | '3' `elem` (x:xs) = intercalate "3" (map abbreviate $ splitOn "3" (x:xs))
    | '4' `elem` (x:xs) = intercalate "4" (map abbreviate $ splitOn "4" (x:xs))
    | '5' `elem` (x:xs) = intercalate "5" (map abbreviate $ splitOn "5" (x:xs))
    | '6' `elem` (x:xs) = intercalate "6" (map abbreviate $ splitOn "6" (x:xs))
    | '7' `elem` (x:xs) = intercalate "7" (map abbreviate $ splitOn "7" (x:xs))
    | '8' `elem` (x:xs) = intercalate "8" (map abbreviate $ splitOn "8" (x:xs))
    | '9' `elem` (x:xs) = intercalate "9" (map abbreviate $ splitOn "9" (x:xs))
    | ' ' `elem` (x:xs) = unwords (map abbreviate $ splitOn " " (x:xs))
    | '\n' `elem` (x:xs) = intercalate "\n" (map abbreviate $ splitOn "\n" (x:xs))
    | '\\' `elem` (x:xs) = intercalate "\\" (map abbreviate $ splitOn "\\" (x:xs))
    | '\'' `elem` (x:xs) = intercalate "\'" (map abbreviate $ splitOn "\'" (x:xs))
    | otherwise = x : (show . length . init) xs ++ [Prelude.last xs]
