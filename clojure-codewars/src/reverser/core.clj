(ns reverser.core
  (:require [clojure.string :as str]))

(defn reverser [s]
  (str/join " " (map #(apply str %) (map #(reverse %) (str/split s #" ")))))

