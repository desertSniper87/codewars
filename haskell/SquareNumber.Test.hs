{-module Codewars.Kata.Square.Test where-}
module SquareNumber.Test where
import SquareNumber (isSquare)
import Test.Hspec

main = hspec $ do
  describe "isSquare" $ do
    it "should work for some examples" $ do
      isSquare (-1) `shouldBe` False
      isSquare  0   `shouldBe` True
      isSquare  3   `shouldBe` False
      isSquare  4   `shouldBe` True
      isSquare 25   `shouldBe` True
      isSquare 26   `shouldBe` False    
    it "should work for random square numbers" $ do
      property $ \n -> isSquare (n^2 :: Integer) `shouldBe` True
