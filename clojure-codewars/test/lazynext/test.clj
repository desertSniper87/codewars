(ns lazynext.test
  (:require [clojure.test :refer :all]
            [lazynext.core :refer [next-item]]))

(deftest SampleTests
  (is (= (next-item (range 1 25) 12) 13))
  (is (= (next-item "testing" \t) \e))
  (is (nil? (next-item [:a :b :c] :d)))
  (is (nil? (next-item [:a :b :c] :c))))