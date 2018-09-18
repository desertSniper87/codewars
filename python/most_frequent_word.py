from collections import Counter
import re


def top_3_words(text):
    # text = ''.join(t for t in text
    #                if str.isalnum(t) == True or
    #                t in [' ', '\''])

    print(text)

    # pattern = re.compile('([\w]+[\']?[\w]?)')
    pattern = re.compile('(?!_\-:\.!)([\w]+[\']?[\w]?[^_\-:\.!\ ]?)')
    text = pattern.findall(text)
    print(text)

    text = map(str.lower, text)
    text = filter(is_unwanted_char, text)
    counter = Counter(text)
    # print(text)

    print(counter.most_common())

    res = []

    for f in counter.most_common(3):
        res.append(f[0])

    return res


def is_unwanted_char(c):
    unwanted_char = ['_', '\'', ';']

    if c not in unwanted_char:
        return True
    return False

