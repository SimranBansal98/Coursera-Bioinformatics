import numpy
#l = length of the k-mers

def getKmers(dna, l):
    kmers = list()
    i=0
    D = dna
    ld = len(D)
    while i<=ld-l:
        kmers.append(D[i:i+l])
        i=i+1
    return kmers

def MostProbableKmer(profile, kmers):
    profile = numpy.array(profile)
    #print(profile)
    probableKmer=None
    probability = 0
    for k in kmers:
        p_k = 1
        chars = list(k)
        i = 0
        while i<len(chars): 
            c = chars[i]
            if c=='A':p_k=p_k*profile[0,i]
            elif c=='C':p_k=p_k*profile[1,i]
            elif c=='G':p_k = p_k*profile[2,i]
            elif c=='T':p_k=p_k*profile[3,i]
            i = i+1
            #print(c,p_k)
        #print(k,p_k)
        
        if p_k==probability:
            if not probableKmer:
                probability = p_k
                probableKmer = k
        elif p_k>probability:
            probability = p_k
            probableKmer = k

    return probableKmer

def main(profile,dna,l):
    kmers = getKmers(dna,l)
    probableKmer = MostProbableKmer(profile, kmers)
    #print(probableKmer)
    return probableKmer

dna = "CACGTCAATCAC"
profile = [[0.6, 0.6, 0],
    [0.33333333, 0.         ,0.        ],
    [0.         ,0.33333333 ,0.66666667],
    [0.         ,0.         ,0.33333333]]
l=3
main(profile,dna,l)