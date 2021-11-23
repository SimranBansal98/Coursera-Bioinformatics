import time
start_time = time.time()

f = open('E_Coli.txt', 'r')
text = f.read() 
k = 9
l = 500
t = 3


def freqMap(seq, length, t):
	pattern = {}	
	i=0
	fmap = set()
	while i<(len(seq)-length):
		p = seq[i:i+length]
		if p in pattern:
			pattern[p] = pattern[p]+1
		else:
			pattern[p] = 1
		i = i+1

	for p in pattern:
		if pattern[p]>=t:
			fmap.add(p)

	return fmap


def findClumps(text, k, l , t):
	pattern = set()
	n = text
	i = 0
	while i<(len(n)-l+1):
		window = n[i:i+l]
		s = freqMap(window, k, t)
		if s:
			pattern = pattern.union(s)
		i=1+i
	print(len(pattern))
	return

findClumps(text,k,l,t)

print(time.time()-start_time)

##1904 - got it.