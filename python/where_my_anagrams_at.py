def anagrams(word, words):
    print(word, words)
    result = []
    for w in words:
        if set(w) == set(word):
            if check_count(w, word) is not None:
                result.append(w)

    return result

def check_count(w1, w2):
    for x in set(w2):
        if w1.count(x) != w2.count(x):
            return 
    return w2



