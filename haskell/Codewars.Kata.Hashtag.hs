module Codewars.Kata.Hashtag where

import Data.Char (isAlpha)

generateHashtag :: String -> Maybe String
generateHashtag case maybeValue of s
    | not $ null filtered  (++) "#" filtered
    | otherwise = Nothing 
    where filtered = filter isAlpha s 
