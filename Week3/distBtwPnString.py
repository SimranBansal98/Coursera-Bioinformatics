import math

def hammingDist(seq1, seq2):
	l = len(seq1)
	i = 0
	dist = 0
	while i<l:
		if seq1[i]!=seq2[i]:
			dist = 1 +dist
		i = i+1
	return dist


def DistanceBetweenPatternAndStrings(pattern,dna):
    dist = 0
    for d in dna:
        D=str(d)
        hDist = math.inf
        lp = len(pattern)
        ld = len(D)
        i=0
        while i<(ld-lp+1) :
            p = D[i:i+lp]
            d = hammingDist(pattern,p)
            if d<hDist:
                hDist = d
            i=i+1
        dist = dist+hDist
    return dist