from tkinter import *
import random as r

def closet():
    closets = ['- Выдвигающийся', '- Шкаф для денег', '- Полка', '- С дверцей', '- Просто шкаф', '- Книжный шкаф', '- Купе', '- Навесной', '- Шкаф для скелетов', '- Комод']
    res = closets[r.randint(0, 9)]
    answer.config(text=res)

root = Tk()
root.title('Какой ты шкаф сегодня?')
root.geometry('400x400')

headline = Label(text='Какой ты шкаф сегодня?', justify=CENTER, font='Courier 14')
answer = Label(text=' ', justify=CENTER, font='Courier 14')
butt = Button(text='Узнать', font='Courier 14', background="#333", foreground="#eee", activebackground="#eee", activeforeground="#333", padx="40", pady="15", command=closet)

headline.place(relx=.2, rely=.1)
answer.place(relx=.2, rely=.2)
butt.place(relx=.5, rely=.5, anchor="c", height=50, width=130, bordermode=OUTSIDE)

root.mainloop()