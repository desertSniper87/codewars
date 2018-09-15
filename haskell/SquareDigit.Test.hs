import SquareDigit
import Test.QuickCheck
import Test.Hspec

main = hspec $ do
  describe "Testing solution:" $ do
    it "Should double a positive integer:" $ do
      squareDigit 9119 `shouldBe` 811181
      squareDigit (-1) `shouldBe` (-1)
