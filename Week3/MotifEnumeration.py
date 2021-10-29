import findNeighbours

#this is the brute force approach with very high time complexity
#k=length of the k-mers, 
#dist = hamming distance between the k-mers and the dna sequences
#dna = list of dnas
def MotifEnumeration(k,dist,dna):
	patterns = set()
	for d in dna:
		i = 0
		pattern = set()
		while i<len(d)-k+1:
			kmer = d[i:i+k]
			pattern = pattern.union(set(findNeighbours.findNeighbours_atmostd(kmer,dist)))
			i = i+1
		
		if len(patterns)==0: patterns = patterns.union(pattern)
		else: patterns = patterns-(patterns-pattern)				
	print (" ".join(str(x) for x in patterns))
	return patterns