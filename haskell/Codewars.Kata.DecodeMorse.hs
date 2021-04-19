module Codewars.Kata.DecodeMorse (decodeMorse) where

import Codewars.Kata.DecodeMorse.Preload (morseCodes)

import Data.Map.Strict ((!))
import Data.Function(on)
import Data.List(groupBy)
import Data.Char(isSpace)

decodeMorse :: String -> String
decodeMorse string = map (! morseCodes) $ filter((/=) " ") $ groupBy ((==) `on` isSpace) string