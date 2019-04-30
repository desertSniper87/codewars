(ns lazynext.test
  (:require [clojure.test :refer :all]
            [lazynext.core :refer [next-item]]))

(deftest SampleTests
  (is (= (next-item (range 1 25) 12) 13))
  (is (= (next-item "testing" \t) \e))
  (is (nil? (next-item "testing" \k)))
  (is (nil? (next-item [:a :b :c] :d)))
  (is (nil? (next-item [:a :b :c] :c)))
  (is (nil? (next-item (list :a :b :c) :d)))
  (is (= (next-item (list :a :b :c :d) :a) :b)))
