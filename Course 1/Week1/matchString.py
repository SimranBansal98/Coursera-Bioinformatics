pattern = "ATGATCAAG"
i = 0
count = 0
while i<len(seq):
	
	p = seq[i:i+len(pattern)]
	if p==pattern:
		count = count+1
		print (i)
	i = i+1
print()
print(count)