import Control.Monad.State

fib n = flip evalstate (0, 1) $ do
  forM [0..(n-1)] $ \_ -> do
    (a, b) <- get
    
