import random

q = input("What is bothering you?:")
x = int(input("How many alternatives do you have?")); # int which saves the number of decisions
d = [input("Share the alternative") for i in range(0,x)] # variables to be decided 
if(input("do you they have the same probability? (y/n)") == 'y'):#check if the probability of each symbol is different
	p = [float(input("insert the probability of the event " + d[i] + '\n' )) for i in range(0,x) ] #probability of echa decision
	if(sum(p) != 1 ): #if the sum of each decision isn't equal to one
		print("do it again")
	print(random.choices(d, p))#print the decision	
else:#if there isn't different probability among the decisions
	print(d[random.randint(0,x-1)])
