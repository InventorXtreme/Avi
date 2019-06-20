import tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import pickle
import turtle
import subprocess
from subprocess import call
import sys
from AviEditor import Avi
root = tk.Tk()
root.title="main"

# x = tk.Label(root, text = "hey")
# x.pack()

filename = filedialog.askopenfilename(filetypes = (("Avi Character Files ","*.chr"),("all files","*.*")))
file = open(filename,"rb")
fdicte = pickle.load(file)
file.close()
labels = []
entrys = []
for key in fdicte.keys():
    labels.append(tk.Label(root, text = key))
    entrys.append(tk.Entry(root))


i = 0
keylist = fdicte.keys()
while(i < len(labels)):
    labels[i].pack()
    entrys[i].pack()
    i += 1

listcount = 0
for key in fdicte.keys():
    entrys[listcount].insert(0,fdicte[key])
    listcount += 1


def fetch():
    global filename
    fnum = 0
    for key in fdicte.keys():
        fdicte[key] = entrys[fnum].get()
        fnum +=1
        print(fdicte)

    file = open(filename, "wb")
    pickle.dump(fdicte,file)
    file.close()

def render():
    global renderbut
    try:
        renderbut.config(text="Exit")
        #exec(open("AviEditor.py").read())
        why = Avi(fdicte)
        why.render()
    except:
        pass
        sys.exit(0)



run = tk.Button(root, text="Save", command=fetch)
run.pack()
renderbut = tk.Button(root,text="Render/Exit",command=render)
renderbut.pack()


root.mainloop()