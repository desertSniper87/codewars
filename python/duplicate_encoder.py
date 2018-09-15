def duplicate_encode(word):
    out = ""
    word = word.lower()
    for i in word:
        if word.count(i) > 1:
            out += ')'
        else:
            out += '('

    return out


