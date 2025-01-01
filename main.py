import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_GREEN='#82c997'
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps=0
timer=None
timer_running=False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps, timer_running
    reps=0
    timer_running=False
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    tick.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, timer_running

    if not timer_running:
        timer_running=True
        reps+=1
        work_sec=WORK_MIN*60
        short_break_sec=SHORT_BREAK_MIN*60
        long_break_sec=LONG_BREAK_MIN*60
        work_done=math.floor(reps/2)
        marks=''
        for _ in range(work_done):
            marks+='✓'

        if reps%8==0:
            title_label.config(text='Break',fg=RED)
            count_down(long_break_sec)
            reset_timer()
        elif reps%2==0:
            title_label.config(text='Break', fg=PINK)
            count_down(short_break_sec)
        else:
            title_label.config(text='Work', fg=GREEN)
            count_down(work_sec)
        tick.config(text=marks)
    elif timer_running:
        pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count): 
    global timer_running
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<=9:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down, count-1)
    else:
        timer_running=False
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=40, bg=YELLOW)

tomato_img=tkinter.PhotoImage(file="./tomato.png")
canvas=tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112, image=tomato_img)
timer_text=canvas.create_text(100,140, text=f"{WORK_MIN}:00",fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1,row=1)

title_label=tkinter.Label(text="Timer", font=(FONT_NAME,45,'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

start_button=tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button=tkinter.Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

tick=tkinter.Label(text='', fg=DARK_GREEN, bg=YELLOW, font=(FONT_NAME, 15, 'bold'))
tick.grid(column=1, row=3)
window.mainloop()