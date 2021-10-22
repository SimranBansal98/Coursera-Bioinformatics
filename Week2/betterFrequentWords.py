#for an input genome sequence, objective is to find all the k-mers with highest mismatches.
#Step 1 - 	for a selected length k of the k-mers, find all the k-mers in its d-neighbourhood i.e. with ATMOST d mismatches
#Step 2 - 	count all the mismatches of all the k-mers
#Step 3 - 	Now, find the mos frequent mimatch

#Example - Text = 'AGT', kmer length of k = 2 and mismatches d = 1
#K-mers from AGT = AG and GT
#for k-mer AG with 1 allowed mimatches, neighborhood = {AT, AC, AA, CG, TG, GG}
#similarly, for GT = {GG, GA, GC, TT, AT, CT}
#freqMap = {AT = 2; AC = 1; AA=1; CG=1; TG=1; GG=2;GA=1;GC=1;TT=1; CT=1}
#maxFreq = 2
#and so, mismatches with maxFreq = patterns = {AT, GG}=> Result required

import time
start_time = time.time()

def findNeighbours(pattern,d):
	neighbourhood = []
	##checks for pattern of length 0 and if the length is 0, returns an empty list	
	if len(pattern)==0:return(neighbourhood)
	##if d==0, it means no change is requires in the sequence and so the sequence is returned in the form of a list
	if d==0:return(neighbourhood.append(pattern))

	##if length of sequence is 1, then by default d cannot be any value other than 1 and therefore, the simple string is returned
	if len(pattern)==1: return(['A', 'G', 'C', 'T'])

	##the actual computation is occurring here, if d==1, then it changes the string at every position for all ATGC and returns the list 
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

	length = len(pattern) ##storing the length of pattern in a variable for covinience
	subPattern = pattern[1:]##this would be the pattern that would be called until d=0
	intitalPattern = pattern[0]#this is the suffix

	#Case1-----
	#Not changing the character at initial position of the string so, at this point d = 0
	#for the rest of the subpattern, calling the function again and so, from here d=d
	s1 = []
	suffixPatternNeighbours1 = findNeighbours(subPattern, d)
	for x in suffixPatternNeighbours1:
		s1.append(intitalPattern + x)
	
	#Case 2------
	#Changing the intial character of the pattern and so, d=1 has been done 
	#for the remaining subpattern, again calling the fucntion for d-1 changes
	s2 = []
	suffixPatternNeighbours2 = findNeighbours(subPattern, (d-1))
	prefixPatternNeighbours = ['A', 'G', 'C', 'T']
	for x in prefixPatternNeighbours:
		for y in suffixPatternNeighbours2:
			s2.append((x+y))

	#combining the values obtained from the above two cases
	neighbourhood = neighbourhood + s1+s2
	return neighbourhood


def frequentWordsWithMismatches(text,k,d):
	patterns = [] ##this will be the final list of frequent wotds with mimatches
	freqMap = {} ##this dicitonary for saving the frquency of elements occuring in neighbourhood of k-mers of text
	i=0
	while i<=(len(text)-k):
		pattern = text[i:(i+k)]
		if d!=0:
			##finding the neighbourhood of the pattern i.e. the all the strings with d number of mutations using the function findNEighbours()
			neighbourhood = findNeighbours(pattern, d)
			##Since the original function includes the original pattern too, so,removing it
			neighbourhood.remove(pattern)
			#converting to list to remove repeats
			neighbourhood = set(neighbourhood)
			#iterating over neighbours and counting the frequency of each element of neighbours and storing it in the dicitonary
			for n in neighbourhood:
				if n in  freqMap:
					##if n is already present in the freqMap, adding it's frquency by 1
					freqMap[n] = freqMap[n]+1
				else:
					## if n is not present in the freqMap, adding it to the same and setting it's original frquency to 1
					freqMap[n] = 1
		else:
			##if d = 0, do't need to run the above complex algo and so, for simplicity, added this section
			if pattern in  freqMap:
				freqMap[pattern] = freqMap[pattern]+1
			else:
				freqMap[pattern] = 1
		i = i+1	

	##converting values of dicitionary into list and storing it in 'freq' 
	freq = freqMap.values()	
	##finding the max frequency because this value will find thw words with most mismatches
	maxFreq = max(freq)
	#For the maximum frquency, finding all the macthing patterns
	for pattern in freqMap:
		if freqMap[pattern]==maxFreq:
			patterns.append(pattern)

	##returning the set of the patterns
	return set(patterns)
	

def main():
	
	##given or known
	text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
	k = 4
	d = 1

	##
	patterns = frequentWordsWithMismatches(text,k,d)
	print (*patterns, sep=' ')
	print(len(patterns))
	print(time.time()-start_time)
	return

main()