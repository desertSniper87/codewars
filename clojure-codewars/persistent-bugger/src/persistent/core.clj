(ns persistent.core)

(defn persistence [n]
  (def number (atom n))
  (def nos-mult (atom 0))
  (while (not (= (count (str n)) 1))
    (do (swap! number))
        (swap! nos-mult inc))))

(defn bugger [n]
  ())







