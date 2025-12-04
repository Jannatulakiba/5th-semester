import random

SuccList ={ 'A':[['T',11],['B',13],['C',21]], 'T':[['D',27],['B',13]],'B':[['D',27],['E',3]], 'C':[['F',25],['G',4]], 'D':[['H',101],['I',99]],'F': [['J',67]]
,'G':[['K',99],['L',3]],'H':[['M',17]],'I':[['M',17]],'J':[['M',17]]}
Start='A'

Closed = list()
Candidate = [['T',11],['B',13],['C',21]]

def MOVEGEN(N):
	New_list=list()
	if N in SuccList.keys():
		New_list=SuccList[N]
	
	return New_list

def SORT(L):
	L.sort(key = lambda x: x[1],reverse=True) 
	return L 
	
def heu(Node): #Node = ['B',2]--> [Node[0],Node[1]]
	return Node[1]

def APPEND(L1,L2):
	New_list=list(L1)+list(L2)
	return New_list

def Iterated_Hill_Climbing(Start,n):
	global Closed
	N=[Start,5]
	bestNode=N
	CLOSED=[N]
	print("\nInitial Point=",N)
	for i in range(1,n+1):
		print("\n*******************************")
		print("For iteration i=",i)
		N= random.choice(Candidate)
		CHILD = MOVEGEN(N[0])
		SORT(CHILD)
		print("\nStart=",N)
		print("Sorted Child List=",CHILD)
		newNode=CHILD[0]
		CLOSED=[N]
	
		while heu(newNode) > heu(N):
			print("\n---------")
			N= newNode
			print("N=",N)
			CLOSED = APPEND(CLOSED,[N])
			CHILD = MOVEGEN(N[0])
			print("Child List=",CHILD)
			SORT(CHILD)
			print("Sorted Child List=",CHILD)
			print("CLOSED=",CLOSED)
			newNode=CHILD[0]
			if heu(newNode) > heu(bestNode):
				bestNode=newNode

	Closed=CLOSED
	return bestNode
	
#Driver Code
bestNode=Iterated_Hill_Climbing(Start,3) #call search algorithm
print("Best Node=",bestNode)

