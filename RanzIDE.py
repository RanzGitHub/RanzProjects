from tkinter import *
IDE = Tk()
IDE.title("RanzIDE")
def run():
    code = editor.get("1.0", END)
    exec(code)
menu_bar = Menu(IDE)
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)
IDE.config(menu=menu_bar)
editor = Text()
editor.pack()
IDE.mainloop()