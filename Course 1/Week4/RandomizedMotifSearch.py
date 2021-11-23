import random
import sys
from numpy.core.numeric import Infinity

sys.path.insert(0, './Week3')
from helperFunctions import pseudo_count_profile, Score
from mostProbableKmer import MostProbableKmer, getKmers

def get_kmers(dna, l):
    ## l = length of kmers--->should be k
    ## ld = length of dna sequence
    kmers = list()
    i=0
    D = dna
    ld = len(D) 
    while i<=ld-l:
        kmers.append(D[i:i+l])
        i=i+1
    return kmers

def randomized_motif_search(Motifs, k,t,dna):
    ##in this funntion we get best motifs and best score for 1 iteration
    
    bestMotifs = Motifs
    best_score = Score(bestMotifs, t)
        
    while True:
        profile = pseudo_count_profile(bestMotifs)
        motifs = list()
        for d in dna:
            m = MostProbableKmer(profile,d,k)
            motifs.append(m)
        score = Score(motifs,t)
        if score < best_score:
            bestMotifs = motifs
            best_score = score
        else:
            break
    
    return bestMotifs, best_score

if __name__ == '__main__':
    k =int(input())
    t=int(input())
    #k=8
    #t=5
    #dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
    dna= input().split()

    kmers = []
    for d in dna:
        kmers.append(getKmers(d,k))
    
    BestMotifs= list()
    BestScore= Infinity
    
    i=1
    while i!=1000:
        random_motifs = list()
        
        for kmer in kmers:
            random_motifs.append(random.choice(kmer))
        
        (Motifs, score) = randomized_motif_search(random_motifs,k,t,dna)
        
        if score<BestScore:
            BestScore = score
            BestMotifs = Motifs
        i=i+1
    print(BestScore)   
    print(*BestMotifs, sep=" ")