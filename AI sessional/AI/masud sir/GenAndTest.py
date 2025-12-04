import random
SuccList={'a':['b','c'],'b':['a','c','d'],'c':['a','b','d'],'d':['b','c']}
Start='a'
Goal='d'

SUCCESS=True
FAILURE=False
def GOALTEST(N):
	if N == Goal:
		return True
	else:
		return False

def GEN_CANDIDATE(N):
	New_list=list()
	if N in SuccList.keys():
		New_list=SuccList[N]
	print("New_list=",New_list)
	return New_list
	
def GenAndTest():
	current=Start
	
	while len(current) != 0:
		print("----------------------")
		print("candidate=",current)
		gen_candi=GEN_CANDIDATE(current)
		print("gen_candi=",gen_candi)
		current=random.choice(gen_candi)
		
		if GOALTEST(current):
			print(f"\nGoal is {current} found")
			return SUCCESS
	return FAILURE
	
#Driver Code
result=GenAndTest() #call search algorithm
print(result)
