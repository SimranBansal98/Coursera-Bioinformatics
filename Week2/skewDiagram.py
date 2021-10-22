def minSkew(dia):
	a = min(dia)
	i = 0
	minSkewPos = list()
	while i<len(dia):
		if dia[i]==a: minSkewPos.append(i)
		i=i+1
	print(*minSkewPos, sep=' ')
	print()
	return

def skewDiagram(seq):
	i=0
	dia = [0]
	while i<len(seq):
		if seq[i]=='C':

			dia.append(dia[i]-1)
		elif seq[i]=='G':

			dia.append(dia[i]+1)
		else: 
			dia.append(dia[i])
		i=i+1
	return dia	
		

def main():
	#seq = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
	#f = open('dataset_7_10.txt', 'r')
	#seq = f.read() 
	seq = 'CATTCCAGTACTTCGATGATGGCGTGAAGA'
	dia = skewDiagram(seq)
	minSkew(dia)
main()