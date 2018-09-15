module CreatePhoneNumber where

createPhoneNumber :: [Int] -> String
createPhoneNumber x = (fmap (++ ( concatMap show $ take 3 x )) (++ "(") ("")) ++ ") " ++ (concatMap show $ take 3 $ drop 3 x) ++ "-" ++ (concatMap show $ drop 6 x)
