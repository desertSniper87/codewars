{-# OPTIONS -fno-warn-tabs #-}

module PrinterError.Test (main) where
import PrinterError (printerError)

import Test.Hspec
import Test.QuickCheck
import Text.Printf (printf)

testPrinter :: [Char] -> [Char] -> Spec
testPrinter s u = 
    it (printf "should return printerError for s : %s --> %s " s u) $
        printerError s `shouldBe` u

main = hspec $ do

    describe "printerError" $ do
        testPrinter "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz" "3/56"
