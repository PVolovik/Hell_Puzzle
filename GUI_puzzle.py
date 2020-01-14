from tkinter import *
from PIL import Image, ImageTk
from game_analys import *
from tkinter import messagebox

cur_numb = NewGame(0)
def new_game():
    global cur_numb
    cur_numb = NewGame(0)
    set_value()

def set_value():
    global cur_numb
    for i in range(9):
        elem = Label(width=3, text=str(cur_numb.gameList[i]), font="Arial 18", fg='#006400', justify=CENTER, relief=GROOVE)
        params = {'ipadx': 1, 'ipady': 3, 'padx': 1, 'pady': 1}
        elem.grid(row=2, column=i, **params)

    if list_int(cur_numb.gameList) == 0:
        messagebox.showinfo("Ура!", "Ты выйграл!")
    elif list_int(cur_numb.gameList) == 123456789:
        messagebox.showinfo("Ура!", "Ты проиграл!")

def value_up(pos):
    global cur_numb
    cur_numb.make_move(pos,'+')
    steps['text'] = f"Шагов: {cur_numb.step}"
    set_value()

def value_down(pos):
    global cur_numb
    cur_numb.make_move(pos,'-')
    steps['text'] = f"Шагов: {cur_numb.step}"
    set_value()

root = Tk()
root.title("Hell Puzzle")
root.geometry('800x400+400+200')


start_game_btn = Button(root, text="New game", command=new_game)
start_game_btn.grid(row=0, column=3, columnspan=3, ipadx=10, ipady=6, padx=10, pady=10)


ar_up = ImageTk.PhotoImage(Image.open('Arrow-Up.gif'))
ar_down = ImageTk.PhotoImage(Image.open('Arrow-Down.gif'))

params={}

for r in range(1,5):
    for c in range(9):
        if r==1:
            elem = Button(image=ar_up, width=60, relief = FLAT, fg='#800000', activeforeground='#800000', command=lambda pos=c+1: value_up(pos))
            #elem.bind('<Button-1>', lambda event, pos=c + 1: value_up(event, pos))
        elif r==4:
            elem = Button(image=ar_down, width=60, relief = FLAT, fg='#800000', activeforeground='#800000', command=lambda pos=c+1: value_down(pos))
            #elem.bind('<Button-1>', lambda event, pos=c+1: value_down(event, pos))
        elif r==3:
            elem = Label(text=f'#{c+1}')
            params = {'ipadx': 10, 'ipady': 1, 'padx': 1, 'pady': 1}
        elif r==2:
            elem = Label(width=3, text='0', font="Arial 18", fg='#006400', justify = CENTER, relief = GROOVE)

            params = {'ipadx': 1, 'ipady': 3, 'padx': 1, 'pady': 1}
        elem.grid(row=r, column=c, **params)

steps = Label(text=f"Шагов: {cur_numb.step}", font="Arial 14")
params = {'ipadx': 5, 'ipady': 5, 'padx': 5, 'pady': 5}
steps.grid(row=5, column=0, **params)

root.mainloop()