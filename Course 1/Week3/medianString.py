import distBtwPnString
import math

def k_gen(k):
    kmers = [""]
    for i in range(k):
        for elements in set(kmers):
            kmers.append(elements+'A')
            kmers.append(elements+'T')
            kmers.append(elements+'G')
            kmers.append(elements+'C')
            kmers.remove(elements)
    return set(kmers)

def Median_String(Dna,k):
    dist = math.inf
    medianS = set()
    kmers = k_gen(k)
    for kmer in kmers:
        d = distBtwPnString.DistanceBetweenPatternAndStrings(kmer,Dna)
        if d==dist:
            dist = d
            medianS.add(kmer)
        elif d<dist:
            dist =d
            medianS.clear()
            medianS.add(kmer)
    return medianS
    
def main():
    k = int(input())
    Dna = input().split()
    print("      ")
    medianS = Median_String(Dna,k)
    print (" ".join(str(x) for x in medianS))
    return

main()