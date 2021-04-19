module Codewars.Exercise.MergeChecker where

isMerge :: [Char] -> [Char] -> [Char] -> Bool
isMerge s x y
    |  s == x && y == ""  = True
    |  s /= x && y == ""  = False
    |  s == y && x == ""  = True
    |  s /= y && x == ""  = False
    |  s == "" = False
isMerge (s:ss) (x:xs) (y:ys)
    | s == x && s == y = isMerge ss xs (y:ys) || isMerge ss (x:xs) ys
    | s == x = isMerge ss xs (y:ys)
    | s == y = isMerge ss (x:xs) ys
    | otherwise = False