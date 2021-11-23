import numpy as np
import copy

def CountMotif(motifs):
    count = np.zeros(shape=(4, len(motifs[0])))
    nuclelotide = ['A', 'C', 'G', 'T']
    for m in motifs:
        i = 0
        while i<len(m):
            s = m[i]
            if s=='A':count[0,i] = count[0,i] + 1
            elif s=='C':count[1,i] = count[1,i]+1
            elif s=='G':count[2,i]=count[2,i]+1
            elif s=='T':count[3,i] = count[3,i]+1
            i = i+1
    return count    

def ProfileMotif(motifs):
    l = len(motifs)
    countMotif = CountMotif(motifs)
    profile = copy.deepcopy(countMotif)
    profile = profile/l
    return profile

def pseudo_count_profile(motifs):
    l = len(motifs)
    countMotif = CountMotif(motifs)
    profile = copy.deepcopy(countMotif)
    profile = profile+1
    s=[sum(x) for x in zip(*profile)]
    profile = profile/s[0]
    return profile
    

def Entropy(profile,l):
    entropy=[0]*l
    i = 0    
    entropy_pd = 0
    while i<l:
        for p in profile[:,i]:
            if p!=0:
                entropy[i] = entropy[i] -p*np.log2(p)
        entropy_pd = entropy[i]+entropy_pd
        i=i+1
    print(entropy_pd)
    return entropy_pd

def Score(motifs, t):
    count = CountMotif(motifs)
    xmax = count.max(axis=0)
    score = 0
    for x in xmax:
        score = score+t-x
    return  score    