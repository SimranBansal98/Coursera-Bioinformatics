from collections import defaultdict

def add_edge(graph,u,v):
    graph[u].append(v)

def debruijn(dna,k):
    graph = defaultdict(list)
    for i in range(len(dna)-k+1):
        u = dna[i:i+k-1]
        v = dna[i+1:i+k]
        add_edge(graph,u,v)
    f =open("debrujin.txt", "w")
    for key in graph:
        f.write("%s" %key)
        f.write("->")
        lst = map(str, graph[key])
        line = ",".join(lst)
        f.write("%s\n" %line)

dna = "TAATGCCATGGGATGTT"
k = 2
debruijn(dna,k)