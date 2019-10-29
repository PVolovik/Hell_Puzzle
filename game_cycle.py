import random
import time
import os
import sys
import game_analys

start_time = time.time()

path = os.path.dirname(os.path.abspath(sys.argv[0]))+"\mylisting.txt"
myList = game_analys.reader_numb(path)
f = open(path, 'w')
f.write("{0:13}{1:10}{2:10}\n".format("Number","Step_old","Step_new"))

	
for bla in myList:
	cur_numb = game_analys.NewGame(bla[0], mode=1, old_step=bla[1])

	flag = True if cur_numb.start != "123456789" else False
	while flag:
		
		cur_numb.reshator()

		if cur_numb.gameList[0]==0:
			f.write("{0:0>9}    {1:<10}{2}\n".format(cur_numb.start,cur_numb.old_step, cur_numb.step))
			flag=False
			continue
		elif cur_numb.gameList[0] != 1:
			for i in range(cur_numb.gameList[0],10): # когда не 0 только первый
				cur_numb.make_move(i,"+")
				cur_numb.make_move(i,"-")
		else:	
			for i in range(9): # когда первый 1
				cur_numb.make_move(2,"+")
				cur_numb.make_move(2,"-")
				
		if game_analys.list_int(cur_numb.gameList)==0 and not flag:
			f.write("{0:0>9}    {1:<10}{2}\n".format(cur_numb.start,cur_numb.old_step, cur_numb.step))
		elif game_analys.list_int(cur_numb.gameList)==123456789:
			print("Случился косяк на шаге %s" %cur_numb.step); flag=False
f.write("--- %s seconds ---" % (time.time() - start_time))
f.close
print("buy")
		










