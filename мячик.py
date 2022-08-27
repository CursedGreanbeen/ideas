from tkinter import *


root = Tk()
c = Canvas(width=300, height=300,
           bg='white')
c.focus_set()
c.pack()

ball = c.create_oval(140, 140, 160, 160,
                     fill='green')
c.bind('<Up>',
       lambda event: c.move(ball, 0, -4) if c.coords(ball)[1] >= 4 else False)
c.bind('<Down>',
       lambda event: c.move(ball, 0, 4) if c.coords(ball)[3] <= 300 else False)
c.bind('<Left>',
       lambda event: c.move(ball, -4, 0) if c.coords(ball)[0] >= 4 else False)
c.bind('<Right>',
       lambda event: c.move(ball, 4, 0) if c.coords(ball)[2] <= 300 else False)



root.mainloop()