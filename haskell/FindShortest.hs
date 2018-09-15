module FindShortest where
find_shortest :: String -> Integer
find_shortest x = fromIntegral (foldr1 min [ y | y <- map length [ w | w <- words x ] ] )
