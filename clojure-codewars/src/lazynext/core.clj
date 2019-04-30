(ns lazynext.core
  (:import (clojure.lang LongRange PersistentVector)))

(defn next-item
  "Returns the value that comes after item in xs or nil"
  [xs item]
  (cond
    (= (class xs) LongRange)
    (nth xs (+ (.indexOf xs item) 1))
    (= (class xs) String)
    (get xs (+ (clojure.string/index-of xs item) 1))
    (= (class xs) PersistentVector)
    (cond
      (< (.indexOf xs item) 0) nil
      :else
      (get xs (+ (.indexOf xs item) 1)))))