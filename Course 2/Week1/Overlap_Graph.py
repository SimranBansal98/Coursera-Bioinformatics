def overlap_graph(kmers):
    N  = len(kmers)
    back = list()
    front = list()
    for i in range(N):
        kmer = kmers[i]
        L = len(kmer)
        front.append(kmer[0:L-1])
        back.append(kmer[1:L])
    
    dict = {}
   
    outputFile = open("String_Composition.txt", "w")

    for i in range(N):
        b = back[i]
        dict[kmers[i]] = []
        for j in range(N):
            if b == front[j]:
                dict[kmers[i]].append(kmers[j])
        if dict[kmers[i]]==[]:
            del dict[kmers[i]]
        else:
            outputFile.write("%s" %kmers[i])
            outputFile.write("->")
            lst = map(str, dict[kmers[i]])
            line = ",".join(lst)
            outputFile.write("%s\n" %line)

    

if __name__ == '__main__':
    with open("input.txt") as file:
        kmers = file.readlines()
        kmers = [line.rstrip() for line in kmers]
    overlap_graph(kmers)             