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
	print(dist)	
	return dist

def main():
	seq1 = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
	seq2 = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'
	hammingDist(seq1, seq2)

main()			