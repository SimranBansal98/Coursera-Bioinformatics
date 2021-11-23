import helperFunctions as hfn
import mostProbableKmer as mpk

def greedymotifsearch(dna,k,t):
    bestMotifs = [d[:k] for d in dna]
    bestScore = hfn.Score(bestMotifs,t)
    kmer = mpk.getKmers(dna[0], k)
    for km in kmer:
        motif =[]
        motif.append(km)
        j=1
        while j<t:
            profile = hfn.ProfileMotif(motif)
            mp = mpk.main(profile,dna[j],k)
            motif.append(str(mp))
            j = j+1
        score = hfn.Score(motif, t)    
        if score<bestScore:
            bestScore = score
            bestMotifs = motif
    
    return bestMotifs

def main():
    k = int(input())
    t = int(input())
    dna = input().split()
    bestMotif = greedymotifsearch(dna,k,t)
    print(*bestMotif, sep= " ")

main()