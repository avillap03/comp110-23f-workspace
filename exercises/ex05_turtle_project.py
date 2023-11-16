"""Turtle Landscape Drawing - Mountain Sunset!"""

__author__ = "730621663"

from turtle import Turtle, colormode, done
from random import randint


def sky(a: float, b: float, x: float, y: float, z: float, chi: Turtle) -> None:
    """Function to draw the different layers of the sky."""
    chi.hideturtle
    chi.speed(20)
    colormode(255)
    chi.color(x, y, z)
    chi.pencolor(x, y, z)
    chi.penup()
    chi.goto(a, b)
    chi.pendown()    
    chi.begin_fill()
    idx: int = 0
    while idx < 4:
        width: int = 10000
        height: int = 75
        chi.forward(width if idx % 2 == 0 else height)
        chi.right(90)
        idx += 1
    chi.end_fill()


def sun(x: float, y: float, width: float, bel: Turtle) -> None:
    """Function to draw the sun using a circle."""
    bel.hideturtle() 
    bel.speed(20)
    colormode(255)
    bel.color(244, 210, 4)
    bel.pencolor(244, 210, 4)
    bel.penup()
    bel.goto(x, y)
    bel.pendown()    
    bel.begin_fill()
    idx: int = 0 
    while idx < 50:
        bel.forward(width)
        bel.left(7.2)
        x += width
        idx += 1
    bel.end_fill()


def mountains_1(x: float, y: float, width: float, mat: Turtle) -> None:
    """Function to draw first set of mountains using separate and different sized triangles."""
    mat.hideturtle()
    mat.speed(20) 
    colormode(255)
    mat.color(82, 101, 164)
    mat.pencolor(82, 101, 164)
    mat.penup()
    mat.goto(x, y)
    mat.pendown()    
    mat.begin_fill()
    idx: int = 0 
    while idx < 3:
        mat.forward(width)
        mat.left(120)
        x += width
        idx += 1
    mat.end_fill()


def mountains_2(x: float, y: float, width: float, mel: Turtle) -> None:
    """Function to draw a second set of mountains using separate and different sized triangles."""
    mel.hideturtle()
    mel.speed(20) 
    colormode(255)
    mel.color(47, 64, 121)
    mel.pencolor(47, 64, 121)
    mel.penup()
    mel.goto(x, y)
    mel.pendown()    
    mel.begin_fill()
    idx: int = 0 
    while idx < 3:
        mel.forward(width)
        mel.left(120)
        x += width
        idx += 1
    mel.end_fill()


def mountains_3(x: float, y: float, width: float, mic: Turtle) -> None:
    """Function to draw a third set of mountains using separate and different sized triangles."""
    mic.hideturtle()
    mic.speed(20) 
    colormode(255)
    mic.color(33, 45, 84)
    mic.pencolor(33, 45, 84)
    mic.penup()
    mic.goto(x, y)
    mic.pendown()    
    mic.begin_fill()
    idx: int = 0 
    while idx < 3:
        mic.forward(width)
        mic.left(120)
        x += width
        idx += 1
    mic.end_fill()


def birds(x: float, y: float, cam: Turtle) -> None:
    """Function to draw multiple birds at random positions using random from randint."""
    cam.hideturtle() 
    cam.speed(20)
    cam.pencolor("black") 
    cam.penup()
    cam.goto(x, y)
    cam.pendown()   
    cam.setheading(60)
    cam.circle(10, 180)
    cam.setheading(120)
    cam.circle(10, 180)


def ground(x: float, y: float, ele: Turtle) -> None: 
    """Function to draw the ground."""
    ele.hideturtle()
    ele.speed(20) 
    colormode(255)
    ele.color(215, 215, 109)
    ele.pencolor(215, 215, 109)
    ele.penup()
    ele.goto(x, y)
    ele.pendown()    
    ele.begin_fill()
    idx: int = 0 
    while idx < 4:
        width: int = 10000
        height: int = 200
        ele.forward(width if idx % 2 == 0 else height)
        ele.right(90)
        idx += 1
    ele.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    ele = Turtle()
    ground(-800, -200, ele)

    chi = Turtle()
    for i in range(7):
        y_coordinate = -53 + (i * 75)
        size = 179 - (i * 10)
        sky(-800, y_coordinate, 235, size, 40, chi)
    
    bel = Turtle()
    sun(-280, -100, 20, bel)

    mat = Turtle()
    x_coordinates = [-720, -450, -200, 75, 350]
    sizes = [400, 320, 350, 300, 220]
    for i in range(5):
        mountains_1(x_coordinates[i], -200, sizes[i], mat)

    mel = Turtle()
    x_coordinates = [-800, -350, -120, 490]
    sizes = [250, 270, 250, 340]
    for i in range(4):
        mountains_2(x_coordinates[i], -200, sizes[i], mel)

    mic = Turtle()
    x_coordinates = [-500, 30, 250]
    sizes = [200, 180, 210]
    for i in range(3):
        mountains_3(x_coordinates[i], -200, sizes[i], mic)

    cam = Turtle()
    idx: int = 0
    while idx < 10:
        birds(randint(-600, 600), randint(0, 325), cam)
        idx += 1

    done()
   

if __name__ == "__main__":
    main()
