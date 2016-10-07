#THIS IS THE WINDOW

from Tkinter import *
import time

class Application(Frame):
    """Create all the objects"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Enter time: ")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        #Create entry
        self.tm_ent = Entry(self)
        self.tm_ent.grid(row = 1, column = 1, sticky = W)

        #Create Enter-button
        self.submit_btn = Button(self, text = "Submit", command = self.timer)
        self.submit_btn.grid(row = 1, column = 0, sticky = W)

        #Create text widget to display timer
        self.timer_txt = Text(self, width = 35, height = 30, wrap = WORD)
        self.timer_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def timer(self):
        """ Display message """
        timeCont = self.tm_ent.get()
        timeContMin = int(timeCont) / 60
        timeContSec = int(timeCont) % 60
        self.timer_txt.delete(0.0, END)
        self.timer_txt.insert(0.0, "Minutes: " + str(timeContMin) + " Seconds: " + str(timeContSec))



#main
root = Tk()
root.title("Pomodoro")
root.geometry("250x150")

app = Application(root)
root.mainloop()
