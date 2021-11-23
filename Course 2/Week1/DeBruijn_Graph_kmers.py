from collections import defaultdict

def add_edge(graph,u,v):
    graph[u].append(v)

def debruijn(patterns):
    graph = defaultdict(list)
    for i in range(len(patterns)):
        pattern = patterns[i]
        L = len(pattern)
        u = pattern[0:L-1]
        v = pattern[1:L]
        add_edge(graph,u,v)
    f =open("debrujin.txt", "w")
    for key in graph:
        f.write("%s" %key)
        f.write("->")
        lst = map(str, graph[key])
        line = ",".join(lst)
        f.write("%s\n" %line)


with open("input.txt") as file:
        patterns = file.readlines()
        patterns = [line.rstrip() for line in patterns]

debruijn(patterns)