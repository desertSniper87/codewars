module NthSeries.Test where
import NthSeries
{-module Codewars.Kata.NthSeries.Test where-}
{-import Codewars.Kata.NthSeries-}

import Test.Hspec
import Text.Printf (printf)

--testSumSeries :: Integer -> String -> SpecWith (Arg Expectation)
testSumSeries nb r = 
    it (printf " %i " nb) $
        seriesSum nb `shouldBe` r
    
main = hspec $ do
    describe "Nth series" $ do
        testSumSeries 0 "0.00"
        testSumSeries 9 "1.77"
        testSumSeries 15 "1.94"
