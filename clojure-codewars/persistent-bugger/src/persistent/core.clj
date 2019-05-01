(ns persistent.core)

(defn multiply-digits  [n]
  (reduce * (map #(Character/digit % 10) (str n))))


(def mult-times (atom 0))

(defn persistence [n]
  (if (= (quot n 10) 0)
   (do
     (let [x @mult-times]
     (reset! mult-times 0)
       x))
   (do
     (swap! mult-times inc)
     (persistence (multiply-digits n)))))












