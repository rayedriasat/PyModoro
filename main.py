from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
started = False
paused = False
current_sec = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps, started
    reps += 1
    check_marks.config(text="✔️" * (reps // 2))
    if started == True:
        return
    else:
        started = True
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)


def pause_timer():
    global paused, current_sec
    if not paused:
        pause_button.config(text="Play ▶️")
        print(f"{current_sec}")
        window.after_cancel(timer)
        paused = True
    else:
        pause_button.config(text="Pause ⏸️")
        paused = False
        countdown(current_sec)


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(clock_txt, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps, started
    started = False
    reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(sec):
    global current_sec, timer
    current_sec = sec
    count_min = sec // 60
    count_sec = sec % 60
    canvas.itemconfig(clock_txt, text=f"{count_min:02}:{count_sec:02}")
    if sec > 0 and not paused:
        timer = window.after(1000, countdown, sec - 1)
    elif sec <= 0:
        global started
        started = False
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PyModoro")
window.config(padx=110, pady=80, bg=YELLOW)
canvas = Canvas(bg=YELLOW, width=200, height=244, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas.grid(row=1, column=1)
clock_txt = canvas.create_text(
    100, 132, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white"
)

title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(row=0, column=1)

start_button = Button(text="Start ⏳", command=start_timer, padx=10, pady=10)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset 🔃", command=reset_timer, padx=10, pady=10)
reset_button.grid(row=2, column=2)
pause_button = Button(text="Pause ⏸️", command=pause_timer, padx=10, pady=10)
pause_button.grid(row=2, column=1)

check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_marks.grid(row=3, column=1)


window.mainloop()
