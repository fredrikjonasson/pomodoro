from Tkinter import *
import time

#Main
root = Tk()
root.title("Pomodoro")
root.geometry("300x200")
tid = 0
onoff = True

class Pomodoro(Frame):
    """Create all objects"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Enter time: ")
        self.inst_lbl.grid(row = 0, column = 0, columnspan =2, sticky = W)

        #Create entry
        self.tm_ent = Entry(self)
        self.tm_ent.grid(row = 1, column = 1, sticky = W)

        #Create Enter-button
        self.submit_btn = Button(self, text = "Submit", command = self.timer_set)
        self.submit_btn.grid(row = 1, column = 0, sticky = W)

        #Create Start-button
        self.start_btn = Button(self, text = "Start", command = self.timer_on)
        self.start_btn.grid(row = 2, column = 0, sticky = W)

        #Create Stop-button
        self.stop_btn = Button(self, text = "Stop", command = self.timer_off)
        self.stop_btn.grid(row = 2, column = 1, sticky = W)

        #Create Reset-button
        self.stop_btn = Button(self, text = "Reset", command = self.timer_set)
        self.stop_btn.grid(row = 2, column = 2, sticky = W)

        #Create text widget to display timer
        self.timer_txt = Text(self, width = 35, height = 30, wrap = WORD)
        self.timer_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def timer_set(self):
        global tid
        tid = self.tm_ent.get()
        self.timer_dsp()
        
    def timer_dsp(self):
        timeContMin = int(tid) / 60
        timeContSec = int(tid) % 60
        self.timer_txt.delete(0.0, END)
        self.timer_txt.insert(0.0, "Minutes: " + str(timeContMin) + " Seconds: " + str(timeContSec))
        
    def timer_update(self):
        global tid
        while onoff:
            tid = int(tid) - 1
            time.sleep(1)
            self.timer_dsp()
            root.update()
            
    def timer_on(self):
        global onoff
        onoff = True
        self.timer_update()

    def timer_off(self):
        global onoff
        onoff= False
        self.timer_update()
        
       
app = Pomodoro(root)
root.mainloop()
