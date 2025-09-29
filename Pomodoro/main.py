import tkinter as tk
from tkinter import *
import time
import math

work = 25 * 60
rest = 5 * 60
longer_rest = 15 * 60

reps = 0
timer = None

# TIMER RESET------------------------------------------------------------------------------------------

def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

# COUNTDOWN-------------------------------------------------------------------------------------------

def start_timer():  
    global reps
    reps += 1
    time.sleep(1)
               
    if reps % 2 == 0:
        count_down(rest)
        title_label.config(text="Break", fg="white", font=("Lato", 24, "bold"), bg="black")
    elif reps % 4 == 0:
        count_down(longer_rest)
        title_label.config(text="Take a longer break.", fg="white", font=("Lato", 24, "bold"), bg="black")
    else: 
        count_down(work)
        title_label.config(text="Work", fg="white", font=("Lato", 24, "bold"), bg="black")

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

    if count_sec < 10:
        canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
    else:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

# UI---------------------------------------------------------------------------------------------

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="black")

title_label = Label(text="Timer", fg="white", font=("Lato", 24, "bold"), bg="black")
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg="black", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Lato", 24, "bold"))  
canvas.grid(column=1, row=1)

# BUTTONS-----------------------------------------------------------------------------------------

start_button = tk.Button(window, text="Start", command=start_timer)
start_button.grid(column=0, row=3)

reset_button = tk.Button(window, text="Reset", command=reset_timer)
reset_button.grid(column=2, row=3)


window.mainloop()


