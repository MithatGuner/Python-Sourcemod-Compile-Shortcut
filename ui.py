#!/usr/bin/env python
# coding=utf-8

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
    import Tkinter, Tkconstants, tkFileDialog
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    import tkinter, Tkconstants, tkFileDialog
import os
import commands
from ayar import *



root = Tk()
root.title("Pluginler.com Eklenti Derle")
root.geometry("190x100")

def dialog():
    root.filename = tkFileDialog.askopenfilename(initialdir = "/home/satan/Masaüstü/Sourcemod/addons/sourcemod/scripting/",title = "Dosya Seç",filetypes = (("Sourcemod Script","*.sp"),("Tüm Dosyalar","*.*")))
    dosya = (root.filename)
    veri = os.path.split(dosya)[1]
    yazi = commands.getstatusoutput(scriptdizin +'; ./compile.sh ' + str(veri))
    print("*"*80)
    print(str(yazi))
    print("*"*80)

etiket = Label(root,text="Pluginler.com")
etiket.grid(padx=1, pady=10)
button1 = Button(root, text = " Eklenti Seç " , width=20, command=dialog)
button1.grid(padx=1, pady=20)


root.mainloop()
