import time
start_time = time.time()

def filterPattern(pattern, t):
	p = set()
	for key in pattern:
		if len(pattern[key])>=t:
			p.add(key)
	return p


def findPattern(text, k):
	pattern = {}
	i=0
	while i<(len(text)-k):
		s = text[i:i+k]
		if s in pattern:
			pattern[s].append(i)
		else:
			pattern[s] = list()
			pattern[s].append(i)
		i = i+1
	return pattern	

k = 9#5 	#length of the n-mer
l = 500#50 	#length of the clump
t = 3#4	#number of times n-mer should be in clump
f = open('E_Coli.txt', 'r')
text = f.read()
#text = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
countPatterns = set()
count = 0
length = len(text)

while count<=(length-l+1):	
	window = text[count:count+l-1]
	pattern = findPattern(window, k)
	p = filterPattern(pattern , t)
	countPatterns = countPatterns.union(p)
	count = count+1	

print(countPatterns)
print(len(countPatterns))
print(time.time()-start_time)

#1904
#this is longer and it sucks.. improvised is better - correct it.