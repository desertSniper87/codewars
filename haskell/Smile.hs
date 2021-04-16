module Smile where

import Control.Monad (liftM2)
countListComp :: Eq a => [a] -> a -> Int
countListComp [] find = 0
countListComp ys find = length xs
    where xs = [xs | xs <- ys, xs == find]

validEyes :: Char -> Bool
validEyes x = x `elem` ":;"

validSmile :: Char -> Bool
validSmile x  = x `elem` ")D"

validNose :: Char  -> Bool
validNose x = x `elem` "-~"

countSmily :: String -> Bool
countSmily "" = False 
countSmily [x] = False
countSmily [x, xs] = validEyes x && validSmile xs
countSmily (x:xs:rest)
    | validEyes x && validNose xs && validSmile (head rest) = True
    | otherwise = False

countSmileys :: [String] -> Int
countSmileys = length . filter countSmily