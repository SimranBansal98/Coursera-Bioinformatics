##this function has been described in betterFrequentWords.py
def hammingDist(seq1, seq2):
	if len(seq1)!=len(seq2):
		raise Exception("Length of strings not same")
		return 
	l = len(seq1)
	i = 0
	dist = 0
	while i<l:
		if seq1[i]!=seq2[i]:
			dist = 1 +dist
		i = i+1
	return dist

def findNeighbours_exactlyd(pattern, neighbourhood, d):
	neighbourhood_atmost = set()
	for x in neighbourhood:
		if d == hammingDist(pattern,x):
			neighbourhood_atmost.add(x)
	return neighbourhood_atmost
		
def findNeighbours_atmostd(pattern,d):
	neighbourhood = []	
	if len(pattern)==0:return(neighbourhood)
	if d==0:return(neighbourhood.append(pattern))
	if len(pattern)==1: return(['A', 'G', 'C', 'T'])

	if d==1:
		i=0
		while i<len(pattern):
			s1 = pattern
			s1 = s1[:i]+'A'+s1[i+1:]
			neighbourhood.append(s1)
			s1 = s1[:i]+'G'+s1[i+1:]			
			neighbourhood.append(s1)
			s1 = s1[:i]+'C'+s1[i+1:]
			neighbourhood.append(s1)
			s1 = s1[:i]+'T'+s1[i+1:]
			neighbourhood.append(s1)
			i = i+1
		return neighbourhood


	length = len(pattern)
	subPattern = pattern[1:]
	intitalPattern = pattern[0]

	s1 = []
	suffixPatternNeighbours1 = findNeighbours_atmostd(subPattern, d)
	for x in suffixPatternNeighbours1:
		s1.append(intitalPattern + x)
	
	s2 = []
	suffixPatternNeighbours2 = findNeighbours_atmostd(subPattern, (d-1))
	prefixPatternNeighbours = ['A', 'G', 'C', 'T']
	for x in prefixPatternNeighbours:
		for y in suffixPatternNeighbours2:
			s2.append((x+y))

	neighbourhood = neighbourhood + s1+s2
	return neighbourhood

def main():
	pattern ='ACGT'
	d=3
	neighbourhood = findNeighbours_atmostd(pattern, d)
	neighbourhood = set(neighbourhood)
	print(len(neighbourhood))
	#neighbourhood_atmost = findNeighbours_exactlyd(pattern,neighbourhood, d)
	#print(*neighbourhood_atmost, sep=' ')
	#print(len(neighbourhood_atmost))

main()