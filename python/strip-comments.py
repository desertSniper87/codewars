import re

def solution(string, markers):
    # s = re.search('#.*\n', string)
    if markers==[]:
        return string

    pattern = r'[ ]?['
    for i in markers:
        pattern += '\\' + i  
    pattern += ']'

    pattern1 = pattern + '.*\n'
    pattern2 = pattern + '.*$'

    print(pattern1)
    print(pattern2)

    string = re.sub(pattern1, '\n', string)
    string = re.sub(pattern2, '', string)
    print(string)
    return string 
    # for _ in s:
        # print(_)


import nose.tools as Test

# solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas"
try:
    # Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
    # Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
    # Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", []), "apples, pears # and bananas\ngrapes\nbananas !apples")
    Test.assert_equals(solution("cherries avocados\noranges avocados apples bananas bananas\npears strawberries watermelons watermelons apples\n@ pears apples pears lemons oranges\n' pears bananas lemons strawberries bananas", ['#', '-', ',', '^', '?', '=', '!', '@', '.']), "cherries avocados\noranges avocados apples bananas bananas\npears strawberries watermelons watermelons apples\n\n' pears bananas lemons strawberries bananas")
except AssertionError as s:
    print(s)
