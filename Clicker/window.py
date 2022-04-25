import pyautogui
from tkinter import *
from tkinter import messagebox
from child_window import ChildWindow
import random
import threading
import time

based_clicks = 0


def click():
    while 0 == 0:
        start = time.time()
        for i in range(0, based_clicks):
            pyautogui.press('space')

        end = time.time()
        if end - start < 1:
            time.sleep(1 - (end - start))


thr1 = threading.Thread(target=click, daemon=True)
thr1.start()


class Window:
    left = 0
    bottom = 0
    counter = 0
    message = ""
    color = 0

    def __init__(self, width, height, title, left=0, bottom=0, resizeable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+{left}+{bottom}")
        self.root.resizable(resizeable[0], resizeable[1])
        self.label = Label(self.root, text="Label", bg='cyan', relief=RAISED, font="TimesNewRoman 17")
        self.left = left
        self.bottom = bottom
        self.change_color("yellow")
        self.root.bind('<KeyPress>', self.random_color)
        self.counter = 0
        self.message = "You have " + str(self.counter) + " points"
        self.label = Label(self.root, width=30, height=2, text="You have 0 points")
        self.color = 0

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.label.pack()
        Button(self.root, text="red", bg="red", width=20, command=lambda: self.change_color("red")).pack(anchor=E)
        Button(self.root, text="orange", bg="orange", width=20, command=lambda: self.change_color("orange")).pack(
            anchor=E)
        Button(self.root, text="yellow", bg="yellow", width=20, command=lambda: self.change_color("yellow")).pack(
            anchor=E)
        Button(self.root, text="green", bg="green", width=20,
               command=lambda: self.change_color("green")).pack(anchor=E)
        Button(self.root, text="Buy 1 click per\n second for 100 points", width=20, height=4,
               command=self.purchase_notice).pack(anchor=E)
        Button(self.root, text="Quit", width=20, command=self.exit).pack(anchor=E)
        Button(self.root, text="Click Me!", bg="green", width=50, height=20,
               command=lambda: self.random_color("K")).pack()

    def purchase_notice(self):
        if self.counter >= 10:
            self.counter -= 10
            self.message = "You have " + str(self.counter) + " points"
            self.label.configure(text=self.message, fg=str(self.color))
            global based_clicks
            based_clicks += 1

    def exit(self):
        choice = messagebox.askyesno("Quit", "Do you want to quit?")
        if choice:
            self.root.destroy()

    def random_color(self, event):
        rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color = "#%02x%02x%02x" % rgb
        self.change_color(self.color)

    def change_color(self, color):
        self.color = color
        self.counter += 1
        self.message = "You have " + str(self.counter) + " points"
        self.label.configure(text=self.message, fg=self.color)
        self.root.configure(bg=self.color)

    def create_child(self, width, height, title, left=0, bottom=0, resizeable=(False, False)):
        ChildWindow(self.root, width, height, title, left, bottom, resizeable)


if __name__ == "__main__":
    window = Window(800, 800, "Tkinter")
    window.create_child(400, 400, "Child")
    window.run()
