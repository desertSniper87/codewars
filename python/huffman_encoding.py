class Node:
    left = None
    right = None
    val = None
    char = None
    def __init__(self, val=0, char=None, left=None, right=None):
        self.left = left
        self.right = right
        if left!=None and right!=None:
            self.val = left.val + right.val
        else:
            self.val = val
        self.char = char

    @classmethod
    def leafNode(cls, v, c):
        return cls(val=v, char=c, left=None, right=None)

    @classmethod
    def irNode(cls, left, right):
        if left.val<right.val:
            return cls(left=right, right=left)
        else:
            return cls(left=left, right=right)



def traverse(n, code={}, stack=[]):
    print("code, stack: ", code, stack)
    print(n.char, n.val)
    if (n.left!=None):
        print(stack)
        print("left")
        stack.append('0')
        traverse(n.left)

    if (n.right!=None):
        print(stack)
        stack.append('1')
        print("right ")
        traverse(n.right)

    if (n.char!=None):
        code[n.char]=''.join(x for x in stack)
        stack.pop()

    return code



def frequencies(s):
    l = []
    for i in set(s):
        l.append((i, s.count(i)))

    l.sort(key=lambda tup:tup[1] )
    return l

def encode(freqs, s):
    print("freqs, s: ", freqs, s)
    print("type(freqs), type(s): ", type(freqs), type(s))
    if freqs==[] and s=='':
        return None
    elif freqs==[] and s!='':
        return None
    elif freqs!=[] and s=='':
        return None
    elif freqs!=[] and s==[]:
        return ''


    x = freqs.pop(0)
    n1 = Node.leafNode(x[1], x[0])
    x = freqs.pop(0)
    n2 = Node.leafNode(x[1], x[0])

    n = Node.irNode(n1, n2)


    for i in freqs:
        n = Node.irNode(n, Node.leafNode(i[1], i[0]))


    # print("code, stack: ", code, stack)
    code = traverse(n)
    # code = traverse(n, code={}, stack=[])
    print(code)
    output = ""

    # print(code)

    for i in s:
        output += code[i]

    return output 
  
# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    return ""

a = "aaaabcc"

l = frequencies(a)
t = []
for i in l:
    t.append(list(i))
print(t)

encoded_string = (encode(frequencies(a), a))
print(len(encoded_string))


a = "vbbbvvbbbbv"
l = frequencies(a)
encoded_string = (encode(frequencies(a), a))
# print(encoded_string)

a = "ababababa"
l = frequencies(a)
encoded_string = (encode(frequencies(a), a))
print(encoded_string)

print(encode([("a", 1)], ""))
encode([('a', 1), ('b', 1)], "ab")
print(encode([], ""))

# import unittest

# fs = frequencies("aaaabcc")

# t = unittest.TestCase()

# t.assertEqual( encode( fs, "" ), "" )
# t.assertEqual( decode( fs, "" ), "" )

# t.assertEqual( encode( [], "" ), None );
# t.assertEqual( decode( [], "" ), None );
# t.assertEqual( encode( [('a', 1)], "" ), None );
# t.assertEqual( decode( [('a', 1)], "" ), None );
