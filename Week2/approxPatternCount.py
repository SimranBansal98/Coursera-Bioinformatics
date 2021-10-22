def hammingDist(seq1, seq2, distance):
	if len(seq1)!=len(seq2):
		raise Exception("Length of strings not same")
		return 
	i = 0
	dist = 0
	while i<len(seq1):
		if seq1[i]!=seq2[i]:
			dist = 1 +dist
		i = i+1

	if dist<=distance:
		return True
	return False

def main():
	seq1 = 'TGT'
	sequence = 'CGTGACAGTGTATGGGCATCTTT'
	lenSeq1 = len(seq1)
	distance = 1
	i = 0
	matches = list()
	while i<(len(sequence)-lenSeq1+1):
		seq2 = sequence[i:i+lenSeq1] 
		if hammingDist(seq1, seq2, distance):
			matches.append(i)
		i = i+1
	print(*matches, sep=' ')
	print(len(matches))
main()	