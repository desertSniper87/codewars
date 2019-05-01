(ns the-shell-game-test
  (:require [clojure.test :refer :all]
            [the-shell-game :refer :all]))

(deftest basic-test
  (testing "An empty swap set doesn't move the ball"
    (is (= (find-the-ball 5 []) 5)))
  (testing "Some games"
    (is (= (find-the-ball 0 [[0 1] [2 1] [0 1]]) 2))))
