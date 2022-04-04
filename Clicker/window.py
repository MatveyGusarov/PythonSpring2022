from tkinter import *
from tkinter import messagebox
from child_window import ChildWindow
import random


class Window:
    left = 0
    bottom = 0

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

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Button(self.root, text="red", bg="red", width=20, command=lambda: self.change_color("red")).pack(anchor=E)
        Button(self.root, text="orange", bg="orange", width=20, command=lambda: self.change_color("orange")).pack(
            anchor=E)
        Button(self.root, text="yellow", bg="yellow", width=20, command=lambda: self.change_color("yellow")).pack(
            anchor=E)
        Button(self.root, text="green", bg="green", width=20, command=lambda: self.change_color("green")).pack(anchor=E)
        Button(self.root, text="Buy 1 click per second", width=20, command=self.purchase_notice).pack(anchor=E)
        Button(self.root, text="Quit", width=20, command=self.exit).pack(anchor=E)
        Button(self.root, text="Click Me!", bg="green", width=50, height=20, command=lambda: self.random_color("K")).pack()

    def purchase_notice(self):
        child = ChildWindow(self.root, 200, 200, "Child", self.left, self.bottom, (False, False))
        child.run("You buy 1 click per second!")

    def exit(self):
        choice = messagebox.askyesno("Quit", "Do you want to quit?")
        if choice:
            self.root.destroy()

    def random_color(self, event):
        rgb = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        color = "#%02x%02x%02x" % rgb
        self.change_color(color)

    def change_color(self, color):
        self.label.configure(text=color, fg=color)
        self.root.configure(bg=color)

    def create_child(self, width, height, title, left=0, bottom=0, resizeable=(False, False)):
        ChildWindow(self.root, width, height, title, left, bottom, resizeable)


if __name__ == "__main__":
    window = Window(800, 800, "Tkinter")
    window.create_child(400, 400, "Child")
    window.run()
