#imports

from  tkinter import *

#screen build

screen = Tk()
screen.geometry("250x150")
screen.title("calendar")
screen.config(background = "tan1")

# defs

def showCal():
    new_screen = Tk()
    new_screen.geometry("250x150")
    new_screen.title("calendar")
    new_screen.config(background = "tan1")
    new_screen.mainloop()


#widgets

calendar = Label(screen,text = "CALENDAR",bg = "white", fg = "tan1", font = ("times",28,"bold"))
calendar.grid(row = 1, column = 1)

year = Label(screen,text = "YEAR",bg = "white", fg = "tan1", font = ("times",18,"bold"))
year.grid(row = 2, column = 1, pady = 20)

entry = Entry(screen)
entry.grid(row = 2,column = 2, pady = 20 )

show = Button(screen, text = "show", fg = "tan1", bg = "white", command = showCal)
show.grid(row = 2, column = 3, padx = 20)

#finish ups

screen.mainloop()