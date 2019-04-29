(ns digitizer.core)

(defn digitize [n]
  (map #(Integer/parseInt %) (reverse (clojure.string/split (str n) #""))))