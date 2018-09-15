# class word:
    # def __init__(self, char, left=None, right=None):
        # self.left = []
        # self.right = []
        # self.char = char

# words = []

from collections import defaultdict

def dfs(graph, v):
    stack = []
    discovered = []

    stack.append(v)

    while(stack!=[]):
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for i in graph[v]:
                stack.append(i)

    return discovered

def visit(graph, v, visited, stack):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            visit(graph, i, visited, stack)

    if v not in stack:
        stack.append(v)



def toposort(graph, letter_set):
    stack = []
    visited = {}
    print(letter_set)
    for i in letter_set:
        visited[i] = False
    unmarked = list(graph.keys())

    for i in unmarked:
        visit(graph, i, visited, stack)

    return stack

def recoverSecret(triplets):
    letter_set = set()
    left = defaultdict(set)
    right = defaultdict(set)
    # out_vert = defaultdict(int)
    # in_vert = defaultdict(int)


    for t in triplets:
        # words.append(word(trplt[1], trplt[0], trplt[2]))
        letter_set.update(t)

        left[t[1]].add(t[0])
        right[t[1]].add(t[2])

        left[t[2]].add(t[0])
        left[t[2]].add(t[1])

        right[t[0]].add(t[1])
        right[t[0]].add(t[2])

    # for i in left:
        # out_vert[i] += len(left[i])
        # for j in left[i]:
            # out_vert[j] -= 1

    # for i in right:
        # in_vert[i] += len(right[i])
        # for j in right[i]:
            # in_vert[j] -= 1

    for i in right:
        for j in right[i]:
            left[j].add(i)


    # print(dfs(left, 't'))
    return "".join(toposort(left, list(letter_set)))


    # __import__('pprint').pprint(left)
    # __import__('pprint').pprint(right)
    # __import__('pprint').pprint(out_vert)
    # __import__('pprint').pprint(in_vert)








