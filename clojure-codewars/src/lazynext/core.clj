(ns lazynext.core
  (:import (clojure.lang LongRange PersistentVector PersistentList)))

(defn next-item
  "Returns the value that comes after item in xs or nil"
  [xs item]
  (cond
    (= (class xs) LongRange)
    (nth xs (+ (.indexOf xs item) 1))
    (= (class xs) String)
    (cond
      (nil? (clojure.string/index-of xs item)) nil
      :else
     (get xs (+ (clojure.string/index-of xs item) 1)))
    (= (class xs) PersistentVector)
    (cond
      (< (.indexOf xs item) 0) nil
      :else
      (get xs (+ (.indexOf xs item) 1)))
    (= (class xs) PersistentList)
    (nth xs (+ (.indexOf xs item) 1))))