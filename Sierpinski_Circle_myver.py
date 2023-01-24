import math 
import turtle
import copy 
import random
import colorsys

def pos_init(lst):
    last_element = lst.pop()
    if last_element == 1:
        lst.insert(0, 1)
    elif last_element == 0:
        lst.insert(0, 0)
    return lst

def initialize_color_list():
    """
    Generates a list of 7 random colors in hexadecimal format, and ensures that the color is not repeated.
    Returns:
    list[str]: A list of 7 strings representing the hexadecimal values of the colors.
    """
    color_list = set()
    for i in range(7):
        # Generate random HSL values
        h, s, l = (random.random() for _ in range(3))
        # Convert HSL to RGB values
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        # Convert RGB values to hexadecimal format
        color = '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))
        # Add the colors to the list
        if color not in color_list:
            color_list.add(color)
    return list(color_list)    


def drawCircle(x, y, r, colour, myTurtle):
    myTurtle.penup()
    myTurtle.setpos(x, y)
    myTurtle.pendown()
    myTurtle.fillcolor(colour)
    myTurtle.begin_fill()
    myTurtle.circle(r)
    myTurtle.end_fill()


def sierpinski_circle(myTurtle, big_R, degree, points, circlePattern, color_list):
    drawCircle(points[0], points[1], big_R, color_list[degree % len(color_list)], myTurtle)
    small_R = big_R / (1 + math.sqrt(2))
    if degree > 0:
        quadrant = get_quad(points, small_R, big_R, circlePattern[degree % len(color_list)])
        for i in quadrant:
            drawCircle(quadrant[i][0], quadrant[i][1], small_R, color_list[degree % len(color_list)], myTurtle)
            sierpinski_circle(myTurtle, small_R, degree - 1, quadrant[i], circlePattern, color_list)


def get_quad(points, small_R, big_R, myQueue): 
    x, y = points[0], points[1]
    quadrants_coordinates = {
        "I": [x + small_R, y + big_R],
        "II": [x + small_R, y + big_R - (2 * small_R)], 
        "III": [x - small_R, y + big_R - (2 * small_R)], 
        "IV": [x - small_R, y + big_R]
    }
    quadrants_to_remove = [quadrant for quadrant, value in quadrants_coordinates.items() if myQueue[list("I II III IV".split()).index(quadrant)] == 0]
    for quadrant in quadrants_to_remove:
        del quadrants_coordinates[quadrant]

    return quadrants_coordinates


def patternGen(degree, myQueue):
    pattern = {degree: myQueue}
    for i in range(degree - 1, 0, -1):
        pattern[i] = pos_init(copy.deepcopy(pattern[i + 1])) # create a new copy of the list
    return pattern


def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myTurtle.speed(0)

    degree = 3
    big_R = 170
    point = [0, 0]
    myQueue = [1, 1, 0, 1]
    color_list = initialize_color_list()

    circlePattern = patternGen(degree, myQueue)

    sierpinski_circle(myTurtle, big_R, degree, point, circlePattern, color_list)

    myTurtle.hideturtle()
    myWin.exitonclick()
  

main()