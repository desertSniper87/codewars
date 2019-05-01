(ns kata.bus-testing
  (:require [clojure.test :refer :all])
  (:use [kata.bus :rename {number solution}]))

(deftest basic-tests
  (is (= 5 (solution [[10 0] [3 5] [5 8]])))
  (is (= 17 (solution [[3 0] [9 1] [4 10] [12 2] [6 1] [7 10]])))
  (is (= 21 (solution [[3 0] [9 1] [4 8] [12 2] [6 1] [7 8]]))))