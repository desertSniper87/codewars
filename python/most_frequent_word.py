from collections import Counter
import re


def top_3_words(text):
    pattern = re.compile('[\.:?;_\-,!/]+')
    text = re.sub(pattern, ' ', text)

    pattern = re.compile('[^\w][\']+[^\w]')
    text = re.sub(pattern, '', text)

    text = text.lower().split()

    counter = Counter(text)
    print(counter.most_common())

    print(text)

    ret = []

    for i in counter.most_common(3):
        ret.append(i[0])

    return ret
