import random
import time
import os
import sys

def _int(L):
	num = 0
	for i, v in enumerate(reversed(L)):
		num += v * 10 ** i
	return num

def reader_numb(path):
	res = [(int(x[7:16]),int(x[24:-1])) for x in open(path).readlines()]
	return res
	
def make_move(pos, sign):
	global gameList, step
	pos = int(pos)
	# step_move = 0
	# pos1, sign1 = pos, sign
	if sign == "+":
		if gameList[pos-1]-1==-1:
			gameList[pos-1] = gameList[pos-1] + 1 if gameList[pos-1]!=9 else 0
		else:
			gameList[gameList[pos-1]-1] = gameList[gameList[pos-1]-1]-1 if gameList[gameList[pos-1]-1]!=0 else 9
			gameList[pos-1] = gameList[pos-1] + 1 if gameList[pos-1]!=9 else 0
			
	elif sign == "-":
		if gameList[pos-1]-1==-1:
			gameList[pos-1] = gameList[pos-1] - 1 if gameList[pos-1]!=0 else 9
		else:
			gameList[gameList[pos-1]-1] =gameList[gameList[pos-1]-1] + 1 if gameList[gameList[pos-1]-1]!=9 else 0
			gameList[pos-1] = gameList[pos-1] - 1 if gameList[pos-1]!=0 else 9
	step +=1

def zeroing(pos, q=0):
	flag = gameList[pos-1]
	while gameList[pos-1] !=0 or gameList[pos-1]==pos:
		if gameList[pos-1] > pos: make_move(pos,"+")
		elif gameList[pos-1] < pos: make_move(pos,"-")
		else: break
	if flag!=1 and q!=0:
		rep = pos if gameList[pos-2]==0 else pos+1
		for j in range(2, rep):
			zeroing(j)
			
def not_problem():
	global gameList
	
	for i in range(2,10):
		zeroing(i); 
		sw = i if gameList[i-2]==0 else i+1
		for j in range(2, sw):
			zeroing(j, 1)
			
def problemator():
	global gameList, step
	problempos = []
	for i in range(len(gameList)):
		if i+1==gameList[i]: problempos.append(i+1)
	return problempos

def reshator():
	global gameList
	
	while _int(gameList[1:])!=0:
		not_problem()
		
		problem=problemator()
		#problem = 
		if problem:
			for i in range(9):
				if gameList[i] == 0 and i+1>problem[0]: 
					for j in range(problem[0]): make_move(i+1,"+"); #print("tut")
					make_move(i+1,"-")
					zeroing(problem[0])
				elif gameList[i] == 0 and i+1<problem[0]: 
					for j in range(problem[0]): make_move(i+1,"-"); #print("tut")
					make_move(i+1,"+")
					zeroing(problem[0])
				else: continue
		not_problem()		
				
		if _int(gameList[1:])!=0 and _int(gameList[1:])>10:		
			for i in gameList[1:]:
				if i==0: continue
				else:
					for j in range(1,i+1):
						make_move(9,"+"); 
			make_move(9,"-")
		if _int(gameList[1:-1])==0 and gameList[-1]==9: make_move(2,"-")


def new_game(numb=0):
	new_numb = numb if numb!=0 else [random.randint(0,9) for i in range(9)]
	return new_numb


path = os.path.dirname(os.path.abspath(sys.argv[0]))+"\mylisting.txt"
f = open(path, 'w')
f.write("{0:13}{1:10}{2:10}\n".format("Number","Step_old","Step_new"))
#myList = reader_numb(r'C:\Users\Chesare\Desktop\Scripts Python\listing.txt')	

start_time = time.time()	
	
for bla in range(100): 
	gameList = new_game()
	number = _int(gameList)
	step=0
	
	flag = True if _int(gameList) != 123456789 else False
	while flag:
		
		reshator()				

		if gameList[0]==0:
			f.write("{0:0>9}    {1:<10}\n".format(number,step))
			flag=False
			continue
		elif gameList[0] != 1:
			for i in range(gameList[0],10): # когда не 0 только первый
				make_move(i,"+")
				make_move(i,"-")
		else:	
			for i in range(9): # когда первый 1
				make_move(2,"+")
				make_move(2,"-")
				
		if _int(gameList)==0 and not flag:
			f.write("{0:0>9}    {1:<10}\n".format(number,step))
		elif _int(gameList)==123456789:
			print("Поздравляю, ты проиграл! Шагов %s" %step); flag=False
f.write("--- %s seconds ---" % (time.time() - start_time))
f.close
print("buy")
		










