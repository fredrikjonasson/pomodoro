# -*- coding: utf-8 -*-
import time

def main():
    focus_sec = int(input("Fokus i sekunder:"))
    focus_min = int(input("Fokus i minuter:"))

    break_sec = int(input("Vilopaus i sekunder:"))
    break_min = int(input("Vilopaus i minuter:"))

    n = int(input("Antal loopar:"))
    for i in range(n):
        focusTime(focus_sec, focus_min)
        breakTime(break_sec, break_min)
    
    
def formatTime(x):
    minutes=int(x/60)
    seconds_rem=int(x%60)
    if(seconds_rem<10):
        return(str(minutes) + ":0" + str(seconds_rem))
    else:
        return(str(minutes) + ":" + str(seconds_rem))

def focusTime(focus_sec, focus_min):
    focus_tot = focus_sec + (focus_min*60)
    
    for x in range(focus_tot, -1, -1):
        time.sleep(1)
        print(formatTime(x))
    print "NU VILAR DU!"

def breakTime(break_sec, break_min):
    break_tot = break_sec + (break_min*60)
    
    for x in range(break_tot, -1, -1):
        time.sleep(1)
        print(formatTime(x))
    print "NU ARBETAR DU IGEN1!"

main()
