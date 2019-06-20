import turtle
import pickle
from tkinter import filedialog
from tkinter import Tk

class Avi:
    def __init__(self, descriptionlist):
        self.dlist = descriptionlist.copy()

    def render(self):
        turtle.tracer(0, 0)
        self.face = turtle.Turtle()
        self.face.shape("circle")
        if self.dlist["face size"] == "med":
            self.face.shapesize(5,4,0)
        self.face.penup()
        self.face.right(90)
        self.face.backward(240)
        self.face.left(90)

        self.lefteye = turtle.Turtle()
        self.lefteye.shape("circle")
        self.lefteye.shapesize(1,0.5,0)
        self.lefteye.penup()
        self.lefteye.right(90)
        self.lefteye.backward(260)
        self.lefteye.left(90)
        self.lefteye.backward(20)

        self.righteye = turtle.Turtle()
        self.righteye.shape("circle")
        self.righteye.shapesize(1, 0.5, 0)
        self.righteye.penup()
        self.righteye.right(90)
        self.righteye.backward(260)
        self.righteye.left(90)
        self.righteye.forward(20)

        self.lefteyei = turtle.Turtle()
        self.lefteyei.shape("circle")
        self.lefteyei.color(self.dlist["eye color"])
        self.lefteyei.shapesize(0.5, 0.25, 0)
        self.lefteyei.penup()
        self.lefteyei.right(90)
        self.lefteyei.backward(260)
        self.lefteyei.left(90)
        self.lefteyei.backward(20)

        self.righteyei = turtle.Turtle()
        self.righteyei.shape("circle")
        self.righteyei.color(self.dlist["eye color"])
        self.righteyei.shapesize(0.5, 0.25, 0)
        self.righteyei.penup()
        self.righteyei.right(90)
        self.righteyei.backward(260)
        self.righteyei.left(90)
        self.righteyei.forward(20)

        self.smile1 = turtle.Turtle()
        self.smile1.shape("square")
        self.smile1.color(self.dlist["lip color"])
        self.smile1.shapesize(0.25,2,0)
        self.smile1.penup()
        self.smile1.right(90)
        self.smile1.backward(210)
        self.smile1.left(90)

        self.nose = turtle.Turtle()
        self.nose.shape("square")
        self.nose.color("wheat")
        self.nose.shapesize(1,0.30,0)
        self.nose.penup()
        self.nose.right(90)
        self.nose.backward(235)
        self.nose.left(90)

        if self.dlist["hair type"] == "mohawk":
            self.mohawk = turtle.Turtle()
            self.mohawk.shape("triangle")
            self.mohawk.color(self.dlist["hair color"])
            self.mohawk.penup()
            self.mohawk.left(90)
            self.mohawk.forward(285)

        if self.dlist["hair type"] == "dmohawk":
            self.dmohawk = turtle.Turtle()
            self.dmohawk.shape("triangle")
            self.dmohawk.color(self.dlist["hair color"])
            self.dmohawk.penup()
            self.dmohawk.left(90)
            self.dmohawk.forward(285)
            self.dmohawk.left(180)

        if self.dlist["hair type"] == "d":
            self.hd1 = turtle.Turtle()
            self.hd1.shape("triangle")
            self.hd1.color(self.dlist["hair color"])
            self.hd1.penup()
            self.hd1.left(90)
            self.hd1.forward(285)
            self.hd1.left(180)

            self.hd2 = turtle.Turtle()
            self.hd2.shape("triangle")
            self.hd2.color(self.dlist["hair color"])
            self.hd2.penup()
            self.hd2.forward(20)
            self.hd2.left(90)
            self.hd2.forward(280)
            self.hd2.left(150)

            self.hd3 = turtle.Turtle()
            self.hd3.shape("triangle")
            self.hd3.color(self.dlist["hair color"])
            self.hd3.penup()
            self.hd3.backward(20)
            self.hd3.left(90)
            self.hd3.forward(280)
            self.hd3.left(210)

        self.body = turtle.Turtle()
        self.body.shape("circle")
        self.body.shapesize(15,7,0)
        self.body.color(self.dlist["body color"])
        self.body.penup()
        self.body.left(90)
        self.body.forward(30)
        self.body.right(90)

        # self.neck = turtle.Turtle()
        # self.neck.shape("square")
        # self.neck.shapesize(1, 1, 0)
        # self.neck.penup()
        # self.neck.right(90)
        # self.neck.backward(170)
        # self.neck.left(90)

        if (self.dlist["skin color"] == "tan"):
            self.face.fillcolor("tan")
            self.face.pencolor("tan")
            # self.neck.fillcolor("tan")
            # self.neck.pencolor("tan")
        elif (self.dlist["skin color"] == "brown"):
            self.face.fillcolor("saddle brown")
            self.face.pencolor("saddle brown")
            # self.neck.fillcolor("saddle brown")
            # self.neck.pencolor("saddle brown")

        turtle.update()
        turtle.getscreen()._root.mainloop()
        exit()






# #fdict = {"face size": "med", "skin color": "tan", "eye color": "red", "hair type": "d", "hair color": "sienna", "lip color" : "crimson"}
# Tk().withdraw()
# filename = filedialog.askopenfilename(filetypes = (("Avi Character Files ","*.chr"),("all files","*.*")))
# file = open(filename,"rb")
# fdict = pickle.load(file)
# file.close()
# x = Avi(fdict)
# x.render()


