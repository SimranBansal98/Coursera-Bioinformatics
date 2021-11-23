#error in this file

import time
start_time = time.time()

def checkClump(listFreq, l,t): #checking if the number of k-mers are greater than t in a clump of size l
	if len(listFreq)<t: return False
	i=0
	while i<(len(listFreq)-t+1):
		j = i+t-1
		if (listFreq[j]-listFreq[i])<l:return True
		i = i+1
	return False

def listDistPattern(pattern, l, t): #getting the locations of each k-mer
	clumpPatterns = set()
	for key in pattern:
		freqDist = pattern.get(key)
		clumpExist = checkClump(freqDist, l , t)
		if clumpExist:clumpPatterns.add(key)
	print(len(clumpPatterns))
	return	

def findPattern(text, k): #finding the location of all the k-mers and storing it in a dictionary
	pattern = {}
	i=0
	while i<=(len(text)-k):
		s = text[i:i+k]
		if s in pattern:
			pattern[s].append(i)
		else:
			pattern.setdefault(s,[])
			pattern[s].append(i)
		i = i+1
	return pattern	

def main():
	k = 9#5 		#length of the n-mer
	l = 500#50		#length of the clump
	t = 3#4			#number of times n-mer should be in clump
	f = open('E_Coli.txt', 'r')
	text = f.read() 
	#text = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"

	pattern = findPattern(text,k)
	listDistPattern(pattern, l,t)
	print(time.time()-start_time)
	return

main()

#1904 - getting 1910 - there is an error.. find it.
