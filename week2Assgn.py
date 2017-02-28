def numbers(n):
	numlist=[]
	while (n>0):
		r=n%10
		numlist=numlist+[r]
		n=n-r
		n=n/10
	return(numlist)
	
def intreverse(n):
	numlist=numbers(n)
	fin=0
	k=len(numlist)
	mul=10**(k-1)
	#return(numlist)
	#return(k)
	for i in range(0,k):
		fin=fin+(numlist[i]*mul)
		mul=mul/10
		fin=int(fin)
	return(fin)
	
def matched(s):
	op=0
	cl=0
	for i in range(0,(len(s))):
		if(s[i]=="("):
			op=op+1
		if(s[i]==")"):
			cl=cl+1
		if(cl>op):
			return(False)
	if(op==cl):
		return(True)
	else:
		return(False)
		
def factors(n):
	factorlist=[]
	for i in range(1,n+1):
		if(n%i)==0:
			factorlist=factorlist+[i]
	return(factorlist)
	
def isprime(n):
	return(factors(n)==[1,n])
	#1 is not counted as prime as output of factors(1) is [1] whereas it should be [1,1] to be qualified as prime

def sumprimes(s):
	sum=0
	for i in range(0,len(s)):
		if(isprime(s[i])==True):
			sum=sum+s[i]
	return(sum)
	
#Hooray!! Week 2 assignment complete!