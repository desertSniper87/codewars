module A9n where

import Data.List.Split (splitOn)
import Data.List (intercalate)

abbreviate :: String -> String
abbreviate "" = ""
abbreviate (x:xs)
    | length (x : xs) < 4 = x : xs
    | '-' `elem` (x:xs) = intercalate "-" (map abbreviate $ splitOn "-" (x:xs))
    | otherwise = x : (show . length . init) xs ++ [Prelude.last xs]