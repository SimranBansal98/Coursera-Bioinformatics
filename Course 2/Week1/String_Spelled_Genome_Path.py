def string_spelled(kmers):
    N = len(kmers) ##Number of kmers  
    path = kmers[0]
    for i in range(1,N):
        kmer = kmers[i]
        path = path+kmer[-1]
    print (path)

if __name__ == '__main__':
    with open("input.txt") as file:
        kmers = file.readlines()
        kmers = [line.rstrip() for line in kmers]
    string_spelled(kmers)