(ns kata.bus)
(defn cur-bus [b]
  (- (first b) (last b)))
(defn number [bus-stops]
  (reduce + (map cur-bus bus-stops)))




