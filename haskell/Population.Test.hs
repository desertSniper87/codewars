{-module Codewars.G964.Arge.Test (main) where-}
{-import Codewars.G964.Arge (nbYear)-}

module Population.Test (main) where
import Population (nbYear)

import Test.Hspec
import Test.QuickCheck
import Text.Printf (printf)

testNbYear :: Int -> Double -> Int -> Int -> Int -> Spec
testNbYear p0 percent aug p u = 
    it (printf "should return nbYear for n: %d %s %d %d " p0 (show percent) aug p) $
        nbYear p0 percent aug p `shouldBe` u

main = hspec $ do

    describe "nbYear" $ do
        testNbYear 1500 5 100 5000 15
        testNbYear 1500000 2.5 10000 2000000 10
        testNbYear 1500000 0.25 1000 2000000 94
