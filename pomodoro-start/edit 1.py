import time
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None
work = True





# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global work
    work = True
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="You Got This!", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0



def skip():
    global work
    global reps
    work = True
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="Skipped", font=(FONT_NAME, 30, "bold"))
    marks = ""

    if reps % 2 != 0:
        work_sessions = math.floor(reps / 2 + 1)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
        if reps % 8 == 0:
            reps = 0
            check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global work
    if work:
        work = False
        global reps
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break_sec)
            title_label.config(text="Break", fg=RED)
            reps = 0
            check_marks.config(text="")
        elif reps % 2 == 0:
            count_down(short_break_sec)
            title_label.config(text="Break", fg=PINK)
        else:
            count_down(work_sec)
            title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global work
        work = True
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Study Program")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="You Got This!", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=2)

skip_button = Button(text="Skip", highlightthickness=0, command=skip)
skip_button.grid(column=3, row=3)

check_marks = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

def function_call(event=None):
    for i in range(10):
        print('Hello', i)
        # wait for pause_var to be updated
        window.wait_variable(pause_var)
    print('done')



window.mainloop()
