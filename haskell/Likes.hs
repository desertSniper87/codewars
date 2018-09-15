module Likes where

likes :: [String] -> String
likes[] = "no one likes this"
likes[a] = a ++ " likes this"
likes[a, b] = a ++ " and " ++ b ++ " like this"
likes[a, b, c] = a ++ ", " ++ b ++ " and " ++ c ++ " like this"
likes[a, b, c, d] = a ++ ", " ++ b  ++ " and 2 others like this"
likes x 
    |   length x > 4 = head x ++ ", " ++ x !! 1  ++ " and " ++ show ((length x) - 2) ++ " others like this"
