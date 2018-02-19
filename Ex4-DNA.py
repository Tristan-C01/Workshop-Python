dna=open("DNA.txt").read()
a=0.0
b=len(dna)
for x in range (0,b):
    if(dna[x]=='C'):
        a=a+1
    elif(dna[x]=='G'):
        a=a+1
d=(a/b)*100
print "The percentage of C and G in the DNA code is ",d
