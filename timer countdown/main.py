import tkinter
from tkinter import *
from time import *
from datetime import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .5
SHORT_BREAK_MIN = .25
LONG_BREAK_MIN = 2
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


    # canvas.config


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = int(WORK_MIN * 60)  # I didn't mulitp
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = LONG_BREAK_MIN * 60
    # if reps = 1st, 3rd, 5th or 7th rep you work for 25 min
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(fg=RED, text="Long Break")
        # checkmark_count()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(fg=PINK, text="Short Break")
        print(2)
        # checkmark_count()
    else:
        count_down(work_sec)
        title_label.config(fg=GREEN, text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # green_check = ["✔"]
    new_row = 4
    count_minutes = math.floor(count / 60)  # determines the number of minutes and rounds it down
    count_seconds = count % 60  # uses the modulo operand to make sure
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    # elif reps == 8:
    #     count = 0

    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)

        # if reps % 2 == 0:
        #     checkmark_count()


# ---------------------------- UI SETUP ------------------------------- #
green_check = "✔"
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# my code
# def checkmark_count():
#     global green_check
# green_check += "✔"
check_marks = Label(bg=YELLOW)
check_marks.grid(column=1, row=3)

title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW,
                    fg=GREEN)  # prints the timer label on the screen
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0,
                      command=start_timer)  # creates a click button that calls the button_clicked function
start_button.config(width=5)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0,
                      command=reset_timer)  # creates a click button that calls the button_clicked function
reset_button.config(width=5)
reset_button.grid(column=2, row=2)

window.mainloop()

# if reps == 1 or reps == 3 or reps == 5 or reps == 7:
#     count_down(work_sec)

# if reps = 2nd, 4th, 6th you do 5 min break /SHORT_BREAK
# elif reps == 2 or reps == 4 or reps == 6:
#     count_down(short_break_sec)

# ON the 8th rep you do the Long Break
# elif reps == 8:
#     count_down(long_break_sec)

# count_down(short_break_sec)
# count_down(long_break_sec)
# count_down(5 * 60) #calls the count_down function and sends the number of seconds as an input
# converts the minutes to seconds.

# text="✔"
# chec = ""
