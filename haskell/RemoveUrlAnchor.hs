module RemoveUrlAnchor where

import Data.List.Split (splitOn)

removeUrlAnchor :: String -> String
removeUrlAnchor s = head (splitOn "#" s)


