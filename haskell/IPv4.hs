module IPv4 where
import Data.Word  (Word32)

type IPString = String

-- word32ToIP :: Word32 -> IPString


word32ToIP w = w `div` 2 ^ 16