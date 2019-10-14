import random
import time
import os
import sys
import game_analys

path = os.path.dirname(os.path.abspath(sys.argv[0]))+"\mylisting.txt"
f = open(path, 'w')
f.write("{0:13}{1:10}{2:10}\n".format("Number","Step_old","Step_new"))
#myList = reader_numb(r'C:\Users\Chesare\Desktop\Scripts Python\listing.txt')	

game_analys.mode=1
start_time = time.time()	
	
for bla in range(1000): 
	gameList = game_analys.new_game()
	number = game_analys._int(gameList)
	step=0
	
	flag = True if game_analys._int(gameList) != 123456789 else False
	while flag:
		
		game_analys.reshator()				

		if gameList[0]==0:
			f.write("{0:0>9}    {1:<10}\n".format(number,step))
			flag=False
			continue
		elif gameList[0] != 1:
			for i in range(gameList[0],10): # когда не 0 только первый
				game_analys.make_move(i,"+")
				game_analys.make_move(i,"-")
		else:	
			for i in range(9): # когда первый 1
				game_analys.make_move(2,"+")
				game_analys.make_move(2,"-")
				
		if _int(gameList)==0 and not flag:
			f.write("{0:0>9}    {1:<10}\n".format(number,step))
		elif _int(gameList)==123456789:
			print("Поздравляю, ты проиграл! Шагов %s" %step); flag=False
f.write("--- %s seconds ---" % (time.time() - start_time))
f.close
print("buy")
		










