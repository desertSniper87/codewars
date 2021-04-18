module Pangram where

import Data.Char ( isAlpha, toLower )
import qualified Data.Set as Set

isPangram :: String -> Bool
isPangram x = (==) 26 $ length . Set.fromList $ map toLower $  filter isAlpha x