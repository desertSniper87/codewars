(ns clojure.bit-counting)

(defn count-bits [n]
  (if (= n 0) 0
   ((frequencies (Integer/toString n 2)) \1)))

