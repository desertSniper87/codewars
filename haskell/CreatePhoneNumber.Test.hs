import CreatePhoneNumber
import Test.QuickCheck
import Test.Hspec

main = hspec $ do
  describe "Running tests" $ do
      it "Example case" $ do
        createPhoneNumber [1,2,3,4,5,6,7,8,9,0] `shouldBe` "(123) 456-7890"
