import random

SuccList ={ 'A':[['T',11],['B',13],['C',21]], 'T':[['D',27],['B',13]],'B':[['D',27],['E',3]], 'C':[['F',25],['G',4]], 'D':[['H',101],['I',99]],'F': [['J',67]]
,'G':[['K',99],['L',3]],'H':[['M',17]],'I':[['M',17]],'J':[['M',17]]}
Start='A'

Closed = list()
def MOVEGEN(N):
	New_list=list()
	if N in SuccList.keys():
		New_list=SuccList[N]
	
	return New_list

def heu(Node): #Node = ['B',2]--> [Node[0],Node[1]]
	return Node[1]

def APPEND(L1,L2):
	New_list=list(L1)+list(L2)
	return New_list

def Random_Walk(Start,n):
	global Closed
	node=[Start,5]
	bestNode=node
	CLOSED=[node]
	print("\nInitial Point=",node)
	for i in range(1,n+1):
		print("\n*******************************")
		print("For iteration i=",i)
		CHILD = MOVEGEN(node[0])
		if(len(CHILD) != 0):
			node=random.choice(CHILD)
			CLOSED=APPEND(CLOSED,[node])
			print("\nCurrent node=",node)
			print("Closed List=",CLOSED)
			if heu(node) > heu(bestNode):
				bestNode=node

	Closed=CLOSED
	return bestNode

#Driver Code
bestNode=Random_Walk(Start,4) #call search algorithm
print("Best Node=",bestNode)