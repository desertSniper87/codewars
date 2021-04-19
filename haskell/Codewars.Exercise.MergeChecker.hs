module Codewars.Exercise.MergeChecker where

isMerge :: String -> String -> String -> Bool
isMerge "" _ _ = False
isMerge _ "" "" = True 
isMerge (s:ss) (x:xs) (y:ys)
    | s == x = isMerge ss xs (y:ys)
    | s == y = isMerge ss (x:xs) ys
    | null ys || null xs = True 
    | otherwise = False 
