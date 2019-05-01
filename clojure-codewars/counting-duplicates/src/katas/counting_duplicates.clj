(ns katas.counting-duplicates)

(defn greater1? [mentry]
  (< 1 (val mentry)))

(defn duplicate-count [text]
  (count (filter greater1? (frequencies (clojure.string/lower-case text)))))

