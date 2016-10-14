from Tkinter import *
import time
#Code for profiling
import cProfile, pstats, StringIO
pr = cProfile.Profile()
pr.enable()

#Main
root = Tk()
root.configure(bg="pink")
root.title("Pomodoro")
root.geometry("250x100")
tid = 0
onoff = True
vilotid = 300

class Pomodoro(Frame):
    """Create all objects"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Enter time:", bg="pink")
        self.inst_lbl.grid(row = 0, column = 0, sticky = NW)

        #Create entry
        self.tm_ent = Entry(self)
        self.tm_ent.grid(row = 0, column = 1, sticky = W)

        #Create Enter-button
        self.submit_btn = Button(self, text = "Submit", command = self.timer_set, bg="pink")
        self.submit_btn.grid(row = 1, column = 0)

        #Create Start-button
        self.start_btn = Button(self, text = "Start", command = self.timer_on, bg="pink")
        self.start_btn.grid(row = 1, column = 1, sticky = W)

        #Create Stop-button
        self.stop_btn = Button(self, text = "Stop", command = self.timer_off, bg="pink")
        self.stop_btn.grid(row = 1, column = 1)

        #Create Reset-button
        self.stop_btn = Button(self, text = "Reset", command = self.timer_reset, bg="pink")
        self.stop_btn.grid(row = 1, column = 1, sticky = E)

        #Create text widget to display timer
        self.timer_txt = Text(self, width = 20, height = 2, wrap = WORD)
        self.timer_txt.grid(row = 3, column = 0, columnspan = 3, sticky = W+E+N+S)

    def timer_set(self):
        global tid
        tid = self.tm_ent.get()
        self.timer_dsp()
        
    def timer_dsp(self):
        if tid>=1:
            timeContMin = int(tid) / 60
            timeContSec = int(tid) % 60
            self.timer_txt.delete(0.0, END)
            self.timer_txt.insert(0.0, "            Arbete")
            self.timer_txt.insert(0.0, "Minutes: " + str(timeContMin) + " Seconds: " + str(timeContSec))
            root.update()
        else:
            vilotimeContMin = int(vilotid) / 60
            vilotimeContSec = int(vilotid) % 60
            self.timer_txt.delete(0.0, END)
            self.timer_txt.insert(0.0, "       Vilodags")
            self.timer_txt.insert(0.0, "Minutes: " + str(vilotimeContMin) + " Seconds: " + str(vilotimeContSec))
            root.update()
            
    def timer_update(self):
        global tid
        global vilotid
        while onoff and tid >= 1:
            tid = int(tid) - 1
            time.sleep(1)
            self.timer_dsp()
        while onoff and tid <= 1:
            vilotid = int(vilotid) - 1
            time.sleep(1)
            self.timer_dsp()
            
    def timer_on(self):
        global onoff
        onoff = True
        self.timer_update()

    def timer_off(self):
        global onoff
        onoff= False
        self.timer_update()

    def timer_reset(self):
        global tid
        tid = 0
        self.timer_dsp()
        

app = Pomodoro(root)
root.mainloop()

# Profiling
pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()
