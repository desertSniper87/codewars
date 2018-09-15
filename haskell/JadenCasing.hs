module JadenCasing where
import Data.Char
import Data.List

toJadenCase :: String -> String
toJadenCase = concat . map (\(c:cs) -> toUpper c : cs) .  groupBy(\a b -> isSpace a == isSpace b ) 
 
