from tkinter import *
import tkinter


class ChildWindow:
    text = ""
    parent = tkinter.Tk

    def __init__(self, parent, width, height, title, left=0, bottom=0, resizeable=(False, False), text=""):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+{left}+{bottom}")
        self.root.resizable(resizeable[0], resizeable[1])
        self.text = text

    def run(self, text):
        self.draw(text)

    def draw(self, text):
        Label(self.root, text=text, justify=LEFT).grid(row=0, column=0, sticky=W)
